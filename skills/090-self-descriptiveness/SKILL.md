---
name: self-descriptiveness
description: >-
  Makes an interface or artifact explain its current state, affected object,
  and available actions in context when users say "why is this button
  disabled", "show what state this item is in", or "make the next action
  explain itself". Checks state/action inference at the point of use. Not for
  standalone explanation clarity (see comprehensibility), message timing in a
  conversation (see communicativeness), or backend diagnostic inference alone
  (see observability).
---
# Self-Descriptiveness

## Definition and scope

Self-descriptiveness means an interface or artifact exposes enough context to explain
its current state and available actions. Connect object, state, action conditions,
and effects where the user acts; separate a standalone explanation (`comprehensibility`),
feedback timing (`communicativeness`), and backend inference (`observability`).

## Use when / Don't use when

- Apply when users cannot tell whether work is saved, which object an action affects,
  why a control is disabled, or what the next available action will do.
- Route a separate confusing guide to `comprehensibility` and an unseen progress
  update to `communicativeness` when delivery/timing is the actual problem.
- Route visual recognition of the label to `legibility`; a clear glyph does not
  establish that the label explains current state or permitted action.

## Workflow

1. Clarify: Read state/action code, eligibility rules, UI or CLI view code, response
   handling, and interaction docs before specifying what the artifact should explain.
   If the actual state or action effect is unknown, then Ask the user or inspect its
   authoritative source rather than inventing a reassuring status or next step.

2. Specify: Map object/state to visible context, permitted actions, disabling reasons,
   action effects, pending/confirmed distinctions, and an interpretation oracle.
   If a practical interface clarification is requested, then propose this state record:

   ```text
   Illustrative state/action trial; confirm with the user/stakeholder:
   Scope: the requested artifact, actual object identity and source-backed states.
   Cues: current state, available action, its precondition/effect, and why unavailable.
   Example bound: 0 wrong state/action inferences on the agreed interaction fixtures.
   Preservation: existing action permissions and effects; wording cannot grant new capability.
   Evidence: actual state-to-view output, next-action answers, pending/error counterexamples.
   Limits: no invented success acknowledgement or timing/notification guarantee.
   Open items: state source, audience, accepted cues, action authority and trial owner.
   ```

   Ask at most three groups about confusing states/objects; available actions and
   actual effects; and audience context or defaults that should change.
   Proceed to view/state mappings while unknown action meanings stay unresolved.
   If no acceptance bound exists, then offer the illustrative inference trial and
   confirm with the user/stakeholder before declaring the cues sufficient.

3. Design/Implement: Read [state-cue patterns](./references/design-patterns.md) when
   exposing object context, disabled reasons, or pending/confirmed status.
   If an action is unavailable, then explain its real unmet condition at the point
   of use instead of linking only to a general manual that lacks the current state.
   If work is pending, then preserve that distinction until the accepted completion
   evidence exists; do not relabel an initiated action as a completed result.

4. Verify: Exercise the state/action matrix through normal views and responses,
   including stale context, pending work, disabled controls, and failed actions.
   If users infer a different state or effect from the rendered cues, then revise
   the relevant mapping and retest without supplying the answer in advance.

5. Report: Return state/view mappings, preserved action semantics, audience answers,
   and states or effects that remain unexplained or untested.
   If only static label assertions passed, then distinguish them from evidence that
   the intended audience can infer the current state and next permitted action.

## Specification patterns

- **State cue:** For `{object_and_state}`, `{artifact}` shall expose `{state_context}`
  so `{audience}` can infer `{current_state_and_object}` under `{allowed_context}`,
  verified by `{state_view_fixture_and_unaided_answers}` at `{confirmed_error_bound}`.
- **Action cue:** For `{available_or_disabled_action}`, the artifact shall expose
  `{real_condition_and_effect}` at `{point_of_use}`, checked against
  `{action_guard_and_effect_oracle}` without changing `{permission_or_behavior}`.
- **Pending result:** During `{unconfirmed_operation}`, `{view}` shall distinguish
  `{pending_from_confirmed_result}`, verified through `{pending_error_success_states}`.

Use the illustrative inference bound only for the agreed state/task set;
confirm with the user/stakeholder. Ask the user for unknown action or state semantics.

## Rules of thumb

- Do derive status wording from the state that authorizes its available actions;
  an optimistic label can tell users a draft is saved while the action still uses unsaved data.
- Do show a disabled action's actual unmet precondition nearby; a generic unavailable
  label cannot tell the user what the current state permits them to change.
- Do identify the affected object or scope where actions appear; a clear action verb
  attached to stale record context can explain the wrong operation to the user.
- Do name the effect users are choosing, not just the navigation step; a Continue
  label cannot explain a commit or submission that changes the object's state.
- Do distinguish initiated, pending, and confirmed results in the view; a click alone
  cannot supply the completion evidence that a success label implies.
- Don't collapse states with different next actions under one friendly label;
  apparent simplicity can hide the condition needed to infer a permitted next step.

## Verification

Use state/view integration checks, action-guard comparisons, and point-of-use audience
questions. Check labels, reasons, object context, and actual effects through pending,
error, and completed responses. Retain what remains unchanged after a failed action.
Track state/action misinferences, not label presence alone; interpretation evidence
and event-delivery timing answer different acceptance questions.

## Done checklist

- [ ] Match displayed state/object context to the authoritative state fixture.
- [ ] Compare available controls with actual action guards and required conditions.
- [ ] Exercise disabled controls with the correct current reason and permitted next step.
- [ ] Check action wording against the actual affected object and state effect.
- [ ] Preserve pending/confirmed distinctions through success and error paths.
- [ ] Verify failed-action views explain retained state rather than implying completion.
- [ ] Obtain unaided state/action answers or explicitly mark audience evidence missing.

## Failure modes

- Showing completed status when the action has only been initiated.
- Explaining an unavailable action without its current unmet condition.
- Keeping a correct label attached to stale object context.
- Using friendly wording that hides different permitted actions in distinct states.

## References

- Read [state-cue patterns](./references/design-patterns.md) when linking status,
  object scope, disabled reasons, and actual action effects at the point of use.
- Read [submission-view example](./references/worked-example.md) when checking
  concrete draft/pending/error outputs without inventing a successful submission.
