---
name: functionality
description: >-
  Defines required capabilities when tickets say "we need an export operation", "there is no way to cancel a queued export", or "list what the export service must do". Not for wrong existing behavior (see correctness), task fit (see suitability), or achieved outcomes (see effectiveness).
---

# Functionality

## Definition and scope

Functionality means the system provides the explicitly required operations or
capabilities. Define each capability through an actor, preconditions, observable
result, and supported state effects.
Separate capability presence from task fit (`suitability`), stakeholder outcome
attainment (`effectiveness`), and incorrect existing behavior (`correctness`).

## Use when / Don't use when

- Apply when an export service lacks a required operation or needs a concrete
  catalogue of supported capabilities.
- Include reachable implementation paths, not only menu labels or method names.
- Route a present operation's wrong branch result to `correctness`.
- Route whether an available export serves a particular recipient task to
  `suitability`.
- Route whether use actually achieves the stakeholder's goal to `effectiveness`.

## Workflow

1. Clarify: Read entrypoints, handlers, state transitions, contracts, docs, and
   existing capability tests before specifying additions.
   Identify what actors can actually invoke and observe.
   If the requested capability has no result or supported state boundary, then
   Ask the user what operation must exist and what establishes its completion.

2. Specify: Record the required operations, actors, inputs, preconditions,
   results, state effects, and unsupported states.
   If no target is given, then propose a labeled illustrative default:
   every named operation has an invocable path and its declared observable effect
   for the supplied cases; confirm with the user/stakeholder.
   Ask at most three questions on capability scope, actors, and state behavior
   before adding an operation.

3. Design/Implement: Read [capability decisions](./references/design-guide.md)
   when adding an entrypoint and its actual state effect.
   If a cancellation operation is required only for queued jobs, then expose that
   precondition and implement the queued-state transition rather than advertising all-state cancellation.
   If a handler is only a placeholder, then keep the capability unimplemented
   until its required result exists.

4. Verify: Invoke each required operation through the actual service boundary
   and inspect its declared result and effect.
   If only a method or documentation entry exists, then report capability absence
   rather than accepting the catalogue label as implementation evidence.

5. Report: Return the capability catalogue, implemented paths, supported states,
   observed effects, and gaps.
   If capability presence is established, then keep separate claims about speed,
   safety, task fit, and outcome attainment unverified unless also evaluated.

## Specification patterns

- **Operation:** For `{actor_and_preconditions}`, the system shall provide
  `{operation}` accepting `{inputs}` and producing
  `{observable_result_and_state_effect}`, verified by `{actual_entrypoint_fixture}`.
- **State boundary:** `{operation}` shall support `{declared_states}` and return
  `{unsupported_state_result}` in `{other_states}`, checked by
  `{state_specific_invocation_and_effect_inspection}`.

Use the illustrative invocable-capability proposal in Specify when no numbers
are supplied; confirm with the user/stakeholder before accepting the catalogue.

## Rules of thumb

- Define an operation by what the actor can obtain from it, not by a method name;
  a cancel handler that only acknowledges still lacks the required cancellation effect.
- Keep supported states in the capability claim; queued-job cancellation does not
  establish cancellation of work already executing.
- Distinguish a catalogue entry from an invocable service path; a disabled button
  or unwired route does not supply the operation it names.
- Keep capability presence separate from quality guarantees; an export operation
  can exist without evidence that it meets a response-time or task-fit objective.

## Verification

Use capability-to-entrypoint review, service invocation, and state-effect fixtures.
Trace the actual handler rather than calling a helper unavailable to the actor.
Exercise each named operation in supported and unsupported states.
Retain absent operations and placeholder results in the gap list.
Check that observed effects match the declared capability boundary.
Use concurrency checks separately if the operation promises concurrent state
protection; a sequential fixture cannot establish that guarantee.
Do not infer task suitability from a successful invocation alone.

## Done checklist

- [ ] Enumerate required operations and actors.
- [ ] State each operation's inputs and observable result.
- [ ] Identify the actual invocable implementation path.
- [ ] Exercise supported-state behavior and required effects.
- [ ] Check declared unsupported states without false success.
- [ ] Record placeholders, unwired operations, and remaining gaps.
- [ ] Separate capability evidence from untested quality claims.

## Failure modes

- Treating a UI label as an implemented operation.
- Returning accepted without the required state effect.
- Advertising cancellation in states the implementation does not support.
- Claiming task fit or outcome success solely because an operation can be called.

## References

- Read [capability decisions](./references/design-guide.md) when adding
  observable operations and explicit supported-state boundaries.
- Read [export operation example](./references/worked-example.md) when checking
  a capability catalogue against actual invocation and state effects.
