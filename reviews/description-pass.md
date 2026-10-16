# Description pass findings

All 63 authored descriptions now fit within 350 characters (252-349 characters after folding YAML). Previously, 53 exceeded that limit. Each now contains three quoted developer-ticket/chat phrases, except Accessibility/Access Control, which contains four across its two branches. All 190 complete trigger phrases are unique across the authored descriptions, including against the rest of each other description after case folding. That exact-phrase check is stronger than checking only the nearest sibling, but does not establish semantic exclusivity.

Every existing `(see slug)` pointer remains, every target exists in the catalogue, and every description retains a `Not for` clause. No sibling exclusion was removed to fit the limit. The table below conservatively records compressed scope qualifications, cautions, and discovery branches as well as lost detail; retaining the slugs does not mean every boundary has equal precision. These qualifications remain in the unchanged bodies and references. This is a discovery-text pass, not approval of broader claims.

The fixed lexical checker regressed overall. Strict near-miss warnings increased from 22 to 27; flagged pairs increased from 139 to 190. This pass does not demonstrate better routing.

## Before/after checker findings

Baseline: commit `3a9360b`, captured before edits. Both runs used the same 63 authored candidates, 504 eval cases, and unchanged scorer. Half the cases omit the distinguishing fact and require clarification. Counts are checker findings, not accuracy estimates or independent trials.

| Finding | Before | After |
| --- | ---: | ---: |
| `expected_not_top` | 192 | 263 |
| `near_pair_no_signal` | 38 | 60 |
| `near_pair_tie` | 3 | 5 |
| `near_target_outranks_sibling` | 22 | 27 |
| `no_keyword_signal` | 10 | 28 |
| `top_tie` | 30 | 27 |
| Cases with any flag | 217 | 303 |
| Distinct flagged pairs | 139 | 190 |

Flags overlap within cases and pairs; these rows must not be summed as a failure count.

| Case group | Flagged before | Flagged after | Strict near-miss before | Strict near-miss after |
| --- | ---: | ---: | ---: | ---: |
| Fact omitted; clarification required | 170 | 212 | 13 | 15 |
| Distinguishing fact present | 47 | 91 | 9 | 12 |

Of the former strict near-miss warnings, 16 disappeared and 6 remain; 21 appeared. Disappearing warnings are lexical changes, not proven fixes.

The scorer uses exact word-set overlap without stemming, synonyms, or negation handling. Shorter descriptions remove formal vocabulary used by some frozen evals; everyday triggers do not necessarily share those words. Excluded siblings also contribute matching words. For example, the modifiability near-miss about measured versus estimated effort overlaps Agility's excluded phrase “code-edit effort”; that is not a positive Agility claim. Nevertheless, the increase in explicit-case warnings remains a real limitation requiring human routing review.

## Per-skill lengths and compressed qualifications

Lengths count the parsed description, including spaces and punctuation, excluding YAML syntax. “No additional qualification loss” means the existing acceptance boundary survives in shorter wording; it is not a claim of perfect routing.

