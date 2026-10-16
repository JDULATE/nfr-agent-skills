# Contributing to nfr-agent-skills

These instructions apply to authoring, reviewing, and maintaining this repository.
They do not govern using an existing skill on another project; see
[AGENTS.md](AGENTS.md) for consumer guidance.

Read the [disambiguation map](references/disambiguation-map.md),
[standards allowlist](references/standards-allowlist.md), and
[quality rubric](references/quality-rubric.md) when authoring or reviewing skills.
The rubric requires at least 17/20 and no zeros; validation alone is not approval.

## GLOBAL RULES (apply to every phase)

You are building `nfr-agent-skills`, a repo of 114 agent skills, one per Non-Functional Requirement (NFR).

Anti-hallucination rules:
1. Work ONLY from files in this repo and from the instructions in the current phase. Do not rely on memory for facts you cannot verify.
2. Never invent standards, clause numbers, URLs, tool flags, library versions, statistics, or quotes. Cite only items listed in `references/standards-allowlist.md` (created in Phase 2). If unsure, omit the claim.
3. Numeric targets (e.g. "99.9%", "p95 < 300 ms") are ALWAYS labeled as illustrative examples and must be paired with "confirm with the user/stakeholder". Never present a number as a universal requirement.
4. If something is unknown or depends on context, write "Ask the user" instead of guessing.
5. Do only what the current phase says. Do not start the next phase. Do not edit skills outside the current batch.
6. At the end of each phase, run the validators, commit, print a short report (done / uncertain / needs human review), and STOP.

Work happens in phases. Do only the phase you are told to run, then stop.

## Skill-writing rules from Phase 3

- Voice: imperative, addressed to the agent ("Ask...", "Add...", "Reject..."). No marketing language, no "it is important to".
- Description: third person, includes what + when + 3-6 natural trigger phrases a user might say + "Not for ..." clause naming sibling slugs. Keep it at 350 characters or fewer and state the nearest-sibling ambiguity in the description itself.
- The Workflow must contain real decision rules and must tell the agent to read the existing codebase/docs before specifying anything.
- Specification patterns must give the agent a way to produce a requirement even when the user gives no numbers: propose labeled-illustrative defaults and ask the user to confirm.
- Rules of thumb contain only rules whose acceptance question is specific to this skill. Use 4-6 bullets; move shared safeguards to Workflow or Verification rather than padding the list.
- Put long material (checklists, worked examples, a requirement-spec example, anti-pattern catalog) in `references/*.md`, each under 150 lines, each linked from SKILL.md.
- Include at least one short worked example per skill in references/. Fill every input the example names, include a failing case and a before/after remediation, and make no causal claim the fixture does not support.
- Keep scope honest: every branch promised in the description needs an example. If a branch has no example, narrow the description.
- Update `status` to "draft" in nfr-list.json for these.

In the final rule above, "these" means the skills explicitly authorized in the
current pilot or batch. Phase 2 keeps all 114 entries at `todo` and writes no bodies.

## Structure and execution contract

These updated authoring limits supersede older limits in the template. A validator
pass does not replace manual review of the authoring contract.

- Use `templates/SKILL.template.md` for section order. Target 80-180 body lines;
  do not exceed 250. Keep the description between 60 and 350 characters. State
  the nearest-sibling ambiguity, such as tail latency versus variation, within
  the description; do not leave that boundary only in the body.
- Review the combined footprint: use 200-300 lines as a guideline for the complete
  SKILL.md plus its directly linked reference files, including blank lines and
  frontmatter. This combined guideline is not a ceiling. Keep each reference
  under 150 lines, with design guides up to 80 lines. Report the combined count;
  do not pad short useful material or duplicate sections to reach a lower bound.
  Meeting a line budget does not demonstrate distinct decisions or sufficient depth.
- Write design guides as decision tables: observed evidence -> intervention ->
  how to verify. Include at least three concrete interventions and a short code,
  config, or pseudocode sketch where one applies. Retain use-when context and
  trade-offs in the decisions. Allow up to 80 lines; do not fit every guide to
  the same line count.
