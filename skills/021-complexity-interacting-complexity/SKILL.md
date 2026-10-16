---
name: complexity-interacting-complexity
description: >-
  Maps interaction burden when tickets say "these flags change each other", "callbacks trigger a chain reaction", or "how many paths must we reason about". Not for choosing fewer mechanisms (see simplicity) or locating one execution defect (see debuggability).
---

# Complexity/Interacting Complexity

## Definition and scope

Interaction complexity is the reasoning or coordination burden created by
elements and their dependencies. Describe the concrete paths, shared decisions,
and reachable combinations rather than assigning an unexplained complexity score.
Separate assessing that burden from choosing fewer mechanisms (`simplicity`)
and finding a particular execution defect (`debuggability`).

## Use when / Don't use when

- Apply when flags, callbacks, shared state, or ordering constraints multiply
  the cases a maintainer must reason about.
- Bound the scenario and explain which interactions make it difficult.
- Route a decision to remove unnecessary architecture to `simplicity`.
- Route the impact and effort of one requested edit to `modifiability`.
- Route general cause inspection without an interaction-burden question to
  `analyzability`; do not use this skill as a synonym for all diagnosis.

## Workflow

1. Clarify: Read call paths, event subscriptions, flag definitions, state
   ownership, architecture docs, and scenario tests before specifying.
   Identify the decision a maintainer must reason through.
   If "too complex" names no scenario or burden, then Ask the user which paths,
   combinations, or coordination obligations are obstructing the work.

2. Specify: Record elements, dependency types, supported combinations, reachable
   states, interaction evidence, and the proposed acceptance question.
   If no threshold exists, then propose a labeled illustrative default:
   explain the selected scenario with an explicit path/combination ledger and
   eliminate unexplained reentry obligations; confirm with the user/stakeholder.
   Ask at most three questions on scenario scope, required interactions, and
   acceptable changes before proposing a bounded intervention.

3. Design/Implement: Read [interaction decisions](./references/design-guide.md)
   when addressing feedback, coupled flags, or shared coordination.
   If a cycle is reachable, then identify its activating conditions and actual
   termination rule before changing the callback graph.
   If a dependency merely moves behind a facade, then keep its interaction in
   the ledger; do not claim it disappeared.

4. Verify: Reconstruct the before/after graph and reachable scenario cases under
   the same declared boundary. Check required behavior separately.
   If enumeration is incomplete, then record the unexplored combinations and
   avoid calling the analyzed subset the full interaction space.

5. Report: Return the interaction ledger, evidence of reachable paths, changed
   obligations, preserved behavior, and unresolved cases.
   If only a structural proxy was counted, then name that proxy and withhold
   claims about actual human reasoning time or general defect reduction.

## Specification patterns

- **Interaction explanation:** For `{scenario_and_supported_combinations}`,
  `{analysis_artifact}` shall identify `{dependencies_shared_decisions_and_cycles}`
  with `{reachability_evidence}`, verified by `{code_and_scenario_crosscheck}`.
- **Burden reduction:** Changing `{interaction_boundary}` shall remove
  `{specified_reentry_or_coordination_obligation}` while preserving
  `{required_behavior}`, checked using `{before_after_case_ledger}`.

Use the illustrative scenario-ledger proposal in Specify when no number is given;
confirm with the user/stakeholder before making it an acceptance gate.

## Rules of thumb

- Distinguish possible dependency edges from reachable interaction paths; a flag
  combination can make a syntactic cycle irrelevant or activate a hidden one.
- Track callback reentry separately from call count; repeated entry can introduce
  a termination obligation that a shorter static graph conceals.
- Keep shared decisions visible across module boundaries; moving a dependency
  behind a facade does not remove the need to coordinate that decision.
- Do not equate fewer branches with a smaller supported state space; independent
  choices and cross-choice constraints determine the cases that need reasoning.

## Verification

Use dependency inspection, bounded state exploration, and scenario traces.
Name the graph boundary, edge meanings, and observation procedure.
Keep unsupported, unreachable, untested, and failed combinations distinct.
Retain raw traces and the same starting state for before/after cases.
Cross-check dynamic edges with source subscriptions and callback registration.
Check the actual termination or refusal outcome for reachable feedback.
Use static scores only as named proxies with stated limitations.

## Done checklist

- [ ] Define the scenario and the reasoning or coordination question.
- [ ] Inventory dependency types and shared decisions.
- [ ] Enumerate supported combinations and unexplored cases.
- [ ] Establish reachability for the interactions being reported.
- [ ] Explain termination obligations for any reachable feedback.
- [ ] Compare changed interaction obligations against preserved behavior.
- [ ] Bound conclusions to the analyzed graph and evidence.

## Failure modes

- Calling a large file complex without identifying an interaction.
- Treating every syntactic combination as reachable.
- Hiding dependencies behind a facade and claiming the burden vanished.
- Reporting a lower proxy score as measured human understanding.

## References

- Read [interaction decisions](./references/design-guide.md) when choosing
  interventions for feedback, coupled choices, and coordination.
- Read [callback/flag example](./references/worked-example.md) when mapping
  reachable interactions before claiming a reduced reasoning obligation.
