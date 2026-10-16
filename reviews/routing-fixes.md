# Routing miss revision findings

## Scope and preservation

- Revised the 69 descriptions implicated by the 94 approved misses: 68 previously chosen skills plus the expected extensibility entrypoint.
- All descriptions remain at or below 350 characters with three quoted developer phrases. Every original Not for clause is preserved exactly, including its sibling pointers.
- Preserved all 114 skill bodies and non-description frontmatter fields. The other 45 descriptions, original evals, catalogue, index, scripts, original routing snapshots and original results are unchanged.
- Added routing questions for the actual neighboring concerns instead of broad keyword triggers. Extensibility now begins by inspecting hooks for a requested addition without core edits; building or widening the hook still belongs to extendability.
- No answer label, prompt wording, or expected group was changed to improve a score.

## Focused evaluation

The test contains the original 94 failed prompt ids plus 174 unique sibling controls. Controls are the existing near-miss prompts from the affected skills, selected one hop only and deduplicated against the frozen routing prompts. All 114 descriptions remain candidates. The seven previously passing user-voice prompts were not rerun.

The baseline for this same subset is copied from the original completed routing run. Every additional control previously passed.

| Group | Baseline correct / total | First revision check | Final revision check | Final accuracy |
| --- | ---: | ---: | ---: | ---: |
| explicit | 112 / 112 | 112 / 112 | 112 / 112 | 100.00% |
| vague | 62 / 155 | 91 / 155 | 92 / 155 | 59.35% |
| user_voice | 0 / 1 | 1 / 1 | 1 / 1 | 100.00% |

- Of the original 94 misses, 36 now match the key and 58 remain misses.
- Five of the 174 previously passing controls now miss. All five are labeled vague; all 112 explicit controls still pass.
- The failed report-plugin user-voice prompt now selects extensibility as expected.
- The final subset has 205 correct answers and 63 misses. All 268 ids were answered once with a valid slug or ask.

## Execution limits

- Managed permissions blocked the standalone CLI while initializing its user-level Codex runtime. It produced no routing answers and was not scored.
- Both revision checks used separate fresh Codex agents with fork_turns=none. Each was instructed to read only the candidate catalogue and unlabeled prompts; neither received labels, earlier choices, reviews, selection metadata, or parent conversation. Both agents reported reading only the two input files.
- The original baseline used CLI default; the fresh-agent checks inherit the primary model. The model identity is not asserted to match the earlier CLI default, and the score changes cannot be attributed solely to the descriptions.
- First check task: /root/blinded_router_fixes. Final check task: /root/blinded_router_fixes_round2. The first answers, score and catalogue are preserved separately.
- The second check followed focused clarification changes for generality, recoverability, comprehensibility and extensibility. Both checks are reported; the first outcome is not hidden.
- A generated blocked-CLI runtime directory remains outside the repo under the workspace because managed policy rejected its cleanup. It is not part of this commit. The failed standard test also left an inaccessible temporary directory.

## Original misses still failing

The frozen key expects ask for every row below. These remain observations, not adjudicated description defects.

