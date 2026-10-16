# Batch 14 authoring findings

Batch 14 contains ids 19, 38, 56, 58, 83, and 93.
The catalogue now records these six entries as draft.
Four belong to Portability & Interoperability; two belong to Design Structure &
Flexibility. Category membership does not alter their acceptance questions.

## Description and boundary findings

The descriptions were drafted before the bodies and compared with the cluster
boundaries and available sibling descriptions.
Each contains three quoted developer phrases and a nearest-sibling boundary.
No quoted trigger is repeated verbatim in another authored description.
This is a literal phrase check, not evidence of semantic separation.

| Skill | Final description characters | Boundary present in description |
| --- | --- | --- |
| compatibility | 201 | coexistence versus meaningful exchange |
| distributivity | 191 | node allocation versus workload growth curves |
| integratability | 206 | assembly work versus exchange meaning |
| interoperability | 200 | exchange meaning versus assembly effort |
| replaceability | 210 | substitution versus coexistence alone |
| standardizability-standardization-standard | 221 | selection/adoption versus checking selected rules |

The compatibility trigger was narrowed from running two versions to running two
tools because its example demonstrates independent tools sharing settings.
The new descriptions do not promise automatic migration, unrestricted rollback,
or an external compliance result.

The description-first comparison found assembly and exchange separable when the
prompt identifies either glue work or interpretation.
It did not establish a unique route for "connect these systems."
Broad distribution and standardization requests also need clarification.
The final probes below preserve those ambiguities.

## Per-skill weaknesses and post-fix transfer findings

### 019 compatibility

The settings fixture is concrete but covers a dictionary-level collision, not
dependency-loader behavior, process resource conflicts, or simultaneous file
mutation. Those branches remain design considerations requiring repository
evidence. No actual same-product revision matrix has been exercised.

The definition's protected-behavior boundary depends on stakeholder selection.
The illustrative preservation default cannot establish which incidental
standalone outputs a real project must preserve.

Post-fix transfer count: 4 tested; 3 specific, 1 partly shared, 0 transferable.
Nearest siblings in bullet order: integratability, replaceability,
integratability, availability.
The partly shared dependency-resolution practice accepts both consumers'
co-resident needs here; assembly effort is a different acceptance question.

### 038 distributivity

The sequential centralized fixture does not demonstrate a deployed mechanism
that checks assignment and commits effects without an intervening reassignment.
The design guide calls out that missing implementation obligation.
Network partitions, authority failover, and partially copied mutable state remain
outside the demonstrated model.

The local meaning of distributivity still needs human confirmation.
This skill does not establish a general mathematical or standardized definition.

Post-fix transfer count: 4 tested; 2 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: expandability, interoperability,
recoverability, scalability.
Revision-bearing messages overlap exchange design, but this rule accepts
effect-authority enforcement. Checkpoint validation overlaps recovery, but the
movement rule gates a change of active node ownership.

### 056 integratability

The fixture demonstrates a configuration-name mismatch and a bounded composition
edit. It does not measure integration effort across teams, waiting dependencies,
or missing public interfaces. The task ledger must not be promoted to a
calendar-cost prediction.

Clean reconstruction overlaps replicability, and composition boundaries overlap
modifiability. The acceptance boundary remains work required to connect supplied
pieces; a real request may legitimately need those siblings as separate concerns.

Post-fix transfer count: 4 tested; 2 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: modifiability, installability,
interoperability, replicability.
The retained partially shared rules concern expansion of assembly work and
undeclared registration prerequisites, rather than general change cost or
independent reproduction.

### 058 interoperability

The example supplies a pack-to-item conversion and separates queued acceptance
from applied completion. It does not demonstrate field-clearing semantics,
duplicate delivery, fractional conversion, or every participant revision.
Those checks apply only when the actual contract includes them.

A payload capture alone cannot confirm the receiver's effect. The example is an
authored trace, not an execution against independently implemented endpoints.

Post-fix transfer count: 4 tested; 3 specific, 1 partly shared, 0 transferable.
Nearest siblings in bullet order: accuracy, integratability, consistency,
compatibility.
Presence distinctions overlap consistency, but the retained rule accepts the
participants' interpretation of exchanged intent.

### 083 replaceability

The example deliberately confines substitution to reads. New writes are disabled,
so the unchanged snapshot observation does not validate rollback after writes,
online migration, or concurrent cutover. The description stays at substitution
and caller preservation without promising those branches.

Negative-outcome comparison also supports correctness. Its substitution-specific
question is whether existing callers retain their obligations when the old
provider is unavailable. State reconciliation overlaps handoff concerns but
accepts continued caller operations through the replacement here.

Post-fix transfer count: 4 tested; 2 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: correctness, transferability, compatibility,
recoverability.
The retirement and reverse-readability rules require replacement boundaries that
coexistence or generic restoration would not establish.

### 093 standardizability-standardization-standard

The fixture demonstrates a proposed local event vocabulary, not stakeholder
consensus. Its decision state stays proposed even after the synthetic producer
outputs match. The archive exception prevents an all-producers adoption claim.

Resolving names cannot settle domain disagreements without an authoritative
meaning. The example supplies that meaning explicitly and therefore does not
show how to obtain agreement when teams disagree about the underlying concept.

