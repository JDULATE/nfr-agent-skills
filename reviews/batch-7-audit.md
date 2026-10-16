# Batch 7 audit

## Basis and principal findings

This skeptical source review covers every skill assigned to this batch in nfr-list.json, including any approved pilot, and every reference file under those skills. The authoring guide, rubric, disambiguation map and allowlist provide the contract. Existing reviews were not read as evidence. This is an agent review, not an independent human or blinded evaluation. No skill, catalogue, index, validator or threshold was changed.

- **Concrete routing inconsistency in Survivability.** Its body contrasts mission scope with Availability's normal all-journey accounting, and its description excludes all-service uptime. Availability actually supports a named journey and audience. Severe disruption, surviving resources and mission/authority constraints distinguish these skills; an all-services assumption does not.
- **Maturity is primarily an evidence review.** The skill honestly advertises operational-history assessment, but its Design/Implement label should not be mistaken for a repository code-change method. New documentation cannot manufacture post-fix operating experience.
- **State examples are generally stronger than filled execution procedures.** Atomicity and Durability have concrete identities and state oracles; Recovery and Survivability identify reconciliation but leave the difficult ambiguous/conflicting effect resolution unfilled.
- **There are useful positive practices.** Atomicity stages private work, Stability introduces explicit transition rules and Recovery bootstraps dependencies. The batch is not only a set of generic cautions, although several Rules of thumb are portable safeguards.

## Structure and description measurements

Line counts include blank lines; body excludes frontmatter. Combined includes full SKILL.md and all its references. These are authoring counts, not system targets.

| Id / slug | Description characters | Body / full | Reference lines | Combined | Rules / done / failure modes |
| --- | ---: | --- | --- | ---: | --- |
| 011 atomicity | 456 | 123 / 128 | design-patterns.md: 35; worked-example.md: 41 | 204 | 6 / 7 / 5 |
| 039 durability | 487 | 122 / 127 | design-patterns.md: 35; worked-example.md: 36 | 198 | 6 / 7 / 5 |
| 065 maturity | 475 | 121 / 126 | design-patterns.md: 35; worked-example.md: 36 | 197 | 5 / 7 / 5 |
| 080 recoverability | 518 | 125 / 130 | design-patterns.md: 44; worked-example.md: 35 | 209 | 6 / 8 / 6 |
| 092 stability | 473 | 122 / 127 | design-patterns.md: 35; worked-example.md: 34 | 196 | 6 / 7 / 5 |
| 097 survivability | 560 | 125 / 130 | design-patterns.md: 43; worked-example.md: 36 | 209 | 6 / 8 / 6 |

## Per-skill findings and full transfer test

Each source bullet is quoted in full, in its original order. Transferable means the entire bullet could serve the named sibling unchanged. Partly means the technique transfers but the acceptance framing needs alteration. Specific means that sibling has a different acceptance question. Shared safeguards can be necessary without satisfying the stricter requirement for distinctive Rules of thumb. Judgments use the repository conventions; they do not claim standardized meanings.

### 011 atomicity

**Description and boundary:** All-or-none visibility, operation effects and observer are clear; Durability/Recoverability/Consistency exclusions appear in the description. Vague make this transactional language still needs the operation boundary and may mean durability instead.

**Repository actions and design depth:** Map participating effects, keep private staged work, choose a publication boundary and capture coherent observer snapshots. These are actual practices, not only evidence headings. The design remains tool-agnostic and correctly does not promise simultaneous visibility to independent external recipients.

**Worked example:** Named job and team, explicit complete-before/after and both forbidden subsets, failed between-write path, later compensation and mixed-time reader make a concrete state example. A successful candidate publication mechanism is not instantiated, so it is a contract illustration rather than executable storage design.

**Three weakest passages:**

