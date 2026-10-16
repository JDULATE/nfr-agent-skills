---
name: auditability
description: >-
  Defines evidence for independent review when tickets say "the reviewer cannot reconstruct this approval", "our audit trail leaves gaps", or "this export cannot answer the auditor". Not for actor identity (see accountability), artifact links (see traceability), or checking selected rules (see conformance).
---
# Auditability

## Definition and scope

Auditability means an intended reviewer can examine retained evidence to answer
a stated question about actions or controls. Establish provenance, usable retrieval,
and explicit gaps; distinguish actor attribution (`accountability`), connected
artifact history (`traceability`), and satisfying selected rules (`conformance`).

## Use when / Don't use when

- Apply when an examiner cannot reconstruct the evidence for a scoped approval,
  control decision, exception, or review period without relying on the original author.
- Route missing runtime actor identity alone to `accountability`.
- Route requirement/change/evidence links alone to `traceability`; connected
  artifacts can still be inadequate for an independent examination question.

## Workflow

1. Clarify: Read evidence-producing code, retention/access/query docs, control
   records, and actual reviewer questions before prescribing more logs.
   If the examination question or reviewer's permitted view is unknown, then
   Ask the user; do not infer audit sufficiency from the existence of an event store.

2. Specify: Record question, review scope, expected evidence, provenance, ordering,
   access, lifetime, retrieval procedure, redaction, and treatment of missing material.
   If the request is a practical evidence review, then offer this record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Question: named action/control claim over an explicitly bounded review scope.
   Reviewer: independent permitted role, using the approved evidence view and retrieval route.
   Evidence: source/revision, actor/action/result where needed, exceptions, and known gaps.
   Trial gate: 0 unsupported affirmative conclusions in the agreed examination fixtures.
   Retention/access: stakeholder-approved policy; missing durations or authority remain open.
   Method: reviewer reconstructs the answer without private author explanations.
   Status: proposed examination contract, not a legal audit or compliance verdict.
   ```

   Ask at most three groups about question/reviewer; evidence scope, provenance
   and gaps; and retention, access or answer criteria. Continue to a retrieval/evidence design.
   If no criterion exists, then propose the illustrative unsupported-conclusion
   gate and confirm with the user/stakeholder before accepting the fixture scope.

3. Design/Implement: Read [examination practices](./references/design-patterns.md)
   when retaining evidence, exposing retrieval, or distinguishing absent records.
   If a reviewer needs private knowledge to interpret a record, then supply the
   approved schema/decision context rather than counting a successful export as examinability.
   If evidence expired or collection failed, then expose the gap and its scope;
   absence must not silently become evidence that no exception or action occurred.

4. Verify: Give the scoped question and permitted evidence view to the intended
   review role; reproduce the retrieval and inspect the supported answer.
   If redaction or missing provenance prevents an answer, then report that
   limitation without bypassing the approved access boundary to manufacture a pass.

5. Report: Return the question/evidence map, retrieval procedure, observed
   examiner outcomes, provenance limits and unresolved records.
   If only the evidence author could reconstruct the answer, then mark independent
   examination unverified rather than declaring the evidence audit-ready.

## Specification patterns

- **Examination:** For `{review_question_and_scope}`, `{permitted_reviewer}` shall
  retrieve and interpret `{required_evidence}` through `{approved_view}`, producing
  `{supported_answer_or_explicit_gap}` under `{confirmed_answer_rule}`.
- **Evidence boundary:** Retain `{provenance_order_exceptions_and_collection_gaps}`
  under `{approved_lifetime_and_access}`, verified by `{retrieval_and_missing_record_cases}`
  without `{unsupported_absence_or_compliance_inference}`.

Use the illustrative examination gate if no measure is supplied; confirm with
the user/stakeholder. Ask the user for legal/policy requirements rather than inventing retention duties.

## Rules of thumb

- Do start with the review question, not log volume; many unrelated events cannot
  establish the specific control or exception the examiner must evaluate.
- Don't treat missing evidence as evidence of no action; retention expiry and
  collection gaps can make the same empty query mean something entirely different.
- Do preserve provenance and decision context with the approved evidence view;
  a detached event export can be readable yet impossible to evaluate independently.
- Do test examination under the reviewer's actual access and redaction constraints;
  an author's privileged query is not proof that the intended examiner can answer.
- Don't call a connected artifact chain an audit conclusion; the reviewer must
  still assess whether those records support the particular question.
- Do keep contradictory and exception evidence retrievable beside favorable cases;
  a curated success-only export cannot support an independent control examination.

## Verification

Use evidence-retrieval rehearsal, provenance review, and independent-question
reconstruction categories. Exercise normal, contradictory, redacted, expired and
collection-gap records. Record exact scope/query, permitted view, source revisions,
answer and uncertainty. Inspect lifetime/access decisions manually; a logging
library or export success alone establishes no examiner sufficiency or legal compliance.

## Done checklist

- [ ] Bound the question, review scope and permitted independent reviewer.
- [ ] Map required evidence, provenance and decision context to a retrieval route.
- [ ] Reproduce the approved query/view without private author explanations.
- [ ] Inspect contradictory and exception records as well as favorable evidence.
- [ ] Exercise redaction, expiry and collection-gap cases without false absence conclusions.
- [ ] Check retention/access against supplied policy and disclose unresolved decisions.
- [ ] Record supported answers and unanswerable portions separately.

## Failure modes

- Adding logs without identifying the question they must answer.
- Treating an empty query as proof no exception occurred.
- Exporting favorable events while hiding contradictory or missing records.
- Using author-only privileges or knowledge to claim independent examinability.

## References

- Read [examination practices](./references/design-patterns.md) when structuring
  retained evidence, reviewer views or explicit missing-record outcomes.
- Read [approval-examination example](./references/worked-example.md) when provenance,
  exceptions and a collection gap determine what a reviewer can honestly conclude.
