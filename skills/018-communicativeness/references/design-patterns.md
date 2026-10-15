# Event-to-message patterns

Choose delivery behavior from real event semantics and the agreed recipient need.

## Event/message matrix

- Use when accepted, running, completed, and failed are distinct business events.
- Trade-off: more explicit states can require more message handling; a shorter
  exchange can omit information a user needs before choosing an action.
- Verify: map each visible statement to its source event and inspect its next action;
  a queue receipt must not produce a completed-result claim.

## Task-correlated monotonic outcome

- Use when progress or notifications can arrive out of order or be replayed.
- Trade-off: retaining task/revision identity requires state; transport order
  alone may not establish the right business-state precedence.
- Verify: replay older progress after completion for the same task and confirm
  the completed outcome remains; separately handle a legitimately newer attempt.

## Persistent retrieval point

- Use when the user can leave before a result is ready.
- Trade-off: history adds storage and lifecycle decisions; a transient message
  is simpler but can be missed permanently.
- Verify: leave, complete the task, return, and retrieve its actual result through
  the agreed channel without manufacturing display/read receipts.

## Outcome and delivery separation

- Use when a task succeeds but sending its feedback fails.
- Trade-off: delivery retries improve the chance of communication but must not
  rerun the business operation merely to recreate its message.
- Verify: fail delivery, retry the message, and inspect unchanged business outcome;
  report transport, render, and acknowledgement evidence as distinct stages.
