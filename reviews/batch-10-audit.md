# Batch 10 audit

## Scope and basis

This source-based skeptical review covers ids 41, 72, 74, 77, 88 and 99: each
SKILL.md and both directly linked references. The authoring guide, quality rubric
and disambiguation map supply the acceptance contract. No file in reviews/ was
read as audit evidence. This is not a blinded review: the reviewing agent also
has the preceding authoring context. Skills, catalogue, index and tooling are unchanged.

## Principal findings

- **Material authoring weakness: implementation decisions are thinner than measurement decisions.**
  Every design guide contains genuine use-when / trade-off / verify content, not
  empty headings. However, most entries establish boundaries, accounting or
  evidence. Performance names queries, reuse and concurrency without choosing
  an intervention from observed evidence. Predictability says to inspect an
  exceptional path without demonstrating how to bound its work. QoS says to
  revise scheduling/admission without a worked scheduling policy. Scalability
  locates shared/serial/skew problems without a concrete remediation experiment.
  These are useful assessment skills, but less complete implementation guides
  than their Design/Implement headings and descriptions suggest.
- **Material specificity weakness: low text similarity does not establish distinct rules.**
  The full transfer test below finds 20 transferable, 11 partly transferable and
  3 specific rules. This is a strict editorial judgment, not a validator result.
  Shared measurement safeguards can be necessary; necessity alone does not meet
  the guide's stronger requirement that Rules of thumb distinguish the NFR.
  This finding concerns acceptance logic, not a request to remove safeguards
  from workflows or verification.
- **Concrete diagnostic overclaim in the QoS example.** The title calls batch
  work "starved", but the fixture supplies zero completions in an eligible
  minute, not actual scheduling, wait or service observations. The proposed
  completion minimum fails correctly; starvation is not established. A long
  running job or failed execution could also produce that completion count.
  `077-quality-of-service/references/worked-example.md` therefore establishes
  a failed contract more strongly than it establishes its named cause.
- **Routing remains context-dependent, especially latency tails versus variation.**
  Performance accepts percentile bounds and Predictability accepts outliers.
  A vague tail-latency complaint does not identify which acceptance question
  matters. Descriptions contain useful exclusions, but cannot supply the missing
  distinction. The routing findings below retain ties rather than invent intent.
- **The Sustainability scope is broader than its demonstrated depth.** The
  description promises useful device life and lifecycle tradeoffs, but the
  only filled example and numeric fast path concern operational energy. The
  device-life branch delegates usable-service/horizon criteria to the user;
  it does not demonstrate a repository change and its lifecycle evidence.

## Full Rules of thumb transfer test

Bullet numbers follow each skill's Rules of thumb in source order. Quoted text
is the opening of the actual bullet. Transferable means the whole original
bullet could serve the named sibling unchanged. Partly means its technique
transfers but its acceptance framing remains tied to the current skill.
Specific means the nearest sibling would need a different acceptance question.
Sibling meanings below follow the repository map, not standardized definitions.

### 041 efficiency-device-efficiency

| Bullet and source opening | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. "Do divide by correct useful results rather than attempts" | sustainability | Transferable | The exact denominator guard applies to the energy-per-correct-report example. |
| 2. "Don't call a faster implementation more resource-efficient without measuring consumption" | sustainability | Transferable | Elapsed speed alone also cannot establish the resource saving used to justify a stewardship option. |
| 3. "Do include cache fill, retries and background work under the agreed boundary" | sustainability | Transferable | The same omitted-work boundary can fabricate an energy-per-result saving without any wording change. |
| 4. "Do keep CPU time, transferred bytes and peak retained space as distinct measures" | performance-efficiency-time-or-space-bounds | Transferable | An operation's space and other resource constraints also cannot compensate for one another without an agreed rule. |
| 5. "Don't infer energy, emissions or monetary savings from a CPU ratio alone" | sustainability | Transferable | This is directly the sibling's proxy-versus-objective evidence rule. |

Counts: 5 transferable; 0 partly; 0 specific. The ratio denominator defines this
skill, but does not alone make a rule exclusive to it: Sustainability deliberately
uses the same functional-unit mechanism for a different objective.

### 072 performance-efficiency-time-or-space-bounds

