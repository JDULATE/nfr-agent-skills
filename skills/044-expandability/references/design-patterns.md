# Capacity admission and operating transition

Use these patterns to make an added resource useful to an existing installation.
Do not assume a particular platform, scheduling mechanism, or resource-size ratio.

## Admission and capability check

- **Use when:** New units must meet an existing type, credential, placement, or
  addressing contract before accepting work. Make rejection and registration visible.
- **Trade-off:** Stricter checks can delay expansion; omitting them can leave an
  allocated resource unusable or assigned work it cannot actually perform.
- **How to verify:** Admit a valid synthetic unit, reject an unsupported one,
  and inspect the installed unit's actual eligibility for the target work class.

## Placement and redistribution

- **Use when:** Added workers, storage, or partitions need routing or state movement
  before contributing capacity. Name the placement owner and transition checkpoints.
- **Trade-off:** Redistribution consumes temporary capacity and can disturb ongoing
  work; the admitted unit may not contribute immediately or evenly.
- **How to verify:** Trace representative work or data onto the new resource and
  compare usable capacity before, during, and after the transition.

## Shared-ceiling ledger

- **Use when:** A controller, routing table, license decision, or data layout can
  cap useful additions. Record the limit and where it is enforced in the installation.
- **Trade-off:** Changing a ceiling may require a separate architecture or commercial
  decision; do not treat an observed limit as a universal platform fact.
- **How to verify:** Inspect the actual configuration and rehearse the supported
  boundary with a safe fixture; preserve the rejection or bottleneck evidence.

## Partial-addition checkpoint

- **Use when:** Registration or redistribution can stop after some work is assigned.
  Preserve enough state to resume or intentionally remove the partial addition.
- **Trade-off:** Checkpoints need ownership and cleanup; removing a unit prematurely
  may discard state that the rest of the installation already relies on.
- **How to verify:** Interrupt admission and movement at distinct stages, then
  resume or unwind using the accepted operator procedure and inspect owned work.

## Requirement record and review checks

Capture starting shape, supported unit, usable capacity metric, target delta,
headroom, service-transition bound, shared ceilings, and retry/cleanup evidence.
Illustrative addition scope only: 1 extra supported unit;
confirm with the user/stakeholder. Obtain the actual useful capacity target separately.

- Reject counting a registered unit that cannot receive representative work.
- Separate resource admission success from workload throughput improvement.
- Keep temporary redistribution cost visible alongside final steady-state capacity.
