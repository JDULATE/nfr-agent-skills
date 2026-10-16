# Batch 6 audit

## Basis and principal findings

This skeptical source review covers every skill assigned to this batch in nfr-list.json, including any approved pilot, and every reference file under those skills. The authoring guide, rubric, disambiguation map and allowlist provide the contract. Existing reviews were not read as evidence. This is an agent review, not an independent human or blinded evaluation. No skill, catalogue, index, validator or threshold was changed.

- **Rule specificity needs review.** Most mechanisms are real, but assurance provenance, result preservation, shared-dependency and measurement guards frequently transfer to siblings. Low textual similarity would not detect this.
- **Dependability is mostly assurance work.** Its claim/evidence ledger is useful and honestly advertised; the generic repair-selection sentence provides less coding guidance than the failure-specific skills.
- **A negative gate is not a positive assurance case.** Dependability's unresolved-counterexample gate and Safety's prohibited-action gate cannot alone establish supported subclaims or timely required actions. The full workflows add these obligations, so this is a fast-path completeness weakness rather than proof that the skills automatically approve failures.
- **Availability is an inherited size exception.** Its combined footprint is 439 lines against the 150-250 guideline. Every individual reference remains below the hard reference limit. Its larger design guide provides real additional depth; this is not evidence that it should be compressed blindly.
- **A small diagnostic overstatement exists in Fault Tolerance.** Clearing an injected fault before any work arrives does not by itself test recovery; it simply fails to demonstrate continuation during exposure.

## Structure and description measurements

Line counts include blank lines; body excludes frontmatter. Combined includes full SKILL.md and all its references. These are authoring counts, not system targets.

| Id / slug | Description characters | Body / full | Reference lines | Combined | Rules / done / failure modes |
| --- | ---: | --- | --- | ---: | --- |
| 015 availability | 308 | 155 / 164 | deployment-example.md: 59; design-patterns.md: 102; measurement-contract.md: 114 | 439 | 7 / 8 / 5 |
| 037 dependability | 439 | 121 / 126 | design-patterns.md: 42; worked-example.md: 37 | 205 | 5 / 7 / 5 |
| 048 fault-failure-tolerance | 480 | 125 / 130 | design-patterns.md: 44; worked-example.md: 38 | 212 | 6 / 8 / 5 |
| 081 reliability | 474 | 123 / 128 | design-patterns.md: 35; worked-example.md: 38 | 201 | 6 / 7 / 5 |
| 086 robustness | 547 | 124 / 129 | design-patterns.md: 43; worked-example.md: 37 | 209 | 6 / 7 / 6 |
| 087 safety | 459 | 126 / 131 | design-patterns.md: 43; worked-example.md: 39 | 213 | 6 / 8 / 5 |

## Per-skill findings and full transfer test

Each source bullet is quoted in full, in its original order. Transferable means the entire bullet could serve the named sibling unchanged. Partly means the technique transfers but the acceptance framing needs alteration. Specific means that sibling has a different acceptance question. Shared safeguards can be necessary without satisfying the stricter requirement for distinctive Rules of thumb. Judgments use the repository conventions; they do not claim standardized meanings.

### 015 availability

**Description and boundary:** Natural uptime/deployment triggers and real Reliability/Recoverability pointers. SLA/SLO is broad language: a latency-only SLO also fits Performance, which is excluded in the body but not the description. The description does not falsely promise universal availability.

**Repository actions and design depth:** The most developed implementation guide in this batch: shutdown/draining, distinct health decisions, rollout choices, schema compatibility, bounded retries, shedding and shared-failure mapping each have selection context, tradeoffs and concrete exercises. The proposed accounting record remains demanding for a quick deployment fix.

**Worked example:** The deployment example supplies checkout, retirement routing, recorded acceptance and a mandatory-store negative case. It has no filled actual order identities, timings or observed rollout trace. A separate measurement contract gives a complete good/bad/unknown numeric ledger; its arithmetic is correct. This is deeper than the later compact examples, but distributed across several files.

**Three weakest passages:**

