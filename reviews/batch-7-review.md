# Batch 7 findings

## Description-first routing

Six descriptions were authored before bodies and compared with the local
reliability/resilience boundaries, approved pilot entrypoints, and adjacent
batch-6 descriptions. The shared guide, rubric, disambiguation map, and allowlist
supplied the contract. All earlier skills and the approved pilots are preserved;
batch-6 approval is not a Phase-6 reviewed-status promotion.

This table reports manual semantic routing, not a model execution or keyword test.

| Request | Best fit / ambiguity | Acceptance question and first missing fact |
| --- | --- | --- |
| Do not leave half an update | atomicity | Which effects and observers belong to the all-or-none boundary? |
| Make the save safe | Tie: atomicity / durability / recoverability | Is the concern partial visibility, loss after acknowledgement, or restoring usable state? |
| Confirmed changes disappear after restart | durability | What acknowledgement promised preservation, and which event removes the state? |
| Restore from backup after the outage | recoverability | What usable state, allowed loss, and restored journey define completion? |
| Prove that our backup works | recoverability, durability may contribute | Is success a completed restore or persistence of acknowledged versions through a named event? |
| Is this release mature enough for wider use? | maturity | What intended use and actual operation/defect history support readiness? |
| Run this workload without failures | reliability outside batch | A future operating interval, not historical readiness evidence. |
| Stop this control from flapping | stability | Which control output, held/changed conditions, and permitted settling behavior? |
| Make response times predictable | predictability outside batch | General variability bounds; drift/oscillation is not established by the wording. |
| Stabilize the system | Tie: stability / reliability / robustness | Does stabilize mean control drift, crashes, or uncontrolled adverse conditions? |
| Keep essential dispatch working during a site loss | survivability | Which essential results, disrupted dependencies, mission duration, and permitted degradation? |
| Add automatic failover | fault-failure-tolerance / recoverability unresolved | Must results continue during the fault, or may service stop before restoration? |
| Disaster recovery | recoverability / survivability unresolved | Restore normal operation, or keep essential mission work functioning during the disruption? |
| Protect the data | No unique batch-7 route | Is the property disclosure, alteration, all-or-none update, acknowledged persistence, or restoration? |
| Everything should stay available | availability outside batch | Which user journeys/calendar; no essential-only mission boundary is supplied. |

Distinct trigger phrases do not force an answer to the vague save, stabilize,
backup, failover, and disaster requests. The descriptions carry their nearest
exclusions rather than depending on the body to supply every likely boundary.

## Full rule transfer findings

Every rule is quoted with the nearest plausible sibling in the repository map.
Transferable means the whole rule could move unchanged; partly means a shared
mechanism with a materially different acceptance question; specific means the
nearest tested sibling can legitimately accept a different outcome. These are
manual judgments, not results from an independent agent or user experiment.

### 011-atomicity

**Bullet 1: specific; nearest sibling `consistency`.**

> Don't count later compensation as all-or-none visibility; an observer that saw the partial effect already defeats that operation's visibility contract.

Later reconciliation can satisfy some explicit agreement models, while this rule rejects it as proof that no partial view ever occurred; the acceptance questions differ.

**Bullet 2: transferable; nearest sibling `consistency`.**

> Do inspect the observer's read boundary as well as the writes; assembling separate-time reads can mimic a partial view even when the commit is indivisible.

Coherent reader snapshots also prevent false disagreement reports between representations, so this entire observer-boundary check is reusable unchanged.

**Bullet 3: transferable; nearest sibling `recoverability`.**

> Do separate irreversible external publication from private intermediate work; a rolled-back local write does not retract an already observed external effect.

Restoration work must also account for external effects that local rollback cannot retract; this whole visibility/effect safeguard transfers.

**Bullet 4: partly; nearest sibling `durability`.**

> Don't infer atomicity from an all-success path; interruption between effects is exactly where the forbidden subset can become visible.

Both need interruption tests, but a forbidden participating subset is a visibility failure rather than disappearance of acknowledged state after an event.

**Bullet 5: partly; nearest sibling `durability`.**

> Do publish the operation result only at its real visibility boundary; returning success after an early participating write invites observers to accept a partial unit.

Acknowledgement ordering matters to both, but the required boundary here is joint participating visibility, not post-event persistence.

**Bullet 6: transferable; nearest sibling `recoverability`.**

> Do resolve an unknown commit outcome before replaying the operation; a lost acknowledgement is not evidence that no participating effects committed.

Recovery replay must also distinguish a lost acknowledgement from a genuinely uncommitted operation; the full unknown-outcome rule can move unchanged.

