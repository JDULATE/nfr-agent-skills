# Batch 6 findings

## Scope and description-first routing

The Availability pilot and its references are preserved as the approved existing
batch member. Five new descriptions were written before their bodies and compared
with the reliability/resilience cluster. All three approved pilot entrypoints and
the shared authoring contract were read. Batch-5 approval did not promote draft
statuses to reviewed or authorize changes to previous skills.

The routing table is a manual boundary review, not a running-agent test or the
later keyword-overlap heuristic. Missing failure semantics were not supplied by
an inferred universal definition.

| Request | Best fit / ambiguity | Acceptance boundary and first missing fact |
| --- | --- | --- |
| Make this more reliable | Tie: reliability / availability / dependability | Are failures occurring, is usable time insufficient, or is the concern reliance across multiple failure properties? |
| Stop recurring crashes during our normal workload | reliability | Failure occurrence over exposure; what operating profile, interval, and failure boundary matter? |
| Improve uptime | availability, existing pilot | Required usable service and time/request accounting; which journey and calendar? |
| Keep serving when a worker crashes | fault-failure-tolerance | Explicit component fault with continued required result; what fault scope and degradation are allowed? |
| Add failover | fault-failure-tolerance / recoverability unresolved | Must the required result continue during the fault, or may service stop and then be restored? |
| Bad input should not bring down the process | robustness | Controlled adverse-input handling; which effects, bounds, and unaffected work must be preserved? |
| Survive a network partition | fault-failure-tolerance / robustness / survivability unresolved | Which partition model and required result; is mission survival rather than ordinary service the acceptance question? |
| Can we rely on this for the mission? | dependability | Combined scoped reliance argument; which failure concerns and decisions need supporting evidence? |
| Restore the database after an outage | recoverability outside batch | Restoration and lost-state limits, not uninterrupted fault service. |
| Prevent this cleanup from causing irreversible loss | safety | Stakeholder-defined harmful outcome and unsafe action; which retained data and permitted deletion conditions? |
| Protect against malicious input | security-control-and-security outside batch, robustness may contribute | What adversary, asset, and misuse path; is controlled response a supporting constraint? |
| Do not lose an acknowledged write | durability outside batch | Persistence across named events; the interval/fault requirements may coexist but do not replace that property. |
| Restart automatically when it fails | reliability / recoverability unresolved | Is the goal preventing failures or restoring service after them? A restart does not erase occurrence. |
| Shut it down whenever anything goes wrong | No justified single mechanism | Which harmful outcomes and service obligations apply? Stopping is not assumed safe or an availability improvement. |

The five new descriptions use distinct natural trigger phrases and real canonical
sibling pointers. Broad reliability, failover, partition, and shutdown language
still needs clarification; the descriptions do not claim a unique route for it.

## Full rule transfer findings

Every Rules of thumb bullet is quoted, including all seven in the preserved
Availability pilot. The nearest sibling is the most plausible boundary comparison
from the map, not a claim about an unauthored sibling body. Transferable means
the whole instruction can serve that sibling unchanged; partly means shared
mechanism with a materially different acceptance question; specific means the
nearest tested sibling would accept a different decision. These judgments are
manual and do not establish empirical model routing.

### 015-availability

**Bullet 1: transferable; nearest sibling `reliability`.**

> Do admit a probe sample to good eligible time only when the user-facing journey produces its required result; a healthy process alone cannot supply that sample.

Checking the required business result rather than process health also establishes required-behavior success in a reliability trial; the good-time label does not make the mechanism exclusive.

**Bullet 2: partly; nearest sibling `fault-failure-tolerance`.**

> Do measure deployment interruption from the loss of usable service to its return, including in-flight requests; drain traffic to preserve that journey, rather than declaring the handoff outage-free because a replacement instance is healthy.

Both inspect in-flight work during handoff, but the whole instruction measures deployment outage duration rather than acceptance under a declared component fault.

**Bullet 3: transferable; nearest sibling `fault-failure-tolerance`.**

