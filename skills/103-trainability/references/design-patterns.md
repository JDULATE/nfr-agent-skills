# Instruction patterns

Design training assets only for the authorized skills and practice environment.

## Objective/decision/assessment alignment

- Use when instruction promises a practical skill rather than information exposure.
- Trade-off: a concrete objective narrows the lesson; broad background may remain
  useful but must not inflate the claimed assessed competence.
- Verify: map the objective to a decision and observable output in a separate
  assessment case; mark objectives without such evidence unassessed.

## Guided practice and independent case

- Use when worked steps or feedback are needed during instruction.
- Trade-off: answer-bearing guidance can teach a procedure but also leak the
  assessment answer if the same instance is reused.
- Verify: rehearse the guided case, then assess another instance requiring the
  same skill; record instructor cues instead of crediting them to the learner.

## Resettable synthetic exercise

- Use when the lesson changes files, records, job state, or other shared fixtures.
- Trade-off: reset support adds maintenance but prevents one learner inheriting
  another's completed work or an unreproducible failure state.
- Verify: inspect starting state, expected exercise effect, and post-reset state;
  check the next learner cannot pass before performing the assessed action.

## Product/material revision binding

- Use when instructions depend on behavior or configuration that can change.
- Trade-off: version binding exposes maintenance work instead of letting a
  visually polished lesson silently drift from current behavior.
- Verify: compare the lesson's operation and answer key with current source/docs;
  flag drift and avoid teaching unsupported recovery or production actions.
