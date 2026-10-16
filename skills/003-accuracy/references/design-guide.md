# Error-reduction decisions

Use a confirmed reference model before changing reported values.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Paired readings show a stable offset in the fitting cases | Store an explicit correction parameter with its applicable conditions | Correction may not apply outside those conditions | Evaluate separate reference cases before accepting the correction |
| A conversion uses a different unit than the reference | Normalize to the confirmed comparison unit before subtraction | Conversion precision becomes part of the error path | Recompute known paired values through the actual conversion |
| Display rounding moves a failing value onto the acceptance boundary | Compare at retained precision, then round only for presentation | Display and acceptance values need clear labels | Exercise a raw value just outside tolerance that displays on the boundary |
| Reference uncertainty spans the acceptance boundary | Return an indeterminate comparison under the agreed reference rule | Fewer apparently decisive pass/fail results | Vary the reference within its supplied bounds and inspect whether the decision changes |

## Comparison sketch

Illustrative pseudocode; no statistical interpretation is implied.

```text
compare(raw, reference, correction, tolerance):
    corrected = raw - correction
    signed_error = corrected - reference
    absolute_error = abs(signed_error)
    return {
        corrected: corrected,
        signed_error: signed_error,
        absolute_error: absolute_error,
        pass: absolute_error <= tolerance
    }
```

Apply this only after unit alignment and the reference-uncertainty decision.
Keep display formatting outside the comparison.
A correction parameter is not evidence of a physical cause.

## Intervention boundary

If deviations vary with quantity, do not assume an offset is adequate.
Inspect the paired pattern and propose a different model only with supporting
data and domain confirmation. Do not silently fit a more complex correction
until it matches the same evaluation cases.
