"""Synthetic scorer checks; these do not run the prepared blinded routing test."""

import contextlib
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import score_routing as scorer


class RoutingScoreTests(unittest.TestCase):
    def setUp(self):
        self.key = [
            {"id": "x1", "group": "explicit", "expected": "alpha"},
            {"id": "x2", "group": "vague", "expected": "ask"},
            {"id": "x3", "group": "user_voice", "expected": ["alpha", "beta", "ask"]},
        ]

    def test_groups_acceptable_sets_and_exact_choices(self):
        for choice in ("alpha", "beta", "ask"):
            report = scorer.score([{"id": "x1", "choice": "alpha"},
                                   {"id": "x2", "choice": "ask"},
                                   {"id": "x3", "choice": choice}], self.key)
            self.assertEqual(report["misses"], [])
            self.assertTrue(all(s["accuracy"] == 1 for s in report["groups"].values()))
        report = scorer.score([{"id": "x1", "choice": "ask"},
                               {"id": "x2", "choice": "alpha"},
                               {"id": "x3", "choice": "unrecognized-choice"}], self.key)
        self.assertEqual(len(report["misses"]), 3)
        self.assertTrue(all(s["accuracy"] == 0 for s in report["groups"].values()))

    def test_missing_answers_are_misses_with_full_denominators(self):
        report = scorer.score([{"id": "x1", "choice": "alpha"}], self.key)
        self.assertEqual(len(report["misses"]), 2)
        self.assertTrue(all(m["reason"] == "missing" and m["choice"] is None
                            for m in report["misses"]))
        self.assertEqual(report["groups"]["vague"]["missing"], 1)
        self.assertEqual(report["groups"]["user_voice"]["total"], 1)
        self.assertEqual(len(scorer.score([], self.key)["misses"]), 3)

    def test_results_reject_duplicate_unknown_and_malformed_records(self):
        bad_results = [None, {}, [{"id": "absent", "choice": "alpha"}],
                       [{"id": "x1", "choice": "alpha"}] * 2,
                       [{"id": "x1", "choice": ["alpha"]}],
                       [{"id": "x1", "choice": " "}],
                       [{"id": "x1", "choice": "alpha", "expected": "alpha"}],
                       [{"id": 1, "choice": "alpha"}]]
        for results in bad_results:
            with self.subTest(results=results), self.assertRaises(ValueError):
                scorer.score(results, self.key)

    def test_key_rejects_conflicting_groups_and_invalid_choices(self):
        for changes in ({"group": "other"}, {"expected": []},
                        {"expected": ["alpha", "alpha"]}, {"expected": [False]},
                        {"expected": "ask"}, {"group": "vague", "expected": "alpha"}):
            key = copy.deepcopy(self.key)
            key[0].update(changes)
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                scorer.score([], key)
        for key in ([], {}, self.key + [self.key[0]]):
            with self.assertRaises(ValueError):
                scorer.score([], key)

    def test_empty_group_and_no_mutation(self):
        key = copy.deepcopy(self.key[:1])
        results = [{"id": "x1", "choice": "alpha"}]
        before = copy.deepcopy((key, results))
        report = scorer.score(results, key)
        self.assertIsNone(report["groups"]["vague"]["accuracy"])
        self.assertEqual((key, results), before)

    def test_cli_json_text_errors_and_read_only_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            key_path, results_path = root / "key.json", root / "results.json"
            key_path.write_text(json.dumps(self.key), encoding="utf-8")
            results_path.write_text('[{"id":"x2","choice":"wrong"}]', encoding="utf-8-sig")
            before = {p.name: p.read_bytes() for p in root.iterdir()}
            args = [str(results_path), "--key", str(key_path)]
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(scorer.main(args + ["--json"]), 0)
            self.assertEqual(len(json.loads(out.getvalue())["misses"]), 3)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(scorer.main(args), 0)
            self.assertEqual(out.getvalue().count("MISS "), 3)
            self.assertIn("user_voice:", out.getvalue())
            self.assertEqual({p.name: p.read_bytes() for p in root.iterdir()}, before)
            results_path.write_text('{', encoding="utf-8")
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(scorer.main(args), 2)


if __name__ == "__main__":
    unittest.main()
