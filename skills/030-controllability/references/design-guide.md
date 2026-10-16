# Runtime control decisions

Choose a mechanism that makes the requested state reachable and confirmable.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| The command returns accepted while the worker keeps claiming. | Publish separate accepted and applied results. Operators must handle an intermediate state. | Inspect worker feedback and claims after applied pause. |
| A toggle retry unexpectedly resumes a paused worker. | Send absolute desired states with command identity. State handling is more explicit. | Duplicate a pause and verify the target remains paused. |
| Pause blocks the channel carrying resume. | Separate control processing from work intake. The worker retains an active control loop. | Pause intake, then apply resume through that loop. |
| A delayed old command overrides current intent. | Add a per-target ordering fence and superseded result. Clients must handle stale commands. | Apply a newer pause before an older resume and inspect the final state. |
| Operators target a recycled display name. | Address the current worker identity and reject a mismatched incarnation. Commands may need reissue after replacement. | Replace the worker instance and verify the old target cannot control its successor silently. |

## Control-loop sketch

```text
on_command(command):
  require authorized(command.actor, command.target)
  if command.order is older than applied_order:
    return superseded
  desired_intake = command.target_intake_state
  applied_order = command.order
  publish_applied_state()

work_loop:
  process_control_messages()
  if desired_intake == running:
    claim_next_job()
  advance_existing_work()
```

The sketch assumes one ordered control owner for the target.
A concurrent implementation must supply the ordering guarantee, not merely copy
the variable names. Active work policy is a separate contract choice.

Applied pause means the intake gate has changed, not that all active jobs finished.
Keep those state predicates separate when an operator task needs both.
