# Phase 3 pilot revision review

Review the availability, privacy, and readability drafts only. No batch was started.
The latest revision changes privacy and this review only; the other pilots retain
their previous content and assessment.
These are author-assigned scores, not user approval or an independent evaluation.
The earlier perfect scores were too confident about cross-NFR specificity; the
follow-up audit corrected eight rules. Retain the pilots as drafts for user review.

## Current rubric scores

Use the criteria in `references/quality-rubric.md`, scored 0-2 with at least
17/20 and no zeros required. Assign a provisional 1 for workflow execution
confidence: the fast paths are specified but have not been forward-tested with
an independent agent on incomplete requests. Do not claim that author inspection
proves the agent will honor the question ceiling or continue to design correctly.

| Criterion | Availability | Privacy | Readability |
| --- | --- | --- | --- |
| 1. Description has clear WHAT + WHEN + triggers + a "Not for" pointer | 2 | 2 | 2 |
| 2. Definition is correct and distinguishes siblings | 2 | 2 | 2 |
| 3. Workflow is executable: an agent could follow it without extra context | 1 | 1 | 1 |
| 4. Specification patterns are measurable and testable | 2 | 2 | 2 |
| 5. Rules of thumb are specific to this NFR (not interchangeable with another skill) | 2 | 2 | 2 |
| 6. Verification names concrete, real checks | 2 | 2 | 2 |
| 7. Done checklist items are objectively checkable | 2 | 2 | 2 |
| 8. No invented facts, standards, or unlabeled numbers | 2 | 2 | 2 |
| 9. Concise: no filler, no repetition, imperative voice | 2 | 2 | 2 |
| 10. Progressive disclosure: depth lives in references/, linked with "read when" guidance | 2 | 2 | 2 |
| **Provisional total** | **19/20** | **19/20** | **19/20** |

The latest request explicitly asks for an honest weaknesses list rather than
unsupported perfect scores. Keep this execution-confidence weakness visible;
do not promote the pilots to approved gold examples on these scores alone.
Criterion 6 assesses the concrete checks named by the skill, not a claim that
those checks were performed against a deployed application.

## Changes in this revision

### Latest privacy-only revision

- Add [privacy design patterns](../skills/075-privacy/references/design-patterns.md):
  eight mechanisms, each with use conditions, trade-offs, and verification. Cover
  recipient serializers, field tags, choice propagation, TTL/scheduled retention,
  hard/soft delete and tombstones, restore suppression, retryable deletion, and
  log/error redaction. Link the guide from Design/Implement and References.
- Expand the inventory's Copies row, the defaults block, and Verification to cover
  logs, error trackers, URLs/query strings, third-party SDKs/tags, and replay or
  screenshots. Check initial capture and transmission, not just display masking.
- Broaden discovery with the user's regulation/request labels and personal-data
  terms. Record those labels as stakeholder-supplied constraints; ask what policy
  or counsel requires of the system without asserting obligations as facts.
  State that the output is an engineering requirement, not a compliance conclusion.
- Include sensitive categories and minors in the first grouped question, together
  with the conditional request for stricter handling. Keep the complete inventory
  row and lifecycle record in one labeled defaults block and at most three question
  groups total, then proceed to reversible design with unresolved policy visible.
- Add a filled synthetic support-contact inventory row. Distinguish the illustrative
  deletion deadline from retention after case closure and backup expiry. Do not
  treat a hypothetical approved rotation event as an established project schedule.
- Remove only privacy's frontmatter `status` as explicitly requested. Its catalogue
  status remains `draft`; do not alter the template, the other pilots, or shared tooling.

### Prior pilot revision retained

- [Availability](../skills/015-availability/SKILL.md): open with the plain meaning,
  broaden discovery to uptime, downtime, zero-downtime deployment, high availability,
  and SLA/SLO requests, and retain exclusions for reliability and recoverability.
  Add a complete labeled defaults block, at most three grouped questions, and a
  path to reversible design while answers are pending. Route design choices through
  the new [pattern guide](../skills/015-availability/references/design-patterns.md).
