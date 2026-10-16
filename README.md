# nfr-agent-skills

114 skills for turning software quality concerns into scoped agent work, plus a
selector that helps choose among them. Give a coding agent a concern such as
deployment downtime, unnecessary personal data, or hard-to-read code; the relevant
skill guides it through clarification, requirements, implementation, and verification.
These concerns are called **Non-Functional Requirements (NFRs)** in this catalogue.

**[v0.1.0 pre-release](https://github.com/JDULATE/nfr-agent-skills/releases/tag/v0.1.0):
all 115 skills are drafts.** Terminology boundaries are repository conventions,
not standardized definitions. Using a skill does not establish compliance or
production readiness.

[Browse the catalogue](INDEX.md) · [Quick start](#quick-start) ·
[Evidence and limitations](#evidence-and-limitations) · [Contribute](CONTRIBUTING.md)

## Quick start

You need a coding agent that can read Markdown and access your project's files.
Git is needed for cloning; Python is needed only for repository maintenance checks.

1. Download this repository or clone it:

   ```sh
   git clone https://github.com/JDULATE/nfr-agent-skills.git
   ```

2. Choose a skill from [INDEX.md](INDEX.md). Keep its entire folder, including
   `references/`, accessible to your agent.

3. In your project's agent session, give the agent the checkout path and a request:

   ```text
   Read skills/075-privacy/SKILL.md in the nfr-agent-skills checkout I provided.
   Follow its Workflow for this project: we keep sending email addresses to
   analytics, but we only use account IDs. Propose the smallest change that
   stops sending email addresses. State assumptions before building.
   ```

The intended result is a scoped proposal for the affected data flow, followed by
the authorized change and relevant checks. The agent should identify the producer
and recipient, state assumptions, and report what it verified and what remains
unknown. This is an example request, not a recorded successful implementation.

## Install selected skills in Codex

According to [official OpenAI documentation](https://developers.openai.com/codex/skills),
Codex discovers skill names, descriptions, and paths, then reads the full
`SKILL.md` when selected. For project discovery, put complete skill folders in
`.agents/skills/` within your project. Codex scans these directories from its
working directory up to the repository root. The documented user-wide location
is `$HOME/.agents/skills`; symlinked skill folders are also supported.

For example, copy `skills/075-privacy/` into your project so it looks like this:

```text
your-project/
  AGENTS.md
  .agents/
    skills/
      075-privacy/
        SKILL.md
        references/
```

If you install only skill folders, copy the **Apply the skill** section of this
repository's [AGENTS.md](AGENTS.md#apply-the-skill) into your own project's
`AGENTS.md`. This repository's `AGENTS.md` is not read from your project merely
because the skill folders are installed.

In Codex CLI or the IDE extension, use `/skills` or a `$` mention with the skill's
frontmatter name, which omits the numeric folder prefix:

```text
$privacy Stop sending email addresses to analytics; we only use account IDs.
```

Codex can also select a skill from its description. Install only the skills you
need: large collections can have descriptions shortened or skills omitted from
the initial discovery list. This checkout's top-level `skills/` directory is not
itself a documented discovery location. The documented format and locations were
checked, but installation on another machine remains unverified.

For other agents, use the explicit-file approach in the quick start. Automatic
discovery, installation locations, and invocation syntax for other hosts have not
been verified here.

## Choose the right skill

Use an individual skill for one identified concern. Read the
[disambiguation map](references/disambiguation-map.md) when nearby terms overlap.

| Request | Starting skill |
| --- | --- |
| Users get logged out every time we deploy. | [Availability](skills/015-availability/SKILL.md) |
| We keep storing emails we never use. | [Privacy](skills/075-privacy/SKILL.md) |
| Reduce nesting and rename confusing locals. | [Readability](skills/078-readability/SKILL.md) |
| Which NFRs matter for this service? | [NFR selector](skills/000-nfr-selector/SKILL.md) |

Use `$nfr-selector` for explicit NFR selection, broad requests such as "make this
production-ready", or several qualities together. It reads the index and sibling
boundaries, proposes the smallest useful set, identifies conflicts, and sequences
the individual skills. Selecting skills does not verify readiness.

Keep the selector connected to this bundle's `INDEX.md`, `selector.json`, and
`references/disambiguation-map.md`. If you copy its folder separately, also give
the agent the bundle path; the selector folder alone lacks those shared resources.

Each skill follows **Clarify → Specify → Design/Implement → Verify → Report**.
The workflows ask the agent to inspect existing code and docs, state assumptions
before building, ask at most three questions, build the smallest version that
meets the request, and report verification limits. See [AGENTS.md](AGENTS.md)
for consumer guidance; the phased authoring process applies to contributions,
not to using a skill on your project.

## Evidence and limitations

- All skills remain drafts. Repository validation checks structure and content
  constraints; it does not establish that workflows produce better implementations.
- Routing was tested on a small authored set and selected reruns, including
  **12 held-out prompts, with 11/12 accepted choices**. The remaining prompt
  concerned a recurring bug: the router chose maturity, while asking the user
  was judged better. This result is not a catalogue-wide accuracy estimate.
- Fast paths were exercised in a few manual scratch runs by the maintainer.
  A no-skills baseline behaved about the same on one task. Broad real-task
  coverage, independent replication, and deployment-level evidence are missing.
- About 175 audited transferable Rules of thumb bullets in batches 2–9 were not
  retrofitted; that earlier estimate was not independently recounted during
  release preparation. Also, 21 skills have only three Rules of thumb.
- Host compatibility is not established by repository validation. Every skill's
  frontmatter contains only `name` and `description`; draft status lives in the
  catalogue.

The [final report in the repository](https://github.com/JDULATE/nfr-agent-skills/blob/master/reviews/final-report.md)
contains counts, routing provenance, uncertain claims, and known weaknesses.
The `reviews/` directory is development evidence retained in Git and excluded
from Git archive exports, including release source archives.

## Repository layout

| Path | Contents |
| --- | --- |
| [skills/](skills/) | 114 NFR entrypoints and the selector, with local references |
| [INDEX.md](INDEX.md) | Generated catalogue with links and status |
| [nfr-list.json](nfr-list.json), [selector.json](selector.json) | Catalogue metadata and draft status |
| [references/](references/) | Terminology conventions, standards allowlist, authoring guide, and rubric |
| [evals/](evals/) | Routing fixtures, frozen keys, historical snapshots, and supplied results |
| [scripts/](scripts/), [tests/](tests/) | Validation, indexing, routing scoring, and maintenance tooling |

## Contributing and checks

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing a skill. It defines scope,
authoring phases, the quality rubric, and validation requirements. Run these
checks from the repository root with Python; the scripts use its standard library:

```sh
python scripts/validate_skills.py
python -m unittest discover -s tests
python scripts/build_index.py
```

A successful validator run reports zero errors; tests should report `OK`, and
the index builder should report 115 entries. CI runs on pushes and pull requests
and also checks that the generated index matches the committed file. A passing
check is not skill approval or evidence of better implementation outcomes.

Report defects or unclear sibling boundaries through
[GitHub issues](https://github.com/JDULATE/nfr-agent-skills/issues), with the skill
slug, request, observed behavior, and expected behavior.

## License

[MIT](LICENSE).