Count: 3 transferable, 2 partly, 1 specific.

### 039-durability

**Bullet 1: specific; nearest sibling `atomicity`.**

> Don't treat immediate read-after-write visibility as post-event preservation; the same live process may still be serving state the named failure would remove.

Immediate visibility can bear directly on all-or-none observation; this rule explicitly demands post-event preservation rather than accepting that visibility as evidence for the promised property.

**Bullet 2: transferable; nearest sibling `recoverability`.**

> Do anchor the expected-state ledger to observed acknowledgements, not attempted writes; otherwise unaccepted work can be misreported as lost confirmed state.

A recovery loss comparison also needs the expected set to distinguish acknowledged from merely attempted work; this whole accounting instruction transfers.

**Bullet 3: transferable; nearest sibling `recoverability`.**

> Do test the promised event boundary itself; a process restart cannot establish preservation across storage destruction when the same storage survives the test.

A recovery rehearsal also must not substitute a surviving-store restart for a destroyed-store scenario, so the event-scope check moves unchanged.

**Bullet 4: transferable; nearest sibling `fault-failure-tolerance`.**

> Don't count copies without tracing their failure dependencies and commit state; unconfirmed or jointly lost copies cannot justify the acknowledged-state promise.

Unconfirmed or jointly lost copies also cannot support a continued-result fault model; this dependency/commit safeguard is not exclusive.

**Bullet 5: transferable; nearest sibling `consistency`.**

> Do distinguish permitted supersession from missing persistence by identity/version; comparing only the latest value can incorrectly call a legitimate later change data loss.

Identity/version and legitimate supersession also distinguish disagreement from lawful updates across representations, making this whole comparison rule reusable.

**Bullet 6: partly; nearest sibling `atomicity`.**

> Do inspect acknowledgement ordering against the persistence condition; adding a backup later does not fix a success promise already sent before its required boundary.

Both inspect when success is emitted, but later backup creation relates to persistence after acknowledgement rather than whether participating changes were published together.

Count: 4 transferable, 1 partly, 1 specific.

### 065-maturity

**Bullet 1: specific; nearest sibling `reliability`.**

> Don't substitute release age for exercised experience; an old but unused feature supplies no operating history for the new audience that will depend on it.

Reliability can accept a new future trial without historical age, while this rule specifically rejects deployment age as demonstrated experience of intended use.

**Bullet 2: transferable; nearest sibling `maintainability`.**

> Do link recurring defects across renamed tickets and releases; administrative closure must not reset the record of unresolved operating experience.

Maintenance investigation can also require linked recurring defects despite ticket closure; the whole operational-record rule is reusable.

**Bullet 3: transferable; nearest sibling `reliability`.**

> Do distinguish code-fixed from followed-up in relevant operation; a patch's presence does not establish that the reported failure stayed resolved after use.

A reliability defect claim also cannot infer sustained operational resolution from a patch alone; this repair/follow-up distinction transfers unchanged.

**Bullet 4: transferable; nearest sibling `dependability`.**

> Don't import another environment's incident-free history without its context; changed workloads or configurations can leave the intended release insufficiently experienced.

A combined reliance case likewise cannot import irrelevant environment history, so the evidence-context limitation fits unchanged.

**Bullet 5: transferable; nearest sibling `reliability`.**

> Do preserve observation gaps beside quiet incident periods; missing failure reports cannot support demonstrated readiness when qualifying operation was unobserved.

Observation gaps also prevent a clean operational failure-history claim, so retaining them is a shared evidence safeguard.

Count: 4 transferable, 0 partly, 1 specific.

### 080-recoverability

**Bullet 1: partly; nearest sibling `availability`.**

> Don't stop the recovery clock at process startup; restored state and the agreed business journey must be verified before declaring the restoration endpoint.

Availability also needs actual journey usability, but the full instruction defines the end of a restoration procedure rather than a service-calendar good-time sample.

**Bullet 2: transferable; nearest sibling `survivability`.**

> Do account for credentials, keys, artifacts, and control dependencies in the disrupted boundary; a backup cannot restore service through an unavailable prerequisite.

An essential alternate also fails when required credentials, artifacts, or controls lie inside the severe disruption; this whole dependency rule transfers.

**Bullet 3: partly; nearest sibling `durability`.**

> Do reconcile snapshot and replay boundaries before reopening writers; gaps lose required work and overlaps can repeat effects despite a clean restore log.

Replay gaps and overlap can lose preserved results too, but reopening writers after restoration is a larger procedure than proving persistence of an acknowledged change.

