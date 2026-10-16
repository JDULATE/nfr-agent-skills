# Parser selector localization example

This is an illustrative synthetic execution, not an observed repository defect.
All values and proposed fixture behavior are illustrative examples;
confirm with the user/stakeholder before adopting the parser contract.

## Filled execution record

| Field | Fixture value |
| --- | --- |
| Parser revision | selector-fern |
| Input | label=red;value=7 |
| Grammar boundary | semicolon-separated named fields; value must be an integer |
| Expected result | integer 7 |
| Initial state | no cache, no prior parsed record, no side effects |
| Dependencies | string selection and integer conversion only |
| Observed symptom | integer conversion of red;value=7 fails |
| Captured location | conversion call after first-equals selection |
| Carried state after failure | none |
| Localization question | conversion semantics or wrong selected candidate? |

## Failing path

The original selector takes everything after the first equals sign:
```text
candidate = split_once(input, "=").right
result = integer(candidate)
```

For the recorded input, candidate is red;value=7.
The conversion exception is consistent with that non-integer candidate.
The value field itself contains 7, so the next discriminating check is field selection.

Input value=7 produces candidate 7 and succeeds.
Removing the value field instead would change the required input contract and
would not be a valid smaller reproducer of this selector problem.

## Remediation of the localization gap

Capture the selected field before conversion:
```text
expected_field = value
actual_selection = suffix_after_first_equals
candidate = red;value=7
```

The first supported divergence is selection of the suffix rather than the
named value field. This explains the constructed failure without blaming
integer conversion or a system-wide dependency.

## Corrective experiment

Split the record into named fields, select value, and convert that field only.
| Input | Before candidate / result | After candidate / result |
| --- | --- | --- |
| label=red;value=7 | red;value=7 / conversion error | 7 / integer 7 |
| value=7 | 7 / integer 7 | 7 / integer 7 |
| label=red;value=bad | red;value=bad / conversion error | bad / conversion error |

The malformed value still fails, so the experiment is not merely an exception suppressor.
Each case starts with empty parser state and leaves no stored result.

## Requirement example and limits

For this recorded failure, the debugging path shall expose the selected candidate
and field boundary before conversion and connect the mismatch to selector-fern.

This local experiment does not establish handling of duplicate keys, escaping,
missing fields, or a production parser's full grammar. Those inputs are outside
the stated fixture contract and remain separate implementation decisions.