- `references/worked-example.md`: "A candidate must change the real commit/publication mechanism" - The faulty state is clear, but the repaired mechanism and its actual boundary are not filled.
- `references/design-patterns.md`: "a snapshot/version rule" - Names the necessary observer contract without a concrete reader schedule demonstrating both coherent and incoherent views.
- `SKILL.md`: "resolve an unknown commit outcome before replaying the operation" - Useful but transferable to Recoverability; it does not specifically prevent partial visibility.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't count later compensation as all-or-none visibility; an observer that saw the partial effect already defeats that operation's visibility contract. | consistency | Partly | Compensation and history matter to agreement too, but simultaneous all-or-none visibility is the current acceptance question. |
| 2. Do inspect the observer's read boundary as well as the writes; assembling separate-time reads can mimic a partial view even when the commit is indivisible. | consistency | Transferable | A mixed-time reader can also fabricate disagreement between representations without a stored inconsistent state. |
| 3. Do separate irreversible external publication from private intermediate work; a rolled-back local write does not retract an already observed external effect. | integrity | Transferable | Rolling back local state cannot undo an externally visible prohibited alteration either. |
| 4. Don't infer atomicity from an all-success path; interruption between effects is exactly where the forbidden subset can become visible. | durability | Partly | Success-only tests are weak evidence for both; the forbidden subset specifically concerns atomic visibility rather than post-event preservation. |
| 5. Do publish the operation result only at its real visibility boundary; returning success after an early participating write invites observers to accept a partial unit. | durability | Partly | Acknowledgement ordering transfers, but early partial publication and lost acknowledged persistence are different promises. |
| 6. Do resolve an unknown commit outcome before replaying the operation; a lost acknowledgement is not evidence that no participating effects committed. | recoverability | Transferable | The recovery guide also must classify unknown in-flight commits before replay to avoid duplicate effects. |

Transfer counts: 3 transferable; 3 partly; 0 specific.

### 039 durability

**Description and boundary:** Acknowledged identity/version plus subsequent event distinguishes the property. Verify committed writes survive storage failure is a valid trigger only after the actual loss event and promise are narrowed; the default example covers process restart, not storage destruction.

**Repository actions and design depth:** Trace persistence/acknowledgement ordering, retain an independent oracle, map copy failure domains and retrieve authoritative post-event state. These are concrete review/test actions. The guide does not instantiate a persistence-condition change or a loss exercise beyond process restart.

**Worked example:** Named document, confirmed content/version, unknown later save and legitimate supersession are concrete carried state. It deliberately leaves the unknown save unresolved and does not assume the old version remains queryable. This is a good negative interpretation example, but not a completed ambiguity-resolution trace.

**Three weakest passages:**

- `SKILL.md`: "Trial gate: 0 missing acknowledged versions" - Versions can suggest historical retention even though the later text correctly allows a latest-state promise; the shorthand gate needs the supersession qualification beside it.
- `references/worked-example.md`: "Unknown save-mint resolved" - The table labels a resolution checkpoint without filling the authoritative observation that resolves the unknown outcome.
- `references/design-patterns.md`: "inspect the implementation/config rather than assuming a flush or replica label suffices." - Correct review discipline, but no positive example selects and verifies a concrete persistence boundary.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't treat immediate read-after-write visibility as post-event preservation; the same live process may still be serving state the named failure would remove. | recoverability | Partly | Warm-read limitations transfer, but preserved acknowledged state differs from restoration of the usable system. |
| 2. Do anchor the expected-state ledger to observed acknowledgements, not attempted writes; otherwise unaccepted work can be misreported as lost confirmed state. | recoverability | Transferable | Lost-work reconciliation must also distinguish confirmed acknowledgements from attempted work. |
| 3. Do test the promised event boundary itself; a process restart cannot establish preservation across storage destruction when the same storage survives the test. | fault-failure-tolerance | Partly | Exercising the actual model transfers; this rule frames the result as preservation rather than continued service. |
| 4. Don't count copies without tracing their failure dependencies and commit state; unconfirmed or jointly lost copies cannot justify the acknowledged-state promise. | recoverability | Transferable | The restore promise also depends on copy versions, confirmation state and shared loss dependencies. |
| 5. Do distinguish permitted supersession from missing persistence by identity/version; comparing only the latest value can incorrectly call a legitimate later change data loss. | integrity | Transferable | Permitted version changes must also be distinguished from unintended alteration when judging protected current state. |
| 6. Do inspect acknowledgement ordering against the persistence condition; adding a backup later does not fix a success promise already sent before its required boundary. | recoverability | Partly | Acknowledgement/persistence obligations constrain the recovery loss allowance, but response ordering is primarily the preservation promise. |

Transfer counts: 3 transferable; 3 partly; 0 specific.

### 065 maturity

**Description and boundary:** Readiness from actual operating and defect-handling history is honest. Is this release proven enough overlaps Dependability until the decision is specifically historical readiness rather than a broader reliance case.

**Repository actions and design depth:** Mostly code-history reading, release/incident reconciliation, defect lineage and an evidence ledger. This is primarily documentary assessment, not implementation work; the description correctly says assesses. The narrow honest scope is intended-use operational-readiness evidence, with planned qualification kept separate.

