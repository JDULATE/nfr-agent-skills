---
name: reconfigurability
description: >-
  Controls transitions between operating configurations when tickets say "switch modes without losing queued jobs", "resume the interrupted config change", or "who owns work during the switch". Not for the options menu (see configurability), tuning a value (see adjustability), or supporting alternatives (see flexibility).
---
# Reconfigurability

## Definition and scope

Reconfigurability means an established operating arrangement can transition to
another with its agreed state handling intact. Accept intermediate ownership,
application, and completion behavior; distinguish valid settings (`configurability`),
scalar tuning (`adjustability`), and independent alternatives (`flexibility`).

## Use when / Don't use when

- Apply when live queues, ownership, routing, or processing stages must move from
  an existing configuration to another without unexplained state loss.
- Route defining settings to `configurability`; parsing the target document does
  not establish that running work has moved to that arrangement.
- Route a sequence of future transitions and inherited obligations to `evolvability`.

## Workflow

1. Clarify: Read arrangement-selection code, queue/state ownership, application
   checkpoints, rollback behavior, and operator docs before specifying a transition.
   If the request is only an existing scalar adjustment, then use `adjustability`;
   Ask the user what arrangement or in-progress ownership actually changes here.

2. Specify: Record old/target arrangements, accepted work identities, admission
   rules, intermediate owners, cutover evidence, interruption limits, and recovery path.
   If the user wants a configuration change now, then propose this transition record:

   ```text
   Illustrative transition record; confirm with the user/stakeholder:
   Start/target: inspected arrangements and their configuration identities.
   Work: accepted pending and running task identities retained through checkpoints.
   Example bound: 0 unexplained lost accepted task identities in the rehearsal.
   Ownership: agreed finish/drain/transfer rule; duplicate effects need separate policy.
   Completion: target admits and finishes representative work, not merely a valid file.
   Failure: inspect partial application and resume/reverse only under compatible state rules.
   Open items: interruption, duplicate handling, checkpoint semantics, owners and authority.
   ```

   Ask at most three questions about changed arrangement and retained work; allowed
   interruption/duplication; and resume/reversal or proposed defaults needing revision.
   Proceed to a checkpoint design without assuming lossless or interruption-free change.
   If a bound is missing, then offer the illustrative identity-loss bound and
   confirm with the user/stakeholder before accepting its scope or work semantics.

3. Design/Implement: Read [transition patterns](./references/design-patterns.md) when
   choosing admission boundaries, ownership transfer, or partial-application recovery.
   If old work can finish under the old arrangement, then separate its completion
   from admitting new work to the target rather than silently reinterpreting its state.
   If reversal cannot read state already written under the target, then expose that
   incompatibility and design resume or repair instead of promising file-only rollback.

4. Verify: Carry accepted identities and outputs through start, intermediate
   checkpoints, interrupted application, and target completion.
   If a unit exists in neither arrangement's recoverable work record, then fail
   the retained-state claim even when the target configuration reports ready.

5. Report: Return checkpoint evidence, task owners/results, interruption effects,
   actual target work, and resume/reversal limitations.
   If only independent old/new starts were tested, then withhold the transition
   claim until carried-state and interrupted-application cases have evidence.

## Specification patterns

- **Transition:** Moving `{old_arrangement}` to `{target_arrangement}` shall retain
  `{accepted_work_and_meanings}` under `{ownership_and_admission_rule}`, within
  `{confirmed_loss_interruption_and_duplicate_bounds}`, checked by `{checkpoint_rehearsal}`.
- **Interruption:** After failure at `{application_checkpoint}`, `{operator_or_controller}`
  shall perform `{agreed_resume_or_reversal}` using `{retained_state}`, evidenced by
  `{interrupted_transition_and_completion_trace}`.

Use the illustrative loss-bound proposal only for its agreed rehearsal scope;
confirm with the user/stakeholder. Ask the user for interruption and duplicate-effect policy.

## Rules of thumb

- Do attach work to its arrangement identity during cutover; a target-ready signal
  cannot explain which semantics an old in-progress task will finish under.
- Do define who accepts new work while old ownership drains or transfers; changing
  routing first can strand accepted tasks between otherwise valid arrangements.
- Do checkpoint actual accepted ownership, not just a saved target configuration;
  resuming from a file revision alone can skip work never admitted by the new owner.
- Do test reversal against state written after partial application; restoring the
  old selector cannot make that state readable under old arrangement semantics.
- Do finish representative work through the target after cutover; validating its
  document or starting an empty target does not prove the running arrangement changed.
- Don't hide mixed old/target ownership behind a single applied flag; partial
  application needs a recoverable owner for each retained task before completion.

## Verification

Use transition integration rehearsals, ownership reconciliation, and checkpoint
failure injection. Compare accepted task identities with owners and completed
outputs at each stage. Observe stranded tasks, mixed configuration identities,
and repeated effects separately from target readiness; exercise actual recovery
from an intermediate state rather than restarting the fixture empty.

## Done checklist

- [ ] Reconcile pending/running identities against each checkpoint's ownership record.
- [ ] Check new admissions follow the declared old/target boundary during application.
- [ ] Finish old work under its retained semantics or verify the accepted transfer.
- [ ] Interrupt application after ownership begins moving and exercise recovery.
- [ ] Compare completed outputs with the agreed duplicate/loss policy.
- [ ] Finish representative work through the applied target arrangement.
- [ ] Test reversal state compatibility or identify why only forward recovery is supported.
- [ ] Account for every mixed-state task before marking application complete.

## Failure modes

- Equating a valid target document with a completed running transition.
- Switching routing while accepted work loses its recoverable owner.
- Claiming rollback from an old file while new writes have incompatible meaning.
- Rehearsing only clean independent starts and erasing intermediate state.

## References

- Read [transition patterns](./references/design-patterns.md) when planning admission,
  ownership checkpoints, interruption recovery, or compatible reversal.
- Read [queued-work example](./references/worked-example.md) when carrying concrete
  accepted tasks through an interrupted change instead of resetting the fixture.