- Cover graceful shutdown/draining, readiness versus liveness, rolling, blue-green,
  canary, schema compatibility, timeouts/bounded retries, shedding, and shared failure
  mapping. Give every pattern a use condition, trade-off, and controlled verification
  exercise. Do not prescribe a tool, version, flag, capacity count, or universal timeout.
- Add the requested illustrative time-accounting arithmetic to the
  [measurement contract](../skills/015-availability/references/measurement-contract.md).
  Keep its example window, durations, percentages, and comparison inside explicitly
  illustrative guidance with stakeholder confirmation. Distinguish accounting bounds
  from measurement coverage and from interruptions between samples.
- [Privacy](../skills/075-privacy/SKILL.md) and
  [readability](../skills/078-readability/SKILL.md): apply only the requested fast-path,
  discovery, definition, and hedging revisions. Keep the earlier purpose, anonymity,
  disclosure, visual-legibility, and conceptual-explanation boundaries intact.
- Remove redundant numeric proposals from the Specification patterns sections;
  point to each skill's labeled defaults block instead. Preserve explicit confirmation
  where defaults become acceptance criteria, policy decisions, or reported attainment.
- In the prior revision, keep `status: draft` in frontmatter because `SKILL.template.md`
  contains `status: todo`. That earlier conditional instruction did not trigger;
  the current explicit request removes the field from privacy only. All three
  catalogue statuses remain `draft`; template and generator are unchanged.
- Extend the validator to reject sibling pointers absent from the catalogue.
  Cover descriptions, distinction and routing text, explicit sibling labels, local
  skill paths, and directly linked supporting references. Accept registered siblings
  that have not yet been authored. Add positive, negative, ordinary-code, reference,
  and CLI exit-code checks in two new test methods.

## Prior nine-rule transfer audit retained

Ask: could each selected rule sit in Security or Reliability unchanged?

| Pilot/rule | Finding before the transfer audit | Current boundary |
| --- | --- | --- |
| Availability 1 | General journey probes could fit reliability. | Admission to good eligible time requires the business result. |
| Availability 2 | Traffic draining alone was general deployment advice. | Measure loss and return of usable service, including in-flight work. |
| Availability 4 | Shared-failure mapping alone could fit reliability. | Replica health does not establish good journey time through shared dependencies. |
| Privacy 2 | Recipient filtering could become confidentiality-only guidance. | Limit even an authorized recipient to purpose-needed personal fields. |
| Privacy 5 | Already specific; retained. | Restores must respect the personal-data disposal decision and evidence lifetime. |
| Privacy 6 | Omitting raw payloads was generic secure logging advice. | Give disposal evidence its own minimization purpose and expiry. |
| Readability 1 | Already specific; retained. | Reduce the intended reader's domain-term decoding burden. |
| Readability 3 | Effect preservation alone could fit correctness or reliability. | Use guards only when they reduce tracing and backtracking burden. |
| Readability 5 | Preserving external names alone could fit compatibility. | Expose an opaque key's meaning locally for the reader without changing the contract. |

The eighth rule changed in that audit was availability's optional-dependency rule:
classify its outage by whether the accepted journey still earns good time.
The earlier privacy audit also added unverified-request and unrelated-subject
controls; keep those checks and the concrete before/after analytics JSON.

## Validation evidence

- Selected privacy validation checked one skill with zero errors. Full validation
  checked the same three with zero errors and 111 absent `todo` entries.
- The unchanged foundation suite passed all 19 tests in the prior pilot revision,
  including the two sibling-check methods; this privacy-only pass reran validators.
- Current body lengths: availability 155 lines; privacy 170; readability 152.
  Description lengths: 308, 480, and 314 characters, with five, six, and five quoted
  trigger phrases respectively. All use real catalogue slugs in their exclusions.
- Supporting lengths: availability measurement 114, deployment example 59, design
  patterns 102; privacy lifecycle 101, analytics example 82, and design patterns 92; readability protocol
  76 and calculation example 72. Each file is under 150 lines and directly linked
  with Read/when guidance; none links to a further reference.
- Body word-five-gram Jaccard similarities: availability/privacy 0.007997,
  availability/readability 0.007332, privacy/readability 0.007277; all below 0.35.
- All workflows retain the five required steps and explicit If/then decisions.
  Each fast path has a single labeled full-record block and a three-question ceiling.
  Each Clarify step reads existing source and documentation before specification.
