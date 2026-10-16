# Batch 11 authoring findings

Seven skills are draft: 036 demonstrability, 051 formality, 066 measurability,
076 provability, 082 repeatability, 101 testability, and 110 verifiability.
The required guide, disambiguation map, allowlist, rubric, and approved pilot
entrypoints informed the work. No existing file in reviews/ was read.

Descriptions preceded bodies. Each has three developer-style trigger phrases,
valid sibling pointers, and an explicit exclusion. Complete trigger phrases do
not occur in another current skill description after case folding. This tests
literal duplication, not semantic routing quality.

## Per-skill findings

### 036 demonstrability

The scene covers a simulated payment refusal and a contrasting approval, not a live provider or every payment state. No actual audience replay was performed. Read-only receipts improve inspectability only if the eventual demo runner binds them to the executed scene; that runner is a project implementation obligation.

Scene-artifact provenance was moved into Verification; the redundant narrator-only bullet was replaced with the distinct action-before-consequence showing rule.

Post-fix transfer test on every retained rule: 3 specific,
0 partly shared, 0 transferable.
Nearest siblings in retained-bullet order: `verifiability`, `verifiability`, `verifiability`.


### 051 formality

The cancelled-terminal interpretation is a proposed policy. In particular, rejecting cancellation while running needs stakeholder agreement; the example exposes that decision instead of silently adopting it. The case readings check the proposed vocabulary, not a production state machine or a parser implementation.

Undefined expressions, omitted cells, and semantic versus syntactic precision remain separate decisions.

Post-fix transfer test on every retained rule: 3 specific,
1 partly shared, 0 transferable.
Nearest siblings in retained-bullet order: `provability`, `provability`, `provability`, `provability`.
Stable symbol meanings are also proof premises; this bullet accepts unambiguous notation, not a proved proposition.

### 066 measurability

The clock domain and exact fixture resolution are constructed assumptions. No real collector's precision, overhead, or event coverage was established. Ordinal-to-numeric misuse is discussed as a metric-definition risk but does not have its own worked fixture; the description stays with counting, units, and queue delay.

Unit-expression and resolution safeguards were moved into Verification. Calibration fitness and metric-versus-threshold separation remain measurement-design decisions.

Post-fix transfer test on every retained rule: 3 specific,
1 partly shared, 0 transferable.
Nearest siblings in retained-bullet order: `observability`, `formality`, `observability`, `verifiability`.
Diagnostic signals also need a faithful interval, but this accepts the construct's definition rather than a state explanation.

### 076 provability

The argument is deliberately restricted to sequential mathematical integers and a nonnegative initial state. The finite trace checks support the examples, not the universal conclusion; the separate establishment/preservation argument supplies that model result. Machine arithmetic, concurrency, and correspondence to actual source remain undischarged.

A wording error calling the integer model bounded was corrected to scoped. The initial-state premise, refused transition, and representation limits are explicit.

Post-fix transfer test on every retained rule: 3 specific,
1 partly shared, 0 transferable.
Nearest siblings in retained-bullet order: `verifiability`, `testability`, `formality`, `formality`.
Arithmetic meanings belong to notation too; this bullet limits theorem correspondence and concurrency coverage.

### 082 repeatability

The invoice fixture demonstrates a hidden counter mismatch and a reset remedy, not intrinsic randomness or an independent reconstruction. The proposed rerun count is illustrative and cannot establish universal determinism. Resetting a live global identifier would be outside the example's scope and could invalidate a real carry contract.

Post hoc comparison exclusions were moved into Verification rather than rephrased as a skill-specific rule.

Post-fix transfer test on every retained rule: 2 specific,
1 partly shared, 0 transferable.
Nearest siblings in retained-bullet order: `testability`, `replicability`, `replicability`.
Resetting fixtures supports tests too; here it defines equivalence between whole repeated procedures.

### 101 testability

