# Batch 10 findings

## Description-first routing and scope

Six descriptions were authored before bodies. The shared authoring guide, rubric,
allowlist, complete disambiguation map and approved pilot entrypoints supplied the
contract; adjacent Expandability and Stability descriptions were also inspected.
Earlier skills and pilots remain unchanged, and previous approvals do not promote
draft statuses to reviewed. Catalogue aliases and categories are preserved.

The overlapping Efficiency alias does not merge ids 41 and 72. The comparison
below is manual semantic routing, not a model test or the later keyword heuristic.

| Request | Best fit / ambiguity | Acceptance question and first missing fact |
| --- | --- | --- |
| Make this more efficient | efficiency-device-efficiency / performance-efficiency-time-or-space-bounds unresolved | Resource per useful result, elapsed-time/space ceiling, or another objective? |
| Use less CPU per completed report | efficiency-device-efficiency | Which useful result, resource scope, background work and comparable workload? |
| Keep peak memory below our operation budget | performance-efficiency-time-or-space-bounds | What operation, concurrent workload, measurement boundary and confirmed ceiling? |
| Make this endpoint faster | performance-efficiency-time-or-space-bounds | Which result, offered load, start/end anchors and latency/throughput criterion? |
| It is fast on average but sometimes stalls | predictability | Which conditional variation/outlier limit and treatment of timeouts or unfinished work? |
| Stop the controller flapping | stability outside batch | Drift/reversals and held/changed conditions, not general completion-time variation. |
| Interactive jobs must not wait behind batch | quality-of-service | Which trusted classes, shared constraint, admitted load and obligations for both classes? |
| Give one tenant a better tier | quality-of-service / accessibility-access-control unresolved | Scheduling/service treatment or permission/entitlement policy? |
| Add more workers | expandability outside batch | Admission/placement of resources, unless the goal is the demand/resource growth curve. |
| Handle ten times the users | scalability | Which workload axis, resource policy and required result/quality at each point? |
| Throughput plateaus as demand rises | scalability | Offered versus completed work, backlog, skew and fixed-resource policy? |
| Reduce energy per useful report | sustainability, efficiency may contribute | Which measured energy boundary, functional output and stewardship objective? |
| Lower the cloud bill | affordability outside batch; efficiency may contribute | Financial budget, resource ratio or environmental/lifecycle objective? |
| Delay replacing these devices | sustainability if stewardship is intended | Which useful life, workload/service requirements, horizon and lifecycle tradeoffs? |
| The system should remain worthwhile | viability outside batch | Continued stakeholder value is not automatically an environmental stewardship goal. |

Bare efficiency, better tier, and generic savings remain clarification cases.
The new descriptions use distinct natural trigger phrases and name real nearest
sibling slugs. Sustainability does not infer energy, emissions or lifecycle
benefit from CPU, cost or newer equipment alone.

## Full rule transfer findings

Every Rules of thumb bullet is quoted and compared with the nearest plausible
sibling in the repository map. Transferable means the whole instruction can move
unchanged; partly means a shared mechanism with a different acceptance scope;
specific means the nearest tested sibling can legitimately accept a different
result. These are manual judgments, not independent agent or benchmark evidence.

### 041-efficiency-device-efficiency

**Bullet 1: partly; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Do divide by correct useful results rather than attempts; dropping required results can reduce total CPU while leaving resource per valid outcome unchanged or worse.

A performance envelope also needs correct completions, but resource per valid outcome is a different acceptance metric from useful throughput or elapsed time.

**Bullet 2: specific; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Don't call a faster implementation more resource-efficient without measuring consumption; parallel work can change elapsed time without reducing the chosen resource total.

Performance may legitimately improve elapsed time without reducing resource consumption; this rule rejects using that improvement alone as the resource-efficiency verdict.

**Bullet 3: transferable; nearest sibling `sustainability`.**

> Do include cache fill, retries and background work under the agreed boundary; moving consumption outside the foreground timer can fabricate a per-result saving.

