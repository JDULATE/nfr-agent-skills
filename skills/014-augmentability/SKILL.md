---
name: augmentability
description: >-
  Designs supplementary capabilities when users say "add an assistant alongside
  this workflow", "enrich this without replacing it", "attach an optional helper",
  or "keep the original feature usable". Not for improving only the existing
  capability's own results (see enhanceability) or extension-hook contracts alone
  (see extensibility).
---
# Augmentability

## Definition and scope

Augmentability means adding a supporting capability while the original capability
continues in its original role. Give the addition separate acceptance criteria
and an explicit attachment boundary; distinguish improvement of the original
result (`enhanceability`) and a general plug-in contract (`extensibility`).

## Use when / Don't use when

- Apply to an optional assistant, annotation panel, or supporting service with
  its own useful result alongside an established workflow.
- Look for a request to remove the helper without losing the original function.
- Route changes solely to the original function's output quality to `enhanceability`.
- Route implementing a named new function inside core source to `extendability`
  when preserving a separately accepted supporting role is not the question.

## Workflow

1. Clarify: Inspect the original code path, user-flow docs, side-effect boundaries,
   and ownership of the proposed helper before defining what it may add.
   Identify a complete original journey and the helper's separately observable result.
   If those results cannot be separated, then Ask the user whether this is an
   enhancement of the existing capability instead of a supplementary capability.

2. Specify: Set the attachment inputs, optional outputs, activation and removal
   behavior, data access, and the original contract that must remain intact.
   If the user wants a quick augmentation, then offer this bounded record:

   ```text
   Illustrative augmentation defaults; confirm with the user/stakeholder:
   Original: the documented journey and its existing accepted outputs and writes.
   Supplement: a separately identified supporting result requested by the user.
   Boundary: helper output stays separate; no new authority to change core decisions.
   Baseline target: 0 changes to original outcomes in the agreed removal fixture.
   Activation: explicit opt-in for the example; no hidden mandatory helper dependency.
   Evidence: helper present, absent, delayed, and removed; compare original results.
   Open choices: recipient/data scope, who may accept helper output, and ownership.
   ```

   Limit initial questions to three groups: what the helper contributes; what the
   original must still do without it; and what data, authority, and timing it may use.
   Begin an attachment design with unresolved permissions visibly unimplemented.
   If a numeric preservation target is absent, then propose the illustrative
   fixture bound above and confirm with the user/stakeholder before adopting it.

3. Design/Implement: Use [attachment patterns](./references/design-patterns.md) when
   choosing separate presentation, a read-only projection, or explicit adoption.
   If the helper is allowed to modify the original state, then put that action
   behind the agreed adoption boundary instead of giving every suggestion write authority.
   If the original waits for the helper without needing its result, then decouple
   that wait or obtain explicit acceptance of the new dependency.

4. Verify: Exercise original-only, supplemented, helper-failed, and helper-removed
   cases with matching original inputs; evaluate the helper's result separately.
   If the original output changes merely because the helper is installed, then
   trace that coupling and resolve it before claiming a removable supplement.

5. Report: Show the helper's accepted scope, attachment points, original-path
   comparison, adoption authority, and remaining coupling or copied data.
   If removal has not been exercised, then leave independent original operation
   unverified even if the supplemented demonstration succeeds.

## Specification patterns

- **Attachment:** The system shall provide `{supplement_result}` alongside
  `{original_journey}` through `{attachment_boundary}`, verified against separate
  `{helper_acceptance_cases}` and `{original_contract_cases}`.
- **Removal:** When `{helper}` is absent, disabled, or removed, `{original_journey}`
  shall retain `{specified_outputs_and_side_effects}` within `{confirmed_difference_bound}`,
  checked using `{matched_input_fixture}`.
- **Adoption:** A supplementary recommendation shall change `{original_state}` only
  after `{agreed_adoption_action}`, evidenced by `{state_and_action_trace}`.

Carry the example preservation bound into a proposal only with stakeholder confirmation;
Ask the user where helper effects are deliberately allowed to alter the original result.

## Rules of thumb

- Do label helper-derived output separately from the original authoritative result;
  don't make a suggestion look like a decision the original workflow already made.
- Do give a support panel its own acceptance cases; don't call it an improvement
  merely because the original page now contains more material.
- Do maintain an original-only route through the workflow; don't turn helper
  initialization into an unexplained prerequisite for completing that route.
- Do distinguish displaying a recommendation from applying it; don't let a helper
  write through a read-only attachment under the guise of enrichment.
- Do track helper-owned projections for removal; don't leave an abandoned projection
  as a hidden dependency of the original feature.
- Don't claim augmentation from a replacement that removes the original result;
  identify that changed role and revisit the requested scope.

## Verification

Use differential journey checks, dependency-isolation exercises, and state-transition
reviews. Compare original outputs and writes with and without the supplement.
Check whether slow helper responses delay the original completion path or appear
after the user has moved to another original record. Verify explicit adoption
changes the intended state and that mere display does not. Inspect uninstall or
disable behavior and any helper-owned data left accessible after removal.

## Done checklist

- [ ] Name original and supplementary results separately.
- [ ] Identify every attachment read, write, and user-visible output.
- [ ] Agree helper activation, adoption authority, and data scope.
- [ ] Record what remains usable when the helper is missing or slow.
- [ ] Compare original outcomes across helper presence and absence.
- [ ] Test removal and inspect helper-owned projections and dependencies.
- [ ] Report helper acceptance independently of original-contract preservation.

## Failure modes

- Giving helper output the same status as an approved original decision.
- Replacing the original journey while describing the change as optional enrichment.
- Making original completion depend on an unneeded helper response.
- Removing the helper UI while its state changes still affect the original path.

## References

- Read [attachment patterns](./references/design-patterns.md) when choosing the
  helper's authority, coupling, data projection, or removal strategy.
- Read [support-panel example](./references/worked-example.md) when specifying a
  supplementary result without silently changing the original workflow.