- Decimal arithmetic recomputed the illustrative window partition and each ratio
  in the measurement contract; the displayed four-decimal-place results match.
  The upper and coverage numerators mean different things despite equal results here.
- The earlier readability example compiled and matched outcomes in six synthetic
  keyword-call cases, including a missing-key exception. The analytics before/after
  JSON parsed and matched its stated field allowlist. Those examples are unchanged.
- The only named source of standards permissions remains the URL-free repository
  allowlist. No legal duties, standards characteristic lists, external URLs, editions,
  or tool-specific commands were introduced in the pilot artifacts.

## Honest weaknesses and limitations

- **Fast-path execution is untested:** No independent agent has applied these
  instructions to a vague improvement request, been asked a formal-spec request,
  or been interrupted by missing policy answers. The three-question ceiling is an
  instruction, not automatically enforced. Withhold full workflow confidence until
  such runs show both nonblocking design and correct handling of unresolved decisions.
- **Defaults are not contextual requirements:** Continuous service, the accounting
  window, deletion timing, and the reading budget are examples. They may be unsuitable
  for a real service, retention policy, or audience. Ask the user for the actual
  boundary; do not implement irreversible disposal or claim an accepted target from
  the block alone. Improvement mode permits reversible design, not invented authority.
- **Availability pattern selection is not exercised:** The guide states design and
  verification choices, but no real routing handoff, schema transition, timeout
  budget, overload experiment, or failover was run. Long-lived sessions and shared
  state can invalidate a proposed rollback; inspect the actual implementation.
- **Availability sampling still has blind spots:** Arithmetic checks classified
  durations only. Successful probes do not demonstrate continuous service between
  samples. Ask the user for cadence, locations, workload coverage, and unknown-data
  acceptance; collect a real observation window before reporting attainment.
- **Privacy inventory and authority are unknown:** The synthetic payload does not
  discover SDK-enriched fields, production joins, backup copies, or processor erasure.
  Ask the user which regulations apply and request relevant source text and policy
  decisions. Verify the real copy inventory and deletion evidence per destination.
- **Privacy capture coverage is untested:** No real SDK startup, tag injection,
  URL/query-string logging, error capture, replay frame, or screenshot has been
  inspected. Structured-field checks alone cannot show that an image or nested
  diagnostic payload omitted the same personal marker. Exercise actual capture
  paths and inspect stored recipient copies before claiming coverage.
- **Privacy mechanism semantics are unconfirmed:** Schema tags may not reach derived
  outputs; a configured TTL may only mark expiry; soft deletion and tombstones may
  retain matchable personal data. No store or processor behavior was measured here.
  Verify the chosen store, job ledger, suppression keys, and retry outcomes against
  the approved lifecycle rather than treating the pattern name as evidence.
- **Sensitive/minor scope is unresolved:** No real subject category or stricter
  handling policy is supplied by this synthetic scenario. The conditional question
  is not an assessment of who uses a real application, and a user-named regulation
  or request label does not determine a deadline. Obtain policy/counsel-defined
  system behavior from the stakeholder and retain its attribution.
- **Readability has no audience evidence:** The worked example exposes a subtotal;
  it does not demonstrate a prose rewrite, a guard transformation, or a measured
  reduction in reader mistakes. Six synthetic arithmetic cases do not cover arbitrary
  numeric objects or all exceptions. Ask the user for representative reader tasks,
  meaning-preservation boundaries, and unaided audience observations.
- **Sibling validation is syntactic:** Recognize explicit pointers such as
  `(see slug)`, distinction labels, Route-to-code-form references, sibling labels,
  and local skill paths. Do not claim natural-language understanding of an unmarked
  prose mention or dynamically constructed name. Prefer explicit `(see slug)`
  pointers when introducing a sibling. The check validates catalogue membership,
  not sibling appropriateness or the existence of an authored destination file.
- **Routing and approval remain open:** The six description exclusions are valid
  catalogue entries whose skills remain `todo`. These are routing pointers, not
  loadable sibling skills today. No batch, trigger evaluation, or release work is
  authorized by this revision; the pilots still need user approval.

Stop after validation and the requested `phase 3: pilot revisions (privacy)` commit.
