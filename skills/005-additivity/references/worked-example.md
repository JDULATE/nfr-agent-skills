# Worked example: combine processing increments

Use this invented exact-count example, not a result measured from the user's system.
Suppose project code and experiment notes describe a completed-work counter and
distinct increments that add work under the same fixture.

## Inspect and propose

Read the counter update path, increment identity rule, and measurement notes.
Ask the user whether completed units are distinct and whether replay should create
new work. Do not infer those policies from a counter's variable name.

Illustrative values only; confirm with the user/stakeholder before using these
values or the acceptance bound in a project:

| Measurement | Completed units |
| --- | --- |
| Baseline | 10 |
| Baseline with increment A | 12 |
| Baseline with increment B | 13 |
| Observed baseline with A and B | 15 |

Subtract the baseline to obtain contributions of 2 and 3 units. Calculate the
expected combined outcome as 10 + 2 + 3 = 15 units, not 12 + 13 = 25.
The illustrative residual is 15 - 15 = 0 units; confirm with the user/stakeholder
before accepting that exact-count bound for the real metric.

Write: "Under the matched completed-work fixture, combining the named increments
shall preserve their distinct baseline-relative units under the agreed sum rule,
within `{confirmed_absolute_tolerance}`, verified by the contribution ledger."

## Expose a false positive

Now make A and B refer to the same synthetic work identity. Under a unique-work
policy, expect a union of identities rather than the isolated gains' simple sum.
If the implementation still increments the total on both deliveries, record a
duplicate contribution. If the user instead intends separate work on every
delivery, record that policy and derive a different expectation explicitly.

Compare reversed order and an empty increment as well. Report the rule, matched
conditions, and residual; the arithmetic demonstration alone does not establish
additivity in a production pipeline or explain every interaction it may exhibit.
