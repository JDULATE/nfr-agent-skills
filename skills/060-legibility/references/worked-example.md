# Worked example: a literal identifier with confusable symbols

Assume a fictional asset view must display the literal identifier `asset_O0Il`.
Its suffix contains uppercase O, digit zero, uppercase I, and lowercase l in that
order. This is a synthetic content fixture, not a naming recommendation.

Illustrative recognition bound only: 0 transcription errors for the selected string;
confirm with the user/stakeholder before adopting the content, conditions or bound.
Propose: "Under `{recorded_viewing_conditions}`, `{audience}` shall distinguish
`{literal_identifier_characters}` within `{confirmed_error_bound}`, verified by
`{unaided_transcription_against_source}` without changing `{identifier_value}`."

| Render or response | Interpretation against the source oracle |
| --- | --- |
| Viewer transcribes `asset_O0Il` | Matches the literal fixture; not proof under other displays |
| Viewer transcribes `asset_00Il` | Uppercase O was confused with zero |
| Viewer transcribes `asset_O0II` | Final lowercase l was confused with uppercase I |
| Candidate view shows only `asset_O0` | Clipping loses required suffix content even if visible symbols are recognized |
| Source identifier changed to `asset_asset` | Different content, not improved recognition of the reported identifier |

Record the actual display/medium, font used, scaling, background, and audience
context for every candidate. Compare rendered outputs under those same conditions;
do not infer a result from a requested style value that the target never delivered.
Test a fallback condition if applicable and inspect the whole identifier boundary.

Carry the exact source string into each render and preserve the answer key before
asking viewers to transcribe it. Provide the distinguishing-character explanation
only after collecting the unaided answer, or it becomes a coached response.
If no target viewer is available, report render/content checks and the missing
recognition evidence separately. No real font, monitor, participant, or accessibility
standard was tested by this example.
