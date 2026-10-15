# Availability design patterns

Select a pattern for an observed outage path and the required journey result.
Use the trade-off to choose a controlled exercise; do not infer a guarantee from
a deployment label or prescribe a tool, timeout, replica count, or rollout size.

## Graceful shutdown and draining

- **Use when:** A retiring instance loses new or in-flight requests during changes.
  Stop admitting new work through the serving path, let accepted work finish within
  its agreed deadline, and close resources in dependency order.
- **Trade-off:** Draining can delay retirement and consume temporary capacity;
  long-lived sessions need an explicit continuation or disconnect decision.
- **How to verify:** Send distinguishable work before and during retirement;
  inspect routing, completion, duplicate effects, and interruption intervals.
  Exercise the drain deadline and check unfinished work is reported honestly.

## Readiness vs liveness

- **Use when:** The platform needs separate decisions about admitting traffic and
  restarting a process. Define readiness around the instance's ability to serve its
  required role; define liveness around a condition that restarting can remedy.
- **Trade-off:** A broad readiness dependency can withdraw every instance during
  a shared outage; dependency-based restarts can add churn without fixing that outage.
  Decide which dependency failures should affect routing, restarting, or neither.
- **How to verify:** Exercise startup, local process failure, optional dependency
  loss, and mandatory shared dependency loss. Inspect each routing and restart
  decision against the intended behavior; measure the end-to-end journey separately.

## Rolling rollout

- **Use when:** Old and new instances can coexist while traffic moves incrementally.
  Keep enough serving capacity for the measured workload during replacement.
- **Trade-off:** Mixed versions need compatible requests and stored data; reduced
  capacity during the transition can make a previously usable journey unavailable.
- **How to verify:** Route work across old and new versions during replacement;
  exercise peak-relevant load, in-flight work, rollback, and the weakest capacity stage.

## Blue-green rollout

- **Use when:** A replacement serving environment can be prepared before switching
  routing away from the current environment. Define switch and rollback criteria.
- **Trade-off:** Parallel environments consume resources, and shared storage or
  irreversible writes can prevent rollback even if routing can switch back.
- **How to verify:** Run journeys against the replacement, switch normal routing,
  inspect session and connection behavior, and rehearse switching back with data
  written by the replacement. Report any state that the old environment cannot read.

## Canary rollout

- **Use when:** A limited, defined audience can exercise a change before expansion.
  Choose signals and stop criteria for the affected journeys and audience segments.
- **Trade-off:** Limited exposure may miss rare paths or unrepresented audiences;
  sharing a database or migration can expose users outside the canary traffic group.
- **How to verify:** Exercise a failing canary and confirm expansion stops and
  routing recovers. Inspect shared-state effects and segment-specific journey
  results; do not infer broad availability from a quiet or unrepresentative canary.

## Backward-compatible schema changes

- **Use when:** A rollout or rollback mixes versions that read and write shared data.
  Introduce compatible additions, move readers and writers, and remove obsolete
  structures only after verifying old consumers and rollback needs are retired.
- **Trade-off:** Overlap can require temporary duplication, backfill work, or extra
  compatibility paths; it is not permission to retain data beyond its approved lifetime.
- **How to verify:** Test old and new readers against old and new writes, interrupted
  backfills, missing new fields, and rollback. Check the actual data forms needed
  by each version rather than assuming a successful migration means safe coexistence.

## Timeouts and bounded retries

- **Use when:** Dependency waits occupy the journey's remaining completion budget.
  Allocate dependency timeouts within that budget; retry only failures for which
  another attempt is useful and repeated effects are safe or explicitly reconciled.
- **Trade-off:** A short timeout can reject work that would finish; extra attempts
  consume capacity and can duplicate side effects. Bound attempts and total elapsed
  time; define cancellation and delay behavior instead of adding retries everywhere.
- **How to verify:** Delay or drop dependency responses, including after a write
  commits. Inspect total duration, attempt limits, cancellation, duplicate results,
  and original-attempt accounting under the agreed availability definition.

## Load shedding

- **Use when:** Admitting more work prevents the defined essential journeys from
  finishing. Identify work that may be refused and the response users should receive.
- **Trade-off:** Refused eligible work remains unsuccessful for its own service
  contract. Protecting a critical path does not justify silently excluding rejected
  work or disadvantaged audience segments from the availability denominator.
- **How to verify:** Increase offered work in a controlled environment; inspect
  admission decisions, critical journey completion, rejection signals, queue bounds,
  recovery after load subsides, and accounting for every affected request class.

## Single-point-of-failure mapping

- **Use when:** A required journey depends on a component or operational action
  with no usable alternative. Map storage, routing, credentials, control services,
  deployment steps, and human handoffs alongside the serving instances.
- **Trade-off:** Adding an alternative adds coordination and operating costs;
  apparent alternatives can still share the dependency that caused the outage.
- **How to verify:** Disable each mapped dependency in a controlled exercise and
  inspect the required user result. Check proposed alternatives' shared dependencies
  and failover behavior before counting them as distinct availability protection.
