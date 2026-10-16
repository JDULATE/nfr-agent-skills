# nfr-agent-skills

114 Non-Functional Requirement (NFR) skills and a selector for choosing among them.
Each skill helps an agent clarify a concern, propose requirements, make a scoped
change, and report verification. Browse [INDEX.md](INDEX.md) for the catalogue.

**All 115 skills are drafts.** No release is tagged by this Phase 6 work.
The terminology boundaries are proposed repository conventions, not standardized
definitions. These workflows do not establish compliance or production readiness.

## Use with Codex

Verified against [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills):
Codex discovers skill names, descriptions, and paths, then reads the full SKILL.md
when a skill is selected. SKILL.md requires name and description frontmatter.
Repository discovery scans `.agents/skills` from the working directory up to the
repository root; the documented user location is `$HOME/.agents/skills`.
Symlinked skill folders are supported. Large installed collections can have
descriptions shortened or skills omitted from the initial discovery list.

Keep this checkout accessible. Copy or link selected complete skill folders from
`skills/` into your project's `.agents/skills/`, for example:

```text
your-project/
  .agents/skills/
    006-adjustability/
      SKILL.md
      references/
    000-nfr-selector/
      SKILL.md
      references/
```

The top-level `skills/` directory in this checkout is not itself a documented
Codex discovery location. Installing a few relevant skills avoids relying on
every description fitting in the discovery list. No installation was performed
or tested on another machine during this work; the documented locations and
format were confirmed, while environment-specific installation remains unverified.

For the selector, retain access to this bundle's INDEX.md, selector.json, and
references/disambiguation-map.md. If copied separately, give the agent the bundle
path; copying the selector folder alone does not supply its catalogue resources.

In Codex CLI or the IDE extension, use `/skills` or a `$` mention to select a
skill by its frontmatter name, such as `$adjustability` or `$nfr-selector`.
Codex can also choose a skill from its description.

Example requests:

- `$adjustability Make this batch cap runtime-changeable within the same worker setup.`
- `$nfr-selector Which NFRs matter for this service? Propose the smallest useful set.`

Use the selector for explicit NFR selection, broad readiness requests, or several
qualities together. Use an individual skill directly for one identified concern.

## Other agents

For an agent that can read Markdown files, explicitly point it to the chosen
`skills/NNN-slug/SKILL.md`, ask it to read the file before building, and follow its
Workflow. Provide linked references and project access as needed. Automatic
discovery, invocation syntax, and installation locations for other hosts are
unverified here; do not assume that they scan Codex's directories.
Read [AGENTS.md](AGENTS.md) for consumer guidance.

## Quality and evidence limits

Routing was tested on a small authored set and selected reruns, including 12
held-out prompts. The held-out result was 11/12; one ambiguous recurring-bug
prompt chose maturity, where asking the user was judged better. Routing accuracy
does not demonstrate that the workflows produce better implementations.

Fast paths were exercised in a few scratch runs only, as reported by the user.
A no-skills baseline behaved about the same on one task. These observations do
not establish a benefit over the baseline. Broad real-task workflow coverage,
independent replication, and deployment-level results are missing.
Availability and readability retain a repository-specific status frontmatter
field rejected by the supplemental Skill Creator checker. Their runtime host
compatibility has not been demonstrated by the repository validator passing.
Development checkouts retain counts, routing provenance, uncertain claims, and
known weaknesses in `reviews/final-report.md`. Reviews are development evidence
and are excluded from future Git archive exports.

## Repository layout and contributions

- `skills/`: 114 NFR entrypoints plus `000-nfr-selector`, with local references.
- `nfr-list.json`: the unchanged 114-NFR catalogue; `selector.json`: selector status.
- `INDEX.md`: generated skill links and draft status.
- `references/`: terminology conventions, standards allowlist, and quality rubric.
- `evals/`: routing fixtures, frozen keys, historical snapshots, and supplied results.
- `scripts/`, `tests/`: scaffolding, validation, indexing, and routing scoring.
- `reviews/`: retained development findings, not release documentation.

For authoring rules and commands, read [CONTRIBUTING.md](CONTRIBUTING.md).
The phased authoring process applies to contributions, not to using a skill.
