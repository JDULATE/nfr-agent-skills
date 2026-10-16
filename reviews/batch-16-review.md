# Batch 16 authoring findings

Batch 16 contains ids 21, 22, 34, 45, 91, and 94 under
Design Structure & Flexibility. All six catalogue entries are draft.

## Description-first findings

Descriptions were written before bodies and compared with the repository's
proposed sibling boundaries. Available descriptions for additivity,
integratability, conciseness, formality, analyzability, and modifiability were
also inspected. The remaining unauthored siblings were compared through the
disambiguation map rather than invented descriptions.

| Skill | Description characters | Acceptance boundary in the description |
| --- | --- | --- |
| complexity-interacting-complexity | 258 | interaction burden versus choosing fewer mechanisms or locating one execution defect |
| composability | 256 | combined behavior versus assembly effort or summed contributions |
| decomposability | 266 | separable responsibilities versus organizing dependencies or joining parts |
| expressiveness | 277 | missing representable distinctions versus brevity or interpretation precision |
| simplicity | 296 | unnecessary mechanisms versus interaction analysis or reading flow |
| structuredness | 278 | dependency organization versus separability or matching peer conventions |

Each description has three quoted developer phrases and real catalogue pointers.
No quoted trigger phrase is repeated verbatim in another authored description.
That literal check does not establish semantic routing precision.

The pre-body comparison distinguished an explicit ownership failure in a joined
pipeline from excessive integration work. It also separated a forbidden
dependency direction from the ability to run extracted responsibilities.
Broad architecture requests did not provide enough evidence for unique routing;
the final probes retain those ambiguities.

## Per-skill weaknesses and post-fix transfer findings

### 021 complexity-interacting-complexity

The callback fixture explores only the declared flag values and subscriptions.
It uses a repeated-state inspection guard to expose reachable reentry; it does
not establish how a real unbounded or asynchronous execution terminates.
The changed notification order is explicitly permitted by the fixture, not a
general recommendation.

Removing the modeled reentry obligation is not a measurement of human reasoning
time, overall system complexity, or defect reduction.
The qualitative acceptance proposal needs a stakeholder to identify which
reasoning or coordination question actually matters.

Post-fix transfer count: 4 tested; 1 specific, 3 partly shared, 0 transferable.
Nearest siblings in bullet order: structuredness, debuggability, decomposability,
simplicity.
Reachability also informs graph checks; reentry can aid defect investigation;
shared decisions affect split boundaries. Here those practices explain the
interaction obligations a maintainer must reason about, rather than accepting
organized edges, a localized defect, or separable parts.

### 022 composability

The borrowed-stream example is synchronous and supplies the stage contracts.
It does not demonstrate retries, cancellation, concurrent writers, or automatic
error propagation in a particular programming language.
The pseudocode lifetime wrapper is deliberately not a complete error envelope.

The example preserves a primary stage failure and reports failed cleanup
separately. It does not claim that a failed close finalized the stream.
The order-independence warning has no worked commutativity example; the description
therefore promises shared lifetime and error behavior, not arbitrary reordering.

Post-fix transfer count: 4 tested; 2 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: integratability, replaceability, additivity,
operability.
Assumption matching helps assembly too, and preserved failure reporting helps
operations. The retained questions concern the behavior of the actual joined
chain, including incompatible stage lifetime obligations.

### 034 decomposability

The example separates a calculation from rendering through inert data.
It does not establish a remote-service boundary or a split across a transaction
or shared mutable invariant.
The design guide keeps unsupported coordination under an existing owner rather
than assuming a process boundary solves it.

Independent fixtures can still hide coupling in a supposedly inert wrapper.
The worked mutant exposes that issue, but real boundary types and constructors
need project inspection. A successful extraction does not show that every
responsibility should be deployed independently.

Post-fix transfer count: 4 tested; 1 specific, 3 partly shared, 0 transferable.
Nearest siblings in bullet order: structuredness, modifiability, atomicity,
testability.
Explicit data also reduces change coupling, invariant ownership overlaps state
coordination, and private-state fakes affect tests. The accepted result here is
independent execution of the responsibility without its neighbor's internals.