A stewardship comparison also needs background, retry and displaced work inside its declared functional-unit boundary; this whole accounting instruction transfers.

**Bullet 4: transferable; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Do keep CPU time, transferred bytes and peak retained space as distinct measures; an improvement in one dimension cannot silently compensate for another required bound.

Independent memory, traffic and CPU bounds also cannot be silently traded in a performance contract, so the complete dimension-separation instruction applies unchanged.

**Bullet 5: transferable; nearest sibling `sustainability`.**

> Don't infer energy, emissions or monetary savings from a CPU ratio alone; those claims need their own objective, boundary and supported conversion evidence.

Sustainability likewise cannot infer measured energy or emissions from CPU alone, making this whole conversion-evidence safeguard reusable.

Count: 3 transferable, 1 partly, 1 specific.

### 072-performance-efficiency-time-or-space-bounds

**Bullet 1: transferable; nearest sibling `availability`.**

> Do time through the required result, including queues inside the chosen boundary; moving work after an early success response can hide the latency the user needs bounded.

The approved pilot also binds usable service to the required result and deadline; timing through queued/downstream completion can serve that check unchanged.

**Bullet 2: transferable; nearest sibling `scalability`.**

> Don't remove timeouts, rejects or unfinished work from a favorable latency story; a fast successful subset does not establish the offered-work contract.

A growth trial also cannot hide rejected or unfinished demand behind fast completions; the whole offered-work instruction transfers.

**Bullet 3: transferable; nearest sibling `predictability`.**

> Do retain the percentile method and raw samples; averaging per-instance percentiles cannot substitute for calculating the agreed statistic over the eligible observation set.

A distribution/variation review using percentiles also needs the raw set and declared calculation rather than averaged summaries, so this whole rule transfers.

**Bullet 4: transferable; nearest sibling `scalability`.**

> Do distinguish requested arrivals, active concurrency and completed throughput; slowing the load source can hide the queueing envelope that produced the complaint.

A scaling curve can also be falsified by a slowing arrival source, making this full demand/concurrency/completion distinction reusable.

**Bullet 5: partly; nearest sibling `efficiency-device-efficiency`.**

> Do inspect space under the actual data and concurrency envelope; a small-input single-call peak cannot establish the simultaneous loaded operation's memory ceiling.

Matching data and concurrency matters to resource comparisons too, but the whole statement specifically rejects inadequate evidence for a peak-space ceiling.

Count: 4 transferable, 1 partly, 0 specific.

### 074-predictability

**Bullet 1: transferable; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Don't replace raw extremes with a stable average; similar means can conceal very different surprises in the individual completion outcomes the user needs bounded.

A latency contract also cannot use a favorable mean to hide relevant slow observations, so this raw-extreme instruction transfers unchanged.

**Bullet 2: transferable; nearest sibling `stability`.**

> Do compare meaningful condition groups before blaming variability; cold starts and cached repeats may answer different conditional questions rather than one unexplained spread.

A drift/oscillation review also must distinguish changed conditions from unexplained within-condition behavior; the full conditional-comparison instruction applies unchanged.

**Bullet 3: transferable; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Do preserve timeouts and unfinished work beside completed observations; dropping the slowest unknown outcomes can manufacture a narrow observed range.

A deadline/distribution check likewise needs unfinished and timed-out observations visible, making the entire censoring rule reusable.

**Bullet 4: transferable; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Don't call uniform slowness acceptable solely because spread improved; predictable completion can still violate the independent absolute deadline.

Uniformly slow completion also fails an independent performance deadline, so this full paired-metric safeguard transfers unchanged.

**Bullet 5: transferable; nearest sibling `repeatability`.**

> Do predeclare window and outlier exclusions; deleting inconvenient pauses after observation changes the variability contract instead of meeting it.

Consistent-result procedures also cannot choose favorable windows/exclusions after observation, so this complete protocol rule transfers.

**Bullet 6: transferable; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Do trace rare variable-work paths, not only the usual hotspot; eliminating typical cost can leave the exceptional branch that dominates the surprise unchanged.

