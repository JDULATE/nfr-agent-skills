# Operator task decisions

Design for the whole runtime task, not just a convenient command.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| Operators cannot tell whether a task is already running. | Add ownership and checkpoint preflight before the write branch. Starting the task may require waiting or handoff. | Present an active owner and verify no second writer starts. |
| A partial rerun duplicates committed output. | Derive resumption from a verified committed boundary and separate uncommitted staging. More state must be inspected. | Resume a partial fixture and compare the final content with the expected artifact. |
| The runbook assumes the original operator remembers the last step. | Export target, ownership, checkpoint, and next branch as resume context. The task interface gains an artifact. | Hand the context to a fresh operator and select the same next action. |
| Command success does not establish the requested result. | Add task-level exit inspection and publication evidence. Completion may remain unresolved. | Return a successful command with an absent final artifact; the task must not pass. |
| A blocked task suggests endless retries. | Provide a state-bearing handoff and a non-mutating stop branch. Work may finish later under another owner. | Exercise the blocked state and inspect that the handoff contains the retained progress. |

## Procedure sketch

```text
state = inspect_export(target)
if state.owner is active:
  return handoff(target, state.owner, state.committed_chunks)
discard_only_verified_uncommitted_staging(target)
resume_remaining_chunks(target, state.committed_chunks)
result = inspect_published_artifact(target)
if result.matches_required_content:
  return task_complete(result)
return task_incomplete(current_resume_context(target))
```

Discarding staging is authorized only for the task's verified uncommitted data.
Do not turn this example into permission to delete unknown partial artifacts.

Keep the exit proof separate from a command's acceptance receipt.
If ownership cannot be determined, take the uncertainty branch rather than
assuming the export is safe to mutate.
