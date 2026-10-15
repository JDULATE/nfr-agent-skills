"""Validate skill content, references, citations, and word-five-gram originality."""

import argparse
import itertools
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from _common import ROOT, SECTIONS, frontmatter, load_catalog, select_ids, skill_path

# These are detection patterns, not claims that any matched standard exists.
URL = re.compile(r"(?:https?://|www\.)[^\s<>\]\)\"']+", re.I)
STANDARD = re.compile(
    r"\b(?:"
    r"(?:ISO(?:/IEC)?(?:/IEEE)?|IEC|IEEE|RFC|EN|DIN|BS)\s*[-:]?\s*\d+[\w.:-]*(?:-\d+)?"
    r"|NIST(?:\s+(?:SP|FIPS|CSF))?(?:\s+\d+[\w.:-]*)?"
    r"|OWASP(?:\s+(?:ASVS|SAMM|MASVS|WSTG|Top\s+10))?(?:\s+\d+(?:\.\d+)*)?"
    r"|WCAG(?:\s+\d+(?:\.\d+)*)?"
    r"|PCI\s+DSS(?:\s+\d+(?:\.\d+)*)?"
    r"|SOC\s+[12]|CIS(?:\s+Controls)?"
    r")\b", re.I,
)
UNFINISHED = re.compile(r"\b(?:TODO|TBD|lorem)\b|\[citation needed\]|<(?!https?://)[^<>\n]+>", re.I)


def links(text):
    """Extract inline and reference-definition destinations, not prose paths."""
    inline = re.findall(r"\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", text)
    definitions = re.findall(r"^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)", text, re.M)
    return [item.strip("<>") for item in inline + definitions]


def citations(text):
    urls = {match.group().rstrip(".,;:!?") for match in URL.finditer(text)}
    # Avoid recognizing a standard a second time inside an already checked URL.
    prose = URL.sub(" ", text)
    standards = {re.sub(r"\s+", " ", match.group()).upper() for match in STANDARD.finditer(prose)}
    return urls, standards


def citation_errors(text, allowed):
    if allowed is None:
        return []
    urls, standards = citations(text)
    allowed_urls, allowed_standards = allowed
    return ([f"URL not in standards allowlist: {item}" for item in sorted(urls - allowed_urls)]
            + [f"Standard ID not in standards allowlist: {item}" for item in sorted(standards - allowed_standards)])


def reference_errors(root, path, text, allowed):
    errors, seen = [], set()
    reference_roots = {(path.parent / "references").resolve(), (root / "references").resolve()}

    def inspect(source, content, depth):
        for destination in links(content):
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc:
                continue
            relative = unquote(parsed.path).replace("\\", "/")
            if "references" not in relative.split("/"):
                continue
            target = (source.parent / relative).resolve()
            if depth:
                errors.append(f"References nest deeper than one level: {source.name} -> {destination}")
            if target.parent not in reference_roots:
                errors.append(f"Reference must be a direct file in references/: {destination}")
                continue
            if not target.is_file():
                errors.append(f"Missing reference file: {destination}")
                continue
            if target not in seen:
                seen.add(target)
                ref_text = target.read_text(encoding="utf-8")
                if UNFINISHED.search(ref_text):
                    errors.append(f"Unfinished content in reference: {destination}")
                errors.extend(f"{destination}: {message}" for message in citation_errors(ref_text, allowed))
                inspect(target, ref_text, depth + 1)
        # A reference can link another reference by basename, without repeating references/.
        if depth:
            for destination in links(content):
                parsed = urlsplit(destination)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                relative = unquote(parsed.path).replace("\\", "/")
                if "references" in relative.split("/"):
                    continue  # Already reported above.
                target = (source.parent / relative).resolve()
                if target.parent in reference_roots and target.suffix.lower() == ".md":
                    errors.append(f"References nest deeper than one level: {source.name} -> {destination}")
                    if not target.is_file():
                        errors.append(f"Missing reference file: {destination}")

    inspect(path, text, 0)
    local_refs = path.parent / "references"
    if local_refs.exists():
        for ref in local_refs.rglob("*"):
            if ref.is_file() and ref.parent.resolve() != local_refs.resolve():
                errors.append(f"Nested references directory: {ref.relative_to(path.parent)}")
    return errors