Tail-latency investigation also needs rare costly paths rather than only usual hotspots; the full exceptional-path instruction transfers.

Count: 6 transferable, 0 partly, 0 specific.

### 077-quality-of-service

**Bullet 1: partly; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Don't use an aggregate latency pass to accept every service class; one class can satisfy it while another violates its own declared treatment.

Performance may inspect subpopulations, but this rule accepts independently differentiated service-class contracts rather than one operation envelope.

**Bullet 2: partly; nearest sibling `scalability`.**

> Do test lower-class progress under sustained favored-class demand when that progress is required; an idle favored queue cannot expose starvation.

Rising-load trials can reveal starvation too, but sustained favored-class demand and another class eligibility specifically test a treatment/progress obligation.

**Bullet 3: partly; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Don't apply strict priority blindly when another class has a positive minimum; preserving the favored class alone can violate the joint service contract.

An operation envelope can include a deadline, while the full instruction resolves competing independent class minimums that a favored-only envelope cannot accept.

**Bullet 4: transferable; nearest sibling `accessibility-access-control`.**

> Do derive class entitlement from the trusted policy source; a caller labeling itself urgent must not silently seize the protected resource treatment.

Access Control also needs trusted entitlement rather than caller-supplied privilege labels; this entire class-authority instruction transfers.

**Bullet 5: transferable; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Do inspect downstream shared pools after separating ingress queues; hidden recombination can erase the end-to-end differentiation the classes were promised.

A performance path can also recombine at a hidden pool after ingress separation, so this end-to-end contention instruction applies unchanged.

**Bullet 6: transferable; nearest sibling `scalability`.**

> Do count admitted, rejected and unfinished work by class; rejecting one class without the agreed policy cannot become an apparent scheduling-quality improvement.

A mixed growth workload also needs honest admitted/rejected/unfinished work by relevant class; the whole accounting rule is reusable.

Count: 3 transferable, 3 partly, 0 specific.

### 088-scalability

**Bullet 1: transferable; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Do name the growing dimension and held conditions; more stored accounts is not evidence for more simultaneously active requests or larger per-request data.

A fixed-load envelope also needs exact workload dimensions instead of conflating idle accounts with active requests, so this whole scope rule transfers.

**Bullet 2: specific; nearest sibling `expandability`.**

> Don't call resource admission a successful growth curve; a new worker may be usable while the shared bottleneck still caps useful service at rising demand.

An installation can successfully admit a usable worker while the growth envelope still fails; this rule explicitly rejects admission as the scalability acceptance result.

**Bullet 3: transferable; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Do keep offered work, completed work and backlog together at each point; a throughput plateau with accumulating demand is not successful scaling of that demand.

An offered-throughput performance contract can also fail with a completion plateau/backlog, making the full result/demand ledger rule reusable.

**Bullet 4: transferable; nearest sibling `efficiency-device-efficiency`.**

> Do label resource changes separately from workload changes; extra capacity can hide fixed-resource saturation and its cost when both axes move without explanation.

A resource-per-result comparison also must disclose resource changes and cost rather than move both comparison axes invisibly; the whole rule transfers.

**Bullet 5: partly; nearest sibling `quality-of-service`.**

> Do exercise declared hot-key/tenant skew, not just evenly spread work; balanced test traffic can miss the partition that limits the requested growth envelope.

Tenant skew can also affect differentiated treatment, but this instruction specifically challenges the growth envelope rather than class obligations alone.

**Bullet 6: partly; nearest sibling `efficiency-device-efficiency`.**

> Don't extrapolate linear improvement beyond the tested range; coordination and changed data distribution remain unverified rather than solved by a fitted line.

Resource comparisons also need bounded inference, while the full rule rejects a linear capacity forecast over untested demand/distribution growth.

Count: 3 transferable, 2 partly, 1 specific.

### 099-sustainability

**Bullet 1: specific; nearest sibling `efficiency-device-efficiency`.**

