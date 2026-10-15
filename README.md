# nfr-agent-skills

Foundation for 114 Non-Functional Requirement (NFR) agent skills.
Phase 1 contains data and tooling only; `skills/` is intentionally empty.

Run from this directory:

```sh
python -m unittest discover -s tests -v
python scripts/generate_skills.py --dry-run
python scripts/validate_skills.py
python scripts/build_index.py
```

The scripts use the Python standard library. Generation without `--dry-run`
creates unfinished `todo` stubs which deliberately fail content validation.
Existing files are always preserved, regardless of catalogue or file status.
Use `--only 15,75,78` to select catalogue ids for generation or validation.

Full validation permits absent `todo` skills while work is pending; an explicit
`--only` selection requires those files to exist. Existing stubs are checked,
not silently skipped. Selected bodies are compared with all existing bodies.
Citation checks activate when the Phase 2 standards allowlist exists.

Frontmatter supports top-level plain, quoted, and block string fields; unsupported
YAML constructs fail with an error. Installation and contribution docs await
later phases. Empty `skills/` is recreated by the scripts after a fresh checkout,
because Git does not track empty directories.
