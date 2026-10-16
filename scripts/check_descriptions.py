"""Read-only lexical routing probes; warnings are not semantic routing verdicts."""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import re
import sys

from _common import ROOT, frontmatter, load_skill_entries, select_ids, skill_path


STOP_WORDS = frozenset("""a an and are as at be been but by can could do does for from has have how i if
in into is it its me my need not of on or our please see should so that the their
them these they this to us use using want was we were what when where which who
will with would you your asked say says users make help alone only without
""".split())


def keywords(text):
    """Lowercase word sets, hyphens split, no stemming or synonym expansion."""
    return {word for word in re.findall(r"[a-z][a-z0-9]*", text.lower())
            if word not in STOP_WORDS}


def overlap(left, right):
    """Exact set Jaccard; compare fractions before rounding for display."""
    union = left | right
    return Fraction(len(left & right), len(union)) if union else Fraction(0)


def load_eval(root, row, by_slug):
    path = root / "evals" / f"{row['id']:03}-{row['slug']}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ValueError(f"{path.name}: {error}") from error
    if not isinstance(data, dict) or type(data.get("id")) is not int:
        raise ValueError(f"{path.name}: expected object with integer id")
    if data["id"] != row["id"] or data.get("slug") != row["slug"]:
        raise ValueError(f"{path.name}: id/slug does not match catalogue")
    seen = set()
    for kind in ("should_trigger", "near_miss"):
        cases = data.get(kind)
        if not isinstance(cases, list) or len(cases) != 4:
            raise ValueError(f"{path.name}: {kind} requires exactly 4 prompts")
        for index, case in enumerate(cases, 1):
            label = f"{path.name}:{kind}[{index}]"
            if not isinstance(case, dict):
                raise ValueError(f"{label}: expected a prompt object")
            prompt = case.get("prompt")
            if not isinstance(prompt, str) or not prompt.strip():
                raise ValueError(f"{label}: empty prompt")
            normalized = " ".join(prompt.lower().split())
            if normalized in seen:
                raise ValueError(f"{label}: duplicate prompt within this eval")
            seen.add(normalized)
            present = case.get("distinguishing_fact_present")
            if type(present) is not bool:
                raise ValueError(f"{label}: distinguishing_fact_present must be boolean")
            expected = "route" if present else "clarify"
            if case.get("expected_behavior") != expected:
                raise ValueError(f"{label}: expected_behavior must be {expected}")
            if not present:
                question = case.get("clarifying_question")
                if not isinstance(question, str) or not question.strip():
                    raise ValueError(f"{label}: missing clarifying question")
            if kind == "near_miss":
                sibling = case.get("intended_sibling")
                if not isinstance(sibling, str) or sibling not in by_slug:
                    raise ValueError(f"{label}: unknown intended sibling")
                if sibling == row["slug"]:
                    raise ValueError(f"{label}: intended sibling cannot be this skill")
    return data


