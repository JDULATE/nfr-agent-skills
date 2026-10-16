"""Shared catalogue validation and string-frontmatter parsing; no dependencies."""

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = (
    "Definition and scope", "Use when / Don't use when", "Workflow",
    "Specification patterns", "Rules of thumb", "Verification",
    "Done checklist", "Failure modes", "References",
)


def slugify(name):
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def load_catalog(root):
    entries = json.loads((root / "nfr-list.json").read_text(encoding="utf-8"))
    if not isinstance(entries, list) or len(entries) != 114:
        raise ValueError("Catalogue must contain exactly 114 entries")
    ids, slugs = [], []
    for row in entries:
        if not isinstance(row, dict) or type(row.get("id")) is not int:
            raise ValueError("Each entry needs an integer id")
        for field in ("name", "slug", "category", "status"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f"Entry {row['id']}: missing string {field}")
        aliases = row["name"].split("/") if "/" in row["name"] else []
        if row.get("aliases") != aliases:
            raise ValueError(f"Entry {row['id']}: aliases must match slash variants")
        if row["slug"] != slugify(row["name"]):
            raise ValueError(f"Entry {row['id']}: slug does not match name")
        if row["status"] not in {"todo", "draft", "reviewed"}:
            raise ValueError(f"Entry {row['id']}: unknown status")
        ids.append(row["id"])
        slugs.append(row["slug"])
    if sorted(ids) != list(range(1, 115)) or len(set(slugs)) != 114:
        raise ValueError("Catalogue requires ids 1..114 and unique slugs")
    return entries


def select_ids(value, entries):
    if value is None:
        return {row["id"] for row in entries}
    if not re.fullmatch(r"\d+(?:,\d+)*", value):
        raise ValueError("--only requires comma-separated integer ids")
    selected = {int(item) for item in value.split(",")}
    if not selected <= {row["id"] for row in entries}:
        raise ValueError("--only contains an unknown id")
    return selected


def load_skill_entries(root):
    """Keep the 114-NFR catalogue intact; load the optional selector separately."""
    entries = load_catalog(root)
    manifest = root / "selector.json"
    if manifest.exists():
        selector = json.loads(manifest.read_text(encoding="utf-8"))
        required = {"id": 0, "name": "NFR Selector", "slug": "nfr-selector",
                    "aliases": [], "category": "Orchestration", "status": "draft"}
        if selector != required or type(selector.get("id")) is not int:
            raise ValueError("selector.json must describe the draft 000-nfr-selector")
        entries = [selector] + entries
    return entries


def skill_path(root, row):
    return root / "skills" / f"{row['id']:03d}-{row['slug']}" / "SKILL.md"


def frontmatter(text):
    """Parse a documented YAML subset; reject unsupported syntax explicitly."""
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("Missing frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("Unclosed frontmatter") from None
    fields, index = {}, 1
    while index < end:
        line = lines[index]
        index += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([a-zA-Z][\w-]*):\s*(.*)", line)
        if not match:
            raise ValueError("Unsupported frontmatter: use top-level string fields")
        key, value = match.groups()
        if key in fields:
            raise ValueError(f"Duplicate frontmatter key: {key}")
        if value in {">", ">-", ">+", "|", "|-", "|+"}:
            block = []
            while index < end and (not lines[index].strip() or lines[index][0].isspace()):
                block.append(lines[index].strip())
                index += 1
            fields[key] = (" " if value.startswith(">") else "\n").join(block).strip()
        elif value.startswith('"'):
            fields[key] = json.loads(value)
        elif value.startswith("'"):
            if not value.endswith("'") or len(value) < 2:
                raise ValueError("Unclosed single-quoted frontmatter")
            fields[key] = value[1:-1].replace("''", "'")
        else:
            if value.startswith(("[", "{", "&", "*", "!")) or ": " in value:
                raise ValueError("Unsupported YAML construct; quote this string")
            fields[key] = re.split(r"\s+#", value, maxsplit=1)[0].strip()
        if not isinstance(fields[key], str):
            raise ValueError(f"Frontmatter {key} must be a string")
    return fields, "".join(text.splitlines(keepends=True)[end + 1:])