> Do count an optional-dependency outage as good time only if the remaining path still meets the accepted service boundary; count a missing mandatory result as bad.

An optional dependency may fail without losing the accepted result under a fault model too; the same good/bad classification rule can be used unchanged.

**Bullet 4: partly; nearest sibling `fault-failure-tolerance`.**

> Do probe through shared storage and routing when measuring customer-visible good time; separate replica health histories cannot establish that the shared journey was usable during their common dependency's outage.

Shared-path testing is necessary to a fault model as well, while customer-visible good-time accounting remains specifically the availability acceptance question.

**Bullet 5: transferable; nearest sibling `fault-failure-tolerance`.**

> Do preserve the same success boundary during fallback; reject stale or read-only operation as available when the agreed journey requires fresh data or writes.

A continued-service fault contract also cannot replace a fresh write with a stale/read-only result unless degradation was accepted; the whole safeguard applies unchanged.

**Bullet 6: partly; nearest sibling `reliability`.**

> Don't remove planned maintenance from the denominator unless the approved service calendar explicitly excludes it; retain the excluded intervals in reports.

Operating intervals also need predeclared exclusions, but maintenance in a service-calendar denominator is an availability-specific accounting decision.

**Bullet 7: transferable; nearest sibling `reliability`.**

> Don't average away an unavailable audience segment; retain per-location and per-journey results before applying an agreed combined measure.

Preserving affected segments before aggregation also prevents hiding a failure-prone operating profile; the unchanged instruction is reusable for reliability reporting.

Count: 4 transferable, 3 partly, 0 specific.

### 037-dependability

**Bullet 1: partly; nearest sibling `safety`.**

> Don't average strong uptime evidence with an unsupported harmful-outcome claim; compensating scores cannot establish a reliance condition that must independently hold.

An independently required harmful-outcome condition cannot be averaged away in Safety either, but weighing multiple reliance conditions is the umbrella decision here.

**Bullet 2: transferable; nearest sibling `reliability`.**

> Do attach operating assumptions to every supporting subclaim; a favorable test outside the intended use cannot justify the umbrella reliance decision by proximity.

A reliability assurance argument also needs evidence within the operating assumptions of its claim; this whole evidence-scope instruction transfers.

**Bullet 3: transferable; nearest sibling `trustability`.**

> Do keep contrary incidents beside supporting evidence; deleting a defeating case makes the assurance story cleaner without repairing the broken reliance premise.

A trust decision supported by inspectable claims must retain defeating evidence too, so this counterexample rule is not exclusive to failure assurance.

**Bullet 4: transferable; nearest sibling `trustability`.**

> Don't count repeated reports of the same experiment as independent assurance; shared provenance leaves the same untested assumptions in the combined argument.

Duplicate evidence reports also fail to supply independent support for a broader justified trust claim; the provenance instruction moves unchanged.

**Bullet 5: partly; nearest sibling `safety`.**

> Do compare mitigations across the selected reliance conditions before recommending them; disabling a needed function may improve a local failure metric while defeating the mission.

A harm-control decision must consider competing consequences, but the full rule checks the combined mission reliance conditions, not only hazard paths.

Count: 3 transferable, 2 partly, 0 specific.

### 048-fault-failure-tolerance

**Bullet 1: transferable; nearest sibling `availability`.**

> Do require the alternate path to survive the modeled fault itself; extra workers sharing its failed store cannot satisfy continuation of a store-dependent result.

A journey availability mechanism can fail on the same shared store, so verifying the alternate survives that dependency is also useful there unchanged.

**Bullet 2: specific; nearest sibling `recoverability`.**

> Don't call restart-after-interruption tolerance; inspect service through the detection and handoff interval instead of accepting only its eventual return.

This explicitly rejects restoration as the acceptance question; a recoverability task can legitimately accept service return after interruption.

**Bullet 3: transferable; nearest sibling `availability`.**

> Do enforce the accepted result semantics during degradation; a fallback page cannot stand in for a committed write required throughout the modeled fault.

The availability pilot already requires the same result boundary during fallback; this whole degradation rule applies there unchanged.

