# Resource per correct report

This is a hypothetical accounting fixture, not a profile of real workers.
Required report contents and quality are identical for all compared candidates.

## Illustrative inputs and ratio

Illustrative fixture and target; confirm with the user/stakeholder:
Compare scoped CPU-seconds per correct report and propose a 10% reduction target.

| Candidate | CPU-seconds | Correct reports | CPU-seconds per correct report |
| --- | ---: | ---: | ---: |
| Baseline | 20 | 100 | 0.20 |
| Less total work but missing required results | 16 | 80 | 0.20 |
| Matched useful output candidate | 18 | 100 | 0.18 |

The missing-results candidate consumes less total CPU but does not improve the
ratio and violates the unchanged useful-output obligation.
The matched-output candidate's illustrative ratio reduction is 10%; confirm with
the user/stakeholder before adopting this target or treating a real comparison as accepted.

## Carried scope and negative case

Retain the input set, correct-result validation and device/config state with the
resource ledger. If the candidate moves work into another process outside the
counter, mark the omitted consumption instead of accepting a whole-task saving.
If reuse adds cache fill or expiry work, include it under the agreed horizon.

## Proposed requirement and verification

For the confirmed workload/output quality, compare scoped CPU per correct report
against the baseline using the agreed allocation rule, while retaining existing
service constraints. Recompute from retained totals and inspect incorrect/missing
results separately. The ratio does not establish measured energy, cost or carbon.
No worker run, profiler reading or operational saving was observed in this example.
