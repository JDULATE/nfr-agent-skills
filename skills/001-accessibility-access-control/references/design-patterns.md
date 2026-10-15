# Separate branch practices

Choose the branch first. Accessible interaction and action permission are independent claims.

## Accessibility: semantic task controls and errors

- Use when control purpose/state or an error is unavailable in the audience's interaction mode.
- Trade-off: exposed names and feedback must match the actual task; adding labels
  without correct state/meaning can mislead rather than remove the barrier.
- Verify: inspect the presented control/error meaning and complete the actual task
  under the agreed input/assistive conditions, including invalid input and correction.

## Accessibility: focus across state transitions

- Use when dialogs, validation, navigation, or removed elements interrupt task focus.
- Trade-off: automatically moving focus can itself disrupt work; select the next
  task-relevant point rather than prescribing one location for every interaction.
- Verify: trace opening, operation, error, closing, and return with the intended
  input method; inspect where the user continues and whether the next action remains operable.

## Access Control: actor/action/resource matrix

- Use when role labels alone do not express team, object, ownership, or state limits.
- Trade-off: finer policy context improves precision but requires a trusted source
  and explicit decisions for missing, changed, or conflicting context.
- Verify: exercise allowed and forbidden matrix cells, including a valid role on
  a different resource scope; inspect the actual effect, not just response text.

## Access Control: final enforcement and changed authority

- Use when direct/background calls or stale decisions can bypass a guarded screen.
- Trade-off: boundary enforcement and policy re-evaluation can affect in-flight work;
  revocation timing must be supplied by the stakeholder rather than invented.
- Verify: call alternate entrypoints, change authority between view and effect,
  and inspect the confirmed decision's effect with valid controls retained.

Do not infer a standards pass, legal duty, or permission policy from the catalogue label.