**Worked example:** Named releases, contexts, defect records, suspected recurrence and future bulk plan carry a concrete distinction between historical and proposed evidence. Actual episode durations, deployed patch identity and a post-fix observed result are not filled. No implementation output is implied by ticket bookkeeping.

**Three weakest passages:**

- `SKILL.md`: "each readiness condition supported, explicitly conditional, or unresolved." - This classifies evidence but does not specify which conditional/unresolved states permit wider use; the decision owner remains necessary.
- `references/worked-example.md`: "Same suspected symptom after patch under new ticket" - A useful suspected recurrence, but the example does not show the evidence that distinguishes shared cause from coincident symptoms.
- `references/worked-example.md`: "Add missing follow-up locations to the evidence ledger" - Adds bookkeeping without supplying the absent operational follow-up; correctly not a repair of demonstrated experience.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't substitute release age for exercised experience; an old but unused feature supplies no operating history for the new audience that will depend on it. | reliability | Partly | Exercised profile rather than age transfers; demonstrated history for a new audience is a readiness question. |
| 2. Do link recurring defects across renamed tickets and releases; administrative closure must not reset the record of unresolved operating experience. | maintainability | Transferable | Maintenance diagnosis also needs causal defect lineage rather than administrative ticket closure. |
| 3. Do distinguish code-fixed from followed-up in relevant operation; a patch's presence does not establish that the reported failure stayed resolved after use. | reliability | Transferable | A code patch alone also does not demonstrate continued required behavior under the relevant operational profile. |
| 4. Don't import another environment's incident-free history without its context; changed workloads or configurations can leave the intended release insufficiently experienced. | reliability | Transferable | Incident-free results from a different profile cannot establish the intended scenario without context. |
| 5. Do preserve observation gaps beside quiet incident periods; missing failure reports cannot support demonstrated readiness when qualifying operation was unobserved. | dependability | Transferable | An operational reliance case also cannot treat unobserved quiet periods as positive readiness support. |

Transfer counts: 4 transferable; 1 partly; 0 specific.

### 080 recoverability

**Description and boundary:** Restored usability/state, loss allowance and replay are clear; continuation and acknowledged persistence are excluded. Resume interrupted work without replaying it twice also fits the fault-handoff identity concern and needs the before/after interruption distinction.

**Repository actions and design depth:** Dependency bootstrap, coherent snapshot/replay boundary, in-flight reconciliation and full journey milestones are real practices. The guide names resumable recovery but does not work through a failed intermediate recovery and restart.

**Worked example:** Snapshot includes a named order, replay repeats it and introduces another, then reconciles actual effects before journey validation. The milestone table has no filled timestamps or replay positions. The second order may have an external effect; the example honestly marks it unknown instead of assuming exactly-once execution.

**Three weakest passages:**

- `references/worked-example.md`: "Retain bootstrap, import, replay, and validation timestamps" - Lists required clock state without filling a trace that exercises the illustrative deadline.
- `references/design-patterns.md`: "inspect intermediate state, retry/resume effects, and all shortcuts" - Interrupted recovery is named but no intermediate progress/ownership state demonstrates a safe resumption.
- `SKILL.md`: "classify ambiguous in-flight work before replay" - The principle is concrete but also belongs in Atomicity/ownership handoff; a recovery-specific resolution example is still absent.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't stop the recovery clock at process startup; restored state and the agreed business journey must be verified before declaring the restoration endpoint. | availability | Partly | A real business result rather than healthy process transfers; elapsed restoration rather than usable-time accounting is the current unit. |
| 2. Do account for credentials, keys, artifacts, and control dependencies in the disrupted boundary; a backup cannot restore service through an unavailable prerequisite. | survivability | Transferable | The severe-disruption alternate must likewise obtain keys and control prerequisites without lost normal dependencies. |
| 3. Do reconcile snapshot and replay boundaries before reopening writers; gaps lose required work and overlaps can repeat effects despite a clean restore log. | durability | Partly | Required-state preservation is relevant, but rebuilding a coherent snapshot/replay state before reopening writers is restoration-specific framing. |
| 4. Don't infer acceptable lost work from backup frequency; compare actual restored state with the stakeholder's loss allowance and acknowledged-state obligations. | durability | Transferable | Backup frequency cannot determine acceptable loss of acknowledged changes under that promise either. |
| 5. Do record warm caches, preloaded secrets, and already-running dependencies in a rehearsal; they can hide recovery work that the declared disruption removes. | survivability | Transferable | Borrowed warm credentials or normal services also invalidate a continuity trial whose disruption removes them. |
| 6. Do classify ambiguous in-flight work before replay; retrying everything can restore apparent throughput while duplicating effects outside the recovery contract. | atomicity | Partly | Unknown-commit handling transfers; duplicate replay effects after restoration are not the same as partial visibility. |

