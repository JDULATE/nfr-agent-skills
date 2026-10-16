---
name: replaceability
description: >-
  Preserves surrounding contracts during substitution when tickets say "swap this provider", "remove the old backend", or "keep callers unchanged after replacement". Not for coexistence alone (see compatibility).
---

# Replaceability

## Definition and scope

Replaceability means substituting one component for another while preserving
specified obligations of the surrounding system. Identify callers, persisted
state, error behavior, and the point at which the old implementation is retired.
Separate substitution from coexistence (`compatibility`) and adapting a boundary
around an implementation that remains in use (`wrappability`).

## Use when / Don't use when

- Apply when changing a provider or backend must preserve existing callers and
  the meaning of previously stored state.
- Include the old implementation's removal, not merely a side-by-side comparison.
- Route independent co-resident operation to `compatibility`.
- Route adding an adapter without replacing the underlying component to
  `wrappability`; an adapter may also be part of a larger substitution.

## Workflow

1. Clarify: Inspect caller interfaces, adapters, stored-state formats, error
   handling, dependency configuration, and cutover docs before specifying.
   Enumerate obligations callers rely on, including negative outcomes.
   If "swap provider" lacks a retirement boundary, then Ask the user what must
   stop depending on the old implementation and which state must remain usable.

2. Specify: Define the substitution boundary, preserved obligations, permitted
   differences, state mapping, cutover preconditions, and rollback limitations.
   If no acceptance target exists, then propose a labeled illustrative default:
   unchanged caller contracts and named old-state reads after old dependency
   removal; confirm with the user/stakeholder.
   Ask at most three grouped questions covering obligations, state/migration,
   and cutover permissions before beginning reversible adapter work.

3. Design/Implement: Read [substitution decisions](./references/design-guide.md)
   when choosing contract adapters, state conversion, or a cutover gate.
   If the new provider exposes different errors, then translate them into the
   preserved caller contract or obtain approval for the changed obligation.
   If new writes cannot be read by the old provider, then mark rollback blocked
   after those writes unless a verified reverse migration is available.

4. Verify: Compare old and new implementations with contract fixtures and
   inspect migrated state; run callers with the old dependency absent.
   If side-by-side checks pass but retirement was not exercised, then leave
   completed substitution unverified.

5. Report: Show the obligation comparison, mapping changes, state reconciliation,
   old-dependency removal check, and the verified cutover boundary.
   If rollback has only been described, then report it as unverified rather than
   promising reversibility after new-format state is created.

## Specification patterns

- **Caller preservation:** Replacing `{old_component}` with `{new_component}`
  shall preserve `{caller_inputs_outputs_and_errors}` for `{cases}`, verified
  by `{contract_comparison_with_old_dependency_absent}`.
- **State continuity:** After `{state_mapping_and_cutover}`, `{existing_records}`
  shall remain usable through `{preserved_caller_operations}`, subject to
  `{approved_differences}`, checked by `{reconciliation_and_negative_cases}`.
- **Retirement gate:** The old dependency shall be retired only after
  `{contract_and_state_evidence}`; reversal shall be permitted only within
  `{verified_reverse_mapping_boundary}`.

For absent targets, use the illustrative preservation proposal in Specify;
confirm with the user/stakeholder before treating it as accepted.

## Rules of thumb

- Preserve negative caller outcomes as well as successful values; replacing a
  missing-record result with an exception can break callers despite matching reads.
- Reconcile old state through the caller's operations, not only record counts;
  equal totals can conceal a replacement that no longer resolves existing keys.
- Exercise the replacement with the old dependency unavailable; a fallback to the
  old provider hides an incomplete substitution.
- Gate rollback on the readability of post-cutover writes by the old component;
  retaining its executable does not make a reverse substitution possible.

## Verification

Use contract comparison, state migration rehearsal, dependency-removal tests,
and controlled cutover categories.
Compare actual values and negative outcomes for the named callers.
Preserve mismatches rather than filtering them from a favorable aggregate.
Inspect configuration and runtime paths for fallback to the old provider.
Check old-state lookup and new-state behavior separately.
Test reversal only in an isolated fixture using the actual reverse-state path;
do not infer it from a feature switch or a saved old deployment.

## Done checklist

- [ ] Identify callers and explicitly preserved obligations.
- [ ] Compare successful and negative contract outcomes.
- [ ] Validate state mapping through existing-key operations.
- [ ] Check approved differences separately from regressions.
- [ ] Run the named callers without the old dependency.
- [ ] Verify cutover preconditions against retained evidence.
- [ ] State the tested reversal boundary and any incompatible new writes.

## Failure modes

- Comparing only successful outputs while error semantics change.
- Declaring migration complete from matching record counts.
- Leaving the old backend as a hidden fallback in the acceptance run.
- Calling a switch back a rollback plan when old code cannot read new state.
- Accepting co-residence as proof that the old implementation can be retired.

## References

- Read [substitution decisions](./references/design-guide.md) when mapping caller
  contracts, persisted state, and retirement gates.
- Read [backend substitution example](./references/worked-example.md) when checking
  old-state lookup and negative outcomes after removing the old provider.
