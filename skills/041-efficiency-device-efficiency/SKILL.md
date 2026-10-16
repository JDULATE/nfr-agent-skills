---
name: efficiency-device-efficiency
description: >-
  Improves useful work relative to consumed device resources when users say "use less CPU per completed report", "reduce bytes moved for the same useful result", or "compare resource cost of these implementations". Fixes result quality, accounting scope, workload and idle/background allocation before comparing ratios. Not for an operation's latency or space ceiling alone (see performance-efficiency-time-or-space-bounds), growth curves (see scalability), or environmental lifecycle claims (see sustainability).
---
# Efficiency/Device Efficiency

## Definition and scope

Efficiency/device efficiency means useful work is related to consumed device
resources in the stated environment. Preserve result quality and accounting scope;
distinguish an operation envelope (`performance-efficiency-time-or-space-bounds`),
workload growth (`scalability`) and stewardship/lifecycle objectives (`sustainability`).

## Use when / Don't use when

- Apply when comparing CPU, transferred bytes, storage work or another defined
  resource per correct useful output under comparable operating conditions.
- Route elapsed-time or peak-space ceilings alone to `performance-efficiency-time-or-space-bounds`.
- Ask the user what the shared Efficiency alias means; lower latency, lower
  resource per result and lower environmental impact are different acceptance questions.

## Workflow

1. Clarify: Read resource-consuming code, result-validation paths, workload docs,
   device/config context and measurement scope before proposing an optimization.
   If useful output or resource ownership is unclear, then Ask the user; do not
   divide by attempted work or exclude transferred costs to improve the ratio.

2. Specify: Record functional output/quality, resource units, boundary, idle and
   background allocation, workload, warm state, baseline, target and service constraints.
   If the request is a resource optimization, then propose this comparison record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Functional unit: correct completed instance of the requested task, quality unchanged.
   Resource: scoped CPU-seconds per useful result; other resource dimensions reported separately.
   Trial target: 10% lower resource per useful result against the agreed baseline.
   Scope: include retries, background and displaced work inside the confirmed boundary.
   Conditions: same input distribution, workload, device/config and recorded warm/idle state.
   Constraints: existing required latency, result, privacy and persistence behavior preserved.
   Evidence: resource total, useful-result count, failures, boundaries and baseline/candidate traces.
   Status: proposed resource comparison, not an energy, emissions or financial-savings claim.
   ```

   Ask at most three groups about useful output/quality; resource scope and test
   conditions; and baseline, target or service constraints. Continue to a scoped change.
   If no target exists, then offer the illustrative resource-reduction trial and
   confirm with the user/stakeholder before accepting its metric or percentage.

3. Design/Implement: Read [resource-accounting practices](./references/design-patterns.md)
   when eliminating repeated work, choosing reuse or comparing displaced resource costs.
   If caching/batching shifts work or retains more state, then account for fill,
   expiry, background and storage costs under the chosen scope before declaring a saving.
   If a candidate finishes fewer correct results, then compare useful-result
   ratios and service constraints rather than accepting its lower aggregate resource total.

4. Verify: Run comparable baseline/candidate workloads, validate outputs and
   retain scoped resource consumption, useful work, failed/retried work and conditions.
   If instrumentation covers only one process while work moved elsewhere, then
   disclose the missing boundary and leave the whole-operation saving unverified.

5. Report: Return the resource-per-result comparison, preserved quality/service
   checks, idle/background allocation and changes in other resource dimensions.
   If resource units cannot support the claimed energy or money conversion, then
   report the measured resource result without inventing those broader savings.

## Specification patterns

- **Resource ratio:** For `{useful_output_and_quality}` under `{workload_and_environment}`,
  consume `{resource_unit}` per useful result at `{confirmed_target}`, using
  `{boundary_and_idle_background_retry_allocation}`, verified by `{ratio_and_quality_checks}`.
- **Equivalent work:** Compare `{baseline_and_candidate}` on `{matched_inputs_and_conditions}`,
  preserving `{service_and_result_constraints}` while reporting `{resource_dimensions}`
  and `{displaced_or_unmeasured_costs}` separately.

Use the illustrative reduction trial if no target exists; confirm with the
user/stakeholder. Ask the user which resource and useful-result boundary is authoritative.

## Rules of thumb

- Do divide by correct useful results rather than attempts; dropping required
  results can reduce total CPU while leaving resource per valid outcome unchanged or worse.
- Don't call a faster implementation more resource-efficient without measuring
  consumption; parallel work can change elapsed time without reducing the chosen resource total.
- Do include cache fill, retries and background work under the agreed boundary;
  moving consumption outside the foreground timer can fabricate a per-result saving.
- Do keep CPU time, transferred bytes and peak retained space as distinct measures;
  an improvement in one dimension cannot silently compensate for another required bound.
- Don't infer energy, emissions or monetary savings from a CPU ratio alone;
  those claims need their own objective, boundary and supported conversion evidence.

## Verification

Use resource profiling, controlled workload comparison and useful-result validation
categories. Retain device/config, input mix, warm state, scope, resource totals,
correct-result counts, retry/background work and timing/space constraints.
Check for displaced consumption and dimension tradeoffs. Recompute ratios from
retained totals; a lower process metric alone does not establish whole-task resource efficiency.

## Done checklist

- [ ] Define useful output, required quality and the selected resource unit.
- [ ] Bound resource ownership and idle/background/retry accounting.
- [ ] Match or disclose baseline/candidate device, workload and warm-state conditions.
- [ ] Validate actual correct-result counts and preserved service constraints.
- [ ] Recompute resource per useful result from retained totals.
- [ ] Inspect displaced work and other resource dimensions separately.
- [ ] Limit energy, cost and lifecycle conclusions to supported additional evidence.

## Failure modes

- Reporting lower total CPU while fewer required results complete correctly.
- Measuring only foreground work after consumption moved into a background service.
- Calling lower latency a resource saving without consumption evidence.
- Combining unlike resource units into an unexplained efficiency score.
- Converting CPU improvement into unsupported energy, carbon or financial savings.

## References

- Read [resource-accounting practices](./references/design-patterns.md) when selecting
  functional units, accounting boundaries or a reuse/batching comparison.
- Read [report-worker example](./references/worked-example.md) when lower aggregate
  CPU does not necessarily improve resource per correct report.
