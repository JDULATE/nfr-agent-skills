# Remaining routing misses: description revision findings

The requested 58 historical misses map to 45 descriptions. Only those description fields changed. Skill bodies, references, catalogue records, existing eval wording, keys, and scripts are unchanged. Each exact existing Not for clause remains intact. Revised descriptions contain three quoted developer phrases, have no duplicated quoted phrase across the catalogue, and range from 252 to 350 characters.

## Blinded comparison

The selected test contains 195 unique unchanged prompts: 58 historical misses and 137 sibling controls. Controls come from the existing near-miss cases of affected skills, matched back to the original blinded prompt IDs. The selection and source mappings are in evals/routing-fixes-58/selection.json. The five prior control regressions were not added as revision targets.

Both comparison runs used fresh ephemeral Codex CLI sessions, the same neutral routing instructions, identical prompt order, identical catalogue formatting, default model settings, ignored user configuration, and inline catalogue/prompt contents. No answer key, previous answer, review, or expected group was supplied. Both transcripts contain one agent message and no tool calls. Model name was not reported by CLI; no model override was used.

| Cases | Before | After | Newly matching | Regressions |
| --- | ---: | ---: | ---: | ---: |
| Requested historical misses | 15/58 | 50/58 | 35 | 0 |
| Sibling controls | 136/137 | 136/137 | 0 | 0 |
| Explicit subgroup | 80/80 | 80/80 | 0 | 0 |
| Vague subgroup | 71/115 | 106/115 | 35 | 0 |
| Total | 151/195 | 186/195 | 35 | 0 |

The historical 58 were failures of the previous agent run. Fifteen already matched in this fresh pre-edit CLI baseline, so 50 historical matches cannot all be attributed to these edits. Eight requested cases still fail the frozen key, plus one previously failing sibling control. Every remaining key expects ask. There are no user-voice cases in this selected set.

An earlier post-edit run used heading-style catalogue formatting. Its results are retained under format-check/: 185/195 overall, 50/58 historical matches, and 80/80 explicit matches. The final run restored the baseline bullet format and changed no descriptions between these two runs. The final run was selected for matched formatting, not for its score. A single paired run does not establish repeatability.

## Remaining disagreements

| ID | Source | Prompt | Before | After | Expected |
| --- | --- | --- | --- | --- | --- |
| r-212433c508cb6344 | requested | Use the validator in the CLI too. | reusability | reusability | ask |
| r-2eec4750902942a8 | requested | Should we keep this product? | viability | viability | ask |
| r-8bfd522e94801264 | sibling control | Make these rules precise. | formality | formality | ask |
| r-9bc5df77b7002ca8 | requested | Make the screen explain itself. | self-descriptiveness | self-descriptiveness | ask |
| r-dd8b0409043f8049 | requested | Where did this wrong value come from? | debuggability | debuggability | ask |
| r-e7f93ec80c7a461b | requested | Is this still worth running? | viability | viability | ask |
| r-ebe06c04252d4ce8 | requested | The export feature is missing. | functionality | functionality | ask |
| r-f02044e5b76544fb | requested | Swap this backend. | replaceability | replaceability | ask |
| r-f5104ee00e36ed63 | requested | Get the service back. | recoverability | recoverability | ask |

These are unresolved scoring disagreements, not silently relabeled successes. Reuse of a validator in another interface, a missing export operation, a backend replacement, service restoration, and continued product value each provide a plausible skill-level route despite missing implementation details. Asking for every missing detail would conflict with the router instruction that implementation questions can follow a known route. The wrong-value prompt still leaves room for execution diagnosis versus broader analysis; screen explanation may concern current-state cues or comprehension. Those interpretations need human adjudication before calling the remaining choices either correct routes or description defects. The precision prompt is a sibling control whose selected formality description was not changed.

## Description changes

