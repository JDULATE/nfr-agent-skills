# Phase 5 full-catalogue findings

## Coverage and preservation

- All 114 catalogue skills are authored (draft); none remain todo.
- Added 51 missing eval files; the 63 existing skill eval files are unchanged.
- Each of the 114 files contains four should-trigger cases and four near-miss cases with real sibling slugs.
- The full run covers 912 prompts: 456 state the distinguishing fact and 456 omit it. Each new file contains four of each.
- Fact-omitted cases retain the existing clarify policy: their named skill is a provisional lead, not an unconditional correct route.
- Skill bodies are unchanged. The edited files passed body-byte hash checks against the starting snapshot; the other skill files match the starting commit. Catalogue, index, shared references, scripts, tests, and blinded routing assets are unchanged.

New eval ids: 003, 007, 009, 016, 019, 020, 021, 022, 028, 029, 030, 031, 033, 034, 036, 038, 040, 045, 049, 051, 052, 053, 055, 056, 058, 062, 064, 066, 067, 069, 070, 071, 073, 076, 082, 083, 084, 085, 091, 093, 094, 095, 101, 104, 107, 109, 110, 111, 112, 113, 114.

## Description findings

- All 114 starting descriptions already met the 350-character limit. Fifteen descriptions were revised for plainer wording or a more accurate exclusion; 99 compliant descriptions were retained.
- Every final description contains three to five quoted developer phrases, a when/use signal, and a Not for clause pointing to real catalogue slugs.
- No normalized exact quoted trigger phrase is shared by any two descriptions, including nearest siblings. This exact-phrase check does not establish semantic separation.
- Auditability now excludes checking selected rules through conformance; the former wording could imply that conformance produces a compliance conclusion.
- The revisions retain every existing sibling pointer. No boundary was removed to fit the length limit. Enhanceability still separates output-error assessment, supporting functions, and successive changes; immunity still limits its exclusion claim to assumptions.
- Short phrases about another engineer, another workflow, or a changed feed can still fit adjacent concerns without context. These remain clarification cases rather than evidence that vocabulary alone selects a skill.

Lengths count the parsed description, including spaces and punctuation, without YAML markup.

| Id | Slug | Before | After | Result |
| --- | --- | ---: | ---: | --- |
| 001 | accessibility-access-control | 334 | 334 | retained |
| 002 | accountability | 300 | 300 | retained |
| 003 | accuracy | 264 | 249 | revised |
| 004 | adaptability | 328 | 318 | revised |
| 005 | additivity | 261 | 261 | retained |
| 006 | adjustability | 257 | 257 | retained |
| 007 | affordability | 256 | 256 | retained |
| 008 | agility | 260 | 260 | retained |
| 009 | analyzability | 278 | 278 | retained |
| 010 | anonymity | 324 | 324 | retained |
| 011 | atomicity | 314 | 314 | retained |
| 012 | attractiveness | 267 | 267 | retained |
| 013 | auditability | 312 | 306 | revised |
| 014 | augmentability | 293 | 293 | retained |
| 015 | availability | 252 | 252 | retained |
| 016 | certainty | 224 | 224 | retained |
| 017 | changeability | 277 | 277 | retained |
| 018 | communicativeness | 289 | 289 | retained |
| 019 | compatibility | 201 | 201 | retained |
| 020 | completeness | 248 | 248 | retained |
| 021 | complexity-interacting-complexity | 258 | 258 | retained |
| 022 | composability | 256 | 256 | retained |
| 023 | comprehensibility | 306 | 306 | retained |
| 024 | comprehensiveness | 297 | 297 | retained |
| 025 | conciseness | 295 | 295 | retained |
| 026 | confidentiality | 287 | 287 | retained |
| 027 | configurability | 311 | 311 | retained |
| 028 | conformance | 239 | 239 | retained |
| 029 | consistency | 246 | 246 | retained |
| 030 | controllability | 301 | 301 | retained |
| 031 | correctness | 309 | 309 | retained |
| 032 | customizability | 301 | 301 | retained |
| 033 | debuggability | 288 | 288 | retained |
| 034 | decomposability | 266 | 261 | revised |
| 035 | defensibility | 336 | 336 | retained |
| 036 | demonstrability | 281 | 281 | retained |
| 037 | dependability | 304 | 304 | retained |
| 038 | distributivity | 191 | 191 | retained |
| 039 | durability | 308 | 308 | retained |
| 040 | effectiveness | 275 | 275 | retained |
| 041 | efficiency-device-efficiency | 310 | 310 | retained |
| 042 | enhanceability | 347 | 314 | revised |
| 043 | evolvability | 299 | 299 | retained |
| 044 | expandability | 300 | 300 | retained |
| 045 | expressiveness | 277 | 269 | revised |
| 046 | extendability | 290 | 290 | retained |
| 047 | extensibility | 306 | 306 | retained |
| 048 | fault-failure-tolerance | 303 | 303 | retained |
| 049 | feasibility | 274 | 270 | revised |
| 050 | flexibility | 307 | 307 | retained |
| 051 | formality | 283 | 283 | retained |
| 052 | functionality | 286 | 286 | retained |
| 053 | generality | 324 | 318 | revised |
| 054 | immunity | 345 | 348 | revised |
| 055 | installability | 260 | 260 | retained |
| 056 | integratability | 206 | 206 | retained |
| 057 | integrity | 300 | 300 | retained |
| 058 | interoperability | 200 | 200 | retained |
| 059 | learnability | 294 | 294 | retained |
| 060 | legibility | 339 | 339 | retained |
| 061 | likeability | 266 | 266 | retained |
| 062 | localizability | 276 | 276 | retained |
| 063 | maintainability | 288 | 288 | retained |
| 064 | manageability | 307 | 307 | retained |
| 065 | maturity | 327 | 315 | revised |
| 066 | measurability | 280 | 280 | retained |
| 067 | mobility | 304 | 304 | retained |
| 068 | modifiability | 316 | 316 | retained |
| 069 | nomadicity | 301 | 301 | retained |
| 070 | observability | 303 | 303 | retained |
| 071 | operability | 301 | 301 | retained |
| 072 | performance-efficiency-time-or-space-bounds | 323 | 323 | retained |
| 073 | portability | 309 | 309 | retained |
| 074 | predictability | 326 | 326 | retained |
| 075 | privacy | 324 | 324 | retained |
| 076 | provability | 284 | 284 | retained |
| 077 | quality-of-service | 315 | 315 | retained |
| 078 | readability | 270 | 270 | retained |
| 079 | reconfigurability | 321 | 321 | retained |
| 080 | recoverability | 346 | 346 | retained |
| 081 | reliability | 325 | 325 | retained |
| 082 | repeatability | 294 | 294 | retained |
| 083 | replaceability | 210 | 210 | retained |
| 084 | replicability | 297 | 295 | revised |
| 085 | reusability | 280 | 280 | retained |
| 086 | robustness | 340 | 340 | retained |
| 087 | safety | 310 | 310 | retained |
| 088 | scalability | 342 | 342 | retained |
| 089 | security-control-and-security | 319 | 319 | retained |
| 090 | self-descriptiveness | 321 | 321 | retained |
| 091 | simplicity | 296 | 296 | retained |
| 092 | stability | 335 | 335 | retained |
| 093 | standardizability-standardization-standard | 221 | 221 | retained |
| 094 | structuredness | 278 | 278 | retained |
| 095 | suitability | 310 | 310 | retained |
| 096 | supportability | 321 | 321 | retained |
| 097 | survivability | 349 | 349 | retained |
| 098 | susceptibility | 335 | 335 | retained |
| 099 | sustainability | 328 | 328 | retained |
| 100 | tailorability | 347 | 347 | revised |
| 101 | testability | 295 | 295 | retained |
| 102 | traceability | 312 | 312 | retained |
| 103 | trainability | 339 | 339 | retained |
| 104 | transferability | 319 | 319 | retained |
| 105 | trustability | 331 | 331 | retained |
| 106 | understandability | 297 | 297 | retained |
| 107 | uniformity | 314 | 321 | revised |
| 108 | usability | 285 | 285 | retained |
| 109 | variability | 289 | 293 | revised |
| 110 | verifiability | 320 | 320 | retained |
| 111 | versatility | 305 | 305 | retained |
| 112 | viability | 307 | 309 | revised |
| 113 | visibility | 335 | 335 | retained |
| 114 | wrappability | 325 | 325 | retained |