| Bullet and source opening | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. "Do time through the required result, including queues inside the chosen boundary" | quality-of-service | Transferable | Per-class elapsed-time contracts need the identical completion boundary. |
| 2. "Don't remove timeouts, rejects or unfinished work from a favorable latency story" | scalability | Transferable | A successful subset also cannot establish the offered-work contract at a growth point. |
| 3. "Do retain the percentile method and raw samples" | predictability | Transferable | Tail/outlier interpretation has the same raw-sample and aggregation hazard. |
| 4. "Do distinguish requested arrivals, active concurrency and completed throughput" | scalability | Transferable | Generator slowdown can hide the very growth envelope that the sibling tests. |
| 5. "Do inspect space under the actual data and concurrency envelope" | efficiency-device-efficiency | Transferable | The sibling preserves space constraints and needs the same loaded peak-space check alongside a resource ratio. |

Counts: 5 transferable; 0 partly; 0 specific. All are useful, concrete practices;
their placement does not demonstrate that this skill's rules are distinctive.

### 074 predictability

| Bullet and source opening | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. "Don't replace raw extremes with a stable average" | performance-efficiency-time-or-space-bounds | Transferable | A mean can equally conceal cases that violate an operation's timing envelope. |
| 2. "Do compare meaningful condition groups before blaming variability" | performance-efficiency-time-or-space-bounds | Partly | Stratification transfers, but diagnosing unexplained spread rather than testing an absolute bound supplies this bullet's framing. |
| 3. "Do preserve timeouts and unfinished work beside completed observations" | performance-efficiency-time-or-space-bounds | Transferable | A completed-only sample can manufacture a favorable operation latency result too. |
| 4. "Don't call uniform slowness acceptable solely because spread improved" | performance-efficiency-time-or-space-bounds | Partly | Preserving an independent deadline transfers, while rejecting spread-only acceptance specifically answers Predictability's tradeoff. |
| 5. "Do predeclare window and outlier exclusions" | performance-efficiency-time-or-space-bounds | Transferable | Post-hoc exclusion of pauses can also change a percentile-bound contract instead of meeting it. |
| 6. "Do trace rare variable-work paths, not only the usual hotspot" | performance-efficiency-time-or-space-bounds | Partly | Exceptional-path tracing transfers, but unchanged surprise after a typical-path improvement is explicitly the variation acceptance question. |

Counts: 3 transferable; 3 partly; 0 specific.

### 077 quality-of-service

| Bullet and source opening | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. "Don't use an aggregate latency pass to accept every service class" | performance-efficiency-time-or-space-bounds | Specific | Independent treatment of multiple classes is the map's QoS criterion, rather than one operation envelope. |
| 2. "Do test lower-class progress under sustained favored-class demand" | performance-efficiency-time-or-space-bounds | Specific | Lower-versus-favored progress under contention requires the differentiated-class acceptance question. |
| 3. "Don't apply strict priority blindly when another class has a positive minimum" | performance-efficiency-time-or-space-bounds | Specific | Conflicting class obligations are the actual acceptance issue, not merely latency measurement hygiene. |
| 4. "Do derive class entitlement from the trusted policy source" | accessibility-access-control | Transferable | Trusted entitlement rather than a caller's asserted privilege fits the map's access-control branch unchanged. |
| 5. "Do inspect downstream shared pools after separating ingress queues" | performance-efficiency-time-or-space-bounds | Partly | End-to-end bottleneck inspection transfers, while loss of promised class differentiation is QoS-specific framing. |
| 6. "Do count admitted, rejected and unfinished work by class" | performance-efficiency-time-or-space-bounds | Partly | Outcome accounting transfers, while deciding whether class-selective rejection violates treatment needs the class policy. |

Counts: 1 transferable; 2 partly; 3 specific. This is the strongest rule set in
the batch under the strict acceptance-question test.

### 088 scalability

