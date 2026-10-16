---
name: availability
description: >-
  Improves and measures usable service time when tickets say "users get logged out on deploy", "checkout goes down during releases", or "count our downtime". Not for failure-free operation (see reliability) or restoring usable state (see recoverability).
status: draft
---
# Availability

## Definition and scope

Availability means users can use a service when they need it.
Define that service through named journeys, required results, audiences, and service
times, including accepted degraded modes. Distinguish failure-free operation
(`reliability`) and restoration after disruption (`recoverability`) from whether
the required service is usable now.

## Use when / Don't use when

- Apply when users lose access during deploys, dependencies fail, or an uptime
  objective needs a customer-visible measurement rule.
- Route failure frequency without a service-readiness question to `reliability`.
- Route backup restoration steps to `recoverability`; route continued operation
  under a modeled component fault to `fault-failure-tolerance` when that is the focus.
- Route slow but otherwise usable operations to `performance-efficiency-time-or-space-bounds`;
  include slowness here only if an agreed completion deadline defines usable service.

## Workflow

1. Clarify: Read existing routes and deployment code alongside dependency maps,
   incident reports, service docs, and monitoring definitions before specifying.
   Identify the user journey, audience, service calendar, and usable result.
   If the user wants a practical improvement rather than a formal specification,
   then use the fast path in Specify; otherwise Ask the user for missing calendar,
   deadline, or degraded-mode decisions before accepting a service contract.

2. Specify: Select time-based or request-based accounting and write the eligibility,
   success, exclusion, unknown-data, and aggregation rules before proposing a target.
   Name the observation window, sampling resolution, affected locations, and owner.
   If a formal target is missing, then offer the illustrative proposal below and
   confirm with the user/stakeholder before declaring the contract accepted.
   For the improvement fast path, propose the entire record in this single block:

   ```text
   Illustrative defaults — confirm with the user/stakeholder:
   Journey/result: the requested journey and documented business success result.
   Audience/calendar: documented audience; continuous service if no calendar exists.
   Metric/target/window: good eligible time / eligible time; 99.9%; rolling 30 days.
   Sampling: journey probes each 1 minute at the affected documented locations.
   Bin rule: any failed sample makes a bin bad; absent trustworthy samples mean unknown.
   Deadline: existing end-to-end journey deadline; if absent, Ask the user.
   Exclusions/retries: no maintenance exclusion; retain the original attempt outcome.
   Unknowns: charge unknown time against attainment and report coverage separately.
   Degraded mode: retain every required journey result; no new relaxation by default.
   Evidence/owner: probe outcomes, outage ledger, query revision, existing service owner.
   Status: design assumptions pending answers; no claim that an objective is met.
   ```

   Ask at most three questions total on this path: which journey/result/deadline
   matters; which audiences, service hours, or accounting defaults need changes;
   and which deployment, data-loss, cost, or rollback constraints must be preserved.
   Use available answers and proceed to reversible design while answers are pending.
   If a missing decision blocks a concrete change, then design the options and
   identify that decision without inventing a service promise.

3. Design/Implement: Trace the journey's outage-producing path. Read
   [design patterns](./references/design-patterns.md) when choosing a continuity
   mechanism and its verification evidence.
   If deployment causes interruption, then evaluate draining, readiness, rollout
   strategy, and schema compatibility using the deployment patterns in that file.
   If dependency delays or overload block the journey, then evaluate deadline-bound
   retries and shedding using its dependency and overload patterns.
   If a mandatory component has no usable alternative, then map that failure point
   and evaluate a fallback or redundancy without assuming replica independence.
   If a fallback loses required freshness, authorization, or write behavior, then
   classify that journey as unavailable and Ask the user before redefining success.

4. Verify: Exercise the journey across deployment, dependency loss, and recovery
   in a controlled environment; retain observations and the accounting calculation.
   If telemetry disappears or locations disagree, then report unknown time and
   affected segments separately; do not turn missing evidence into successful time.

