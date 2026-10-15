# Rendered symbol-recognition patterns

Establish the real content and viewing conditions before proposing style changes.
These patterns contain no universal size/contrast threshold or compliance claim.

## Confusion-pair render comparison

- **Use when:** Specific glyphs or symbols are mistaken for one another. Compare
  candidate renders using the actual identifier context, not only a specimen alphabet.
- **Trade-off:** A style that separates a pair may make another distinction worse;
  keep the real confusing content and required symbol set in the comparison.
- **How to verify:** Obtain unaided literal transcriptions under the agreed display
  conditions and compare exact character positions with the source oracle.

## Actual font and fallback inspection

- **Use when:** Requested assets or glyph coverage may differ from delivered content.
  Inspect what the target render actually uses for the relevant symbols.
- **Trade-off:** Source styling alone cannot establish a delivered render, and a
  fallback can alter symbol shapes without changing the underlying character string.
- **How to verify:** Compare the intended and actual glyph output, including a
  missing-asset/fallback fixture where the target environment supports that test.

## Visibility preservation under layout changes

- **Use when:** Scaling, spacing, or restyling is proposed. Preserve all required
  characters in the final region, including prefixes, suffixes, and adjacent labels.
- **Trade-off:** Larger symbols can consume space and hide other needed content;
  recognition of a visible fragment does not establish presentation of the full identifier.
- **How to verify:** Inspect actual rendered boundaries at agreed conditions and
  transcribe the entire string, retaining clipping and substitution as failures.

For an illustrative recognition fixture, propose 0 symbol-transcription errors;
confirm with the user/stakeholder. Ask the user for audience, viewing setup and
allowed changes; style names and author preference cannot establish viewer recognition.
