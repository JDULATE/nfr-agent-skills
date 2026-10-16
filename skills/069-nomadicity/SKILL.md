---
name: nomadicity
description: >-
  Restores useful work after relocation when tickets say "resume my draft after reconnecting elsewhere", "pick up where I left off at the next site", or "reopen saved work after changing networks". Not for uninterrupted activity during movement (see mobility) or outage restoration (see recoverability).
---

# Nomadicity

## Definition and scope

Nomadicity means useful operation can be reestablished after a user or device
relocates between environments. Preserve enough task context to resume after the
declared pause and reconnection; distinguish activity continuing during movement
(`mobility`) and restoring a disrupted service (`recoverability`).

## Use when / Don't use when

- Apply when saved work cannot be reopened after disconnecting and reconnecting elsewhere.
- Apply when task context still points at resources from the previous location.
- Route continuity during the movement itself to `mobility`.
- Route software runtime migration to `portability`.
- Ask the user which subject relocates and what work must resume; do not infer that
  a successful reconnect has restored useful operation.

## Workflow

1. Clarify: Read saved task/context formats, local persistence, connection bootstrap,
   identity checks, endpoint selection, and post-connect behavior before specifying.
   Identify the pre-move task, pause boundary, new environment, and useful resumed action.
   If the request requires no pause during movement, then clarify the `mobility`
   boundary rather than presenting a suspend/resume design as equivalent.

2. Specify: Record saved work, acknowledged state, pending changes, endpoint rebinding,
   revalidation, conflicts, and the resumed action's required result.
   If no resumption contract exists, then propose labeled illustrative defaults:
   preserve the requested task snapshot, rebind confirmed resources after reconnect,
   and verify an actual resumed edit; confirm with the user/stakeholder.
   Ask for any resumption deadline rather than guessing a universal duration.

3. Design/Implement: Read [post-relocation decisions](./references/design-guide.md)
   when choosing saved context, resource rebinding, or resume validation.
   If a checkpoint holds an old location's endpoint, then resolve the current
   resource through task identity. If permissions or remote state changed, then
   revalidate and surface the decision before applying saved writes.
   If the task cannot be resumed, then preserve its context and explain the gap
   instead of opening an empty task as if nothing had been lost.

4. Verify: Save the task, suspend, relocate, reconnect, and perform the required
   action from the saved context. Inspect local and remote work after resumption.
   If connectivity succeeds but the task cannot be used, then report resumption
   incomplete. Retain unresolved conflicts, failed reconnects, and unfinished work.
   Read [draft relocation example](./references/worked-example.md) for a filled
   pause/rebind/resume sequence and an explicit changed-remote-state case.

5. Report: Return the relocation model, saved context, rebinding/revalidation
   results, resumed task outcome, and remaining conflicts.
   If operation paused during movement, then state that accepted boundary and
   do not report uninterrupted mobility.

## Specification patterns

- **Resume:** After `{declared_pause_and_relocation}`, `{subject}` shall resume
  `{task}` from `{saved_context}` in `{new_environment}` and complete
  `{useful_action}`, verified by `{resumed_state_and_output}`.
- **Rebinding:** Saved `{location_bound_resources}` shall be resolved through
  `{stable_task_identity_and_current_policy}`; unavailable resources shall produce
  `{explicit_preserved_context_result}`.
- **Conflict:** When `{saved_and_current_state}` disagree, resumption shall
  follow `{confirmed_conflict_policy}` rather than `{silent_overwrite_or_reset}`.

For absent numeric targets, use the illustrative saved-task proposal in Specify
and confirm with the user/stakeholder. Reconnection alone is not the acceptance predicate.

## Rules of thumb

- Do make the suspension/resumption boundary explicit; a post-move reopened task
  cannot establish that the activity continued during the journey.
- Do save resumable task context rather than just a former network address;
  the address may reconnect while the user's actual work remains unavailable.
- Do rebind location-dependent handles through the saved task identity; restoring
  an old endpoint literally can select an unavailable or different resource.
- Do verify a useful action on the resumed task, not merely successful login
  or link establishment; those events do not establish that saved work is usable.

## Verification

Use relocation fixtures, saved-context inspection, reconnect integration,
permission revalidation, and remote-revision comparison categories.
Retain the original snapshot and pending edits through failed reconnects.
Exercise a changed endpoint and a changed remote revision separately.
Check current authorization using the existing policy before applying saved writes.
Compare source task meaning, pending changes, and resumed action output.
Keep conflict and missing-resource outcomes visible instead of silently resetting.
State explicitly that the accepted procedure includes a pause during relocation.

## Done checklist

- [ ] Identify the relocating subject and declared suspension boundary.
- [ ] Capture the required task state and pending changes.
- [ ] Record old and new environment resource bindings.
- [ ] Revalidate current resource identity and authority after reconnect.
- [ ] Complete a useful action from the restored task context.
- [ ] Surface remote conflicts without silently replacing saved work.
- [ ] Preserve context when reconnection or resource resolution fails.
- [ ] Separate post-relocation resumption from active-movement continuity.

## Failure modes

- Calling successful login proof that the task resumed.
- Reopening an empty task while silently discarding saved changes.
- Restoring an old endpoint without checking the current resource binding.
- Overwriting changed remote state with an old saved snapshot.
- Advertising uninterrupted mobility for a procedure that explicitly suspends.

## References

- Read [post-relocation decisions](./references/design-guide.md) when choosing
  saved-context fields, resource rebinding, and resume validation.
- Read [draft relocation example](./references/worked-example.md) when verifying
  useful post-move work and preserving an unresolved conflict.
