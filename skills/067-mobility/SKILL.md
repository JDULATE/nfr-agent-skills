---
name: mobility
description: >-
  Preserves active client work through movement when tickets say "keep this upload running as networks change", "switch connections without restarting the task", or "roaming starts the upload again". Not for resuming after a relocation pause (see nomadicity) or moving software platforms (see portability).
---

# Mobility

## Definition and scope

Mobility means a moving user, device, or service preserves the agreed continuity
of its activity. Apply this entrypoint to active client work across network-path
movement, with a declared logical task and handoff boundary; distinguish resuming
after relocation (`nomadicity`) and moving execution platforms (`portability`).

## Use when / Don't use when

- Apply when client path changes restart an upload that should remain active.
- Apply when old and new connections compete to own the same ongoing task.
- Route deliberate suspension followed by post-move resumption to `nomadicity`.
- Route adapting the program to another runtime to `portability`.
- Ask the user what moves and what continuity means; a new transport connection
  need not mean a new application task, but an explicit task restart is different.

## Workflow

1. Clarify: Read client task state, transport construction, routing/identity,
   acknowledgment handling, permissions, and existing movement behavior first.
   Identify the moving subject, logical activity, handoff conditions, and required continuity.
   If an interruption budget or allowed fallback is unknown, then Ask the user
   before promising that an arbitrary path change is seamless.

2. Specify: Record the stable task identity, old/new paths, handoff ownership,
   acknowledged progress, pending inputs, allowed interruption, and completion rule.
   If no contract exists, then propose labeled illustrative defaults:
   keep the requested task active, preserve its acknowledged prefix and pending input,
   and avoid a user restart in the declared handoff; confirm with the user/stakeholder.
   Leave numeric gap or latency limits open rather than guessing them.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [active handoff decisions](./references/design-guide.md)
   when choosing task/path separation and overlap handling.
   If a path identifier is used as task identity, then separate those identities.
   If both paths may act during handoff, then define current ownership and fence the
   retired path. If the target cannot support the declared continuity, then expose
   that limitation rather than silently substituting a suspend-and-reopen workflow.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Change the path during active work and inspect task identity,
   acknowledged/pending progress, in-flight ownership, and completion.
   If the client creates a replacement task or requires a user restart, then
   report the continuity requirement failed even if the upload eventually finishes.
   Preserve failed handoffs, timeouts, and unfinished tasks.
   Read [upload handoff example](./references/worked-example.md) for a filled overlap case.

5. Report: Return the movement model, application continuity evidence, path changes,
   interruption observations, and unsupported transition conditions.
   If only an overlapping-path fixture was exercised, then do not claim arbitrary
   network movement or permanent-disconnection continuity.

## Specification patterns

- **Active continuity:** During `{declared_client_path_change}`,
  `{logical_activity}` shall retain `{identity_progress_and_pending_input}`
  without `{user_restart_or_forbidden_transition}`, verified by `{task_trace}`.
- **Handoff ownership:** Across `{old_and_new_paths}`, only
  `{current_handoff_owner}` shall advance `{task_state}`; retired-path messages
  shall follow `{confirmed_fence_rule}`.
- **Continuity bound:** The movement shall satisfy `{confirmed_interruption_budget}`
  measured at `{application_activity_boundary}`, reporting `{unfinished_handoffs}`.

For no numeric target, offer the illustrative active-task defaults in Specify
and confirm with the user/stakeholder. Keep an unspecified time budget unaccepted.

## Rules of thumb

- Do bind the active task to application identity rather than the current network
  path; replacing a connection must not automatically create a replacement upload.
- Do hand ownership from the old path to the new one explicitly during overlap;
  keeping both paths connected does not authorize both to advance the task.
- Do keep path reconnection inside the active task lifecycle when continuity is
  required; a successful suspend-and-reopen flow meets a different acceptance question.

## Verification

Use client path-change simulation, task-state inspection, handoff ordering,
and acknowledgment/replay checks.
Verify the same logical task before, during, and after movement.
Compare committed progress, pending inputs, completion identity, and user-visible
restart requirements.
Exercise delayed old-path acknowledgments and an unavailable replacement path.
Check that retirement follows the declared replacement-readiness condition;
do not destroy the sole usable route before that condition holds in an overlap test.
Check current authorization under the existing policy when a new path is established.
Retain raw traces, missing acknowledgments, interruption observations, timeouts,
and unfinished work instead of counting later completion as proof of continuity.
Separate transport behavior from application activity and do not claim every
possible network handoff from one controlled case.

## Done checklist

- [ ] Identify the moving subject and application continuity boundary.
- [ ] Separate stable task identity from old/new path identity.
- [ ] Resolve allowed interruption and fallback decisions.
- [ ] Exercise a path change while the task remains active.
- [ ] Verify ownership and retired-path fencing during overlap.
- [ ] Preserve acknowledged progress and pending inputs.
- [ ] Check completion without a user-requested task restart.
- [ ] Report unsupported no-overlap or unavailable-path cases.

## Failure modes

- Creating a new upload whenever its network connection changes.
- Reporting continuity because a restarted task eventually completes.
- Letting both path owners advance the same task during overlap.
- Destroying the old route before the declared replacement readiness condition.
- Calling an unmeasured interruption seamless.

## References

- Read [active handoff decisions](./references/design-guide.md) when choosing
  task/path identity, overlap ownership, and continuity boundaries.
- Read [upload handoff example](./references/worked-example.md) when distinguishing
  active task continuity from a successful post-move restart.