**Bullet 4: partly; nearest sibling `integrity`.**

> Do resolve commit ownership during overlapping failover; otherwise apparently continued service can duplicate the effect the tolerance contract must preserve.

Commit ownership also protects against unintended alterations, but preserving effects during failover is a narrower fault-exposure condition than general integrity controls.

**Bullet 5: partly; nearest sibling `reliability`.**

> Don't infer concurrent-fault tolerance from isolated fault exercises; overlap changes the available continuation paths and must match the claimed model.

Evidence must match claimed conditions in either concern, while concurrent fault combinations and alternate continuation paths specifically define this model.

**Bullet 6: specific; nearest sibling `recoverability`.**

> Do hold the injected fault long enough for the agreed workload to exercise the alternate path; clearing it before work arrives tests recovery, not continuation under exposure.

Holding a fault while exercising the alternate is meant to reject a restoration-only experiment; Recoverability instead accepts restoration evidence after disruption.

Count: 2 transferable, 2 partly, 2 specific.

### 081-reliability

**Bullet 1: partly; nearest sibling `availability`.**

> Do keep failure occurrence separate from restoration time; an instant restart cannot make the preceding required-behavior violation disappear from the trial.

Availability can retain failure events, but its acceptance metric measures usable service time; the whole rule protects a continuous failure-occurrence trial rather than that ratio.

**Bullet 2: partly; nearest sibling `repeatability`.**

> Don't reset the failure-free clock without declaring a new trial boundary; combining only the surviving tails hides the continuity the interval claim requires.

Trial boundaries matter for repeated procedures too, but selecting only surviving tails directly defeats a failure-free continuity claim, not repeatability by itself.

**Bullet 3: transferable; nearest sibling `availability`.**

> Do retain the original attempt's violated result when a retry succeeds unless the agreed failure unit is explicitly the complete retried interaction.

The approved pilot also preserves original attempt outcomes unless the agreed unit includes retries; this accounting instruction transfers unchanged.

**Bullet 4: partly; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Do drive the declared operational profile during exposure; an idle process cannot establish failure-free execution of work that the trial never exercised.

A performance test must also exercise the relevant workload, but an idle interval here specifically fails to evidence continuous required-behavior execution.

**Bullet 5: transferable; nearest sibling `robustness`.**

> Do distinguish a permitted rejected input from a failure of required behavior; counting every error response can penalize a correctly enforced operating contract.

Controlled adverse handling likewise treats permitted rejection as valid behavior; this whole rejection-versus-failure distinction fits it unchanged.

**Bullet 6: transferable; nearest sibling `dependability`.**

> Don't generalize a clean bounded run to a future failure probability without an agreed model; observed absence is not a universal failure-free guarantee.

Combined assurance must also avoid unsupported probability generalization from a clean run; the inference limitation can move unchanged.

Count: 3 transferable, 3 partly, 0 specific.

### 086-robustness

**Bullet 1: transferable; nearest sibling `security-control-and-security`.**

> Do bound expanded work before materializing an adverse input's full structure; a size error after the allocation cannot demonstrate controlled resource behavior.

An adversary may exploit the same expansion path, so early work bounds can be an unchanged control in a security task with that threat model.

**Bullet 2: transferable; nearest sibling `reliability`.**

> Don't accept an error response while orphaned jobs or reservations keep growing; repeated rejected inputs can still exhaust the shared process after their responses return.

Orphaned work from rejected requests can also create operational failures, making this whole lifecycle safeguard reusable under the relevant reliability profile.

**Bullet 3: transferable; nearest sibling `correctness`.**

> Do inspect state after rejecting partially processed input; an error code cannot excuse business mutations the controlled-rejection contract forbids.

A specified no-mutation rejection contract is also a correctness requirement; the error-path assertion does not depend exclusively on robustness.

**Bullet 4: partly; nearest sibling `fault-failure-tolerance`.**

> Do keep a valid control task running alongside adverse traffic; rejecting bad requests is insufficient if the same path starves the work meant to stay unaffected.

