---
name: manageability
description: >-
  Coordinates fleet policy when asked "reconcile node settings", "find missed fleet updates", or "track local exceptions". Ask the user if fleet policy vs one runtime task is unclear. Not for one runtime task (see operability), one state-changing command (see controllability), or configuration transitions (see reconfigurability).
---

# Manageability

## Definition and scope

Manageability means administrators can coordinate policy and lifecycle decisions
across a declared set of managed targets. Bind desired configuration, inventory,
exceptions, and reconciliation to each target; distinguish one runtime task
(`operability`), one state command (`controllability`), and applying a particular
configuration transition (`reconfigurability`).

## Use when / Don't use when

- Apply when a fleet setting is requested but its per-node adoption is unclear.
- Apply when a local exception spreads accidentally to other installations.
- Route executing a particular operator procedure to `operability`.
- Route a pause or resume command's applied state to `controllability`.
- Route a single configuration transition's in-flight handling to `reconfigurability`.

## Workflow

1. Clarify: Read inventory sources, configuration distribution, agent behavior,
   policy precedence, permissions, and administration docs before defining a rollout.
   Identify managed identities, desired policy, authorized scope, and exception owners.
   If fleet membership or the policy owner is unclear, then Ask the user before
   treating a selection query as authorization to change every discovered target.

2. Specify: Record the selected inventory revision, desired policy revision,
   precedence, exception scope/end condition, per-target observations, and reconciliation.
   If no fleet record exists, then propose labeled illustrative defaults:
   explicit target identities, desired-versus-observed revisions, local exceptions,
   and unresolved offline targets; confirm with the user/stakeholder.
   Ask the user for any required convergence deadline.

3. Design/Implement: Read [fleet administration](./references/design-guide.md)
   when choosing reconciliation, exception handling, or replacement-target rules.
   If dispatch acknowledgment is mistaken for adoption, then add per-target observations.
   If a node is offline, then retain pending intent rather than mark it compliant.
   If an exception ends or membership changes, then recompute the applicable policy
   under its declared precedence instead of copying another node's effective state.

4. Verify: Reconcile an ordinary target, an exception target, and an unreachable
   target against the declared policy. Check a reconnect and exception end.
   If observation is absent or stale, then keep that target unresolved.
   Preserve inventory changes, failures, and pending targets in the rollout record.
   Read [fleet exception example](./references/worked-example.md) for a complete
   desired/observed ledger and the limits of an aggregate "applied" result.

5. Report: Return desired policy, effective per-target policy, adoption evidence,
   unresolved targets, exceptions, and remaining reconciliation work.
   If only reachable agents were inspected, then report that scope instead of
   declaring the whole selected inventory converged.

## Specification patterns

- **Fleet policy:** For `{selected_inventory_revision}`, reconcile
  `{desired_policy}` with `{observed_target_state}` using
  `{precedence_and_exception_rules}`, reporting `{per_target_outcomes}`.
- **Membership:** A replacement or newly admitted target shall receive
  `{applicable_policy}` through `{identity_and_assignment_rule}`, without
  inheriting `{unrelated_target_exception}`.
- **Exception lifecycle:** Exception `{owner_scope_and_end_condition}` shall
  override only `{named_assignment}`; on its end, resume `{base_policy}`
  and confirm through `{target_observation}`.

For an unspecified deadline, use the illustrative fleet record in Specify and
confirm with the user/stakeholder; keep convergence timing undecided.

## Rules of thumb

- Do retire assignments when a target leaves the managed inventory; a decommissioned
  node is not an unreachable node awaiting ordinary policy convergence.
- Do calculate exceptions at the target assignment, not by mutating the shared
  base policy; one diagnostic node must not make every node verbose.
- Do bind administration to stable target identities and incarnations; a replacement
  node must have its assignment evaluated rather than inherit an old name's exception.
- Do reconcile from the declared policy hierarchy, not a neighbor's effective state;
  that neighbor may have a legitimate local exception.

## Verification

Use inventory reconciliation, configuration-agent integration, policy precedence,
and administration authorization checks.
Inspect desired, effective, and observed policy separately for each selected target.
Do not use delivery of a policy message as evidence of actual target adoption.
Exercise unreachable agents, reconnect, replacement identity, and an exception end.
Record the selected population and membership changes before any aggregate result.
Keep failed, pending, excluded, and unknown targets visible beside successful adoption.
Inspect whether stale observations or message acceptance are being counted as compliance.
A policy ledger can establish administrative convergence only within its declared
inventory and observation boundary.

## Done checklist

- [ ] Identify the authorized inventory and target incarnations.
- [ ] Record the desired policy revision and precedence.
- [ ] Calculate ordinary and exception target assignments independently.
- [ ] Inspect observed adoption rather than dispatch acknowledgments.
- [ ] Retain unreachable or stale targets as unresolved.
- [ ] Reconcile a reconnect and an ended exception.
- [ ] Check replacement-target assignment without exception leakage.
- [ ] Bound aggregate conclusions by the inspected inventory.

## Failure modes

- Marking a rollout complete when messages were merely accepted.
- Copying one node's exception into the common fleet policy.
- Counting offline or stale agents as compliant.
- Reusing a retired target's exception solely because its display name returned.
- Reconciling from a neighbor rather than the declared policy hierarchy.

## References

- Read [fleet administration](./references/design-guide.md) when choosing
  target assignment, policy reconciliation, and exception-lifecycle mechanisms.
- Read [fleet exception example](./references/worked-example.md) when separating
  base policy, local overrides, adoption evidence, and unreachable targets.
