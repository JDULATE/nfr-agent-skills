"""Synthetic guards check scope preservation, equivalence, and safe previews."""

import contextlib
import io
from pathlib import Path
import shutil
import sys
import unittest
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import add_workflow_guards as guards


def fixture(specify="Record the agreed behavior.", design="Use the existing implementation."):
    return ("---\nname: fixture\ndescription: Preserved fixture description.\n---\n"
            "# Fixture\n\n## Workflow\n\n1. Clarify: Inspect the code.\n\n"
            f"2. Specify: {specify}\n\n3. Design/Implement: {design}\n\n"
            "4. Verify: Check results.\n\n5. Report: State limitations.\n\n"
            "## Specification patterns\n\nPreserve this section exactly.\n")


class WorkflowGuardTests(unittest.TestCase):
    def test_transform_preserves_surroundings_and_is_idempotent(self):
        original = fixture().replace("\n", "\r\n")
        updated, _ = guards.transform(original)
        self.assertEqual(original.split("## Workflow")[0], updated.split("## Workflow")[0])
        self.assertEqual(original.split("## Specification patterns")[1], updated.split("## Specification patterns")[1])
        self.assertIn(guards.normalized(guards.SPECIFY), guards.normalized(updated))
        self.assertIn(guards.normalized(guards.IMPLEMENT), guards.normalized(updated))
        self.assertEqual(guards.transform(updated)[0], updated)
        self.assertNotIn("\n", updated.replace("\r\n", ""))

    def test_equivalent_wording_is_skipped_per_step(self):
        specify = ("Show all assumptions and proposed defaults before implementation; "
                   "ask up to three questions; pause for the user's reply only if "
                   "a decision exceeds the minimum version.")
        design = ("Build only the smallest authorized version. Offer larger extensions "
                  "separately; obtain the user's yes before adding them.")
        original = fixture(specify, design)
        self.assertEqual(guards.transform(original)[0], original)
        partial = fixture("Ask at most three questions.", design)
        updated, changes = guards.transform(partial)
        self.assertNotEqual(partial, updated)
        self.assertEqual(changes, ["Specify=add", "Design/Implement=skip-equivalent"])

    def test_dry_run_and_invalid_plan_do_not_write(self):
        root = ROOT / (".foundation-test-workflow-" + uuid.uuid4().hex)
        root.mkdir()
        try:
            path = root / "skills/001-fixture/SKILL.md"
            path.parent.mkdir(parents=True)
            path.write_text(fixture(), encoding="utf-8")
            before = path.read_bytes()
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(guards.apply(root, dry_run=True), 1)
            self.assertEqual(path.read_bytes(), before)
            bad = root / "skills/002-bad/SKILL.md"
            bad.parent.mkdir()
            bad.write_text(fixture() + "\n" * 260, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "250"):
                guards.apply(root)
            self.assertEqual(path.read_bytes(), before)
        finally:
            target = root.resolve()
            if target.parent != ROOT.resolve() or not target.name.startswith(".foundation-test-workflow-"):
                raise ValueError("Refusing cleanup outside the fixture workspace")
            shutil.rmtree(target)


if __name__ == "__main__":
    unittest.main()