Unaffected work also matters during component faults, but adverse-traffic admission can legitimately reject the bad input rather than continue its required result.

**Bullet 5: transferable; nearest sibling `recoverability`.**

> Do verify behavior after the adverse condition ends; a process that remains wedged has not shown controlled recovery to its declared normal operating envelope.

Returning to the normal envelope after exposure is a restoration outcome too; this whole instruction fits a scoped recoverability check.

**Bullet 6: transferable; nearest sibling `correctness`.**

> Don't normalize malformed values into invented business data just to avoid an exception; controlled rejection can be correct when silent coercion would corrupt meaning.

Not inventing business data through silent coercion also preserves specified meaning in correctness; this is a shared boundary safeguard.

Count: 5 transferable, 1 partly, 0 specific.

### 087-safety

**Bullet 1: specific; nearest sibling `reliability`.**

> Do judge the control against the harmful outcome's causal path, not an error count; a quiet system can still issue the action that makes the situation hazardous.

Failure/error occurrence is deliberately rejected as the hazard-control oracle; the decision instead depends on an action-to-harm causal path.

**Bullet 2: specific; nearest sibling `availability`.**

> Don't assume stopping is the safe response; an omitted or late action may be the path to harm, so the required uncertain-state behavior needs its own justification.

The rule explicitly rejects blanket stopping as safe because omission or delay can cause harm; usable-service accounting does not determine that justified action policy.

**Bullet 3: transferable; nearest sibling `security-control-and-security`.**

> Do enforce a confirmed hazard constraint at the point that commits the effect; a warning screen cannot protect the same action reached through another entrypoint.

Enforcing a constraint at the actual effect boundary and checking alternate entrypoints also applies unchanged to misuse prevention.

**Bullet 4: transferable; nearest sibling `security-control-and-security`.**

> Do inspect whether required state evidence changes before commitment; a safe earlier decision cannot justify an unsafe action after its hazard conditions change.

A changed state between authorization and effect can also defeat an adversarial control; this stale-decision rule transfers without modification.

**Bullet 5: specific; nearest sibling `recoverability`.**

> Don't accept failover or recovery as a harm-control substitute unless it breaks the identified causal path; restored service can still produce the harmful action.

Restoring service is insufficient unless it breaks the harm path; Recoverability can legitimately accept restored service without making that hazard-control claim.

**Bullet 6: transferable; nearest sibling `dependability`.**

> Do retain competing harmful consequences and control bypasses as unresolved paths; a favorable primary scenario does not authorize accepting their residual exposure.

Competing consequences, bypasses, and owned residual exposure also belong in a combined reliance case; this whole counterexample limitation transfers.

Count: 3 transferable, 0 partly, 3 specific.

Across all rules: 20 transferable, 11 partly, 5 specific.
Shared failure/result semantics explain much of the overlap, but do not eliminate the weakness. Boundary-specific descriptions and evidence contracts carry more routing precision than the reusable safeguards.

## Per-skill findings and remaining weaknesses

- **Availability, preserved pilot:** The service boundary, time/request distinction,
  unknown-data bounds, journey probes, and implementation patterns are concrete.
  Its broad SLA/SLO trigger still needs clarification when a user means another
  service property. The full footprint is 439 lines, above the later combined
  150-250 guideline, although every body/reference passes its individual limit.
  Existing approval is preserved; that exception does not authorize rewriting the
  pilot. Result preservation and shared-dependency rules remain transferable.
- **Dependability:** The claim/assumption/evidence ledger and counterexample gate
  distinguish combined reliance from one operational metric. Most immediate work
  is repository evidence investigation and documentation; implementation changes
  are limited to concrete supporting gaps, not an invented universal assurance
  architecture. Evidence relevance and criticality remain judgment calls requiring
  an owner. Several evidence-provenance rules also fit Trustability, and a tidy
  ledger alone does not establish an actual reliable or safe system.