- `SKILL.md`: "define an SLA/SLO" - The description can attract objectives whose acceptance question is latency or another property rather than usable service.
- `SKILL.md`: "Journey/result: the requested journey and documented business success result." - A sensible placeholder for fast-path defaults, but not a filled requirement when the requested journey is ambiguous.
- `references/deployment-example.md`: "Suppose those artifacts show incoming traffic reaching a retiring worker" - The causal condition is hypothetical; no concrete routing/retirement event ledger demonstrates the change before and after.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do admit a probe sample to good eligible time only when the user-facing journey produces its required result; a healthy process alone cannot supply that sample. | fault-failure-tolerance | Partly | The end-to-end result check transfers, but assigning good eligible time is the availability accounting question. |
| 2. Do measure deployment interruption from the loss of usable service to its return, including in-flight requests; drain traffic to preserve that journey, rather than declaring the handoff outage-free because a replacement instance is healthy. | fault-failure-tolerance | Transferable | Continuity during a modeled retirement fault also needs draining and in-flight result evidence. |
| 3. Do count an optional-dependency outage as good time only if the remaining path still meets the accepted service boundary; count a missing mandatory result as bad. | fault-failure-tolerance | Partly | Preserving the degraded result transfers; classifying good/bad time supplies the current framing. |
| 4. Do probe through shared storage and routing when measuring customer-visible good time; separate replica health histories cannot establish that the shared journey was usable during their common dependency's outage. | fault-failure-tolerance | Partly | Shared-dependency probing transfers; replica health cannot establish the sibling continuation contract either, but good-time accounting differs. |
| 5. Do preserve the same success boundary during fallback; reject stale or read-only operation as available when the agreed journey requires fresh data or writes. | fault-failure-tolerance | Transferable | The same fallback semantics must preserve the required result during a modeled fault. |
| 6. Don't remove planned maintenance from the denominator unless the approved service calendar explicitly excludes it; retain the excluded intervals in reports. | reliability | Partly | Predetermined exposure exclusions transfer, but the service calendar denominator is an availability-specific object. |
| 7. Don't average away an unavailable audience segment; retain per-location and per-journey results before applying an agreed combined measure. | quality-of-service | Partly | Segment masking resembles class masking; location/journey availability is not itself differentiated scheduling. |

Transfer counts: 2 transferable; 5 partly; 0 specific.

### 037 dependability

**Description and boundary:** Cross-property reliance and three natural evidence-review triggers are explicit. Trustability is distinguished only in the body; a generic reliance question can still match both descriptions.

**Repository actions and design depth:** Primarily an assurance/evidence ledger and a conditional recommendation. That is an honest scope for this description; forcing code edits where the missing premise is operational evidence would be inappropriate. The guide identifies gap types but gives little selection detail for the smallest concrete repair.

**Worked example:** Named work order, owning team, subclaims, supporting trace and duplicate-dispatch counterexample form a concrete decision state. The candidate stable-operation-identity and ownership assertions are proposed, not implemented; no actual result/effect record demonstrates a successful repair.

**Three weakest passages:**

- `SKILL.md`: "0 unresolved critical counterexamples before recommending reliance." - This negative gate alone does not require positive support for each subclaim; the later workflow correctly does, so the gate is insufficient in isolation.
- `SKILL.md`: "identify the smallest relevant code/config, test, operational, or documentation change" - Names possible output categories without a decision procedure for selecting a repair.
- `references/worked-example.md`: "A candidate may enforce stable operation identity" - The example does not fill the operation/effect decision or show how the proposed mechanism changes the defeated premise.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't average strong uptime evidence with an unsupported harmful-outcome claim; compensating scores cannot establish a reliance condition that must independently hold. | trustability | Transferable | A stakeholder reliance decision also cannot average away an independently required harmful-outcome condition. |
| 2. Do attach operating assumptions to every supporting subclaim; a favorable test outside the intended use cannot justify the umbrella reliance decision by proximity. | trustability | Transferable | The same scoped evidence and assumption rule supports justified reliance beyond operational failures. |
| 3. Do keep contrary incidents beside supporting evidence; deleting a defeating case makes the assurance story cleaner without repairing the broken reliance premise. | trustability | Transferable | Removing a defeating counterexample equally undermines that sibling decision premise. |
| 4. Don't count repeated reports of the same experiment as independent assurance; shared provenance leaves the same untested assumptions in the combined argument. | trustability | Transferable | Duplicate evidence has the same shared-provenance limitation in a trust claim. |
| 5. Do compare mitigations across the selected reliance conditions before recommending them; disabling a needed function may improve a local failure metric while defeating the mission. | safety | Partly | Mitigation conflicts and mission-preserving behavior transfer, but the current rule coordinates a combined reliance case. |

