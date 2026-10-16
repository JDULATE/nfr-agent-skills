# Phase 5 authored-skill dry run

## Findings

The run covers the 63 catalogue entries whose status is not todo. Each has an
eval file with four should-trigger and four near-miss prompts, giving 504 cases.
Exactly 252 prompts omit the distinguishing fact: two should-trigger and two
near-miss cases per skill. Those cases expect clarification and name a provisional
routing lead; they are not unconditional binary routing truths. No hidden project
facts or answers were supplied to the scorer.

The full run found 22 near-miss comparisons where the evaluated skill's description
outscored its intended sibling: nine explicit cases and thirteen underspecified
cases. There are also three positive near-pair ties and 38 near-pairs with no
shared keyword signal. These are distinct from the overall top-ranking question.

Across the entire authored competitor pool, 192 cases do not put their intended
lead among the highest-scoring descriptions. Of these, 149 omit the deciding fact
and 43 state it. Thirty cases have positive top-score ties; ten have no keyword
signal anywhere. Flags overlap and must not be added into an error count.

The report lists all 139 flagged lexical pairs below. That number includes
unrelated lexical competitors and zero-signal pairs; it is not a count of proven
semantic boundary defects. No description was edited or automatically repaired.

## Method and label limits

The checker uses set Jaccard overlap: shared prompt/description keywords divided
by their union. It lowercases word tokens, splits hyphens and removes the fixed
stop-word list in the script. It does not stem words, expand synonyms, interpret
negation, read skill bodies or use the clarifying-question metadata for scoring.
Exact fractions determine comparisons and ties; displayed scores are rounded.
The entire description is scored, including Not for exclusions.

All 63 authored descriptions compete for every prompt, even with --only.
The 51 todo entries are excluded, not assigned invented descriptions or zero-score
stand-ins. Every named near-miss sibling in this snapshot is authored. The checker
can report a known but unauthored sibling as unavailable in a future dataset.

The source of the labels is references/disambiguation-map.md, supplemented by
the actual authored definitions and descriptions. Its boundaries are local
repository conventions. The missing-fact annotations are author judgments about
prompt content, not a semantic property proven by the JSON validator.

There are 252 unique prompt strings. Near-misses deliberately reuse authored
siblings' positive prompts to probe both sides of a boundary. The 504 comparisons
are therefore paired and correlated, not independent observations. This English
paraphrase set and keyword heuristic do not measure a real agent's selection
accuracy, calibrate confidence or validate behavior on unseen requests.

## Explicit near-miss priorities

These cases contain the intended distinguishing fact but still rank the target
above its named sibling. They merit human reading before any description change.
Matched keywords and the source descriptions are more informative than the score
alone. Some top-ranked competitors differ from both members of the named pair.

| Case | Evaluated skill | Intended sibling | Target / sibling score | Prompt |
| --- | --- | --- | --- | --- |
| [010 N3](../evals/010-anonymity.json) | anonymity | privacy | 0.085106 / 0.057692 | Limit collection and recipients to the supplied personal-data purpose and propagate withdrawal to every producer and capture path. |
| [013 N3](../evals/013-auditability.json) | auditability | accountability | 0.021739 / 0.000000 | Carry the authenticated initiator and delegated worker separately through the approval job. |
| [026 N3](../evals/026-confidentiality.json) | confidentiality | privacy | 0.080000 / 0.057692 | Limit collection and recipients to the supplied personal-data purpose and propagate withdrawal to every producer and capture path. |
| [041 N3](../evals/041-efficiency-device-efficiency.json) | efficiency-device-efficiency | performance-efficiency-time-or-space-bounds | 0.052632 / 0.024390 | Set an absolute completion-percentile deadline for this operation under a fixed offered workload, with errors and pending outcomes accounted for. |
| [074 N3](../evals/074-predictability.json) | predictability | performance-efficiency-time-or-space-bounds | 0.076923 / 0.024390 | Set an absolute completion-percentile deadline for this operation under a fixed offered workload, with errors and pending outcomes accounted for. |
| [077 N3](../evals/077-quality-of-service.json) | quality-of-service | performance-efficiency-time-or-space-bounds | 0.048780 / 0.024390 | Set an absolute completion-percentile deadline for this operation under a fixed offered workload, with errors and pending outcomes accounted for. |
| [080 N4](../evals/080-recoverability.json) | recoverability | durability | 0.062500 / 0.057692 | Align the confirmed-save response with the promised persistence condition and distinguish valid later supersession from lost state. |
| [081 N3](../evals/081-reliability.json) | reliability | availability | 0.058824 / 0.027027 | Measure good eligible journey time during deploys using the accepted service calendar and explicit unknown bins. |
| [086 N3](../evals/086-robustness.json) | robustness | fault-failure-tolerance | 0.084746 / 0.074074 | Hold a fail-stop worker fault while the alternate path continues the required business result with its state rules intact. |

