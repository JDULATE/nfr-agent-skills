---
name: augmentability
description: >-
  Adds a separately accepted supporting capability when users say "add reply suggestions", "put annotations beside reports", or "add a helper without replacing manual work". Not for improving the original capability (see enhanceability) or admitting through an existing hook (see extensibility).
---
# Augmentability

## Definition and scope

Augmentability means adding a supporting capability while the original capability
continues in its original role. Give the addition separate acceptance criteria
and an explicit attachment boundary; distinguish improvement of the original
result (`enhanceability`) and a general plug-in contract (`extensibility`).

## Use when / Don't use when

- Apply to an assistant, annotation panel, or supporting service with its own
  accepted result; establish whether it is optional or required.
- Test removal independence only where that property was actually promised.
- Route changes solely to the original function's output quality to `enhanceability`.
- Route implementing a named new function inside core source to `extendability`
  when preserving a separately accepted supporting role is not the question.

## Workflow

1. Clarify: Inspect the original code path, user-flow docs, side-effect boundaries,
   and ownership of the proposed helper before defining what it may add.
   Identify a complete original journey and the helper's separately observable result.
   If those results cannot be separated, then Ask the user whether this is an
   enhancement of the existing capability instead of a supplementary capability.

2. Specify: Set attachment inputs, supporting outputs, required/optional status, and
   activation/removal behavior, data access, and the original contract to preserve.
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

   Ask up to three groups: helper result; original-role and dependency constraints;
   and allowed data, adoption effects, and timing. Proceed to attachment design.
   If a preservation target is absent, then confirm the illustrative bound above
   with the user/stakeholder before adoption; leave unresolved permissions unimplemented.

3. Design/Implement: Use [attachment patterns](./references/design-patterns.md) when
   choosing separate presentation, a read-only projection, or explicit adoption.
   If the helper changes original state, then apply the guide's accepted-side-effect
   rule: compare adopted effects with the approved event ledger, display-only
   effects with the untouched original, and role replacements with a revised scope.
   If required support introduces a dependency, then record its accepted behavior;
   do not claim optional removal independence from that required arrangement.

4. Verify: Compare supplemented and failed-helper cases; test original-only and
   removed-helper cases where promised, judging the helper's result separately.
   If an original-state difference is outside the approved effect ledger, then
   fail preservation; do not reject deliberate adopted changes merely for differing.

5. Report: Show the helper's accepted scope, attachment points, original-path
   comparison, adoption authority, and remaining coupling or copied data.
   If promised removal is untested, then leave removal independence unverified;
   required supplements need their own accepted dependency evidence.

## Specification patterns

- **Attachment:** The system shall provide `{supplement_result}` alongside
  `{original_journey}` through `{attachment_boundary}`, verified against separate
  `{helper_acceptance_cases}` and `{original_contract_cases}`.
- **Removal:** When `{helper}` is absent, disabled, or removed, `{original_journey}`
  shall retain `{specified_outputs_and_side_effects}` within `{confirmed_difference_bound}`,
  checked using `{matched_input_fixture}`.
- **Adoption:** A supplementary recommendation shall change `{original_state}` only
  after `{agreed_adoption_action}`, evidenced by `{state_and_action_trace}`.

Confirm the illustrative preservation bound; Ask the user which adoption effects are allowed.

## Rules of thumb

- Do accept the supplementary result independently of the original result; a
  correct original decision cannot stand in for evidence that the helper adds value.
- Do test the original journey without an optional helper; requiring its startup
  turns a promised supplement into part of the original capability's prerequisites.
- Do compare original-state differences with the accepted adoption-effect ledger;
  a deliberate adopted draft change is not failed preservation, but an unlisted
  automatic send changes the original role even when the suggestion is useful.
- Do detach helper projections in a promised removal fixture and rerun original inputs;
  an original read that still needs them disproves independently removable support.
- Don't claim augmentation from a replacement that removes the original result;
  identify that changed role and revisit the requested scope.

## Verification

Use differential journey checks, dependency-isolation exercises, and state-transition
reviews. Compare original outputs and writes with and without the supplement.
Check whether slow helper responses delay the original completion path or appear
after the user has moved to another original record. Verify explicit adoption
matches the accepted effect ledger while display alone preserves original state.
Inspect removal where promised and any helper-owned dependency left behind.

## Done checklist

- [ ] Judge the supplementary result against its own accepted cases.
- [ ] Compare original outputs with helper display only, before any adoption.
- [ ] Match adopted state changes to the named allowed-effect ledger.
- [ ] Reject or flag an obsolete suggestion under the agreed original-state precondition.
- [ ] Complete the original route with an optional helper absent or delayed;
  for a required supplement, check the separately agreed dependency behavior.
- [ ] Trace attachment reads and writes against the accepted data/authority scope.
- [ ] Remove a removable helper and inspect original reads for lingering projections.
- [ ] Compare the original send/commit action after adoption with its retained contract.

## Failure modes

- Giving helper output the same status as an approved original decision.
- Replacing the original journey while describing the change as optional enrichment.
- Claiming an optional original-only route while it requires a helper response.
- Treating an approved adopted draft change as a preservation failure, or accepting
  an unlisted automatic send merely because the suggestion itself is useful.
- Removing the helper UI while its state changes still affect the original path.

## References

- Read [attachment patterns](./references/design-patterns.md) when choosing the
  helper's authority, accepted side effects, required status, or removal strategy.
- Read [support-panel example](./references/worked-example.md) when specifying a
  supplementary result without silently changing the original workflow.
