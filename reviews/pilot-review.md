# Phase 3 pilot self-review

Review only the availability, privacy, and readability pilots. Treat these scores
as the author's rubric assessment, not user approval or an independent evaluation.
Keep all three catalogue entries at `draft` until the user reviews them.

## Artifacts reviewed

- [Availability](../skills/015-availability/SKILL.md): service boundary, accounting,
  dependency and deployment exercises, measurement contract, and deployment example.
- [Privacy](../skills/075-privacy/SKILL.md): purpose and lifecycle inventory,
  recipient boundaries, subject-scoped disposal, and analytics example.
- [Readability](../skills/078-readability/SKILL.md): reading tasks, preserved meaning,
  unaided reader evidence, review protocol, and calculation example.

Use the exact criteria in `references/quality-rubric.md`. Score each criterion
0-2; require at least 17/20 and no zeros. Phase 3 additionally requires fixing
every weakness scoring below 2.

## Final rubric scores

| Criterion | Availability | Privacy | Readability |
| --- | --- | --- | --- |
| 1. Description has clear WHAT + WHEN + triggers + a "Not for" pointer | 2 | 2 | 2 |
| 2. Definition is correct and distinguishes siblings | 2 | 2 | 2 |
| 3. Workflow is executable: an agent could follow it without extra context | 2 | 2 | 2 |
| 4. Specification patterns are measurable and testable | 2 | 2 | 2 |
| 5. Rules of thumb are specific to this NFR (not interchangeable with another skill) | 2 | 2 | 2 |
| 6. Verification names concrete, real checks | 2 | 2 | 2 |
| 7. Done checklist items are objectively checkable | 2 | 2 | 2 |
| 8. No invented facts, standards, or unlabeled numbers | 2 | 2 | 2 |
| 9. Concise: no filler, no repetition, imperative voice | 2 | 2 | 2 |
| 10. Progressive disclosure: depth lives in references/, linked with "read when" guidance | 2 | 2 | 2 |
| **Total** | **20/20** | **20/20** | **20/20** |

## Evidence for the scores

- **Description and boundary:** Each description contains four natural trigger
  phrases and explicit sibling exclusions. Check the availability distinction from
  reliability and recoverability, privacy from confidentiality and anonymity,
  and readability from legibility and comprehensibility against the repository map.
- **Executable workflow:** Each pilot begins by reading the relevant project
  artifacts and has the required five steps with explicit conditional decisions.
  Missing service, data-policy, or audience context prompts "Ask the user".
- **Specification:** Each pilot has three requirement patterns with named decision
  fields, evidence, and acceptance boundaries. Every numeric target proposal in
  the bodies and examples is labeled illustrative and paired with
  "confirm with the user/stakeholder". No target is reported as universally required.
- **Specific design rules:** Availability addresses journey probes, shared outage
  paths, draining, and denominator exclusions. Privacy addresses producer and
  recipient minimization, derived copies, withdrawal, and restored data. Readability
  addresses domain names, intermediate meanings, local reasoning, effect order,
  public names, and prose qualifiers. Retain these concrete distinctions rather
  than substituting generic recommendations to test, document, or monitor.
- **Verification and completion:** Each checklist has eight checkable actions.
  Availability names journey, handoff, dependency-loss, and missing-monitor checks.
  Privacy names negative payload, timing, disposal failure, subject isolation, and
  restore/replay checks. Readability names behavioral comparison, obligation mapping,
  keyword compatibility, and unaided reader questions, with correctness separated
  from speed and static scores.
- **Grounding and voice:** Use the repository's proposed definitions and original
  hypothetical examples; do not assert standards mappings, laws, quotations, tool
  versions, external statistics, or project observations. Use imperative bodies and
  third-person discovery descriptions. Keep examples explicitly hypothetical.
- **Progressive disclosure:** Link each pilot directly to its two supporting files
  with "Read ... when" guidance. Place detailed worksheets, requirement records,
  expanded checks, anti-patterns, and worked examples there. Keep all references
  under 150 lines and avoid outgoing reference chains.

## Weaknesses found and fixed

Initial content assessment: availability 20/20, privacy 19/20, readability 20/20.

- **Privacy, criterion 6, initially 1/2:** Disposal checks covered completion and
  remaining copies but did not explicitly challenge request verification or prove
  that another subject was untouched. Add an unverified-request negative case and
  an unrelated synthetic subject control to the main Verification section, done
  checklist, lifecycle matrix, and worked example. Reassess criterion 6 as 2/2.

No remaining criterion scores below 2 were found in this self-review. Retain the
limitations below rather than presenting rubric completion as operational evidence.

## Validation and integration record

- `python scripts/validate_skills.py --only 15,75,78`: checked three skills,
  no missing selected files, zero errors; citation checks active.
- `python scripts/validate_skills.py`: checked three skills, reported the other
  111 as absent `todo` entries, zero errors.
- `python -m unittest discover -s tests -v`: all 17 tests passed after repairing
  the fixture baseline described below.
- `python scripts/build_index.py`: regenerated the index with only the pilot
  statuses changed to `draft`; category and batch assignments are preserved.
- Body lengths: availability 122 lines, privacy 127, readability 127. Description
  lengths: 285, 293, and 299 characters respectively. Each has four quoted triggers.
- Direct supporting-file lengths: availability 86 and 59; privacy 82 and 63;
  readability 76 and 72 lines. Each pilot has only those two direct references.
- Body word-five-gram Jaccard similarities: availability/privacy 0.005288,
  availability/readability 0.005233, privacy/readability 0.006629; all below 0.35.
- Both Python blocks in the readability example compiled. Outputs or exception
  outcomes matched across six synthetic keyword-call cases, including no items,
  several items, discount and fee handling, a fractional price, and a missing key.
  These checks support preservation for those cases only, not a reader outcome.

The foundation tests initially copied the advancing production statuses into
their empty-scaffold fixtures, causing three failures when the pilots became
drafts. Normalize only those temporary fixture statuses to `todo` after validating
the source catalogue. Preserve assertions about missing drafted files and
non-overwrite behavior. Do not weaken or modify the skill validator.

## Uncertain claims and human review

- **Availability:** Ask the user for service calendars, accepted degraded results,
  deadlines, sampling and aggregation rules, target approval, and the unknown-data
  policy in the project where the skill is used. The sample deployment is invented;
  its outage cause and proposed repair are not findings about an actual system.
- **Privacy:** Ask the user for personal-information scope, purpose authority,
  recipient boundaries, disposal deadlines, backup expiry, and exception decisions.
  Actual processor deletion and restored-data suppression require destination
  evidence; this pilot does not claim either has been performed in a real service.
- **Readability:** Ask the user for audience familiarity, authoritative meaning,
  reading questions, acceptable evidence, and timing decisions. No representative
  reader sessions were conducted. The synthetic arithmetic checks do not establish
  that a reader understands the revised code better.
- **Approval:** Ask the user to review the pilot definitions, specificity, and depth.
  Keep them as drafts; use them as approved gold examples only after that review.

Stop here. Do not author other skills, batch reviews, trigger evaluations, or release
artifacts as part of this phase.
