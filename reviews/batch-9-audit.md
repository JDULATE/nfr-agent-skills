# Batch 9 audit

## Basis and principal findings

This skeptical source review covers every skill assigned to this batch in nfr-list.json, including any approved pilot, and every reference file under those skills. The authoring guide, rubric, disambiguation map and allowlist provide the contract. Existing reviews were not read as evidence. This is an agent review, not an independent human or blinded evaluation. No skill, catalogue, index, validator or threshold was changed.

- **Negative honesty gates are not complete acceptance criteria.** Accountability's no-false-attribution gate allows unknown attribution; Auditability's no-unsupported-affirmative gate allows an unanswerable review; Susceptibility's no-unsupported-classification gate allows unresolved paths. These can be honest outputs, but the record must distinguish them from a fulfilled useful-evidence requirement. The full workflows already supply stronger positive checks, so this is shorthand completeness rather than evidence of automatic false approval.
- **Auditability's example is less filled than its neighbors.** It names policy/exception/gap artifacts but does not provide the actual rule, event values, retrieval query or reconstructed answer. It is a concrete examination protocol, not a completed worked examination.
- **Defensibility demonstrates residual capability more than successful containment.** Revoking new login while a queued job continues is a good negative case. The actual job intervention, clearance and timing trace remain unfilled. Its illustrative deadline begins at operator activation, leaving earlier signal-to-activation delay outside that bound.
- **Immunity and Susceptibility are local conventions with a useful claim-strength boundary.** Exclusion needs a supported enabling-path argument; current reachability classification does not. Their inputs/mechanisms overlap broad Security heavily and vague vulnerability/immune language needs a clarifying question.
- **Trustability is primarily decision presentation and authority alignment.** That scope is honest; neither polished artifacts nor an agent-only walkthrough demonstrates informed stakeholder reliance. Its example lacks an exact corrected decision view.

## Structure and description measurements

Line counts include blank lines; body excludes frontmatter. Combined includes full SKILL.md and all its references. These are authoring counts, not system targets.

| Id / slug | Description characters | Body / full | Reference lines | Combined | Rules / done / failure modes |
| --- | ---: | --- | --- | ---: | --- |
| 002 accountability | 467 | 118 / 123 | design-patterns.md: 35; worked-example.md: 33 | 191 | 5 / 7 / 5 |
| 013 auditability | 477 | 119 / 124 | design-patterns.md: 35; worked-example.md: 32 | 191 | 6 / 7 / 4 |
| 035 defensibility | 540 | 121 / 126 | design-patterns.md: 35; worked-example.md: 34 | 195 | 6 / 7 / 5 |
| 054 immunity | 535 | 119 / 124 | design-patterns.md: 36; worked-example.md: 34 | 194 | 5 / 6 / 6 |
| 098 susceptibility | 491 | 121 / 126 | design-patterns.md: 35; worked-example.md: 32 | 193 | 6 / 7 / 5 |
| 102 traceability | 454 | 121 / 126 | design-patterns.md: 35; worked-example.md: 33 | 194 | 6 / 7 / 5 |
| 105 trustability | 517 | 122 / 127 | design-patterns.md: 35; worked-example.md: 33 | 195 | 6 / 7 / 5 |

## Per-skill findings and full transfer test

Each source bullet is quoted in full, in its original order. Transferable means the entire bullet could serve the named sibling unchanged. Partly means the technique transfers but the acceptance framing needs alteration. Specific means that sibling has a different acceptance question. Shared safeguards can be necessary without satisfying the stricter requirement for distinctive Rules of thumb. Judgments use the repository conventions; they do not claim standardized meanings.

### 002 accountability

**Description and boundary:** Initiator/executor/delegation and the supported identity model distinguish runtime attribution from artifact lineage. Show who approved also fits Auditability until the missing issue is identity binding rather than examiner sufficiency.

**Repository actions and design depth:** Bind validated origin, propagate non-secret delegation references across jobs, correlate actual effect and preserve unknown/shared principals. These are concrete event-schema and lifecycle changes. The guide does not fill the trusted propagation format or its replay/expiry checks.

**Worked example:** Named principal/service/grant, forged actor label, job attempt, retry and unknown origin supply concrete attribution state. Invalid delegation is correctly separate from changing who initiated the attempt. Actual assertion contents, authority lifetime and persisted result record are not filled.