### 045 expressiveness

The policy example demonstrates only the supplied subject relation and negative
forms. It does not establish a complete policy language or secure enforcement.
Owner-only behavior is evaluated under an explicit no-inherited-rule context;
the separate inherited-allow context demonstrates denial versus no-decision.
Changing the combining policy can change effective permission.

The generic distinguishing-input test was moved from Rules of thumb into
Verification. Three rules remain rather than adding filler to reach the normal
four-to-six range. That count exception remains for human review.

Post-fix transfer count: 3 tested; 2 specific, 1 partly shared, 0 transferable.
Nearest siblings in bullet order: formality, configurability, composability.
Denial/no-decision combination semantics overlap composition, but the retained
rule preserves the ability to state distinct intentions through the notation.
An interpreter that ignores a retained tag still fails that capability.

### 091 simplicity

The fixed-export ledger explicitly has no required runtime extension surface
and no registered lifecycle effects. Those supplied facts justify the modeled
removal; an apparently unused registry in a real project may have external
consumers or accepted future obligations.
The example cannot establish that a direct call is generally preferable.

Removing the writer is a failing reduction candidate despite returning the right
text. Preservation of lifecycle effects was moved into Verification because that
safeguard transfers to other architecture changes.
Three mechanism-specific rules remain, below the usual guide range; no replacement
was added solely to restore the count.

Post-fix transfer count: 3 tested; 2 specific, 1 partly shared, 0 transferable.
Nearest siblings in bullet order: flexibility, extensibility,
complexity-interacting-complexity.
A confirmed extension obligation can justify the machinery, but the question here
is whether retaining speculative selection mechanisms serves the accepted purpose.
A facade retaining the same unused dispatch has not met the removal objective.

### 094 structuredness

The graph fixture supplies local role rules rather than a universal architecture.
Its static repair removes an explicit domain-to-delivery edge and cycle while
preserving the named request result.
The callback mutant shows why that result cannot establish all runtime edges.

The generic post-move dependency inspection was moved to Verification.
Three rules remain, so the normal four-to-six range is another human-review
point. The retained rules concern translation role, edge-type organization,
and precise relationship exceptions.

Post-fix transfer count: 3 tested; 1 specific, 2 partly shared, 0 transferable.
Nearest siblings in bullet order: decomposability,
complexity-interacting-complexity, conformance.
The translation location obeys a selected direction rule that separability alone
would not require. Dynamic cycles also matter to interaction analysis, and
exception scoping overlaps checking selected rules, but the accepted boundary
here remains the organization of actual dependencies.

Across the final batch, 21 retained rules were tested: 9 specific, 12 partly
shared, and 0 transferable unchanged.
Three transferable verification practices were moved out of Rules of thumb.
The partially shared verdicts are author judgments about acceptance boundaries,
not an independent audit result.

## Reference footprint and example findings

| Skill | SKILL.md lines | Design guide lines | Worked example lines | Combined lines |
| --- | --- | --- | --- | --- |
| complexity-interacting-complexity | 115 | 38 | 70 | 223 |
| composability | 116 | 39 | 80 | 235 |
| decomposability | 115 | 35 | 78 | 228 |
| expressiveness | 115 | 36 | 74 | 225 |
| simplicity | 116 | 35 | 76 | 227 |
| structuredness | 118 | 38 | 75 | 231 |

Every guide includes evidence/intervention/trade-off/verification decisions and
a short pseudocode sketch. Each has at least three concrete interventions.
All guides and references meet their limits, and combined footprints fall within
the 200-300 line guideline.

Each worked example fills its initial state, named inputs, failing outcome,
remediation, after outputs, and carried state.
The examples include a callback reattachment, premature stream close, live
private-state wrapper, lost policy tag, dropped writer effect, or forbidden
runtime callback as concrete negative controls.