> Don't equate lower CPU, a smaller bill or newer hardware with environmental improvement; each can change without establishing the chosen stewardship objective.

Lower measured CPU per useful result can satisfy device efficiency without proving environmental impact; this rule requires the separate stewardship evidence instead.

**Bullet 2: transferable; nearest sibling `efficiency-device-efficiency`.**

> Do keep useful output and quality fixed in the comparison; stopping required service can reduce measured energy while defeating the agreed functional unit.

A resource-efficiency comparison also must preserve useful output/quality rather than count abandoned service as savings; the full functional-unit rule transfers.

**Bullet 3: transferable; nearest sibling `efficiency-device-efficiency`.**

> Do include idle/shared-device allocation and displaced work within the declared boundary; moving consumption outside a narrow counter is not a whole-system saving.

Shared/idle allocation and displaced work also belong in a whole-task resource comparison, so this accounting instruction applies unchanged.

**Bullet 4: transferable; nearest sibling `efficiency-device-efficiency`.**

> Don't convert energy to emissions using an invented factor; source, location, period and boundary limits must support that distinct claim or remain unknown.

A device-resource report also must not invent an emissions conversion, so the entire source/location/period boundary warning transfers.

**Bullet 5: partly; nearest sibling `efficiency-device-efficiency`.**

> Do separate operational savings from acquisition/replacement/retirement effects; a lower running measurement cannot settle an unmeasured lifecycle tradeoff.

A device-efficiency task may note other costs, but acquisition/replacement/retirement is a lifecycle boundary beyond its resource-per-operation acceptance metric.

**Bullet 6: partly; nearest sibling `viability`.**

> Do test service adequacy when extending device life; retaining unusable equipment does not meet a stewardship objective defined around continued useful service.

Continued stakeholder value can require useful service too, but extending device service life for a stewardship objective is narrower than continued business worth.

Count: 3 transferable, 2 partly, 1 specific.

Across all rules: 22 transferable, 9 partly, 3 specific.
Predictability has no exclusive rule in this comparison: raw outcomes, conditional sampling and honest censoring also serve performance/measurement work. Its distinct acceptance question is observed variation, not an exclusive technique. Shared workload, resource and evidence mechanics remain a substantive specificity limitation for the batch; low literal similarity cannot remove it.

## Per-skill findings and weaknesses

- **Efficiency/Device Efficiency:** The functional-unit denominator, useful-result
  validation, idle/background allocation and displaced resources make the comparison
  concrete. The report fixture exposes lower total CPU without an improved ratio,
  and a separate matched-output improvement. Actual device counters, allocation,
  workload equivalence and preserved service remain unmeasured. Resource dimensions
  and unsupported conversion checks also transfer to Performance and Sustainability;
  resource per useful result is the acceptance boundary, not an exclusive optimization.
- **Performance/Efficiency/Time or Space Bounds:** Required completion, offered
  work, unfinished outcomes, raw percentile method and scoped space are explicit.
  The export example declares its sample/rank rule and distinguishes queue receipt
  from artifact completion. It does not provide a real load generator, meaningful
  sample-size assurance, memory peak or production timing result. Timeout/unfinished
  acceptance must be settled in the target project; the completed sample alone
  cannot certify the whole offered workload. Many checks also fit Scalability.
- **Predictability:** Conditional groups, observed spread, raw extremes, censoring
  and the independent absolute deadline are executable review decisions. The
  uniformly slow example shows why passing a spread criterion cannot establish
  acceptable overall service. No future no-outlier or deterministic guarantee is
  supplied by finite observations. Every rule is reusable in a nearby measurement,
  timing or repeatability concern; the metric contract supplies the distinguishing
  question while rule-technique specificity remains a weakness.
- **Quality of Service:** Trusted class assignment, lower-class eligibility,
  admission, downstream contention and independently accepted class outcomes make
  differentiation testable. The example correctly fails the joint contract when
  interactive timing passes but eligible batch work starves. Actual capacity,
  entitlement authority and feasible paired targets are unknown. A priority flag
  does not establish end-to-end treatment, and the proposed progress window is
  not a universal fairness or scheduling rule.