| Id / skill | Before | After | Compressed qualification / discovery limit |
| --- | ---: | ---: | --- |
| 001 `accessibility-access-control` | 620 | 334 | Actor/action/resource detail is compressed to permission checks; branch clarification remains explicit. |
| 002 `accountability` | 467 | 300 | Delegation and evidence binding are less explicit; initiating/executing actors and the identity model remain. |
| 004 `adaptability` | 451 | 328 | The old-versus-changed comparison is compressed to preserving behavior across changed conditions. |
| 005 `additivity` | 341 | 261 | The declared baseline and aggregation rule move out of discovery text. |
| 006 `adjustability` | 380 | 257 | No additional qualification loss; existing sibling exclusions retained. |
| 008 `agility` | 398 | 260 | No additional qualification loss; existing sibling exclusions retained. |
| 010 `anonymity` | 481 | 324 | Observer knowledge and linkage-model limits are less explicit than the former auxiliary-knowledge wording. |
| 011 `atomicity` | 456 | 314 | Participating effects, observers, and the commit boundary are omitted from discovery text. |
| 012 `attractiveness` | 381 | 267 | No additional qualification loss; existing sibling exclusions retained. |
| 013 `auditability` | 477 | 312 | Evidence provenance, retention, and retrieval are omitted; independent review remains the acceptance question. |
| 014 `augmentability` | 428 | 293 | Optional versus required supplements and separately accepted side effects are no longer explicit. |
| 015 `availability` | 308 | 252 | No additional qualification loss; existing sibling exclusions retained. |
| 017 `changeability` | 385 | 277 | Completion evidence and handoffs are compressed into the request-to-adoption boundary. |
| 018 `communicativeness` | 380 | 289 | Recipient, channel, and next-action detail are omitted; timely feedback remains distinct from state cues. |
| 023 `comprehensibility` | 445 | 306 | Audience and source-grounded interpretation scenarios are no longer explicit. |
| 024 `comprehensiveness` | 441 | 297 | No additional qualification loss; existing sibling exclusions retained. |
| 025 `conciseness` | 456 | 295 | Obligation strength and retained propositions are compressed to preserving meaning and exceptions. |
| 026 `confidentiality` | 449 | 287 | Alternate disclosure paths are shortened to API, cache, and error examples. |
| 027 `configurability` | 414 | 311 | Precedence, scope, and effective-choice verification are omitted. |
| 032 `customizability` | 442 | 301 | The bounded user-authored artifact and its accepted output are no longer explicit. |
| 035 `defensibility` | 540 | 336 | Discovery narrows to containment; detection and contesting active actions are not separately advertised. |
| 037 `dependability` | 439 | 304 | Claim assumptions and counterexamples are compressed to combined failure evidence and gaps. |
| 039 `durability` | 487 | 308 | Subsequent-event scope narrows to named faults in discovery text. |
| 041 `efficiency-device-efficiency` | 286 | 310 | No additional qualification loss; existing sibling exclusions retained. |
| 042 `enhanceability` | 444 | 347 | Retained acceptance criteria are omitted to fit the implementation/refinement boundary plus three triggers. |
| 043 `evolvability` | 403 | 299 | The explicit path-level acceptance sentence is omitted; prior state and carried obligations remain. |
| 044 `expandability` | 326 | 300 | Placement and transition checks are omitted; admission into an existing installation remains. |
| 046 `extendability` | 406 | 290 | Capability/result-type detail is compressed to bounded core changes and missing hooks. |
| 047 `extensibility` | 445 | 306 | The explanatory routing sentence is compressed; existing hook, no core edits, and building/widening exclusions remain. |
| 048 `fault-failure-tolerance` | 480 | 303 | Concurrent-fault limits and permitted degradation are no longer explicit in discovery text. |
| 050 `flexibility` | 458 | 307 | No additional qualification loss; existing sibling exclusions retained. |
| 054 `immunity` | 535 | 345 | The warning that tests do not prove universal exclusion is omitted; explicit premises still bound the claim. |
| 057 `integrity` | 478 | 300 | Trusted provenance and permitted-transition detail are omitted. |
| 059 `learnability` | 415 | 294 | Initial attempts, practice, and unaided transfer are compressed into natural learning complaints. |
| 060 `legibility` | 473 | 339 | Transcription evidence and the named audience are omitted; character/symbol recognition remains. |
| 061 `likeability` | 410 | 266 | Separate positive/negative judgments are omitted; response after use remains explicit. |
| 063 `maintainability` | 471 | 288 | Representative upkeep tasks and retained obligations are compressed to recurring upkeep. |
| 065 `maturity` | 475 | 327 | The intended-use qualification and evidence-gap sentence are less explicit. |
| 068 `modifiability` | 434 | 316 | Measured-versus-estimated effort and affected-contract detail are omitted. |
| 072 `performance-efficiency-time-or-space-bounds` | 306 | 323 | No additional qualification loss; existing sibling exclusions retained. |
| 074 `predictability` | 318 | 326 | The explicit first clarification question is replaced by the variation-versus-absolute-tail-limit exclusion. |
| 075 `privacy` | 480 | 324 | Named regulation/request acronyms and the explicit no-legal-obligations warning are omitted; supplied policy constraints remain. |
| 077 `quality-of-service` | 291 | 315 | No additional qualification loss; existing sibling exclusions retained. |
| 078 `readability` | 314 | 270 | No additional qualification loss; existing sibling exclusions retained. |
| 079 `reconfigurability` | 444 | 321 | Carried in-progress state is expressed by queue/switch triggers rather than a separate scope sentence. |
| 080 `recoverability` | 518 | 346 | Lost-state allowance, milestones, and reconciled work are omitted; usable-state restoration remains explicit. |
| 081 `reliability` | 474 | 325 | The declared interval and retained exposure/restart history are omitted; the operating profile remains. |
| 086 `robustness` | 547 | 340 | Permitted rejection and resource/state bounds are omitted from discovery text. |
| 087 `safety` | 459 | 310 | Stakeholder-defined harm and residual-exposure wording are shortened to named harm. |
| 088 `scalability` | 276 | 342 | No additional qualification loss; existing sibling exclusions retained. |
| 089 `security-control-and-security` | 484 | 319 | Protected assets, trust boundaries, and residual exposure are omitted; adversary paths remain explicit. |
| 090 `self-descriptiveness` | 462 | 321 | The affected-object inference check is compressed into the report-editing trigger. |
| 092 `stability` | 473 | 335 | Settling and directional/reversal evidence are omitted; drift and feedback remain distinct from variation. |
| 096 `supportability` | 477 | 321 | Authorized evidence, reproduction, and escalation are compressed into a specific support encounter. |
| 097 `survivability` | 560 | 349 | Explicit mission selection, degraded authority, and dependency limits are omitted. |
| 098 `susceptibility` | 491 | 335 | Entrypoint and capability detail is compressed; preconditions and no presumption of exploitation remain. |
| 099 `sustainability` | 282 | 328 | No additional qualification loss; existing sibling exclusions retained. |
| 100 `tailorability` | 485 | 347 | No additional qualification loss; existing sibling exclusions retained. |
| 102 `traceability` | 454 | 312 | Typed links and reverse navigation are omitted; versioned artifacts and impact remain. |
| 103 `trainability` | 461 | 339 | Lesson/feedback alignment is compressed to instruction and independent checks. |
| 105 `trustability` | 517 | 331 | Unknowns and decision authority are no longer separately stated; scope, evidence, and limits remain. |
| 106 `understandability` | 468 | 297 | Purpose and cross-component prediction checks are compressed into the whole-system-model boundary. |
| 108 `usability` | 420 | 285 | Audience, assistance, effort, and recovery qualifications are omitted; end-to-end task performance remains. |