| Bullet and source opening | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. "Do name the growing dimension and held conditions" | performance-efficiency-time-or-space-bounds | Partly | Explicit workload dimensions transfer, but confusing stored-account growth with active-demand growth concerns the curve being accepted. |
| 2. "Don't call resource admission a successful growth curve" | expandability | Partly | The admission-versus-service distinction is shared, but accepting the growth curve is outside the sibling's narrower admission question. |
| 3. "Do keep offered work, completed work and backlog together at each point" | performance-efficiency-time-or-space-bounds | Transferable | The same backlog deficit invalidates a throughput envelope, including repeated fixed-load points. |
| 4. "Do label resource changes separately from workload changes" | efficiency-device-efficiency | Partly | Matched resource/workload accounting transfers, while hidden fixed-resource saturation frames a growth-curve question. |
| 5. "Do exercise declared hot-key/tenant skew, not just evenly spread work" | performance-efficiency-time-or-space-bounds | Transferable | Skewed data can violate an operation envelope under a fixed offered load as well. |
| 6. "Don't extrapolate linear improvement beyond the tested range" | predictability | Partly | Finite-evidence caution transfers, but linear resource gains and coordination specifically concern the growth model. |

Counts: 2 transferable; 4 partly; 0 specific.

### 099 sustainability

| Bullet and source opening | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. "Don't equate lower CPU, a smaller bill or newer hardware with environmental improvement" | efficiency-device-efficiency | Transferable | The sibling already needs this exact limitation on conclusions from a resource optimization. |
| 2. "Do keep useful output and quality fixed in the comparison" | efficiency-device-efficiency | Transferable | The same unchanged functional unit is required to interpret a resource-per-useful-result saving. |
| 3. "Do include idle/shared-device allocation and displaced work within the declared boundary" | efficiency-device-efficiency | Transferable | This is the same accounting-boundary safeguard as that sibling's background-work rule. |
| 4. "Don't convert energy to emissions using an invented factor" | efficiency-device-efficiency | Transferable | The complete prohibition also belongs unchanged beside the sibling's explicit energy/emissions conversion limitation. |
| 5. "Do separate operational savings from acquisition/replacement/retirement effects" | efficiency-device-efficiency | Partly | Keeping claims within measured scope transfers, but acquisition and retirement require lifecycle evidence beyond the sibling's device ratio. |
| 6. "Do test service adequacy when extending device life" | efficiency-device-efficiency | Partly | Preserved useful service transfers, but retaining equipment over a service-life horizon is the stewardship acceptance question. |

Counts: 4 transferable; 2 partly; 0 specific. Lifecycle framing is the strongest
boundary here; the worked example exercises only the shared operational ratio.

## Description findings

Lengths count the parsed, folded description, excluding YAML indentation. All
are within the repository limit and contain three quoted natural trigger phrases.
All explicit sibling slugs resolve to catalogue entries. Catalogue membership
does not mean every destination already has an authored body.

| Id | Characters | Semantic trigger overlap and boundary quality |
| --- | ---: | --- |
| 41 | 511 | Resource-use improvement can also imply Sustainability or a Performance space constraint. Explicit exclusions distinguish resource ratio from those objectives and Scalability; the bare word efficiency remains ambiguous by the map's own warning. |
| 72 | 508 | "make this endpoint faster" and response-time budgets overlap Predictability's long pauses and QoS's interactive target. Excludes variation alone, ratio alone and class differentiation; workload-growth exclusion is in the body rather than the description. |
| 74 | 484 | "stop rare long pauses from surprising callers" equally suggests a tail-latency bound. Excludes a central timing target, Stability and Variability, but does not fully resolve a percentile bound versus an outlier/variation requirement. |
| 77 | 531 | "protect interactive work from batch jobs" provides the distinguishing contention fact, so routes strongly. Generic "make interactive fast" would not. Explicit operation/growth/access exclusions are useful. |
| 88 | 548 | "handle twice the users without losing service quality" implies growth but leaves users undefined. Strong exclusions cover resource admission, fixed-load timing and device ratios; the first question must operationalize the growing axis. |
| 99 | 509 | "reduce energy for this workload" overlaps device efficiency's possible resource measurement. The explicit environmental/stewardship objective and ratio-only exclusion are the deciding facts; generic greener/efficient requests remain unresolved. |

The descriptions do not enumerate exclusions against every cluster member.
That alone is not a defect: the material omission is the tail/outlier ambiguity,
not the absence of an exhaustive sibling list within a short description.

## Routing findings