The absolute-completion-percentile prompt favors Predictability over Performance
because exact words such as absolute, completion and deadline occur in the former,
including its boundary discussion; the latter matches percentile but uses different
word forms elsewhere. This is not evidence that the tail-versus-variation boundary
should be removed. The same prompt appears as a near-miss for Efficiency and QoS.

The delegated-actor prompt gives Accountability no exact retained-keyword overlap,
while Auditability matches approval. Initiator/initiating and delegated/delegation
are examples of forms this scorer does not connect. A zero lexical score therefore
does not establish that Accountability's description lacks the concept.

The personal-data collection prompt overlaps Anonymity and Confidentiality,
including terms that appear in sibling exclusions. Preservation versus restoration
and usable-time versus failure-occurrence also produce explicit lexical warnings.
The descriptions remain unchanged pending semantic review.

## Results split by prompt kind

| Case group | Cases | Intended lead not top | Top ties | No global signal | Target outranks near sibling | Positive near tie | No near-pair signal |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| should_trigger / fact omitted | 126 | 75 | 12 | 7 | 0 | 0 | 0 |
| should_trigger / explicit | 126 | 22 | 3 | 0 | 0 | 0 | 0 |
| near_miss / fact omitted | 126 | 74 | 9 | 3 | 13 | 2 | 38 |
| near_miss / explicit | 126 | 21 | 6 | 0 | 9 | 1 | 0 |

## Every strict near-miss warning

S and N in case links mean should-trigger and near-miss, with one-based JSON
array positions. Clarify cases lack the deciding fact and cannot substantiate a
hard negative verdict. The text CLI emits each warning with its prompt; JSON
output also includes matched keywords, top candidates and clarifying questions.

