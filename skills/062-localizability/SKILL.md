---
name: localizability
description: >-
  Separates locale behavior from business logic when tickets say "add a language without changing the code", "this date is ambiguous after translation", or "the decimal comma breaks our export". Not for platform moves (see portability) or character recognition (see legibility).
---

# Localizability

## Definition and scope

Localizability means language and locale-dependent behavior can change without
reworking unrelated business behavior. Separate presentation resources and
formatting from canonical values; distinguish moving execution platforms
(`portability`), recognizing rendered characters (`legibility`), and explaining
unclear concepts (`comprehensibility`) from locale adaptation.

## Use when / Don't use when

- Apply when adding a language requires editing business conditions or serialized keys.
- Apply when a displayed date is ambiguous or a decimal format leaks into machine output.
- Route platform-specific execution differences to `portability`.
- Route physical character recognition to `legibility`.
- Ask the user for reviewed wording and locale conventions rather than guessing
  a country's language, date, number, or legal requirements.

## Workflow

1. Clarify: Read resource lookup, formatting/parsing boundaries, data types,
   wire contracts, locale selection, and current translation workflow first.
   Identify the audience, affected surfaces, canonical meaning, and supplied conventions.
   If a real translation or regional rule is not provided, then Ask the user for
   qualified wording and formatting decisions; do not invent authoritative translations.

2. Specify: Record resource keys, named placeholders, locale selection/fallback,
   canonical values, presentation formats, machine-output formats, and review evidence.
   If no contract exists, then propose labeled illustrative defaults:
   external resources and explicit formatters with invariant machine data and
   visible missing-resource results; confirm with the user/stakeholder.
   Keep translation approval and locale correctness distinct from mechanism checks.

3. Design/Implement: Read [locale-boundary decisions](./references/design-guide.md)
   when separating resources, templates, display formats, and parsing.
   If a translated label also acts as a machine key, then introduce a stable key.
   If a locale formatter changes exported machine values, then separate that
   output boundary. If date meaning is unclear, then resolve whether it is a
   calendar date or an instant before choosing any display conversion.

4. Verify: Render the same canonical fixture using the supplied locale profiles.
   Compare resource selection, placeholders, date meaning, and machine output.
   If a resource is missing or wording is unreviewed, then expose that gap rather
   than declaring the locale supported through an accidental fallback.
   Retain failed renderings, parse ambiguities, and review limitations.
   Read [synthetic locale example](./references/worked-example.md) for filled cases.

5. Report: Return extracted resources, formatting boundaries, invariant-data checks,
   missing keys, and language/locale review status.
   If only synthetic profiles were tested, then report mechanism verification
   without claiming a real language, culture, or accessibility outcome was validated.

## Specification patterns

- **Resource adaptation:** For `{audience_and_locale}`, `{surface}` shall use
  `{reviewed_resources_and_named_placeholders}` selected by `{locale_policy}`,
  without altering `{stable_business_keys_and_rules}`.
- **Formatting:** Display `{canonical_date_or_number}` using
  `{confirmed_locale_convention}`, while `{machine_boundary}` retains
  `{canonical_representation_and_meaning}`.
- **Missing resources:** When `{resource_or_locale}` is unavailable, expose
  `{confirmed_missing_or_fallback_behavior}` and record `{unsupported_surface}`.

For missing numeric targets, use the illustrative boundary-preservation defaults
in Specify and confirm with the user/stakeholder; do not invent a translation quality score.

## Rules of thumb

- Do use stable resource keys instead of translated strings in business decisions;
  changing a label must not change which operation the system selects.
- Do keep human locale formatting out of canonical machine fields; a display
  decimal separator must not rewrite the amount representation in an export contract.
- Do translate complete templates with named placeholders rather than concatenated
  word fragments; another resource must be able to reorder the supplied values.
- When audiences select different locales, bind selection to each rendering
  context; changing one view's locale must not alter another audience's output.

## Verification

Use resource-schema checks, formatter fixtures, machine-output comparisons, and
qualified language/layout review categories.
Check placeholder names and types against each resource's required inputs.
Exercise missing resources and the confirmed fallback policy explicitly.
Hold canonical inputs fixed and retain complete rendered outputs and parse failures.
Inspect date ambiguity rather than inferring the intended convention from language alone.
Distinguish a calendar date from an instant and check that formatting preserves
the confirmed date meaning. Interleave different audience contexts to detect leakage.
Check long messages and locale-specific glyph/layout needs with an actual renderer
and qualified audience evidence where those claims are required.
Do not use a passing resource lookup as evidence of correct translation.

## Done checklist

- [ ] Identify the audience, locale decision, and affected surfaces.
- [ ] Record supplied wording and formatting conventions with their review status.
- [ ] Separate stable business keys from presentation resources.
- [ ] Match named placeholders to the canonical input types.
- [ ] Compare date and number displays under each confirmed profile.
- [ ] Preserve machine-output representation across display changes.
- [ ] Exercise missing resources without hiding unsupported surfaces.
- [ ] Mark language and layout claims unverified when review evidence is absent.

## Failure modes

- Using translated labels as program identifiers.
- Concatenating fragments that cannot follow another resource's word order.
- Applying UI number formatting to a machine-readable amount.
- Guessing a regional date interpretation from a language label.
- Calling a locale supported because a fallback string happened to render.

## References

- Read [locale-boundary decisions](./references/design-guide.md) when selecting
  resource keys, named templates, formatting boundaries, and fallback behavior.
- Read [synthetic locale example](./references/worked-example.md) when checking
  date/number presentation without inventing real translation conventions.