Transfer counts: 3 transferable; 3 partly; 0 specific.

### 092 stability

**Description and boundary:** Flapping, directional drift and oscillation distinguish general outcome variation. Description exclusions are useful. Make this stable without a control/held-input fact still ties Reliability, Predictability or Robustness.

**Repository actions and design depth:** Aligned traces, explicit enter/exit bands, dwell, settling and coupled-feedback review are concrete. It gives a positive candidate state rule and tests responsiveness rather than accepting frozen output.

**Worked example:** Economy/burst states and near-boundary versus genuinely sustained input demonstrate carried mode state and candidate hysteresis-style behavior without naming a universal threshold. Enter/exit conditions, timestamps, settling and actual delayed measurements stay symbolic; drift and coupled-controller branches have no filled examples.

**Three weakest passages:**

- `references/worked-example.md`: "Near-boundary above signal" - The signal value, boundary and time are symbolic, so a reader cannot reproduce the candidate trace numerically.
- `references/design-patterns.md`: "trace each controller" - Coupled-loop review is a useful practice but no joint-state sequence shows the reciprocal actions it is meant to diagnose.
- `SKILL.md`: "the agreed settling rule must determine which reversals count" - Important predeclaration hygiene that can move unchanged to Predictability; it is not distinctive control design advice.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't average away alternating control states; a quiet mean can conceal the repeated reversals that the mode-stability requirement actually forbids. | predictability | Partly | Extremes hidden by averages transfer, but repeated control-state reversals rather than general spread supply this rule. |
| 2. Do separate genuine input changes from held-condition drift; responding to changing demand is not itself evidence that a controller is unstable. | predictability | Partly | Condition grouping transfers; justified feedback response versus controller instability is the narrower acceptance issue. |
| 3. Do evaluate a transition band or dwell rule against missed genuine changes; a frozen or sluggish output can stop flapping while failing the required response. | predictability | Partly | Preserving absolute responsiveness alongside reduced variation transfers, but dwell/band control choices are Stability-specific framing. |
| 4. Do align input, action, and observation windows before attributing oscillation; stale measurements can make a justified response look like self-generated reversal. | analyzability | Partly | Time-aligned evidence transfers; oscillation attribution requires the actual feedback acceptance question. |
| 5. Do trace coupled feedback decisions together; independently reasonable controllers can reverse each other's actions and defeat the declared steady operating behavior. | predictability | Partly | Coupled causes can affect variation too, but reciprocal control actions defeating steady behavior describe the specific instability. |
| 6. Don't exclude unsettled intervals after seeing the candidate trace; the agreed settling rule must determine which reversals count toward the accepted bound. | predictability | Transferable | Predeclared transient/window exclusions also prevent manufacturing a favorable variability result after observation. |

Transfer counts: 1 transferable; 5 partly; 0 specific.

### 097 survivability

**Description and boundary:** Severe disruption, essential mission and surviving authority are clear. The Not for all-service uptime exclusion implies Availability needs all services, although its actual skill accepts a named critical journey.

**Repository actions and design depth:** Choose essential results, close surviving dependencies, bind degraded authority/data and reconcile handback. These are concrete continuity actions; implemented offline identity or ledger merging is not assumed.

**Worked example:** Named assignment/team, lost central store/identity, surviving roster/authority/channel and recipient acknowledgement supply meaningful mission state. Actual acknowledgement record, local ledger contents and conflicting handback case are not filled. This is more than process planning, but the hardest reconciliation branch remains a proposed check.

**Three weakest passages:**

