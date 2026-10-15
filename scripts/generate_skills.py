"""Create missing todo stubs; never overwrite existing skill files."""

import argparse
import json
from pathlib import Path

from _common import ROOT, load_catalog, select_ids, skill_path


def generate(root, only=None, dry_run=False):
    entries = load_catalog(root)
    selected = select_ids(only, entries)
    template = (root / "templates" / "SKILL.template.md").read_text(encoding="utf-8")
    count = 0
    if not dry_run:
        (root / "skills").mkdir(exist_ok=True)
    for row in entries:
        if row["id"] not in selected or row["status"] != "todo":
            continue
        path = skill_path(root, row)
        if path.exists():
            continue
        count += 1
        if not dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            content = template.replace("<slug>", row["slug"]).replace("<NFR name>", row["name"])
            description = (
                f"Scaffolds the {row['name']} skill. Use when preparing its authoring; "
                "TODO: replace with scope, triggers, and a sibling exclusion."
            )
            lines = content.splitlines()
            lines[2] = "description: " + json.dumps(description, ensure_ascii=False)
            with path.open("x", encoding="utf-8", newline="\n") as stream:
                stream.write("\n".join(lines) + "\n")
    print(f"{'Would create' if dry_run else 'Created'} {count} todo skill stub(s); existing files preserved.")
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--only", help="Comma-separated catalogue ids")
    parser.add_argument("--dry-run", action="store_true", help="Preview without creating skills")
    args = parser.parse_args()
    try:
        generate(args.root.resolve(), args.only, args.dry_run)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")


if __name__ == "__main__":
    main()
