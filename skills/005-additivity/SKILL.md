---
name: additivity
description: >-
  Specifies and checks preserved contributions when users say "do these gains add
  up", "combine these increments", "avoid counting the benefit twice", or "check
  the combined effect". Not for component assembly contracts alone (see composability)
  or attaching a supplementary capability (see augmentability).
---
# Additivity

## Definition and scope

Additivity means combining increments preserves their individual contributions
under a declared aggregation rule. Define the baseline, units, overlap, and allowed
interaction for this repository's working meaning; distinguish assembly compatibility
(`composability`) and a supporting capability's existence (`augmentability`).

## Use when / Don't use when

- Apply when independently measured contributions are expected to survive combination.
- Investigate double counting, overlapping effects, order dependence, and shared budgets.
- Route interface wiring without a contribution claim to `composability`.
- Route extra deployment capacity to `expandability`; an added instance does not
  establish that its measured contribution combines as expected.

## Workflow

1. Clarify: Read the existing calculation code, metric definitions, experiment docs,
   and combination paths before defining an additive requirement.
   Identify what is combined and which outcome each increment claims to change.
   If the user has not defined an aggregation rule, then Ask the user whether
   contributions are meant to sum, union, or follow another explicit operation.

2. Specify: Record baseline, increment identity, common conditions, units,
   combination rule, overlap policy, and the comparison tolerance.
   If the request is an improvement, then offer this compact starting record:

   ```text
   Illustrative starting record; confirm with the user/stakeholder:
   Scope: named increments and the existing outcome metric under held conditions.
   Reference: unchanged baseline measured alongside isolated and combined increments.
   Rule: stakeholder-chosen aggregation; subtract a shared baseline only once.
   Target: 0 absolute deviation for exact-count examples; confirm units and tolerance.
   Ordering: inspect both addition orders unless the declared rule fixes an order.
   Evidence: isolated results, combination results, overlap ledger, residual calculation.
   Owner/open items: metric owner; unresolved aggregation or measurement noise stays open.
   ```

   Ask no more than three grouped questions: which increments and outcome matter;
   how shared contributions and order should count; and what tolerance and conditions
   are acceptable. Continue with a comparison design while answers are pending.
   If no numeric target is provided for a formal spec, then use the labeled proposal
   above and confirm with the user/stakeholder before accepting its tolerance.

3. Design/Implement: Read [combination patterns](./references/design-patterns.md) when
   separating contribution accounting from shared state and overlap.
   If a shared effect appears in both increments, then deduplicate or explicitly
   allocate it under the chosen rule rather than counting the same effect twice.
   If the measured quantity has no defensible aggregation, then replace the additive
   claim with a separately named combined-outcome requirement and obtain its boundary.

4. Verify: Measure baseline, isolated increments, and their combination with the
   same fixtures and observation procedure; calculate the residual against the rule.
   If residuals depend on input order, resource contention, or measurement drift,
   then expose that interaction instead of hiding it inside a favorable aggregate.

5. Report: Return the rule, baseline treatment, contribution table, residuals,
   overlap decisions, and cases for which combination failed acceptance.
   If isolated and combined conditions differ, then label the comparison inconclusive
   and identify the matched measurement needed before asserting preserved effects.

## Specification patterns

- **Contribution:** Under `{held_conditions}`, combining `{increments}` shall produce
  `{aggregation_rule}` of their separately measured `{metric}` contributions relative
  to `{baseline}`, within `{confirmed_tolerance}`, checked by `{comparison_fixture}`.
- **Overlap:** Combining `{contribution_sets}` shall count `{shared_effect}` according
  to `{deduplication_or_allocation_rule}`, verified against `{attribution_ledger}`.
- **Order:** Applying `{increment_sequence}` shall preserve `{declared_order_property}`
  across `{supported_orders}`, measured by `{residual_check}` at `{accepted_bound}`.

Use the illustrative exact-count tolerance above when proposing an initial requirement;
confirm with the user/stakeholder. Ask the user before treating noisy measurements,
ratios, or bounded resources as quantities whose isolated gains can simply be added.

## Rules of thumb

- Do express contributions relative to the same baseline; don't add full totals
  and thereby include the baseline repeatedly.
- Do identify overlapping members before adding set sizes; don't turn a union's
  shared members into multiple contributions.
- Do state the aggregation operation for the actual metric; don't add percentages,
  elapsed times, or improvements merely because they share a display format.
- Do retain interaction residuals as a named result; don't silently redistribute
  them to make isolated and combined columns agree.
- Do exercise repeated increment delivery under its identity policy; don't count
  a replay as a new contribution when it represents the same increment.
- Don't assume reversing addition order is harmless when contributions mutate
  shared state; check order behavior against the declared rule.

## Verification

Use controlled-comparison, property-based, set-accounting, and numerical-analysis
categories as appropriate to the declared operation. Exercise empty increments,
overlap, repeated identity, reversed order, and a shared resource limit.
Inspect whether fixture changes, normalization, or rounding alter the baseline.
Recompute expected and observed combined outcomes from the retained contributions;
report signed residuals and measurement uncertainty separately from the acceptance bound.

## Done checklist

- [ ] Identify each increment, its identity, and its measured contribution.
- [ ] Fix a baseline and matching measurement conditions.
- [ ] Confirm units and the aggregation operation with the metric owner.
- [ ] Record overlap, replay, and ordering policies.
- [ ] Agree a tolerance and its interpretation for exact or noisy results.
- [ ] Compare isolated and combined cases, including an overlap counterexample.
- [ ] Preserve the residual calculation and unresolved interactions in the report.

## Failure modes

- Adding isolated totals instead of baseline-relative changes.
- Counting an overlapping contribution again because it arrived through another increment.
- Claiming additivity from a combined result without measuring isolated contributions.
- Adjusting rounding or the baseline after observing an inconvenient residual.

## References

- Read [combination patterns](./references/design-patterns.md) when choosing the
  aggregation operation, overlap attribution, or interaction checks.
- Read [increment worked example](./references/worked-example.md) when drafting
  a contribution requirement and checking baseline subtraction with concrete values.