These are synthetic authored traces. The repository tests check tooling, not
production implementations of these designs.
Additional in-memory checks sanity-checked the illustrative flag outcome table,
invoice arithmetic, local policy evaluations, and listed graph edge removal.
They do not independently establish the trace semantics or deployment behavior.

## Routing findings

These are author-side description probes, not a blinded model evaluation.
Six prompts provide a distinguishing fact and six omit it.
Vague requests remain unresolved rather than receiving forced routes.

| Prompt | Choice | Boundary finding / first question |
| --- | --- | --- |
| These flags alter each other's effects; map the combinations and decisions they create. | complexity-interacting-complexity | Which flag values and interaction paths must be explained? The requested acceptance unit is interaction burden. |
| Each pipeline stage works alone, but chaining them changes who closes the stream. | composability | What lifetime and result obligations must the assembled pipeline preserve? This is combined behavior, not glue effort. |
| Extract rendering from billing so each runs without the other's private state. | decomposability | Which responsibilities, state owners, and boundary data must become independent? |
| Our policy format cannot distinguish owner-only access from access by everyone. | expressiveness | Which domain distinctions and evaluation meanings must the notation represent? |
| This fixed export uses a registry and plugin lifecycle although only the fixed formatter is required. | simplicity | Which retained requirements actually need those mechanisms? Candidate removal must preserve the fixed export. |
| Domain modules import the HTTP adapter despite the chosen layer rule. | structuredness | What are the permitted dependency directions and actual imported edges? |
| Simplify this architecture. | ask | Simplicity / complexity-interacting-complexity / decomposability unresolved: remove unneeded mechanisms, map interaction burden, or establish separable parts? |
| Make this modular. | ask | Decomposability / structuredness / composability unresolved: separable responsibilities, dependency organization, or behavior after assembly? |
| This pipeline is a mess. | ask | Composability / complexity-interacting-complexity / readability unresolved: what fails in combined execution, interaction reasoning, or reading flow? |
| Improve our rule language. | ask | Expressiveness / conciseness / formality unresolved: is meaning missing, notation verbose, or interpretation precision undefined? |
| Clean up these packages. | ask | Structuredness / simplicity / readability unresolved: are imports violating a declared rule, mechanisms unnecessary, or source hard to follow? |
| Split this service. | ask | Decomposability / distributivity / scalability unresolved: separate responsibilities, assign execution across nodes, or handle growing demand? |

No explicit probe produced an equal-fit pair under the working boundaries.
That is an author judgment over selected probes, not measured routing accuracy.
The vague probes identify unresolved sibling sets and the information needed
before choosing a skill.

## Validation findings

Selected validation passed all six skills.
Full validation passed 102 authored skills, with 12 absent todo skills and no errors.
All 34 repository tests passed.
The skill-creator quick validator passed every new entrypoint.
Additional structural checks found descriptions within the requested length,
three quoted phrases each, real sibling pointers, no new frontmatter status fields,
and a conditional decision in every workflow step.

The largest body word-five-gram Jaccard involving batch 16 was approximately
0.01616, between completeness and composability, below the unchanged 0.35 limit.
Low textual similarity does not demonstrate distinct acceptance decisions.

The catalogue and generated index changed only for the six batch statuses.
Other skill content, evaluation files, scripts, tests, and shared reference files
were not changed. No existing review file was read during authoring.

## Uncertain claims

No external standard obligation, legal assertion, tool flag, version, statistic,
or unverified quotation was introduced.
Fixture values, role rules, and acceptance defaults are labeled illustrative and
require stakeholder confirmation.

The unresolved project questions are the actual supported interaction space,
join ownership and failure contracts, state invariants at proposed split
boundaries, required language meanings, consumers of candidate mechanisms, and
the intended dependency organization.
No fixture settles those decisions for an unrelated system.

Human review remains necessary for the proposed sibling boundaries, the partly
shared rules, and the three-rule exceptions in expressiveness, simplicity, and
structuredness. The examples establish neither general complexity reduction
nor secure policy enforcement, independent deployment, or maintenance savings.