**Bullet 4: transferable; nearest sibling `durability`.**

> Don't infer acceptable lost work from backup frequency; compare actual restored state with the stakeholder's loss allowance and acknowledged-state obligations.

Neither property can infer acceptable lost acknowledged state from backup cadence; the same stakeholder loss/promise comparison applies unchanged.

**Bullet 5: transferable; nearest sibling `survivability`.**

> Do record warm caches, preloaded secrets, and already-running dependencies in a rehearsal; they can hide recovery work that the declared disruption removes.

Warm credentials and dependencies can also fabricate an alternate mission path surviving a disruption, so the whole rehearsal-honesty instruction transfers.

**Bullet 6: transferable; nearest sibling `atomicity`.**

> Do classify ambiguous in-flight work before replay; retrying everything can restore apparent throughput while duplicating effects outside the recovery contract.

Resolving ambiguous commit outcomes before replay is also needed to avoid a second logical operation; this full effect-boundary instruction is reusable.

Count: 4 transferable, 2 partly, 0 specific.

### 092-stability

**Bullet 1: partly; nearest sibling `predictability`.**

> Don't average away alternating control states; a quiet mean can conceal the repeated reversals that the mode-stability requirement actually forbids.

A variation analysis can also retain raw alternation, but repeated control-state reversal is a narrower failure criterion than general observed variability.

**Bullet 2: partly; nearest sibling `predictability`.**

> Do separate genuine input changes from held-condition drift; responding to changing demand is not itself evidence that a controller is unstable.

Both condition observations on inputs, while the whole instruction distinguishes justified control response from held-condition drift rather than general outlier variation.

**Bullet 3: partly; nearest sibling `performance-efficiency-time-or-space-bounds`.**

> Do evaluate a transition band or dwell rule against missed genuine changes; a frozen or sluggish output can stop flapping while failing the required response.

Response delay can be a performance concern, but the paired reversal-versus-responsiveness trade-off specifically governs whether the anti-flapping rule is acceptable.

**Bullet 4: transferable; nearest sibling `observability`.**

> Do align input, action, and observation windows before attributing oscillation; stale measurements can make a justified response look like self-generated reversal.

Aligned fresh measurements also determine whether runtime evidence supports causal interpretation, so this full time-alignment safeguard can move unchanged.

**Bullet 5: partly; nearest sibling `reliability`.**

> Do trace coupled feedback decisions together; independently reasonable controllers can reverse each other's actions and defeat the declared steady operating behavior.

Interacting controllers can cause required-behavior failures, but their reversing feedback trace directly defines the oscillation acceptance question here.

**Bullet 6: transferable; nearest sibling `predictability`.**

> Don't exclude unsettled intervals after seeing the candidate trace; the agreed settling rule must determine which reversals count toward the accepted bound.

A variability review also cannot choose favorable settling exclusions after inspecting the data; this complete window-selection rule transfers.

Count: 2 transferable, 4 partly, 0 specific.

### 097-survivability

**Bullet 1: partly; nearest sibling `fault-failure-tolerance`.**

> Do prioritize the essential result explicitly before dropping normal features; preserving a convenient subset is not evidence that the stakeholder's mission survived.

A degraded fault contract must also preserve accepted results, but selecting mission priorities before deferring normal functions is specific to the essential-only severe-disruption scope.

**Bullet 2: transferable; nearest sibling `fault-failure-tolerance`.**

> Don't count a standby path as surviving if it still needs a lost control or identity service; the severe-disruption boundary includes those dependencies too.

A routine fault alternate can share the same hidden identity/control dependency too; this whole alternate-path safeguard moves unchanged.

**Bullet 3: partly; nearest sibling `safety`.**

> Do exercise essential decisions with the degraded data and authority actually available; borrowing normal permissions or fresh data can fabricate mission continuity.

Degraded authority and data can affect harmful decisions, but this instruction accepts essential mission work under surviving resources rather than hazard prevention alone.

**Bullet 4: specific; nearest sibling `recoverability`.**

> Don't replace during-disruption result evidence with an eventual normal restore; a recovered system may conceal an interval in which the essential mission stopped.

Recoverability legitimately accepts service restoration after a gap; this rule explicitly rejects that as evidence of results during the disruption.

**Bullet 5: transferable; nearest sibling `recoverability`.**

> Do reconcile alternate-mode work before handing authority back; unresolved duplicate or conflicting mission actions can invalidate the result preserved during disruption.

Restoration resumption likewise needs reconciliation of alternate work and actual effects, so this complete handback rule fits unchanged.

**Bullet 6: specific; nearest sibling `availability`.**

