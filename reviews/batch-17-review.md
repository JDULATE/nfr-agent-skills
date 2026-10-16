# Batch 17 authoring findings

Batch 17 contains ids 53, 85, 107, 109, 111, and 114 under
Design Structure & Flexibility. All six catalogue entries are draft.

## Description-first findings

The six descriptions were drafted before bodies and compared against their
cluster boundaries. The comparison also used the authored descriptions of
composability, expressiveness, structuredness, convention adoption,
configurability, reconfigurability, replaceability, and integratability.

| Skill | Description characters | Boundary stated in the description |
| --- | --- | --- |
| generality | 324 | family abstraction versus distinct roles or contextual reuse |
| reusability | 280 | use in another context versus family coverage or joining contracts |
| uniformity | 314 | conventions across comparable peers versus selection or value agreement |
| variability | 289 | product-family combinations versus instance settings or transitions |
| versatility | 305 | distinct roles versus related cases or reuse elsewhere |
| wrappability | 325 | retained implementation behind a new boundary versus substitution or wiring |

Each description has three quoted developer phrases.
No quoted phrase is repeated verbatim in another authored description.
Literal trigger uniqueness is not evidence of semantic routing precision.

The pre-body probes distinguished interval-family coverage from running an
existing checker in a new context, and product-role diversity from product-family
feature combinations. They also distinguished retaining a native engine from
substituting it. Broad requests remained unresolved; the routing findings below
retain those ambiguities.

Every described branch has a corresponding filled example.
The descriptions stay with numeric interval cases, web/CLI checker reuse, paging
peers, build variants, inventory import/audit, and a structured retained-engine
boundary rather than promising arbitrary generalization or deployment behavior.

## Per-skill weaknesses and post-fix transfer findings

### 053 generality

The family is deliberately limited to finite numeric interval predicates with
matching units and supplied bounds.
The example does not establish date ordering, unit conversion, arbitrary
predicates, or coverage of every numeric representation.
Contrasting examples support the proposed abstraction; they are not a proof of
all future family members.

Source inspection remains necessary because a caller can conceal per-member
redesign while the common evaluator passes its value fixtures.
The declared family also needs stakeholder agreement; a flexible field name
alone does not establish that unrelated operations belong together.

Post-fix transfer count: 4 tested; 2 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: expressiveness, correctness, versatility,
reusability.
Variation data also expresses distinctions, and stable operation meanings also
support correctness. The accepted unit here is coverage of a related family
without another named-case redesign.

### 085 reusability

The fixture demonstrates explicit row input and shared checker identity across
synthetic web and CLI adapters. It does not validate real framework packaging,
distribution, authorization, or measured adaptation effort.

A matching CLI result can still come from copied logic; the example therefore
checks artifact identity separately from output.
The authority safeguard was moved into Verification because protecting caller
policy is not a reuse-specific rule.
Three Rules of thumb remain, below the guide's usual four-to-six range; no
replacement was added just to restore a count.

Post-fix transfer count: 3 tested; 1 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: integratability, composability, generality.
Explicit dependencies and consumer-owned adapters help other concerns too.
Here their acceptance question is whether the same artifact runs in the named
new context without recreating its original ambient dependency.

### 107 uniformity

The comparable peer set covers two list operations and their selected paging
convention only. It does not establish consistency of returned business values,
selection of a convention, or adoption across unrelated interfaces.

The byte-budget operation is explicitly outside the item-count peer set.
Its buffer is supplied as numeric bytes, avoiding an unstated text-encoding
assumption. The example does not generalize byte counting to text encoding.

An exception reminder duplicating the comparability boundary was deleted.
Three retained rules address grouping, actual implementation, and canonical alias
behavior rather than padding back to the normal guide range.

Post-fix transfer count: 3 tested; 1 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: consistency, conformance,
standardizability-standardization-standard.
Handler checks overlap rule conformance, and aliases affect convention adoption.
The retained question is alignment across an already selected comparable peer
set, including equivalent operation meaning.

### 109 variability

The model completely lists the bounded selection space, but the worked example
provides artifact traces only for the named derivation cases.
The validity table is not evidence that every real build has executed.
A separate in-memory constraint check confirms the supplied model has sixteen
selections and nine valid ones; these are fixture counts, not engineering targets.

The implication-direction bullet was moved into Verification because the same
logical safeguard applies to instance configuration.
Three remaining rules concern the product derivation boundary, binding stage,
and selected-feature artifact evidence. This is another count exception requiring
human review, not an attempt to fill a fixed shape.

Post-fix transfer count: 3 tested; 1 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: conformance, reconfigurability, functionality.
Prechecking constraints and verifying capability presence overlap those siblings,
but the accepted result is a valid selected family member and its derived artifacts.

### 111 versatility

The distinct import and audit roles run in one synthetic product.
The fixture covers sequential role use and an explicit key set only.
It does not define concurrent audit/import, missing-key behavior, or all stock
workflows.

Read-only audit is a declared task obligation, not a claim that a real access
control mechanism enforces it.
The stale import-flag mutant shows the state effect a role switch must avoid,
but real context propagation still needs implementation evidence.

Post-fix transfer count: 4 tested; 2 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: functionality, correctness, reusability,
reconfigurability.
State effects and context handoff also matter elsewhere. The accepted distinction
here is separate task outcomes within one product, rather than operation count,
contextual reuse, or a runtime configuration transition alone.

### 114 wrappability

The native reservation component is retained unchanged in the model.
The wrapper comparison covers local synchronous results, rejection, faults,
invalid input, unsupported mode, and duplicate-effect detection.
It does not establish remote delivery, ambiguous-completion recovery,
cancellation, or safe automatic retry.