| Id | Prompt | Previous choice | Final choice |
| --- | --- | --- | --- |
| r-09b28c71fc1887dc | Handle more traffic. | scalability | scalability |
| r-10fa474e5e2b4e6c | Completion feels unpredictable. | predictability | predictability |
| r-136e0a1f295bde94 | Help me debug this failure. | debuggability | debuggability |
| r-1d3450cfae00e2ec | Make this easier to look after. | maintainability | maintainability |
| r-212433c508cb6344 | Use the validator in the CLI too. | reusability | reusability |
| r-25efb477bee0fd0a | We need different editions. | variability | variability |
| r-27ab27a7e5e93872 | Handle more users. | scalability | scalability |
| r-2820e20b462b3c0d | Stop copying this helper. | reusability | reusability |
| r-2eec4750902942a8 | Should we keep this product? | viability | viability |
| r-37eb69ec9d791f9d | Make checkout easier. | usability | usability |
| r-3e20a3b68eff4295 | People do not enjoy this. | likeability | likeability |
| r-40c0859ae907228b | Will this design work here? | feasibility | feasibility |
| r-43071ab7a17cb5f6 | This rule language can't say what we need. | expressiveness | expressiveness |
| r-5174f6e026d7200e | We need to stop using the old provider. | replaceability | replaceability |
| r-526b3ad54e859b5a | Our service needs better uptime. | availability | availability |
| r-52c0dc8b3ab03d92 | Help us wire these services together. | integratability | integratability |
| r-53bb9c6161763cce | Make this dataset less identifying. | anonymity | anonymity |
| r-56677163d27567d6 | Help us hand this project over. | transferability | transferability |
| r-58be2272a38abc93 | Who was behind this change? | accountability | accountability |
| r-5c2b9641f0aa635c | The report sounds too sure. | certainty | certainty |
| r-625806728696d50b | Do not lose service when things break. | fault-failure-tolerance | fault-failure-tolerance |
| r-65962c0fc744f0cf | Help us with a customer issue. | supportability | supportability |
| r-67191eb0ee8982c0 | The new install won't start. | installability | installability |
| r-779c30432ea37800 | We need a demo for the reviewers. | demonstrability | demonstrability |
| r-7a4eb6ae6c5efa60 | We need one shared format. | standardizability-standardization-standard | standardizability-standardization-standard |
| r-7bd98ba2ba8e01c5 | Show why this requirement passed. | verifiability | verifiability |
| r-7fe916099edff214 | Stop these surprise pauses. | predictability | predictability |
| r-808d30d85b9c52d6 | The export isn't useful for our handoff. | suitability | suitability |
| r-8603efdd7d009787 | This feature doesn't fit our workflow. | suitability | suitability |
| r-90a885445e668703 | Changing config loses work. | reconfigurability | reconfigurability |
| r-94e3d0d51dd15ca6 | Make this code easier to read. | readability | readability |
| r-97d13e456376587b | Can we prove this can't happen? | provability | provability |
| r-9bc5df77b7002ca8 | Make the screen explain itself. | self-descriptiveness | self-descriptiveness |
| r-9d5130866c3f7b13 | Can we afford this export? | affordability | affordability |
| r-b4f2c7711d799a00 | Make this service greener. | sustainability | sustainability |
| r-bf22552eb7865121 | We can't check this requirement. | verifiability | verifiability |
| r-c767a2d18ade0424 | Tell us who did this. | accountability | accountability |
| r-cbbab0547d8fcff7 | Can this tool do another job? | versatility | versatility |
| r-cdb119bd268c8ba9 | The receiver doesn't understand our export. | interoperability | interoperability |
| r-cfa11658661e7b94 | On-call can't finish the job. | operability | operability |
| r-d13d56649866b943 | What exactly are we counting? | measurability | measurability |
| r-d3dc202ad6acb822 | We need better fleet controls. | manageability | manageability |
| r-d80e4afa0c3a60d8 | This feels overengineered. | simplicity | simplicity |
| r-d8fbd88e3c5c9e47 | Can we actually build this? | feasibility | feasibility |
| r-dd8b0409043f8049 | Where did this wrong value come from? | debuggability | debuggability |
| r-e1ef58b88335057c | How will we know this passed? | verifiability | verifiability |
| r-e35b63c6e94e25e8 | We get stuck halfway through a rerun. | operability | operability |
| r-e5a4d18a59da6042 | Put a new API around this old function. | wrappability | wrappability |
| r-e7f93ec80c7a461b | Is this still worth running? | viability | viability |
| r-e906f9ac93ac06df | Make the system easier to understand. | understandability | understandability |
| r-ebe06c04252d4ce8 | The export feature is missing. | functionality | functionality |
| r-f02044e5b76544fb | Swap this backend. | replaceability | replaceability |
| r-f0ea1a4c1fd6cc90 | Make this explanation clearer. | comprehensibility | comprehensibility |
| r-f5104ee00e36ed63 | Get the service back. | recoverability | recoverability |
| r-f6f5291508e402a3 | Sometimes this call is much slower. | predictability | predictability |
| r-f840b615d41cf571 | Can we upgrade this algorithm? | enhanceability | enhanceability |
| r-f9b80679850c9047 | Keep us working through a disaster. | survivability | survivability |
| r-fe27712e62d948ec | Spread this work across nodes. | distributivity | distributivity |

## Previously passing sibling controls now failing

The baseline choice and expected choice were ask for each row.

| Id | Prompt | Final choice | Selected description revised |
| --- | --- | --- | --- |
| r-241bf7e42eedd129 | The package layout is a mess. | structuredness | no |
| r-2ed5a3f566cab0d2 | Customers can't see what's happening. | visibility | no |
| r-34075badeb722eb3 | Can we expose this engine differently? | wrappability | yes |
| r-395aa30520cc1f56 | Can we run both versions? | compatibility | no |
| r-3cc486f153304550 | The pieces work alone but not together. | composability | no |

## Original misses now matching the key

