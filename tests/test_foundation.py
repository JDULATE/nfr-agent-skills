"""Synthetic content fixtures exercise tooling, never authored NFR content."""

import contextlib
import io
import json
import shutil
import subprocess
import sys
import unittest
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from _common import SECTIONS, frontmatter, load_catalog, skill_path
from build_index import build
from generate_skills import generate
from validate_skills import citations, five_grams, jaccard, validate


class FoundationTests(unittest.TestCase):
    def setUp(self):
        # Keep fixtures in the workspace. Default mkdir permissions also avoid
        # owner-only temp-directory ACLs incompatible with restricted Windows tokens.
        self.root = ROOT / (".foundation-test-" + uuid.uuid4().hex)
        self.root.mkdir()
        self.addCleanup(self.clean_fixture)
        shutil.copyfile(ROOT / "nfr-list.json", self.root / "nfr-list.json")
        shutil.copytree(ROOT / "templates", self.root / "templates")
        (self.root / "skills").mkdir()
        self.catalog = load_catalog(self.root)

    def clean_fixture(self):
        target = self.root.resolve()
        if target.parent != ROOT.resolve() or not target.name.startswith(".foundation-test-"):
            raise ValueError("Refusing to clean a path outside this test workspace")
        shutil.rmtree(target)

    def save_catalog(self):
        (self.root / "nfr-list.json").write_text(json.dumps(self.catalog), encoding="utf-8")

    def fixture(self, number=15):
        row = self.catalog[number - 1]
        description = "Checks synthetic fixture content when exercising the validation command and its error handling."
        # Unique tokens keep unrelated test fixtures below the duplication threshold.
        body = f"# {row['name']}\n\n" + "\n\n".join(
            f"## {section}\n\n" + " ".join(f"fixture{number}word{i}_{j}" for j in range(12))
            for i, section in enumerate(SECTIONS)
        )
        return f"---\nname: {row['slug']}\ndescription: {json.dumps(description)}\n---\n{body}\n"

    def write_skill(self, number=15, text=None):
        path = skill_path(self.root, self.catalog[number - 1])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text if text is not None else self.fixture(number), encoding="utf-8")
        return path

    def errors(self, only="15"):
        return validate(self.root, only)[0]

    def quiet_generate(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            return generate(self.root, **kwargs)

    def test_catalog_has_exact_count_range_and_unique_slugs(self):
        self.assertEqual(len(self.catalog), 114)
        self.assertEqual([row["id"] for row in self.catalog], list(range(1, 115)))
        self.assertEqual(len({row["slug"] for row in self.catalog}), 114)
        self.assertTrue(all(row["slug"].isascii() for row in self.catalog))
        self.assertEqual(self.catalog[0]["aliases"], ["Accessibility", "Access Control"])
        self.assertEqual(self.catalog[71]["slug"], "performance-efficiency-time-or-space-bounds")
        self.assertEqual(self.catalog[92]["aliases"], ["Standardizability", "Standardization", "Standard"])

    def test_catalog_rejects_duplicate_ids_slugs_and_wrong_count(self):
        original = json.loads(json.dumps(self.catalog))
        for mutation in ("id", "slug", "count"):
            with self.subTest(mutation=mutation):
                self.catalog = json.loads(json.dumps(original))
                if mutation == "count":
                    self.catalog.pop()
                elif mutation == "id":
                    self.catalog[1]["id"] = 1
                else:
                    self.catalog[1]["name"] = self.catalog[0]["name"]
                    self.catalog[1]["slug"] = self.catalog[0]["slug"]
                    self.catalog[1]["aliases"] = self.catalog[0]["aliases"]
                self.save_catalog()
                with self.assertRaises(ValueError):
                    load_catalog(self.root)

    def test_empty_scaffold_passes_but_selected_missing_file_fails(self):
        self.assertEqual(validate(self.root)[:3], ([], 0, 114))
        self.assertIn("Missing skill file", "\n".join(self.errors()))
        self.catalog[14]["status"] = "draft"
        self.save_catalog()
        self.assertIn("Missing skill file", "\n".join(self.errors(None)))

    def test_generator_dry_run_and_idempotency(self):
        self.assertEqual(self.quiet_generate(dry_run=True), 114)
        self.assertEqual(list((self.root / "skills").iterdir()), [])
        self.assertEqual(self.quiet_generate(), 114)
        paths = list((self.root / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(paths), 114)
        before = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths}
        self.assertEqual(self.quiet_generate(), 0)
        self.assertEqual(before, {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths})
        fields, _ = frontmatter(paths[0].read_text(encoding="utf-8"))
        self.assertEqual(fields["status"], "todo")
        self.assertIn("Unfinished content", "\n".join(self.errors()))

    def test_generator_preserves_both_catalog_and_file_status(self):
        path = self.write_skill(text=self.fixture().replace("---\n#", "status: draft\n---\n#"))
        original = path.read_bytes()
        self.catalog[74]["status"] = "draft"
        self.save_catalog()
        self.quiet_generate(only="15,75")
        self.assertEqual(path.read_bytes(), original)
        self.assertFalse(skill_path(self.root, self.catalog[74]).exists())

    def test_valid_fixture_and_frontmatter_variants(self):
        self.write_skill()
        self.assertEqual(self.errors(), [])
        original = self.fixture()
        for value in (
            "Checks synthetic fixture content when exercising the validator command and its checks.",
            "'Checks synthetic fixture content when exercising the validator command and its checks.'",
            ">-\n  Checks synthetic fixture content when exercising\n  the validator command and its checks.",
            "|-\n  Checks synthetic fixture content when exercising\n  the validator command and its checks.",
        ):
            with self.subTest(value=value):
                lines = original.splitlines()
                lines[2] = "description: " + value
                self.write_skill(text="\n".join(lines))
                self.assertEqual(self.errors(), [])

    def test_missing_frontmatter_name_description_and_trigger(self):
        original = self.fixture()
        cases = [
            (original.split("---\n", 2)[-1], "Missing frontmatter"),
            (original.replace("name: availability", "name: privacy"), "name must equal"),
            (original.replace(original.splitlines()[2], 'description: "Short when"'), "60..1024"),
            (original.replace(original.splitlines()[2], "description: " + "x" * 1025), "60..1024"),
            (original.replace(original.splitlines()[2], "description: " + "x" * 80), "word Use or when"),
            (original.replace("name: availability", "name: availability\nname: availability"), "Duplicate"),
        ]
        for content, expected in cases:
            with self.subTest(expected=expected):
                self.write_skill(text=content)
                self.assertIn(expected, "\n".join(self.errors()))

    def test_description_boundaries(self):
        for length in (60, 1024):
            with self.subTest(length=length):
                lines = self.fixture().splitlines()
                lines[2] = "description: Use " + "x" * (length - 4)
                self.write_skill(text="\n".join(lines))
                self.assertEqual(self.errors(), [])

    def test_missing_reordered_and_duplicate_sections(self):
        original = self.fixture()
        cases = [original.replace("## Verification", "## Other"),
                 original.replace("## Verification", "## Report").replace("## Failure modes", "## Verification"),
                 original + "\n## Verification\n"]
        for content in cases:
            with self.subTest(content=content[-30:]):
                self.write_skill(text=content)
                self.assertIn("sections", "\n".join(self.errors()))

    def test_body_line_limit_and_unfinished_tokens(self):
        original = self.fixture()
        _, body = frontmatter(original)
        self.write_skill(text=original + "\n" * (250 - len(body.splitlines())))
        self.assertEqual(self.errors(), [])
        self.write_skill(text=original + "\n" * (251 - len(body.splitlines())))
        self.assertIn("250 lines", "\n".join(self.errors()))
        for marker in ("TODO", "TBD", "lorem", "[citation needed]", "<metric>"):
            with self.subTest(marker=marker):
                self.write_skill(text=original + "\n" + marker)
                self.assertIn("Unfinished content", "\n".join(self.errors()))

    def test_citations_activate_with_allowlist_and_require_exact_matches(self):
        # Reserved-domain URLs here are synthetic parser fixtures, not references.
        allowed_url = "https://example.invalid/allowed"
        citations_text = f"ISO/IEC 25010; ISO/IEC/IEEE 29148; WCAG; OWASP ASVS; {allowed_url}"
        self.write_skill(text=self.fixture() + citations_text)
        self.assertEqual(self.errors(), [])  # No Phase 2 allowlist yet.
        refs = self.root / "references"
        refs.mkdir()
        (refs / "standards-allowlist.md").write_text(citations_text, encoding="utf-8")
        self.assertEqual(self.errors(), [])
        for invalid in ("ISO/IEC 25012", "WCAG 2.2", allowed_url + "/extra"):
            with self.subTest(invalid=invalid):
                self.write_skill(text=self.fixture() + invalid)
                self.assertIn("not in standards allowlist", "\n".join(self.errors()))
        urls, standards = citations(citations_text)
        self.assertEqual(urls, {allowed_url})
        self.assertIn("ISO/IEC/IEEE 29148", standards)

    def test_reference_existence_reference_style_and_one_level_depth(self):
        path = self.write_skill(text=self.fixture() + "\nRead when testing: [fixture](./references/check.md).\n")
        self.assertIn("Missing reference", "\n".join(self.errors()))
        refs = path.parent / "references"
        refs.mkdir()
        ref = refs / "check.md"
        ref.write_text("Synthetic parser fixture.\n", encoding="utf-8")
        self.assertEqual(self.errors(), [])
        ref.write_text("[next](next.md)\n", encoding="utf-8")
        errors = "\n".join(self.errors())
        self.assertIn("nest deeper", errors)
        self.assertIn("Missing reference", errors)
        self.write_skill(text=self.fixture() + "\n[fixture][check]\n\n[check]: ./references/absent.md\n")
        self.assertIn("Missing reference", "\n".join(self.errors()))

    def test_references_check_nested_directories_and_citations(self):
        path = self.write_skill(text=self.fixture() + "\n[fixture](references/check.md)\n")
        refs = path.parent / "references"
        (refs / "nested").mkdir(parents=True)
        (refs / "nested" / "check.md").write_text("Synthetic fixture.", encoding="utf-8")
        (refs / "check.md").write_text("ISO/IEC 25012", encoding="utf-8")
        global_refs = self.root / "references"
        global_refs.mkdir()
        (global_refs / "standards-allowlist.md").write_text("ISO/IEC 25010", encoding="utf-8")
        errors = "\n".join(self.errors())
        self.assertIn("Nested references", errors)
        self.assertIn("not in standards allowlist", errors)

    def test_cross_skill_copy_detection_in_batch(self):
        self.write_skill(15)
        duplicate = self.fixture().replace("name: availability", "name: privacy")
        self.write_skill(75, duplicate)
        errors = "\n".join(self.errors("75"))
        self.assertIn("015-availability / 075-privacy", errors)
        self.assertIn("Jaccard 1.000", errors)
        self.write_skill(75)
        self.assertEqual(self.errors("15,75"), [])
        self.assertEqual(jaccard(five_grams("a b c d e"), five_grams("a b c d f")), 0)
        self.assertEqual(jaccard(set(), set()), 0)

    def test_only_rejects_invalid_ids_and_unknown_skill_fails_full_run(self):
        for only in ("0", "115", "15,", "abc", ""):
            with self.subTest(only=only), self.assertRaises(ValueError):
                validate(self.root, only)
        path = self.root / "skills" / "999-unknown" / "SKILL.md"
        path.parent.mkdir()
        path.write_text(self.fixture(), encoding="utf-8")
        self.assertIn("Unknown skill", "\n".join(self.errors(None)))

    def test_index_grouping_status_links_and_determinism(self):
        self.catalog[14]["category"] = "Fixture group"
        self.catalog[14]["status"] = "draft"
        self.save_catalog()
        with contextlib.redirect_stdout(io.StringIO()):
            build(self.root)
            original = (self.root / "INDEX.md").read_bytes()
            build(self.root)
        self.assertEqual(original, (self.root / "INDEX.md").read_bytes())
        index = original.decode()
        self.assertIn("## Fixture group", index)
        self.assertIn("[015 Availability](skills/015-availability/SKILL.md) — draft", index)
        self.assertEqual(index.count("- ["), 114)

    def test_validator_cli_exit_codes(self):
        command = [sys.executable, str(ROOT / "scripts" / "validate_skills.py"), "--root", str(self.root)]
        passed = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(passed.returncode, 0, passed.stderr)
        failed = subprocess.run(command + ["--only", "15"], capture_output=True, text=True)
        self.assertEqual(failed.returncode, 1)
        self.assertIn("Missing skill file", failed.stdout)


if __name__ == "__main__":
    unittest.main()