- Fill every input named in a worked example, including carried state, conditions,
  and evidence used to decide the result. Do not leave unfilled "retain X" lists.
  Show a failing case and one before/after remediation with actual fixture inputs
  and outputs. Attribute a cause only when the fixture supports it; distinguish
  an observed failed requirement from an unestablished diagnosis.
- Keep folder names as a three-digit, zero-padded id plus slug, such as
  `skills/015-availability/SKILL.md`. Use the unprefixed slug in frontmatter `name`.
- Follow Clarify, Specify, Design/Implement, Verify, Report in that order. Put
  an imperative instruction and an explicit conditional decision in every step.
- Include 2-3 measurable specification patterns. Let content determine item counts:
  use 4-6 NFR-specific rules, 6-10 objective done checks, and 3-6 concrete
  failure modes. Do not impose a fixed shape across skills or add filler to reach
  matching counts; do not vary counts merely to make skills appear different.
- Test every Rules of thumb bullet against its nearest sibling's acceptance
  question. Before committing, move or delete every bullet whose verdict is
  "transferable". Shared measurement safeguards belong in Workflow or Verification:
  denominators, retaining raw samples, preserving timeouts and unfinished work,
  predeclared exclusions, and matched conditions. A different noun does not make
  an acceptance question specific. Report the transfer-test counts after fixing;
  do not put a transfer-test table in the authoring review.
- Use named placeholders such as `{behavior}`, `{condition}`, `{metric}`, and
  `{stakeholder_confirmed_target}` in authored requirement patterns. The current
  validator rejects unresolved angle-bracket template text, including in references.
- Label every proposed numeric target as an illustrative example and include
  the words "confirm with the user/stakeholder" beside it. Record unconfirmed
  values as proposed; do not report them as accepted requirements.
- Read `references/disambiguation-map.md` before choosing a meaning or sibling
  pointer. These are proposed repository conventions, not standardized definitions.
  Ask the user if their terminology differs; record the chosen boundary.
- Read `references/standards-allowlist.md` before citing a standard. Check the
  permitted ids and human-review status manually as well as running the validator.
- Cite ISO/IEC 25010 generically as "ISO/IEC 25010 product quality model". Never
  attribute specific characteristic names, lists, counts, groupings, or
  edition-specific mappings to it. Keep the repository taxonomy explicitly local.
- Link supporting files directly under the skill's `./references/` directory
  with "read when ..." guidance. Do not link from a reference to further references.
  Keep each supporting file under 150 lines. Shared contract files are read
  directly at the start of a phase rather than through chained skill references.
- Name a tool category unless a repository source verifies the specific tool
  and any command or flags. Omit unsupported standards and factual claims.
- Write original body content. Validation compares word 5-gram Jaccard similarity
  with all existing skills and rejects scores over 0.35; do not evade this check
  by adding filler. Distinguish the underlying decisions instead.

## Authoring phases

Run only the phase, batch, or targeted maintenance task the user authorizes.
This overview documents the process; it does not authorize starting another phase.

| Phase | Scope and stop condition |
| --- | --- |
| 1 - Foundation | Establish the 114-entry catalogue, template, generator, validator, index tooling, and CI without skill content; validate, commit, and stop. |
| 2 - Authoring contract | Establish the allowlist, proposed sibling boundaries, categories and batches, rubric, and authoring contract without skill bodies; commit and stop for review. |
| 3 - Pilot | Author only availability, privacy, and readability; validate and review against the rubric, commit, and stop for pilot approval. |
| 4 - Batch production | Read the authoring contract and approved pilots, author only the requested catalogue batch with linked references, validate and review, update its status/index, commit, and stop. |
| 5 - Trigger evaluations | Prepare should-trigger and near-miss prompts, run the authorized description/routing checks, record ambiguity and findings, commit, and stop. Keep held-out prompts separate from description tuning. |
| 6 - Release preparation | Add the selector and release documentation, mark only validated and adequately reviewed skills reviewed, run final checks, rebuild the index, record outstanding uncertainty, and tag the authorized release. Stop. |

