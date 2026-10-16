---
name: tailorability
description: >-
  Fits supported workflows when asked "choose night-shift presets", "map team needs to presets", or "fit team schedules". Ask the user if supported choices vs custom behavior is unclear. Not for authored behavior (see customizability), defining settings (see configurability), alternatives (see flexibility), or external changes (see adaptability).
---
# Tailorability

## Definition and scope

Tailorability means fitting supported deployment or workflow behavior to a named
stakeholder's context. Map contextual needs to available choices and demonstrate
that fit; separate stakeholder-authored behavior (`customizability`), the settings
menu (`configurability`), and general alternative coverage (`flexibility`).

## Use when / Don't use when

- Apply when a team, department, or operating context has specific tasks and
  constraints that existing supported choices may satisfy in a particular arrangement.
- Route new customer-defined behavior to `customizability` rather than promising
  contextual fit by inventing an unsupported option.
- Route an external operating-condition change to `adaptability`; choosing a team
  recipe and accommodating a changed dependency have different acceptance evidence.

## Workflow

1. Clarify: Read workflow code, supported settings, preset docs, actor/task context,
   and existing deployment recipes before proposing a contextual fit.
   If a requested need has no supported behavior, then Ask the user whether to
   relax that need or separately scope new behavior under `customizability`.

2. Specify: Map each context need to a choice, prerequisite, retained shared
   obligation, task fixture, and owner; separate must-haves from preferences.
   If the user wants a fitted deployment/workflow, then propose this context record:

   ```text
   Illustrative fit record; confirm with the user/stakeholder:
   Context: named stakeholder, actual actors/tasks, and inspected operating constraints.
   Needs: confirmed must-haves separated from preferences and unsupported requests.
   Recipe: existing choices only, with dependencies and winning context scope recorded.
   Example bound: 0 unmet agreed must-have needs in the selected context task fixtures.
   Preservation: shared outcomes and explicitly unaffected context behavior.
   Evidence: need-to-choice matrix, fresh recipe application, task results, gap decisions.
   Owner/status: context owner; priorities, scope and fit criterion remain proposed.
   ```

   Ask at most three groups about context/tasks; must-haves and allowed trade-offs;
   and available choices, shared obligations, or proposed defaults needing revision.
   Proceed to a recipe alternative while unsupported needs remain explicit gaps.
   If a target is absent, then propose the illustrative fit bound and confirm with
   the user/stakeholder before treating the selected needs or fixtures as complete.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [fit patterns](./references/design-patterns.md) when
   deriving a supported recipe from contextual needs and checking shared obligations.
   If a preference conflicts with a must-have, then obtain the context owner's
   priority decision instead of hiding the trade-off in a plausible preset.
   If live work must move to the fitted arrangement, then separate that transition
   under `reconfigurability`; a correct recipe does not prove stateful application.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Apply the recipe from declared starting conditions and exercise the
   stakeholder's tasks, shared outcomes, and unaffected-context controls.
   If tasks succeed only after an undocumented patch, then record unsupported fit
   rather than claiming the supplied choices accommodate this context.

5. Report: Return the need-to-choice/task matrix, fitted recipe, observed gaps,
   retained shared outcomes, and priorities the stakeholder has not decided.
   If the task sample or context is incomplete, then limit the fit claim to the
   exercised needs rather than declaring the whole department accommodated.

## Specification patterns

- **Context fit:** For `{stakeholder_context}`, `{supported_recipe}` shall satisfy
  `{confirmed_must_have_needs}` under `{actor_and_task_conditions}`, verified by
  `{need_to_choice_and_result_matrix}` within `{confirmed_gap_bound}`.
- **Shared obligations:** Applying `{context_recipe}` shall preserve
  `{shared_outcomes_and_unaffected_context_behavior}`, checked by
  `{context_and_control_tasks}` with `{permitted_differences}` explicit.

Use the illustrative gap-bound proposal only for the confirmed context sample;
confirm with the user/stakeholder. Ask the user before inventing needs or priorities.

## Rules of thumb

- Do link each selected option to a named context need and task result; a long
  preset list cannot demonstrate that this stakeholder's operating constraints fit.
- Do retain unmet must-haves as fit gaps; relabeling them preferences makes an
  unsupported context appear accommodated without changing the available behavior.
- Do keep a reproducible recipe of supported choices; an undocumented source patch
  turns contextual fitting into new behavior without exposing that scope change.
- Do test shared outcomes as well as local preferences; a team-friendly route that
  omits a required common commit is not an acceptable fit under that shared obligation.
- Don't change a global default merely to fit one team unless its wider effects
  are accepted; local fit is unproved if other declared contexts silently lose theirs.

## Verification

Use context/task acceptance matrices, recipe replay, and scope/precedence inspection.
Exercise must-haves, preference conflicts, unsupported needs, and an unaffected
context from matched starts. Inspect undocumented post-setup repairs and the
specific unmet need behind failed tasks; a valid preset file alone cannot establish
that the resulting workflow fits the stakeholder's task context.

## Done checklist

- [ ] Trace each confirmed must-have to a supported choice and passing task result.
- [ ] Retain unsupported needs and unresolved preference conflicts as explicit gaps.
- [ ] Recreate the fitted recipe without hidden source or operator patches.
- [ ] Exercise shared obligations under the fitted task arrangement.
- [ ] Check a declared unaffected context after applying the scoped recipe.
- [ ] Reconcile result differences against the context owner's accepted priorities.

## Failure modes

- Calling the presence of a preset a demonstrated fit without context task evidence.
- Hiding an unmet must-have by changing its priority after seeing the result.
- Introducing bespoke code while reporting only supported-choice tailoring.
- Fitting one team by silently changing shared defaults for every context.

## References

- Read [fit patterns](./references/design-patterns.md) when mapping needs to choices,
  separating preferences from must-haves, or checking shared context obligations.
- Read [team-workflow example](./references/worked-example.md) when proving fit with
  concrete task state and controls rather than a list of selectable modes.