The deadline example shows construction-time time control, scripted response selection, and semantic outcome discrimination. It does not exercise a real scheduler, live transport, or actual dependency injection framework. The public-input check remains tied to the project's existing input policy; no new rejection policy is invented.

Incidental call-order assertions and normal-construction regression checks were moved into Verification.

Post-fix transfer test on every retained rule: 1 specific,
2 partly shared, 0 transferable.
Nearest siblings in retained-bullet order: `controllability`, `verifiability`, `debuggability`.
Construction boundaries affect safe controls too; this rule makes test time controllable without a live operator override. Semantic distinctions also help inspect failures; here they establish a harness's ability to reject a wrong branch.

### 110 verifiability

The acceptance route concerns a serialized cancellation condition. It cannot decide concurrent cancellation behavior or production log completeness. A prepared acceptance route is explicitly separated from product attainment; no real queue requirement was accepted or marked met.

Missing-evidence handling was moved into Verification. The design sketch was corrected to check final state as well as receipt and dispatch evidence.

Post-fix transfer test on every retained rule: 1 specific,
2 partly shared, 0 transferable.
Nearest siblings in retained-bullet order: `testability`, `demonstrability`, `measurability`.
Test outcomes matter to both; this refuses to substitute code execution coverage for a requirement verdict. Proxy adequacy matters to measures too; this treats unavailable acceptance inputs as a claim-to-evidence feasibility gap.

The retained rules total 24. Demonstrability, Repeatability, Testability,
and Verifiability each retain three rules after shared or redundant material was
removed or moved. This is below the guide's usual four-to-six range and follows
the instruction not to pad to a count. Partly shared verdicts above remain
judgment calls for independent review; zero transferable is an author assessment,
not an independent audit result.

Done items map to distinct evidence: visible scene/result/substitution for
Demonstrability; vocabulary, missing-cell policy, and boundary readings for
Formality; construct, units, calibration, and unresolved pairs for Measurability;
establishment, preservation, premises, and correspondence for Provability;
initial state, carry, comparison, and actual outcomes for Repeatability;
control, branch discrimination, normal construction, and override isolation for
Testability; obtainable inputs, pass/fail/inconclusive rehearsal, and method
versus attainment for Verifiability. Matching item counts alone are not evidence
of either duplication or depth.

## Footprint and description findings

Combined footprint includes the full entrypoint and both directly linked references.
Every body is below the hard maximum; each reference is below 150 lines and each
design guide is below 80. All combined footprints fall within the 200-300 guideline
without treating it as a ceiling.

| Skill | Description characters | Entrypoint lines | Design guide lines | Worked example lines | Combined lines |
| --- | ---: | ---: | ---: | ---: | ---: |
| `demonstrability` | 281 | 114 | 37 | 81 | 232 |
| `formality` | 283 | 116 | 37 | 80 | 233 |
| `measurability` | 280 | 129 | 40 | 76 | 245 |
| `provability` | 284 | 120 | 41 | 80 | 241 |
| `repeatability` | 294 | 120 | 37 | 74 | 231 |
| `testability` | 295 | 124 | 36 | 78 | 238 |
| `verifiability` | 320 | 125 | 46 | 75 | 246 |

Each design guide contains an evidence/intervention/verification decision table,
trade-offs, and a short tool-agnostic sketch. Guide lengths follow the decisions
rather than a common line target. Each worked example names its inputs, expected
outputs, carried state, failing case, remediation, and after result. Examples
are synthetic illustrations, not repository implementation observations.

## Description routing check

This was a manual author check of descriptions against the local cluster
conventions, performed before bodies. The final Verifiability exclusion was
sharpened to “constructing proofs” so it can still select a proof as an acceptance
method without claiming to construct the argument. This is not an independent
blinded routing test or a routing accuracy measurement.

The explicit probes have distinct primary matches. The remaining probes omit
the distinguishing fact; a single winner would overstate what their wording says.