These are manual semantic probes, not measured model routing accuracy. A tentative
lead is not an exclusive winner where the prompt omits the acceptance distinction.

| Prompt | Best fit / tie | Reason and first question |
| --- | --- | --- |
| "make this faster" | 72 tentative; 74 possible | No variation or class fact is supplied. Ask the user: which completed operation is slow, and is the concern its elapsed bound or inconsistent outcomes? |
| "our p95 is too high" | 72 / 74 unresolved | Both an operation percentile bound and unusual tail behavior fit. Ask the user: do you need an absolute latency limit, a variation/outlier rule, or both under which workload? |
| "stop the random long pauses" | 74 tentative; 72 also fits | Variation language favors 74, but a deadline may be the actual requirement. Ask the user: is success reduced spread under comparable conditions or meeting a completion deadline? |
| "use less memory" | 41 / 72 unresolved | Consumption per useful output and an operation's peak-space ceiling are different requirements. Ask the user: lower memory per useful result, or stay within a peak-space bound under a stated concurrency/data load? |
| "use the cores better" | No exclusive winner; 41 / 72 / 88 plausible | Utilization does not identify resource cost, completion speed or growth. Ask the user: which useful-result, elapsed-time or workload-growth outcome should improve? |
| "keep interactive work fast" | 72 tentative; 77 conditional | No competing class is named. Ask the user: does interactive work compete with a distinct class that also has a treatment obligation? |
| "batch jobs block checkout" | 77 tentative; 72 also relevant | Named interfering workloads favor class treatment, but the desired batch obligation is absent. Ask the user: what must checkout and batch each receive under shared-resource contention? |
| "support larger imports" | 72 / 88 unresolved | One large operation's envelope differs from behavior across growing data sizes. Ask the user: is acceptance a bound for a specified import size or a service/resource curve as sizes grow? |
| "add more workers" | No batch-10 winner; expandability tentative | Resource admission alone is batch 1's acceptance question. Ask the user: add usable capacity, or establish how service changes as demand and resources grow? |
| "handle more users" | 88 tentative; 72 possible | Growth is implied, but idle accounts, active sessions and arrivals differ. Ask the user: which user-related workload dimension grows and which service bounds must remain acceptable? |
| "make the service greener" | 99 tentative; objective unresolved | Stewardship language selects a conversation, not a metric. Ask the user: which environmental or service-life objective and evidence boundary should determine success? |
| "reduce CPU per valid report" | 41 | Useful output and resource unit are explicit. Ask the user: which workload, accounting boundary and required report quality/service constraints define the comparison? |
| "extend the useful life of our devices" | 99 | Device service life supplies the lifecycle fact. Ask the user: what useful service must those devices continue delivering, over what horizon, and what replacement evidence is available? |

## Workflow and repository action findings

All six Clarify steps explicitly inspect existing code and documentation before
specification. Every named step contains an explicit If/then decision. The fast
paths provide a single proposed record with illustrative defaults. They ask
three groups of questions, not necessarily only three atomic questions; each
group bundles multiple stakeholder decisions. This can still be a heavy intake.

| Id | Concrete repository work actually supported | Remaining gap |
| --- | --- | --- |
| 41 | Inspect resource paths and retries/background work; profile matched runs; validate useful results; investigate reuse/batching. | No filled reuse/batch intervention demonstrates retained state, invalidation or cost allocation before and after a change. |
| 72 | Inspect code/queries/queues; correct timer anchors; generate load; retain raw outcomes; measure scoped space. | Fix selection is largely generic critical-path inspection; mixed failed/rejected/unfinished outcomes have no filled acceptance example. |
| 74 | Group traces; correlate rare branches; repeat conditions; check variation and absolute constraints. | No concrete rare-path change is worked through to a valid improved result. |
| 77 | Inspect trusted class mapping and scheduler/pools; exercise contention and forged labels; retain per-class results. | The agent is told to revise admission/scheduling but receives no concrete policy choice and state-transition example. |
| 88 | Exercise declared demand points; inspect partitions/shared work; compare resource series and backlog. | The example diagnoses no actual limiting path and demonstrates no remediation/resource-response comparison. |
| 99 | Inspect resource/device evidence; compare measured operational energy; check preserved service and displaced consumption. | Device-life implementation and lifecycle evidence remain much less developed than the energy ledger. |