**Three weakest passages:**

- `SKILL.md`: "0 falsely attributed actions" - A negative gate can hold when every actor is unknown; coverage for the cases the source can resolve needs the positive binding checks elsewhere in the workflow.
- `references/design-patterns.md`: "trace initiating principal, delegated authority, executor and operation identity across each handoff" - Lists the required fields without a filled propagation record or stale/replayed delegation transition.
- `references/worked-example.md`: "If grant-mint was invalid" - The invalid-grant branch remains conditional rather than showing an explicit recorded denial/effect and separate origin.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do retain initiating principal and executor separately across delegation; a service account completing the work does not identify who requested it. | auditability | Transferable | An examiner reconstructing a delegated approval also needs both initiator and executor rather than only a service account. |
| 2. Don't turn a caller-supplied actor string into trusted attribution; bind the recorded principal to the actual validated identity context at the action boundary. | security-control-and-security | Transferable | A caller actor string must not become trusted identity in the broader threat/control model either. |
| 3. Do preserve unknown or shared identity honestly; choosing a likely human can produce a more readable record while falsely assigning responsibility. | auditability | Transferable | An independent review must preserve unsupported/shared identity instead of falsely naming a person. |
| 4. Do separate attempted, authorized, and completed actions; an identity on the request does not establish that the actor caused the final business effect. | auditability | Transferable | An examiner also must distinguish request, authorization and observed final effect to answer who acted. |
| 5. Don't retain bearer credentials merely to identify the actor later; use the approved non-secret identity/evidence reference and its access/lifetime policy. | privacy | Transferable | Minimum approved identity evidence and exclusion of live bearer secrets fit personal-data evidence handling unchanged. |

Transfer counts: 5 transferable; 0 partly; 0 specific.

### 013 auditability

**Description and boundary:** Independent permitted examination for a named question is clear. Prove what evidence supports a control can still fit Traceability/Trustability until sufficiency, navigation or delegation is specified.

**Repository actions and design depth:** Question-to-evidence matrix, approved retrieval view, schema context, gap markers and reproducible review package are concrete docs/query/event-schema outputs. This is not merely adding logs. Independent role simulation is not an actual independent human examination.

**Worked example:** Approval event, policy revision, exception and gap are concrete artifact types, but no literal event fields, policy rule, query or fully reconstructed answer is supplied. The table chiefly describes how evidence limitations affect the answer; it is closer to a protocol than a filled examination.

**Three weakest passages:**

- `SKILL.md`: "0 unsupported affirmative conclusions" - An always-unanswerable view also meets this negative gate; the useful answer elements and supported gaps need separate acceptance decisions.
- `references/worked-example.md`: "a linked exception" - Neither its value nor the rule it changes is filled, so the actual approval decision cannot be reconstructed from the example.
- `references/design-patterns.md`: "retain scope, query/view, provenance and result limits" - The reproducible package is a field list without a filled query/view and answer showing independent interpretation.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do start with the review question, not log volume; many unrelated events cannot establish the specific control or exception the examiner must evaluate. | trustability | Partly | Question-relevant evidence transfers; a permitted independent examiner rather than a stakeholder delegation decision frames the current rule. |
| 2. Don't treat missing evidence as evidence of no action; retention expiry and collection gaps can make the same empty query mean something entirely different. | accountability | Transferable | Missing runtime records likewise cannot establish that no attributable action occurred. |
| 3. Do preserve provenance and decision context with the approved evidence view; a detached event export can be readable yet impossible to evaluate independently. | trustability | Partly | Evidence context/provenance transfers; independent interpretation is Auditability-specific framing. |
| 4. Do test examination under the reviewer's actual access and redaction constraints; an author's privileged query is not proof that the intended examiner can answer. | confidentiality | Partly | Actual recipient access matters, but answering an examination question is not the disclosure-authorization acceptance question. |
| 5. Don't call a connected artifact chain an audit conclusion; the reviewer must still assess whether those records support the particular question. | traceability | Transferable | A trace map also must not promote a navigable artifact chain to an audit conclusion. |
| 6. Do keep contradictory and exception evidence retrievable beside favorable cases; a curated success-only export cannot support an independent control examination. | dependability | Transferable | An operational assurance case also cannot suppress counterexamples in a curated success-only package. |