| Id | Prompt | Final choice | Expected |
| --- | --- | --- | --- |
| r-0d6c45b5898145ff | Both changes help alone but not together. | ask | ask |
| r-11a7978c48245818 | Check whether this follows the rules. | ask | ask |
| r-1d8c5d5257e59ead | We need a better audit trail. | ask | ask |
| r-290e28507504f2f8 | The recipient can't use the package. | ask | ask |
| r-2a15293fe4223b00 | Stop adding a special case for every input. | ask | ask |
| r-2a223324cbf197c0 | Another engineer gets a different answer. | ask | ask |
| r-354eada869c66e98 | Can we call this confirmed? | ask | ask |
| r-3caae219ae15a22e | Does this pass on a rerun? | ask | ask |
| r-454ecee0a31f2d9b | It only runs on the old machine. | ask | ask |
| r-4712a66798dbd10d | The page feels uninviting. | ask | ask |
| r-473db3456a90cbc0 | Keep people informed. | ask | ask |
| r-4bc32bb365518dff | Stop overload breaking the worker. | ask | ask |
| r-50cd37978f2a9caf | Which worker owns this job? | ask | ask |
| r-544e2a4c3a959b68 | Fit this tool to our team. | ask | ask |
| r-591489b007912170 | Let admins tweak this. | ask | ask |
| r-5929e4dc4b473e3c | Make this configurable. | ask | ask |
| r-5d6985e8f00a2ac7 | We need to support cancellation. | ask | ask |
| r-668347a0cdc41cb3 | We can't reproduce the timeout in tests. | ask | ask |
| r-6753b4b72a1bf7aa | Do these optimizations work well together? | ask | ask |
| r-677ac388c80fc716 | Is the old version proven enough? | ask | ask |
| r-68251e946af55326 | Split this module up. | ask | ask |
| r-68c83d508f9634a9 | People misread these IDs. | ask | ask |
| r-6fa5f18f3c835424 | Can we combine these improvements? | ask | ask |
| r-76bb5405eadfabb3 | Teams keep inventing their own names. | ask | ask |
| r-7998f646cf36b5db | The export is missing something. | ask | ask |
| r-79e7379966bc813d | This function returns the wrong result. | ask | ask |
| r-8482677b2640a033 | Is the worker stuck? | ask | ask |
| r-8b076602fa74b927 | Move this service to the new host. | ask | ask |
| r-8bfd522e94801264 | Make these rules precise. | ask | ask |
| r-91964c7b1654e2f3 | Let departments work differently. | ask | ask |
| r-b26b3e06a3869d22 | We need to use it beyond imports. | ask | ask |
| r-dc35686fd9e8cf9f | Let customers plug in their own report formats without touching core code. | extensibility | extensibility |
| r-e37944566e76aaf2 | Make this faster. | ask | ask |
| r-e491734c35b483bd | Our fixes take too much effort. | ask | ask |
| r-e7298d8feff7dca8 | Does this feature actually help? | ask | ask |
| r-fa4d7c768527ffb7 | Our tail latency needs work. | ask | ask |

## Description lengths

