# Active client handoff decisions

Use these decisions for the declared application continuity boundary.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| A new connection creates a new task id. | Keep task identity outside transport construction. More persistent task context is needed. | Change paths and inspect the same active logical task. |
| Overlapping paths both advance progress. | Assign a current path owner with a handoff fence. Delayed old-path work needs explicit handling. | Deliver an old-path message after ownership changes and inspect unchanged progress. |
| The old route is removed before the new route is usable. | Use a declared readiness/handoff condition for overlap where supported. Both paths may consume resources temporarily. | Hold replacement readiness and verify the usable route is not retired early. |
| A path disappears with unacknowledged input. | Retain task-level pending input and reconcile against acknowledged progress. This needs storage and a completion rule. | Lose an acknowledgment during the fixture and inspect that no input is silently skipped. |
| The environment cannot meet the requested continuity. | Report the unsupported case or negotiate a different contract. Resume-after-pause is a different result. | Exercise the unavailable-path case and avoid claiming the active continuity predicate passed. |

## Handoff sketch

```text
task = existing_active_task()
new_path = prepare_replacement_path()
if not declared_ready(new_path):
  return handoff_pending(task, old_path_retained_where_usable)
owner = advance_path_generation(task, new_path)
resume_transport_for_same_task(task, owner, acknowledged_prefix)
retire_old_path_after_handoff()
ignore_retired_generation_progress()
```

The sketch assumes the declared overlap/readiness mechanism is available.
It is not a guarantee that an old path remains usable after physical disconnection.

## Continuity boundary

A transport can reconnect while an application activity remains active.
Record which layer the contract concerns.
If the application instead enters suspended and asks the user to reopen it after
relocation, describe that as post-move resumption rather than uninterrupted activity.