Transfer counts: 3 transferable; 3 partly; 0 specific.

### 035 defensibility

**Description and boundary:** Active adversarial capability, authorized operator and containment distinguish design-time Security and passive Observability. Generic stop compromised access still overlaps the Access Control revocation branch until active response intent is stated.

**Repository actions and design depth:** Map independent capabilities, implement scoped operator controls, preserve evidence/valid work and test reversal. The guide is strong on scope and effect checks, thinner on selecting a concrete cancellation/session mechanism or its race handling.

**Worked example:** Named credential/session/job/report and separately granted queued-work control give meaningful carried capability state. A continuing job correctly defeats full containment after revoke. No timestamps, actual canceled/running job state or filled clearance decision demonstrate a successful complete intervention.

**Three weakest passages:**

- `SKILL.md`: "within 2 minutes of confirmed operator activation." - Properly illustrative, but it bounds activation-to-effect only; the broader detect/respond promise has no filled signal-to-activation criterion.
- `references/worked-example.md`: "Granted queued-work intervention" - The decisive intervention is a placeholder; no concrete state transition shows stopping already-running versus pending effects.
- `references/design-patterns.md`: "exercise confirmed clearance criteria" - The guide names reversal testing without a filled clearance record or reopened-capability negative case.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't equate an alert with containment; inspect whether the adversary can still produce the protected effect after the response control reports completion. | security-control-and-security | Transferable | A broad control review also cannot count an alert as containment while the adversary still produces the effect. |
| 2. Do distinguish credential revocation, session interruption and queued-work cancellation; removing one capability does not establish that the others stopped. | accessibility-access-control | Transferable | The revocation branch must likewise distinguish new login, active session and previously accepted work under its policy. |
| 3. Do scope the response to the confirmed adversarial path and granted authority; stopping unrelated essential work can exceed the permitted containment contract. | security-control-and-security | Transferable | A control that disables unrelated required use can also violate the declared security/product scope. |
| 4. Do retain the activity and response evidence needed to evaluate the intervention; destroying it during cleanup can prevent checking what capability actually persisted. | auditability | Partly | Retaining intervention records supports examination, but evaluating continued adversarial capability is a response question. |
| 5. Don't release containment because a health probe is green; restored service does not show that the adversarial identity, session or alternate path is gone. | security-control-and-security | Transferable | Health restoration also cannot establish the adversary path is removed in the broader threat/control case. |
| 6. Do verify reversal against its clearance conditions; reopening the capability before those conditions hold can undo the very containment being accepted. | security-control-and-security | Transferable | Reversing a restriction before its clearance condition holds reopens the protected misuse path there too. |

Transfer counts: 5 transferable; 1 partly; 0 specific.

### 054 immunity

**Description and boundary:** Explicit mechanism-backed class exclusion and assumptions distinguish finite robustness trials. Can this input ever reach an interpreter also fits Susceptibility until the requested claim is exclusion rather than current reachability.

**Repository actions and design depth:** Remove an enabling path, inspect alternate/dependency closure, enforce premises and reopen claims after changes. This is a useful narrow structural review. It correctly avoids calling a source sketch a formal proof.

**Worked example:** Fixed operation mapping, payload-as-data, alternate loader and config toggle provide a clear class-enabling counterexample. No literal map, payload path or inspected dependency supplies the positive structural closure, so the candidate remains a conditional argument outline.

**Three weakest passages:**