| Prompt | Match or clarification result | Boundary / first question |
| --- | --- | --- |
| Show the audience a declined payment with no charge. | `demonstrability` | Visible scenario outcome; not a universal argument or acceptance-method design. |
| Define whether cancelled is a terminal state in this notation. | `formality` | Meaning of the representation; not proof that implementation follows it. |
| Define the unit and start/end events for queue delay. | `measurability` | Operational measure; not inferring the reason for a stalled queue. |
| Prove a reservation cannot make the balance negative under these integer assumptions. | `provability` | Universal argument with premises; selected tests cannot establish it. |
| Rerun this procedure with the same starting state and runner. | `repeatability` | Held setup; independent reconstruction belongs to replicability. |
| Inject a clock so tests can force the expiration branch. | `testability` | Control seam; acceptance evidence selection is a separate question. |
| Choose feasible evidence for whether this cancellation requirement is met. | `verifiability` | Requirement-to-method binding; no request for new test seams. |
| Make this convincing. | ask; unresolved between sibling concerns | Show a scenario, construct proof, or design acceptance evidence? |
| Make this more precise. | ask; unresolved between sibling concerns | Resolve notation, clarify wording, or define a metric? |
| We need better numbers. | ask; unresolved between sibling concerns | Define a measurement or improve the measured property? |
| Can we guarantee this? | ask; unresolved between sibling concerns | Which claim, assumptions, and kind of evidence are required? |
| It only works sometimes. | ask; unresolved between sibling concerns | Same-setup variation, normal-operation failure, or reconstruction elsewhere? |
| Make this easier to test. | ask; unresolved between sibling concerns | Missing control/observation seam or missing acceptance criterion? |
| How do we know it works? | ask; unresolved between sibling concerns | Which requirement and is the need a demo, tests, or proof? |

The observed ambiguity remains concentrated in vague claims about confidence,
precision, and testing. “Make this easier to test” can lead to Testability when a
seam is missing or Verifiability when the acceptance meaning is absent; neither
distinguishing fact is supplied. “It only works sometimes” can concern
Repeatability, Predictability, or Reliability. No description is treated as a
license to guess those missing facts.

## Validation findings

- Batch validator: seven checked, zero errors.
- Full validator: 70 authored checked, 44 absent todo skills, zero errors.
- Existing test suite: all 34 tests pass; no tests or tooling were changed.
- Skill-creator quick validation: all seven entrypoints pass.
- Read-only authoring assertions check description length, trigger count and
  uniqueness, explicit conditional wording in every workflow step, and reference limits.
- Highest word-five-gram body similarity involving this batch:
  0.013470 between `formality` and `testability`,
  below the unchanged 0.35 validator limit. Low overlap is not semantic originality proof.
- Read-only synthetic checks confirm the measurement arithmetic, reservation
  counterexample and fixed traces, deadline endpoint mutation detection, and
  cancellation pass/fail/inconclusive distinctions. Finite reservation checks
  were not treated as an unbounded proof.
- Catalogue changes are limited to these seven status transitions; the generated
  index reflects them. Earlier skills and the frozen blinded-test files are unchanged.

No Phase 5 evals were authored for these skills. The earlier blinded catalog/key
remains a snapshot of the prior 63 skills; the blinded test was not run here.
The automatic description checker therefore does not yet have complete eval
coverage for the newly authored batch.

## Uncertain claims

No external standards, edition mappings, legal obligations, named library
versions, tool flags, or empirical product statistics were asserted in the new
skills. Numerical fixture values and the proposed rerun count are illustrative
and paired with stakeholder confirmation; mathematical boundaries and unit
definitions are distinguished from operational targets.

The uncertain applicability decisions are the repository's local semantic splits,
the desired cancellation policy, actual instrument precision and clock mapping,
the real procedure's reset/carry boundary, proof-to-code correspondence, and the
evidence access available to the eventual reviewer. Those remain project-context
decisions. Partly shared transfer judgments and manual routing matches require
independent human review. Constructed fixtures do not establish behavior of any
real payment, queue, invoice, or reservation implementation.