Transfer counts: 4 transferable; 1 partly; 0 specific.

### 048 fault-failure-tolerance

**Description and boundary:** Fault model, required continuation and allowed degradation are explicit. Survive/failover language also fits Survivability or Recoverability when interruption and mission scope are unknown; the latter is excluded in the description, the former in the body.

**Repository actions and design depth:** Useful concrete ownership, fencing, operation identity, shared-failure and degraded-result practices. The example correctly separates fail-stop from a later delayed-old-owner exercise rather than pretending a stopped worker keeps executing.

**Worked example:** Named workers, operation and shared store; pending/result/owner transitions are explicit. Actual deadlines, ownership primitive and exposure duration remain unfilled. The negative delayed-owner model extension is stated honestly and improves causal precision.

**Three weakest passages:**

- `SKILL.md`: "clearing it before work arrives tests recovery, not continuation under exposure." - Without work or a restored-result check it may test neither property; the contrast overstates what such an empty exercise establishes.
- `SKILL.md`: "while an independently serving path remains." - An explicit proposed premise, not demonstrated independence; a fast-path consumer must not treat it as a discovered repository fact.
- `references/worked-example.md`: "That ownership check and the effect must enforce the intended contract together" - Correct but abstract: no concrete ownership-state transition shows how a stale commit is prevented.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do require the alternate path to survive the modeled fault itself; extra workers sharing its failed store cannot satisfy continuation of a store-dependent result. | availability | Transferable | An alternate serving path that shares the failed mandatory store cannot establish usable service either. |
| 2. Don't call restart-after-interruption tolerance; inspect service through the detection and handoff interval instead of accepting only its eventual return. | recoverability | Partly | The interruption/restoration distinction is shared, but recovery accepts restoration rather than uninterrupted tolerance. |
| 3. Do enforce the accepted result semantics during degradation; a fallback page cannot stand in for a committed write required throughout the modeled fault. | availability | Transferable | A fallback page also cannot satisfy availability of an agreed committed-write journey. |
| 4. Do resolve commit ownership during overlapping failover; otherwise apparently continued service can duplicate the effect the tolerance contract must preserve. | recoverability | Partly | Replay/ownership reconciliation transfers; preserving uninterrupted handoff rather than restored state supplies the current framing. |
| 5. Don't infer concurrent-fault tolerance from isolated fault exercises; overlap changes the available continuation paths and must match the claimed model. | survivability | Transferable | Isolated fault trials also cannot establish continuation under the combined disruption model. |
| 6. Do hold the injected fault long enough for the agreed workload to exercise the alternate path; clearing it before work arrives tests recovery, not continuation under exposure. | availability | Partly | Holding exposure while observing work transfers, but without any work even recovery is not established by the exercise. |

Transfer counts: 3 transferable; 3 partly; 0 specific.

### 081 reliability

**Description and boundary:** Failure occurrence over an operating profile is clear, with Availability/Fault Tolerance/Recoverability exclusions. Recurring ordinary failures can also fit Maturity until the user distinguishes future trial from historical readiness.

**Repository actions and design depth:** Lifecycle inspection, sustained reproduction, event ledger and regression checks are executable. The guide is stronger on preserving occurrence evidence than on selecting defect repairs. The example does supply a concrete hypothetical stale-handle lifecycle fix.

**Worked example:** Named jobs, failure identity, original attempt, restart and retry carry meaningful state. Illustrative timing is labeled. The event history proves the stated interrupted trial failed; the stale handle is correctly a supposition to verify, not a diagnosis inferred from the restart.