- `SKILL.md`: "0 unresolved counterexamples to the scoped exclusion argument." - No known counterexample alone is insufficient without a supported mechanism and closure; the full workflow correctly requires the positive argument too.
- `references/worked-example.md`: "no reachable handler or loader interprets that caller text as commands." - This is the central premise, not demonstrated closure in the example.
- `references/design-patterns.md`: "whether the claim is reopened when it does not." - The invalidation practice does not specify a concrete claim-to-config/dependency artifact that would detect the change.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't call rejected examples class exclusion; a handler that accepts the same dangerous interpretation elsewhere defeats the structural claim despite those passes. | security-control-and-security | Partly | Bypass paths defeat security prevention too; exclusion of the entire class requires the stronger structural claim. |
| 2. Do name the mechanism that removes the enabling path; retry, timeout or cleanup after exposure may bound damage without excluding the class from occurring. | robustness | Partly | The distinction prevents confusing bounded response with exclusion, but the sibling explicitly accepts controlled exposure. |
| 3. Do include alternate loaders and entrypoints in the reachability argument; removing the normal path is insufficient if another supported path still enables it. | security-control-and-security | Transferable | A broader prevention review also must inspect alternate handlers/loaders that enable the same adversarial effect. |
| 4. Don't silently move a configuration assumption into an unconditional claim; changing that condition must reopen the stated exclusion argument. | susceptibility | Transferable | The exposure classification likewise must reopen when its configuration premise changes. |
| 5. Do distinguish a conditional exclusion argument from absence of observed failures; more clean examples cannot repair an unexamined enabling path. | provability | Partly | Clean examples versus a conditional argument transfers; an actually formal proof needs more than the current source-backed exclusion case. |

Transfer counts: 2 transferable; 3 partly; 0 specific.

### 098 susceptibility

**Description and boundary:** Exposure/preconditions and explicit reachable/blocked/unknown states are clear. It overlaps Security threat-path mapping almost completely at the mechanism level; requested output scope is what makes the narrower skill useful.

**Repository actions and design depth:** Read source/config/grants, build a precondition ledger, toggle scoped fixtures and recheck alternate paths after an authorized reduction. These are concrete analysis tasks. An actual reduction is optional and only weakly demonstrated.

**Worked example:** Disabled public route, unknown scheduler grant and granted administrative fixture produce distinct honest classifications. The transformation, influence predicate and exact config/grant values are symbolic. No concrete reduced-exposure change and positive-use outcome is worked through.

**Three weakest passages:**

- `SKILL.md`: "0 unsupported exposure classifications" - Useful negative honesty gate, but no minimum resolved path or decisive evidence is required by that shorthand.
- `references/worked-example.md`: "the deployed scheduler permission is unavailable to inspect." - Correctly unknown, but the worked example stops before showing the fact that would resolve that important path.
- `references/worked-example.md`: "disable or constrain the confirmed enabling path" - Names an intervention family without filling a changed precondition and the rechecked alternate/valid-use effects.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do keep unknown separate from blocked; missing configuration evidence cannot establish that the adverse influence lacks a route to the affected operation. | immunity | Transferable | Missing configuration evidence also cannot establish that a class-enabling route is excluded. |
| 2. Don't infer exposure solely from a dependency name; the relevant capability, configuration and reachable invocation must fit the specified influence. | security-control-and-security | Transferable | Threat findings also need capability, configuration and reachable invocation, not only a dependency name. |
| 3. Do distinguish reachable operation from demonstrated adverse effect; locating an input path does not establish that exploitation actually succeeded. | security-control-and-security | Transferable | The broader threat review also must separate reached code from a demonstrated successful adverse effect. |
| 4. Do preserve each blocking precondition and its evidence; changing that condition can reopen exposure even when no application source changed. | immunity | Transferable | Mechanism exclusion also depends on retained premises and must reopen when a blocker changes. |
| 5. Don't promote a blocked current path to permanent class exclusion; alternate entrypoints and future configuration changes remain separate evidence obligations. | immunity | Transferable | A scoped current blocker likewise cannot establish permanent class exclusion across alternate routes or configurations. |
| 6. Do trace internal and background paths for the declared influence as well as public routes; absence from the visible interface does not establish non-exposure. | security-control-and-security | Transferable | The wider control review also must inspect internal/background adversary routes rather than only a visible UI. |

Transfer counts: 6 transferable; 0 partly; 0 specific.

### 102 traceability

**Description and boundary:** Typed, revisioned, forward/reverse relationships distinguish actor identity and examination verdicts. Find what this change affects also fits Analyzability; the description does not state a boundary against that sibling.

**Repository actions and design depth:** Create stable IDs/typed revisioned edges, retain superseded evidence and walk changes back to requirements. Concrete docs/metadata/link-checking work is appropriate. The design reference does not specify a filled edge record or maintenance/invalidation mechanism.