No skill is merely planning/status work. Their strongest executable contribution
is measurement and acceptance integrity; the principal gap is positive design depth.

## Guides, examples and counts

Line counts include blank lines. Body counts exclude frontmatter; combined counts
include the full SKILL.md and its two linked references. Every reference is below
150 lines; every combined footprint is inside the 150-250 guideline.

| Id | Body | Full SKILL.md | Design guide | Example | Combined | Rules / done / failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 41 | 119 | 124 | 35 | 35 | 194 | 5 / 7 / 5 |
| 72 | 121 | 126 | 43 | 35 | 204 | 5 / 7 / 6 |
| 74 | 121 | 126 | 35 | 33 | 194 | 6 / 7 / 5 |
| 77 | 125 | 130 | 35 | 35 | 200 | 6 / 8 / 5 |
| 88 | 121 | 126 | 35 | 35 | 196 | 6 / 7 / 5 |
| 99 | 124 | 129 | 35 | 35 | 199 | 6 / 7 / 5 |

Predictability, Scalability and Sustainability have identical complete count
triples. Five skills have seven done items and five failure modes. Five guides
have exactly 35 lines and four practice sections; Performance has five practices
in 43 lines. This is evidence of a shared editorial shape, not proof of author
intent. Some counts have content justification: QoS separates class assignment,
eligibility and independent class acceptance; Performance adds a distinct
load-generator failure. Repeated accounting/window/boundary checks show less
distinctive content even where the wording differs.

The done items mostly identify evidence that can be inspected, rather than
restating the five workflow headings. Some bundle distinct checks: Performance's
last item combines correctness and disclosure; Sustainability's scope/source and
lifecycle limitations require more than one observation. A matching count alone
does not demonstrate filler or independent verification coverage.

### Example evidence

- **41:** Concrete CPU totals, correct-result counts and computed ratios;
  accounting scope/config is named but not filled. The missing-result designation
  is asserted by the fixture, not derivable from the result count alone without
  the offered-input set and end-of-window state. No actual reuse/cache state or
  before/after implementation is supplied. More than a checklist, but primarily
  an arithmetic acceptance counterexample.
- **72:** Concrete completion distribution, declared nearest-rank method,
  acceptance-versus-artifact checkpoints and a valid pooled-percentile
  counterexample. This has the strongest explicit carried result state. The
  rejected/unfinished row is hypothetical outside the numeric set, so the
  default's mixed-outcome acceptance policy is not exercised. The text correctly
  leaves that policy unresolved instead of declaring a whole-workload pass.
- **74:** Concrete raw timing lists, spread results and independent deadline.
  Conditions are requested, not populated; the rare-path cause is hypothetical.
  The example successfully rejects a uniformly slow candidate but does not
  demonstrate an acceptable implementation or reproducible conditional fixture.
- **77:** Concrete class outcomes and independent acceptance results. Trusted
  classification, cap, mix and eligibility are carried-state categories without
  filled queue/scheduling transitions. Failed completion progress is supported;
  diagnosed starvation is not. "Unconstrained downstream pool" is also unclear
  in a contention investigation: the example does not identify what could limit it.
- **88:** Concrete offered/completed rates, accumulating deficit and timing at
  multiple points. Fixed resources and no rejections are stated; actual resource
  amount, duration and backlog endpoints are not filled. The text properly
  refuses to infer a specific bottleneck from the plateau. No added-resource
  series demonstrates the other advertised comparison branch.
- **99:** Concrete energy/output ratios with clear operational-versus-lifecycle
  limits. Meter source, horizon and idle allocation remain unfilled categories.
  The calculation is structurally close to Efficiency's ratio example, with a
  different objective and valid additional interpretation limits. No filled
  device-life case exercises the other major scope branch.

## Three weakest passages per skill

These are editorial weaknesses in the current sources, not unsupported claims
that the cited practices are technically wrong.