The main change replaces generic if-unclear hedging with concrete sibling-selection questions. Trigger wording was tightened where necessary to retain every original exclusion within the character budget. Some full-sentence questions consume space that could otherwise hold richer ticket wording; this is a remaining trade-off. No skill meaning was changed to forbid an otherwise legitimate route.

| ID | Slug | Before characters | After characters |
| ---: | --- | ---: | ---: |
| 002 | accountability | 278 | 329 |
| 007 | affordability | 260 | 295 |
| 010 | anonymity | 313 | 322 |
| 015 | availability | 286 | 314 |
| 016 | certainty | 241 | 295 |
| 023 | comprehensibility | 313 | 350 |
| 033 | debuggability | 296 | 327 |
| 036 | demonstrability | 303 | 324 |
| 038 | distributivity | 243 | 262 |
| 042 | enhanceability | 331 | 345 |
| 045 | expressiveness | 290 | 300 |
| 048 | fault-failure-tolerance | 303 | 325 |
| 049 | feasibility | 282 | 291 |
| 052 | functionality | 321 | 349 |
| 055 | installability | 292 | 330 |
| 056 | integratability | 234 | 265 |
| 058 | interoperability | 236 | 252 |
| 061 | likeability | 314 | 342 |
| 063 | maintainability | 319 | 340 |
| 064 | manageability | 329 | 339 |
| 066 | measurability | 318 | 331 |
| 071 | operability | 338 | 346 |
| 074 | predictability | 343 | 313 |
| 076 | provability | 281 | 302 |
| 078 | readability | 298 | 325 |
| 079 | reconfigurability | 328 | 344 |
| 080 | recoverability | 343 | 325 |
| 083 | replaceability | 234 | 259 |
| 085 | reusability | 310 | 320 |
| 088 | scalability | 346 | 346 |
| 090 | self-descriptiveness | 350 | 312 |
| 091 | simplicity | 330 | 337 |
| 093 | standardizability-standardization-standard | 251 | 268 |
| 095 | suitability | 280 | 319 |
| 096 | supportability | 329 | 316 |
| 097 | survivability | 348 | 341 |
| 099 | sustainability | 337 | 348 |
| 104 | transferability | 349 | 333 |
| 106 | understandability | 333 | 350 |
| 108 | usability | 317 | 334 |
| 109 | variability | 310 | 340 |
| 110 | verifiability | 322 | 320 |
| 111 | versatility | 318 | 335 |
| 112 | viability | 345 | 302 |
| 114 | wrappability | 297 | 330 |

Exact before/after strings are retained in description-changes.json. The current and baseline catalogue snapshots are separate; the original full-catalogue routing artifacts remain historical snapshots.

## Validation and limitations

- Full repository validator: 114 checked, no absent todo skills, zero errors.
- Full unittest suite: 34 tests passed under normal restored permissions; no temporary-directory workaround was required.
- Routing scorer accepted all 195 unique answers with no missing, duplicate, unknown, or invalid choices. Its successful exit indicates valid grading inputs, not perfect routing.
- Scope checks confirmed unchanged bodies and non-description frontmatter for all skills, unchanged descriptions outside the selected 45, and exact preservation of selected boundary tails.
- Supplemental Skill Creator validator: 43 of the 45 selected skills pass. Availability and readability retain pre-existing status frontmatter rejected by that supplemental tool. The repository validator accepts it; this description-only revision does not remove it.
- Read-only lexical checker on the 45 affected eval sets: 360 prompts, 180 without the distinguishing fact, 237 flagged pairs. Flag counts: expected_not_top 183; near_pair_no_signal 42; near_pair_tie 3; near_target_outranks_sibling 12; no_keyword_signal 16; top_tie 35. These overlapping warnings are heuristic findings, not routing accuracy; descriptions were not changed in response to them.
- No new factual standards claims were introduced. The unresolved claims concern prompt interpretation and whether frozen ask labels are appropriate. No scoring labels were changed.

Raw comparison transcripts, input hashes, CLI arguments, results, scores, supplemental findings, and check outputs are retained in evals/routing-fixes-58/.