- **Scalability:** Named axes, fixed-versus-added resource series, skew and
  offered/completed/backlog evidence distinguish growth from capacity admission.
  The plateau fixture exposes a failed growth point even when the completed
  subset's timing appears acceptable. Its numbers do not identify the actual
  bottleneck or establish steady-state duration, generator capacity or future
  linear scaling. Real service bounds/resource costs remain target decisions,
  and per-point accounting techniques overlap with Performance and Efficiency.
- **Sustainability:** The stakeholder objective, functional output, evidence
  provenance, allocation, displacement and operational/lifecycle boundary are
  explicit. The energy fixture cannot establish total lifecycle benefit, emissions
  or that replacing hardware is preferable. Metering, supported factors, period,
  scope and service-life adequacy require source/user evidence. The energy default
  applies only if energy is the chosen objective; a device-life request requires
  its own usable-service/horizon contract rather than an assumed energy target.

Internal rubric assessment retained specificity and unexecuted empirical evidence
as limitations rather than claiming perfect scores. No independent forward-test,
benchmark, service guarantee or environmental outcome was produced. The shared
Efficiency alias remains a proposed local split from the disambiguation map.

## Distinct checks and count rationale

- Efficiency checks functional unit/resource, ownership/allocation, matched
  conditions, correct results/service, ratio reconstruction, displacement/dimensions
  and unsupported conversions.
- Performance checks result/workload/boundaries, timer anchors, all outcome classes,
  raw-statistic reproduction, actual offered demand, space under concurrency/data
  and preserved correctness/unmeasured scope.
- Predictability checks conditional range/window, raw group membership, extremes,
  censored work, matched comparison, independent absolute constraints and finite coverage.
- Quality of Service checks trusted classes/mix, independent obligations, spoofed
  labels, sustained eligibility, downstream treatment, per-class results, uncompensated
  class failures and infeasible/unoffered cases.
- Scalability checks growth axis/skew, resource policy, offered demand, per-point
  useful results/backlog, bottleneck/resource response, first failures/cost and tested range.
- Sustainability checks objective, equivalent useful service/horizon, boundary/
  displacement, evidence type, selected outcome, lifecycle tradeoffs and conversion scope.

Rule/check/failure counts are Efficiency 5/7/5; Performance 5/7/6; Predictability
6/7/5; Quality of Service 6/8/5; Scalability 6/7/5; Sustainability 6/7/5.
Redundant generic preserve-required-behavior rules were removed from Efficiency
and Performance while keeping those constraints in their workflow/verification.
Counts follow these distinct checks, not a fixed shape or the five workflow steps;
matching counts elsewhere are not a claim of equivalent content or depth.

## References and footprint

All guides contain concrete use-when, trade-off and verification practices.
Efficiency covers useful output, allocation, reuse and displaced dimensions;
Performance adds required-result timing, offered work, sample calculation,
critical-path changes and space; Predictability covers condition groups/extremes/
exceptional paths and absolute constraints; Quality of Service covers assignment,
joint obligations, downstream resources and eligibility; Scalability covers axes,
resource series, saturation/source capability and tested range; Sustainability
covers objective evidence, allocation, displacement and useful device life.

Each worked example has explicit synthetic inputs, expected outputs, carried
state/measurement boundaries and negative interpretations. No fixture is presented
as measured target-system data. Every reference is directly linked with read-when
guidance, under its individual limit, and contains no nested reference chain.

| Skill | Description characters | Body | Complete SKILL.md | Design guide | Worked example | Combined |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| efficiency-device-efficiency | 511 | 119 | 124 | 35 | 35 | 194 |
| performance-efficiency-time-or-space-bounds | 508 | 121 | 126 | 43 | 35 | 204 |
| predictability | 484 | 121 | 126 | 35 | 33 | 194 |
| quality-of-service | 531 | 125 | 130 | 35 | 35 | 200 |
| scalability | 548 | 121 | 126 | 35 | 35 | 196 |
| sustainability | 509 | 124 | 129 | 35 | 35 | 199 |

