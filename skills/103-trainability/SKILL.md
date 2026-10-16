---
name: trainability
description: >-
  Designs instruction and independent skill checks when tickets say "replace the demo with practice exercises", "people finish the course but cannot do the job", or "write training with a separate skills check". Not for learning through use (see learnability), topic coverage (see comprehensiveness), or current task success (see usability).
---
# Trainability

## Definition and scope

Trainability means instruction and practice enable the target audience to acquire
required task skills. Build a teaching intervention with separate assessment;
distinguish learning through product use (`learnability`), topic breadth
(`comprehensiveness`), and present task performance (`usability`).

## Use when / Don't use when

- Apply to a course, tutorial, exercise pack, instructor guide, or training sandbox
  whose learners must later perform a specified task without answer-bearing help.
- Route ordinary product discovery without a lesson intervention to `learnability`.
- Route adding neglected documentation subjects to `comprehensiveness`; exposing
  material does not establish that instruction taught the intended skill.

## Workflow

1. Clarify: Read actual task code, operating docs, current lessons, exercise
   fixtures, and prerequisite records before prescribing a curriculum.
   If a lesson teaches behavior the product no longer supports, then identify
   the version mismatch and resolve it before designing skill assessment.

2. Specify: Align target skills, prerequisites, instruction, practice, feedback,
   assessment cases, support limits, and instructional version.
   If the user requests practical training, then offer this intervention record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Learner/skill: named audience, known prerequisites, and the requested repository task.
   Intervention: explanation, guided exercise, feedback, and separate unaided assessment.
   Trial scope: 2 changed-instance assessment cases covering contrasting decisions.
   Oracle: expected outcome and reasoning tied to current code/docs, not attendance.
   Support: answer-bearing guide available in practice, withheld during unaided assessment.
   Environment: synthetic resettable sandbox; no production mutation by default.
   Evidence: material revision, exercise state, hints, assessment outputs, and skill gaps.
   Limits: no credential, retention, or operational authorization inferred from completion.
   ```

   Ask at most three groups about skills/prerequisites; permitted environment and
   instruction modes; and assessment support, criteria, or later-use expectations.
   Begin a lesson/fixture proposal with unresolved training decisions visible.
   If no assessment target exists, then propose the illustrative case trial and
   confirm with the user/stakeholder before setting the pass rule.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [instruction patterns](./references/design-patterns.md)
   when producing skill-aligned exercises, feedback, and assessment fixtures.
   If the lesson reveals the assessment answer, then replace the assessment
   instance while preserving the same target decisions and difficulty assumptions.
   If exercises change shared state, then provide a reset and inspect its result
   so a later learner cannot pass because an earlier learner finished the work.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Rehearse lessons and resets against current behavior; check outputs
   and reasoning on separate assessment cases with actual support recorded.
   If only lesson attendance or guided completion is known, then mark independent
   skill acquisition unverified rather than awarding it through the lesson checklist.

5. Report: Deliver the lesson, practice/reset assets, assessment key, observed
   assistance, version fit, and skills not demonstrated.
   If a learner passes a sandbox assessment, then limit the conclusion to that
   assessment; do not infer production permission or retention beyond the trial.

## Specification patterns

- **Teaching outcome:** After `{instruction_and_practice}`, `{learner_prerequisites}`
  shall perform `{target_skill}` on `{separate_assessment_instances}` under
  `{support_limits}`, meeting `{confirmed_output_and_reasoning_rule}`.
- **Training reproducibility:** For `{material_and_product_revision}`, `{exercise}`
  shall start from `{declared_state}`, produce `{observable_outcome}`, and reset
  to `{clean_state}`, verified by `{rehearsal_and_next_learner_checks}`.

Use the illustrative assessment trial if no training criterion is available;
confirm with the user/stakeholder. Ask the user which skills need later retention evidence.

## Rules of thumb

- Do map each lesson objective to a separately assessed task decision; covering
  slides about a concept cannot substitute for demonstrating the taught skill.
- Don't reuse a guided exercise's exact answer as the independent assessment;
  the learner can reproduce the lesson without acquiring its decision skill.
- Do reset exercise state and verify the next learner's starting conditions;
  inherited completed work can produce a false training pass without any learner action.
- Do tag instruction and answer keys with the product behavior they teach;
  a polished obsolete lesson trains a decision the current system rejects.
- Don't count attendance, page views, or quiz recall alone as task-skill evidence
  when the objective is performing a repository or operational workflow.
- Do separate instructor hints from assessed unaided work; a facilitator's
  successful diagnosis must not be credited as the trainee's acquired skill.

## Verification

Use lesson rehearsal, sandbox reset checks, objective-to-assessment mapping,
and learner task observation categories. Compare practice instructions and keys
with the actual product revision. Inspect initial, changed, and reset fixture
states. Record assessment outputs, reasoning, hints, and unassessed objectives;
successful asset generation alone does not establish effective instruction.

## Done checklist

- [ ] Trace every claimed skill to instruction, practice, and an assessment decision.
- [ ] Reconcile lesson behavior and answer keys with the current product revision.
- [ ] Rehearse practice from declared synthetic starting state to expected output.
- [ ] Verify reset removes prior learner results and restores the next starting state.
- [ ] Inspect assessment cases for answer leakage from guided examples.
- [ ] Record learner outputs, reasoning, and actual assistance separately.
- [ ] List unassessed skills and later-retention evidence that remains unavailable.
- [ ] Distinguish assessment success from operational authorization or certification.

## Failure modes

- Delivering a polished slide deck with no assessable task skill.
- Letting the walkthrough reveal the supposedly independent assessment answer.
- Passing a learner because exercise state was already completed.
- Teaching an obsolete operation against a current-version answer key.
- Reporting independent competence from attendance or facilitator rescue.

## References

- Read [instruction patterns](./references/design-patterns.md) when aligning
  objectives, sandbox state, feedback, and independent assessment.
- Read [import-recovery lesson](./references/worked-example.md) when designing
  a version-bound lesson with resettable practice and a new assessment case.
