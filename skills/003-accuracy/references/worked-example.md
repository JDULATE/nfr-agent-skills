# Reference-based weighing correction

This is a synthetic fixture with illustrative quantities, tolerance, and error
criteria; confirm with the user/stakeholder before using them as requirements.
It does not establish a real instrument's physical calibration.

## Filled comparison record

| Input | Value |
| --- | --- |
| Quantity and unit | displayed mass in grams |
| Operating condition | fixture bench mode amber; unchanged across cases |
| Reference source | stakeholder-supplied fixture reference table revision cedar |
| Reference interpretation | assigned exact values for this model only |
| Pairing | reading and reference share the same sample id |
| Error model | corrected reading minus reference; absolute magnitude for acceptance |
| Illustrative tolerance | absolute error at most 0.5 g; confirm with the user/stakeholder |
| Fitting cases | seed-a and seed-b |
| Evaluation cases | check-c and check-d; not used to select the correction |
| Correction owner | measurement feature maintainer role |
| Initial correction state | offset=0 g |
| Persistent observation state | the raw/reference table below, unchanged after correction |

| Sample | Role | Reference g | Raw reading g |
| --- | --- | --- | --- |
| seed-a | fitting | 100 | 102 |
| seed-b | fitting | 200 | 202 |
| check-c | evaluation | 250 | 252.2 |
| check-d | evaluation | 300 | 301.8 |

## Before remediation

With offset=0, check-c has signed error +2.2 g and absolute error 2.2 g.
Check-d has signed error +1.8 g and absolute error 1.8 g.
Both fail the illustrative tolerance.

The fitting differences are +2 g in each seed case.
That supports trying an offset in this model; it does not establish why the
instrument is offset or whether the pattern holds outside the supplied conditions.

## Remediation and after outputs

Set offset=2 g based only on the seed cases.
Retain raw readings; calculate corrected values separately.

| Evaluation sample | Corrected g | Signed error g | Absolute error g | Outcome |
| --- | --- | --- | --- | --- |
| check-c | 250.2 | +0.2 | 0.2 | pass |
| check-d | 299.8 | -0.2 | 0.2 | pass |

Correction state is now offset=2 g.
The raw/reference table remains unchanged.
The signed average is zero, but the point errors are not zero.

## Display-rounding negative

Use an independent comparison input with offset=0, reference=100 g,
and raw=100.54 g under the same illustrative 0.5 g tolerance.
Raw absolute error is 0.54 g, so it fails.
Formatting the reading to one decimal gives 100.5 g and would incorrectly pass
if the comparison used that display value.
Keep the raw comparison and display output separate.

## Uncertainty-limited branch

Supply reference interval [99.9, 100.1] g and corrected reading=100.6 g.
Possible absolute errors range from 0.5 to 0.7 g.
Under the proposed rule that a comparison is indeterminate when the supplied
reference interval changes pass/fail, this case is indeterminate.
That rule is illustrative; confirm with the user/stakeholder.
No probability or confidence percentage is inferred from the interval.

## Limits

Report the separate evaluation cases and precision check, not a general accuracy
guarantee. Other quantities, physical conditions, drift, and the authority of a
real reference source remain outside this fixture.