## Validation findings

- python scripts/validate_skills.py: checked 114 skills, zero absent todo skills, zero errors.
- python -m unittest discover -s tests -v: 34 tests passed.
- python scripts/check_descriptions.py --json: successful full-catalogue run; all 114 skills participate as description candidates and eval owners.
- Description limits, trigger counts, sibling pointers, exact trigger uniqueness, body preservation, and existing-eval preservation passed the additional read-only checks.

## Checker findings

The checker measures Jaccard overlap of lowercase word sets. It does not interpret negation, synonyms, intent, or exclusion clauses. Warnings are heuristic observations, not measured routing accuracy. No description was edited in response to a checker score alone.

| Finding | Cases flagged |
| --- | ---: |
| expected_not_top | 438 |
| near_pair_no_signal | 78 |
| near_pair_tie | 9 |
| near_target_outranks_sibling | 41 |
| no_keyword_signal | 28 |
| top_tie | 48 |

Flags can overlap on the same case. Expected-not-top and top-tie findings compare against all descriptions; near-target findings compare the eval owner with its intended sibling. A no-signal pair is not evidence that the two skills are semantically equivalent.

The following table lists every pair emitted by the full checker, including ties, no-signal sibling comparisons, and unexpected competitors. Pair order and counts are taken directly from its output. Case indices are one-based.