- **Fault/Failure Tolerance:** The model records exposure, alternate path, allowed
  degradation, and ownership/effect semantics. The worker example explicitly keeps
  fail-stop and delayed-old-commit exercises separate instead of silently changing
  the fault model. It does not select a real atomicity/fencing implementation or
  prove independent storage/routing. A network-partition trigger needs more context
  than the fail-stop worked example supplies; the guide treats it as a distinct
  model and never infers coverage from process loss.
- **Reliability:** Event, exposure, retry, and reset accounting distinguish failure
  occurrence from usable time and restoration. The sustained-state investigation
  points to real lifecycle code and result checks rather than prescribing retries
  as a cure. Trial length, failure unit, profile representativeness, and observation
  coverage remain stakeholder/project choices. No statistical confidence or future
  failure probability is supported by the hypothetical trace. Event accounting and
  allowed-rejection checks overlap with Availability and Robustness.
- **Robustness:** Early work bounds, response/work separation, reservations, actual
  mutations, and valid control tasks make containment testable. The malformed
  import example leaves real resource budgets and parser limits unresolved;
  it cannot claim a complete operating envelope without them. Most mechanics also
  fit a security threat or reliability defect using the same failure path. That
  is a substantive transfer weakness; the adverse-response contract supplies the
  boundary, not exclusive ownership of validation or cleanup techniques.
- **Safety:** Harm, hazardous conditions, unsafe actions/omissions, commitment-time
  state, alternate entrypoints, and residual decisions are explicit. The example
  uses stakeholder-defined harmful loss of retained operational records; it is
  neither a physical-control example nor evidence of a regulated safety process.
  It supplies no concurrency primitive guaranteeing that state and deletion are
  bound together. A real domain may require additional expertise, hazards, and
  evidence that this local convention does not establish. Effect-boundary and
  changed-state rules also apply to Security and the combined Dependability case.

Internal rubric assessment found no missing criterion and retained semantic-rule
specificity as an improvement area rather than claiming perfect scores. The
findings do not replace independent review, target-system fault experiments,
actual hazard analysis, or observed long-running production evidence.

## Verification diversity and count rationale

- Availability's checks distinguish service boundary, degraded semantics,
  accounting contract, unknown/exclusion rules, outage exercise, segmentation,
  metric reproduction, and remaining outage ownership.
- Dependability checks claim scope, relevant evidence, shared assumptions/provenance,
  defeating incidents, mitigation conflicts, unresolved ownership, and recommendation limits.
- Fault/Failure Tolerance checks model definition, alternate-path dependencies,
  transition result semantics, held-fault work, ownership effects, honest interruption
  classification, fault clearance, and approved degradation/exclusions.
- Reliability checks failure unit, exercised exposure, continuous results, retries
  and resets, event deduplication, coverage gaps, and inference boundaries.
- Robustness checks adverse/valid classes, early budgets, response/resource bounds,
  no forbidden effects, valid controls, repetition/overlap scope, and post-state.
- Safety checks grounded harm, causal path, enforcing boundary, unknown-state policy,
  changed-state timing, alternate entrypoints, actual effects, and residual ownership.

Rule/check/failure-mode counts are Availability 7/8/5, Dependability 5/7/5,
Fault/Failure Tolerance 6/8/5, Reliability 6/7/5, Robustness 6/7/6, Safety 6/8/5.
A redundant unsupported-subclaim rule was removed from Dependability rather than
padding its count. Shared counts are disclosed; the done items map to distinct
evidence, not the five workflow steps or an imposed universal item count.

## Design depth and footprint

The new guides contain use-when, trade-off, and how-to-verify practices with
specific evidence. Dependability includes concrete repository outputs;
Fault/Failure Tolerance separates shared dependencies, ownership, operation identity,
degradation, and partitions; Reliability focuses on occurrence/profile evidence;
Robustness adds admission, retained work, effects, isolation, and cleanup;
Safety separates harm, effect enforcement, state validity, uncertainty, and defeat.
No linked reference nests further reference links.

