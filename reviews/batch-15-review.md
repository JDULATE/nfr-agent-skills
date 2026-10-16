# Batch 15 authoring findings

Batch 15 contains accuracy, certainty, completeness, conformance, consistency,
and correctness: ids 3, 16, 20, 28, 29, and 31.
All six are draft in the catalogue under Correctness & Data Quality.

## Description-first findings

Descriptions were drafted and compared against the proposed cluster boundaries
before bodies were written. The comparison also included available descriptions
for comprehensiveness, integrity, measurability, provability, trustability, and
standardizability-standardization-standard.

| Skill | Final description characters | Stated acceptance boundary |
| --- | --- | --- |
| accuracy | 264 | reference error versus specified computation and confidence |
| certainty | 224 | warranted confidence versus value error and formal proof |
| completeness | 248 | bounded membership versus explanatory breadth and computed values |
| conformance | 239 | checking selected rules versus choosing a convention |
| consistency | 246 | representation agreement versus reference error and alteration |
| correctness | 309 | behavioral contract versus reference error, membership, and selected-rule checking |

Each description contains three quoted developer phrases.
No exact quoted phrase is shared with another authored description.
Literal uniqueness does not establish routing precision.

The description-first probes distinguished explicit reference, membership,
agreement, confidence, and selected-rule requests.
They could not uniquely route broad quality requests without a comparison object.
Those unresolved probes remain in the routing findings below.

Completeness was narrowed to export membership language after checking its
example coverage. A general case-dispatch trigger would have promised a branch
without a worked example. The body retains conditional guidance for that concern.

## Per-skill weaknesses and transfer findings

### 003 accuracy

The fixture fits a constant offset using a small supplied reference table and
checks separate evaluation cases. It does not establish linearity, physical
calibration, drift, or accuracy under different conditions.
The correction is a demonstrated candidate for this model, not an identified
physical cause of the error.

Reference intervals receive an explicitly proposed indeterminate-decision rule.
No probability interpretation or confidence coverage is established.
Real reference authority, uncertainty treatment, and tolerances remain
stakeholder decisions.

Post-fix transfer count: 4 tested; 2 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: correctness, measurability, correctness,
certainty.
Signed-versus-absolute comparison overlaps measurement design; the acceptance
question here is closeness to the reference, not defining a metric generally.
Reference uncertainty also qualifies confidence, but the rule limits attribution
of an exact error to the instrument.

### 016 certainty

The qualitative policy cannot supply calibrated probability.
Its authoritative ledger is assumed by the fixture; the example does not
establish whether that ledger truthfully reflects delivery.

The first version of the sketch omitted an outcome for wholly contrary evidence.
The final sketch and example distinguish contradicted from both unverified
and conflicting, so a negative authoritative assertion is not promoted to support.
Cached-label requalification still depends on a project-supplied validity rule.

Post-fix transfer count: 4 tested; 3 specific, 1 partly shared, 0 transferable.
Nearest siblings in bullet order: provability, accuracy, consistency,
trustability.
Conflicting observations overlap agreement concerns, but the rule bounds the
strength of the claim made from unresolved evidence.

### 020 completeness

The example enumerates a fixed source snapshot.
It does not demonstrate a real snapshot mechanism or reconciliation under source
mutation. Required-set quality remains a separate assumption: a complete export
of an incomplete inventory is not evidence that the inventory covers reality.

Both the cursor fault and duplicate append are explicitly supplied in the fixture.
Equal counts alone would not identify those causes in an actual export.
Case dispatch is discussed as conditional guidance but has no worked example;
the final description therefore stays with export membership.

Post-fix transfer count: 4 tested; 3 specific, 1 partly shared, 0 transferable.
Nearest siblings in bullet order: correctness, comprehensiveness, traceability,
accuracy.
Identity comparison can detect a behavioral defect too, but the accepted unit
here is a bounded required member, not arbitrary value correctness.

### 028 conformance

The local rule fixture covers field presence/type and spelling only.
The pseudocode is a focused predicate sketch, not a full rule-result engine:
unknown, applicability, exception authority, and revision attribution still need
the surrounding implementation described in the workflow.

The rule-revision safeguard was moved from Rules of thumb into Verification
because it transfers as an evidence safeguard.
A separate original-artifact failure was identified and added: inserting a schema
default before checking cannot establish that the original artifact conformed.
Its negative example keeps a repaired artifact distinct from the original.

Post-fix transfer count: 4 tested; 3 specific, 1 partly shared, 0 transferable.
Nearest siblings in bullet order: correctness, verifiability, debuggability,
standardizability-standardization-standard.
The partly shared rule separates unknown/not-applicable from passed in a
selected-rule result. It does not claim that all unknown evidence is a
conformance-specific concern.

### 029 consistency

The fixture supplies exact-revision authority reads and an explicit semantic
alias map. Many real systems may not offer that read boundary; the skill requires
confirmation of a supported model rather than assuming this one is available.

A sequential cache refresh does not establish concurrent state/metadata
publication, partition behavior, or any propagation-delay bound.
The unresolved response in the authority-unavailable case is not counted as
successful agreement evidence.
Two matching wrong views remain consistent under their agreement model; their
factual accuracy has not been established.

Post-fix transfer count: 4 tested; 2 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: accuracy, interoperability, accuracy, integrity.
Semantic equivalence overlaps exchange meaning, but here it compares state
representations. Revision relabeling can also be an alteration concern, while
this rule accepts truthful agreement at the declared revision boundary.

### 031 correctness

The specification-grounded discount example exercises finite cases in a pure,
sequential model. It does not establish concurrent coupon redemption, persistence
failures, negative inputs, or other unspecified domains.
An independent expected-result table can still reflect a wrong or disputed
specification; authority resolution remains necessary.