| Id | Passage | Weakness |
| --- | --- | --- |
| 41 | SKILL.md: "Compare `{baseline_and_candidate}` on `{matched_inputs_and_conditions}`" | The Equivalent work pattern specifies a comparison procedure without itself supplying an acceptance target or decision rule. |
| 41 | design-patterns.md: "Use when repeated computation or transfers suggest cache/reuse/batch candidates." | Names candidate families but does not help choose one or carry its correctness/accounting state through an intervention. |
| 41 | SKILL.md: "Do keep CPU time, transferred bytes and peak retained space as distinct measures" | A sound general metric/constraint safeguard that transfers unchanged to Performance. |
| 72 | design-patterns.md: "Use when queries, repeated work, dependencies or serialization occupy measured time." | A list of locations to investigate rather than a concrete practice for changing the dominant path. |
| 72 | SKILL.md: "If a candidate trades memory, correctness or rejected work for speed, then check the confirmed constraints" | Rejects an invalid speedup but gives little positive guidance for a valid design choice. |
| 72 | worked-example.md: "resolve their acceptance policy before claiming the whole offered-work envelope passed." | Correctly leaves a gap open, but the only filled example never shows how the verdict changes with mixed outcome classes. |
| 74 | design-patterns.md: "correlate raw slow cases with actual execution paths and compare the same condition groups after the change" | Assumes a change without demonstrating a bounded-work or other concrete intervention. |
| 74 | SKILL.md: "Do predeclare window and outlier exclusions" | A transferable measurement-integrity rule, not distinctive variation design advice. |
| 74 | worked-example.md: "Retain input/data, load, device/config and warm-state group for each trace." | States carried-state fields but fills none, limiting reproducibility of the example's conditional comparison. |
| 77 | SKILL.md: "revise admission/scheduling or negotiate the conflicting contract" | Offers the right categories of response without a concrete selection rule or viable mechanism example. |
| 77 | worked-example.md title: "Interactive latency with starved batch work" | Claims a cause that the completion-only numeric trace does not establish. |
| 77 | worked-example.md: "If separate ingress queues recombine at an unconstrained downstream pool, inspect that pool" | Unconstrained is ambiguous here; no demonstrated bottleneck explains why this pool would erase treatment. |
| 88 | SKILL.md: "inspect shared state, serial work and demand distribution" | A diagnostic search list, with no next implementation decision after a cause is confirmed. |
| 88 | design-patterns.md: "compare useful outcomes and retain shared-state/coordination constraints" | Important evidence, but not a concrete fixed-versus-added-resource intervention. |
| 88 | worked-example.md: "Keep the resource amount fixed for this series." | The fixture never fills that resource amount or observation duration, leaving its load curve underspecified for reproduction. |
| 99 | SKILL.md: "specify usable-service and retirement evidence with the user rather than imposing the energy target." | An honest boundary, but much weaker execution guidance than the energy branch despite the description's device-life promise. |
| 99 | design-patterns.md: "leave net impact unknown where evidence does not cover replacement or retirement." | Correct reporting restraint; it does not show a concrete service-life option or an evidence-backed comparison. |
| 99 | worked-example.md: "Retain the hypothetical meter source, worker boundary, period, idle allocation" | The example names required provenance/allocation state without supplying it. |

## Verification and uncertainties

- Selected validation: `python scripts/validate_skills.py --only 41,72,74,77,88,99`
  checked 6 skills, 0 absent todo skills, 0 errors.
- Full validation: `python scripts/validate_skills.py` checked 63 skills, 51 absent
  todo skills, 0 errors. Absent todo entries are not completed skills.
- Independent arithmetic assertions passed for the CPU ratios/reduction,
  operational-energy ratio/reduction, both percentile fixtures, both observed
  ranges and the offered-minus-completed rates. No actual workload, resource,
  scheduler, lifecycle or environmental test was performed.
- Numeric example targets and observations are explicitly illustrative and paired
  with confirmation language. No unlabeled universal system target was found.
  No external URLs, edition/characteristic claims or new standard citations
  were found in these skill sources.
- Transfer classifications and routing ties are reviewer judgments from local
  boundaries, not empirically validated agent behavior. Count symmetry cannot
  establish whether the author wrote to a target shape. Actual capacity,
  environmental impact and feasibility of illustrative obligations remain unknown.
- No skills were changed, no threshold was changed and no later batch was started.
