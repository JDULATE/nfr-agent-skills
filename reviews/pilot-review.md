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

The follow-up checklist audit below found that the initial specificity assessment
was too generous. Its corrections supersede the initial criterion 5 judgments;
the final table above describes the revised content. Retain the limitations below
rather than presenting rubric completion as operational evidence.

## Initial validation and integration record (before checklist audit)

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

## Follow-up checklist audit

Ask of each selected rule: **Could this sit in Security or Reliability unchanged,
or does its acceptance decision belong specifically to the named NFR?** Inspect
the other rules too; replacing the NFR's name in generic advice is not a fix.

### Three sampled rules per pilot

| Pilot and rule position | Rule before this audit, abbreviated | Could it fit a different NFR unchanged? | Decision and resulting acceptance question |
| --- | --- | --- | --- |
| Availability 1 | Probe a business result rather than process health. | Yes: reliability checks can use the same advice. | Rewrite around admission to good eligible time: did this observation satisfy the journey's availability boundary? |
| Availability 2 | Drain traffic and include in-flight work. | Yes: general reliability or deployment advice. | Rewrite around measuring the interruption from lost usable service through its return, including in-flight work. |
| Availability 4 | Map shared dependencies; do not assume replicas are independent. | Yes: reliability failure modeling. | Rewrite around whether replica health histories establish customer-visible good time through a shared dependency outage. |
| Privacy 2 | Derive a recipient-specific payload for its approved purpose. | Potentially: recipient filtering can remain a general confidentiality rule. | Rewrite to constrain even an authorized recipient: are unused personal fields being sent despite access permission? |
| Privacy 5 | Prevent restored data from repopulating deleted records; bound suppression evidence. | No: the accepted personal-data deletion decision and evidence expiry define the rule. | Keep it; ask whether restoration undoes the agreed disposal lifecycle, rather than merely restoring valid stored state. |
| Privacy 6 | Omit raw personal payloads from disposal logs. | Yes: secure logging advice can reuse it. | Rewrite around the disposal log's own purpose and expiry: does the log recreate a profile beyond its accepted evidence lifetime? |
| Readability 1 | Name locals for domain meaning rather than unfamiliar abbreviations. | No: the intended reader's decoding burden defines success. | Keep it; ask whether the name exposes the value's meaning to that audience. |
| Readability 3 | Flatten nesting only while preserving effect and exit order. | Yes: behavioral preservation fits reliability or correctness. | Rewrite around reader tracing and backtracking; retain nesting when scattered exits make following outcomes harder. |
| Readability 5 | Preserve external names and keyword contracts while renaming. | Yes: compatibility and regression prevention can reuse it. | Rewrite around exposing an opaque key's meaning locally so the reader benefits without changing the external contract. |

Also rewrite availability rule 3, found during the full rules scan: classify an
optional-dependency outage by whether the accepted journey still earns good time,
instead of giving generally reusable advice to isolate dependencies. Seven sampled
rules and this additional rule changed. Keep purpose, accounting, or reader-task
decisions in the rule itself rather than merely labeling it with an NFR name.

On this audit, reassess criterion 5 as initially 1/2 for each pilot, then 2/2 after
the rewrites. The final author-assigned totals remain 20/20; they do not establish
independent behavioral validity or erase the initial review's missed weaknesses.

### Workflow, numbers, descriptions, and boundaries

- Inspect all 15 steps: each contains an explicit If/then decision. Make inspection
  of code and documentation explicit in availability and privacy Clarify; readability
  already requires surrounding source and adjacent documentation before specifying.
- Inspect every digit occurrence in the nine skill and supporting files: all nine
  requirement-target occurrences have an illustrative label and an adjacent
  "confirm with the user/stakeholder" instruction. Other digit occurrences in those
  files are the workflow step numbers. Find no unqualified numeric requirement.
- Find no named regulation or asserted legal deadline in the privacy artifacts.
  Add "Ask the user which regulations apply" and require relevant source text.
  Keep collection purpose and lifecycle distinct from permission to disclose, and
  keep identity-unlinkability claims in the anonymity sibling.
- Read all descriptions as discovery text: retain four plausible user phrases
  per pilot and explicit Not-for exclusions. Check all six exclusion slugs against
  `nfr-list.json`: they exist as canonical entries. Their skill files do not yet
  exist because they remain `todo`; this audit does not pretend otherwise or create
  out-of-phase stubs. Treat them as catalogue routing pointers until authored.
- Keep readability focused on code and text organization, meaning, and reader
  tracing. Keep character recognition and display contrast with legibility and
  accessibility concerns with the sibling boundaries in the disambiguation map.
- Open every reference and check its use: availability supplies a checkout handoff
  and mandatory-store failure; readability supplies executable before/after code;
  privacy now supplies concrete before/after event JSON and names forbidden fields.
  The privacy example previously named a flow but left its exact payload abstract.
  Parse the revised JSON and check the stated field boundary; do not treat that
  parser check as a production data-flow or disposal test.
- Confirm both direct links in each pilot have Read/when guidance, each target
  exists, and none of the six supporting files links onward to another reference.

### Current artifact evidence

| Pilot | Body lines | Description characters | Supporting file line counts |
| --- | --- | --- | --- |
| Availability | 124 | 285 | measurement contract 86; deployment example 59 |
| Privacy | 131 | 293 | lifecycle contract 84; analytics example 82 |
| Readability | 129 | 299 | review protocol 76; calculation example 72 |

All supporting files remain under 150 lines. Current body word-five-gram Jaccard
similarities are availability/privacy 0.005074, availability/readability 0.005092,
and privacy/readability 0.006404. Re-run selected and full validation after this
audit; both must report zero errors before committing.

### Concrete limitations remaining

- **Availability sampling:** The contract's lower and upper ratios describe its
  classified bins. They do not bound interruptions between successful probes.
  No real observation window or monitor-failure dataset has been collected; Ask
  the user for cadence, coverage, and unknown-bin acceptance in the target project.
- **Availability example scope:** The worked example covers order acceptance during
  a deployment and a mandatory-store outage. It does not demonstrate long-lived
  session continuity, regional failover, or recovery of in-flight streaming work.
  If those are required, extend the project's journey and interruption exercises.
- **Privacy scope evidence:** The payload example proves only what its synthetic
  before/after objects contain. No production serializers, SDK-enriched fields,
  cross-store subject matching, or external recipient erasure have been exercised.
  Ask the user for the real destination inventory and evidence for each copy.
- **Privacy policy:** No regulation-specific source text or applicable-policy
  decision is established by these artifacts. Ask the user which regulations apply
  and how collection, exceptions, and disposal are authorized; the illustrative
  durations must never substitute for those decisions.
- **Readability evidence:** There are no unaided reader observations. The example
  demonstrates a single intermediate calculation, not a prose rewrite or a guard
  transformation. The six earlier synthetic execution cases do not cover arbitrary
  numeric objects, side effects, or every exception; Ask the user for representative
  reader tasks and preserve the actual project's behavioral contract when applying it.
- **Routing and approval:** The six excluded sibling skills are catalogue entries
  awaiting their own batches. A routing pointer is not a loadable skill today.
  These pilots remain drafts, and author-assigned rubric scores do not constitute
  the user's approval for gold examples or batch production.

Stop here. Do not author other skills, batch reviews, trigger evaluations, or release
artifacts as part of this phase.
