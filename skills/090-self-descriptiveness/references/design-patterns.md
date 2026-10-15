# Explaining state and action in context

Tie wording to actual application states and effects. Visible labels can be true
strings in a test while conveying the wrong state to the intended user.

## State/action view matrix

- **Use when:** Different object states permit different actions. Map source state,
  affected object, visible status, enabled action, and expected effect together.
- **Trade-off:** Too many labels can overwhelm a view; merging states that allow
  different actions can remove the very distinction the user needs.
- **How to verify:** Exercise the matrix through normal views, inspect actual guards,
  and ask what state/action the user infers without showing the answer key.

## Current disabling reason

- **Use when:** A control cannot run because a current prerequisite is unmet.
  Show the actual reason and permitted next step alongside the affected action.
- **Trade-off:** Static explanatory text can become stale when state changes;
  the source of the action guard and the displayed reason must stay aligned.
- **How to verify:** Change the prerequisite, inspect action availability and reason,
  and reject a generic reason that describes a different object's state.

## Pending, confirmed, and retained-state cues

- **Use when:** An initiated action can still fail or leave earlier state intact.
  Expose pending versus confirmed result and what remains after an error.
- **Trade-off:** Optimistic interaction may be useful, but success wording must not
  imply a confirmed effect the system has not established under its actual contract.
- **How to verify:** Pause, complete, and fail the action; compare actual state,
  available next actions, and user-inferred effect at each point.

An illustrative state/action task bound is 0 incorrect inferences on the agreed
fixtures; confirm with the user/stakeholder. This says nothing about message timing,
notification delivery, or general audience success outside those states.
