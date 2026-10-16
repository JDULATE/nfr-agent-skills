---
name: simplicity
description: >-
  Removes unjustified mechanisms when asked "remove this unused dispatcher", "drop the fixed-path registry", or "justify this plugin framework". Ask the user if unnecessary machinery vs interaction burden is unclear. Not for mapping interaction burden (see complexity-interacting-complexity) or reading flow alone (see readability).
---

# Simplicity

## Definition and scope

Simplicity means avoiding unnecessary concepts and mechanisms for a stated
purpose. Identify which requirements justify each mechanism before choosing
a less elaborate design. Separate removing avoidable machinery from analyzing
interaction burden (`complexity-interacting-complexity`) and improving reading
flow without changing design mechanisms (`readability`).

## Use when / Don't use when

- Apply when a fixed requirement is implemented through registries, lifecycle
  hooks, or indirection that serves no accepted current obligation.
- Bound the supported purpose before deciding that an abstraction is unnecessary.
- Route mapping difficult flag or callback interactions to
  `complexity-interacting-complexity`.
- Route clearer naming or source organization alone to `readability`.
- Route introducing a necessary extension contract to `extendability`;
  this skill does not presume that all extensibility is waste.

## Workflow

1. Clarify: Read supported-feature docs, call sites, configuration, extension
   registrations, tests, and architecture decisions before proposing removal.
   Identify actual consumers of each candidate mechanism.
   If a mechanism's purpose is unknown, then Ask the user whether it satisfies
   a required variation or lifecycle obligation before calling it unnecessary.

2. Specify: Record retained requirements, candidate mechanisms, the obligations
   they serve, permitted removals, and preserved behavior.
   If no reduction target exists, then propose a labeled illustrative default:
   remove only mechanisms with no identified required role in the fixed path,
   preserving its contract; confirm with the user/stakeholder.
   Ask at most three grouped questions about the supported purpose, external
   consumers, and future obligations already accepted by the stakeholder.

3. Design/Implement: Read [removal decisions](./references/design-guide.md)
   when replacing unjustified registries, lifecycle layers, or duplicate paths.
   If the fixed path needs no runtime selection, then consider a direct call
   rather than preserving an unused selection framework.
   If removal destroys a required extension or lifecycle effect, then keep that
   mechanism or propose a different reduction with the obligation intact.

4. Verify: Compare retained contract cases before/after and inspect the removed
   mechanisms' consumers and effects.
   If a shorter implementation drops an accepted result or refusal, then reject
   that candidate regardless of its smaller source footprint.

5. Report: Return the requirement-to-mechanism ledger, justified removals,
   preserved behavior, and intentionally unsupported variations.
   If only mechanism count changed, then report that structural observation
   without claiming measured comprehension, performance, or maintenance savings.

## Specification patterns

- **Purpose fit:** For `{fixed_supported_purpose}`, `{path}` shall satisfy
  `{retained_contract}` without `{unjustified_mechanism}`, verified by
  `{consumer_ledger_and_behavior_comparison}`.
- **Removal boundary:** Removing `{candidate_layer}` shall preserve
  `{results_refusals_and_lifecycle_effects}` for `{supported_cases}`,
  checked by `{before_after_contract_evidence}`.

Use the illustrative requirement-led removal proposal in Specify when no number
is supplied; confirm with the user/stakeholder before discarding an obligation.

## Rules of thumb

- Remove a selection mechanism only when the supported purpose does not require
  selecting among alternatives; a currently unused hook can still have an accepted role.
- Do not keep a registry solely to anticipate unspecified future variants;
  distinguish an accepted extension obligation from speculation before retaining it.
- Prefer a direct fixed-path call over a new facade that merely hides the same
  unused dispatch machinery; concealment does not remove the mechanism.

## Verification

Use requirement-to-mechanism review, consumer search, and focused behavior
regression categories. Inspect registrations and external callers as well as
the most common entrypoint.
Retain original inputs, output artifacts, refused cases, and lifecycle effects.
Check required initialization and cleanup independently of the removed wrapper.
Record unanswered ownership or consumer questions rather than treating absence
of evidence as permission to remove a supported feature.
Distinguish actual deleted mechanisms from renamed wrappers.
Use source size and mechanism counts as descriptive evidence only.

## Done checklist

- [ ] Bound the supported purpose and accepted variations.
- [ ] Map candidate mechanisms to actual required obligations.
- [ ] Inspect registrations and consumers outside the main path.
- [ ] Confirm removals that change an exposed extension surface.
- [ ] Compare supported outputs and refusal behavior.
- [ ] Check preserved lifecycle effects independently of wrappers.
- [ ] Report structural reduction without unmeasured benefit claims.

## Failure modes

- Calling an abstraction unnecessary without checking its consumers.
- Removing required behavior to achieve a smaller implementation.
- Replacing an unused framework with a facade around the same framework.
- Retaining hypothetical extension machinery without a confirmed obligation.

## References

- Read [removal decisions](./references/design-guide.md) when deciding which
  mechanisms lack a role in the accepted purpose.
- Read [fixed-export example](./references/worked-example.md) when comparing a
  direct path with a registry that has no required selection role.
