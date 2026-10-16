# Blinded routing findings

Fresh Codex CLI session: 01a14599-513d-74a2-ac72-344065c0b3a2.

The router received the 114-skill catalogue and 490 unique prompts only, with the neutral router instructions. It received no answer key, original labeled evals, audit findings, expected distribution, or parent conversation. The successful session made no tool calls. The CLI default model was used; its model name was not reported in the JSONL events.

Preparation commit: bc5c71616a796f60bf7beb808e9deee18c64cc51.

An earlier fresh session could not read the files because CLI policy blocked its file-reading commands. It returned no routing answers and was not scored. The successful fresh session received the same blinded files inline on stdin; read-only permissions were retained.

## Scores against the frozen key

Scoring command: python scripts/score_routing.py routing-results.json

| Group | Correct | Total | Accuracy | Missing |
| --- | ---: | ---: | ---: | ---: |
| explicit | 242 | 242 | 100.00% | 0 |
| vague | 147 | 240 | 61.25% | 0 |
| user_voice | 7 | 8 | 87.50% | 0 |

Total misses: 94. All 490 ids were answered exactly once using a valid catalogue slug or ask. The raw answer bytes were copied unchanged into routing-results.json.

These are misses against the existing key, not adjudicated description defects. The vague labels include cases questioned in the preceding audit. Descriptions, skill bodies, original evals, and their labels are unchanged. No miss has been reclassified.

## User-voice misses

| Id | Prompt | Router choice | Expected acceptable choices |
| --- | --- | --- | --- |
| r-dc35686fd9e8cf9f | Let customers plug in their own report formats without touching core code. | ask | extensibility |

## Explicit misses

None.

## Vague misses

The key expects ask for every row below. The router instead selected the listed skill.

