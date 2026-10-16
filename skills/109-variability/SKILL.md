---
name: variability
description: >-
  Constrains product-family features when asked "reject invalid builds", "make export require audit", or "list allowed feature sets". Before routing editions, Ask the user: feature-combination rules, instance settings, or custom content? Not for settings of one instance (see configurability) or applying a transition (see reconfigurability).
---

# Variability

## Definition and scope

Variability means a product family represents explicit variation points and
allowed combinations. Define how selected features derive a valid variant and
which combinations the family forbids.
Separate family-level alternatives from settings of an instance
(`configurability`) and transitions between arrangements (`reconfigurability`).

## Use when / Don't use when

- Apply when editions or build variants combine features whose dependencies
  and exclusions must be enforced before deriving the product.
- Identify the product-family boundary and the stage where choices bind.
- Route documenting settings of one running instance to `configurability`.
- Route applying a live arrangement change to `reconfigurability`.
- Route custom stakeholder-authored behavior to `customizability` when it is
  outside the declared product-family variation points.

## Workflow

1. Clarify: Read feature manifests, build selection, generated artifacts,
   edition docs, and dependency rules before modeling variants.
   Identify what actually differs between family members.
   If "more variants" names no product family or binding stage, then Ask the
   user whether the concern is family derivation, instance settings, or a live transition.

2. Specify: Record variation points, allowed values, defaults if confirmed,
   implications, exclusions, binding stage, and derivation evidence.
   If no target exists, then propose a labeled illustrative default:
   declared feature constraints checked before any variant artifacts are emitted;
   confirm with the user/stakeholder.
   Ask at most three questions about the family, feature relationships,
   and binding/derivation boundary before changing build logic.

3. Design/Implement: Read [variant decisions](./references/design-guide.md)
   when encoding implications, exclusions, and artifact derivation.
   If a selection violates a constraint, then refuse it before partial output.
   If an enabled feature has no derivation rule, then report an incomplete
   variant model rather than silently omitting the feature.

4. Verify: Enumerate the bounded selection space or a declared coverage subset,
   checking validity decisions and actual derived artifacts separately.
   Preserve rejected combinations and failed builds in the evidence.
   If not all combinations were evaluated, then identify the untested region
   instead of claiming the whole family is validated.

5. Report: Return the variation model, binding stage, valid/invalid findings,
   derived artifact evidence, and unsupported combinations.
   If only build-time choices were checked, then withhold claims about safe
   runtime switching or migration of existing instance state.

## Specification patterns

- **Selection validity:** For `{product_family}`, selections at `{binding_stage}`
  shall satisfy `{feature_implications_and_exclusions}`, verified by
  `{enumerated_combination_or_declared_subset_checks}`.
- **Derivation:** Each valid `{selection}` shall derive
  `{corresponding_artifacts}`; invalid `{selection}` shall produce
  `{named_refusal}` before `{forbidden_partial_artifacts}`.

Use the illustrative pre-derivation validation proposal in Specify when no
numeric objective exists; confirm with the user/stakeholder before accepting it.

## Rules of thumb

- Validate the selected family member before deriving artifacts; rejecting a
  manifest after emitting incompatible modules does not prevent an invalid variant.
- Keep the binding stage explicit; a build-time feature choice does not establish
  a supported setting or safe transition in an already running instance.
- Make every enabled feature visible in derivation evidence; silently dropping
  a selected feature changes the variant instead of satisfying its constraints.

## Verification

Use feature-constraint checks, bounded combination enumeration, and artifact
inspection. Record each selection and its expected validity independently.
Compare valid selections with actual manifests, modules, or generated config.
Inspect invalid selections for partial artifacts and misleading success status.
Retain all evaluated outcomes, defaults, and the declared selection-space boundary.
Check optional features independently of dependent features to catch reversed
implications.
Preserve implication direction: export requiring audit does not force export
into every audited variant.
Do not substitute a settings form for evidence of product-family derivation.

## Done checklist

- [ ] Define the family and the stage where choices bind.
- [ ] Enumerate variation points and confirmed defaults.
- [ ] Specify implication and exclusion directions.
- [ ] Check validity before generating variant artifacts.
- [ ] Compare enabled features with actual derivation output.
- [ ] Exercise dependent and independent feature combinations.
- [ ] Inspect rejected selections for forbidden partial output.
- [ ] Identify any unevaluated combination region.

## Failure modes

- Confusing an implication with a bidirectional dependency.
- Deriving modules before discovering an invalid selection.
- Silently disabling a selected feature to make a variant build.
- Reporting build-time validity as proof that live switching is safe.

## References

- Read [variant decisions](./references/design-guide.md) when encoding
  constraints and selecting the derivation boundary.
- Read [edition-family example](./references/worked-example.md) when enumerating
  a bounded feature space and checking actual artifact selection.