def check(root=ROOT, only=None):
    root = Path(root)
    catalogue = load_skill_entries(root)
    by_slug = {row["slug"]: row for row in catalogue}
    authored = [row for row in catalogue if row["status"] != "todo"]
    authored_ids = {row["id"] for row in authored}
    selected = authored_ids if only is None else select_ids(only, catalogue)
    if not selected <= authored_ids:
        missing = ",".join(map(str, sorted(selected - authored_ids)))
        raise ValueError(f"--only selects unauthored todo ids: {missing}")

    # --only selects evals, never a smaller competitor pool.
    descriptions = {}
    for row in authored:
        path = skill_path(root, row)
        try:
            fields, _ = frontmatter(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise ValueError(f"{path}: {error}") from error
        description = fields.get("description")
        if fields.get("name") != row["slug"] or not isinstance(description, str) or not description.strip():
            raise ValueError(f"{path}: missing/mismatched name or description")
        descriptions[row["slug"]] = keywords(description)

    records = []
    pairs = defaultdict(lambda: {"counts": Counter(), "case_ids": set()})
    flag_counts = Counter()
    omitted = 0
    for row in authored:
        if row["id"] not in selected:
            continue
        data = load_eval(root, row, by_slug)
        for kind in ("should_trigger", "near_miss"):
            for index, case in enumerate(data[kind], 1):
                prompt_words = keywords(case["prompt"])
                scores = {slug: overlap(prompt_words, words)
                          for slug, words in descriptions.items()}
                expected = row["slug"] if kind == "should_trigger" else case["intended_sibling"]
                expected_score = scores.get(expected)
                target_score = scores[row["slug"]]
                top_score = max(scores.values(), default=Fraction(0))
                top = sorted(slug for slug, score in scores.items()
                             if score == top_score and score > 0)
                flags = []
                case_id = f"{row['id']:03}-{row['slug']}:{kind}[{index}]"

                def pair_finding(left, right, finding):
                    if left != right:
                        entry = pairs[tuple(sorted((left, right)))]
                        entry["counts"][finding] += 1
                        entry["case_ids"].add(case_id)

                if not top:
                    flags.append("no_keyword_signal")
                if expected_score is None:
                    flags.append("sibling_unavailable")
                elif top and expected not in top:
                    flags.append("expected_not_top")
                    for winner in top:
                        pair_finding(expected, winner, "expected_not_top")
                if len(top) > 1:
                    flags.append("top_tie")
                    for left, right in combinations(top, 2):
                        pair_finding(left, right, "top_tie")
                if kind == "near_miss" and expected_score is not None:
                    if target_score > expected_score:
                        flags.append("near_target_outranks_sibling")
                        pair_finding(row["slug"], expected, "near_target_outranks_sibling")
                    elif target_score == expected_score:
                        finding = "near_pair_tie" if target_score > 0 else "near_pair_no_signal"
                        flags.append(finding)
                        pair_finding(row["slug"], expected, finding)
                flag_counts.update(flags)
                omitted += not case["distinguishing_fact_present"]
                records.append({
                    "case_id": case_id, "skill_id": row["id"], "skill_slug": row["slug"],
                    "kind": kind, "prompt": case["prompt"], "expected_slug": expected,
                    "distinguishing_fact_present": case["distinguishing_fact_present"],
                    "expected_behavior": case["expected_behavior"],
                    "clarifying_question": case.get("clarifying_question"),
                    "target_score": round(float(target_score), 6),
                    "expected_score": None if expected_score is None else round(float(expected_score), 6),
                    "top_score": round(float(top_score), 6), "top_candidates": top,
                    "shared_target_keywords": sorted(prompt_words & descriptions[row["slug"]]),
                    "shared_expected_keywords": None if expected_score is None else sorted(prompt_words & descriptions[expected]),
                    "flags": flags,
                })
    # Broad selection is itself a routing fact. Preserve the half-underspecified
    # coverage rule for the 114 NFRs without mislabeling selector positives vague.
    nfr_records = [case for case in records if case["skill_id"] != 0]
    nfr_omitted = sum(not case["distinguishing_fact_present"] for case in nfr_records)
    if only is None and nfr_records and nfr_omitted * 2 < len(nfr_records):
        raise ValueError("At least half of all authored prompts must omit the distinguishing fact")
    pair_results = [{"pair": list(pair), "counts": dict(sorted(entry["counts"].items())),
                     "case_ids": sorted(entry["case_ids"])} for pair, entry in pairs.items()]
    pair_results.sort(key=lambda entry: (-len(entry["case_ids"]), entry["pair"]))
    return {
        "method": "Jaccard of lowercase word sets after fixed stop words; no stemming, synonyms or negation handling",
        "label_policy": "Underspecified labels are provisional leads for clarification, not unconditional routing truths",
        "candidate_pool": [row["slug"] for row in authored],
        "selected_ids": sorted(selected),
        "summary": {"authored_skills": len(authored), "todo_excluded": len(catalogue) - len(authored),
                    "eval_skills": len(selected), "prompts": len(records),
                    "distinguishing_fact_omitted": omitted, "flags": dict(sorted(flag_counts.items())),
                    "ambiguous_pairs": len(pair_results)},
        "ambiguous_pairs": pair_results, "cases": records,
    }


def print_report(result):
    summary = result["summary"]
    print("Heuristic routing dry run; warnings are not proof or a pass/fail accuracy score.")
    print(f"Candidates: {summary['authored_skills']} authored; {summary['todo_excluded']} todo excluded.")
    print(f"Evaluated {summary['eval_skills']} skills / {summary['prompts']} prompts; "
          f"{summary['distinguishing_fact_omitted']} omit the distinguishing fact.")
    print("Flags: " + json.dumps(summary["flags"], sort_keys=True))
    for entry in result["ambiguous_pairs"]:
        print("PAIR " + " <> ".join(entry["pair"]) + ": " + json.dumps(entry["counts"], sort_keys=True))
        print("  " + "; ".join(entry["case_ids"]))
    for case in result["cases"]:
        if "near_target_outranks_sibling" in case["flags"]:
            print(f"NEAR-MISS {case['case_id']}: target {case['target_score']:.6f} > "
                  f"{case['expected_slug']} {case['expected_score']:.6f}; "
                  f"{case['expected_behavior']}: {case['prompt']}")
    for case in result["cases"]:
        if "sibling_unavailable" in case["flags"] or "no_keyword_signal" in case["flags"]:
            print(f"UNRESOLVED {case['case_id']}: {','.join(case['flags'])}; {case['prompt']}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", metavar="ID,ID,...", help="Select authored eval ids; keep all authored competitors")
    parser.add_argument("--json", action="store_true", help="Print all per-prompt scores, flags and ambiguous pairs as JSON")
    args = parser.parse_args(argv)
    try:
        result = check(only=args.only)
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, ensure_ascii=True, indent=2))
    else:
        print_report(result)
    # Successful evaluation can have many warnings; only invalid inputs fail.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