| Id | Prompt | Router choice | Source eval cases |
| --- | --- | --- | --- |
| r-09b28c71fc1887dc | Handle more traffic. | scalability | 038-distributivity:near_miss[1] |
| r-0d6c45b5898145ff | Both changes help alone but not together. | additivity | 022-composability:near_miss[2] |
| r-10fa474e5e2b4e6c | Completion feels unpredictable. | predictability | 074-predictability:should_trigger[1]; 092-stability:near_miss[1] |
| r-11a7978c48245818 | Check whether this follows the rules. | conformance | 028-conformance:should_trigger[1]; 093-standardizability-standardization-standard:near_miss[1] |
| r-136e0a1f295bde94 | Help me debug this failure. | debuggability | 009-analyzability:near_miss[1]; 033-debuggability:should_trigger[1] |
| r-1d3450cfae00e2ec | Make this easier to look after. | maintainability | 063-maintainability:should_trigger[1]; 068-modifiability:near_miss[1]; 096-supportability:near_miss[1] |
| r-1d8c5d5257e59ead | We need a better audit trail. | auditability | 002-accountability:near_miss[1]; 013-auditability:should_trigger[1]; 102-traceability:near_miss[1] |
| r-212433c508cb6344 | Use the validator in the CLI too. | reusability | 085-reusability:should_trigger[2]; 111-versatility:near_miss[2] |
| r-25efb477bee0fd0a | We need different editions. | variability | 109-variability:should_trigger[1] |
| r-27ab27a7e5e93872 | Handle more users. | scalability | 044-expandability:near_miss[1]; 088-scalability:should_trigger[1] |
| r-2820e20b462b3c0d | Stop copying this helper. | reusability | 053-generality:near_miss[1]; 085-reusability:should_trigger[1] |
| r-290e28507504f2f8 | The recipient can't use the package. | transferability | 104-transferability:should_trigger[2] |
| r-2a15293fe4223b00 | Stop adding a special case for every input. | generality | 053-generality:should_trigger[1]; 085-reusability:near_miss[1]; 111-versatility:near_miss[1] |
| r-2a223324cbf197c0 | Another engineer gets a different answer. | replicability | 084-replicability:should_trigger[2] |
| r-2eec4750902942a8 | Should we keep this product? | viability | 007-affordability:near_miss[2]; 049-feasibility:near_miss[2]; 112-viability:should_trigger[2] |
| r-354eada869c66e98 | Can we call this confirmed? | certainty | 016-certainty:should_trigger[1] |
| r-37eb69ec9d791f9d | Make checkout easier. | usability | 001-accessibility-access-control:near_miss[1]; 108-usability:should_trigger[1] |
| r-3caae219ae15a22e | Does this pass on a rerun? | repeatability | 036-demonstrability:near_miss[2]; 082-repeatability:should_trigger[2] |
| r-3e20a3b68eff4295 | People do not enjoy this. | likeability | 061-likeability:should_trigger[2]; 105-trustability:near_miss[2]; 108-usability:near_miss[2] |
| r-40c0859ae907228b | Will this design work here? | feasibility | 049-feasibility:should_trigger[2] |
| r-43071ab7a17cb5f6 | This rule language can't say what we need. | expressiveness | 045-expressiveness:should_trigger[1] |
| r-454ecee0a31f2d9b | It only runs on the old machine. | portability | 067-mobility:near_miss[2]; 073-portability:should_trigger[2]; 084-replicability:near_miss[2] |
| r-4712a66798dbd10d | The page feels uninviting. | attractiveness | 012-attractiveness:should_trigger[2]; 060-legibility:near_miss[2] |
| r-473db3456a90cbc0 | Keep people informed. | communicativeness | 018-communicativeness:should_trigger[1]; 090-self-descriptiveness:near_miss[1] |
| r-4bc32bb365518dff | Stop overload breaking the worker. | robustness | 048-fault-failure-tolerance:near_miss[2]; 054-immunity:near_miss[2]; 086-robustness:should_trigger[2]; 087-safety:near_miss[2]; 098-susceptibility:near_miss[2] |
| r-50cd37978f2a9caf | Which worker owns this job? | distributivity | 038-distributivity:should_trigger[2] |
| r-5174f6e026d7200e | We need to stop using the old provider. | replaceability | 019-compatibility:near_miss[2]; 083-replaceability:should_trigger[2] |
| r-526b3ad54e859b5a | Our service needs better uptime. | availability | 015-availability:should_trigger[2] |
| r-52c0dc8b3ab03d92 | Help us wire these services together. | integratability | 022-composability:near_miss[1]; 056-integratability:should_trigger[1]; 058-interoperability:near_miss[1] |
| r-53bb9c6161763cce | Make this dataset less identifying. | anonymity | 010-anonymity:should_trigger[1] |
| r-544e2a4c3a959b68 | Fit this tool to our team. | tailorability | 100-tailorability:should_trigger[1] |
| r-56677163d27567d6 | Help us hand this project over. | transferability | 104-transferability:should_trigger[1] |
| r-58be2272a38abc93 | Who was behind this change? | accountability | 002-accountability:should_trigger[1]; 013-auditability:near_miss[1] |
| r-591489b007912170 | Let admins tweak this. | adjustability | 006-adjustability:should_trigger[1]; 027-configurability:near_miss[1] |
| r-5929e4dc4b473e3c | Make this configurable. | configurability | 006-adjustability:near_miss[1]; 027-configurability:should_trigger[1]; 032-customizability:near_miss[1]; 079-reconfigurability:near_miss[1]; 109-variability:near_miss[1] |
| r-5c2b9641f0aa635c | The report sounds too sure. | certainty | 003-accuracy:near_miss[2]; 016-certainty:should_trigger[2] |
| r-5d6985e8f00a2ac7 | We need to support cancellation. | functionality | 052-functionality:should_trigger[2] |
| r-625806728696d50b | Do not lose service when things break. | fault-failure-tolerance | 048-fault-failure-tolerance:should_trigger[2]; 097-survivability:near_miss[2] |
| r-65962c0fc744f0cf | Help us with a customer issue. | supportability | 096-supportability:should_trigger[1] |
| r-668347a0cdc41cb3 | We can't reproduce the timeout in tests. | testability | 033-debuggability:near_miss[2]; 101-testability:should_trigger[2] |
| r-67191eb0ee8982c0 | The new install won't start. | installability | 055-installability:should_trigger[1]; 073-portability:near_miss[1] |
| r-6753b4b72a1bf7aa | Do these optimizations work well together? | additivity | 005-additivity:should_trigger[1] |
| r-677ac388c80fc716 | Is the old version proven enough? | maturity | 065-maturity:should_trigger[2] |
| r-68251e946af55326 | Split this module up. | decomposability | 034-decomposability:should_trigger[1]; 094-structuredness:near_miss[1] |
| r-68c83d508f9634a9 | People misread these IDs. | legibility | 062-localizability:near_miss[2] |
| r-6fa5f18f3c835424 | Can we combine these improvements? | additivity | 005-additivity:should_trigger[2] |
| r-76bb5405eadfabb3 | Teams keep inventing their own names. | standardizability-standardization-standard | 093-standardizability-standardization-standard:should_trigger[2] |
| r-779c30432ea37800 | We need a demo for the reviewers. | demonstrability | 036-demonstrability:should_trigger[2] |
| r-7998f646cf36b5db | The export is missing something. | completeness | 020-completeness:should_trigger[1] |
| r-79e7379966bc813d | This function returns the wrong result. | correctness | 003-accuracy:near_miss[1]; 020-completeness:near_miss[1]; 031-correctness:should_trigger[1]; 052-functionality:near_miss[1] |
| r-7a4eb6ae6c5efa60 | We need one shared format. | standardizability-standardization-standard | 028-conformance:near_miss[1]; 093-standardizability-standardization-standard:should_trigger[1]; 107-uniformity:near_miss[1] |
| r-7bd98ba2ba8e01c5 | Show why this requirement passed. | verifiability | 102-traceability:should_trigger[1] |
| r-7fe916099edff214 | Stop these surprise pauses. | predictability | 072-performance-efficiency-time-or-space-bounds:near_miss[2]; 074-predictability:should_trigger[2] |
| r-808d30d85b9c52d6 | The export isn't useful for our handoff. | suitability | 040-effectiveness:near_miss[2]; 052-functionality:near_miss[2]; 095-suitability:should_trigger[2] |
| r-8482677b2640a033 | Is the worker stuck? | observability | 009-analyzability:near_miss[2]; 070-observability:should_trigger[2] |
| r-8603efdd7d009787 | This feature doesn't fit our workflow. | suitability | 095-suitability:should_trigger[1] |
| r-8b076602fa74b927 | Move this service to the new host. | portability | 055-installability:near_miss[1]; 062-localizability:near_miss[1]; 073-portability:should_trigger[1]; 104-transferability:near_miss[1] |
| r-8bfd522e94801264 | Make these rules precise. | formality | 045-expressiveness:near_miss[1]; 051-formality:should_trigger[1] |
| r-90a885445e668703 | Changing config loses work. | reconfigurability | 109-variability:near_miss[2] |
| r-91964c7b1654e2f3 | Let departments work differently. | tailorability | 032-customizability:near_miss[2]; 100-tailorability:should_trigger[2] |
| r-94e3d0d51dd15ca6 | Make this code easier to read. | readability | 023-comprehensibility:near_miss[1]; 025-conciseness:near_miss[1]; 060-legibility:near_miss[1]; 078-readability:should_trigger[1] |
| r-97d13e456376587b | Can we prove this can't happen? | provability | 051-formality:near_miss[1]; 076-provability:should_trigger[1] |
| r-9bc5df77b7002ca8 | Make the screen explain itself. | self-descriptiveness | 018-communicativeness:near_miss[1]; 090-self-descriptiveness:should_trigger[1] |
| r-9d5130866c3f7b13 | Can we afford this export? | affordability | 007-affordability:should_trigger[1]; 049-feasibility:near_miss[1] |
| r-b26b3e06a3869d22 | We need to use it beyond imports. | versatility | 053-generality:near_miss[2]; 111-versatility:should_trigger[2] |
| r-b4f2c7711d799a00 | Make this service greener. | sustainability | 099-sustainability:should_trigger[1] |
| r-bf22552eb7865121 | We can't check this requirement. | verifiability | 066-measurability:near_miss[2]; 110-verifiability:should_trigger[2] |
| r-c767a2d18ade0424 | Tell us who did this. | accountability | 002-accountability:should_trigger[2]; 102-traceability:near_miss[2] |
| r-cbbab0547d8fcff7 | Can this tool do another job? | versatility | 111-versatility:should_trigger[1] |
| r-cdb119bd268c8ba9 | The receiver doesn't understand our export. | interoperability | 019-compatibility:near_miss[1]; 056-integratability:near_miss[1]; 058-interoperability:should_trigger[1] |
| r-cfa11658661e7b94 | On-call can't finish the job. | operability | 030-controllability:near_miss[1]; 071-operability:should_trigger[1] |
| r-d13d56649866b943 | What exactly are we counting? | measurability | 066-measurability:should_trigger[1] |
| r-d3dc202ad6acb822 | We need better fleet controls. | manageability | 030-controllability:near_miss[2]; 064-manageability:should_trigger[2]; 071-operability:near_miss[2] |
| r-d80e4afa0c3a60d8 | This feels overengineered. | simplicity | 021-complexity-interacting-complexity:near_miss[1]; 091-simplicity:should_trigger[1] |
| r-d8fbd88e3c5c9e47 | Can we actually build this? | feasibility | 007-affordability:near_miss[1]; 049-feasibility:should_trigger[1]; 112-viability:near_miss[1] |
| r-dd8b0409043f8049 | Where did this wrong value come from? | debuggability | 033-debuggability:should_trigger[2]; 070-observability:near_miss[2]; 101-testability:near_miss[2] |
| r-e1ef58b88335057c | How will we know this passed? | verifiability | 036-demonstrability:near_miss[1]; 076-provability:near_miss[1]; 101-testability:near_miss[1]; 110-verifiability:should_trigger[1] |
| r-e35b63c6e94e25e8 | We get stuck halfway through a rerun. | operability | 055-installability:near_miss[2]; 064-manageability:near_miss[2]; 071-operability:should_trigger[2] |
| r-e37944566e76aaf2 | Make this faster. | performance-efficiency-time-or-space-bounds | 041-efficiency-device-efficiency:near_miss[1]; 072-performance-efficiency-time-or-space-bounds:should_trigger[1]; 074-predictability:near_miss[1]; 077-quality-of-service:near_miss[1] |
| r-e491734c35b483bd | Our fixes take too much effort. | maintainability | 063-maintainability:should_trigger[2] |
| r-e5a4d18a59da6042 | Put a new API around this old function. | wrappability | 114-wrappability:should_trigger[1] |
| r-e7298d8feff7dca8 | Does this feature actually help? | effectiveness | 040-effectiveness:should_trigger[1] |
| r-e7f93ec80c7a461b | Is this still worth running? | viability | 112-viability:should_trigger[1] |
| r-e906f9ac93ac06df | Make the system easier to understand. | understandability | 023-comprehensibility:near_miss[2]; 024-comprehensiveness:near_miss[2]; 106-understandability:should_trigger[2] |
| r-ebe06c04252d4ce8 | The export feature is missing. | functionality | 040-effectiveness:near_miss[1]; 052-functionality:should_trigger[1]; 095-suitability:near_miss[1] |
| r-f02044e5b76544fb | Swap this backend. | replaceability | 083-replaceability:should_trigger[1]; 114-wrappability:near_miss[1] |
| r-f0ea1a4c1fd6cc90 | Make this explanation clearer. | comprehensibility | 051-formality:near_miss[2] |
| r-f5104ee00e36ed63 | Get the service back. | recoverability | 048-fault-failure-tolerance:near_miss[1]; 080-recoverability:should_trigger[1]; 097-survivability:near_miss[1] |
| r-f6f5291508e402a3 | Sometimes this call is much slower. | predictability | 082-repeatability:near_miss[2] |
| r-f840b615d41cf571 | Can we upgrade this algorithm? | enhanceability | 042-enhanceability:should_trigger[2]; 043-evolvability:near_miss[2] |
| r-f9b80679850c9047 | Keep us working through a disaster. | survivability | 097-survivability:should_trigger[1] |
| r-fa4d7c768527ffb7 | Our tail latency needs work. | performance-efficiency-time-or-space-bounds | 072-performance-efficiency-time-or-space-bounds:should_trigger[2]; 088-scalability:near_miss[2] |
| r-fe27712e62d948ec | Spread this work across nodes. | distributivity | 038-distributivity:should_trigger[1] |