Every reference is under 150 lines and every combined footprint meets the
150-250 guideline. The shared four-practice presentation in most guides is not
empty headings; line counts alone do not establish independent decisions or
absence of semantic overlap.

## Final routing consistency

Body review retains the description-first routing table. Bare efficiency, a
better tier and generic savings still need the listed first question. Resource
ratio, operation envelope, observed variation, class treatment, growth curve and
stewardship objective remain separate acceptance questions despite shared metrics.
No Phase-5 evals, keyword ranking, live routing, infrastructure purchase or batch-11
skill was produced. Sustainability retains its Business & Fitness catalogue category.

## Uncertain claims

- **Efficiency:** Useful-result definition/quality, resource ownership, counter
  scope, idle/background allocation, device conditions, displaced work and preserved
  service need confirmation. The CPU ledger establishes no actual resource, energy,
  cost or environmental saving.
- **Performance:** Workload/arrival source, success boundary, eligibility/rank
  method, timeout/pending policy, percentile coverage, environment and memory scope
  are unresolved target facts. The sample arithmetic does not establish measured
  performance or confidence about production tails.
- **Predictability:** Conditional groups, sampling/window, rare-path causes,
  censored outcomes, acceptable variation and absolute deadlines need evidence.
  A finite range comparison provides no future outlier exclusion or controller stability proof.
- **Quality of Service:** Class authority, offered/admitted mix, capacity,
  downstream contention, eligible progress windows, feasible paired targets and
  rejection policy need stakeholder/source decisions. No actual scheduling guarantee exists.
- **Scalability:** Growth dimensions, realistic skew, resource policy/cost,
  generator capability, observation duration, saturation cause and acceptable
  service range are unknown. A hypothetical plateau proves neither a real bottleneck
  nor future linear/unlimited capacity.
- **Sustainability:** Selected objective, meter/proxy provenance, units, system/
  lifecycle boundary, allocation, displaced work, supported impact factors, device
  service life and total effects need confirmation. No operational fixture proves
  emissions, net lifecycle benefit or a purchasing/replacement recommendation.

Ask the user for missing context. New skills cite no external standard, URL,
clause, tool flag, library version, legal duty, population statistic or impact
factor. Numeric system targets and fixtures are illustrative with stakeholder
confirmation. Calculations are local example arithmetic, not unsupported claims
about devices, applications or environmental results.

## Validation evidence

- `python scripts/validate_skills.py --only 41,72,74,77,88,99`: six skills, zero errors.
- `python scripts/validate_skills.py`: 63 skills checked, 51 absent todo entries, zero errors.
- `python -m unittest discover -s tests -v`: all 19 foundation tests passed.
- Skill-creator frontmatter validation: all six new skills valid.
- Scope/catalogue checks passed: only the six authorized todo statuses became
  draft; previous skills, pilots, shared contracts, scripts, tests and similarity
  threshold remain unchanged. Sustainability retains its original category.
- Trigger, workflow/code/docs, numeric-label, direct-reference, individual-limit
  and combined-footprint checks passed. Every reviewed rule quote matches current content.
- All 34 rule bullets have named-sibling findings: 22 transferable, 9 partly
  transferable and 3 specific against the selected nearest comparison.
- Local arithmetic checks passed for CPU resource ratios/reduction, the declared
  percentile/rank fixtures and counterexample, observed timing ranges, unserved
  rates, and the operational-energy ratio/reduction. These checks validate fixture
  arithmetic, not empirical device, service or environmental results.
- Maximum batch-involving body five-gram Jaccard is 0.018637157833430402 for
  efficiency-device-efficiency/predictability, below unchanged 0.35. Literal-copy
  detection does not establish semantic exclusivity or resolve the transfer findings.
