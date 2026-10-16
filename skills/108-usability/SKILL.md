---
name: usability
description: >-
  Checks task interaction when asked "observe checkout errors", "test unaided completion", or "measure recovery effort". Before routing ease complaints, Ask the user: task success/effort, learning, feelings, or appearance? Not for learning (see learnability), feelings after use (see likeability), or visual appeal (see attractiveness).
---
# Usability

## Definition and scope

Usability means the intended audience can complete its tasks in the stated
usage context. Accept the real task outcome, effort, errors, and recovery under
explicit support conditions; distinguish acquired ability (`learnability`),
subjective response (`likeability`), and visual appeal (`attractiveness`).

## Use when / Don't use when

- Apply when users cannot achieve a goal, select the wrong object, lose work,
  or need avoidable intervention to finish an interaction.
- Route improvement of novice acquisition specifically to `learnability`.
- Route visual recognition obstacles to `legibility` and interaction barriers
  for specified audiences to `accessibility-access-control` as appropriate.
- Route failed backend business rules to `correctness`; include them as task
  blockers here without disguising a behavior defect as a cosmetic rewrite.

## Workflow

1. Clarify: Inspect task-flow code, forms, state persistence, error paths, docs,
   and existing user/task evidence before proposing an interaction change.
   If the stated goal is merely a button click, then identify the actual result
   the user needs and inspect how the system establishes that result.

2. Specify: Define audience, context, task input, success state, prohibited
   outcomes, support, effort/error accounting, and recovery conditions.
   If the user asks for a practical fix, then propose this task record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Audience/context: intended users, documented device/context, requested workflow.
   Success: authoritative task result for the correct object, not a completion animation.
   Trial: 0 unrecovered critical task errors across the agreed synthetic scenarios.
   Effort: record elapsed task time, backtracking, corrections, and help separately.
   Assistance: existing documented aids; facilitator rescue is an assisted outcome.
   Recovery: preserve valid work after a correctable input error, subject to task rules.
   Constraints: retain authorization, required checks, and consequences of final actions.
   Evidence: input, interaction trace, actual result state, errors, recovery, and assistance.
   Status: proposed scenario criteria; audience observations are not yet available.
   ```

   Ask at most three groups about users/goals/context; success, mistakes and
   consequences; and support, effort or recovery constraints. Continue to a
   reversible interaction design grounded in observed blockers.
   If no numeric target exists, then use the illustrative error trial and confirm
   with the user/stakeholder before accepting its scenario scope or criterion.

3. Design/Implement: Read [task-outcome practices](./references/design-patterns.md)
   when reducing selection errors, preserving work, or exposing correction paths.
   If the fix bypasses a required check to speed completion, then retain that
   check and improve its interaction instead of redefining success around its removal.
   If an error is correctable, then preserve permitted input and point to the
   failed field/action; inspect resulting state before claiming recovery works.

4. Verify: Execute goal-based scenarios with intended users where available;
   retain actual result, errors, work lost, corrections, help, and effort.
   If a success message appears without the correct persisted outcome, then
   record task failure even when the visible interaction seems smooth.

5. Report: Return the changed obstacle, task outcomes, effort/error evidence,
   recovery observations, assistance, and contexts not exercised.
   If only developer checks were run, then separate functional rehearsal from
   audience task-performance evidence and leave the latter unverified.

## Specification patterns

- **Task outcome:** Under `{usage_context_and_support}`, `{audience}` shall achieve
  `{authoritative_goal_state}` for `{task_inputs}`, meeting `{confirmed_error_and_effort_rules}`
  as verified by `{interaction_trace_and_result_check}`.
- **Recovery:** After `{correctable_interaction_error}`, preserve `{valid_work}`
  and enable `{permitted_correction}` without `{prohibited_duplicate_or_wrong_object_result}`,
  verified by `{recovery_scenario_and_authoritative_state_inspection}`.

Use the illustrative task-error trial when no criterion is known; confirm with
the user/stakeholder. Ask the user which scenarios, mistakes, and effort costs matter.

## Rules of thumb

- Do accept the correct task result on the intended object, not a clicked final
  control; a smooth flow that submits the wrong recipient is still a failed task.
- Don't remove mandatory review or authorization to improve completion time;
  bypassing the task's required constraints does not improve its valid completion.
- Do preserve permitted valid work after correctable input errors; forcing full
  re-entry adds task effort unrelated to the correction the user needs to make.
- Do distinguish independent, assisted, abandoned, and incorrect task outcomes;
  facilitator rescue must not disappear inside a nominal completion rate.
- Do exercise correction from the mistaken selection through the final result;
  a visible undo affordance is insufficient if the wrong-object effect persists.
- Don't infer better task performance from a preference vote or visual refresh;
  inspect goal outcomes and effort under the stated interaction conditions.

## Verification

Use goal-based interaction trials, form-state regression, and authoritative-result
inspection categories. Test normal completion, wrong-object selection, invalid
input, correction, abandonment, and duplicate final action where applicable.
Record context, inputs, support, task time, help, errors, and remaining work.
Inspect the actual state after apparent success and recovery; separate functional
checks from intended-audience performance and from subjective preference.

## Done checklist

- [ ] Define the goal with an authoritative result and prohibited wrong outcomes.
- [ ] Trace observed interaction blockers to the changed controls or state behavior.
- [ ] Verify successful completion affects the correct object and satisfies task constraints.
- [ ] Exercise invalid input and inspect preservation of permitted valid work.
- [ ] Verify a mistaken selection can be corrected through to the final result.
- [ ] Retain independent, assisted, abandoned, and failed outcomes distinctly.
- [ ] Report effort, corrections, and help rather than only a final success count.
- [ ] Limit audience and context claims to observed trials or mark them unverified.

## Failure modes

- Accepting a completion animation while the real task result is wrong or absent.
- Improving speed by dropping the check that makes completion valid.
- Erasing correct input when another field fails validation.
- Counting a facilitator-rescued task as independent success.
- Treating an attractive or preferred flow as proven task-performance improvement.
- Showing a correction control without reversing the mistaken task outcome.

## References

- Read [task-outcome practices](./references/design-patterns.md) when selecting
  result oracles, preserving work, or verifying meaningful correction.
- Read [recipient-form example](./references/worked-example.md) when tracing
  selection, validation, correction, and actual task state rather than button clicks.