Review found that insufficient-stock rejection needed its own mapping.
The final sketch distinguishes it from missing items and engine faults, and
unknown native outcomes remain unresolved instead of becoming success.

Post-fix transfer count: 4 tested; 2 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: interoperability, replaceability, reliability,
extensibility.
Outcome meanings overlap exchange contracts and retries affect failure behavior.
The accepted boundary here is preservation of the retained native operation's
meaning and effect through a new interface, not substitution or new behavior.

Across the final batch, 21 retained rules were tested: 9 specific, 12 partly
shared, and 0 transferable unchanged.
Two transferable safeguards were moved into Verification and one repeated
exception reminder was deleted.
These are author judgments, not an independent audit.
Reusability, uniformity, and variability each retain three rules as explicit
exceptions to the usual guide range.

## Reference footprint and worked-example findings

| Skill | SKILL.md lines | Design guide lines | Worked example lines | Combined lines |
| --- | --- | --- | --- | --- |
| generality | 117 | 34 | 71 | 222 |
| reusability | 116 | 37 | 73 | 226 |
| uniformity | 116 | 33 | 66 | 215 |
| variability | 117 | 36 | 80 | 233 |
| versatility | 115 | 34 | 74 | 223 |
| wrappability | 120 | 42 | 69 | 231 |

Each guide has at least three concrete evidence-to-intervention-to-verification
decisions, trade-offs, and a short pseudocode sketch.
All guides and references meet their respective limits.
Combined footprints fall within the 200-300 line guideline without extra files.

Worked examples supply named inputs, initial state, failing outputs, remediation,
after outputs, and carried state. Negative controls expose displaced named-case
branches, copied checker identity, a handler ignoring its parser, omitted derived
features, audit mutation, and duplicate native reservations.

The examples are synthetic authored traces, not production observations.
The repository tests exercise authoring and evaluation tooling.
Additional sanity checks cover bounded feature validity, stock arithmetic,
explicit byte-prefix selection, and empty-name fixture selection; they do not
independently execute the documented end-to-end systems.

## Routing findings

These are author-side description probes, not the blinded routing evaluation.
Six prompts provide a distinguishing fact and six intentionally omit it.

| Prompt | Choice | Boundary finding / first question |
| --- | --- | --- |
| Use one interval abstraction for quantity and duration instead of a branch per field. | generality | Which related cases and operations define the family, and what must work without a new case-specific branch? |
| Run the existing import validator from a CLI without constructing a web request. | reusability | What new context, allowed adapters, and dependency changes bound reuse of the existing artifact? |
| These comparable list routes use different names for the same page-size argument. | uniformity | Which selected peer convention applies, and do the parameters actually have the same meaning? |
| Prevent building a product variant with export enabled and audit disabled. | variability | What feature implication and product-family boundary should the variant model enforce? |
| The same inventory tool must import records and audit discrepancies without changing stock during audit. | versatility | What separate results and state effects define acceptance for each role? |
| Expose a structured API while leaving the legacy reservation implementation in place and unchanged. | wrappability | Which original results, failures, and effects must the new boundary preserve? |
| Make this more generic. | ask | Generality / reusability / expressiveness unresolved: cover a case family, use an artifact elsewhere, or express a missing distinction? |
| We want to reuse this. | ask | Reusability / generality / composability unresolved: in what new context, or is the request about abstraction coverage or assembly? |
| Make these interfaces consistent. | ask | Uniformity / consistency / standardizability-standardization-standard unresolved: align peer conventions, agree on values, or select a convention? |
| Support more variants. | ask | Variability / configurability / extensibility unresolved: product-family combinations, instance settings, or added behavior through a hook? |
| Let this tool do more. | ask | Versatility / functionality / augmentability unresolved: which distinct roles or separately accepted capability must it serve? |
| Put an adapter here. | ask | Wrappability / integratability / replaceability unresolved: retain an implementation behind a new boundary, connect pieces, or substitute an implementation? |

No explicit probe produced an equal-fit pair under the proposed boundaries.
The vague prompts remain unresolved sibling sets rather than successful forced
routes. Selected probes and author judgment do not establish model accuracy.

## Validation findings

Selected validation passed all six skills.
Full validation passed 108 authored skills, with 6 absent todo skills and no errors.
All 34 repository tests passed.
The skill-creator quick validator passed all six entrypoints.
Structural checks found descriptions within the requested limit, three quoted
phrases each, real sibling pointers, no new frontmatter status fields, and an
explicit conditional decision in each workflow step.

The maximum body word-five-gram Jaccard involving batch 17 was approximately
0.02059, between uniformity and wrappability, below the unchanged 0.35 threshold.
This detects copied wording, not semantic duplication or routing quality.

Only the six selected catalogue statuses and generated index entries changed
outside the new skill files and this review.
Existing skill content, eval fixtures, scripts, tests, and shared references
were not edited. No existing review file was read during authoring.

## Uncertain claims

No external standard obligation, legal assertion, library version, tool flag,
statistic, or unverified quotation was introduced.
Fixture values and acceptance proposals are labeled illustrative and require
stakeholder confirmation.

Project-specific decisions remain unresolved: the intended abstraction family,
allowed reuse adaptation, comparable peers and convention authority, actual
product-family constraints and binding stage, distinct role obligations, and
the native behavior a wrapper must preserve.
The fixtures cannot settle those questions for an unrelated project.

Human review remains necessary for partially shared rule boundaries, vague
routing, and the three-rule exceptions in reusability, uniformity, and variability.
No claims of universal generality, zero-cost reuse, broad convention adoption,
safe live variant transitions, concurrent roles, or remote wrapper guarantees
follow from these examples.
