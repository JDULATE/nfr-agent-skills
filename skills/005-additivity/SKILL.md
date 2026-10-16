---
name: additivity
description: >-
  Checks summed gains when asked "compare combined savings", "avoid double-counting", or "measure each contribution". Ask the user if sums vs joined behavior is unclear. Not for assembly contracts (see composability) or admitting resources (see expandability).
---
# Additivity

## Definition and scope

Additivity means combining increments preserves their individual contributions
under a declared aggregation rule, verified by isolated-versus-combined measurements.
Define baseline, units, overlap, and allowed interaction; a combination claim without
preserved measured contributions belongs to assembly compatibility (`composability`),
not this repository's additivity convention.

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
   For noisy metrics, use the repeated matched-block procedure in the combination guide.
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
- Do build the combined expectation from contribution identities, including overlap
  and replay; adding isolated set sizes can manufacture a gain no increment supplied.
- Do derive the combined-outcome equation in the metric's units before comparing
  gains; summing displayed percentages can create a false preservation claim.
- Do retain interaction residuals as a named result; don't silently redistribute
  them to make isolated and combined columns agree.
- Do compute a residual for each supported application order; averaging opposite
  interactions can make the combination look additive when neither order is.

## Verification

Use controlled-comparison, property-based, set-accounting, and numerical-analysis
categories as appropriate to the declared operation. Exercise empty increments,
overlap, repeated identity, reversed order, and a shared resource limit.
Inspect whether fixture changes, normalization, or rounding alter the baseline.
Recompute expected and observed combined outcomes from the retained contributions;
report signed residuals and measurement uncertainty separately from the acceptance bound.

## Done checklist

- [ ] Recompute the combined expectation with the baseline included only once.
- [ ] Match baseline, isolated, and combined fixtures by inputs and observation units.
- [ ] Reconcile combined contribution identities against the overlap/replay ledger.
- [ ] Reproduce signed residuals from retained measurements under the agreed equation.
- [ ] Check supported orders separately rather than accepting their average.
- [ ] Challenge the equation with an overlap or shared-limit counterexample.
- [ ] For noisy metrics, retain repeated matched blocks and evaluate their spread;
  for exact counts, demonstrate why a noisy-measurement procedure is inapplicable.
- [ ] Apply the owner-confirmed tolerance and inconclusive rule to the actual residuals.

## Failure modes

- Adding isolated totals instead of baseline-relative changes.
- Counting an overlapping contribution again because it arrived through another increment.
- Claiming additivity from a combined result without measuring isolated contributions.
- Adjusting rounding or the baseline after observing an inconvenient residual.
- Pooling unmatched runs or stopping at a favorable repeat to hide uncertain interaction.

## References

- Read [combination patterns](./references/design-patterns.md) when choosing the
  aggregation operation, overlap attribution, or repeated noisy-contribution checks.
- Read [increment worked example](./references/worked-example.md) when drafting
  a contribution requirement and checking baseline subtraction with concrete values.