def check_skill(root, row, path, text, allowed):
    errors = []
    try:
        fields, body = frontmatter(text)
    except ValueError as exc:
        return [str(exc)]
    if fields.get("name") != row["slug"]:
        errors.append("Frontmatter name must equal catalogue slug")
    description = fields.get("description", "")
    if not 60 <= len(description) <= 1024:
        errors.append(f"Description must be 60..1024 characters (found {len(description)})")
    if not re.search(r"\b(?:Use|when)\b", description, re.I):
        errors.append("Description must contain the word Use or when")
    if "status" in fields and fields["status"] != row["status"]:
        errors.append("Frontmatter status differs from catalogue status")
    headings = re.findall(r"^##\s+(.+?)\s*$", body, re.M)
    required = [heading for heading in headings if heading in SECTIONS]
    if required != list(SECTIONS):
        errors.append("Required sections missing, duplicated, or out of order")
    if len(body.splitlines()) > 250:
        errors.append(f"Body exceeds 250 lines (found {len(body.splitlines())})")
    if UNFINISHED.search(text):
        errors.append("Unfinished content: TODO, TBD, lorem, citation marker, or angle-bracket placeholder")
    errors.extend(citation_errors(text, allowed))
    errors.extend(reference_errors(root, path, text, allowed))
    return errors


def five_grams(body):
    words = re.findall(r"\b\w+\b", body.casefold())
    return {tuple(words[index:index + 5]) for index in range(len(words) - 4)}


def jaccard(left, right):
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def validate(root, only=None):
    entries = load_catalog(root)
    selected = select_ids(only, entries)
    allowlist = root / "references" / "standards-allowlist.md"
    allowed = citations(allowlist.read_text(encoding="utf-8")) if allowlist.exists() else None
    errors, bodies, checked, pending = [], {}, 0, 0
    expected = {skill_path(root, row).resolve() for row in entries}
    if only is None and (root / "skills").exists():
        for path in (root / "skills").rglob("SKILL.md"):
            if path.resolve() not in expected:
                errors.append(f"Unknown skill path: {path.relative_to(root)}")
    for row in entries:
        path = skill_path(root, row)
        if not path.is_file():
            if row["id"] in selected:
                if only is not None or row["status"] != "todo":
                    errors.append(f"{row['id']:03d}: Missing skill file: {path.relative_to(root)}")
                else:
                    pending += 1
            continue
        text = path.read_text(encoding="utf-8")
        if row["id"] in selected:
            checked += 1
            errors.extend(f"{row['id']:03d}-{row['slug']}: {item}"
                          for item in check_skill(root, row, path, text, allowed))
        try:
            _, body = frontmatter(text)
        except ValueError:
            body = text
        bodies[row["id"]] = (f"{row['id']:03d}-{row['slug']}", five_grams(body))
    for left, right in itertools.combinations(bodies, 2):
        if left not in selected and right not in selected:
            continue
        left_name, left_grams = bodies[left]
        right_name, right_grams = bodies[right]
        similarity = jaccard(left_grams, right_grams)
        if similarity > 0.35:
            errors.append(f"Copy-paste pair {left_name} / {right_name}: Jaccard {similarity:.3f} > 0.35")
    return errors, checked, pending, allowed is not None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--only", help="Comma-separated catalogue ids; selected files must exist")
    args = parser.parse_args()
    try:
        errors, checked, pending, citations_active = validate(args.root.resolve(), args.only)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Checked {checked} skill(s); {pending} absent todo skill(s); {len(errors)} error(s).")
    if not citations_active:
        print("Citation checks pending: Phase 2 standards allowlist does not exist.")
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
