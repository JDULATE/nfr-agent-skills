# Post-relocation resumption decisions

These decisions allow a declared pause; they do not promise active continuity.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| Login works but the old draft is missing. | Persist the task identity, content, revision, and pending changes. More local state needs lifecycle handling. | Suspend, reconnect elsewhere, and perform an edit on that same draft. |
| Saved context contains only the old endpoint. | Resolve the current resource using stable task identity and current environment. Resolution may fail and must stay visible. | Change the endpoint and inspect the resumed resource identity. |
| Remote state changed while the user was away. | Compare saved base revision with current state under an agreed conflict policy. Resumption may wait for a decision. | Introduce a remote revision and verify no silent overwrite occurs. |
| Old credentials are treated as current authority. | Revalidate through the existing policy after reconnect. A task may remain unavailable. | Revoke fixture access and inspect preserved context without an unauthorized write. |
| Failure opens an empty workspace as apparent success. | Return an explicit unresolved resume result with saved context intact. Users may need a recovery decision. | Remove the resource binding and verify the snapshot is retained. |

## Resume sketch

```text
saved = load_saved_task_context()
connection = reconnect_in_new_environment()
resource = resolve_current_task(saved.task_id, connection)
require current_policy_allows_resume(resource)
if resource.revision != saved.base_revision:
  return resume_conflict(saved, resource)
restored = restore_pending_work(saved, resource)
return verify_useful_resumed_action(restored)
```

The sketch does not decide conflict resolution or grant new permissions.
Those choices come from the confirmed project policy.

Keep saved work available when the current resource cannot be resolved.
Do not describe a connected but empty task as a successful resumption.