| Case | Expected behavior | Intended sibling | Target / sibling score |
| --- | --- | --- | --- |
| [005 N1](../evals/005-additivity.json) | clarify | augmentability | 0.033333 / 0.029412 |
| [010 N1](../evals/010-anonymity.json) | clarify | privacy | 0.024390 / 0.022222 |
| [010 N3](../evals/010-anonymity.json) | route | privacy | 0.085106 / 0.057692 |
| [013 N3](../evals/013-auditability.json) | route | accountability | 0.021739 / 0.000000 |
| [026 N1](../evals/026-confidentiality.json) | clarify | privacy | 0.022727 / 0.022222 |
| [026 N3](../evals/026-confidentiality.json) | route | privacy | 0.080000 / 0.057692 |
| [032 N2](../evals/032-customizability.json) | clarify | tailorability | 0.024390 / 0.000000 |
| [039 N1](../evals/039-durability.json) | clarify | atomicity | 0.023256 / 0.000000 |
| [041 N3](../evals/041-efficiency-device-efficiency.json) | route | performance-efficiency-time-or-space-bounds | 0.052632 / 0.024390 |
| [044 N2](../evals/044-expandability.json) | clarify | extendability | 0.032258 / 0.000000 |
| [059 N1](../evals/059-learnability.json) | clarify | trainability | 0.057143 / 0.029412 |
| [061 N2](../evals/061-likeability.json) | clarify | usability | 0.029412 / 0.000000 |
| [074 N3](../evals/074-predictability.json) | route | performance-efficiency-time-or-space-bounds | 0.076923 / 0.024390 |
| [077 N3](../evals/077-quality-of-service.json) | route | performance-efficiency-time-or-space-bounds | 0.048780 / 0.024390 |
| [078 N1](../evals/078-readability.json) | clarify | legibility | 0.076923 / 0.054054 |
| [078 N2](../evals/078-readability.json) | clarify | comprehensibility | 0.038462 / 0.027027 |
| [080 N1](../evals/080-recoverability.json) | clarify | fault-failure-tolerance | 0.025641 / 0.022727 |
| [080 N4](../evals/080-recoverability.json) | route | durability | 0.062500 / 0.057692 |
| [081 N3](../evals/081-reliability.json) | route | availability | 0.058824 / 0.027027 |
| [086 N3](../evals/086-robustness.json) | route | fault-failure-tolerance | 0.084746 / 0.074074 |
| [103 N2](../evals/103-trainability.json) | clarify | comprehensiveness | 0.030303 / 0.000000 |
| [106 N2](../evals/106-understandability.json) | clarify | comprehensiveness | 0.025000 / 0.000000 |

## All flagged lexical pairs

Each row is an unordered pair. Cases counts distinct affected eval cases;
individual flag counts can overlap within a case. Outrank compares a near-miss
target with its intended sibling. Pair tie is positive; no pair signal means both
scores are zero. Not top compares the intended lead with an actual top competitor.
Top tie includes positive tied winners. The sample link identifies one reproducible
case; the CLI/JSON output contains every contributing case identifier.

