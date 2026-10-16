---
name: predictability
description: >-
  Bounds observed variation and outliers under stated conditions when users say "the same task sometimes takes much longer", "make completion times consistent", or "stop rare long pauses from surprising callers". Separates conditional distributions, extreme observations and missing/censored work. Not for a central timing target alone (see performance-efficiency-time-or-space-bounds), control drift or oscillation (see stability), or product-family variation points (see variability).
---
# Predictability

## Definition and scope

Predictability means variation in observed behavior stays within an agreed range
under stated conditions. Bound spread, outliers and conditional differences;
distinguish an absolute operation envelope (`performance-efficiency-time-or-space-bounds`),
control drift/oscillation (`stability`) and product-family options (`variability`).

## Use when / Don't use when

- Apply when equivalent tasks have surprising pauses, inconsistent resource use
  or outcomes whose variation matters independently of a central performance target.
- Route a single elapsed-time ceiling without a variation concern to
  `performance-efficiency-time-or-space-bounds`.
- Route held-condition drift, flapping modes or feedback reversals to `stability`.

## Workflow

1. Clarify: Read execution and queue code, timing/measurement docs, warm-state
   behavior and raw outcome traces before attributing variation to a cause.
   If observations mix different inputs or conditions, then separate relevant
   groups with the user instead of calling their combined spread unexplained jitter.

2. Specify: Record observed variable, conditional groups, range/outlier rule,
   sampling/window, exclusions, unfinished outcomes, baseline and absolute constraints.
   If the user wants consistent completion, then propose this variation record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Variable: required task's end-to-end completion time under one declared condition group.
   Trial bound: observed maximum minus minimum at most 50 ms in the agreed eligible set.
   Conditions: record input shape, demand, device/config and warm/cache state; stratify meaningful differences.
   Accounting: retain raw extremes, timeouts, unfinished and missing samples separately.
   Window/method: agreed observation window and eligibility; no cherry-picked steady subset.
   Other constraints: a narrow spread does not waive the actual absolute deadline or result correctness.
   Evidence: per-group outcomes, extremes, coverage and proposed causes, not a smooth average alone.
   ```

   Ask at most three groups about variable and surprising behavior; condition
   groups/window/missing outcomes; and range, absolute constraints or acceptance.
   Continue to a scoped variation analysis with unconfirmed groups/bounds visible.
   If no target exists, then offer the illustrative observed-range trial and
   confirm with the user/stakeholder before treating its sample set as sufficient.

3. Design/Implement: Read [variation practices](./references/design-patterns.md)
   when reducing variable work or separating warm, queued and competing conditions.
   If extreme cases reveal a distinct input/cache/dependency path, then inspect
   that path rather than smoothing away the observation that exposed it.
   If a candidate makes every result equally slow, then assess the separate
   absolute deadline; lower variation alone cannot establish overall acceptable service.

4. Verify: Repeat the agreed condition groups, retain raw extremes and coverage,
   and compare variation plus absolute/result constraints under the same method.
   If unfinished work is absent from the trace, then report the censoring gap;
   the observed completed-only range cannot establish the whole workload's bound.

5. Report: Return per-condition variation, outliers, missing/censored work,
   changed variable-cost paths and observed absolute limits.
   If only finite observations support the bound, then state that scope without
   claiming no future outlier or a deterministic deadline guarantee.

## Specification patterns

- **Variation:** Under `{condition_group}`, keep `{observed_variable}` within
  `{confirmed_spread_or_outlier_rule}` over `{window_and_eligible_set}`, verified
  by `{raw_grouped_outcomes_extremes_and_coverage}`.
- **Paired constraints:** Reduce `{variation_measure}` for `{task}` while meeting
  `{absolute_performance_and_result_requirements}`, verified by
  `{matched_condition_comparison_and_unfinished_work_accounting}`.

Use the illustrative observed-range trial if no criterion exists; confirm with
the user/stakeholder. Ask the user which unobserved/timeout cases block acceptance.

## Rules of thumb

- Don't replace raw extremes with a stable average; similar means can conceal
  very different surprises in the individual completion outcomes the user needs bounded.
- Do compare meaningful condition groups before blaming variability; cold starts
  and cached repeats may answer different conditional questions rather than one unexplained spread.
- Do preserve timeouts and unfinished work beside completed observations;
  dropping the slowest unknown outcomes can manufacture a narrow observed range.
- Don't call uniform slowness acceptable solely because spread improved;
  predictable completion can still violate the independent absolute deadline.
- Do predeclare window and outlier exclusions; deleting inconvenient pauses
  after observation changes the variability contract instead of meeting it.
- Do trace rare variable-work paths, not only the usual hotspot; eliminating
  typical cost can leave the exceptional branch that dominates the surprise unchanged.

## Verification

Use repeated-condition trials, raw-distribution inspection and exceptional-path
tracing categories. Retain input/cache/load groups, individual outcomes, extrema,
timeouts, missing observations and absolute deadlines. Compare the same eligibility
rules before/after. Record finite coverage and hypothesized causes separately;
observed spread alone establishes neither future absence of outliers nor control-loop stability.

## Done checklist

- [ ] Define variable, condition groups, eligible window and variation/outlier rule.
- [ ] Retain raw outcomes and meaningful warm/input/load differences.
- [ ] Inspect extremes and exceptional paths rather than only averages.
- [ ] Keep timeout, unfinished and missing outcomes visible in the verdict.
- [ ] Compare baseline/candidate variation under the same predeclared method.
- [ ] Check independent absolute performance and result constraints.
- [ ] Limit conclusions to observed coverage without a future no-outlier guarantee.

## Failure modes

- Reporting a stable average while individual tasks have long surprises.
- Mixing distinct conditions then diagnosing their combined spread as unexplained noise.
- Removing unfinished or timed-out tasks to make the range look smaller.
- Making all work uniformly slow and calling the service acceptable.
- Selecting exclusions or windows only after seeing unfavorable outliers.

## References

- Read [variation practices](./references/design-patterns.md) when defining groups,
  retaining censored outcomes or inspecting exceptional work paths.
- Read [consistent-but-slow example](./references/worked-example.md) when variation
  improves but the independent timing requirement remains unsatisfied.
