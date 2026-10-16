# Draft resumption after relocation

This is an illustrative client-task fixture, not a claim about any network service.
All revisions and proposed handling are illustrative examples;
confirm with the user/stakeholder before adopting the resumption contract.

## Filled task record

| Field | Fixture value |
| --- | --- |
| Moving subject | user-elm with the same client device |
| Task / base revision | draft-fern / revision ash |
| Initial remote content | Title: North |
| Pending local change | append line Note: inspect |
| Saved context | task draft-fern, base ash, original title, pending appended line |
| Old environment binding | draft-fern -> endpoint-old |
| New environment binding | draft-fern -> endpoint-new |
| Movement boundary | explicit suspension, disconnected relocation, later reconnect |
| Current authority | same user permitted to resume draft-fern in the normal case |
| Normal remote state after move | revision ash, Title: North |
| Useful resumed action | submit the pending note against base ash |
| Expected result | same draft, revision birch, Title: North then Note: inspect |
| Carry | saved pending change retained until acknowledged or explicitly resolved |
| Conflict policy | report conflict; preserve local work; no automatic overwrite |

## Before remediation

The saved context contains only endpoint-old and the rendered title.
After relocation, endpoint-old is unavailable.
Login at the new environment succeeds, but the client opens an empty draft.
The pending note is absent, so useful operation was not restored.

## Remediation and normal resumption

Save the filled task context before suspension.
After reconnect, resolve draft-fern through endpoint-new and revalidate access.
The current remote revision is still ash, so restore the pending line.
Submit it to draft-fern against base ash.

The acknowledged after state is:
```text
task = draft-fern
remote_revision = birch
content = Title: North; newline; Note: inspect
pending_change = acknowledged
local_saved_context = retained as completed receipt
```

The explicit pause was accepted; no claim is made that editing continued during movement.

## Changed-remote-state failure case

Instead, let the remote task become revision cedar with Title: South during the pause.
The saved base remains ash and the pending line remains Note: inspect.
Resumption returns conflict:
```text
saved_base = ash
remote_revision = cedar
remote_content = Title: South
local_pending = Note: inspect
write_applied = no
```

No local or remote change is silently discarded.
The user must choose the project's conflict resolution.

## Missing binding and revoked authority

If draft-fern cannot be resolved, retain the snapshot and report unresolved resource.
If the supplied current policy denies access, preserve local context and apply no write.
Neither successful login nor a valid old endpoint can override those outcomes.

## Requirement example and limits

After the declared relocation pause, the client shall restore draft-fern's pending
work through the current binding and complete the resumed action or expose the
specified conflict/missing-resource result without losing saved context.

This fixture does not validate uninterrupted activity, real authentication,
remote concurrency control, or an actual network reconnection protocol.
