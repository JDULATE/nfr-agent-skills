---
name: fault-failure-tolerance
description: >-
  Preserves service through faults when asked "serve with a dead worker", "write during a partition", or "test live failover". Ask the user what must continue during which fault before routing failure protection. Not for restoration (see recoverability), uptime accounting (see availability), or adverse input (see robustness).
---
# Fault/Failure Tolerance

## Definition and scope

Fault/failure tolerance means required service continues despite the specified
component faults, possibly within an agreed degraded contract. Name the fault
model and result preserved during exposure; separate restoration after interruption
(`recoverability`), usable-time accounting (`availability`), and general adverse
input behavior (`robustness`).

## Use when / Don't use when

- Apply when service must continue while a worker, link, dependency, or other
  explicitly identified component is faulty or absent.
- Route restoration after admitted service loss to `recoverability`.
- Route severe mission disruption to `survivability` when ordinary service
  continuity is not the acceptance question; do not silently substitute mission scope.

## Workflow

1. Clarify: Inspect serving code, state ownership, failover config, dependency docs,
   and fault history before choosing redundancy or fallback mechanisms.
   If a requested failure has no defined model, then Ask the user which components,
   symptoms, concurrency, duration, and shared dependencies are in scope.

2. Specify: Bind fault assumptions, required result, exposure interval, allowed
   degradation, detection/handoff behavior, state rules, and continuation evidence.
   If the user wants practical failover, then propose this complete exercise record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Journey/result: requested service with existing business and state obligations preserved.
   Fault trial: 1 fail-stop worker fault while an independently serving path remains.
   Model limits: actual routing/store/control dependencies; independence is unverified.
   Exposure: inject and hold the fault through the agreed workload and handoff observations.
   Acceptance: no lost required result in the scoped exercise; deadlines need confirmation.
   Degradation: only explicitly accepted restrictions; stale/read-only is not assumed valid.
   State: preserve identity, ownership, ordering, and duplicate-effect rules during handoff.
   Evidence: injected fault, affected path, business results, gaps, and fault-clearance behavior.
   Status: bounded design trial, not proof for other fault classes or concurrent failures.
   ```

   Ask at most three groups about fault scope and required result; timing,
   degradation and state constraints; and controlled exercise boundaries.
   Proceed to a fault-path design, keeping unknown independence assumptions visible.
   If no target exists, then offer the illustrative fault trial and confirm with
   the user/stakeholder before adopting its model or continuation criterion.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [continuation patterns](./references/design-patterns.md)
   when designing alternate paths, ownership handoff, or degraded service.
   If alternatives share the modeled failing dependency, then revise the fault
   boundary or the mechanism; counting replicas cannot supply the missing alternate path.
   If ownership can overlap during failover, then constrain who may commit results
   before enabling a path that could preserve responses while duplicating effects.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Inject the stated fault in a controlled environment while distinguishable
   work crosses the service; inspect results throughout detection and handoff.
   If service stops and later returns, then report the interruption and restoration
   instead of accepting that trace as uninterrupted fault tolerance.

5. Report: Return the fault model, changed paths, observed continued/degraded
   results, interruptions, state checks, and unsupported fault combinations.
   If only a restart or final health check was exercised, then leave service
   continuity unverified; the required result must be observed during exposure.

## Specification patterns

- **Continued result:** During `{modeled_fault_and_exposure}`, the system shall
  deliver `{required_journey_result}` within `{confirmed_limits}` under `{workload}`,
  verified by `{continuous_result_trace_and_state_assertions}`.
- **Degraded continuation:** Under `{fault_scope_and_concurrency}`, preserve
  `{accepted_subset_and_state_obligations}` while allowing `{approved_degradation}`,
  measured by `{handoff_and_exposure_checks}` with `{excluded_faults}` disclosed.

Use the illustrative fail-stop trial when no model/target is supplied; confirm
with the user/stakeholder. Ask the user for deadlines rather than inferring them from replica count.

## Rules of thumb

- Do require the alternate path to survive the modeled fault itself; extra workers
  sharing its failed store cannot satisfy continuation of a store-dependent result.
- Don't call restart-after-interruption tolerance; inspect service through the
  detection and handoff interval instead of accepting only its eventual return.
- Do enforce the accepted result semantics during degradation; a fallback page
  cannot stand in for a committed write required throughout the modeled fault.
- Do resolve commit ownership during overlapping failover; otherwise apparently
  continued service can duplicate the effect the tolerance contract must preserve.
- Don't infer concurrent-fault tolerance from isolated fault exercises; overlap
  changes the available continuation paths and must match the claimed model.
- Do hold the injected fault long enough for the agreed workload to exercise the
  alternate path; clearing it before work arrives tests recovery, not continuation under exposure.

## Verification

Use controlled fault injection, failover integration, and state-invariant checks.
Correlate fault onset/clearance with requests, handoff, result commits, failed
attempts, and duplicates. Include the transition and return-to-normal path, not
only steady degraded operation. Inspect shared dependencies, partition behavior,
and ownership ambiguity only for the declared model; report untested combinations.

## Done checklist

- [ ] Define fault type, affected boundary, concurrency, duration, and model exclusions.
- [ ] Inspect that the proposed alternate path avoids the modeled failed dependency.
- [ ] Preserve the agreed result and state semantics through detection and handoff.
- [ ] Observe work during the held fault, with actual result assertions.
- [ ] Check lost, duplicated, reordered, or conflicting effects during ownership changes.
- [ ] Classify interruptions as interruptions even when restoration later succeeds.
- [ ] Verify fault-clearance behavior without claiming untested concurrent models.
- [ ] Record approved degradation and unsupported continuation assumptions.

## Failure modes

- Claiming tolerance because a replacement process eventually starts.
- Adding replicas that all depend on the component being failed.
- Returning success while losing a mandatory result during handoff.
- Testing isolated failures and claiming an overlapping-failure guarantee.
- Clearing the fault before any workload exercises the alternate path.

## References

- Read [continuation patterns](./references/design-patterns.md) when selecting
  redundancy, commit ownership, or a degraded service contract under a stated fault.
- Read [worker-loss example](./references/worked-example.md) when tracing
  continued work and duplicate-effect risks during a held fail-stop fault.