- `SKILL.md`: "normal all-journey usable-time accounting" - Availability can measure a selected journey; this contrast makes the sibling boundary narrower than the sibling actually is.
- `references/design-patterns.md`: "rehearse pending and conflicting actions" - The guide does not fill a conflicting alternate/normal authority case or show its reconciliation.
- `references/worked-example.md`: "independently usable operator authority" - An explicitly assumed survivor, but no local authority/version/expiry state demonstrates its independence during the horizon.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do prioritize the essential result explicitly before dropping normal features; preserving a convenient subset is not evidence that the stakeholder's mission survived. | fault-failure-tolerance | Partly | Preserving the agreed subset transfers, but essential mission prioritization under severe disruption is the current scope. |
| 2. Don't count a standby path as surviving if it still needs a lost control or identity service; the severe-disruption boundary includes those dependencies too. | fault-failure-tolerance | Transferable | A continuation path also cannot depend on the identity or control service removed by its fault model. |
| 3. Do exercise essential decisions with the degraded data and authority actually available; borrowing normal permissions or fresh data can fabricate mission continuity. | fault-failure-tolerance | Transferable | An accepted degraded continuation contract also cannot borrow unavailable authority or fresh data. |
| 4. Don't replace during-disruption result evidence with an eventual normal restore; a recovered system may conceal an interval in which the essential mission stopped. | fault-failure-tolerance | Transferable | Later restoration also cannot prove required service continued during a held fault. |
| 5. Do reconcile alternate-mode work before handing authority back; unresolved duplicate or conflicting mission actions can invalidate the result preserved during disruption. | recoverability | Transferable | Reconciliation before normal authority resumes also prevents duplicate or conflicting restored work. |
| 6. Do retain nonessential losses separately from essential-result failures; requiring every normal feature confuses the scoped survival contract with ordinary availability. | availability | Partly | Scoped required versus optional results matter to Availability too; its contract need not include every ordinary feature. |

Transfer counts: 4 transferable; 2 partly; 0 specific.

## Routing probes

Manual semantic probes expose missing facts; these are not measured routing accuracy. A tentative lead does not erase a tie or authorize assumptions.

| Realistic prompt | Best fit / tie | First question and reason |
| --- | --- | --- |
| "make this stable" | 92 / reliability / predictability unresolved | Ask the user: control drift/flapping, qualifying failures, or variation of outcomes? The word alone supplies no mechanism. |
| "make these writes transactional" | 11 / 39 unresolved | Ask the user: all-or-none visible effects or preservation after acknowledgement, and which effects/observers participate? |
| "we lose saved changes after restart" | 39 | Ask the user: which acknowledgement, content/version and subsequent event does the promise cover? |
| "our backups need to work" | 80 tentative; 39 plausible | Ask the user: restored journey/state after disruption or preservation of every acknowledged change through a specified loss event? |
| "can we trust this old release" | 65 tentative; dependability/trustability plausible | Ask the user: historical intended-use readiness or a broader reliance/delegation decision? Release age alone does not decide. |
| "stop the system flapping" | 92 | Ask the user: which control state, held inputs and genuine-change response must be preserved? |
| "keep dispatch working if the site is gone" | 97 tentative; fault-failure-tolerance also fits | Ask the user: which essential mission subset, surviving resources and severe disruption distinguish this from a routine fault model? |
| "recover without duplicate jobs" | 80 tentative; 11 also relevant | Ask the user: what completed/pending/unknown effect state exists at the restore/replay boundary? |
| "never lose data" | 39 tentative; 80 possible | Ask the user: which acknowledged state and event model, and is the promise preservation or reconstructable service with a loss allowance? |
| "we see half an update then it fixes itself" | 11 tentative; consistency possible | Ask the user: did a coherent observer see separately committed effects, or assemble different complete versions through separate-time reads? |
| "let us work offline during outages" | 97 tentative; portability/mobility concerns possible | Ask the user: a severe essential-mission continuity mode or a different relocation/connectivity workflow, with what authority/data limits? |
| "is this ready for more customers" | 65 tentative; scalability also plausible | Ask the user: readiness from actual history or acceptable service/resource behavior as active demand grows? |

## Cross-skill counts, evidence and limitations

Atomicity, Durability and Stability share the complete 6/7/5 count triple. Recoverability and Survivability share 6/8/6. All six design guides use use-when/trade-off/verify entries; four are exactly 35 lines, while Recovery and Survivability are longer. This suggests a common template, not proof that counts were chosen before content. Differences correspond to real replay/bootstrap and mission/authority branches.

All combined footprints fall within the guideline. Done items mostly map to distinct checks, although Maturity's seven checks are evidence reconciliation rather than seven independent runtime tests. Recovery's clock endpoint, restored state and journey assertions are related but verify distinct things; they should not be collapsed merely to vary counts.

Durability explicitly separates historical-version retention from latest-state preservation, and Atomicity explicitly separates stored partial commits from mixed-time observer artifacts. These are substantive boundaries, not filler. The negative missing-version shorthand remains less precise than the fuller Durability explanation.

The default windows and gates are labeled illustrative. No statistical failure probability, storage primitive, exactly-once mechanism or device/site-loss guarantee is invented. Verification still depends on actual source and controlled execution.

All 35 rules were reviewed: 18 transferable, 17 partly and 0 specific. These are editorial judgments, not empirical model evaluations.

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