The most consequential boundary/caution compression is in 042 (retained acceptance criteria), 048 (concurrent faults and permitted degradation), 054 (tests versus proof), 075 (explicit legal-claim restraint), 080 (loss allowance and reconciliation), 081 (declared interval), and 097 (mission selection and degraded authority). These descriptions must not substitute for reading the skill before acting. Privacy's former regulation acronyms are no longer discovery triggers; no legal obligation or compliance conclusion was added.

The two plugin skills still distinguish an existing usable hook without core edits (047) from building/widening the hook or changing the core (046). Performance still concerns absolute bounds at a stated load; Predictability still concerns variation across comparable runs. Privacy still concerns purpose/lifecycle rather than recipient authorization or identity linkage. Similar requests without these facts still require clarification.

## Remaining strict near-miss findings

Each row means the evaluated target lexically outranks its intended sibling. A fact-omitted case has a provisional sibling label, not an unconditional routing verdict.

| Case | Intended sibling | Distinguishing fact |
| --- | --- | --- |
| `005-additivity:near_miss[1]` | `augmentability` | Omitted |
| `008-agility:near_miss[4]` | `modifiability` | Present |
| `010-anonymity:near_miss[1]` | `privacy` | Omitted |
| `012-attractiveness:near_miss[1]` | `likeability` | Omitted |
| `013-auditability:near_miss[3]` | `accountability` | Present |
| `015-availability:near_miss[4]` | `recoverability` | Present |
| `017-changeability:near_miss[4]` | `modifiability` | Present |
| `026-confidentiality:near_miss[1]` | `privacy` | Omitted |
| `039-durability:near_miss[4]` | `recoverability` | Present |
| `046-extendability:near_miss[1]` | `extensibility` | Omitted |
| `048-fault-failure-tolerance:near_miss[1]` | `recoverability` | Omitted |
| `048-fault-failure-tolerance:near_miss[2]` | `robustness` | Omitted |
| `060-legibility:near_miss[4]` | `attractiveness` | Present |
| `061-likeability:near_miss[2]` | `usability` | Omitted |
| `061-likeability:near_miss[3]` | `attractiveness` | Present |
| `061-likeability:near_miss[4]` | `usability` | Present |
| `065-maturity:near_miss[2]` | `dependability` | Omitted |
| `068-modifiability:near_miss[3]` | `maintainability` | Present |
| `075-privacy:near_miss[1]` | `confidentiality` | Omitted |
| `078-readability:near_miss[1]` | `legibility` | Omitted |
| `088-scalability:near_miss[1]` | `expandability` | Omitted |
| `096-supportability:near_miss[2]` | `changeability` | Omitted |
| `096-supportability:near_miss[3]` | `maintainability` | Present |
| `099-sustainability:near_miss[1]` | `efficiency-device-efficiency` | Omitted |
| `099-sustainability:near_miss[4]` | `efficiency-device-efficiency` | Present |
| `100-tailorability:near_miss[2]` | `configurability` | Omitted |
| `102-traceability:near_miss[4]` | `accountability` | Present |

## Verification and scope

- `python scripts/validate_skills.py`: 63 checked, 51 absent todo skills, zero errors.
- `python -m unittest discover -s tests -v`: all 28 tests pass.
- `python scripts/check_descriptions.py --json`: completed successfully; warnings are recorded above, not treated as a passing routing score.
- Additional read-only assertions verified the 350-character cap, three-to-five quoted triggers, real sibling pointers, and exact trigger uniqueness.
- SHA-256 comparisons verified every skill body and every byte outside its description block against the pre-edit snapshot, including other frontmatter fields.
- Hash comparisons verified all 63 eval files, the catalogue, scorer, and scorer tests unchanged. Git scope contains only the 63 description edits and this report.
- No body, reference, eval, catalogue, tool, or test was edited. No batch or further phase was started.

## Uncertainty and human review

Natural phrasing is a judgment about plausible developer language, not an observation of actual ticket frequencies. Exact phrase uniqueness does not remove conceptual overlap: an export-format request, deploy disruption, or data complaint still needs context. The lexical regression and compressed qualifications above need human review; this pass cannot establish semantic routing improvement. No external factual claims, standards, legal obligations, or numeric system targets were introduced.
