"""Add release workflow guards without changing descriptions or other sections.

Preview with --dry-run. Plan every edit before writing; fail rather than exceed
the body limit or guess a missing step. Equivalence is checked per target step.
"""

import argparse
from pathlib import Path
import re
import textwrap

from _common import ROOT, frontmatter


SPECIFY = ("State every assumption and proposed default to the user before building; "
           "ask at most three questions, and stop for the user's reply only when "
           "a decision goes beyond the smallest version.")
IMPLEMENT = ("Build the smallest version that meets the request; list larger "
             "extensions as offers and add them only with the user's yes.")
WORKFLOW = re.compile(r"^## Workflow\r?\n(.*?)(?=^## |\Z)", re.M | re.S)
STEP = re.compile(r"^([1-5])\. ([^:\r\n]+):", re.M)


def normalized(text):
    return " ".join(text.lower().replace("\u2019", "'").split())


def equivalent(text, kind):
    """Conservatively require every requested concept, not an isolated keyword."""
    value = normalized(text)
    if normalized(SPECIFY if kind == "Specify" else IMPLEMENT) in value:
        return True
    if kind == "Specify":
        assumptions = re.search(r"(?:state|show|present|disclose)[^.;]*assumptions?[^.;]*defaults?[^.;]*before (?:building|implementation)", value)
        questions = re.search(r"(?:at most|up to) three (?:clarifying )?questions", value)
        stopping = re.search(r"(?:stop|pause|wait)[^.;]*only (?:when|if)[^.;]*(?:beyond|exceeds|outside)[^.;]*(?:smallest|minimum) version", value)
        return bool(assumptions and questions and stopping)
    minimum = re.search(r"(?:build|implement|start with)[^.;]{0,100}smallest[^.;]*(?:version|surface)", value)
    offers = re.search(r"(?:list|offer|present)[^.!?]*extensions", value)
    consent = "user's yes" in value or "explicit user approval" in value
    return bool(minimum and offers and consent)


def transform(text):
    match = WORKFLOW.search(text)
    if not match:
        raise ValueError("Missing Workflow section")
    workflow = match[1]
    steps = list(STEP.finditer(workflow))
    targets = {int(step[1]): (step, steps[i + 1].start() if i + 1 < len(steps) else len(workflow))
               for i, step in enumerate(steps)}
    newline = "\r\n" if "\r\n" in text else "\n"
    changes = []
    edits = []
    for number, title, sentence in ((2, "Specify", SPECIFY), (3, "Design/Implement", IMPLEMENT)):
        if number not in targets or targets[number][0][2] != title:
            raise ValueError(f"Missing or unexpected step {number}: {title}")
        step, end = targets[number]
        original = workflow[step.start():end]
        if equivalent(original, title):
            changes.append(f"{title}=skip-equivalent")
            continue
        content = original.rstrip("\r\n")
        addition = newline.join(textwrap.wrap(sentence, width=88, initial_indent="   ", subsequent_indent="   "))
        replacement = content + newline + addition + original[len(content):]
        edits.append((step.start(), end, replacement))
        changes.append(f"{title}=add")
    for start, end, replacement in reversed(edits):
        workflow = workflow[:start] + replacement + workflow[end:]
    updated = text[:match.start(1)] + workflow + text[match.end(1):]
    _, body = frontmatter(updated)
    if len(body.splitlines()) > 250:
        raise ValueError("Workflow guards would exceed 250 body lines")
    return updated, changes


def apply(root, dry_run=False):
    paths = sorted((root / "skills").glob("*/SKILL.md"))
    if not paths:
        raise ValueError("No skill entrypoints found")
    plans = []
    for path in paths:
        original = path.read_bytes().decode("utf-8")
        try:
            updated, changes = transform(original)
        except ValueError as error:
            raise ValueError(f"{path.relative_to(root)}: {error}") from error
        plans.append((path, original, updated, changes))
    changed = 0
    for path, original, updated, changes in plans:
        if original != updated:
            changed += 1
            if not dry_run:
                path.write_bytes(updated.encode("utf-8"))
        print(f"{path.relative_to(root).as_posix()}: {', '.join(changes)}")
    print(f"{'DRY RUN' if dry_run else 'APPLIED'}: {changed}/{len(paths)} skill files need changes.")
    return changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Show planned changes without writing skills")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        apply(args.root, args.dry_run)
    except (OSError, ValueError) as error:
        parser.exit(1, f"ERROR: {error}\n")


if __name__ == "__main__":
    main()
