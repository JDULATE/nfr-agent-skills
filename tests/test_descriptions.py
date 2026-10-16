"""Synthetic routing fixtures test the heuristic, not NFR semantic correctness."""

import contextlib
import io
import json
from pathlib import Path
import shutil
import sys
import unittest
from unittest.mock import patch
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_descriptions as checker


class DescriptionTests(unittest.TestCase):
    def setUp(self):
        self.root = ROOT / (".foundation-test-descriptions-" + uuid.uuid4().hex)
        self.root.mkdir()
        self.addCleanup(self.cleanup)
        self.rows = json.loads((ROOT / "nfr-list.json").read_text(encoding="utf-8"))
        for row in self.rows:
            row["status"] = "draft" if row["id"] in (46, 47) else "todo"
        (self.root / "nfr-list.json").write_text(json.dumps(self.rows), encoding="utf-8")
        (self.root / "evals").mkdir()
        for number, word in ((46, "alpha"), (47, "beta")):
            row = self.rows[number - 1]
            path = checker.skill_path(self.root, row)
            path.parent.mkdir(parents=True)
            path.write_text(f"---\nname: {row['slug']}\ndescription: Routes {word} command results when requested.\n---\n", encoding="utf-8")
            peer = self.rows[47 - 1 if number == 46 else 46 - 1]["slug"]
            other_word = "beta" if word == "alpha" else "alpha"
            data = {"id": number, "slug": row["slug"],
                    "should_trigger": self.cases(word), "near_miss": self.cases(other_word, peer)}
            self.save(number, data)

    def cleanup(self):
        target = self.root.resolve()
        if target.parent != ROOT.resolve() or not target.name.startswith(".foundation-test-descriptions-"):
            raise ValueError("Refusing cleanup outside the test workspace")
        shutil.rmtree(target)

    @staticmethod
    def cases(word, sibling=None):
        result = []
        for index, noun in enumerate(("story", "item", "command", "result")):
            present = index >= 2
            case = {"prompt": f"{word} {noun}", "distinguishing_fact_present": present,
                    "expected_behavior": "route" if present else "clarify"}
            if not present:
                case["clarifying_question"] = "Which command/result contract applies?"
            if sibling:
                case["intended_sibling"] = sibling
            result.append(case)
        return result

    def path(self, number):
        row = self.rows[number - 1]
        return self.root / "evals" / f"{number:03}-{row['slug']}.json"

    def load(self, number):
        return json.loads(self.path(number).read_text(encoding="utf-8"))

    def save(self, number, data):
        self.path(number).write_text(json.dumps(data), encoding="utf-8")

    def test_tokenization_and_exact_jaccard(self):
        self.assertEqual(checker.keywords("The ALPHA-beta, alpha!"), {"alpha", "beta"})
        self.assertEqual(checker.keywords("a command and a result"), {"command", "result"})
        self.assertEqual(checker.overlap({"alpha", "beta"}, {"beta", "gamma"}), checker.Fraction(1, 3))
        self.assertEqual(checker.overlap(set(), set()), 0)
        self.assertNotEqual(checker.keywords("workers"), checker.keywords("worker"))

    def test_selector_competes_without_changing_nfr_coverage_contract(self):
        selector = {"id": 0, "name": "NFR Selector", "slug": "nfr-selector",
                    "aliases": [], "category": "Orchestration", "status": "draft"}
        (self.root / "selector.json").write_text(json.dumps(selector), encoding="utf-8")
        path = checker.skill_path(self.root, selector)
        path.parent.mkdir(parents=True)
        path.write_text('---\nname: nfr-selector\ndescription: Selects alpha beta concerns when asked for several qualities.\n---\n', encoding="utf-8")
        positives = self.cases("selection")
        for case in positives:
            case.update(distinguishing_fact_present=True, expected_behavior="route")
            case.pop("clarifying_question", None)
        data = {"id": 0, "slug": "nfr-selector", "should_trigger": positives,
                "near_miss": self.cases("alpha", "extendability")}
        (self.root / "evals/000-nfr-selector.json").write_text(json.dumps(data), encoding="utf-8")
        result = checker.check(self.root)
        self.assertIn("nfr-selector", result["candidate_pool"])
        self.assertEqual(result["selected_ids"], [0, 46, 47])
        self.assertEqual(checker.check(self.root, "0")["summary"]["eval_skills"], 1)

    def test_only_keeps_all_authored_competitors_and_is_read_only(self):
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result = checker.check(self.root, "46")
        self.assertEqual(result["selected_ids"], [46])
        self.assertEqual(result["candidate_pool"], ["extendability", "extensibility"])
        self.assertEqual(result["summary"]["prompts"], 8)
        self.assertEqual(result["summary"]["distinguishing_fact_omitted"], 4)
        self.assertEqual(result["summary"]["todo_excluded"], 112)
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.assertEqual(result, checker.check(self.root, "46"))

    def test_near_miss_outranks_named_sibling(self):
        data = self.load(46)
        data["near_miss"][2]["prompt"] = "alpha command alternative"
        self.save(46, data)
        result = checker.check(self.root, "46")
        case = next(c for c in result["cases"] if c["case_id"].endswith("near_miss[3]"))
        self.assertIn("near_target_outranks_sibling", case["flags"])
        self.assertGreater(case["target_score"], case["expected_score"])
        self.assertTrue(any("near_target_outranks_sibling" in p["counts"] for p in result["ambiguous_pairs"]))

    def test_positive_ties_are_preserved_and_zero_signal_is_not_a_winner(self):
        data = self.load(46)
        data["should_trigger"][0]["prompt"] = "command results"
        data["near_miss"][0]["prompt"] = "command result"
        data["near_miss"][1]["prompt"] = "unmatched vocabulary"
        self.save(46, data)
        result = checker.check(self.root, "46")
        tied = result["cases"][0]
        self.assertEqual(tied["top_candidates"], ["extendability", "extensibility"])
        self.assertIn("top_tie", tied["flags"])
        near_tied = result["cases"][4]
        self.assertIn("near_pair_tie", near_tied["flags"])
        empty = result["cases"][5]
        self.assertEqual(empty["top_candidates"], [])
        self.assertIn("no_keyword_signal", empty["flags"])
        self.assertIn("near_pair_no_signal", empty["flags"])

    def test_known_todo_sibling_is_unscored_not_fabricated(self):
        data = self.load(46)
        data["near_miss"][0]["intended_sibling"] = "portability"
        self.save(46, data)
        result = checker.check(self.root, "46")
        case = result["cases"][4]
        self.assertIsNone(case["expected_score"])
        self.assertIn("sibling_unavailable", case["flags"])
        self.assertNotIn("near_target_outranks_sibling", case["flags"])

    def test_only_rejects_invalid_unknown_and_todo_ids(self):
        for selection in ("bad", "46,", "999", "3"):
            with self.subTest(selection=selection), self.assertRaises(ValueError):
                checker.check(self.root, selection)

    def test_eval_identity_counts_duplicates_and_siblings_are_validated(self):
        original = self.load(46)
        for mutation in ("identity", "count", "duplicate", "unknown", "self", "boolean", "mode", "question"):
            with self.subTest(mutation=mutation):
                data = json.loads(json.dumps(original))
                if mutation == "identity":
                    data["id"] = 47
                elif mutation == "count":
                    data["near_miss"].pop()
                elif mutation == "duplicate":
                    data["near_miss"][0]["prompt"] = data["should_trigger"][0]["prompt"]
                elif mutation == "unknown":
                    data["near_miss"][0]["intended_sibling"] = "unknown-sibling"
                elif mutation == "self":
                    data["near_miss"][0]["intended_sibling"] = "extendability"
                elif mutation == "boolean":
                    data["should_trigger"][0]["distinguishing_fact_present"] = 0
                elif mutation == "mode":
                    data["should_trigger"][0]["expected_behavior"] = "route"
                elif mutation == "question":
                    del data["should_trigger"][0]["clarifying_question"]
                self.save(46, data)
                with self.assertRaises(ValueError):
                    checker.check(self.root, "46")
        self.save(46, original)

    def test_missing_eval_description_and_insufficient_vague_coverage_fail(self):
        data = self.load(46)
        self.path(46).unlink()
        with self.assertRaises(ValueError):
            checker.check(self.root, "46")
        self.save(46, data)
        data["should_trigger"][0]["distinguishing_fact_present"] = True
        data["should_trigger"][0]["expected_behavior"] = "route"
        self.save(46, data)
        self.assertEqual(checker.check(self.root, "46")["summary"]["distinguishing_fact_omitted"], 3)
        with self.assertRaisesRegex(ValueError, "At least half"):
            checker.check(self.root)
        data["should_trigger"][0]["distinguishing_fact_present"] = False
        data["should_trigger"][0]["expected_behavior"] = "clarify"
        self.save(46, data)
        path = checker.skill_path(self.root, self.rows[46])
        path.write_text("---\nname: extensibility\n---\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "description"):
            checker.check(self.root, "46")

    def test_cli_json_text_warnings_and_errors(self):
        data = self.load(46)
        data["near_miss"][2]["prompt"] = "alpha command alternative"
        self.save(46, data)
        real_check = checker.check
        with patch.object(checker, "check", side_effect=lambda only: real_check(self.root, only)):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(checker.main(["--only", "46", "--json"]), 0)
            self.assertEqual(json.loads(output.getvalue())["selected_ids"], [46])
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(checker.main(["--only", "46"]), 0)
            self.assertIn("Heuristic", output.getvalue())
            self.assertIn("NEAR-MISS", output.getvalue())
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(checker.main(["--only", "3"]), 2)


if __name__ == "__main__":
    unittest.main()
