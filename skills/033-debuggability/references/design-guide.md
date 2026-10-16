# Localization design decisions

Choose the next observation that can identify a particular execution's divergence.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| The stack ends in a conversion helper. | Capture the candidate and selection boundary before conversion. Captures may need synthetic data or redaction. | Compare the selected field with the authoritative input contract. |
| Replay depends on a live response that has changed. | Record a permitted response fixture at the boundary. The replay no longer covers that live integration. | Match the original response shape and verify the same named symptom occurs. |
| A reduced input throws, but with a different message. | Restore the removed trigger and reduce under the original symptom predicate. The minimal case may stay larger. | Compare failure type, failing boundary, and candidate value. |
| Trace locations disagree with the checked-out source. | Obtain the matching source/build mapping before attributing the line. This can delay a proposed repair. | Resolve the captured location to the actual expression for that revision. |

## Candidate inspection sketch

```text
capture(input_record, parser_revision)
candidate = selector(input_record)
inspect(candidate, selected_field, expected_field)
convert(candidate)
```

The sketch describes inspection of the real selector.
Replacing the selector with the expected result would destroy the localization evidence.

## Testing the explanation

Use a small corrective experiment at the implicated boundary.
Compare the original failure and a neighboring valid input.
Keep a malformed-value case so an unrelated fallback does not make every input succeed.

Temporary captures can perturb execution or expose sensitive data.
Use the smallest authorized synthetic view and report any replay substitution.
If the original execution is not reproducible, distinguish inspected evidence
from a reconstruction that merely resembles it.
