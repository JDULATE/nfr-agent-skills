"""Build a deterministic category index from the catalogue."""

import argparse
from collections import defaultdict
from pathlib import Path

from _common import ROOT, load_skill_entries, skill_path


def build(root):
    groups = defaultdict(list)
    entries = load_skill_entries(root)
    for row in entries:
        groups[row["category"]].append(row)
    lines = ["# NFR skill index", "", "Generated from `nfr-list.json` and optional `selector.json`. Absent todo skills are pending authoring.", ""]
    for category, category_entries in sorted(groups.items()):
        lines.extend([f"## {category}", ""])
        for row in sorted(category_entries, key=lambda item: item["id"]):
            path = skill_path(root, row).relative_to(root).as_posix()
            lines.append(f"- [{row['id']:03d} {row['name']}]({path}) — {row['status']}")
        lines.append("")
    (root / "INDEX.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Built INDEX.md with {len(entries)} entries.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        build(args.root.resolve())
    except (ValueError, OSError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")


if __name__ == "__main__":
    main()