| Flagged pair | Findings and counts | Case ids |
| --- | --- | --- |
| extendability / extensibility | expected_not_top=2; near_pair_no_signal=1; near_pair_tie=2; near_target_outranks_sibling=1; top_tie=4 | 046-extendability:near_miss[1]; 046-extendability:near_miss[3]; 046-extendability:should_trigger[3]; 047-extensibility:near_miss[1]; 047-extensibility:near_miss[3]; 047-extensibility:should_trigger[1]; 047-extensibility:should_trigger[3] |
| attractiveness / expandability | expected_not_top=6 | 005-additivity:near_miss[2]; 038-distributivity:near_miss[2]; 044-expandability:should_trigger[1]; 044-expandability:should_trigger[2]; 046-extendability:near_miss[2]; 088-scalability:near_miss[1] |
| attractiveness / likeability | expected_not_top=4; near_target_outranks_sibling=2; top_tie=2 | 012-attractiveness:near_miss[1]; 012-attractiveness:should_trigger[2]; 012-attractiveness:should_trigger[3]; 060-legibility:near_miss[2]; 061-likeability:near_miss[3]; 061-likeability:should_trigger[1] |
| controllability / robustness | expected_not_top=6 | 048-fault-failure-tolerance:near_miss[2]; 054-immunity:near_miss[2]; 086-robustness:should_trigger[2]; 086-robustness:should_trigger[3]; 087-safety:near_miss[2]; 098-susceptibility:near_miss[2] |
| likeability / usability | expected_not_top=5; near_target_outranks_sibling=2 | 012-attractiveness:near_miss[3]; 059-learnability:near_miss[2]; 061-likeability:near_miss[2]; 061-likeability:near_miss[4]; 061-likeability:should_trigger[3]; 108-usability:should_trigger[2] |
| observability / recoverability | expected_not_top=6 | 011-atomicity:near_miss[4]; 015-availability:near_miss[4]; 035-defensibility:near_miss[4]; 039-durability:near_miss[4]; 080-recoverability:should_trigger[4]; 081-reliability:near_miss[4] |
| recoverability / sustainability | expected_not_top=6 | 011-atomicity:near_miss[2]; 015-availability:near_miss[2]; 035-defensibility:near_miss[2]; 039-durability:near_miss[2]; 080-recoverability:should_trigger[2]; 081-reliability:near_miss[2] |
| availability / recoverability | expected_not_top=3; near_pair_no_signal=1; near_target_outranks_sibling=1 | 015-availability:near_miss[2]; 015-availability:near_miss[4]; 048-fault-failure-tolerance:near_miss[1]; 080-recoverability:should_trigger[1]; 097-survivability:near_miss[1] |
| changeability / modifiability | expected_not_top=3; near_pair_no_signal=2; near_target_outranks_sibling=1 | 008-agility:near_miss[4]; 017-changeability:near_miss[2]; 017-changeability:near_miss[4]; 068-modifiability:near_miss[2]; 068-modifiability:should_trigger[4] |
| completeness / functionality | expected_not_top=5 | 020-completeness:should_trigger[4]; 031-correctness:near_miss[4]; 040-effectiveness:near_miss[1]; 052-functionality:should_trigger[1]; 095-suitability:near_miss[1] |
| confidentiality / privacy | expected_not_top=4; near_target_outranks_sibling=2 | 026-confidentiality:near_miss[1]; 026-confidentiality:should_trigger[1]; 057-integrity:near_miss[1]; 075-privacy:near_miss[1]; 089-security-control-and-security:near_miss[1] |
| controllability / scalability | top_tie=5 | 048-fault-failure-tolerance:near_miss[2]; 054-immunity:near_miss[2]; 086-robustness:should_trigger[2]; 087-safety:near_miss[2]; 098-susceptibility:near_miss[2] |
| maintainability / supportability | expected_not_top=3; near_pair_no_signal=2; near_target_outranks_sibling=1 | 063-maintainability:near_miss[2]; 063-maintainability:should_trigger[3]; 068-modifiability:near_miss[3]; 096-supportability:near_miss[1]; 096-supportability:near_miss[3] |
| performance-efficiency-time-or-space-bounds / scalability | expected_not_top=4; near_pair_no_signal=1 | 041-efficiency-device-efficiency:near_miss[3]; 072-performance-efficiency-time-or-space-bounds:should_trigger[3]; 074-predictability:near_miss[3]; 077-quality-of-service:near_miss[3]; 088-scalability:near_miss[2] |
| portability / reconfigurability | expected_not_top=5 | 004-adaptability:near_miss[2]; 006-adjustability:near_miss[2]; 027-configurability:near_miss[2]; 050-flexibility:near_miss[2]; 079-reconfigurability:should_trigger[2] |
| robustness / scalability | expected_not_top=5 | 048-fault-failure-tolerance:near_miss[2]; 054-immunity:near_miss[2]; 086-robustness:should_trigger[2]; 087-safety:near_miss[2]; 098-susceptibility:near_miss[2] |
| agility / readability | expected_not_top=4 | 023-comprehensibility:near_miss[1]; 025-conciseness:near_miss[1]; 060-legibility:near_miss[1]; 078-readability:should_trigger[1] |
| attractiveness / reliability | expected_not_top=4 | 015-availability:near_miss[1]; 037-dependability:near_miss[1]; 065-maturity:near_miss[1]; 081-reliability:should_trigger[1] |
| composability / integratability | expected_not_top=4 | 022-composability:should_trigger[1]; 022-composability:should_trigger[2]; 034-decomposability:near_miss[2]; 085-reusability:near_miss[2] |
| comprehensiveness / maturity | expected_not_top=4 | 024-comprehensiveness:should_trigger[2]; 025-conciseness:near_miss[2]; 103-trainability:near_miss[2]; 106-understandability:near_miss[2] |
| effectiveness / suitability | expected_not_top=3; near_pair_no_signal=1; near_target_outranks_sibling=1 | 040-effectiveness:near_miss[4]; 052-functionality:near_miss[4]; 095-suitability:near_miss[2]; 095-suitability:should_trigger[4] |
| efficiency-device-efficiency / sustainability | expected_not_top=2; near_pair_no_signal=1; near_target_outranks_sibling=2 | 041-efficiency-device-efficiency:should_trigger[4]; 099-sustainability:near_miss[1]; 099-sustainability:near_miss[2]; 099-sustainability:near_miss[4] |
| recoverability / reliability | expected_not_top=3; near_pair_no_signal=1 | 048-fault-failure-tolerance:near_miss[3]; 080-recoverability:should_trigger[3]; 081-reliability:near_miss[2]; 097-survivability:near_miss[3] |
| reliability / robustness | expected_not_top=4 | 015-availability:near_miss[3]; 037-dependability:near_miss[3]; 065-maturity:near_miss[3]; 081-reliability:should_trigger[3] |
| accountability / observability | expected_not_top=3 | 066-measurability:near_miss[3]; 070-observability:should_trigger[3]; 113-visibility:near_miss[3] |
| accountability / traceability | near_pair_no_signal=2; near_target_outranks_sibling=1 | 002-accountability:near_miss[2]; 102-traceability:near_miss[2]; 102-traceability:near_miss[4] |
| adaptability / integratability | expected_not_top=3 | 004-adaptability:should_trigger[1]; 004-adaptability:should_trigger[2]; 050-flexibility:near_miss[1] |
| adaptability / modifiability | expected_not_top=3 | 008-agility:near_miss[2]; 017-changeability:near_miss[2]; 068-modifiability:should_trigger[2] |
| additivity / efficiency-device-efficiency | expected_not_top=3 | 041-efficiency-device-efficiency:should_trigger[1]; 072-performance-efficiency-time-or-space-bounds:near_miss[1]; 099-sustainability:near_miss[1] |
| additivity / extendability | top_tie=3 | 041-efficiency-device-efficiency:should_trigger[1]; 072-performance-efficiency-time-or-space-bounds:near_miss[1]; 099-sustainability:near_miss[1] |
| adjustability / analyzability | top_tie=3 | 002-accountability:should_trigger[1]; 009-analyzability:should_trigger[2]; 013-auditability:near_miss[1] |
| agility / traceability | expected_not_top=3 | 002-accountability:near_miss[2]; 013-auditability:near_miss[2]; 102-traceability:should_trigger[2] |
| anonymity / likeability | expected_not_top=3 | 010-anonymity:should_trigger[2]; 026-confidentiality:near_miss[2]; 075-privacy:near_miss[2] |
| attractiveness / manageability | expected_not_top=3 | 030-controllability:near_miss[2]; 064-manageability:should_trigger[2]; 071-operability:near_miss[2] |
| attractiveness / robustness | expected_not_top=3 | 012-attractiveness:should_trigger[4]; 060-legibility:near_miss[4]; 086-robustness:should_trigger[1] |
| augmentability / enhanceability | near_pair_tie=1; top_tie=2 | 014-augmentability:near_miss[3]; 042-enhanceability:should_trigger[4]; 043-evolvability:near_miss[4] |
| augmentability / interoperability | expected_not_top=3 | 005-additivity:near_miss[1]; 014-augmentability:should_trigger[1]; 042-enhanceability:near_miss[1] |
| certainty / controllability | expected_not_top=3 | 030-controllability:should_trigger[1]; 064-manageability:near_miss[1]; 071-operability:near_miss[1] |
| certainty / portability | expected_not_top=3 | 067-mobility:near_miss[4]; 073-portability:should_trigger[4]; 084-replicability:near_miss[4] |
| changeability / feasibility | expected_not_top=3 | 017-changeability:should_trigger[2]; 068-modifiability:near_miss[2]; 096-supportability:near_miss[2] |
| communicativeness / likeability | expected_not_top=3 | 018-communicativeness:should_trigger[2]; 018-communicativeness:should_trigger[4]; 113-visibility:near_miss[2] |
| communicativeness / observability | top_tie=3 | 055-installability:near_miss[4]; 064-manageability:near_miss[4]; 071-operability:should_trigger[4] |
| communicativeness / operability | expected_not_top=3 | 055-installability:near_miss[4]; 064-manageability:near_miss[4]; 071-operability:should_trigger[4] |
| composability / usability | expected_not_top=3 | 022-composability:should_trigger[4]; 034-decomposability:near_miss[4]; 085-reusability:near_miss[4] |
| comprehensibility / learnability | expected_not_top=3 | 023-comprehensibility:should_trigger[1]; 024-comprehensiveness:near_miss[1]; 106-understandability:near_miss[1] |
| comprehensibility / traceability | expected_not_top=3 | 023-comprehensibility:should_trigger[3]; 024-comprehensiveness:near_miss[3]; 106-understandability:near_miss[3] |
| conciseness / legibility | expected_not_top=3 | 012-attractiveness:near_miss[4]; 060-legibility:should_trigger[4]; 062-localizability:near_miss[4] |
| confidentiality / customizability | expected_not_top=3 | 001-accessibility-access-control:near_miss[2]; 010-anonymity:near_miss[2]; 026-confidentiality:should_trigger[2] |
| confidentiality / transferability | expected_not_top=3 | 001-accessibility-access-control:near_miss[4]; 010-anonymity:near_miss[4]; 026-confidentiality:should_trigger[4] |
| configurability / customizability | expected_not_top=2; near_pair_no_signal=1 | 027-configurability:should_trigger[2]; 032-customizability:near_miss[1]; 100-tailorability:near_miss[2] |
| conformance / integrity | expected_not_top=3 | 028-conformance:should_trigger[1]; 029-consistency:near_miss[4]; 093-standardizability-standardization-standard:near_miss[1] |
| durability / recoverability | near_pair_no_signal=2; near_target_outranks_sibling=1 | 039-durability:near_miss[2]; 039-durability:near_miss[4]; 080-recoverability:near_miss[2] |
| effectiveness / usability | expected_not_top=3 | 059-learnability:near_miss[4]; 061-likeability:near_miss[4]; 108-usability:should_trigger[4] |
| efficiency-device-efficiency / extendability | expected_not_top=3 | 041-efficiency-device-efficiency:should_trigger[1]; 072-performance-efficiency-time-or-space-bounds:near_miss[1]; 099-sustainability:near_miss[1] |
| efficiency-device-efficiency / uniformity | expected_not_top=3 | 093-standardizability-standardization-standard:near_miss[4]; 094-structuredness:near_miss[4]; 107-uniformity:should_trigger[4] |
| enhanceability / learnability | expected_not_top=3 | 059-learnability:should_trigger[1]; 103-trainability:near_miss[1]; 108-usability:near_miss[1] |
| evolvability / traceability | expected_not_top=3 | 002-accountability:near_miss[4]; 013-auditability:near_miss[4]; 102-traceability:should_trigger[4] |
| fault-failure-tolerance / nomadicity | expected_not_top=3 | 048-fault-failure-tolerance:should_trigger[1]; 080-recoverability:near_miss[1]; 086-robustness:near_miss[1] |
| feasibility / variability | expected_not_top=3 | 007-affordability:near_miss[1]; 049-feasibility:should_trigger[1]; 112-viability:near_miss[1] |
| installability / privacy | expected_not_top=3 | 010-anonymity:near_miss[1]; 026-confidentiality:near_miss[1]; 075-privacy:should_trigger[1] |
| learnability / operability | top_tie=3 | 055-installability:near_miss[2]; 064-manageability:near_miss[2]; 071-operability:should_trigger[2] |
| maintainability / usability | expected_not_top=3 | 063-maintainability:should_trigger[1]; 068-modifiability:near_miss[1]; 096-supportability:near_miss[1] |
| modifiability / usability | expected_not_top=3 | 043-evolvability:near_miss[1]; 063-maintainability:near_miss[1]; 068-modifiability:should_trigger[1] |
| observability / operability | expected_not_top=3 | 055-installability:near_miss[4]; 064-manageability:near_miss[4]; 071-operability:should_trigger[4] |
| portability / replaceability | expected_not_top=3 | 067-mobility:near_miss[2]; 073-portability:should_trigger[2]; 084-replicability:near_miss[2] |
| predictability / viability | expected_not_top=3 | 007-affordability:near_miss[2]; 049-feasibility:near_miss[2]; 112-viability:should_trigger[2] |
| understandability / usability | expected_not_top=3 | 023-comprehensibility:near_miss[2]; 024-comprehensiveness:near_miss[2]; 106-understandability:should_trigger[2] |
| accessibility-access-control / confidentiality | expected_not_top=1; near_pair_no_signal=1 | 001-accessibility-access-control:near_miss[2]; 001-accessibility-access-control:should_trigger[4] |
| accessibility-access-control / usability | expected_not_top=2 | 001-accessibility-access-control:should_trigger[2]; 001-accessibility-access-control:should_trigger[3] |
| accountability / adjustability | expected_not_top=2 | 002-accountability:should_trigger[1]; 013-auditability:near_miss[1] |
| accountability / analyzability | expected_not_top=2 | 002-accountability:should_trigger[1]; 013-auditability:near_miss[1] |
| accountability / augmentability | expected_not_top=2 | 002-accountability:should_trigger[3]; 013-auditability:near_miss[3] |
| accountability / composability | expected_not_top=2 | 002-accountability:should_trigger[4]; 102-traceability:near_miss[4] |
| accountability / durability | expected_not_top=2 | 002-accountability:should_trigger[2]; 102-traceability:near_miss[2] |
| accuracy / atomicity | expected_not_top=2 | 011-atomicity:should_trigger[2]; 057-integrity:near_miss[2] |
| accuracy / attractiveness | top_tie=2 | 011-atomicity:should_trigger[2]; 057-integrity:near_miss[2] |
| accuracy / legibility | expected_not_top=2 | 012-attractiveness:near_miss[2]; 060-legibility:should_trigger[2] |
| accuracy / trustability | expected_not_top=2 | 037-dependability:near_miss[2]; 105-trustability:should_trigger[2] |
| adaptability / analyzability | expected_not_top=2 | 009-analyzability:should_trigger[1]; 033-debuggability:near_miss[1] |
| adaptability / portability | top_tie=2 | 004-adaptability:should_trigger[3]; 050-flexibility:near_miss[3] |
| additivity / installability | expected_not_top=2 | 055-installability:should_trigger[2]; 056-integratability:near_miss[2] |
| adjustability / distributivity | expected_not_top=2 | 006-adjustability:should_trigger[2]; 079-reconfigurability:near_miss[2] |
| affordability / completeness | expected_not_top=2 | 007-affordability:should_trigger[1]; 049-feasibility:near_miss[1] |
| affordability / repeatability | expected_not_top=2 | 007-affordability:should_trigger[2]; 112-viability:near_miss[2] |
| affordability / viability | near_pair_no_signal=1; near_target_outranks_sibling=1 | 007-affordability:near_miss[2]; 112-viability:near_miss[2] |
| agility / changeability | near_pair_no_signal=2 | 008-agility:near_miss[1]; 017-changeability:near_miss[1] |
| agility / modifiability | near_pair_no_signal=1; near_target_outranks_sibling=1 | 008-agility:near_miss[2]; 008-agility:near_miss[4] |
| agility / portability | expected_not_top=2 | 008-agility:should_trigger[1]; 017-changeability:near_miss[1] |
| agility / security-control-and-security | expected_not_top=2 | 086-robustness:near_miss[2]; 089-security-control-and-security:should_trigger[2] |
| analyzability / debuggability | near_pair_no_signal=2 | 009-analyzability:near_miss[1]; 033-debuggability:near_miss[1] |
| atomicity / attractiveness | expected_not_top=2 | 011-atomicity:should_trigger[2]; 057-integrity:near_miss[2] |
| atomicity / fault-failure-tolerance | expected_not_top=2 | 011-atomicity:should_trigger[1]; 039-durability:near_miss[1] |
| attractiveness / customizability | expected_not_top=2 | 032-customizability:should_trigger[2]; 047-extensibility:near_miss[2] |
| attractiveness / flexibility | expected_not_top=2 | 004-adaptability:near_miss[1]; 050-flexibility:should_trigger[1] |
| attractiveness / legibility | near_pair_no_signal=1; near_target_outranks_sibling=1 | 012-attractiveness:near_miss[2]; 060-legibility:near_miss[4] |
| attractiveness / self-descriptiveness | expected_not_top=2 | 018-communicativeness:near_miss[1]; 090-self-descriptiveness:should_trigger[1] |
| attractiveness / versatility | expected_not_top=2 | 053-generality:near_miss[4]; 111-versatility:should_trigger[4] |
| auditability / predictability | expected_not_top=2 | 074-predictability:should_trigger[3]; 092-stability:near_miss[3] |
| availability / debuggability | expected_not_top=2 | 009-analyzability:near_miss[1]; 033-debuggability:should_trigger[1] |
| availability / fault-failure-tolerance | expected_not_top=2 | 015-availability:should_trigger[1]; 081-reliability:near_miss[1] |
| certainty / conformance | expected_not_top=2 | 003-accuracy:near_miss[4]; 016-certainty:should_trigger[4] |
| certainty / formality | expected_not_top=2 | 051-formality:should_trigger[4]; 076-provability:near_miss[4] |
| certainty / integratability | expected_not_top=2 | 003-accuracy:near_miss[2]; 016-certainty:should_trigger[2] |
| certainty / predictability | expected_not_top=2 | 072-performance-efficiency-time-or-space-bounds:near_miss[2]; 074-predictability:should_trigger[2] |
| changeability / integratability | expected_not_top=2 | 008-agility:near_miss[1]; 017-changeability:should_trigger[1] |
| communicativeness / performance-efficiency-time-or-space-bounds | expected_not_top=2 | 072-performance-efficiency-time-or-space-bounds:should_trigger[4]; 088-scalability:near_miss[4] |
| communicativeness / replaceability | expected_not_top=2 | 018-communicativeness:should_trigger[1]; 090-self-descriptiveness:near_miss[1] |
| compatibility / decomposability | expected_not_top=2 | 034-decomposability:should_trigger[3]; 094-structuredness:near_miss[3] |
| compatibility / integratability | expected_not_top=2 | 019-compatibility:should_trigger[1]; 083-replaceability:near_miss[1] |
| compatibility / interoperability | top_tie=2 | 058-interoperability:should_trigger[4]; 104-transferability:near_miss[4] |
| completeness / comprehensiveness | expected_not_top=1; near_pair_no_signal=1; near_target_outranks_sibling=1 | 020-completeness:near_miss[2]; 020-completeness:near_miss[4] |
| completeness / effectiveness | expected_not_top=2 | 020-completeness:should_trigger[4]; 031-correctness:near_miss[4] |
| completeness / usability | expected_not_top=2 | 020-completeness:should_trigger[2]; 031-correctness:near_miss[2] |
| completeness / variability | expected_not_top=2 | 020-completeness:should_trigger[4]; 031-correctness:near_miss[4] |
| complexity-interacting-complexity / integratability | expected_not_top=2 | 021-complexity-interacting-complexity:should_trigger[1]; 091-simplicity:near_miss[1] |
| composability / decomposability | near_pair_no_signal=1; near_target_outranks_sibling=1 | 034-decomposability:near_miss[2]; 034-decomposability:near_miss[4] |
| comprehensibility / understandability | near_pair_tie=1; top_tie=1 | 023-comprehensibility:near_miss[2]; 051-formality:near_miss[2] |
| comprehensiveness / immunity | expected_not_top=2 | 054-immunity:should_trigger[1]; 098-susceptibility:near_miss[1] |
| comprehensiveness / simplicity | top_tie=2 | 054-immunity:should_trigger[1]; 098-susceptibility:near_miss[1] |
| comprehensiveness / understandability | near_pair_no_signal=1; near_pair_tie=1 | 024-comprehensiveness:near_miss[2]; 106-understandability:near_miss[2] |
| configurability / durability | expected_not_top=2 | 039-durability:should_trigger[4]; 080-recoverability:near_miss[4] |
| configurability / effectiveness | expected_not_top=2 | 027-configurability:should_trigger[4]; 100-tailorability:near_miss[4] |
| configurability / reconfigurability | near_pair_no_signal=2 | 027-configurability:near_miss[2]; 079-reconfigurability:near_miss[1] |
| configurability / scalability | expected_not_top=2 | 077-quality-of-service:near_miss[2]; 088-scalability:should_trigger[2] |
| configurability / structuredness | top_tie=2 | 077-quality-of-service:near_miss[2]; 088-scalability:should_trigger[2] |
| conformance / fault-failure-tolerance | expected_not_top=2 | 048-fault-failure-tolerance:should_trigger[2]; 097-survivability:near_miss[2] |
| conformance / formality | expected_not_top=2 | 045-expressiveness:near_miss[1]; 051-formality:should_trigger[1] |
| consistency / visibility | expected_not_top=2 | 029-consistency:should_trigger[2]; 107-uniformity:near_miss[2] |
| correctness / integrity | expected_not_top=2 | 057-integrity:should_trigger[2]; 089-security-control-and-security:near_miss[2] |
| correctness / usability | expected_not_top=2 | 028-conformance:near_miss[2]; 031-correctness:should_trigger[2] |
| customizability / expressiveness | expected_not_top=2 | 032-customizability:should_trigger[4]; 047-extensibility:near_miss[4] |
| demonstrability / repeatability | expected_not_top=2 | 082-repeatability:should_trigger[1]; 084-replicability:near_miss[1] |
| dependability / evolvability | top_tie=2 | 037-dependability:should_trigger[1]; 105-trustability:near_miss[1] |
| dependability / maturity | expected_not_top=2; near_target_outranks_sibling=1 | 037-dependability:should_trigger[2]; 065-maturity:near_miss[2] |
| distributivity / observability | expected_not_top=2 | 009-analyzability:near_miss[2]; 070-observability:should_trigger[2] |
| durability / extendability | expected_not_top=2 | 039-durability:should_trigger[2]; 080-recoverability:near_miss[2] |
| effectiveness / functionality | top_tie=2 | 020-completeness:should_trigger[4]; 031-correctness:near_miss[4] |
| effectiveness / interoperability | expected_not_top=2 | 040-effectiveness:should_trigger[2]; 095-suitability:near_miss[2] |
| effectiveness / predictability | expected_not_top=2 | 072-performance-efficiency-time-or-space-bounds:near_miss[4]; 074-predictability:should_trigger[4] |
| effectiveness / reliability | expected_not_top=2 | 081-reliability:should_trigger[4]; 092-stability:near_miss[4] |
| effectiveness / supportability | expected_not_top=2 | 063-maintainability:near_miss[4]; 096-supportability:should_trigger[4] |
| effectiveness / variability | top_tie=2 | 020-completeness:should_trigger[4]; 031-correctness:near_miss[4] |
| efficiency-device-efficiency / reliability | expected_not_top=2 | 041-efficiency-device-efficiency:should_trigger[2]; 099-sustainability:near_miss[2] |
| enhanceability / wrappability | expected_not_top=2 | 014-augmentability:near_miss[3]; 042-enhanceability:should_trigger[3] |
| evolvability / replaceability | expected_not_top=2 | 042-enhanceability:near_miss[2]; 043-evolvability:should_trigger[2] |
| extendability / variability | expected_not_top=2 | 044-expandability:near_miss[2]; 046-extendability:should_trigger[2] |
| extensibility / replaceability | expected_not_top=2 | 014-augmentability:near_miss[2]; 047-extensibility:should_trigger[2] |
| extensibility / testability | expected_not_top=2 | 101-testability:should_trigger[1]; 110-verifiability:near_miss[1] |
| fault-failure-tolerance / mobility | expected_not_top=2 | 067-mobility:should_trigger[1]; 069-nomadicity:near_miss[1] |
| fault-failure-tolerance / reconfigurability | expected_not_top=2 | 079-reconfigurability:should_trigger[1]; 079-reconfigurability:should_trigger[3] |
| fault-failure-tolerance / recoverability | near_pair_no_signal=1; near_target_outranks_sibling=1 | 048-fault-failure-tolerance:near_miss[1]; 080-recoverability:near_miss[1] |
| fault-failure-tolerance / reliability | expected_not_top=2 | 081-reliability:should_trigger[2]; 092-stability:near_miss[2] |
| fault-failure-tolerance / robustness | near_pair_no_signal=1; near_target_outranks_sibling=1 | 048-fault-failure-tolerance:near_miss[2]; 086-robustness:near_miss[1] |
| feasibility / viability | near_pair_no_signal=2 | 049-feasibility:near_miss[2]; 112-viability:near_miss[1] |
| formality / likeability | expected_not_top=2 | 051-formality:should_trigger[2]; 076-provability:near_miss[2] |
| functionality / sustainability | expected_not_top=2 | 041-efficiency-device-efficiency:near_miss[4]; 099-sustainability:should_trigger[4] |
| functionality / variability | top_tie=2 | 020-completeness:should_trigger[4]; 031-correctness:near_miss[4] |
| generality / provability | expected_not_top=2 | 045-expressiveness:near_miss[2]; 053-generality:should_trigger[2] |
| immunity / simplicity | expected_not_top=2 | 054-immunity:should_trigger[1]; 098-susceptibility:near_miss[1] |
| immunity / susceptibility | expected_not_top=1; near_pair_no_signal=1 | 054-immunity:near_miss[1]; 054-immunity:should_trigger[4] |
| integratability / modifiability | expected_not_top=2 | 056-integratability:should_trigger[4]; 114-wrappability:near_miss[4] |
| integratability / performance-efficiency-time-or-space-bounds | expected_not_top=2 | 072-performance-efficiency-time-or-space-bounds:should_trigger[2]; 088-scalability:near_miss[2] |
| interoperability / scalability | expected_not_top=2 | 044-expandability:near_miss[3]; 088-scalability:should_trigger[3] |
| legibility / readability | expected_not_top=2; near_target_outranks_sibling=1 | 060-legibility:should_trigger[1]; 078-readability:near_miss[1] |
| likeability / predictability | expected_not_top=2 | 074-predictability:should_trigger[1]; 092-stability:near_miss[1] |
| likeability / simplicity | expected_not_top=2 | 021-complexity-interacting-complexity:near_miss[1]; 091-simplicity:should_trigger[1] |
| likeability / trainability | expected_not_top=2 | 059-learnability:near_miss[1]; 103-trainability:should_trigger[1] |
| localizability / readability | expected_not_top=2 | 062-localizability:should_trigger[2]; 073-portability:near_miss[2] |
| localizability / stability | expected_not_top=2 | 074-predictability:near_miss[2]; 092-stability:should_trigger[2] |
| maintainability / modifiability | near_pair_no_signal=1; near_target_outranks_sibling=1 | 068-modifiability:near_miss[1]; 068-modifiability:near_miss[3] |
| manageability / operability | near_target_outranks_sibling=2 | 064-manageability:near_miss[4]; 071-operability:near_miss[2] |
| measurability / susceptibility | expected_not_top=2 | 054-immunity:near_miss[3]; 098-susceptibility:should_trigger[3] |
| operability / trainability | expected_not_top=2 | 030-controllability:near_miss[1]; 071-operability:should_trigger[1] |
| portability / repeatability | expected_not_top=2 | 036-demonstrability:near_miss[4]; 082-repeatability:should_trigger[4] |
| predictability / repeatability | expected_not_top=1; near_pair_no_signal=1; near_target_outranks_sibling=1 | 082-repeatability:near_miss[2]; 082-repeatability:near_miss[4] |
| recoverability / survivability | near_pair_no_signal=1; near_pair_tie=1 | 097-survivability:near_miss[1]; 097-survivability:near_miss[3] |
| replaceability / robustness | expected_not_top=2 | 019-compatibility:near_miss[4]; 083-replaceability:should_trigger[4] |
| safety / stability | expected_not_top=2 | 074-predictability:near_miss[4]; 092-stability:should_trigger[4] |
| scalability / structuredness | expected_not_top=2 | 077-quality-of-service:near_miss[2]; 088-scalability:should_trigger[2] |
| standardizability-standardization-standard / uniformity | expected_not_top=1; near_pair_no_signal=1 | 093-standardizability-standardization-standard:near_miss[2]; 107-uniformity:should_trigger[3] |
| structuredness / uniformity | near_pair_no_signal=1; near_target_outranks_sibling=1 | 094-structuredness:near_miss[2]; 094-structuredness:near_miss[4] |
| structuredness / versatility | expected_not_top=2 | 053-generality:near_miss[2]; 111-versatility:should_trigger[2] |
| supportability / usability | expected_not_top=2 | 063-maintainability:near_miss[2]; 096-supportability:should_trigger[2] |
| accessibility-access-control / visibility | expected_not_top=1 | 001-accessibility-access-control:should_trigger[1] |
| accountability / auditability | near_pair_tie=1 | 013-auditability:near_miss[3] |
| accuracy / certainty | near_pair_no_signal=1 | 003-accuracy:near_miss[2] |
| accuracy / interoperability | expected_not_top=1 | 003-accuracy:should_trigger[4] |
| accuracy / safety | expected_not_top=1 | 087-safety:should_trigger[2] |
| adaptability / completeness | expected_not_top=1 | 004-adaptability:should_trigger[4] |
| adaptability / flexibility | near_pair_no_signal=1 | 004-adaptability:near_miss[1] |
| adaptability / reconfigurability | near_pair_no_signal=1 | 004-adaptability:near_miss[2] |
| additivity / anonymity | expected_not_top=1 | 010-anonymity:should_trigger[1] |
| additivity / augmentability | near_target_outranks_sibling=1 | 005-additivity:near_miss[1] |
| additivity / conciseness | expected_not_top=1 | 025-conciseness:should_trigger[2] |
| additivity / configurability | top_tie=1 | 078-readability:should_trigger[2] |
| additivity / conformance | expected_not_top=1 | 005-additivity:should_trigger[3] |
| additivity / integratability | expected_not_top=1 | 005-additivity:should_trigger[1] |
| additivity / maturity | expected_not_top=1 | 065-maturity:should_trigger[4] |
| additivity / readability | expected_not_top=1 | 078-readability:should_trigger[2] |
| additivity / replicability | top_tie=1 | 078-readability:should_trigger[2] |
| adjustability / configurability | near_pair_no_signal=1 | 006-adjustability:near_miss[1] |
| adjustability / reconfigurability | near_pair_no_signal=1 | 006-adjustability:near_miss[2] |
| affordability / agility | expected_not_top=1 | 008-agility:should_trigger[4] |
| affordability / feasibility | near_pair_no_signal=1 | 007-affordability:near_miss[1] |
| agility / augmentability | expected_not_top=1 | 014-augmentability:should_trigger[2] |
| agility / effectiveness | expected_not_top=1 | 040-effectiveness:should_trigger[1] |
| agility / maintainability | expected_not_top=1 | 008-agility:should_trigger[2] |
| agility / trustability | expected_not_top=1 | 105-trustability:should_trigger[1] |
| analyzability / understandability | expected_not_top=1 | 106-understandability:should_trigger[1] |
| anonymity / confidentiality | near_pair_no_signal=1 | 010-anonymity:near_miss[2] |
| anonymity / immunity | expected_not_top=1 | 010-anonymity:should_trigger[3] |
| anonymity / legibility | expected_not_top=1 | 062-localizability:near_miss[2] |
| anonymity / privacy | near_target_outranks_sibling=1 | 010-anonymity:near_miss[1] |
| atomicity / durability | near_pair_no_signal=1 | 011-atomicity:near_miss[1] |
| atomicity / recoverability | near_pair_no_signal=1 | 011-atomicity:near_miss[2] |
| attractiveness / comprehensiveness | expected_not_top=1 | 020-completeness:near_miss[2] |
| attractiveness / modifiability | expected_not_top=1 | 021-complexity-interacting-complexity:near_miss[2] |
| attractiveness / visibility | expected_not_top=1 | 113-visibility:should_trigger[2] |
| auditability / conformance | expected_not_top=1 | 013-auditability:should_trigger[2] |
| auditability / dependability | expected_not_top=1 | 013-auditability:should_trigger[4] |
| auditability / traceability | near_pair_no_signal=1 | 013-auditability:near_miss[2] |
| augmentability / comprehensiveness | top_tie=1 | 024-comprehensiveness:should_trigger[3] |
| augmentability / expressiveness | expected_not_top=1 | 045-expressiveness:should_trigger[4] |
| availability / feasibility | expected_not_top=1 | 015-availability:should_trigger[2] |
| availability / measurability | expected_not_top=1 | 015-availability:should_trigger[4] |
| availability / reliability | near_pair_no_signal=1 | 015-availability:near_miss[1] |
| availability / simplicity | expected_not_top=1 | 091-simplicity:should_trigger[2] |
| certainty / defensibility | expected_not_top=1 | 035-defensibility:should_trigger[1] |
| changeability / supportability | near_target_outranks_sibling=1 | 096-supportability:near_miss[2] |
| communicativeness / comprehensibility | near_pair_no_signal=1 | 018-communicativeness:near_miss[2] |
| communicativeness / consistency | expected_not_top=1 | 113-visibility:near_miss[4] |
| communicativeness / self-descriptiveness | near_pair_no_signal=1 | 018-communicativeness:near_miss[1] |
| communicativeness / survivability | expected_not_top=1 | 097-survivability:should_trigger[4] |
| communicativeness / visibility | near_pair_no_signal=1 | 113-visibility:near_miss[2] |
| completeness / conciseness | expected_not_top=1 | 025-conciseness:should_trigger[4] |
| completeness / correctness | near_pair_no_signal=1 | 031-correctness:near_miss[2] |
| completeness / privacy | expected_not_top=1 | 075-privacy:should_trigger[4] |
| complexity-interacting-complexity / simplicity | near_pair_no_signal=1 | 021-complexity-interacting-complexity:near_miss[1] |
| composability / reusability | near_target_outranks_sibling=1 | 085-reusability:near_miss[4] |
| comprehensibility / readability | near_pair_no_signal=1 | 078-readability:near_miss[2] |
| comprehensibility / self-descriptiveness | near_pair_no_signal=1 | 090-self-descriptiveness:near_miss[2] |
| comprehensiveness / conciseness | near_pair_no_signal=1 | 025-conciseness:near_miss[2] |
| comprehensiveness / enhanceability | top_tie=1 | 024-comprehensiveness:should_trigger[1] |
| comprehensiveness / trainability | near_pair_no_signal=1 | 103-trainability:near_miss[2] |
| conciseness / defensibility | expected_not_top=1 | 035-defensibility:should_trigger[4] |
| conciseness / expressiveness | expected_not_top=1 | 045-expressiveness:should_trigger[2] |
| conciseness / integrity | expected_not_top=1 | 057-integrity:should_trigger[3] |
| conciseness / readability | expected_not_top=1 | 025-conciseness:should_trigger[1] |
| configurability / functionality | expected_not_top=1 | 052-functionality:should_trigger[2] |
| configurability / readability | expected_not_top=1 | 078-readability:should_trigger[2] |
| configurability / replicability | top_tie=1 | 078-readability:should_trigger[2] |
| configurability / tailorability | near_target_outranks_sibling=1 | 100-tailorability:near_miss[2] |
| configurability / understandability | expected_not_top=1 | 106-understandability:should_trigger[3] |
| configurability / variability | near_pair_no_signal=1 | 109-variability:near_miss[1] |
| conformance / correctness | near_pair_no_signal=1 | 028-conformance:near_miss[2] |
| conformance / demonstrability | expected_not_top=1 | 036-demonstrability:should_trigger[1] |
| conformance / expressiveness | expected_not_top=1 | 045-expressiveness:should_trigger[1] |
| conformance / interoperability | expected_not_top=1 | 028-conformance:should_trigger[2] |
| consistency / interoperability | expected_not_top=1 | 029-consistency:should_trigger[1] |
| controllability / operability | near_target_outranks_sibling=1 | 071-operability:near_miss[1] |
| controllability / self-descriptiveness | expected_not_top=1 | 030-controllability:should_trigger[2] |
| customizability / extensibility | near_pair_no_signal=1 | 047-extensibility:near_miss[2] |
| decomposability / integratability | expected_not_top=1 | 034-decomposability:should_trigger[2] |
| decomposability / self-descriptiveness | expected_not_top=1 | 090-self-descriptiveness:should_trigger[2] |
| decomposability / understandability | expected_not_top=1 | 034-decomposability:should_trigger[4] |
| defensibility / reconfigurability | expected_not_top=1 | 035-defensibility:should_trigger[3] |
| defensibility / recoverability | near_pair_no_signal=1 | 035-defensibility:near_miss[2] |
| defensibility / security-control-and-security | near_pair_no_signal=1 | 035-defensibility:near_miss[1] |
| demonstrability / effectiveness | expected_not_top=1 | 036-demonstrability:should_trigger[4] |
| demonstrability / trustability | expected_not_top=1 | 105-trustability:should_trigger[3] |
| dependability / reliability | near_pair_no_signal=1 | 037-dependability:near_miss[1] |
| distributivity / safety | expected_not_top=1 | 087-safety:should_trigger[3] |
| distributivity / scalability | expected_not_top=1; near_target_outranks_sibling=1 | 038-distributivity:near_miss[3] |
| efficiency-device-efficiency / performance-efficiency-time-or-space-bounds | near_pair_no_signal=1 | 041-efficiency-device-efficiency:near_miss[1] |
| enhanceability / evolvability | near_pair_no_signal=1 | 042-enhanceability:near_miss[2] |
| enhanceability / trainability | expected_not_top=1 | 103-trainability:should_trigger[2] |
| evolvability / maturity | expected_not_top=1 | 065-maturity:should_trigger[1] |
| evolvability / usability | expected_not_top=1 | 043-evolvability:should_trigger[1] |
| expandability / scalability | near_target_outranks_sibling=1 | 088-scalability:near_miss[1] |
| expressiveness / flexibility | expected_not_top=1 | 050-flexibility:should_trigger[2] |
| expressiveness / variability | expected_not_top=1 | 109-variability:should_trigger[1] |
| extensibility / localizability | expected_not_top=1 | 062-localizability:should_trigger[1] |
| extensibility / replicability | top_tie=1 | 062-localizability:should_trigger[1] |
| fault-failure-tolerance / quality-of-service | expected_not_top=1 | 077-quality-of-service:should_trigger[3] |
| fault-failure-tolerance / survivability | expected_not_top=1 | 097-survivability:should_trigger[1] |
| feasibility / integratability | expected_not_top=1 | 049-feasibility:should_trigger[2] |
| feasibility / measurability | expected_not_top=1 | 066-measurability:should_trigger[4] |
| feasibility / suitability | top_tie=1 | 097-survivability:should_trigger[2] |
| feasibility / survivability | expected_not_top=1 | 097-survivability:should_trigger[2] |
| flexibility / reconfigurability | near_pair_no_signal=1 | 050-flexibility:near_miss[2] |
| formality / provability | near_pair_tie=1 | 076-provability:near_miss[4] |
| formality / stability | expected_not_top=1 | 092-stability:should_trigger[3] |
| functionality / suitability | near_target_outranks_sibling=1 | 095-suitability:near_miss[1] |
| immunity / robustness | near_pair_no_signal=1 | 054-immunity:near_miss[2] |
| integratability / maintainability | expected_not_top=1 | 063-maintainability:should_trigger[2] |
| integratability / predictability | expected_not_top=1 | 082-repeatability:near_miss[2] |
| integratability / readability | expected_not_top=1 | 091-simplicity:near_miss[2] |
| integratability / variability | expected_not_top=1 | 109-variability:should_trigger[2] |
| integrity / reusability | expected_not_top=1 | 029-consistency:near_miss[2] |
| integrity / security-control-and-security | near_pair_no_signal=1 | 089-security-control-and-security:near_miss[2] |
| learnability / trainability | near_pair_no_signal=1 | 059-learnability:near_miss[1] |
| legibility / localizability | near_target_outranks_sibling=1 | 062-localizability:near_miss[4] |
| likeability / privacy | expected_not_top=1 | 075-privacy:should_trigger[2] |
| localizability / portability | near_pair_no_signal=1 | 073-portability:near_miss[2] |
| localizability / replicability | expected_not_top=1 | 062-localizability:should_trigger[1] |
| localizability / standardizability-standardization-standard | expected_not_top=1 | 062-localizability:should_trigger[3] |
| maintainability / manageability | top_tie=1 | 077-quality-of-service:should_trigger[2] |
| maintainability / portability | top_tie=1 | 077-quality-of-service:should_trigger[2] |
| maintainability / quality-of-service | expected_not_top=1 | 077-quality-of-service:should_trigger[2] |
| manageability / portability | top_tie=1 | 077-quality-of-service:should_trigger[2] |
| manageability / quality-of-service | expected_not_top=1 | 077-quality-of-service:should_trigger[2] |
| maturity / reliability | near_pair_no_signal=1 | 065-maturity:near_miss[1] |
| measurability / standardizability-standardization-standard | expected_not_top=1 | 066-measurability:should_trigger[2] |
| mobility / modifiability | expected_not_top=1 | 067-mobility:should_trigger[2] |
| mobility / nomadicity | top_tie=1 | 069-nomadicity:near_miss[2] |
| mobility / recoverability | expected_not_top=1 | 069-nomadicity:near_miss[2] |
| modifiability / reconfigurability | expected_not_top=1 | 109-variability:near_miss[2] |
| nomadicity / recoverability | expected_not_top=1; near_target_outranks_sibling=1 | 069-nomadicity:near_miss[2] |
| performance-efficiency-time-or-space-bounds / predictability | near_pair_no_signal=1 | 074-predictability:near_miss[1] |
| performance-efficiency-time-or-space-bounds / quality-of-service | near_pair_no_signal=1 | 077-quality-of-service:near_miss[1] |
| portability / quality-of-service | expected_not_top=1 | 077-quality-of-service:should_trigger[2] |
| provability / structuredness | top_tie=1 | 094-structuredness:should_trigger[2] |
| quality-of-service / scalability | near_pair_no_signal=1 | 077-quality-of-service:near_miss[2] |
| quality-of-service / usability | expected_not_top=1 | 077-quality-of-service:should_trigger[1] |
| readability / replicability | expected_not_top=1 | 078-readability:should_trigger[2] |
| repeatability / replicability | near_pair_tie=1 | 084-replicability:near_miss[1] |
| repeatability / sustainability | expected_not_top=1 | 099-sustainability:should_trigger[1] |
| robustness / safety | near_pair_no_signal=1 | 087-safety:near_miss[2] |
| robustness / susceptibility | near_pair_no_signal=1 | 098-susceptibility:near_miss[2] |
| safety / security-control-and-security | near_pair_no_signal=1 | 087-safety:near_miss[1] |
| safety / supportability | expected_not_top=1 | 087-safety:should_trigger[1] |
| security-control-and-security / susceptibility | expected_not_top=1 | 098-susceptibility:should_trigger[2] |
| suitability / survivability | expected_not_top=1 | 097-survivability:should_trigger[2] |
| suitability / tailorability | expected_not_top=1 | 100-tailorability:should_trigger[1] |
| testability / verifiability | near_target_outranks_sibling=1 | 110-verifiability:near_miss[1] |
| traceability / verifiability | expected_not_top=1 | 102-traceability:should_trigger[1] |
| versatility / visibility | expected_not_top=1 | 111-versatility:should_trigger[1] |