**Worked example:** Named requirement/decision/function/result with old editor versus new reviewer rule makes semantic staleness concrete. It distinguishes historical result from a new unexecuted test and demonstrates reverse orphan detection. Exact revision IDs and literal typed edge records remain unfilled.

**Three weakest passages:**

- `SKILL.md`: "0 unexplained orphan links" - A resolving but semantically wrong edge can pass this shorthand even though later verification rightly rejects it.
- `references/worked-example.md`: "after content review" - The implementation edge is labeled valid without showing the actual changed predicate or basis of that semantic review.
- `references/design-patterns.md`: "explicit relationship types need review" - The guide states the need but supplies no literal edge schema or concrete trigger maintaining it across revisions.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do type the relationship instead of using related as a verification claim; a rationale edge and a passing-evidence edge support different trace questions. | auditability | Partly | Relationship meaning helps examination; navigation semantics alone cannot decide evidentiary sufficiency. |
| 2. Do bind evidence to the requirement meaning and artifact revision it assessed; a valid historical result must not silently verify a changed obligation. | auditability | Transferable | A reviewer also cannot use historical evidence to affirm a changed current obligation without scope/revision checks. |
| 3. Don't equate a resolving path with a correct trace; the linked function or test can exist while addressing a different requirement than the edge asserts. | auditability | Transferable | An existing but irrelevant linked record also fails that sibling question-to-evidence mapping. |
| 4. Do walk from changed code back to affected requirements as well as forward; a forward-only index can hide obligations whose implementation was removed. | analyzability | Transferable | Reverse code-to-obligation navigation also directly supports source-backed change-impact analysis. |
| 5. Do retain superseded lineage separately from current coverage; deleting old relationships can erase why a decision changed without repairing the new evidence gap. | auditability | Transferable | Independent examination of a changed decision also needs retained historical rationale separate from current evidence. |
| 6. Don't mark an obligation satisfied because its test file is linked; the edge needs relevant result status and does not itself establish behavioral success. | verifiability | Transferable | A relevant test pathname is likewise not an observed behavioral result for acceptance evidence. |

Transfer counts: 5 transferable; 1 partly; 0 specific.

### 105 trustability

**Description and boundary:** Stakeholder decision, material limits and actual authority distinguish persuasion from justified delegation. Reliance/claims/evidence overlaps Dependability heavily; the stated decision context rather than mechanism must select the route.

**Repository actions and design depth:** Narrow product/docs claims, place material limits at delegation, retain real permission checks and walk unsupported cases/fallback. These are concrete message/UI/config/test outputs. Artifact review cannot establish informed stakeholder reliance; the skill explicitly admits that limit.

**Worked example:** Draft-only evidence and permission versus automatic-publication wording give concrete claim/authority mismatch and a valid fallback. The new exact user-visible message, filled evidence revision and actual stakeholder decision are not shown. It demonstrates overclaim rejection more than calibrated decision quality.

**Three weakest passages:**

- `SKILL.md`: "0 hidden material limitations" - Materiality remains owner-defined; this gate does not itself require usable evidence or demonstrate informed decision quality.
- `references/worked-example.md`: "Replace the broad promise with scoped draft evidence and visible publication unknowns." - No literal corrected message or filled decision view demonstrates the proposed presentation.
- `references/design-patterns.md`: "separate artifact inspection from observed stakeholder decision quality." - An honest limitation, but no concrete stakeholder task/decision probe shows how the latter would be checked.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't improve trust by hiding a counterexample; a more favorable response to incomplete evidence can worsen the basis for the actual reliance decision. | dependability | Transferable | Hiding a defeating counterexample also undermines an operational reliance case. |
| 2. Do scope capability claims to the context and revision their evidence supports; an unqualified badge can imply permission to rely on untested uses. | dependability | Transferable | Operational assurance also must scope claims to the actual evidence revision and use context. |
| 3. Do place material limits where delegation is decided; a discoverable appendix alone may leave the relevant decision using an unsupported promise. | self-descriptiveness | Partly | In-context explanation transfers; decision-changing evidence limits rather than current interface state supply the trust-support framing. |
| 4. Don't treat an evidence display as granted authority; an informed stakeholder decision and the system's actual permission boundary remain distinct conditions. | accessibility-access-control | Transferable | An authorization branch also must not treat an informative evidence display as a grant of action permission. |
| 5. Do keep unknowns different from favorable evidence; confident wording cannot convert an untested capability into a supported delegation premise. | dependability | Transferable | Unknown capability support cannot become a favorable operational reliance premise through confident wording either. |
| 6. Don't use preference or trust ratings as a substitute for evidence calibration; a reassuring presentation can be liked while overstating what may be relied on. | likeability | Partly | Preference ratings belong there, but the current rule rejects them as evidence for justified delegation rather than measuring sentiment. |

