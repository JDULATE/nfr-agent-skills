---
name: provability
description: >-
  Proves modeled claims when asked "prove the balance invariant", "check every allowed transition", or "list proof assumptions". Ask the user if proof vs selected test evidence is unclear. Not for testing selected cases (see verifiability) or defining notation alone (see formality).
---

# Provability

## Definition and scope

Provability means a precise claim follows from explicit assumptions through a
checkable argument. Construct the model, obligations, and argument that establish
the claimed scope; distinguish defining the notation (`formality`) and gathering
selected acceptance evidence (`verifiability`) from proving the proposition.

## Use when / Don't use when

- Apply when the user requests an invariant or a claim over all modeled states.
- Apply when a proof depends on hidden arithmetic, environment, or transition assumptions.
- Route representative executions without a universal argument to `verifiability`.
- Route undefined symbols or an unsettled model language to `formality`.
- Route a capability showing for an audience to `demonstrability`.

## Workflow

1. Clarify: Inspect implementation branches, data types, state transitions, existing
   assertions, and requirement docs before stating a theorem.
   Identify the requested proposition and the actual code boundary it concerns.
   If "guarantee" lacks a state space or assumptions, then Ask the user whether
   the need is formal assurance, selected checks, or a narrower engineering claim.

2. Specify: Write the proposition, quantified inputs, initial states, transition
   relation, assumptions, and representation-to-code mapping.
   If scope is absent, then propose labeled illustrative defaults: a sequential
   mathematical-integer reservation model and a nonnegative-balance invariant;
   confirm with the user/stakeholder before treating that model as sufficient.
   List implementation arithmetic and concurrency as separate open obligations.

3. Design/Implement: Read [proof construction](./references/design-guide.md)
   when selecting an invariant, exposing a missing premise, or repairing a guard.
   If a reachable counterexample exists, then preserve it and repair the transition
   or revise the agreed claim. If an argument needs a new assumption, then show
   who must establish it instead of silently adding it.
   If production arithmetic or interleaving differs from the model, then expand
   the model or narrow the theorem's implementation coverage explicitly.

4. Verify: Check initial-state establishment, preservation for every modeled
   transition, and the argument's link to the actual proposition.
   If a proof attempt is incomplete, times out, or covers a smaller model, then
   record that outcome rather than converting it into a successful proof.
   Read [reservation example](./references/worked-example.md) when separating a
   valid integer argument from unsupported concurrency or machine-arithmetic claims.

5. Report: Return the theorem, premises, obligation outcomes, counterexamples,
   implementation mapping, and unresolved correspondence gaps.
   If the assumptions are not established for the implementation, then report a
   conditional model result rather than a proved product guarantee.

## Specification patterns

- **Invariant:** Under `{explicit_assumptions}`, every state reachable from
  `{initial_states}` through `{modeled_transitions}` shall satisfy
  `{invariant}`, established by `{checkable_argument_and_obligations}`.
- **Correspondence:** A proof for `{model_revision}` shall apply to
  `{implementation_revision_and_boundary}` only under
  `{validated_representation_and_environment_mapping}`; unresolved mappings
  shall be reported as `{excluded_implementation_claims}`.

For missing scope, use the illustrative scoped model proposal in Specify and
confirm with the user/stakeholder. Never choose a numeric proof bound and present
it as coverage of an unbounded system.

## Rules of thumb

- Do split invariant establishment from preservation; checking only transitions
  cannot prove that an allowed initial state already satisfies the proposition.
- Do discharge the rejected-action branch as well as the successful branch;
  an invariant proof must account for every modeled transition's next state.
- Don't add a convenient premise merely to close an obligation; expose whether
  that premise is enforced by code, supplied by the environment, or still assumed.
- Do bind the theorem to its arithmetic and interleaving model; a sequential
  integer proof does not silently cover overflowing values or concurrent updates.

## Verification

Use proof review, symbolic reasoning, model exploration, and theorem-checking
categories only where the repository actually supports them.
Check each quantifier's domain, each premise, every transition case, and the
conclusion being established. Retain the model and implementation revisions.
Use counterexample traces to show an obligation failure, not just a solver label.
Record incomplete exploration, resource limits, and undischarged obligations.
Review the code/model mapping separately from the mathematical argument.
A successful bounded search excludes counterexamples only in its explored model;
passing example tests does not discharge a universal obligation.

## Done checklist

- [ ] State the proposition with explicit quantified domains.
- [ ] Identify initial states and every modeled transition branch.
- [ ] Separate enforced premises from environmental assumptions.
- [ ] Establish the invariant in each permitted initial state.
- [ ] Discharge or record the preservation obligation for each branch.
- [ ] Preserve any counterexample and its model revision.
- [ ] Inspect arithmetic and concurrency correspondence with the code.
- [ ] Limit the reported theorem to discharged obligations and established premises.

## Failure modes

- Proving a weaker proposition than the requirement while reporting the original claim.
- Adding a premise that excludes the observed bug without enforcing that premise.
- Treating bounded model exploration as an unbounded theorem.
- Applying mathematical-integer reasoning to unchecked machine arithmetic.
- Reporting a model proof as implementation proof without a correspondence argument.

## References

- Read [proof construction](./references/design-guide.md) when choosing obligations,
  repairing a failed transition, or deciding whether a premise is legitimate.
- Read [reservation example](./references/worked-example.md) when checking a small
  invariant and identifying exactly which implementation claims remain outside it.