**Three weakest passages:**

- `SKILL.md`: "Trial: 10 minutes of continuous prescribed operation" - Labeled and confirmed, but no source-specific method chooses an adequate exposure window for a sustained-use defect.
- `references/design-patterns.md`: "replay the source-backed progression" - The guide requires a progression but gives no filled state schedule for reaching the implicated sustained-use condition.
- `references/worked-example.md`: "Suppose source inspection reveals a stale per-job handle" - A useful concrete repair candidate, but no actual handle ownership/state or before/after trace is worked through.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do keep failure occurrence separate from restoration time; an instant restart cannot make the preceding required-behavior violation disappear from the trial. | availability | Partly | Retaining an occurrence helps explain outages, while the acceptance unit here is the failure event rather than unavailable duration. |
| 2. Don't reset the failure-free clock without declaring a new trial boundary; combining only the surviving tails hides the continuity the interval claim requires. | maturity | Partly | Preserving interrupted history transfers; the uninterrupted future trial clock is Reliability-specific framing. |
| 3. Do retain the original attempt's violated result when a retry succeeds unless the agreed failure unit is explicitly the complete retried interaction. | availability | Transferable | The availability measurement contract already preserves original outcomes unless the unit is the whole retried interaction. |
| 4. Do drive the declared operational profile during exposure; an idle process cannot establish failure-free execution of work that the trial never exercised. | maturity | Transferable | Idle deployment also cannot establish exercised operational history for a readiness decision. |
| 5. Do distinguish a permitted rejected input from a failure of required behavior; counting every error response can penalize a correctly enforced operating contract. | robustness | Transferable | Permitted controlled rejection must also be separated from a violated valid-work obligation. |
| 6. Don't generalize a clean bounded run to a future failure probability without an agreed model; observed absence is not a universal failure-free guarantee. | maturity | Transferable | A readiness review must likewise avoid turning a clean bounded run into an unsupported future probability. |

Transfer counts: 4 transferable; 2 partly; 0 specific.

### 086 robustness

**Description and boundary:** Malformed input, resource exhaustion and unaffected work are distinctive triggers; Security/Fault Tolerance/Reliability boundaries are explicit. Overload can still mean ordinary growth and requires the body-level Scalability distinction.

**Repository actions and design depth:** Early admission, bounded expansion, cancellation/cleanup and valid-control isolation are real practices with tradeoffs. Compared with the assurance skills, the workflow gives stronger positive implementation decisions.

**Worked example:** Malformed nested record, valid control, no prefix mutation, reservation release and repeated exposure are concrete states. The raw malformed payload, structural limit, resource budget and reservation-owner race are not filled. It is more than a checklist but not a runnable parser fixture.

**Three weakest passages:**

- `SKILL.md`: "Work limits: existing documented size/depth/queue limits; absent limits remain open." - An honest open decision, but the fast path cannot establish bounded resource behavior from its response deadline alone.
- `references/worked-example.md`: "contains a truncated nested record after an otherwise valid prefix." - No literal input makes the exact parse/partial-processing boundary reproducible.
- `references/design-patterns.md`: "cleanup itself can fail or race with completion" - Names the important race without demonstrating ownership or reconciliation of a failed cleanup.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do bound expanded work before materializing an adverse input's full structure; a size error after the allocation cannot demonstrate controlled resource behavior. | security-control-and-security | Transferable | A threat-driven resource-exhaustion path needs the identical pre-expansion work bound. |
| 2. Don't accept an error response while orphaned jobs or reservations keep growing; repeated rejected inputs can still exhaust the shared process after their responses return. | reliability | Transferable | Leaked reservations after error responses can equally defeat sustained normal-profile operation. |
| 3. Do inspect state after rejecting partially processed input; an error code cannot excuse business mutations the controlled-rejection contract forbids. | atomicity | Partly | Inspecting mutation after failure transfers; controlled rejection is not identical to all-or-none participating effects. |
| 4. Do keep a valid control task running alongside adverse traffic; rejecting bad requests is insufficient if the same path starves the work meant to stay unaffected. | quality-of-service | Transferable | A protected valid class under competing adverse traffic needs the same valid-work control. |
| 5. Do verify behavior after the adverse condition ends; a process that remains wedged has not shown controlled recovery to its declared normal operating envelope. | recoverability | Partly | Post-exposure usable behavior transfers, but robustness includes containment during the adverse condition. |
| 6. Don't normalize malformed values into invented business data just to avoid an exception; controlled rejection can be correct when silent coercion would corrupt meaning. | integrity | Transferable | Silently coercing malformed input into invented values can be an unintended alteration under an integrity contract. |