> Do retain nonessential losses separately from essential-result failures; requiring every normal feature confuses the scoped survival contract with ordinary availability.

The rule allows scoped nonessential losses and rejects requiring every normal feature; ordinary journey/calendar availability must use its accepted service boundary instead.

Count: 2 transferable, 2 partly, 2 specific.

Across all rules: 19 transferable, 11 partly, 5 specific.
Shared observer, event-scope, evidence, and replay practices remain substantial transfer limitations. Distinct acceptance records and descriptions carry the routing boundary; low literal similarity cannot prove semantic exclusivity.

## Per-skill findings and weaknesses

- **Atomicity:** Participating effects, authorized observers, coherent reads,
  publication, and irreversible external effects are explicit. The worked example
  shows both forbidden partial assignment states and a mixed-time reader artifact.
  It does not identify a real transaction/snapshot primitive or prove that the
  proposed private-public boundary exists. Unknown-commit handling and external
  effect limitations also fit Recoverability, so they cannot route the request
  by themselves. A simple final-state test remains inadequate for this contract.
- **Durability:** Acknowledgement, expected state, post-event authority, and event
  scope distinguish preservation from visibility and service restoration. The
  document example carries a confirmed save and an ambiguous later attempt rather
  than treating every attempted write as acknowledged. Actual persistence ordering
  and retrieval authority remain unverified. The version gate is subject to the
  explicit supersession/history contract; it must not silently require retaining
  historical versions when only the current valid state was promised.
- **Maturity:** The intended-use ledger, defect lineage, repair verification,
  and post-fix operation make historical readiness inspectable. Most repository
  work is source/history investigation and evidence/documentation updates rather
  than a direct product algorithm. Relevance of prior episodes and required
  follow-up remain judgment calls; no calendar age, ticket count, or invented
  maturity level supplies readiness. The example's suspected recurrence remains
  uncertain instead of claiming a common cause from similar symptoms alone.
- **Recoverability:** Bootstrap dependencies, snapshot/replay scope, ambiguous
  external effects, milestone timing, and recovered business results provide a
  concrete restoration procedure. The order example cannot promise an external
  deduplication primitive or exactly-once effects. Real loss allowances, restore
  authority, and cold dependency availability remain unresolved. Several replay
  and dependency safeguards transfer to Durability, Atomicity, or Survivability.
- **Stability:** The rule set separates steady inputs, sampled signal, control
  action, settling, and genuine-change response. The symbolic economy/burst trace
  makes a frozen-output false positive explicit. The example supplies no numeric
  transition bands, sampled measurements, or proven controller response; those
  belong to the target's actual envelope. Window alignment and predeclared
  exclusions remain useful unchanged in Observability and Predictability too.
- **Survivability:** Mission priority, independent survivors, degraded authority,
  actual recipient acknowledgement, deferred work, and handback distinguish the
  example from process survival or later normal restoration. The approved local
  roster, communication path, and operator authority are assumed inputs to verify,
  not permission supplied by an offline/manual label. The worked example covers
  one selected site-loss scenario and reachable teams; it establishes neither
  every severe disruption nor a generally safe alternate mode.

Internal rubric assessment found the structural criteria present and retained
rule specificity as a real improvement area. No perfect-score claim is made.
These findings are an author review, not an independent assurance verdict or
observed target-system behavior.

## Distinct checks and count rationale

- Atomicity checks participation, coherent views, actual publication, interrupted
  observations, abort effects, unknown completion, and private/read/visible distinctions.
- Durability checks acknowledged state, independent oracle, promise ordering,
  event coverage, authoritative contents, supersession/ambiguity/loss classification,
  and shared copy dependencies.
- Maturity checks intended-use relevance, actual episodes, observation quality,
  defect recurrence, fix/follow-up links, contrary incidents, and planned-versus-demonstrated use.
- Recoverability checks endpoint/loss, bootstrap, actual restore inputs, replay
  boundary, work classification, business usability, full milestone timing, and shortcuts.
- Stability checks envelope/settling, time alignment, held-condition behavior,
  genuine-change response, missing samples/disabled control, coupled loops, and exclusions.
- Survivability checks essential priority, loss/survivor map, alternate closure,
  authority/data, during-event outputs, work identity, reconciled handback, and separate losses.

Rule/check/failure counts are Atomicity 6/7/5; Durability 6/7/5; Maturity 5/7/5;
Recoverability 6/8/6; Stability 6/7/5; Survivability 6/8/6. Matching counts are
visible and not a quality claim. Items follow the independent evidence needs
above rather than repeating the five workflow steps or filling an item quota.