| Pair | Cases | Outrank | Pair tie | No pair signal | Not top | Top tie | Sample |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| extendability / extensibility | 11 | 0 | 2 | 1 | 0 | 9 | [014 N4](../evals/014-augmentability.json) |
| performance-efficiency-time-or-space-bounds / predictability | 6 | 1 | 0 | 0 | 4 | 2 | [041 N3](../evals/041-efficiency-device-efficiency.json) |
| recoverability / sustainability | 6 | 0 | 0 | 0 | 6 | 0 | [011 N2](../evals/011-atomicity.json) |
| expandability / reconfigurability | 5 | 0 | 0 | 0 | 5 | 0 | [004 N2](../evals/004-adaptability.json) |
| extendability / robustness | 5 | 0 | 0 | 0 | 5 | 0 | [048 N4](../evals/048-fault-failure-tolerance.json) |
| extensibility / robustness | 5 | 0 | 0 | 0 | 5 | 0 | [048 N4](../evals/048-fault-failure-tolerance.json) |
| accountability / changeability | 4 | 0 | 0 | 0 | 4 | 0 | [002 S1](../evals/002-accountability.json) |
| adjustability / changeability | 4 | 0 | 0 | 0 | 0 | 4 | [002 S1](../evals/002-accountability.json) |
| anonymity / privacy | 4 | 2 | 0 | 0 | 3 | 0 | [010 N1](../evals/010-anonymity.json) |
| augmentability / enhanceability | 4 | 0 | 0 | 1 | 3 | 0 | [014 N1](../evals/014-augmentability.json) |
| availability / readability | 4 | 0 | 0 | 0 | 0 | 4 | [014 N1](../evals/014-augmentability.json) |
| availability / recoverability | 4 | 0 | 0 | 1 | 3 | 0 | [015 N2](../evals/015-availability.json) |
| availability / reliability | 4 | 1 | 0 | 2 | 2 | 0 | [015 N1](../evals/015-availability.json) |
| comprehensibility / readability | 4 | 1 | 0 | 0 | 4 | 0 | [018 N2](../evals/018-communicativeness.json) |
| comprehensiveness / trainability | 4 | 1 | 0 | 0 | 4 | 0 | [024 S2](../evals/024-comprehensiveness.json) |
| legibility / readability | 4 | 1 | 0 | 0 | 4 | 0 | [012 N4](../evals/012-attractiveness.json) |
| reliability / scalability | 4 | 0 | 0 | 0 | 4 | 0 | [015 N1](../evals/015-availability.json) |
| additivity / privacy | 3 | 0 | 0 | 0 | 3 | 0 | [010 N1](../evals/010-anonymity.json) |
| anonymity / likeability | 3 | 0 | 0 | 0 | 3 | 0 | [010 S2](../evals/010-anonymity.json) |
| atomicity / durability | 3 | 1 | 0 | 1 | 2 | 0 | [011 N1](../evals/011-atomicity.json) |
| atomicity / modifiability | 3 | 0 | 0 | 0 | 3 | 0 | [008 N2](../evals/008-agility.json) |
| augmentability / sustainability | 3 | 0 | 0 | 0 | 3 | 0 | [005 N1](../evals/005-additivity.json) |
| changeability / comprehensibility | 3 | 0 | 0 | 0 | 3 | 0 | [023 S1](../evals/023-comprehensibility.json) |
| changeability / traceability | 3 | 0 | 0 | 0 | 3 | 0 | [002 N2](../evals/002-accountability.json) |
| changeability / trainability | 3 | 0 | 0 | 0 | 3 | 0 | [017 S2](../evals/017-changeability.json) |
| changeability / usability | 3 | 0 | 0 | 0 | 3 | 0 | [017 S2](../evals/017-changeability.json) |
| confidentiality / customizability | 3 | 0 | 0 | 0 | 3 | 0 | [001 N2](../evals/001-accessibility-access-control.json) |
| customizability / extensibility | 3 | 0 | 0 | 1 | 2 | 0 | [046 N1](../evals/046-extendability.json) |
| durability / recoverability | 3 | 1 | 0 | 1 | 2 | 0 | [039 N2](../evals/039-durability.json) |
| expandability / learnability | 3 | 0 | 0 | 0 | 3 | 0 | [059 S1](../evals/059-learnability.json) |
| fault-failure-tolerance / recoverability | 3 | 1 | 0 | 0 | 3 | 0 | [048 S1](../evals/048-fault-failure-tolerance.json) |
| fault-failure-tolerance / robustness | 3 | 1 | 0 | 0 | 3 | 0 | [048 S3](../evals/048-fault-failure-tolerance.json) |
| learnability / trainability | 3 | 1 | 0 | 1 | 2 | 0 | [059 N1](../evals/059-learnability.json) |
| likeability / usability | 3 | 1 | 0 | 0 | 3 | 0 | [059 N2](../evals/059-learnability.json) |
| maintainability / readability | 3 | 0 | 0 | 0 | 3 | 0 | [063 S1](../evals/063-maintainability.json) |
| modifiability / readability | 3 | 0 | 0 | 0 | 3 | 0 | [043 N1](../evals/043-evolvability.json) |
| trainability / usability | 3 | 0 | 0 | 0 | 0 | 3 | [017 S2](../evals/017-changeability.json) |
| accessibility-access-control / confidentiality | 2 | 0 | 0 | 1 | 1 | 0 | [001 N2](../evals/001-accessibility-access-control.json) |
| accountability / adjustability | 2 | 0 | 0 | 0 | 2 | 0 | [002 S1](../evals/002-accountability.json) |
| accountability / communicativeness | 2 | 0 | 0 | 0 | 2 | 0 | [002 S2](../evals/002-accountability.json) |
| adaptability / availability | 2 | 0 | 0 | 0 | 2 | 0 | [015 S1](../evals/015-availability.json) |
| adaptability / comprehensiveness | 2 | 0 | 0 | 0 | 2 | 0 | [004 S1](../evals/004-adaptability.json) |
| adaptability / flexibility | 2 | 0 | 0 | 2 | 0 | 0 | [004 N1](../evals/004-adaptability.json) |
| adaptability / scalability | 2 | 0 | 0 | 0 | 2 | 0 | [077 N2](../evals/077-quality-of-service.json) |
| adaptability / sustainability | 2 | 0 | 0 | 0 | 2 | 0 | [041 N4](../evals/041-efficiency-device-efficiency.json) |
| adjustability / enhanceability | 2 | 0 | 0 | 0 | 2 | 0 | [006 S1](../evals/006-adjustability.json) |
| adjustability / reliability | 2 | 0 | 0 | 0 | 2 | 0 | [081 S2](../evals/081-reliability.json) |
| agility / reconfigurability | 2 | 0 | 0 | 0 | 2 | 0 | [008 S1](../evals/008-agility.json) |
| atomicity / attractiveness | 2 | 0 | 0 | 0 | 2 | 0 | [011 S2](../evals/011-atomicity.json) |
| attractiveness / likeability | 2 | 0 | 0 | 0 | 0 | 2 | [012 S2](../evals/012-attractiveness.json) |
| availability / enhanceability | 2 | 0 | 0 | 0 | 2 | 0 | [014 N1](../evals/014-augmentability.json) |
| changeability / modifiability | 2 | 0 | 0 | 2 | 0 | 0 | [017 N2](../evals/017-changeability.json) |
| changeability / predictability | 2 | 0 | 0 | 0 | 0 | 2 | [074 S1](../evals/074-predictability.json) |
| communicativeness / self-descriptiveness | 2 | 0 | 0 | 1 | 1 | 0 | [090 N1](../evals/090-self-descriptiveness.json) |
| communicativeness / sustainability | 2 | 0 | 0 | 0 | 2 | 0 | [018 S1](../evals/018-communicativeness.json) |
| conciseness / predictability | 2 | 0 | 0 | 0 | 2 | 0 | [072 N4](../evals/072-performance-efficiency-time-or-space-bounds.json) |
| conciseness / readability | 2 | 0 | 0 | 0 | 2 | 0 | [025 S1](../evals/025-conciseness.json) |
| conciseness / reliability | 2 | 0 | 0 | 0 | 2 | 0 | [081 S4](../evals/081-reliability.json) |
| confidentiality / privacy | 2 | 2 | 0 | 0 | 0 | 0 | [026 N1](../evals/026-confidentiality.json) |
| configurability / safety | 2 | 0 | 0 | 0 | 0 | 2 | [027 S2](../evals/027-configurability.json) |
| customizability / scalability | 2 | 0 | 0 | 0 | 2 | 0 | [032 S2](../evals/032-customizability.json) |
| dependability / maturity | 2 | 0 | 0 | 0 | 2 | 0 | [037 S3](../evals/037-dependability.json) |
| durability / extendability | 2 | 0 | 0 | 0 | 2 | 0 | [039 S2](../evals/039-durability.json) |
| durability / fault-failure-tolerance | 2 | 0 | 0 | 0 | 2 | 0 | [048 S2](../evals/048-fault-failure-tolerance.json) |
| efficiency-device-efficiency / reliability | 2 | 0 | 0 | 0 | 2 | 0 | [041 S2](../evals/041-efficiency-device-efficiency.json) |
| efficiency-device-efficiency / sustainability | 2 | 0 | 0 | 1 | 1 | 0 | [099 N2](../evals/099-sustainability.json) |
| enhanceability / readability | 2 | 0 | 0 | 0 | 2 | 0 | [014 N1](../evals/014-augmentability.json) |
| enhanceability / tailorability | 2 | 0 | 0 | 0 | 2 | 0 | [032 N2](../evals/032-customizability.json) |
| evolvability / sustainability | 2 | 0 | 0 | 0 | 2 | 0 | [042 N2](../evals/042-enhanceability.json) |
| extendability / flexibility | 2 | 0 | 0 | 0 | 2 | 0 | [044 N2](../evals/044-expandability.json) |
| flexibility / scalability | 2 | 0 | 0 | 0 | 2 | 0 | [004 N1](../evals/004-adaptability.json) |
| integrity / scalability | 2 | 0 | 0 | 0 | 2 | 0 | [057 S2](../evals/057-integrity.json) |
| integrity / stability | 2 | 0 | 0 | 0 | 2 | 0 | [074 N2](../evals/074-predictability.json) |
| learnability / usability | 2 | 0 | 0 | 2 | 0 | 0 | [059 N2](../evals/059-learnability.json) |
| legibility / privacy | 2 | 0 | 0 | 0 | 2 | 0 | [012 N2](../evals/012-attractiveness.json) |
| maintainability / modifiability | 2 | 0 | 0 | 1 | 1 | 0 | [063 S2](../evals/063-maintainability.json) |
| maintainability / supportability | 2 | 0 | 0 | 2 | 0 | 0 | [063 N2](../evals/063-maintainability.json) |
| performance-efficiency-time-or-space-bounds / scalability | 2 | 0 | 0 | 0 | 2 | 0 | [044 N3](../evals/044-expandability.json) |
| quality-of-service / security-control-and-security | 2 | 0 | 0 | 0 | 2 | 0 | [086 N2](../evals/086-robustness.json) |
| readability / supportability | 2 | 0 | 0 | 0 | 2 | 0 | [063 N2](../evals/063-maintainability.json) |
| accessibility-access-control / quality-of-service | 1 | 0 | 0 | 0 | 1 | 0 | [001 S1](../evals/001-accessibility-access-control.json) |
| accountability / auditability | 1 | 1 | 0 | 0 | 0 | 0 | [013 N3](../evals/013-auditability.json) |
| accountability / traceability | 1 | 0 | 0 | 1 | 0 | 0 | [102 N2](../evals/102-traceability.json) |
| adaptability / likeability | 1 | 0 | 0 | 0 | 1 | 0 | [004 S2](../evals/004-adaptability.json) |
| additivity / agility | 1 | 0 | 0 | 0 | 1 | 0 | [005 S1](../evals/005-additivity.json) |
| additivity / augmentability | 1 | 1 | 0 | 0 | 0 | 0 | [005 N1](../evals/005-additivity.json) |
| additivity / conciseness | 1 | 0 | 0 | 0 | 1 | 0 | [025 S2](../evals/025-conciseness.json) |
| additivity / readability | 1 | 0 | 0 | 0 | 1 | 0 | [078 S2](../evals/078-readability.json) |
| adjustability / configurability | 1 | 0 | 0 | 1 | 0 | 0 | [027 N1](../evals/027-configurability.json) |
| agility / changeability | 1 | 0 | 0 | 1 | 0 | 0 | [017 N1](../evals/017-changeability.json) |
| agility / maturity | 1 | 0 | 0 | 0 | 1 | 0 | [008 S2](../evals/008-agility.json) |
| agility / modifiability | 1 | 0 | 0 | 1 | 0 | 0 | [008 N2](../evals/008-agility.json) |
| anonymity / confidentiality | 1 | 0 | 0 | 1 | 0 | 0 | [010 N2](../evals/010-anonymity.json) |
| anonymity / maturity | 1 | 0 | 0 | 0 | 1 | 0 | [065 S1](../evals/065-maturity.json) |
| anonymity / supportability | 1 | 0 | 0 | 0 | 0 | 1 | [065 S1](../evals/065-maturity.json) |
| anonymity / sustainability | 1 | 0 | 0 | 0 | 1 | 0 | [010 S1](../evals/010-anonymity.json) |
| atomicity / recoverability | 1 | 0 | 0 | 1 | 0 | 0 | [011 N2](../evals/011-atomicity.json) |
| atomicity / safety | 1 | 0 | 0 | 0 | 1 | 0 | [087 S3](../evals/087-safety.json) |
| attractiveness / legibility | 1 | 0 | 0 | 1 | 0 | 0 | [012 N2](../evals/012-attractiveness.json) |
| auditability / communicativeness | 1 | 0 | 0 | 0 | 1 | 0 | [013 S2](../evals/013-auditability.json) |
| availability / comprehensiveness | 1 | 0 | 0 | 0 | 1 | 0 | [024 S1](../evals/024-comprehensiveness.json) |
| availability / scalability | 1 | 0 | 0 | 0 | 1 | 0 | [015 S4](../evals/015-availability.json) |
| availability / sustainability | 1 | 0 | 0 | 0 | 1 | 0 | [099 S1](../evals/099-sustainability.json) |
| availability / trainability | 1 | 0 | 0 | 0 | 1 | 0 | [103 S2](../evals/103-trainability.json) |
| changeability / learnability | 1 | 0 | 0 | 0 | 1 | 0 | [059 S2](../evals/059-learnability.json) |
| changeability / supportability | 1 | 0 | 0 | 1 | 0 | 0 | [096 N2](../evals/096-supportability.json) |
| comprehensiveness / conciseness | 1 | 0 | 0 | 1 | 0 | 0 | [025 N2](../evals/025-conciseness.json) |
| comprehensiveness / readability | 1 | 0 | 0 | 0 | 1 | 0 | [024 S1](../evals/024-comprehensiveness.json) |
| comprehensiveness / understandability | 1 | 1 | 0 | 0 | 0 | 0 | [106 N2](../evals/106-understandability.json) |
| conciseness / integrity | 1 | 0 | 0 | 0 | 1 | 0 | [057 S3](../evals/057-integrity.json) |
| confidentiality / immunity | 1 | 0 | 0 | 0 | 1 | 0 | [054 S2](../evals/054-immunity.json) |
| customizability / supportability | 1 | 0 | 0 | 0 | 0 | 1 | [096 S1](../evals/096-supportability.json) |
| customizability / tailorability | 1 | 1 | 0 | 0 | 0 | 0 | [032 N2](../evals/032-customizability.json) |
| defensibility / recoverability | 1 | 0 | 0 | 1 | 0 | 0 | [035 N2](../evals/035-defensibility.json) |
| defensibility / safety | 1 | 0 | 0 | 0 | 1 | 0 | [035 S1](../evals/035-defensibility.json) |
| defensibility / survivability | 1 | 0 | 0 | 0 | 1 | 0 | [035 S4](../evals/035-defensibility.json) |
| dependability / reliability | 1 | 0 | 0 | 1 | 0 | 0 | [037 N1](../evals/037-dependability.json) |
| efficiency-device-efficiency / performance-efficiency-time-or-space-bounds | 1 | 1 | 0 | 0 | 0 | 0 | [041 N3](../evals/041-efficiency-device-efficiency.json) |
| evolvability / modifiability | 1 | 0 | 1 | 0 | 0 | 0 | [043 N1](../evals/043-evolvability.json) |
| evolvability / readability | 1 | 0 | 0 | 0 | 1 | 0 | [043 S1](../evals/043-evolvability.json) |
| expandability / extendability | 1 | 1 | 0 | 0 | 0 | 0 | [044 N2](../evals/044-expandability.json) |
| expandability / quality-of-service | 1 | 0 | 0 | 0 | 1 | 0 | [077 S2](../evals/077-quality-of-service.json) |
| flexibility / tailorability | 1 | 0 | 0 | 0 | 1 | 0 | [050 S2](../evals/050-flexibility.json) |
| immunity / susceptibility | 1 | 0 | 0 | 1 | 0 | 0 | [054 N1](../evals/054-immunity.json) |
| integrity / quality-of-service | 1 | 0 | 0 | 0 | 1 | 0 | [057 S1](../evals/057-integrity.json) |
| integrity / security-control-and-security | 1 | 0 | 0 | 1 | 0 | 0 | [089 N2](../evals/089-security-control-and-security.json) |
| likeability / privacy | 1 | 0 | 0 | 0 | 1 | 0 | [075 S2](../evals/075-privacy.json) |
| maturity / reliability | 1 | 0 | 0 | 1 | 0 | 0 | [065 N1](../evals/065-maturity.json) |
| maturity / supportability | 1 | 0 | 0 | 0 | 1 | 0 | [065 S1](../evals/065-maturity.json) |
| performance-efficiency-time-or-space-bounds / quality-of-service | 1 | 1 | 0 | 0 | 0 | 0 | [077 N3](../evals/077-quality-of-service.json) |
| quality-of-service / scalability | 1 | 0 | 0 | 1 | 0 | 0 | [077 N2](../evals/077-quality-of-service.json) |
| readability / trainability | 1 | 0 | 0 | 0 | 1 | 0 | [103 S2](../evals/103-trainability.json) |
| recoverability / reliability | 1 | 0 | 0 | 1 | 0 | 0 | [081 N2](../evals/081-reliability.json) |
| reliability / stability | 1 | 0 | 0 | 1 | 0 | 0 | [092 N2](../evals/092-stability.json) |
| safety / supportability | 1 | 0 | 0 | 0 | 1 | 0 | [087 S1](../evals/087-safety.json) |
| safety / susceptibility | 1 | 0 | 0 | 0 | 1 | 0 | [098 S2](../evals/098-susceptibility.json) |
| security-control-and-security / trustability | 1 | 0 | 0 | 0 | 1 | 0 | [105 S1](../evals/105-trustability.json) |
| self-descriptiveness / susceptibility | 1 | 0 | 0 | 0 | 1 | 0 | [098 S4](../evals/098-susceptibility.json) |
| self-descriptiveness / traceability | 1 | 0 | 0 | 0 | 1 | 0 | [102 S1](../evals/102-traceability.json) |