Post-fix transfer count: 4 tested; 2 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: interoperability, uniformity, conformance,
conformance.
Semantic resolution and exception handling overlap other skills, but these rules
accept the choice and adoption scope of a convention, not exchange operation
alone or checking a rule set that was already selected.

Across the batch, 24 retained rules were tested: 14 specific, 10 partly shared,
and 0 transferable unchanged. All six ended with four rules.
Their counts alone provide no evidence of distinctness; the acceptance boundaries
and partially shared limitations above are the relevant findings.
Measurement preservation and comparable starting conditions reside in Workflow
or Verification rather than Rules of thumb.

## Reference footprint and example findings

| Skill | SKILL.md lines | Design guide lines | Worked example lines | Combined lines |
| --- | --- | --- | --- | --- |
| compatibility | 116 | 36 | 83 | 235 |
| distributivity | 116 | 38 | 75 | 229 |
| integratability | 120 | 35 | 74 | 229 |
| interoperability | 118 | 35 | 80 | 233 |
| replaceability | 119 | 36 | 71 | 226 |
| standardizability-standardization-standard | 118 | 38 | 67 | 223 |

Each guide has four evidence/intervention/trade-off/verification decisions and
a short pseudocode sketch. All are below the guide limit; both references per
skill are below the reference limit. Combined footprints fall within the
200-300 line guideline without additional reference files.

The worked examples fill their initial state, named inputs, output criteria,
remediation, after state, and negative branch.
The replacement example's initial missing-record failure was corrected to match
its declared provider outcome interface.
The adoption sketch now explicitly refuses a missing task identity.

The examples are synthetic authored traces, not observed production evidence.
Their before/after outcomes explain the specified local models; they do not
validate a real repository's implementation of the sketches.

## Routing findings

These are author-side description probes, not a blinded test or measured model
accuracy. The vague half intentionally omits the fact needed to distinguish
siblings. A plausible first candidate does not justify a unique final choice.

| Prompt | Best fit or unresolved candidates | First question / finding |
| --- | --- | --- |
| These tools overwrite each other's preferences when both are installed. | compatibility | Which preferences and lifecycle actions must remain independent? Coexistence interference is explicit. |
| A retired worker still writes after its shard moves. | distributivity | Where is current effect authority checked? Node ownership is explicit, not workload growth. |
| The components run alone, but connecting them requires edits throughout both codebases. | integratability | Which supplied interfaces and permitted glue surface define the assembly boundary? |
| The receiver treats packs as individual items. | interoperability | Which unit contract and conversion context do both parties agree to? Interpretation is explicit. |
| Remove the old provider but keep existing callers and records usable. | replaceability | Which caller outcomes and old-state operations must survive retirement? |
| Choose and adopt a common event vocabulary across these producers. | standardizability-standardization-standard | Who selects the convention and which legacy consumers constrain adoption? |
| Make these work together. | ask; compatibility / integratability / interoperability unresolved | Are they interfering on a shared host, difficult to wire, or disagreeing on exchanged information? |
| We need to distribute this. | ask; distributivity / scalability / expandability unresolved | Is the problem assigning ownership, handling growing demand, or admitting added resources? |
| Connect this new service. | ask; integratability / interoperability unresolved | Is the blocker constructing the connection or agreeing on exchanged values and outcomes? |
| Make the integration better. | ask; integratability / interoperability unresolved | What currently fails: assembly work or interaction meaning? |
| We need another backend. | ask; replaceability / compatibility / extensibility unresolved | Will it replace the existing backend, coexist independently, or attach as an additional supported provider? |
| Standardize these. | ask; standardizability-standardization-standard / conformance / uniformity unresolved | Must a convention be selected, an existing convention checked, or peer presentation made consistent? |

Six prompts have an explicit distinguishing fact and six do not.
No explicit probe produced an equal-fit batch-14 pair under the local boundaries.
All six vague probes remain unresolved rather than being counted as successful
single-skill routes. Several candidates outside batch 14 are intentionally named.

## Validation findings

The selected validator checked six skills with no errors.
The full validator checked 90 authored skills, with 24 absent todo skills and
no errors.
All 34 repository unit tests passed using the ordinary test command.
The skill-creator quick validator passed for each new skill.
Additional structural checks found real sibling pointers, three quoted triggers
per description, no status field in the new frontmatter, and conditional
decisions in each workflow step.

The maximum word-five-gram body Jaccard involving batch 14 was approximately
0.01367, between distributivity and replaceability, below the unchanged 0.35
limit. Similarity does not establish semantic originality or correct routing.

Catalogue changes are limited to these six draft statuses, with the index
regenerated. Existing descriptions, evals, scripts, tests, and other skill
bodies are outside the change set.
No existing review file was read during this batch.

## Uncertain claims

No external standard, legal obligation, tool flag, version, or quantitative
performance claim was introduced. Fixture values and acceptance proposals are
explicitly illustrative and require stakeholder confirmation.

Real authority-and-effect enforcement remains unestablished for distributivity.
Actual integration effort remains unmeasured for integratability.
A read-only substitution does not establish write migration or rollback.
The common-convention example does not establish approval or organizational
adoption beyond its declared synthetic outputs.
Compatibility outside the named settings fixture and interoperability outside
the named value/outcome exchange both require further project-specific evidence.
The proposed repository meanings and partially shared rule boundaries remain
the principal human-review questions.
