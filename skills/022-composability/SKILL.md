---
name: composability
description: >-
  Preserves behavior when joining components when tickets say "these stages break when chained", "who closes the shared stream", or "the pipeline changes error handling". Not for assembly effort (see integratability) or summed contributions (see additivity).
---

# Composability

## Definition and scope

Composability means components can be joined through contracts that preserve
the required behavior of the assembled whole. Define value flow, error meaning,
ordering, and ownership across the join.
Separate combined behavior from assembly effort (`integratability`) and
preservation of summed contributions (`additivity`).

## Use when / Don't use when

- Apply when individually valid stages fail their intended behavior after chaining,
  particularly around resource lifetime, effects, or error propagation.
- Include both local component assumptions and the whole pipeline's obligations.
- Route missing wiring or excessive integration work to `integratability`.
- Route whether separately measured gains add under an aggregation rule to
  `additivity`; joining stages does not establish additive effects.
- Route a new plugin contract to `extensibility` when extension admission is the concern.

## Workflow

1. Clarify: Read stage interfaces, callers, resource creation/cleanup, failure
   paths, and pipeline docs before specifying.
   List each participant's assumptions and guarantees at the join.
   If the request only says "combine them," then Ask the user what assembled
   result and lifetime or error obligations must be preserved.

2. Specify: Record stage order, input/output meanings, effect ownership, resource
   lifetime, error mapping, and the whole-path success/refusal conditions.
   If no target is given, then propose a labeled illustrative default:
   the named chain preserves its result, owner-managed cleanup, and visible
   original failure; confirm with the user/stakeholder.
   Ask at most three grouped questions about the result, shared ownership,
   and failure behavior before a practical composition change.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [join decisions](./references/design-guide.md)
   when resolving lifetime, ordering, and failure-contract mismatches.
   If a stage receives a borrowed resource, then keep its close operation with
   the declared owner rather than inheriting an incompatible standalone default.
   If an adapter changes failure meaning, then expose that change or preserve
   the agreed error at the assembled boundary.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Execute the entire chain with real stage contracts, capturing output,
   effects, resource events, and failures.
   If standalone stage tests pass but the join was not exercised, then leave
   composability unverified; local guarantees may have incompatible assumptions.

5. Report: Return the join contract, stage changes, whole-path outcomes, and
   unresolved ownership or order constraints.
   If only a synthetic sequential chain was checked, then withhold claims about
   untested asynchronous, retry, or concurrent compositions.

## Specification patterns

- **Combined result:** Composing `{ordered_components}` over `{input}` shall
  produce `{whole_result_and_effects}` under `{join_assumptions}`, verified by
  `{end_to_end_stage_fixture}`.
- **Lifetime/failure:** During `{chain}`, `{owner}` alone shall perform
  `{resource_finalization}`, and `{stage_failure}` shall remain
  `{boundary_outcome}` with `{cleanup_evidence}`.

Use the illustrative join-preservation proposal in Specify when numbers are
absent; confirm with the user/stakeholder before adopting its ownership choices.

## Rules of thumb

- Match a downstream stage's preconditions to the actual upstream guarantees;
  compatible-looking signatures do not establish a valid join.
- Keep borrowed-resource cleanup with the declared owner; a stage that closes its
  output can invalidate the next stage even after producing locally correct data.
- Define whether order changes the whole result before rearranging stages;
  individually valid transformations need not commute.
- Preserve the original stage failure at the assembled boundary when cleanup also
  fails; reporting only the cleanup error changes the chain's failure contract.

## Verification

Use end-to-end pipeline fixtures, resource-lifetime traces, and failure injection.
Compare whole-path results with the agreed contract rather than only stage outputs.
Capture resource owner, open/closed state, writes, and cleanup sequence.
Exercise a downstream failure after upstream output and inspect the resulting error.
Keep partial output and failed cleanup visible under the chosen policy.
Retain identical initial inputs when comparing alternative stage arrangements.
Do not infer associativity or order independence without explicit evidence.

## Done checklist

- [ ] Match each join's assumptions with the producer's guarantees.
- [ ] Define the whole result and allowed partial effects.
- [ ] Assign shared-resource ownership and finalization.
- [ ] Exercise the actual stage chain, including trailing writes.
- [ ] Inject a stage failure and inspect its boundary outcome.
- [ ] Check cleanup events and any secondary failure separately.
- [ ] State untested ordering, retry, and concurrency assumptions.

## Failure modes

- Treating matching type signatures as sufficient composition evidence.
- Letting a borrowed resource close before later stages need it.
- Reordering transformations without checking the combined result.
- Replacing a stage error with a secondary cleanup failure.
- Accepting standalone stage checks as proof of the assembled whole.

## References

- Read [join decisions](./references/design-guide.md) when reconciling lifetime,
  ordering, and failure guarantees across components.
- Read [borrowed-stream example](./references/worked-example.md) when checking
  a valid whole-path result after stages share a resource.