Transfer counts: 4 transferable; 2 partly; 0 specific.

## Routing probes

Manual semantic probes expose missing facts; these are not measured routing accuracy. A tentative lead does not erase a tie or authorize assumptions.

| Realistic prompt | Best fit / tie | First question and reason |
| --- | --- | --- |
| "who approved this" | 002 / 013 unresolved | Ask the user: missing actor attribution or inability to reconstruct approval evidence under the reviewer view? |
| "we need an audit trail" | 013 tentative; 002/102 possible | Ask the user: which reviewer question, actor responsibility or artifact lineage must the trail answer? |
| "show why this requirement passed" | 013 / 102 unresolved | Ask the user: navigate typed evidence relationships or evaluate whether retained results justify the claim? |
| "find what changed this decision" | 102 tentative; 002 possible | Ask the user: artifact/version rationale or the runtime principal who performed the action? |
| "can we trust this feature" | 105 tentative; dependability possible | Ask the user: which stakeholder reliance/delegation decision and consequence, or a combined operational failure case? |
| "stop a compromised account doing damage" | 035 tentative; access-control also fits | Ask the user: design/rehearse an active response or implement a standing authorization rule, with which granted controls? |
| "make us immune to malicious inputs" | 054 tentative; robustness/security plausible | Ask the user: which exact class and mechanism-backed exclusion, or bounded response during exposure? Universal immunity is undefined. |
| "are we vulnerable to this dependency issue" | 098 tentative; security also relevant | Ask the user: which adverse influence, deployed invocation, capability and configuration determine exposure? The dependency name alone is insufficient. |
| "the public endpoint is off so are we safe" | 098 / 054 unresolved | Ask the user: classify current exposure or support class exclusion across all declared alternate routes and premises? |
| "prove the logs show no exceptions" | 013 | Ask the user: which review scope, collection coverage, retention and exception evidence make an empty query interpretable? |
| "the bot publishes because its confidence badge is green" | 105 tentative; access-control also relevant | Ask the user: what evidence supports unattended publication and who actually granted that authority? |
| "record the user behind background jobs" | 002 | Ask the user: which trusted initiator/executor/delegation model can the source honestly support? |
| "what tests does this code change invalidate" | 102 / analyzability unresolved | Ask the user: revisioned requirement/evidence lineage or a broader causal change-impact investigation? |

## Cross-skill counts, evidence and limitations

Defensibility, Susceptibility, Traceability and Trustability share the complete 6/7/5 count triple. Accountability has 5/7/5, Auditability 6/7/4 and Immunity 5/6/6. Every guide has four use-when/trade-off/verify practices; six are exactly 35 lines and Immunity is 36. This strong shared shape is visible evidence of templating, but cannot establish whether a particular count was content-driven.

Done lists mostly name distinct evidence: identity binding, independent retrieval, containment effect, structural exclusion, exposure premises, semantic edges or delegation authority. Repeated scope/unknown/actual-effect checks transfer broadly. Seven items is not seven independent experiments; several are documentation and interpretation checks.

Immunity explicitly separates source reasoning from formal proof, and Susceptibility separates reached operation from actual adverse effect. Accountability explicitly refuses proof of a human behind shared credentials. These limitations are substantive safeguards. No unsupported vulnerability identifier, legal duty, security guarantee or proof was found.

Descriptions have natural triggers and valid catalogue pointers, but several overlap at the actual vague prompt: who approved, why a claim passed, can we trust, and what changed all need the missing acceptance question. Additional sibling lists alone would not resolve that absent information.

All 40 rules were reviewed: 30 transferable, 10 partly and 0 specific. These are editorial judgments, not empirical model evaluations.

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