Follow the user's current phase instructions and accepted refinements for exact
artifacts, scope, review format, and commit messages. Targeted repairs do not
start a new batch or authorize release work. Phase gates below retain the
pilot and batch details.

## Phase gates

Phase 3 authors only `015-availability`, `075-privacy`, and `078-readability`.
Run `python scripts/validate_skills.py --only 15,75,78`. Score each against the
rubric internally; fix every weakness scoring below 2. Write findings only in
`reviews/pilot-review.md`, without a self-score or transfer-test table. Commit
`phase 3: pilot skills` and stop for approval. Pilot approval is a separate gate
from validation or a `draft` status.

The pilot is authored in Phase 3 regardless of its production batch assignment:

| Pilot folder | Later production batch |
| --- | --- |
| `015-availability` | 6 |
| `075-privacy` | 8 |
| `078-readability` | 4 |

Keep these entries in their batches so siblings are still reviewed together.
When those batches run, count the approved pilot as an existing batch member,
validate and score it with the batch, and author the remaining members. Preserve
the approved pilot content unless the user explicitly requests changes. The
batch assignment neither postpones pilot authoring nor authorizes rewriting it.

For a user-requested Phase 4 batch, first read this guide, the disambiguation map,
the standards allowlist, the rubric, and all three approved pilot skills. Select
only the ids assigned to that batch in `nfr-list.json`; create only their bodies
and directly linked reference files. Preserve approved pilots and other batches;
if a batch includes an approved pilot, review it as the existing member rather
than rewriting it without a user request. Do not silently treat it as approved.

Run `python scripts/validate_skills.py --only` followed by the comma-separated
batch ids. Assess the rubric internally and fix any result below 17/20 or any
zero. Write `reviews/batch-N-review.md` as findings only: per-skill weaknesses,
evidence, limitations, and an "Uncertain claims" section. Do not include prompt
text, task instructions, self-score tables, or transfer-test tables in authoring
reviews. Include only transfer-test counts after fixes. Keep authoring reviews
focused on authoring findings; do not duplicate the independent audit. Set the authorized batch
to `draft`, run `python scripts/build_index.py`, commit using the requested Phase 4
batch message, report done / uncertain / needs human review, and stop.

Numeric authoring limits and rubric scores here are repository process rules,
not performance, reliability, or other system requirement targets. Batches may
mix categories to keep related terminology together. Categories are navigation
labels; they do not establish universal definitions or citation permissions.

## Validation and maintenance commands

Run from the repository root. Validate the authorized scope and run the full test
suite before committing. Use the full validator for checks across the catalogue:

```sh
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

For a selected set, replace the example ids with the authorized ids:

```sh
python scripts/validate_skills.py --only 15,75,78
python scripts/check_descriptions.py --only 15,75,78
```

Description overlap is a heuristic, not proof of routing accuracy. The routing
scorer grades supplied answers; it does not run a model or generate choices:

```sh
python scripts/score_routing.py path/to/results.json --key path/to/key.json
```

Replace those paths with the intended results and matching key. Missing answers
count as misses against that key; held-out and remaining accuracy are separate.
Preserve frozen prompts, keys, and held-out cases unless the user authorizes a change.

Preview scaffolding or rebuild the index only when the task calls for it:

```sh
python scripts/generate_skills.py --dry-run
python scripts/build_index.py
```

The repository scripts use the Python standard library. Generation without
`--dry-run` creates unfinished `todo` stubs that deliberately fail content
validation. Existing files are preserved regardless of catalogue or file status.
Full validation permits absent `todo` skills; an explicit `--only` selection
requires those skills to exist. Existing stubs are checked, and selected bodies
are compared with all existing bodies. Citation checks use the standards allowlist.
Frontmatter supports top-level plain, quoted, and block string fields; unsupported
YAML constructs fail. Do not regenerate or overwrite authored content as part of
routine validation.

Write findings-only reviews, record uncertainty and verification limits, commit
only the authorized files, report done / uncertain / needs human review, and stop.
