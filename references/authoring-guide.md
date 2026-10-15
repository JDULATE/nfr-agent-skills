# Authoring guide

Read when authoring or reviewing a skill in an authorized phase.

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
- Description: third person, includes what + when + 3-6 natural trigger phrases a user might say + "Not for ..." clause naming sibling slugs.
- The Workflow must contain real decision rules and must tell the agent to read the existing codebase/docs before specifying anything.
- Specification patterns must give the agent a way to produce a requirement even when the user gives no numbers: propose labeled-illustrative defaults and ask the user to confirm.
- Rules of thumb must be things that could be WRONG for another NFR. If a bullet would fit any skill, delete it.
- Put long material (checklists, worked examples, a requirement-spec example, anti-pattern catalog) in `references/*.md`, each under 150 lines, each linked from SKILL.md.
- Include at least one short worked example per skill in references/.
- Update `status` to "draft" in nfr-list.json for these.

In the final rule above, "these" means the skills explicitly authorized in the
current pilot or batch. Phase 2 keeps all 114 entries at `todo` and writes no bodies.

## Structure and execution contract

- Use `templates/SKILL.template.md` for section order. Target 80-180 body lines;
  do not exceed 250. Keep the description between 60 and 1024 characters.
- Review the combined footprint: use 150-250 lines as a guideline for the complete
  SKILL.md plus its directly linked reference files, including blank lines and
  frontmatter. Keep each reference under 150 lines. Report the combined count;
  do not pad short useful material or duplicate sections to reach a lower bound.
  Meeting a line budget does not demonstrate distinct decisions or sufficient depth.
- Keep folder names as a three-digit, zero-padded id plus slug, such as
  `skills/015-availability/SKILL.md`. Use the unprefixed slug in frontmatter `name`.
- Follow Clarify, Specify, Design/Implement, Verify, Report in that order. Put
  an imperative instruction and an explicit conditional decision in every step.
- Include 2-3 measurable specification patterns. Let content determine item counts:
  use 5-10 NFR-specific rules, 6-10 objective done checks, and 3-6 concrete
  failure modes. Do not impose a fixed shape across skills or add filler to reach
  matching counts; do not vary counts merely to make skills appear different.
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

## Phase gates

Phase 3 authors only `015-availability`, `075-privacy`, and `078-readability`.
Run `python scripts/validate_skills.py --only 15,75,78`. Score each against the
rubric in `reviews/pilot-review.md`; fix every weakness scoring below 2. Commit
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
text, task instructions, or self-score tables in batch reviews. Set the authorized batch
to `draft`, run `python scripts/build_index.py`, commit using the requested Phase 4
batch message, report done / uncertain / needs human review, and stop.

Numeric authoring limits and rubric scores here are repository process rules,
not performance, reliability, or other system requirement targets. Batches may
mix categories to keep related terminology together. Categories are navigation
labels; they do not establish universal definitions or citation permissions.
