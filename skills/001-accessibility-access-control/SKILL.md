---
name: accessibility-access-control
description: >-
  Separates interaction barriers from permission checks when tickets say "keyboard users get stuck", "screen reader skips errors", "stop cross-team edits", or "revoked access still works". Asks which branch. Not for looks (see attractiveness), personal-data lifecycle (see privacy), or threat review (see security-control-and-security).
---
# Accessibility/Access Control

## Definition and scope

Accessibility means the intended audience can interact without the identified
barriers; Access Control means actor/action/resource decisions follow the agreed
authorization policy. Treat these as separate branches of the catalogue label,
not synonyms: distinguish general task outcomes (`usability`), visual recognition
(`legibility`), disclosure (`confidentiality`), and broad threats (`security-control-and-security`).

## Use when / Don't use when

- Choose Accessibility for keyboard, focus, semantic-control, error announcement,
  or other specified interaction barriers for a named audience and context.
- Choose Access Control for policy decisions about who may do what to which
  resource, including service identities, alternate entrypoints, and revoked access.
- Ask the user which branch applies to bare access language; record both when
  both are requested, with independent acceptance evidence.
- Route visual appeal to `attractiveness` and personal-data handling purpose or
  lifecycle to `privacy`; neither branch substitutes for those properties.

## Workflow

1. Clarify: Read interaction and authorization code, component/resource models,
   existing tests, supported-context docs, and policy decisions before specifying.
   If the request does not identify the branch, then Ask the user whether the
   problem is an interaction barrier, a permission decision, or both.

2. Specify: For Accessibility, bind audience/task/context, interaction barrier,
   input/assistive conditions, success/error states, and the observable task result.
   For Access Control, bind actor, action, resource/scope, policy state, decision,
   effect boundary, alternate paths, and revocation/unknown-state behavior.
   If the user wants a practical fix, then propose the applicable row(s) together:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Accessibility row: named task with keyboard/focus and exposed control/error semantics.
   Trial gate: 0 task-blocking barriers in the agreed audience/context scenarios.
   Access Control row: actor/action/resource/scope -> confirmed allow/deny and actual effect.
   Trial gate: 0 forbidden effects in the agreed direct-call, cross-scope, and revoked cases.
   Unknowns: audience/support conditions and policy authority stay open; no guessed entitlement.
   Preservation: accessible authorized actions remain usable; hidden UI is not enforcement.
   Evidence: branch-specific interaction observations or actual permission/effect traces.
   Status: proposed bounded checks, not a standards-conformance or universal-access claim.
   ```

   Ask at most three groups about branch/audience or actors; task/barrier or
   resource/policy; and context, revocation, criteria, or required preserved behavior.
   Continue to reversible branch-specific design; keep unresolved policy decisions visible.
   If no target is given, then offer the illustrative gates and confirm with the
   user/stakeholder before adopting either branch's scenario scope.

3. Design/Implement: Read [branch practices](./references/design-patterns.md) when
   fixing interaction semantics/focus or locating authorization enforcement.
   If a dialog or error changes interaction state, then preserve the task's
   operable focus path and expose the changed meaning under the agreed audience conditions.
   If a forbidden action remains callable outside the interface, then enforce the
   confirmed policy at the actual action boundary rather than only hiding its control.
   If policy state can change after a prior decision, then re-evaluate its validity
   at the effect boundary under the confirmed revocation contract.

4. Verify: Exercise Accessibility tasks through the agreed input/assistive
   conditions, including error and return paths. Exercise Access Control allow/deny,
   direct-call, cross-scope, and revoked cases against actual effects.
   If only a scanner result or hidden button was checked, then leave the
   corresponding task-access or permission-enforcement claim unverified.

5. Report: Return the selected branch, requirement rows, changed code, observed
   interaction or authorization evidence, and unsupported contexts/policy cases.
   If both branches apply, then report their outcomes separately; passing either
   cannot establish the other or imply legal/standards compliance.

## Specification patterns

- **Accessible task:** Under `{audience_and_input_assistive_conditions}`, enable
  `{task_and_error_recovery}` with `{confirmed_interaction_constraints}`, verified
  by `{actual_task_focus_semantic_and_result_observations}`.
- **Permission:** For `{actor_action_resource_and_policy_state}`, enforce
  `{confirmed_decision}` at `{effect_boundary}` across `{entrypoints}`, verified
  by `{allowed_and_forbidden_effect_checks}`.
- **Changed authority:** After `{revocation_or_scope_change}`, apply
  `{confirmed_decision_validity_rule}` to `{inflight_and_later_actions}`, verified
  by `{changed_policy_and_actual_effect_trace}`.

Use only the relevant illustrative gate when no criterion exists; confirm with
the user/stakeholder. Ask the user for chosen standards/source criteria if named;
do not invent contrast, timing, permission, legal, or conformance requirements.

## Rules of thumb

- Do preserve an operable focus route through dialog opening, error correction,
  and return; reaching the initial control does not establish an accessible task path.
- Don't replace control meaning or error semantics with visual decoration;
  an audience using another interaction representation still needs the task decision.
- Do observe the actual accessible task with its required input/assistive context;
  a preferred visual style or automated pass cannot establish barrier-free completion.
- Don't treat a hidden or disabled interface action as permission enforcement;
  direct and background calls must still satisfy the confirmed actor/resource policy.
- Do bind authorization to the actual resource scope, not only the action name;
  a valid editor role in one team does not grant edits in another under a scoped policy.
- Do test changed authority at the effect boundary; an earlier allowed screen
  state cannot justify a later forbidden action under the confirmed revocation rule.
- Don't force authentication as a fix for an interaction barrier; choosing the
  wrong branch can add a barrier without repairing either intended acceptance question.

## Verification

Use interaction-task observation, semantic/focus inspection, and permission/effect
integration categories. For Accessibility, inspect keyboard sequence, control
meaning/state, error exposure, and task recovery under agreed audience conditions.
For Access Control, vary actor, operation, object scope, direct/background paths,
and policy changes; inspect effects as well as responses. Retain allowed controls
and negative cases separately. Classify unknown policy/context as unresolved rather than a pass.

## Done checklist

- [ ] Record branch selection and independent acceptance rows when both apply.
- [ ] Exercise the accessible task and its error/return path in agreed conditions.
- [ ] Inspect control meaning/state and focus continuity at changed interaction states.
- [ ] Map authorization decisions to actor, action, resource, and policy state.
- [ ] Check direct/background entrypoints enforce the same confirmed effect policy.
- [ ] Verify cross-scope and changed-authority effects with allowed cases as controls.
- [ ] Separate scanner/UI evidence from actual task and permission observations.
- [ ] Report unsupported audience contexts and unresolved policy decisions by branch.

## Failure modes

- Treating Accessibility and Access Control as two spellings of one concern.
- Passing a visual/automated check while the real interaction task remains blocked.
- Losing focus or error meaning after a dialog or validation transition.
- Hiding a control while the underlying forbidden action remains callable.
- Applying an actor's role without the resource's team/object scope.
- Claiming revocation enforcement from a decision checked only before policy changed.

## References

- Read [branch practices](./references/design-patterns.md) when selecting interaction
  repairs, policy matrices, or effect-boundary enforcement for the chosen branch.
- Read [paired branch examples](./references/worked-example.md) when keeping a
  focus/error task separate from a cross-team permission effect.