The inclusive/exclusive boundary-testing bullet was moved into Verification
because the same check transfers to predicate-based conformance.
Three Rules of thumb remain rather than adding a replacement to reach a count.
That is below the guide's normal four-to-six range and remains a human-review
point; the retained content covers independent behavioral expectations, joint
output/state obligations, and prohibited-state refusal.

Post-fix transfer count: 3 tested; 1 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: testability, atomicity, robustness.
Independent oracles also support testability, and refusal can support controlled
adverse-state behavior. The retained questions concern the specified functional
result, rather than test seams or generic resilience.

Across the final batch, 23 retained bullets were tested: 14 specific, 9 partly
shared, and 0 transferable unchanged.
Two transferable safeguards were moved into Verification during the pass.
The counts are author judgments, not an independent audit verdict.
Raw samples, matching conditions, unfinished work, and denominator/coverage
safeguards remain in Workflow or Verification.

## Reference and example findings

| Skill | SKILL.md lines | Design guide lines | Worked example lines | Combined lines |
| --- | --- | --- | --- | --- |
| accuracy | 119 | 38 | 77 | 234 |
| certainty | 118 | 36 | 71 | 225 |
| completeness | 118 | 33 | 76 | 227 |
| conformance | 121 | 36 | 77 | 234 |
| consistency | 120 | 38 | 73 | 231 |
| correctness | 117 | 37 | 77 | 231 |

Each design guide has at least three concrete interventions, use-when evidence,
trade-offs, verification, and a short pseudocode sketch.
All guides fit the guide limit; each reference is below the reference limit.
Combined footprints fall within the 200-300 line guideline.

Examples supply initial state, named inputs, expected outputs, a failing case,
remediation, and carried after state.
Accuracy separates fitting from evaluation and includes a rounding failure.
Certainty carries claim, policy, and evidence revisions.
Completeness shows the exact identities hidden by matching counts.
Conformance distinguishes original, repaired, unchecked, and exempted artifacts.
Consistency retains the revision of stale data rather than relabeling it.
Correctness checks both output and the coupon state transition.

These are authored synthetic traces.
The repository tests validate authoring/evaluation tooling; they do not execute
a real sensor, delivery ledger, export pipeline, schema engine, cache, or checkout.
Arithmetic and identity-set differences were sanity-checked separately without
claiming production execution.

## Routing findings

These are author-side description probes, not the blinded routing evaluation.
Six prompts supply a distinguishing fact; six intentionally omit it.
The broad prompts remain unresolved rather than receiving forced skill choices.

| Prompt | Choice | Boundary finding / first question |
| --- | --- | --- |
| Our measured weights differ from the supplied reference values. | accuracy | The prompt supplies a reference-value error question; ask what reference authority and error tolerance apply. |
| The UI says confirmed even when no supporting evidence exists. | certainty | The claim strength exceeds supplied support; ask what evidence warrants each label. |
| The required export set has an item missing but the row count looks right. | completeness | Membership, not count or value accuracy, is the acceptance unit; ask which required-set revision applies. |
| Check every event name against the convention we already selected. | conformance | The convention is supplied rather than being chosen; ask for its actual rules and revision. |
| The detail and list disagree for the same entity and revision. | consistency | Agreement at a shared revision is explicit; ask for the authoritative state and equivalence rule. |
| The function rejects the exact boundary that the specification says to accept. | correctness | An input/output rule is identified; ask which approved specification and boundary values apply. |
| Make this more accurate. | ask | Accuracy / correctness / certainty unresolved: is the concern error against a reference, a specified computation, or confidence in an output? |
| These results look wrong. | ask | Correctness / accuracy / consistency unresolved: wrong against which specification, external reference, or other representation? |
| We need complete results. | ask | Completeness / comprehensiveness unresolved: is there an enumerated required set or missing subject matter in an explanation? |
| Make the outputs consistent. | ask | Consistency / conformance / uniformity unresolved: must values agree, artifacts follow a chosen rule, or presentation match? |
| Can we be sure about this? | ask | Certainty / provability / verifiability unresolved: what claim, evidence, and level of assurance are wanted? |
| Fix our data quality. | ask | No unique batch-15 choice: what concrete mismatch, omission, rule violation, or confidence problem is observed? |

No explicit probe produced an equal-fit pair under the repository's working
boundaries. This reflects the probe design and author judgment, not measured
routing accuracy. The vague probes expose unresolved sibling choices.

## Validation findings

The selected validator passed all six skills.
Full validation passed 96 authored skills, with 18 absent todo skills and no errors.
All 34 repository tests passed.
The skill-creator quick validator passed each new entrypoint.
Additional structural checks found descriptions within the requested length,
real sibling pointers, no new frontmatter status fields, and an explicit
conditional decision in each workflow step.

The maximum word-five-gram body Jaccard involving batch 15 was approximately
0.01315, between certainty and completeness, below the unchanged 0.35 threshold.
This check does not establish semantic distinctness.

The six catalogue statuses and generated index were updated.
Existing skills, evaluation fixtures, scripts, tests, and shared reference files
were not changed. No existing review file was read during authoring.

## Uncertain claims

No external standard obligation, legal duty, tool flag, library version,
statistic, or unverified quotation was introduced.
Quantities and acceptance criteria in the synthetic examples are explicitly
illustrative and require stakeholder confirmation.

The principal unresolved issues are actual reference authority and uncertainty,
a defensible confidence policy, the completeness of the declared universe,
the supplied rule set's applicability, the available coordination model, and
the authority of the behavioral specification.
The fixtures cannot resolve these project-specific decisions.
The proposed boundaries and correctness's three-rule exception remain for human
review, along with the partially shared acceptance distinctions above.