5. Report: Deliver the service contract, changes, observed outage intervals,
   coverage gaps, target comparison, and remaining shared failure points.
   If the measurement window is incomplete or a target remains proposed, then mark
   attainment unverified and identify the evidence or decision needed to finish.

## Specification patterns

Substitute confirmed values for braces; retain unconfirmed fields as open decisions.

- **Time:** The system shall complete `{journey}` within `{completion_deadline}`
  during `{service_calendar}`, with good eligible time / total eligible time at
  least `{confirmed_ratio}` over `{observation_window}`, using `{bin_rule}` and
  reporting `{unknown_data_rule}` beside the result.
- **Requests:** The system shall complete `{eligible_request_class}` with
  `{required_business_result}` within `{deadline}` for at least `{confirmed_ratio}`
  of `{eligible_attempts}` over `{window}`, using `{retry_and_exclusion_policy}`.
- **Change continuity:** During `{deployment_or_dependency_event}`, the system
  shall keep `{critical_journey}` usable from `{audience_locations}`, allowing at
  most `{confirmed_interruption}` measured by `{journey_probe_and_time_resolution}`.

For a missing target, use the illustrative accounting defaults in Specify and
confirm with the user/stakeholder; adjust the record to the actual service boundary.

## Rules of thumb

- Do admit a probe sample to good eligible time only when the user-facing journey
  produces its required result; a healthy process alone cannot supply that sample.
- Do measure deployment interruption from the loss of usable service to its return,
  including in-flight requests; drain traffic to preserve that journey, rather than
  declaring the handoff outage-free because a replacement instance is healthy.
- Do count an optional-dependency outage as good time only if the remaining path
  still meets the accepted service boundary; count a missing mandatory result as bad.
- Do probe through shared storage and routing when measuring customer-visible
  good time; separate replica health histories cannot establish that the shared
  journey was usable during their common dependency's outage.
- Do preserve the same success boundary during fallback; reject stale or read-only
  operation as available when the agreed journey requires fresh data or writes.
- Don't remove planned maintenance from the denominator unless the approved
  service calendar explicitly excludes it; retain the excluded intervals in reports.
- Don't average away an unavailable audience segment; retain per-location and
  per-journey results before applying an agreed combined measure.

## Verification

Run journey integration checks through the normal routing and dependency path.
Use deployment rehearsal and fault-injection categories to exercise traffic
handoff and mandatory dependency loss; record the failed step and usable result.
Review readiness and liveness decisions against that result rather than equating
their labels with availability. Compare probe outcomes with request and incident
timelines; inspect coverage, unknown intervals, and exclusion records explicitly.
Use time-series query and synthetic-journey tool categories to recompute the
selected metric from retained observations; do not combine unlike denominators.

## Done checklist

- [ ] Name the required journey, audience, service calendar, and completion deadline.
- [ ] Record accepted degraded behavior and mandatory dependency boundaries.
- [ ] Confirm the denominator, target, observation window, and sampling resolution.
- [ ] Record exclusions, retry accounting, and the unknown-data decision.
- [ ] Exercise deployment handoff and mandatory dependency loss with retained evidence.
- [ ] Inspect each audience segment before reporting the agreed aggregate.
- [ ] Recompute the metric and distinguish measured attainment from missing coverage.
- [ ] Assign owners to remaining outage paths and unresolved service decisions.

## Failure modes

- Counting a healthy worker as available while the user journey fails downstream.
- Removing outages as maintenance after seeing the result instead of following the calendar.
- Calling a fallback successful even though it omits the required business outcome.
- Reporting a favorable observed ratio while hiding an unmeasured interval or audience.
- Claiming redundancy without checking the dependency that every instance still shares.

## References

- Read [measurement contract](./references/measurement-contract.md) when defining
  the denominator, unknown-data policy, probes, or outage review evidence.
- Read [deployment worked example](./references/deployment-example.md) when turning
  a deployment-outage request into a requirement and an executable verification plan.
- Read [design patterns](./references/design-patterns.md) when selecting a shutdown,
  rollout, schema, timeout, shedding, or shared-failure mitigation and its checks.
