---
name: recoverability
description: >-
  Restores usable state after disruption when tickets say "prove we can restore this backup", "the process is up but orders still fail", or "resume work without replaying orders twice". Not for operation during faults (see fault-failure-tolerance), acknowledged-state retention (see durability), or essential mission continuity (see survivability).
---
# Recoverability

## Definition and scope

Recoverability means service and state can be restored to an agreed usable
condition after disruption. Define restored correctness, lost-work allowance,
and elapsed recovery boundaries; distinguish uninterrupted fault service
(`fault-failure-tolerance`), acknowledged-state preservation (`durability`), and
essential mission continuity during severe disruption (`survivability`).

## Use when / Don't use when

- Apply to backup restore, rebuild, interrupted-work reconciliation, restart
  procedures, or proving a recovered service actually performs its required journey.
- Route service continuing throughout a modeled fault to `fault-failure-tolerance`.
- Route preservation of already acknowledged writes through a named event to
  `durability`; record those obligations here without relaxing them through recovery targets.

## Workflow

1. Clarify: Read recovery/startup code, state stores, backup docs, runbooks,
   dependency inventories, and prior recovery traces before proposing a procedure.
   If the required restored result or disruption boundary is unknown, then Ask
   the user; a running process or copied backup is not an assumed recovery endpoint.

2. Specify: Choose disruption, start/finish anchors, restored journey/state,
   acceptable loss, evidence sources, replay reconciliation, dependencies, and authority.
   If the user wants a practical recovery improvement, then offer this record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Scenario: requested disruption and discovered backup/rebuild path in an isolated rehearsal.
   Start/end: disruption observed -> verified usable business journey and reconciled state.
   Timing trial: restore that agreed endpoint within 30 minutes from the start anchor.
   State: compare acknowledged/accepted work against the confirmed loss allowance; unknown stays open.
   Dependencies: artifacts, credentials, keys, runtime, schemas, network, and operator actions.
   Replay: identify completed, pending, duplicate, and unknown work before resuming producers.
   Evidence: milestone timeline, retained snapshot/replay inputs, state comparison, journey result.
   Status: proposed rehearsal criteria, not permission to replace live state or claim backup success.
   ```

   Ask at most three groups about disruption and usable result; time/loss/authority
   requirements; and actual restore dependencies, copies, and replay constraints.
   Continue to an isolated procedure design, retaining missing credentials or state decisions.
   If no time target exists, then offer the illustrative recovery trial and
   confirm with the user/stakeholder before adopting its deadline or endpoint.

3. Design/Implement: Read [restoration practices](./references/design-patterns.md)
   when selecting coherent restore inputs, dependency order, or replay reconciliation.
   If snapshot and replay boundaries disagree, then resolve the gap/overlap before
   resuming writes rather than claiming recovery from a successful import alone.
   If an essential restore dependency lies in the disrupted boundary, then design
   and test its recovery route; a runbook cannot assume its own unavailable prerequisites.

4. Verify: Rehearse from declared disruption through restored state, replay,
   validation, and the actual journey; retain every elapsed milestone.
   If only data import or process startup succeeds, then keep recovery incomplete
   until the agreed state, loss, and usable-result checks pass.

5. Report: Return the procedure and changed automation, observed timing, state
   reconciliation, lost/ambiguous work, dependency gaps, and untested disruptions.
   If rehearsal used warmer inputs or available services absent in the real scenario,
   then disclose that difference and leave the broader recovery claim unverified.

## Specification patterns

- **Restoration:** After `{disruption_and_start_anchor}`, restore `{journey_and_state}`
  by `{confirmed_elapsed_limit}`, with `{confirmed_loss_allowance}`, verified by
  `{milestone_trace_state_comparison_and_business_result}`.
- **Work reconciliation:** Before `{producer_resumption}`, classify `{snapshot_and_replay_work}`
  under `{completed_pending_duplicate_unknown_rules}` and preserve `{required_effects}`,
  verified by `{boundary_gap_overlap_and_idempotence_checks}`.

Use the illustrative restore-time trial if no deadline is supplied; confirm
with the user/stakeholder. Ask the user for the loss allowance instead of choosing one from backup cadence.

## Rules of thumb

- Don't stop the recovery clock at process startup; restored state and the agreed
  business journey must be verified before declaring the restoration endpoint.
- Do account for credentials, keys, artifacts, and control dependencies in the
  disrupted boundary; a backup cannot restore service through an unavailable prerequisite.
- Do reconcile snapshot and replay boundaries before reopening writers; gaps
  lose required work and overlaps can repeat effects despite a clean restore log.
- Don't infer acceptable lost work from backup frequency; compare actual restored
  state with the stakeholder's loss allowance and acknowledged-state obligations.
- Do record warm caches, preloaded secrets, and already-running dependencies in a
  rehearsal; they can hide recovery work that the declared disruption removes.
- Do classify ambiguous in-flight work before replay; retrying everything can
  restore apparent throughput while duplicating effects outside the recovery contract.

## Verification

Use isolated restore rehearsal, dependency-bootstrap checks, state reconciliation,
and recovered-journey integration categories. Record disruption and milestone
anchors, restored inputs, snapshot/replay positions, lost/duplicate/unknown work,
required dependencies, and final business results. Exercise interrupted recovery
where claimed; backup creation logs and a healthy endpoint alone cannot establish restored usability.

## Done checklist

- [ ] Define disruption, timing anchors, restored journey/state, and loss allowance.
- [ ] Verify required artifacts, credentials, keys, and control dependencies are recoverable.
- [ ] Restore from the declared inputs rather than silently using warmer state.
- [ ] Inspect snapshot/replay gap and overlap before writer resumption.
- [ ] Reconcile completed, pending, duplicate, lost, and ambiguous work.
- [ ] Run the restored business journey and state/loss assertions.
- [ ] Retain milestone timing through the full agreed endpoint.
- [ ] Disclose rehearsal shortcuts and untested interruption/disruption assumptions.

## Failure modes

- Treating a backup file or successful import as completed service recovery.
- Measuring only startup while ignoring bootstrap and state verification time.
- Replaying work twice across overlapping snapshot and event boundaries.
- Depending on a credential or artifact service destroyed by the same disruption.
- Declaring acceptable loss from backup cadence without a stakeholder loss contract.
- Hiding warm dependencies that a real recovery scenario would not retain.

## References

- Read [restoration practices](./references/design-patterns.md) when assembling
  restore dependencies, replay boundaries, or a valid recovery endpoint.
- Read [order-store restore example](./references/worked-example.md) when tracing
  accepted work through snapshot, replay, deduplication, and the restored journey.
