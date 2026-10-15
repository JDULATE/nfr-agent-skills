# Worked example: refine the existing date parser

Assume a hypothetical parser already accepts a documented set of date strings
and produces the same structured date result for existing callers. The user wants
fewer incorrect results for those supported strings, not another parsing feature.

## Read the baseline

Inspect parser code, accepted input grammar, reference answers, and consumer docs.
Retain the original corpus and outputs. Ask the user which ambiguous inputs are
in the supported set and which already-correct cases must stay correct.
Do not expand the grammar and call that expansion an improvement on the old task.

## Requirement proposal

Write: "The existing parser shall permit refinement of `{internal_date_strategy}`
while preserving `{supported_input_and_result_contract}`, improving
`{unchanged_error_measure}` over `{retained_corpus}` to `{confirmed_target}`, with
`{protected_input_groups}` unchanged under `{accepted_tradeoff_policy}`."

Illustrative target only: propose 10% fewer reference-answer errors on the retained
corpus; confirm with the user/stakeholder. Do not substitute this value for the
project's acceptance criteria or use a relative target with an empty error baseline.

## Concrete refinement boundary

Keep the public parser's input checks and structured output adapter. Replace the
internal interpretation strategy as the candidate change, retaining old outputs
for comparison. Suppose an ambiguous month label improves but an already supported
numeric form regresses. Show both outcomes; an improved total does not settle
whether that regression is acceptable.

Use this illustrative fixture, with its input meanings defined for the example
only; confirm with the user/stakeholder before adopting these interpretations:

| Input | Reference result | Baseline result | Candidate result |
| --- | --- | --- | --- |
| `May 07` | month May, day 07 | month March, day 07 | month May, day 07 |
| `05-07` | month May, day 07 | month May, day 07 | month July, day 05 |

The candidate fixes the labeled form but breaks the protected numeric form under
this invented grammar. Do not adopt it solely because a larger aggregate improved.
These cases do not establish the illustrative relative-error target; measure that
target on the agreed full corpus without changing its reference answers.

| Fixture | Inspect | Decision |
| --- | --- | --- |
| Previously incorrect supported label | Candidate and baseline against the same reference answer | Count gain only under unchanged scoring |
| Protected numeric form | Original correct answer versus candidate result | Resolve regression before adopting the strategy |
| Unsupported new grammar | Existing rejection behavior | Treat requested support as a separate capability change |
| Candidate deselected | Existing consumer receives the old result meaning | Verify reversal rather than assuming a strategy flag is enough |

Report a refinement design and measured evidence separately. This fictional
corpus provides no actual gain, coverage estimate, or proof about a real parser.