| Id | Slug | Before | After | Boundary clause |
| --- | --- | ---: | ---: | --- |
| 002 | accountability | 300 | 278 | preserved |
| 005 | additivity | 261 | 258 | preserved |
| 006 | adjustability | 257 | 261 | preserved |
| 007 | affordability | 256 | 260 | preserved |
| 010 | anonymity | 324 | 313 | preserved |
| 012 | attractiveness | 267 | 295 | preserved |
| 013 | auditability | 306 | 302 | preserved |
| 015 | availability | 252 | 286 | preserved |
| 016 | certainty | 224 | 241 | preserved |
| 018 | communicativeness | 289 | 304 | preserved |
| 020 | completeness | 248 | 281 | preserved |
| 023 | comprehensibility | 306 | 313 | preserved |
| 027 | configurability | 311 | 312 | preserved |
| 028 | conformance | 239 | 250 | preserved |
| 031 | correctness | 309 | 325 | preserved |
| 033 | debuggability | 288 | 296 | preserved |
| 034 | decomposability | 261 | 296 | preserved |
| 036 | demonstrability | 281 | 303 | preserved |
| 038 | distributivity | 191 | 243 | preserved |
| 040 | effectiveness | 275 | 263 | preserved |
| 042 | enhanceability | 314 | 331 | preserved |
| 045 | expressiveness | 269 | 290 | preserved |
| 047 | extensibility | 306 | 316 | preserved |
| 048 | fault-failure-tolerance | 303 | 303 | preserved |
| 049 | feasibility | 270 | 282 | preserved |
| 051 | formality | 283 | 298 | preserved |
| 052 | functionality | 286 | 321 | preserved |
| 053 | generality | 318 | 331 | preserved |
| 055 | installability | 260 | 292 | preserved |
| 056 | integratability | 206 | 234 | preserved |
| 058 | interoperability | 200 | 236 | preserved |
| 060 | legibility | 339 | 328 | preserved |
| 061 | likeability | 266 | 314 | preserved |
| 063 | maintainability | 288 | 319 | preserved |
| 064 | manageability | 307 | 329 | preserved |
| 065 | maturity | 315 | 321 | preserved |
| 066 | measurability | 280 | 318 | preserved |
| 070 | observability | 303 | 324 | preserved |
| 071 | operability | 301 | 338 | preserved |
| 072 | performance-efficiency-time-or-space-bounds | 323 | 341 | preserved |
| 073 | portability | 309 | 331 | preserved |
| 074 | predictability | 326 | 343 | preserved |
| 076 | provability | 284 | 281 | preserved |
| 078 | readability | 270 | 298 | preserved |
| 079 | reconfigurability | 321 | 328 | preserved |
| 080 | recoverability | 346 | 343 | preserved |
| 082 | repeatability | 294 | 314 | preserved |
| 083 | replaceability | 210 | 234 | preserved |
| 084 | replicability | 295 | 330 | preserved |
| 085 | reusability | 280 | 310 | preserved |
| 086 | robustness | 340 | 348 | preserved |
| 088 | scalability | 342 | 346 | preserved |
| 090 | self-descriptiveness | 321 | 350 | preserved |
| 091 | simplicity | 296 | 330 | preserved |
| 093 | standardizability-standardization-standard | 221 | 251 | preserved |
| 095 | suitability | 310 | 280 | preserved |
| 096 | supportability | 321 | 329 | preserved |
| 097 | survivability | 349 | 348 | preserved |
| 099 | sustainability | 328 | 337 | preserved |
| 100 | tailorability | 347 | 346 | preserved |
| 101 | testability | 295 | 302 | preserved |
| 104 | transferability | 319 | 349 | preserved |
| 106 | understandability | 297 | 333 | preserved |
| 108 | usability | 285 | 317 | preserved |
| 109 | variability | 293 | 310 | preserved |
| 110 | verifiability | 320 | 322 | preserved |
| 111 | versatility | 305 | 318 | preserved |
| 112 | viability | 309 | 345 | preserved |
| 114 | wrappability | 325 | 297 | preserved |

## Validation findings

- Repository validator: all 114 skills checked with zero errors.
- The ordinary full unittest run passed 33 tests and hit one environment error: the managed Windows token could not write or clean a TemporaryDirectory fixture. Relocating that standard temporary directory into the workspace did not resolve its permission behavior.
- The same full suite passed all 34 tests when the test process used a compatibility temporary-directory factory that creates unique directories within the writable workspace with inherited permissions. Test files, assertions, scorer code and skill validator code were unchanged.
- The supplemental Skill Creator checker passed 67 of 69 edited skills. It rejects pre-existing status frontmatter in availability and readability. Those fields were confirmed in the starting commit and retained because only description edits were authorized.
- Preservation checks passed for all bodies, all non-description frontmatter and every original boundary clause. All 114 descriptions have valid pointers and three to five quoted triggers; none share an exact normalized quoted trigger.

## Uncertain judgments and remaining weaknesses

- Several remaining misses already state a plausible routing unit: The export feature is missing selects functionality; Our service needs better uptime selects availability; Use the validator in the CLI too selects reusability. Their key still demands ask. No label adjudication was applied.
- Descriptions cannot guarantee ask for every short request without sometimes confusing missing implementation detail with missing routing information. Remaining misses have not been hidden by redefining those skills or changing their keys.
- Four newly failing controls select descriptions that were deliberately unchanged. These observations do not establish that their descriptions regressed; the evaluation mode and model sampling also differ.
- This is a targeted revision check over previously observed failures and selected siblings, not an independent holdout evaluation or a full-catalogue rerun. Candidate coverage is 114; prompt coverage is the 268 selected cases only.
- The final report does not claim that all 94 misses are fixed. The 58 original misses and five control failures remain visible for human review.

Evidence: evals/routing-fixes/selection.json, baseline-score.json, round-1-score.json, score.json, run.json, validation.json and the preserved raw result files. Final results: routing-fixes-results.json.
