---
name: affordability
description: >-
  Checks budget fit when asked "price this workload", "cap running costs", or "include setup costs". Before routing cost concerns, Ask the user: spending ceiling, delivery constraints, or continued value? Not for delivery under all constraints (see feasibility) or continued value (see viability).
---

# Affordability

## Definition and scope

Affordability means acquisition, operation, or change costs fit the stakeholder's
stated financial constraints. Define the workload, cost boundary, period, and
budget owner before judging a design.
Separate spending-cap fit from delivery under all constraints (`feasibility`)
and continued stakeholder value (`viability`).

## Use when / Don't use when

- Apply when an engineering option needs a costed workload comparison against
  a supplied cap, including setup and recurring costs.
- Include repository-visible cost drivers such as request fan-out, retained
  artifacts, provisioned resources, and change effort when priced by the user.
- Route resource use per useful result without a monetary constraint to
  `efficiency-device-efficiency`.
- Route achievable delivery under technical and organizational constraints to
  `feasibility`; cheap alone does not mean deliverable.
- Route whether continued operation remains worthwhile to `viability`.

## Workflow

1. Clarify: Read workload code, deployment/configuration, cost records, ownership
   docs, and any supplied rate model before specifying a budget requirement.
   Identify which actions generate each charge.
   If a rate, period, currency, or cost owner is missing, then Ask the user;
   do not invent a vendor price or convert unknown quantities into money.

2. Specify: Record the costed workload, fixed and variable items, setup/change
   costs, period, approved cap, and uncertainty cases.
   If the user supplies no cap, then propose a labeled illustrative default:
   compare candidate totals without assigning an affordability pass until the
   budget owner confirms the boundary and cap; confirm with the user/stakeholder.
   Ask at most three grouped questions on the cost boundary, workload/rates,
   and required behavior before proposing an engineering change.

3. Design/Implement: Read [cost-fit decisions](./references/design-guide.md)
   when evaluating batching, retention scope, or cost admission.
   If a supplied rate depends on request count, then evaluate supported batching
   while preserving the required result and accepted failure behavior.
   If a cap can be met only by omitting required work, then present the scope
   trade-off instead of reporting the unchanged workload as affordable.

4. Verify: Recompute candidate costs from observed cost drivers and the declared
   rate model. Compare required workload outputs before and after the change.
   Retain raw counts, failed work, unfinished jobs, and excluded items.
   If rates are estimates or cost items are unknown, then report a scenario or
   incomplete estimate rather than an established budget pass.

5. Report: Return the cost ledger, engineering change, preserved-result evidence,
   cap comparison, and remaining assumptions.
   If only a synthetic rate model was used, then limit the conclusion to that
   model and leave actual billing and spending approval unresolved.

## Specification patterns

- **Budget fit:** For `{workload_and_period}`, the total of
  `{included_setup_fixed_variable_and_change_costs}` shall fit
  `{stakeholder_confirmed_cap_and_currency}` under `{supplied_rate_model}`,
  verified by `{cost_driver_trace_and_recomputed_ledger}`.
- **Cost intervention:** Changing `{cost_driver}` shall preserve
  `{required_workload_results}` while meeting `{confirmed_cost_boundary}`,
  checked by `{before_after_outputs_and_cost_calculation}`.

Use the illustrative comparison proposal in Specify when no numeric target is
given; confirm with the user/stakeholder before treating any option as affordable.

## Rules of thumb

- Count setup and committed fixed charges within the declared budget boundary;
  a small per-request price does not establish that the whole workload fits.
- Translate a resource reduction into cost only under the supplied charging rule;
  fewer calls do not save money in a model that charges only per processed record.
- Keep prepaid capacity and incremental spend distinct when comparing options;
  do not charge the same commitment again as though every request bought it anew.
- Do not declare a cheaper skipped workload affordable for the original scope;
  identify the removed obligation and obtain a revised budget/scope decision.

## Verification

Use cost-driver instrumentation, ledger review, and workload replay categories.
Record the exact rate assumptions and workload revision used in each comparison.
Check fixed/variable item ownership to avoid missing or duplicated charges.
Exercise a high-cost scenario supplied by the stakeholder without presenting it
as a forecast. Keep unknown items explicit rather than assigning zero.
Verify batching against the actual provider contract before relying on it.
Distinguish modeled cost, observed usage, and confirmed billed cost.

## Done checklist

- [ ] Name workload, period, budget owner, and cost boundary.
- [ ] Attribute supplied rates and identify unknown cost items.
- [ ] Reconcile setup, committed, and incremental charges.
- [ ] Capture the cost drivers affected by the intervention.
- [ ] Compare preserved workload results before and after the change.
- [ ] Recompute the total and cap decision from the ledger.
- [ ] Report estimates and actual billing evidence separately.

## Failure modes

- Looking only at a marginal request price while ignoring setup charges.
- Treating reduced device usage as a proven monetary saving without a rate model.
- Double-counting a committed charge as both fixed and incremental spend.
- Dropping required work silently to make the total fit.

## References

- Read [cost-fit decisions](./references/design-guide.md) when selecting
  a repository change against a supplied budget model.
- Read [batching budget example](./references/worked-example.md) when comparing
  full-workload outputs with a fixed-plus-variable cost ledger.
