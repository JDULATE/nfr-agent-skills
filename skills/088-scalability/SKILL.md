---
name: scalability
description: >-
  Tests behavior as demand grows when tickets say "handle more users without adding errors", "why does throughput stop rising", or "does another worker help under load". Not for resource admission (see expandability), fixed-load bounds (see performance-efficiency-time-or-space-bounds), or unit resource cost (see efficiency-device-efficiency).
---
# Scalability

## Definition and scope

Scalability means service behavior and resource needs remain acceptable as a
specified workload dimension grows. Inspect the growth curve and its tested
limits; distinguish admitting deployment capacity (`expandability`), one fixed-load
envelope (`performance-efficiency-time-or-space-bounds`) and resource per result
(`efficiency-device-efficiency`).

## Use when / Don't use when

- Apply when users/data/arrivals/tenants or another declared axis grow and
  bottlenecks, skew, coordination, backlog or resource demand change service behavior.
- Route adding an admitted worker/storage unit alone to `expandability`.
- Route a single workload's timing bound to `performance-efficiency-time-or-space-bounds`;
  one good point cannot establish acceptable behavior as demand grows.

## Workflow

1. Clarify: Read request/data paths, partition/coordination code, resource policy,
   workload docs and existing load evidence before choosing a growth axis.
   If users means accounts, active sessions or arrivals ambiguously, then Ask
   the user which dimension grows and what behavior/resources must remain acceptable.

2. Specify: Record growth axis, input mix/skew, resource policy, baseline and
   load points, service/result limits, saturation criteria, generator capacity and costs.
   If the user wants growth headroom, then propose this curve record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Axis: named offered workload dimension, holding other declared dimensions explicit.
   Trial points: baseline, 2 times baseline and 4 times baseline demand.
   Resource policy: fixed resources first; any added-resource series is labeled separately.
   Acceptance: confirmed useful throughput, latency, correctness and backlog bounds at each point.
   Data: retain size distribution, hot-key/tenant skew and background/dependency demand.
   Evidence: offered/completed/error/rejected work, resource amounts and per-point service results.
   Limits: report first unacceptable tested point; no linear or unlimited extrapolation.
   ```

   Ask at most three groups about growth axis/data; resource policy and service
   constraints; and trial points, budget or saturation decisions. Continue to a bounded curve design.
   If no growth scope exists, then offer the illustrative load points and confirm
   with the user/stakeholder before using them as the claimed demand range.

3. Design/Implement: Read [growth-curve practices](./references/design-patterns.md)
   when locating shared work, skew, coordination or a resource-dependent bottleneck.
   If added workers do not improve useful completions, then inspect shared state,
   serial work and demand distribution before claiming admission itself solved scalability.
   If source and wait evidence identify shared coordination as the cap, then
   test independent key ownership only where the ordering contract permits it.
   If declared skew concentrates work on an unsplittable key, then retain that
   limit rather than assuming more partitions admit the required growth.
   If resources change between points, then retain that policy and its costs;
   compare fixed-resource and added-resource behavior rather than presenting one unlabeled curve.

4. Verify: Offer each declared demand/data point with a capable generator and
   inspect service correctness, throughput, backlog and resources through the run.
   If queued or rejected demand grows while completion plateaus, then report
   saturation under that policy even if the completed subset looks fast.

5. Report: Return tested curves/points, resource policy, skew, first unacceptable
   conditions, candidate bottlenecks and resource/service tradeoffs.
   If the highest tested point passes, then limit the claim to that observed
   scope; do not infer unlimited growth or linear gains from another resource addition.

## Specification patterns

- **Growth envelope:** As `{workload_axis}` ranges over `{confirmed_points}` under
  `{data_mix_and_resource_policy}`, preserve `{service_and_result_bounds}`,
  verified by `{per_point_offered_completed_backlog_and_resource_evidence}`.
- **Resource response:** For `{resource_change_series}`, report `{useful_capacity_and_quality_change}`
  against `{fixed_resource_baseline}` with `{coordination_and_skew_conditions}`
  and `{untested_ranges}` explicit.

Use the illustrative baseline/multiplier series if no growth scope is supplied;
confirm with the user/stakeholder. Ask the user for service and resource limits before declaring acceptable growth.

## Rules of thumb

- Do name the growing dimension and held conditions; more stored accounts is not evidence for more simultaneously active requests or larger per-request data.
- Don't call resource admission a successful growth curve; a new worker may be usable while the shared bottleneck still caps useful service at rising demand.
- Don't extrapolate linear improvement beyond the tested range; coordination and changed data distribution remain unverified rather than solved by a fitted line.
- Do reduce shared coordination before buying another worker when added workers flatten the capacity curve; compare demand growth with coordination removed and retained to test that specific growth limit.

## Verification

Use stepped/ramped workload trials, bottleneck/partition inspection and resource
series comparison categories. Retain per-point demand, data/skew, environment,
resource amounts, useful completion, rejects/errors, backlog and timing bounds.
Check generator limits and observation duration. Preserve failed points and
plateaus; an admitted replica or a single peak-throughput number is not a verified growth envelope.

Apply these measurement and policy checks during verification:

- Do keep offered work, completed work and backlog together at each point; a throughput plateau with accumulating demand is not successful scaling of that demand.
- Do exercise declared hot-key/tenant skew, not just evenly spread work; balanced test traffic can miss the partition that limits the requested growth envelope.
- Do label resource changes separately from workload changes; extra capacity can hide fixed-resource saturation and its cost when both axes move without explanation.

## Done checklist

- [ ] Define growth axis, data/skew and held workload/environment conditions.
- [ ] Record fixed versus changing resource policies for every curve/point.
- [ ] Verify the generator offers the declared growing demand.
- [ ] Inspect useful results, timing, errors/rejects and backlog at each point.
- [ ] Check shared/serial/partition bottlenecks against actual resource response.
- [ ] Retain first unacceptable tested conditions and the costs of added resources.
- [ ] Limit growth claims to observed points without linear/unlimited extrapolation.

## Failure modes

- Counting newly admitted workers as proof the workload can grow acceptably.
- Changing demand and resources together without disclosing the resource policy.
- Reporting completed throughput while unserved demand accumulates elsewhere.
- Testing only uniform traffic while production scope includes declared hot partitions.
- Extrapolating a few passing points to unlimited or linear future capacity.

## References

- Read [growth-curve practices](./references/design-patterns.md) when choosing
  axes, resource series, skew or a saturation/bottleneck probe.
- Read [coordination-ceiling example](./references/worked-example.md) when comparing
  a fixed-resource intervention with a separate added-worker growth series.