Transfer counts: 4 transferable; 2 partly; 0 specific.

### 087 safety

**Description and boundary:** Named harm and causal unsafe-action scope distinguish generic error handling. Deletion/retention in the example also fits Integrity and Privacy; the stakeholder harm criterion is what selects Safety.

**Repository actions and design depth:** Effect-boundary constraints, state validity at commitment, uncertainty policy and bypass review are concrete. No external safety obligation or universal safe shutdown is asserted. Domain reviewers and the harm model remain necessary inputs.

**Worked example:** Held/released/unknown retention states, stale preview, actual deletion and direct bypass carry a concrete hazardous state change. The action-caused loss is worked through; a competing harm from omitted or delayed action is only asked about, despite being a major rule.

**Three weakest passages:**

- `references/worked-example.md`: "Ask for any competing harm from delayed cleanup" - The omission-harm branch is a question rather than a filled counterexample exercising the no-universal-shutdown rule.
- `references/design-patterns.md`: "inspect how the implementation binds the checked evidence to the effect" - No concrete state/version binding is demonstrated; the text properly avoids assuming atomicity.
- `SKILL.md`: "0 prohibited actions in the agreed hazardous-condition scenarios." - The proposed negative gate does not itself ensure required actions occur in time; workflow and the uncertainty pattern carry that separate obligation.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do judge the control against the harmful outcome's causal path, not an error count; a quiet system can still issue the action that makes the situation hazardous. | security-control-and-security | Partly | Causal effect analysis transfers, but harm can arise without the adversary required by the sibling. |
| 2. Don't assume stopping is the safe response; an omitted or late action may be the path to harm, so the required uncertain-state behavior needs its own justification. | robustness | Partly | Avoiding blanket refusal transfers; justification against harmful omission rather than controlled valid-work behavior supplies the safety boundary. |
| 3. Do enforce a confirmed hazard constraint at the point that commits the effect; a warning screen cannot protect the same action reached through another entrypoint. | security-control-and-security | Partly | Final-effect enforcement and bypass review transfer, but a hazard constraint is not necessarily an adversarial control. |
| 4. Do inspect whether required state evidence changes before commitment; a safe earlier decision cannot justify an unsafe action after its hazard conditions change. | integrity | Partly | Changed-state validation at mutation transfers; unsafe consequences require the additional harm model. |
| 5. Don't accept failover or recovery as a harm-control substitute unless it breaks the identified causal path; restored service can still produce the harmful action. | dependability | Transferable | An umbrella reliance argument also cannot substitute restored service for a separately required harm-control premise. |
| 6. Do retain competing harmful consequences and control bypasses as unresolved paths; a favorable primary scenario does not authorize accepting their residual exposure. | dependability | Transferable | The combined assurance case also needs competing harms, unresolved bypasses and owned residual decisions. |

Transfer counts: 2 transferable; 4 partly; 0 specific.

## Routing probes

Manual semantic probes expose missing facts; these are not measured routing accuracy. A tentative lead does not erase a tie or authorize assumptions.

