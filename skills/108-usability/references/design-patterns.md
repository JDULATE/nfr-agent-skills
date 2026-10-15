# Task-outcome practices

Choose changes from a concrete audience goal and the actual task-result contract.

## Authoritative result oracle

- Use when a flow reports success before the meaningful result is clear.
- Trade-off: checking actual state requires a result observer beyond the UI,
  but prevents celebrating a smooth interaction that affected the wrong object.
- Verify: trace task input and selected object through confirmation to persisted
  outcome; separate pending acceptance from the business result.

## Correctable-input preservation

- Use when one invalid field causes users to repeat otherwise valid work.
- Trade-off: retained input can reduce correction effort, but sensitive or stale
  values may require separate policy; do not preserve prohibited data by default.
- Verify: trigger the field error, inspect permitted retained values, correct it,
  and check the final result without weakening the required validation rule.

## Mistake-to-correction path

- Use when an incorrect selection or premature action can be corrected.
- Trade-off: a true reversal may be impossible for some actions; a cosmetic undo
  affordance must not promise a reversal the underlying task cannot provide.
- Verify: follow the erroneous action through correction and inspect remaining
  effects; disclose irreversible actions and agreed alternative remedies.

## Outcome/effort/support record

- Use when an apparently improved flow changes assistance or completion accounting.
- Trade-off: recording traces and effort costs more than counting finish clicks
  but exposes the difference between independent completion and rescue.
- Verify: classify actual result, help, abandonment, errors, corrections, and effort;
  compare equivalent goals and contexts rather than preference or screenshot ratings.
