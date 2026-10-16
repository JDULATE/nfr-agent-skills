---
name: controllability
description: >-
  Makes runtime state changes controllable when tickets say "pause intake without killing active jobs", "resume only this worker", or "the stop command says OK but work keeps starting". Not for status display (see visibility), fleet policy (see manageability), or whole operator tasks (see operability).
---

# Controllability

## Definition and scope

Controllability means authorized operators can drive a system into a specified
runtime state and establish that the transition took effect. Define the command,
target, transition, and feedback; distinguish a complete operator task
(`operability`), fleet policy administration (`manageability`), and
read-only state inference (`observability`).

## Use when / Don't use when

- Apply when pause, resume, or stop acknowledges a request without reaching its target state.
- Apply when operators cannot address the intended worker or interrupt its intake separately.
- Route a full operational procedure to `operability`.
- Route policy assignment and reconciliation across installations to `manageability`.
- Route adding test-only controls to `testability`.

## Workflow

1. Clarify: Read command handlers, worker loops, authorization, state ownership,
   and operational docs before defining a control.
   Identify the authorized actor, target identity, requested state, and in-flight policy.
   If "stop" could mean pause intake, abort active work, or terminate the process,
   then Ask the user which state and effects are intended before implementing it.

2. Specify: Record preconditions, allowed transitions, command identity,
   acknowledgment meaning, completion evidence, supersession, and unknown outcomes.
   If no control record exists, then propose labeled illustrative defaults:
   pause new intake while active work finishes, resume through the same control
   channel, and require worker-state feedback; confirm with the user/stakeholder.
   Ask the user for any required completion deadline instead of inventing one.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [control design](./references/design-guide.md) when
   selecting a target-state command and a feedback path.
   If acknowledgment only means queued, then expose a separate applied-state result.
   If pausing work also disables its command reader, then separate control intake.
   If concurrent commands can supersede each other, then define an ordering fence
   and reject stale transitions rather than guessing the final intent.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Command pause, observe intake cessation, let active work follow the
   agreed policy, then command resume. Check target isolation and stale-command handling.
   If feedback is absent, then report unknown rather than completing the transition
   on acknowledgment alone. Retain failed and unfinished command attempts.
   Read [worker pause example](./references/worked-example.md) when testing
   acknowledgment, applied state, and a later resume independently.

5. Report: Return the control contract, state transitions, applied-state evidence,
   target boundaries, and incomplete or superseded operations.
   If the actor lacks authority or the target state cannot be confirmed, then
   report that limit without claiming a completed operational change.

## Specification patterns

- **State command:** For `{authorized_actor_and_target}`, command
  `{requested_state}` shall produce `{applied_state_and_inflight_policy}`
  under `{preconditions}`, confirmed by `{worker_feedback}`.
- **Ordering:** A command superseded by `{newer_control_intent}` shall not
  reverse `{current_applied_state}`; report `{superseded_or_unknown_result}`
  using `{target_and_command_identity}`.

Use the illustrative pause/resume proposal in Specify for an unquantified request
and confirm with the user/stakeholder. Keep an unstated timing bound unresolved.

## Rules of thumb

- Do distinguish accepted intent from applied worker state; a queued pause
  cannot establish that the worker has stopped claiming new jobs.
- Do express a requested end state rather than a blind toggle when the operator
  must verify a specific state; duplicate toggles can reverse that intent.
- Do keep the control reader reachable while work intake is paused; otherwise
  the same pause can remove the operator's path to resume.
- Do fence a superseded command against the newer applied intent; an old resume
  must not silently undo a later pause for the same worker.

## Verification

Use command-path integration, worker-state inspection, concurrency simulation,
and authorization checks. Observe claims after applied pause, not just return codes.
Verify existing active work follows the chosen finish/abort policy.
Exercise duplicate commands, delayed application, supersession, absent feedback,
and an unrelated worker as a scope control.
Keep denied commands and failed transitions visible in the command ledger.
Use the existing permission model; a runtime control is not a test backdoor.
Review explicit completion and unknown states before adding automatic recovery actions.

## Done checklist

- [ ] Resolve the requested runtime state and in-flight work policy.
- [ ] Bind actor authority and target identity to the command.
- [ ] Distinguish queued acknowledgment from applied-state feedback.
- [ ] Demonstrate that pause blocks new claims without disabling resume.
- [ ] Exercise duplicate and superseded commands.
- [ ] Verify an unrelated worker remains unchanged.
- [ ] Report missing feedback or incomplete transitions as unresolved.

## Failure modes

- Reporting a worker paused because its command was accepted by a queue.
- Pausing the only reader capable of receiving resume.
- Reversing intent by retrying a toggle after an ambiguous response.
- Applying an old resume after a newer pause.
- Treating an unknown command outcome as permission to issue a destructive inverse.

## References

- Read [control design](./references/design-guide.md) when defining target states,
  control transport, applied feedback, and supersession.
- Read [worker pause example](./references/worked-example.md) when distinguishing
  accepted commands from actual intake control and verified resumption.