## Vague misses grouped by router choice

| Router choice | Misses |
| --- | ---: |
| accountability | 2 |
| additivity | 3 |
| adjustability | 1 |
| affordability | 1 |
| anonymity | 1 |
| attractiveness | 1 |
| auditability | 1 |
| availability | 1 |
| certainty | 2 |
| communicativeness | 1 |
| completeness | 1 |
| comprehensibility | 1 |
| configurability | 1 |
| conformance | 1 |
| correctness | 1 |
| debuggability | 2 |
| decomposability | 1 |
| demonstrability | 1 |
| distributivity | 2 |
| effectiveness | 1 |
| enhanceability | 1 |
| expressiveness | 1 |
| fault-failure-tolerance | 1 |
| feasibility | 2 |
| formality | 1 |
| functionality | 2 |
| generality | 1 |
| installability | 1 |
| integratability | 1 |
| interoperability | 1 |
| legibility | 1 |
| likeability | 1 |
| maintainability | 2 |
| manageability | 1 |
| maturity | 1 |
| measurability | 1 |
| observability | 1 |
| operability | 2 |
| performance-efficiency-time-or-space-bounds | 2 |
| portability | 2 |
| predictability | 3 |
| provability | 1 |
| readability | 1 |
| reconfigurability | 1 |
| recoverability | 1 |
| repeatability | 1 |
| replaceability | 2 |
| replicability | 1 |
| reusability | 2 |
| robustness | 1 |
| scalability | 2 |
| self-descriptiveness | 1 |
| simplicity | 1 |
| standardizability-standardization-standard | 2 |
| suitability | 2 |
| supportability | 1 |
| survivability | 1 |
| sustainability | 1 |
| tailorability | 2 |
| testability | 1 |
| transferability | 2 |
| understandability | 1 |
| usability | 1 |
| variability | 1 |
| verifiability | 3 |
| versatility | 2 |
| viability | 2 |
| wrappability | 1 |

## Evidence and limits

- routing-results.json preserves the fresh router output. evals/routing-session.jsonl preserves its event transcript; evals/routing-run.json records input hashes, session id, CLI version, prompt prefix, no-tool-call check, and usage.
- reviews/routing-score.json contains the scorer output. The tables above join every miss to its exact prompt; original eval source indices are one-based.
- This is one routing run against repository-authored prompts and the current descriptions. It is not a general estimate of routing performance.
- No holdout split, repeat run, model comparison, or description rewrite was performed. One completed set of routing answers was evaluated; the earlier blocked attempt supplied no answers.
