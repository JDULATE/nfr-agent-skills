---
name: performance-efficiency-time-or-space-bounds
description: >-
  Bounds latency, including tail-percentile deadlines, throughput and space at a stated load when asked "faster exports", "response budget" or "memory ceiling". Not for spread/variation (see predictability), resource per result (see efficiency-device-efficiency), or class treatment (see quality-of-service).
---
# Performance/Efficiency/Time or Space Bounds

## Definition and scope

Performance/efficiency/time or space bounds means an operation meets agreed
elapsed-time, throughput or space limits for a stated workload. Declare the
result and measurement envelope; distinguish resource per useful result
(`efficiency-device-efficiency`), variation (`predictability`), class treatment
(`quality-of-service`) and behavior as load grows (`scalability`).

## Use when / Don't use when

- Apply to slow journeys, response deadlines, throughput requirements, or an
  operation's peak-space budget under an explicit workload and environment.
- Route resource consumption ratios alone to `efficiency-device-efficiency`.
- Route competing service-class treatment to `quality-of-service`; a single
  aggregate latency number cannot establish every class's contract.

## Workflow

1. Clarify: Read the critical-path code, request/job boundaries, queries, queues,
   cancellation and measurement docs before choosing a performance target.
   If start/end or required completion is unclear, then Ask the user; transport
   acceptance or a partial result must not silently replace business completion.

2. Specify: Record workload/data shape, arrival/concurrency, environment, success,
   timing/space boundary, aggregation, exclusions, unfinished work and target.
   If the user asks for a practical speed fix, then propose this envelope:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Operation: requested journey through its actual required completed result.
   Timing trial: p95 elapsed completion time at most 300 ms under the agreed offered workload.
   Statistic: declare the sample/rank calculation; retain raw outcomes and slow cases.
   Load: explicit offered arrivals, concurrency, data sizes/skew and environment; missing values open.
   Accounting: include queue/dependency time at the chosen boundary; retain rejects/timeouts/unfinished work.
   Space: report scoped peak retained memory separately; no unconfirmed ceiling assumed.
   Evidence: offered/completed/error counts, elapsed samples, backlog, space and result checks.
   Status: proposed timing trial, not a universal endpoint budget or measured result.
   ```

   Ask at most three groups about operation/workload; timing/space boundaries
   and outcome rules; and target, environment or constraints. Continue to a measured-path design.
   If no criterion exists, then offer the illustrative elapsed-time trial and
   confirm with the user/stakeholder before accepting its percentile, budget or workload.

3. Design/Implement: Read [operation-envelope practices](./references/design-patterns.md)
   when inspecting queues, dependency work, data access or space growth.
   If a timer omits queue or downstream completion, then align it with the
   required boundary before choosing a fix that merely moves elapsed work elsewhere.
   If a candidate trades memory, correctness or rejected work for speed, then
   check the confirmed constraints instead of declaring a latency-only improvement sufficient.
   If independent lookups dominate completion, then test bounded batching; if
   materialization breaches space, then stream private pages before final publication.

4. Verify: Generate the declared offered workload, inspect correct completion,
   raw elapsed outcomes, unfinished/rejected work and scoped space peaks.
   If the generator stops offering work when responses slow, then disclose the
   changed demand and do not claim the original arrival-rate envelope was exercised.

5. Report: Return the changed path, complete envelope, statistic method, raw/summary
   results, correctness, backlog, rejection and space evidence.
   If only a local function or quiet-load run was measured, then bound the claim
   to that condition rather than inferring end-to-end or loaded performance.

## Specification patterns

- **Elapsed result:** For `{operation_and_result}` under `{workload_environment_and_data}`,
  meet `{confirmed_latency_statistic_and_limit}` between `{start_end_anchors}`,
  verified by `{raw_outcomes_and_explicit_timeout_unfinished_accounting}`.
- **Throughput/space:** Under `{offered_work_and_concurrency}`, complete
  `{confirmed_useful_throughput}` while respecting `{scoped_space_limit}` and
  `{result_constraints}`, verified by `{completion_backlog_error_and_peak_space_trace}`.

Use the illustrative timing envelope if no bound is supplied; confirm with the
user/stakeholder. Ask the user for the offered workload and space scope instead of assuming them.

## Rules of thumb

- Do combine independent serial lookups when their round trips dominate the operation deadline; compare the batched critical path with the same required completed artifact.
- Do overlap independent dependency waits only within the operation's space envelope; select concurrency from the latency/space tradeoff rather than treating maximum parallelism as the goal.
- Do stream bounded pages when full materialization breaches the operation's peak-space ceiling; keep final publication dependent on the required complete result.
- Do shorten queued service demand before increasing execution concurrency when queue time consumes the completion budget; higher dispatch throughput alone need not satisfy the operation deadline.

## Verification

Use load generation, critical-path tracing, result integration and scoped memory
observation categories. Inspect offered versus completed work, raw latency ranks,
queue time, timeouts/rejects, pending work and peak space. Record warm/cold state,
data shape and environment. Recompute the agreed statistic from eligible outcomes;
a profiler hotspot or an empty queue after the run alone proves no operation envelope.

Apply these measurement and policy checks during verification:

- Do time through the required result, including queues inside the chosen boundary; moving work after an early success response can hide the latency the user needs bounded.
- Don't remove timeouts, rejects or unfinished work from a favorable latency story; a fast successful subset does not establish the offered-work contract.
- Do retain the percentile method and raw samples; averaging per-instance percentiles cannot substitute for calculating the agreed statistic over the eligible observation set.
- Do distinguish requested arrivals, active concurrency and completed throughput; slowing the load source can hide the queueing envelope that produced the complaint.
- Do inspect space under the actual data and concurrency envelope; a small-input single-call peak cannot establish the simultaneous loaded operation's memory ceiling.

## Done checklist

- [ ] Define operation/result, workload/data, environment and timing/space boundaries.
- [ ] Inspect timer anchors against actual queued and downstream completion.
- [ ] Retain offered, completed, failed, rejected and unfinished outcomes distinctly.
- [ ] State and recompute the statistic from its eligible raw observations.
- [ ] Check the generator actually offered the declared workload during slowdown.
- [ ] Inspect scoped space peaks under the declared data/concurrency conditions.
- [ ] Verify required content/correctness against the complete result oracle.
- [ ] Disclose unmeasured boundaries and unresolved mixed-outcome acceptance rules.

## Failure modes

- Timing acceptance while the required work finishes elsewhere later.
- Passing a latency target by discarding slow, timed-out or rejected work.
- Averaging percentile summaries instead of applying the agreed sample calculation.
- Allowing a slow generator to reduce the offered demand unnoticed.
- Extrapolating quiet small-input measurements to loaded or large-data bounds.
- Making an operation fast by removing required behavior.

## References

- Read [operation-envelope practices](./references/design-patterns.md) when defining
  measurement/load boundaries, optimizing queues or checking space tradeoffs.
- Read [bounded-export example](./references/worked-example.md) when batching and
  streaming must satisfy latency, space and mixed-outcome acceptance together.
