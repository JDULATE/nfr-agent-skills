---
name: legibility
description: >-
  Checks character recognition when asked "distinguish I from l", "fix lookalike symbols", or "test this font on the display". Ask the user if characters vs reading flow is unclear. Not for code/text reading flow (see readability), visual appeal (see attractiveness), or broader access barriers (see accessibility-access-control).
---
# Legibility

## Definition and scope

Legibility means the intended audience can visually distinguish displayed characters
and symbols under specified conditions. Check rendered recognition while preserving
the content; separate reading meaning (`readability`), aesthetic response
(`attractiveness`), and the broader accessibility branch of `accessibility-access-control`.

## Use when / Don't use when

- Apply when identifiers, characters, or symbols are confused in an actual display,
  print, or viewing condition despite known intended content.
- Route unclear concepts or sentence organization to `comprehensibility` or
  `readability`; recognizing letters is not evidence of interpreting their meaning.
- Route broad interaction barriers to `accessibility-access-control`; do not claim
  that a symbol-recognition fix establishes an accessibility standard or compliance.

## Workflow

1. Clarify: Read rendering code, style/font assets, display docs, target content,
   and audience/viewing requirements before prescribing a visual change.
   If the complaint is semantic rather than visual recognition, then Ask the user
   which characters are confused or route the interpretation problem to `readability`.

2. Specify: Record content/oracle, intended audience, display medium, rendered
   conditions, allowed adjustments, recognition task, and an accepted error criterion.
   If the user wants a practical display improvement, then propose this record:

   ```text
   Illustrative recognition trial; confirm with the user/stakeholder:
   Content: observed ambiguous characters/identifiers with an exact source answer key.
   Conditions: affected display, rendered font, scaling, background and viewing context.
   Example bound: 0 symbol-transcription errors on the agreed identifier fixture.
   Design: compare approved rendering changes while preserving source characters.
   Evidence: actual rendered samples, unaided transcription, confusion pairs and conditions.
   Limits: no universal font size, contrast ratio, or accessibility-conformance conclusion.
   Open items: audience needs, actual viewing setup, allowable styles, trial acceptance.
   ```

   Ask at most three questions about confusing content and audience; actual viewing
   conditions; and allowed presentation changes or proposed trial needing revision.
   Proceed to rendering alternatives rather than guessing a universal style threshold.
   If no criterion is supplied, then offer the illustrative fixture bound and
   confirm with the user/stakeholder before adopting it as a recognition requirement.

3. Design/Implement: Read [recognition patterns](./references/design-patterns.md) when
   choosing glyph distinctions, rendering conditions, or a transcription comparison.
   If a style changes distinguishability, then compare the actual rendered symbols
   rather than inferring recognition from a font name or a source-style value alone.
   If enlarging or restyling content clips or substitutes characters, then repair
   that presentation loss before judging the remaining visible symbols legible.

4. Verify: Render the preserved content under the agreed conditions and obtain
   unaided audience transcriptions against the source-character oracle.
   If viewers confuse a symbol, then retain that confusion and its condition;
   do not average it away with easy strings or explain the answer before scoring.

5. Report: Return rendered conditions, actual content, character confusions,
   preservation checks, and recognition evidence or its absence.
   If no target viewer inspected the render, then label recognition unverified;
   static style inspection is supporting evidence, not an audience observation.

## Specification patterns

- **Recognition:** Under `{rendered_viewing_conditions}`, `{audience}` shall
  distinguish `{characters_and_symbols}` within `{confirmed_error_bound}`, verified
  by `{unaided_transcription_against_source_oracle}` with `{source_content}` preserved.
- **Rendering preservation:** At `{agreed_display_and_scaling}`, `{content}` shall
  retain `{required_visible_characters}` without `{clipping_or_substitution}`,
  evidenced by `{render_comparison_and_content_check}`.

The illustrative error bound covers only its selected content and conditions;
confirm with the user/stakeholder. Ask the user for unverified display/audience assumptions.

## Rules of thumb

- Do test the actual confusing glyph pairs in their rendered context; a font that
  looks clear in a specimen may still obscure the identifier this audience must recognize.
- Do preserve the literal identifier while improving its rendering; replacing a
  confusing source character changes the content rather than proving it distinguishable.
- Do inspect fallback rendering as well as the requested font; missing glyph support
  can make the delivered symbols differ from the design specimen being accepted.
- Do retain difficult characters in the recognition set; removing them can improve
  an error count without repairing the visual confusion the user reported.
- Don't accept larger text that hides required suffixes through clipping; visible
  glyph recognition cannot compensate for content no longer presented to the viewer.

## Verification

Use rendered-content comparison, glyph-confusion transcription, and layout/clipping
inspection categories. Record display/medium, font actually used, scaling, background,
and viewing context rather than prescribing a standard threshold without a source.
Compare exact character sequences, not inferred word meaning. Observe confusion
pairs by condition; no viewer evidence means the recognition claim remains open.

## Done checklist

- [ ] Match source characters to the rendered sample without content substitution.
- [ ] Exercise the reported confusion pairs under the agreed viewing conditions.
- [ ] Inspect actual/fallback glyph rendering rather than requested style alone.
- [ ] Check required characters remain visible after layout/scaling changes.
- [ ] Record unaided transcriptions and exact mismatches against the source oracle.
- [ ] Separate unavailable audience evidence from static rendering inspection.

## Failure modes

- Changing an identifier to avoid testing a visually confusing original character.
- Testing a font specimen while a different fallback reaches the actual display.
- Counting easy strings while omitting the reported confusable pairs.
- Enlarging text until required trailing characters disappear.
- Claiming accessibility conformance from a legibility fixture alone.

## References

- Read [recognition patterns](./references/design-patterns.md) when choosing visual
  conditions, actual/fallback glyph checks, or transcription evidence.
- Read [identifier example](./references/worked-example.md) when comparing literal
  character recognition without changing the source identifier or interpreting its meaning.