## References and line budgets

Every guide gives concrete use-when, trade-off, and verification practices.
Atomicity addresses observers and external effects; Durability addresses promises,
copy state, independent oracles, and supersession; Maturity addresses demonstrated
use and defect follow-up; Recoverability addresses bootstrap, replay, validation,
and interrupted/warm rehearsals; Stability addresses aligned feedback traces and
response trade-offs; Survivability addresses priorities, surviving resources,
degraded authority, work ledgers, and handback. No guide is just a list of headings.

Each worked example carries explicit synthetic input, expected output, and state
or evidence across checkpoints. All examples disclose their hypothetical nature
and missing implementation evidence. No reference links through to another reference.

| Skill | Description characters | Body | Complete SKILL.md | Design guide | Worked example | Combined |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| atomicity | 456 | 123 | 128 | 35 | 41 | 204 |
| durability | 487 | 122 | 127 | 35 | 36 | 198 |
| maturity | 475 | 121 | 126 | 35 | 36 | 197 |
| recoverability | 518 | 125 | 130 | 44 | 35 | 209 |
| stability | 473 | 122 | 127 | 35 | 34 | 196 |
| survivability | 560 | 125 | 130 | 43 | 36 | 209 |

All individual references are under 150 lines and all combined footprints meet
the 150-250 guideline. These authoring counts establish neither semantic
exclusivity nor a guarantee about the example systems.

## Final routing consistency

Body review retains the description-first routing table. The ambiguous save,
stabilize, backup, failover, and disaster requests still need the listed first
question. No body expands its description to claim every use of safe, proven,
or disaster. All-or-none views, acknowledged preservation, historical readiness,
restored usability, drift/oscillation, and essential mission persistence remain
distinct acceptance questions despite shared verification mechanisms.
No Phase-5 evals, keyword-overlap ranking, or live-agent routing experiment was performed.

## Uncertain claims

- **Atomicity:** The real participating set, observer coherence, commit boundary,
  external effects, abort semantics, and unknown-result resolution need source/user
  confirmation. The assignment example establishes no storage transaction guarantee.
- **Durability:** Acknowledgement meaning, persistence condition, surviving storage,
  event model, authoritative retrieval, and supersession/history obligations remain
  target-project decisions. The document trace proves no actual retained data or
  device/site-loss protection.
- **Maturity:** Intended use, relevant historical exposure, severity, recurrence
  linkage, repair effectiveness, observation quality, and readiness authority need
  evidence. Fictional release records establish no actual operational maturity or
  future failure probability.
- **Recoverability:** Restored business state, allowable loss, timing anchors,
  keys/artifacts, snapshot/replay semantics, external effects, and resumption rights
  require confirmation. No backup import, measured recovery time, or actual exactly-once
  behavior was produced by the example.
- **Stability:** Actual control variables, noise, input/environment bands, settling,
  transition rules, sampling, feedback coupling, and responsiveness limits are unknown.
  A symbolic candidate trace is not an observed stability result or universal control design.
- **Survivability:** Essential mission decisions, severity/scope, surviving resources,
  degraded authority/data, recipient reachability, duration, and handback effect
  rules require stakeholder/source evidence. No local roster or alternate grants
  real permission, and no actual site loss or mission persistence was tested.

Ask the user for unknown context. No standards, URLs, clause numbers, legal
obligations, platform-specific flags, library versions, or population statistics
were added. Numeric system targets are illustrative and paired with stakeholder
confirmation. Mechanisms are options to inspect in the real code, not inferred
product guarantees or claims of executed tests.

## Validation evidence

- `python scripts/validate_skills.py --only 11,39,65,80,92,97`: six skills, zero errors.
- `python scripts/validate_skills.py`: 45 skills checked, 69 absent todo entries, zero errors.
- `python -m unittest discover -s tests -v`: all 19 foundation tests passed.
- Skill-creator frontmatter validation: all six new skills valid.
- Catalogue/scope checks passed: only the six authorized statuses became draft;
  earlier skills, approved pilots, shared contracts, scripts, tests, and the
  similarity threshold remain unchanged.
- Workflow decisions and code/docs inspection, description triggers, numeric labels,
  direct links, individual limits, and combined footprints passed scoped checks.
- All 35 Rules of thumb bullets have named-sibling transfer findings: 19 transferable,
  11 partly transferable, and 5 specific against the nearest tested sibling.
- Maximum batch-involving body five-gram Jaccard is 0.015909090909090907 for
  atomicity/durability, below unchanged 0.35. Literal similarity does not detect
  or resolve the semantic transfers recorded above.