| Realistic prompt | Best fit / tie | First question and reason |
| --- | --- | --- |
| "make this more reliable" | 81 tentative; 15/37 plausible | Ask the user: fewer failures, more usable time, or a combined reliance decision? The bare quality label supplies no acceptance unit. |
| "keep checkout working during deploys" | 15 tentative; 48 also fits | Ask the user: is success usable-time accounting across deployment or uninterrupted results during a specified worker fault? |
| "survive a database outage" | 48 tentative; 97 conditional | Ask the user: which result must continue, and is this a routine component fault or a severe minimum-mission scenario? |
| "make the parser handle bad input" | 86 | Ask the user: which adverse input classes, permitted rejections and unaffected valid work define controlled behavior? |
| "stop the worker crashing every night" | 81 tentative; 86 possible | Ask the user: what operating/state progression precedes the crash, and does it involve adverse exposure or normal valid work? |
| "prove we can depend on this release" | 37 tentative; 65 possible | Ask the user: a combined failure-assurance case or demonstrated readiness from operational history? |
| "add another replica" | No exclusive batch-6 winner | Ask the user: resource admission, usable-service protection, or continuation under which modeled fault? Replica count does not identify the goal. |
| "make deletion safe" | 87 / 57 / 75 unresolved | Ask the user: harmful loss, prohibited alteration, or personal-data disposal policy? The word safe does not define harm. |
| "restore it quickly after a crash" | No batch-6 winner; recoverability | Ask the user: which restored journey/state endpoint and loss allowance are required? Eventual return is not fault continuation. |
| "retries make the errors disappear" | 81 / 15 unresolved | Ask the user: is the failure unit an original attempt or a complete retried interaction, and is the concern occurrence or usability? |
| "prevent malformed requests starving real users" | 86 tentative; quality-of-service possible | Ask the user: controlled adverse traffic or differentiated obligations between service classes? |
| "is a low error rate enough to call this safe" | 87 | Ask the user: which harmful outcome and causal action/omission must the controls prevent? Error counts do not supply that model. |

## Cross-skill counts, evidence and limitations

Dependability has 5/7/5 rules/done/failures and Reliability 6/7/5; Fault Tolerance and Safety share 6/8/5. Five of six failure-mode lists have five items; Robustness has six. Counts are within the contract, but repeated result/coverage/shared-boundary guards supply much of the shape. Intent cannot be inferred from the matching counts.

Done items mostly map to distinct inspectable evidence: event units, ownership effects, coverage, valid controls and actual harm boundaries. Availability's last item includes ownership/decision follow-up rather than a new runtime verification. Dependability's seven items naturally concern the assurance case, not seven independent code tests.

Availability's expanded design guide demonstrates concrete deployment decisions; Fault Tolerance, Robustness and Safety also contain actual practices. Reliability's guide chiefly defines exposure and evidence. No implementation guarantee follows from the illustrative traces. Pilot content was reviewed in place and preserved.

Availability's frontmatter still includes status; the current template includes status too. This audit therefore does not claim a template violation merely because later skills keep status only in the catalogue.

All 36 rules were reviewed: 19 transferable, 17 partly and 0 specific. These are editorial judgments, not empirical model evaluations.

All five workflow steps in every audited skill contain an If/then decision. Every Clarify step directs inspection of existing code and documents before specification. Proposed records and confirmation language are present. Several fast paths group many decisions into three question groups; that can be more demanding than three short questions.

Every design reference has substantive use-when / trade-off / verify content; none is an empty heading skeleton. Every reference is below 150 lines. Meeting a line budget does not establish implementation depth or distinct acceptance logic.

No unlabeled universal numeric system target or unsupported external citation was found in these sources. Targets are illustrative and paired with user/stakeholder confirmation. Regulation labels are not evidence of legal duties. No source was verified through external browsing; this audit follows the repository-only boundary.

## Verification and uncertain claims

- Selected validation across batches 6-9: 25 skills checked, 0 absent todo skills, 0 errors.
- Full validation: 63 skills checked, 51 absent todo skills, 0 errors. Absent todo skills are unfinished catalogue entries.
- The Availability lower/upper/coverage arithmetic was independently recomputed and passed; other scenarios predominantly use symbolic state transitions rather than numerical calculations.
- No runtime, production, destructive, accessibility-user, fault-injection or stakeholder acceptance exercise was performed. Worked examples remain hypothetical.
- Routing ties, transfer labels and depth assessments are reviewer judgments. Count similarity cannot establish author intent. Real policies, fault feasibility, observer knowledge and acceptance authority remain project-specific unknowns.
- Skills and prior reviews are unchanged; no production batch was started.
