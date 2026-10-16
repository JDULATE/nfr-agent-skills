---
name: accuracy
description: >-
  Reduces error against a reference when tickets say "our sensor readings are off", "the reported weight misses the reference", or "rounding hides the measurement error". Not for following a specified algorithm (see correctness) or confidence labels (see certainty).
---

# Accuracy

## Definition and scope

Accuracy means a value is close enough to an agreed reference under a stated
error model. Identify what the reference represents and how its uncertainty
affects the comparison. Separate observed value error from following a specified
algorithm (`correctness`) and the confidence attached to an output (`certainty`).

## Use when / Don't use when

- Apply when measured or reported quantities differ from reference observations,
  including systematic offsets or precision choices that conceal error.
- Require the quantity, units, reference authority, and acceptable error model.
- Route a calculation that violates its approved formula to `correctness`.
- Route an unsupported confidence label to `certainty`; a confident value can
  still have substantial reference error.
- Route defining a collection procedure without an error question to `measurability`.

## Workflow

1. Clarify: Read measurement code, conversions, calibration configuration,
   reference fixtures, and domain documentation before specifying.
   Identify which reference observations are authoritative for the stated use.
   If reference authority or comparability is unknown, then Ask the user rather
   than treating an existing output as ground truth.

2. Specify: Record quantity, unit, reference revision, pairing rule, signed and
   absolute error definitions, tolerance, and reference-uncertainty treatment.
   If tolerance is missing, then propose a labeled illustrative default:
   compare unrounded paired values against the stakeholder's reference, with
   pass/fail left open until tolerance is confirmed; confirm with the user/stakeholder.
   For a practical fix, ask at most three questions about reference authority,
   error/tolerance, and operating conditions before proposing a correction.

3. Design/Implement: Read [error-reduction decisions](./references/design-guide.md)
   when evaluating conversion, offset correction, or comparison precision.
   If paired errors support an offset correction, then isolate its fitted
   parameters from the cases used to evaluate it.
   If the reference uncertainty can change the acceptance decision, then report
   an indeterminate comparison instead of attributing the difference to the system.

4. Verify: Compare raw observations and corrected outputs with their paired
   reference values under the declared conditions.
   Preserve original samples, missing observations, and evaluation membership.
   If a sample cannot be paired, then report it as unevaluated rather than zero error.
   Inspect both signed error and absolute error before applying the chosen criterion.

5. Report: Return the reference record, correction, per-case errors, aggregate
   calculations if requested, and uncertainty-limited decisions.
   If only fixture cases were evaluated, then limit the accuracy claim to them
   and do not infer performance on unobserved quantities or operating conditions.

## Specification patterns

- **Point error:** For `{quantity_and_conditions}`, reported `{value_in_unit}`
  shall differ from `{paired_reference}` by at most `{confirmed_tolerance}`
  under `{reference_uncertainty_rule}`, verified using `{unrounded_comparison}`.
- **Correction:** Applying `{correction_revision}` shall satisfy
  `{error_criterion}` on `{evaluation_cases_not_used_to_fit}`, reporting
  `{signed_and_absolute_errors_and_unpaired_cases}`.

For absent targets, use the illustrative comparison proposal in Specify;
confirm with the user/stakeholder before assigning pass/fail or choosing a tolerance.

## Rules of thumb

- Diagnose an offset from paired reference differences, not from a desired display
  value; forcing a pleasing reading can move the result farther from the reference.
- Do not accept small signed mean error as small point error; opposite deviations
  can cancel even while individual readings exceed the agreed error tolerance.
- Compare before display rounding; a value rounded onto the tolerance boundary
  must not hide an unrounded reference error outside that boundary.
- Keep reference uncertainty distinct from instrument error; an uncertain reference
  cannot justify claiming the device missed an exact value it never established.

## Verification

Use paired-reference fixtures, conversion review, and correction evaluation.
Keep fitting and evaluation cases identified; retain unfavorable results.
Check unit alignment before subtracting values.
Recompute errors from unrounded data, including cases just inside and outside
the tolerance. Evaluate any correction under the stated operating conditions.
Report coverage and excluded or unpaired observations with their reasons.
Do not equate repeatable outputs with accurate outputs; repeatability has no
external reference requirement.
Use reference uncertainty only under a stakeholder-confirmed interpretation,
not an invented statistical guarantee.

## Done checklist

- [ ] Identify quantity, unit, conditions, and reference authority.
- [ ] Check pairing and conversion against actual fixture values.
- [ ] Confirm the error model and tolerance or mark acceptance unresolved.
- [ ] Separate fitting cases from correction-evaluation cases.
- [ ] Recompute unrounded signed and absolute errors.
- [ ] Check the display-rounding boundary and uncertainty-limited cases.
- [ ] Bound the reported claim to evaluated observations and conditions.

## Failure modes

- Using yesterday's system output as an unquestioned truth reference.
- Reporting cancelling signed deviations as uniformly small error.
- Evaluating a correction only on the cases used to fit it.
- Rounding before comparison and hiding an out-of-tolerance observation.
- Claiming exact error against a reference whose uncertainty is unresolved.

## References

- Read [error-reduction decisions](./references/design-guide.md) when selecting
  a correction and comparison boundary.
- Read [weighing example](./references/worked-example.md) when calculating
  paired errors and separating a fitted offset from its evaluation.
