---
name: robustness
description: >-
  Bounds bad-input effects when asked "reject oversized requests safely", "release failed reservations", or "avoid partial rejected rows". Ask the user if input stress vs modeled faults is unclear. Not for component faults (see fault-failure-tolerance), threat review (see security-control-and-security), or normal-profile failures (see reliability).
---
# Robustness

## Definition and scope

Robustness means behavior stays controlled under unexpected inputs, stress, or
environmental deviations. Define permitted rejection, bounded resource effects,
and state preserved for unaffected work; distinguish required-service continuation
under modeled faults (`fault-failure-tolerance`) and adversarial threat/control
coordination (`security-control-and-security`).

## Use when / Don't use when

- Apply when malformed, oversized, pathological, or stressful conditions cause
  uncontrolled allocation, repeated work, partial effects, or damage to unrelated tasks.
- Route workload-growth behavior under ordinary service targets to `scalability`.
- Route normal-profile failure occurrence to `reliability`; include adverse inputs
  here only with an explicit controlled-response contract.

## Workflow

1. Clarify: Read input/parser code, allocation and queue paths, error handling,
   dependency boundaries, operating docs, and observed adverse traces first.
   If the request asserts an adversary or harmful outcome, then retain that context
   and separate the security or safety acceptance question instead of assuming benign stress.

2. Specify: Name adverse classes, baseline valid work, response contract, input/work
   budgets, resource scope, state boundaries, and behavior after the condition clears.
   If the user wants defensive handling, then propose this bounded-response record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Classes: malformed and over-budget inputs discovered on the requested path.
   Response trial: classify and reject the adverse request within 2 seconds of admission.
   Work limits: existing documented size/depth/queue limits; absent limits remain open.
   Effects: no business mutation for the rejected request; preserve unrelated valid state.
   Other work: run a valid control task during exposure and after the adverse request ends.
   Resource evidence: scoped memory/queue/CPU observations, baseline, and retained-work state.
   Repetition: repeated adverse requests must not accumulate orphaned tasks or reservations.
   Status: proposed response criterion, not permission to reject required valid work.
   ```

   Ask at most three groups about adverse classes and valid-work obligations;
   allowed rejection, budgets and shared-state effects; and exercise boundaries.
   Continue to a bounded parser/admission/error-path design with unknown limits explicit.
   If no target exists, then offer the illustrative response trial and confirm
   with the user/stakeholder before using its interval or rejection policy.

3. Design/Implement: Read [bounded-response patterns](./references/design-patterns.md)
   when locating early limits, partial-effect cleanup, or shared-budget isolation.
   If a limit is checked after expensive expansion, then move admission before
   that expansion or bound the expansion itself; catching its final error is insufficient.
   If failed work reserves state/resources, then release or reconcile them under
   the actual lifecycle so repeated bad requests cannot silently consume the service.

4. Verify: Exercise adverse inputs and stress at the declared boundary while
   inspecting rejected work, resource use, unaffected results, and post-exposure state.
   If the error response is prompt but retained work keeps growing, then fail
   the controlled-response claim instead of accepting the status code alone.

5. Report: Return adverse classes, limits, changed admission/error paths, bounded
   observations, state checks, and valid conditions not yet exercised.
   If only isolated requests were checked, then disclose that scope and leave
   repeated/overlapping exposure claims unverified.

## Specification patterns

- **Controlled rejection:** For `{adverse_class}`, the system shall produce
  `{permitted_response}` within `{confirmed_interval}` while respecting
  `{resource_and_state_bounds}`, verified by `{adverse_trace_and_side_effect_checks}`.
- **Unaffected work:** During and after `{adverse_exposure}`, preserve
  `{unrelated_work_and_state}` under `{agreed_isolation_limits}`, verified by
  `{valid_control_tasks_resource_observations_and_cleanup_checks}`.

Use the illustrative rejection trial when no response target is supplied;
confirm with the user/stakeholder. Ask the user for valid-work and resource bounds rather than guessing them.

## Rules of thumb

- Do bound expanded work before materializing an adverse input's full structure;
  a size error after the allocation cannot demonstrate controlled resource behavior.
- Don't accept an error response while orphaned jobs or reservations keep growing;
  repeated rejected inputs can still exhaust the shared process after their responses return.
- Do inspect state after rejecting partially processed input; an error code cannot
  excuse business mutations the controlled-rejection contract forbids.
- Do keep a valid control task running alongside adverse traffic; rejecting bad
  requests is insufficient if the same path starves the work meant to stay unaffected.
- Do verify behavior after the adverse condition ends; a process that remains
  wedged has not shown controlled recovery to its declared normal operating envelope.
- Don't normalize malformed values into invented business data just to avoid an
  exception; controlled rejection can be correct when silent coercion would corrupt meaning.

## Verification

Use boundary-input generation, controlled stress, error-path integration, and
resource/state observation categories. Exercise malformed structure, budget edges,
partial processing, repetition, and overlapping work where in scope. Retain response
timing, scoped resource peaks, live work/reservations, mutations, and valid-control
results. Compare baseline and post-exposure state; no error message alone proves containment.

## Done checklist

- [ ] Define adverse input/stress classes and legitimate work that must remain valid.
- [ ] Inspect that budgets apply before or during expensive expansion, not only after it.
- [ ] Assert the agreed error response and resource/elapsed-work bounds.
- [ ] Check rejected work leaves no forbidden mutation or orphaned reservation.
- [ ] Run valid control tasks during and after adverse exposure.
- [ ] Exercise repeated or overlapping adverse work for every such claimed scope.
- [ ] Report baseline, peak, retained work, and post-exposure state separately.

## Failure modes

- Catching an exception only after an over-budget expansion exhausts resources.
- Returning an error while background work or reservations remain unbounded.
- Partially mutating business state before rejecting the same request.
- Passing bad-input tests while unrelated valid requests cannot finish.
- Claiming repeated-load containment from isolated-input checks alone.
- Coercing invalid values into plausible but invented business data.

## References

- Read [bounded-response patterns](./references/design-patterns.md) when choosing
  early admission, expansion limits, cleanup, or shared-resource checks.
- Read [malformed-import example](./references/worked-example.md) when rejection,
  reservations, and unrelated valid work need separate state assertions.
