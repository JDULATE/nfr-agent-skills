---
name: expandability
description: >-
  Designs deployment capacity additions when users say "add another storage unit",
  "grow this installation", "attach more workers", or "remove the capacity ceiling".
  Not for workload-to-resource growth behavior alone (see scalability) or a new
  functional capability inside core code (see extendability).
---
# Expandability

## Definition and scope

Expandability means an installation can gain usable capacity through planned
resource or deployment-unit additions. Specify the admission, placement, routing,
and operating transition that make an addition usable; distinguish the growth
curve under workload (`scalability`) and a new function (`extendability`).

## Use when / Don't use when

- Apply to an installation that must admit more storage, workers, partitions,
  or another explicitly supported resource unit.
- Examine an addition's operational steps and limits, not just its purchase or allocation.
- Route demand growth, throughput curves, and bottleneck scaling to `scalability`.
- Route relocation to another execution platform to `portability`; more deployed
  units do not by themselves establish that the platform can change.

## Workflow

1. Clarify: Inspect deployment code, capacity and placement configuration, routing,
   data movement, operator docs, and recorded installation limits first.
   Identify which resource can be added and what usable capacity means for this service.
   If extra capacity is confused with supporting more work efficiently, then
   Ask the user whether the immediate concern is addition mechanics or workload scaling.

2. Specify: Name the starting installation, admitted unit, resulting capacity
   measure, transition constraints, supported limits, and operator evidence.
   If the user wants a capacity improvement, frame it with this example record:

   ```text
   Illustrative capacity-addition record; confirm with the user/stakeholder:
   Addition target: admit 1 extra unit of the named existing deployment resource.
   Baseline/result: measured initial capacity and separately measured usable added capacity.
   Preconditions: supported unit type, placement rules, credentials, and required headroom.
   Transition: existing service results remain within the agreed interruption boundary.
   Accounting: allocated resources are not counted as usable until routing/placement succeeds.
   Evidence: admission, representative work on the new unit, partial failure, and operator record.
   Open limits: final capacity target, migration time, shared bottlenecks, and responsible owner.
   ```

   Ask at most three question groups about the unit and usable result, permitted
   disruption or data movement, and installation limits or operating cost.
   Then design an addition rehearsal using documented capabilities where answers are missing.
   If no numeric addition scope was supplied, then offer the labeled unit count
   above and confirm with the user/stakeholder before treating it as accepted capacity.

3. Design/Implement: Read [capacity admission patterns](./references/design-patterns.md)
   when planning registration, work placement, headroom, and partial-addition handling.
   If added capacity requires moving existing state, then specify placement and
   interruption evidence instead of assuming registration completes expansion.
   If a shared controller or fixed partition limit blocks useful addition, then
   expose that ceiling and evaluate an approved change rather than merely allocating more units.

4. Verify: Rehearse addition from the real starting shape, direct representative
   work to the added resource, and measure usable capacity under the named constraints.
   If an added unit is registered but receives no usable work, then investigate
   routing, eligibility, or placement before reporting the installation expanded.

5. Report: Return the admitted resource, observed capacity delta, transition
   effects, remaining ceilings, failed-addition state, and operator actions.
   If no workload growth experiment was performed, then describe the demonstrated
   addition only and leave claims about scaling behavior to their own evidence.

## Specification patterns

- **Admission:** Starting from `{installation_shape}`, the system shall admit
  `{supported_resource_addition}` and expose `{confirmed_usable_capacity_delta}`
  measured by `{placement_and_capacity_probe}` under `{operating_conditions}`.
- **Transition:** Adding `{resource_unit}` shall preserve `{existing_service_results}`
  within `{accepted_interruption_or_movement_bound}`, verified during
  `{registration_rebalance_and_failure_rehearsal}`.
- **Ceiling:** The installation shall support additions up to `{confirmed_capacity_limit}`
  with `{declared_shared_constraints}`, evidenced by `{boundary_configuration_and_exercise}`.

Use the example unit count for planning only after confirmation; Ask the user for
the capacity delta and transition bounds rather than promising linear growth.

## Rules of thumb

- Do count added capacity after representative work can use it; don't equate
  an allocated or registered unit with a functioning increase in service capacity.
- Do inspect controller, address, partition, and routing ceilings before admitting
  more units; don't multiply serving capacity while ignoring a fixed admission limit.
- Do budget temporary headroom for required data movement; don't spend all spare
  capacity on new steady-state allocation before the transition can complete.
- Do distinguish changing placement rules from physically adding resources;
  an idle added unit needs a placement explanation, not another allocation.
- Do bind addition checkpoints to the new unit's actual work ownership and admission
  stage; don't call it added while it owns work but cannot join the serving set.
- Don't infer an equal throughput increase from equal-sized additions; record
  the actual usable capacity delta and keep workload scaling as a separate question.

## Verification

Use deployment rehearsal, capacity accounting, placement inspection, and operational
failure-injection categories. Compare admitted versus serving units and allocated
versus usable capacity. Exercise a rejected unit, interrupted registration, state
movement, and the installation's declared boundary. Inspect work distribution and
shared-controller pressure during the transition. Preserve service and capacity
observations separately so an addition can fail acceptance without hiding its cost.

## Done checklist

- [ ] Describe the baseline installation and supported addition type.
- [ ] Confirm the usable capacity measure and intended delta.
- [ ] Inspect admission, placement, routing, and shared-controller limits.
- [ ] Record transition headroom and accepted service disruption.
- [ ] Run representative work on the admitted resource.
- [ ] Exercise partial admission and identify retry or cleanup ownership.
- [ ] Report demonstrated capacity separately from untested scaling expectations.

## Failure modes

- Counting allocated resources that the service cannot route work onto.
- Hitting a fixed controller limit after adding otherwise valid units.
- Consuming transition headroom before a required redistribution finishes.
- Reporting linear throughput growth from resource count alone.

## References

- Read [capacity admission patterns](./references/design-patterns.md) when defining
  registration, placement, transition resources, or failed-addition recovery.
- Read [worker-addition example](./references/worked-example.md) when writing a
  capacity requirement that distinguishes admitted workers from usable capacity.