## Execution and verification

The full text and JSON commands completed successfully. The text output emits
every flagged pair and each strict near-miss comparison. --only 41,72,74,77,88,99
evaluated 48 prompts against all 63 authored candidates, with 24 omitted-fact
cases. Selecting todo id 3 was rejected with exit code 2. Evaluation warnings
leave exit code 0; malformed or missing input fails with exit code 2.

The commands used are reproducible from the repository root:

~~~text
python scripts/check_descriptions.py
python scripts/check_descriptions.py --json
python scripts/check_descriptions.py --only 41,72,74,77,88,99 --json
python -m unittest discover -s tests -v
python scripts/validate_skills.py
~~~

The test suite has 28 passing tests: 19 existing foundation tests and nine new
synthetic checker tests. Coverage includes exact overlap, stop words, ties,
zero-signal handling, strict near-miss warnings, absent sibling descriptions,
--only selection versus competitors, input/label validation, read-only behavior,
determinism and CLI output/exit handling. These tests do not certify the semantic
labels or demonstrate an NFR implementation.

Full skill validation checked 63 skills and 51 absent todo entries with zero
errors. No skill, description, catalogue, reference contract, index or production
batch was changed. No full-catalogue Phase 5 completion or release is claimed.

## Uncertain claims and human review

Vague prompts can support several skills because the acceptance fact is absent;
Ask the user before treating a provisional lead as established. Explicit prompts
can still involve more than one legitimate NFR, so their negative labels deserve
review too. Near-miss selection covers authored siblings rather than every
catalogue boundary. Uncovered sibling boundaries include later accuracy,
composability, observability, conformance and business-fitness concerns. No candidate
description or eval file was manufactured for those todo entries, and no result
establishes routing quality against their unwritten descriptions.

Negation, word forms, generic vocabulary and description length can produce
lexical artifacts. The long pre-revision descriptions and shortened batch-10
descriptions have different token-set sizes, which affects Jaccard. Reused prompts
also make pair frequencies sensitive to the chosen eval graph. No threshold or
automated wording change was used to hide these findings. Semantic agent tests
and stakeholder clarification are still required to resolve the flagged pairs.