| Skill | Description characters | Body | Complete SKILL.md | References | Combined |
| --- | ---: | ---: | ---: | --- | ---: |
| availability | 308 | 155 | 164 | measurement 114; design 102; example 59 | 439 |
| dependability | 439 | 121 | 126 | design 42; example 37 | 205 |
| fault-failure-tolerance | 480 | 125 | 130 | design 44; example 38 | 212 |
| reliability | 474 | 123 | 128 | design 35; example 38 | 201 |
| robustness | 547 | 124 | 129 | design 43; example 37 | 209 |
| safety | 459 | 126 | 131 | design 43; example 39 | 213 |

All new combined footprints meet the 150-250 guideline. The unchanged approved
pilot is the existing combined-footprint exception. Each individual reference
is under 150 lines. Footprint compliance alone does not establish semantic depth.

## Final routing consistency

The description-first table remains the final manual routing result after body
review. Generic reliability, failover, partition, and shutdown requests still
need the first clarifying question shown there. Uptime, occurrence, modeled-fault
continuation, controlled adverse response, causal harm, and combined reliance
remain different acceptance questions even where mechanisms overlap.
No Phase-5 eval artifacts, keyword-ranking results, or live-agent routing outcomes
were produced. No batch-7 skill was authored.

## Uncertain claims

- **Availability:** Real journeys, calendars, deadlines, unknown-data decisions,
  probe coverage, failure independence, and availability attainment remain target
  project decisions/evidence. The approved examples establish no real uptime result.
- **Dependability:** Mission use, unacceptable effects, criticality, evidence
  relevance, subclaim independence, and residual acceptance need stakeholder/source
  confirmation. The fictional dispatch claim is not an actual reliance recommendation.
- **Fault/Failure Tolerance:** Actual fault classes/concurrency, alternate-path
  independence, state ownership, atomic effect semantics, permitted degradation,
  and deadlines are unknown. A fail-stop example does not establish partition or
  overlapping-fault coverage. No actual mechanism or fault exercise is claimed.
- **Reliability:** Required behavior, qualifying event unit, profile, trial interval,
  resets, retry semantics, observation gaps, and model for any extrapolation need
  confirmation. The stale-handle cause is a stated hypothetical, not a diagnosed
  repository defect or a production reliability estimate.
- **Robustness:** Real input/work limits, resource scope, partial-effect contract,
  cleanup/cancellation ownership, and unaffected-work criteria are unknown. The
  malformed import trace is illustrative; it proves neither measured containment
  nor resistance against an adversary.
- **Safety:** Harm definitions, retention state, competing omission/timing harms,
  commitment enforcement, control failure/bypass behavior, domain constraints, and
  residual-decision authority require user evidence. The cleanup policy is fictional,
  creates no legal retention duty, and establishes no certification or broad safety.

Ask the user for these context-dependent decisions. No standards, clauses, URLs,
library versions, legal obligations, or population statistics are added by the
new skills. Numeric trial proposals are illustrative with stakeholder confirmation;
observed examples are never invented. Shared engineering mechanisms are design
options to inspect and verify in the target code, not unverified platform guarantees.

## Validation evidence

- `python scripts/validate_skills.py --only 15,37,48,81,86,87`: six skills, zero errors.
- `python scripts/validate_skills.py`: 39 skills checked, 75 absent todo entries, zero errors.
- `python -m unittest discover -s tests -v`: all 19 foundation tests passed.
- Skill-creator frontmatter validation: all five newly authored skills valid.
- Scope guards passed: only five todo statuses became draft; the approved pilot,
  all previous skills, shared contracts, scripts, tests, and similarity limit remain unchanged.
- Workflow decision rules, code/docs inspection, numeric proposal labels,
  description triggers, reference links, individual limits, and new combined budgets passed.
- All 36 Rules of thumb bullets have named-sibling transfer findings: 20 transferable,
  11 partly transferable, and 5 specific against the selected nearest comparison.
- Maximum batch-involving body five-gram Jaccard is 0.015977961432506887 for
  fault-failure-tolerance/robustness, below the unchanged 0.35 limit. Literal-copy
  detection does not resolve the semantic transfers listed in this review.