Distinct flagged pairs: 337.

### Near-miss cases where the owner outranks its sibling

| Case | Intended sibling | Owner score | Sibling score | Behavior | Prompt |
| --- | --- | ---: | ---: | --- | --- |
| 005-additivity:near_miss[1] | augmentability | 0.038462 | 0.037037 | clarify | Add something useful to the editor. |
| 008-agility:near_miss[4] | modifiability | 0.064516 | 0.055556 | route | Bound measured versus estimated effort for this named code change, including its migration and verification impact. |
| 010-anonymity:near_miss[1] | privacy | 0.031250 | 0.030303 | clarify | Clean up our customer data. |
| 012-attractiveness:near_miss[1] | likeability | 0.047619 | 0.000000 | clarify | Make the experience better. |
| 015-availability:near_miss[4] | recoverability | 0.027027 | 0.022727 | route | Reconcile overlapping snapshot and replay identities before resuming writers and compare restored state with the agreed loss allowance. |
| 017-changeability:near_miss[4] | modifiability | 0.083333 | 0.055556 | route | Bound measured versus estimated effort for this named code change, including its migration and verification impact. |
| 020-completeness:near_miss[4] | comprehensiveness | 0.107143 | 0.096774 | route | Review the manual's topic coverage for its intended readers, not membership of records in an export. |
| 026-confidentiality:near_miss[1] | privacy | 0.032258 | 0.030303 | clarify | Clean up our customer data. |
| 034-decomposability:near_miss[2] | composability | 0.047619 | 0.045455 | clarify | Help us combine these components. |
| 038-distributivity:near_miss[3] | scalability | 0.111111 | 0.081081 | route | Increase concurrent users and record how throughput, errors and resource needs change across the workload growth. |
| 039-durability:near_miss[4] | recoverability | 0.047619 | 0.022727 | route | Reconcile overlapping snapshot and replay identities before resuming writers and compare restored state with the agreed loss allowance. |
| 040-effectiveness:near_miss[4] | suitability | 0.085714 | 0.054054 | route | Choose the report capability that fits this team's stated handoff context, rather than counting available features. |
| 046-extendability:near_miss[1] | extensibility | 0.080000 | 0.038462 | clarify | Let people add plugins. |
| 048-fault-failure-tolerance:near_miss[1] | recoverability | 0.035714 | 0.000000 | clarify | Get the service back. |
| 048-fault-failure-tolerance:near_miss[2] | robustness | 0.034483 | 0.000000 | clarify | Stop overload breaking the worker. |
| 060-legibility:near_miss[4] | attractiveness | 0.057143 | 0.000000 | route | Review the palette and composition using appearance judgments under the same viewing conditions. |
| 061-likeability:near_miss[2] | usability | 0.095238 | 0.041667 | clarify | People struggle with the app. |
| 061-likeability:near_miss[3] | attractiveness | 0.103448 | 0.066667 | route | Compare static visual styles for aesthetic appeal to the intended audience without treating task success as the verdict. |
| 061-likeability:near_miss[4] | usability | 0.030303 | 0.028571 | route | Fix task interaction obstacles and verify the real goal, rather than judging only preference or newly acquired ability. |
| 062-localizability:near_miss[4] | legibility | 0.032258 | 0.028571 | route | Change the rendering so readers can distinguish the characters without changing the wording or its structure. |
| 064-manageability:near_miss[4] | operability | 0.054054 | 0.027027 | route | Define the entry conditions, actions and exit checks for rerunning this runtime job, including what to do with partial state. |
| 065-maturity:near_miss[2] | dependability | 0.066667 | 0.000000 | clarify | Do we have enough assurance? |
| 068-modifiability:near_miss[3] | maintainability | 0.058824 | 0.057143 | route | Improve continuing diagnosis, repair and modification across representative recurring upkeep tasks. |
| 069-nomadicity:near_miss[2] | recoverability | 0.066667 | 0.060606 | clarify | We lose work after a crash. |
| 071-operability:near_miss[1] | controllability | 0.034483 | 0.031250 | clarify | Give on-call a way to stop this. |
| 071-operability:near_miss[2] | manageability | 0.035714 | 0.034483 | clarify | We need better fleet controls. |
| 075-privacy:near_miss[1] | confidentiality | 0.064516 | 0.033333 | clarify | Stop exposing this data. |
| 078-readability:near_miss[1] | legibility | 0.041667 | 0.033333 | clarify | The text is hard to read. |
| 082-repeatability:near_miss[4] | predictability | 0.125000 | 0.093023 | route | Explain and bound the variation between repeated service runs under matched conditions, including rare pauses. |
| 085-reusability:near_miss[4] | composability | 0.028571 | 0.000000 | route | When the middle stage rejects a row, make the whole chain agree on what stops, what continues, and who releases the input. |
| 088-scalability:near_miss[1] | expandability | 0.033333 | 0.031250 | clarify | We need more capacity. |
| 094-structuredness:near_miss[4] | uniformity | 0.030303 | 0.027778 | route | Align the peer forms' treatment of the same validation action so callers do not relearn it for each form. |
| 095-suitability:near_miss[1] | functionality | 0.076923 | 0.038462 | clarify | The export feature is missing. |
| 096-supportability:near_miss[2] | changeability | 0.037037 | 0.000000 | clarify | We cannot seem to ship this. |
| 096-supportability:near_miss[3] | maintainability | 0.060606 | 0.057143 | route | Improve continuing diagnosis, repair and modification across representative recurring upkeep tasks. |
| 099-sustainability:near_miss[1] | efficiency-device-efficiency | 0.037037 | 0.034483 | clarify | Use fewer resources. |
| 099-sustainability:near_miss[4] | efficiency-device-efficiency | 0.108108 | 0.102564 | route | Compare bytes transferred per useful decoded result before choosing the packed representation; keep output quality fixed. |
| 100-tailorability:near_miss[2] | configurability | 0.068966 | 0.040000 | clarify | Let us control its behavior. |
| 102-traceability:near_miss[4] | accountability | 0.028571 | 0.027778 | route | Shared credentials only identify a service; preserve that limit instead of assigning a guessed human actor. |
| 110-verifiability:near_miss[1] | testability | 0.040000 | 0.038462 | clarify | This is hard to test. |
| 112-viability:near_miss[2] | affordability | 0.038462 | 0.000000 | clarify | This service is getting expensive. |

## Limitations and uncertain judgments

- The repository disambiguation map supplies local conventions, not standardized definitions. Expected labels depend on those conventions and need human semantic review.
- The 51 new files use developer questions and concrete repository tasks. Some explicit cases necessarily state contracts, states, or evidence; naturalness is an author judgment, not a tested population result.
- Reusing a sibling case as a near miss makes the boundary comparison inspectable but correlates examples. Prompt totals are not independent observations.
- Four near misses per skill cover selected siblings rather than every possible overlap in a cluster.
- The 63 existing eval files retain their original wording and judgments. They were not rewritten to match the new prompts.
- Some generic prompts admit several sibling interpretations even after a provisional lead is recorded. Their correct next action remains to ask the supplied question.
- Synthetic checker and scorer tests establish implementation behavior, not the semantic correctness of these new labels or actual agent routing performance.
- Existing blinded-routing assets remain the earlier snapshot. No blinded routing test was run, and this report contains no measured model accuracy.
- The flagged pairs and near misses above remain review findings. Their scores did not authorize changes to descriptions, skill bodies, or the catalogue.
