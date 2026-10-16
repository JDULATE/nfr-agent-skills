"""Grade supplied routing answers; never generate or solicit routing choices.

Give a blinded router only evals/routing-catalog.md and routing-prompts.json.
Keep routing-key.json and the original labeled evals out of its context.
Collect a JSON array of {"id": "opaque prompt id", "choice": "slug or ask"}.
Additional result fields are ignored for scoring. A supplied runner_up is
retained only as a diagnostic beside a miss; it never earns credit.
Then run: python scripts/score_routing.py results.json

Choices must be exact canonical slugs or "ask". Missing answers count as misses
against the complete key; duplicate and unknown ids are input errors. Accuracy
is reported separately for held-out cases and the rest, as well as overall
explicit, vague, and user_voice groups. Optional held_out key fields must be
booleans; absent means false. Held-out cases also report acceptable_choice,
acceptable_ask, or wrong. A successful exit means valid grading inputs, not
that the routing answers passed a threshold.
"""

import argparse
import json
from pathlib import Path
import sys


GROUPS = ("explicit", "vague", "user_voice")
DEFAULT_KEY = Path(__file__).resolve().parents[1] / "evals" / "routing-key.json"


def record_id(row, label):
    if not isinstance(row, dict):
        raise ValueError(f"{label}: expected an object")
    value = row.get("id")
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError(f"{label}: id must be a nonempty string without outer whitespace")
    return value


def score(results, key):
    """Return group totals and every miss, without writing files or routing prompts."""
    if not isinstance(key, list) or not key:
        raise ValueError("Key must be a nonempty JSON array")
    expected = {}
    for index, row in enumerate(key, 1):
        label = f"key[{index}]"
        case_id = record_id(row, label)
        if set(row) not in ({"id", "group", "expected"},
                            {"id", "group", "expected", "held_out"}):
            raise ValueError(f"{label}: expected id, group, expected, and optional held_out fields only")
        held_out = row.get("held_out", False)
        if not isinstance(held_out, bool):
            raise ValueError(f"{label}: held_out must be a boolean")
        if case_id in expected:
            raise ValueError(f"{label}: duplicate id {case_id}")
        group = row["group"]
        if group not in GROUPS:
            raise ValueError(f"{label}: invalid group")
        choices = row["expected"]
        if isinstance(choices, str):
            choices = [choices]
        if (not isinstance(choices, list) or not choices
                or any(not isinstance(c, str) or not c.strip() or c != c.strip() for c in choices)):
            raise ValueError(f"{label}: expected must be a choice or nonempty list of choices")
        if len(set(choices)) != len(choices):
            raise ValueError(f"{label}: duplicate acceptable choice")
        if group == "vague" and choices != ["ask"]:
            raise ValueError(f"{label}: vague prompts must expect ask only")
        if group == "explicit" and "ask" in choices:
            raise ValueError(f"{label}: explicit prompts must expect a skill")
        expected[case_id] = (group, choices, held_out)

    if not isinstance(results, list):
        raise ValueError("Results must be a JSON array of id/choice objects")
    answers = {}
    runner_ups = {}
    for index, row in enumerate(results, 1):
        label = f"results[{index}]"
        case_id = record_id(row, label)
        if not {"id", "choice"}.issubset(row):
            raise ValueError(f"{label}: required id and choice fields are missing")
        if case_id not in expected:
            raise ValueError(f"{label}: unknown id {case_id}")
        if case_id in answers:
            raise ValueError(f"{label}: duplicate id {case_id}")
        choice = row["choice"]
        if not isinstance(choice, str) or not choice.strip() or choice != choice.strip():
            raise ValueError(f"{label}: choice must be a nonempty string without outer whitespace")
        answers[case_id] = choice
        if "runner_up" in row:
            runner_ups[case_id] = row["runner_up"]

    groups = {group: {"correct": 0, "total": 0, "answered": 0, "missing": 0}
              for group in GROUPS}
    cohorts = {name: {"correct": 0, "total": 0, "answered": 0, "missing": 0}
               for name in ("held_out", "rest")}
    held_out_cases = []
    misses = []
    for case_id, (group, choices, held_out) in expected.items():
        choice = answers.get(case_id)
        correct = choice in choices
        outcome = ("acceptable_ask" if choice == "ask" else "acceptable_choice") if correct else "wrong"
        for stats in (groups[group], cohorts["held_out" if held_out else "rest"]):
            stats["total"] += 1
            stats["answered"] += choice is not None
            stats["missing"] += choice is None
            stats["correct"] += correct
        if held_out:
            held_out_cases.append({"id": case_id, "group": group, "choice": choice,
                                   "expected": choices, "outcome": outcome,
                                   "choice_in_acceptable_set": correct})
        if not correct:
            misses.append({"id": case_id, "group": group, "choice": choice,
                           "expected": choices, "held_out": held_out, "outcome": outcome,
                           "reason": "missing" if choice is None else "incorrect"})
            if case_id in runner_ups:
                misses[-1]["runner_up"] = runner_ups[case_id]
    for stats in (*groups.values(), *cohorts.values()):
        stats["accuracy"] = stats["correct"] / stats["total"] if stats["total"] else None
    return {"groups": groups, "cohorts": cohorts,
            "held_out_cases": held_out_cases, "misses": misses}


def print_report(report):
    for cohort, stats in report["cohorts"].items():
        accuracy = "n/a" if stats["accuracy"] is None else f"{stats['accuracy']:.2%}"
        print(f"{cohort}: {stats['correct']}/{stats['total']} ({accuracy}); "
              f"answered {stats['answered']}; missing {stats['missing']}")
    print("Overall groups (held-out and rest):")
    for group, stats in report["groups"].items():
        accuracy = "n/a" if stats["accuracy"] is None else f"{stats['accuracy']:.2%}"
        print(f"{group}: {stats['correct']}/{stats['total']} ({accuracy}); "
              f"answered {stats['answered']}; missing {stats['missing']}")
    for case in report["held_out_cases"]:
        choice = "<missing>" if case["choice"] is None else repr(case["choice"])
        print(f"HELD_OUT {case['id']}: {case['outcome']}; choice={choice}; "
              f"choice_in_acceptable_set={case['choice_in_acceptable_set']}; "
              f"expected={json.dumps(case['expected'])}")
    for miss in report["misses"]:
        choice = "<missing>" if miss["choice"] is None else repr(miss["choice"])
        runner_up = f"; runner_up={json.dumps(miss['runner_up'])}" if "runner_up" in miss else ""
        print(f"MISS {miss['id']} [{miss['group']}]: choice={choice}; "
              f"expected={json.dumps(miss['expected'])}; held_out={miss['held_out']}; "
              f"outcome={miss['outcome']}; reason={miss['reason']}{runner_up}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", type=Path, help="JSON array of id/choice objects")
    parser.add_argument("--key", type=Path, default=DEFAULT_KEY, help="Answer key (default: evals/routing-key.json)")
    parser.add_argument("--json", action="store_true", help="Print cohort/group metrics, held-out outcomes, and every miss as JSON")
    args = parser.parse_args(argv)
    try:
        results = json.loads(args.results.read_text(encoding="utf-8-sig"))
        key = json.loads(args.key.read_text(encoding="utf-8-sig"))
        report = score(results, key)
    except (OSError, ValueError, TypeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
