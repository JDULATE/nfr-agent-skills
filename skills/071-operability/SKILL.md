---
name: operability
description: >-
  Defines operator task paths when asked "handle a partial rerun", "verify task completion", or "set on-call exit checks". Before routing operator trouble, Ask the user: whole task, single command, or support case? Not for fleet policy (see manageability), a single control action (see controllability), or a user support case (see supportability).
---

# Operability

## Definition and scope

Operability means an authorized operator can complete a defined runtime task and
recognize its outcome. Connect entry conditions, actions, partial-state branches,
and verified exit or handoff; distinguish fleet administration (`manageability`),
a single state-changing control (`controllability`), and investigation of a
user support case (`supportability`).

## Use when / Don't use when

- Apply when on-call has a command but cannot complete the surrounding task.
- Apply when a partial export leaves an operator unsure whether to resume, stop, or hand off.
- Route fleet policy and inventory reconciliation to `manageability`.
- Route the mechanics of an individual pause/resume control to `controllability`.
- Route restoring system state after disruption to `recoverability` when restoration,
  rather than performing the operator task, is the acceptance question.

## Workflow

1. Clarify: Read the runbook, task entrypoints, checkpoints, permissions, active-work
   ownership, and result artifacts before prescribing operational actions.
   Identify the authorized operator, target, intended outcome, and stopping boundary.
   If the task could change live state beyond the authorized scope, then Ask the user
   for that scope and prepare the procedure without executing an unauthorized change.

2. Specify: Write the task's entry checks, required inputs, action branches,
   progress observations, interruption/resume rule, exit proof, and escalation owner.
   If no task contract exists, then propose labeled illustrative defaults:
   inspect ownership and committed progress, resume only the remaining requested
   work, and verify the final artifact; confirm with the user/stakeholder.
   Leave recovery-time or completion deadlines open unless supplied.

3. Design/Implement: Read [operator task design](./references/design-guide.md)
   when connecting commands into a resumable task with a verifiable outcome.
   If state is ambiguous, then add an inspection step before the write action.
   If another writer owns the task, then stop at the defined handoff instead of
   launching competing work. If a partial checkpoint exists, then branch using its
   committed boundary rather than the operator's memory of the last command.

4. Verify: Walk the procedure from an ordinary, partially completed, and blocked
   entry state using synthetic or otherwise authorized targets.
   If a command succeeds but the required artifact is absent or wrong, then the
   operator task is not complete. Retain failed and unfinished task attempts.
   Read [partial export example](./references/worked-example.md) when checking
   resume behavior and a blocked-task handoff without duplicating output.

5. Report: Return the executable procedure, input/output artifacts, verified task
   outcomes, restart point, and unresolved handoffs.
   If only command syntax was checked, then report task completion unverified
   rather than calling the runbook operationally usable.

## Specification patterns

- **Task completion:** An authorized `{operator}` shall complete
  `{runtime_task}` from `{supported_entry_states}` using
  `{observable_branch_conditions}`, verified by `{task_exit_artifact}`.
- **Interrupted task:** After `{interruption}`, the procedure shall identify
  `{committed_progress_and_current_owner}`, select `{resume_or_handoff_branch}`,
  and preserve `{already_completed_result}`.
- **Blocked task:** When `{stop_condition}` holds, the task shall return
  `{non_destructive_handoff_record}` to `{responsible_owner}` rather than
  attempt `{unsupported_action}`.

Use the illustrative task contract in Specify for an unquantified request and
confirm with the user/stakeholder. Do not infer an operator time budget from the example.

## Rules of thumb

- Do give the task an observable entry and exit predicate; a successful command
  receipt cannot stand in for a completed export artifact.
- Do branch the procedure on inspectable current state, not the remembered last
  command; an operator taking over mid-task needs the same decision inputs.
- Do make an interrupted task yield its resume context as an operator-facing
  artifact; private process memory cannot support the next operator's continuation.

## Verification

Use runbook walkthrough, task integration, checkpoint inspection, and interruption
simulation categories.
Try the procedure with a fresh operator context using only its published inputs.
Inspect active ownership before resumption and verify the committed boundary.
Check final content and publication state rather than accepting a return code.
Exercise a blocked branch and verify no new writer or output mutation occurs.
Inspect its handoff for the blocked action, observed owner, and retained progress;
do not prescribe blind retries in place of that evidence.
Keep partial work, failures, denied actions, and unresolved decisions in the task record.
Separate operator usability from the correctness of an underlying control primitive.

## Done checklist

- [ ] Resolve the operator, target, task outcome, and authorized action scope.
- [ ] Obtain the procedure's inputs without private author knowledge.
- [ ] Distinguish ordinary, partial, and blocked entry states.
- [ ] Follow current-state branch conditions through the task.
- [ ] Verify committed progress is preserved on resume.
- [ ] Inspect the task's final artifact and publication state.
- [ ] Exercise a non-mutating blocked-task handoff.
- [ ] Capture resume context for a subsequent operator.

## Failure modes

- Calling a task complete because its first command returned success.
- Resuming from memory rather than the committed checkpoint.
- Launching a second writer while another operator owns the task.
- Restarting partial work from the beginning and duplicating committed output.
- Ending a runbook at "contact someone" without the task state needed for handoff.

## References

- Read [operator task design](./references/design-guide.md) when joining
  inspection, action, resumption, and handoff into a usable runtime procedure.
- Read [partial export example](./references/worked-example.md) when verifying
  a complete operator task across partial and blocked starting states.
