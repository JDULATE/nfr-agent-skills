# Batch 8 audit

## Basis and principal findings

This skeptical source review covers every skill assigned to this batch in nfr-list.json, including any approved pilot, and every reference file under those skills. The authoring guide, rubric, disambiguation map and allowlist provide the contract. Existing reviews were not read as evidence. This is an agent review, not an independent human or blinded evaluation. No skill, catalogue, index, validator or threshold was changed.

- **Anonymity's default gate covers only one of its own goals.** The skill explicitly supports identity recovery and cross-context linkage separately, but the proposed gate only counts named-identity links. A stable unnamed profile could fail the latter goal while passing that shorthand gate. The workflow notices this distinction; the proposed record is less complete.
- **Strong mechanism overlap remains in Rules of thumb.** Producer filtering, final-effect enforcement, positive controls, trusted authority and alternate-path checks are valuable but often fit sibling skills unchanged. In particular, Integrity's approval example and Access Control's scoped mutation branch share acceptance territory.
- **The two-branch access skill is honest but inherently harder to route.** It does not falsely merge accessibility with authorization. Its guide contains only two short practices per branch, and its candidate examples leave exact focus/semantics or race-safe authority binding unfilled.
- **Privacy is an inherited size exception with useful depth.** Its combined footprint is 455 lines against the 150-250 guideline; every reference is below 150 lines. The expanded pattern catalogue adds substantive lifecycle mechanisms. The approved pilot was not edited.
- **Security's broad promise is shown through one narrow export path.** The example is concrete and valid, but mainly demonstrates recipient authorization and detection/prevention rather than coordination across multiple asset properties.

## Structure and description measurements

Line counts include blank lines; body excludes frontmatter. Combined includes full SKILL.md and all its references. These are authoring counts, not system targets.

| Id / slug | Description characters | Body / full | Reference lines | Combined | Rules / done / failure modes |
| --- | ---: | --- | --- | ---: | --- |
| 001 accessibility-access-control | 620 | 140 / 145 | design-patterns.md: 37; worked-example.md: 38 | 220 | 7 / 8 / 6 |
| 010 anonymity | 481 | 123 / 128 | design-patterns.md: 35; worked-example.md: 36 | 199 | 6 / 7 / 6 |
| 026 confidentiality | 449 | 122 / 127 | design-patterns.md: 35; worked-example.md: 34 | 196 | 6 / 7 / 5 |
| 057 integrity | 478 | 124 / 129 | design-patterns.md: 35; worked-example.md: 34 | 198 | 6 / 7 / 5 |
| 075 privacy | 480 | 170 / 180 | analytics-example.md: 82; data-lifecycle-contract.md: 101; design-patterns.md: 92 | 455 | 8 / 8 / 6 |
| 089 security-control-and-security | 484 | 124 / 129 | design-patterns.md: 43; worked-example.md: 36 | 208 | 6 / 8 / 5 |

## Per-skill findings and full transfer test

Each source bullet is quoted in full, in its original order. Transferable means the entire bullet could serve the named sibling unchanged. Partly means the technique transfers but the acceptance framing needs alteration. Specific means that sibling has a different acceptance question. Shared safeguards can be necessary without satisfying the stricter requirement for distinctive Rules of thumb. Judgments use the repository conventions; they do not claim standardized meanings.

### 001 accessibility-access-control

**Description and boundary:** The combined label honestly separates six natural interaction/authorization triggers and explicitly asks which access branch applies. It cannot be a single coherent NFR boundary: bare access language remains ambiguous by design. Body definitions also distinguish usability, legibility, disclosure and threats.

**Repository actions and design depth:** Focus transitions, control/error semantics, actor/action/resource matrices and final-effect policy checks are actual repository work. Two branches share one Workflow and document budget; only two short design entries serve each branch. There is limited room for more complex component or permission-state transitions.

**Worked example:** The dialog sequence supplies empty subject, error correction, invoking control and return focus. The permission example supplies named editor, report/team scope and direct cross-team mutation. These have concrete inputs and carried state, but no actual accessibility representation or race-safe policy-binding mechanism is instantiated.

**Three weakest passages:**

- `SKILL.md`: "Handles two separate branches" - An honest catalogue compromise, but a router still needs a branch decision before executing most of the skill.
- `references/worked-example.md`: "Task-relevant focus and meaningful controls" - The expected output does not fill a target focus element or the exposed control/error representation.
- `references/design-patterns.md`: "change authority between view and effect" - Names the crucial transition but does not demonstrate how current authority is bound to the final effect without a second race.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do preserve an operable focus route through dialog opening, error correction, and return; reaching the initial control does not establish an accessible task path. | usability | Transferable | An intended keyboard task also fails usability when its dialog/error/return focus path is broken. |
| 2. Don't replace control meaning or error semantics with visual decoration; an audience using another interaction representation still needs the task decision. | self-descriptiveness | Transferable | Task-relevant control meaning and exposed error state directly serve in-context explanation in another interaction representation. |
| 3. Do observe the actual accessible task with its required input/assistive context; a preferred visual style or automated pass cannot establish barrier-free completion. | usability | Transferable | A style preference or automated scan cannot establish real task completion in the actual use context either. |
| 4. Don't treat a hidden or disabled interface action as permission enforcement; direct and background calls must still satisfy the confirmed actor/resource policy. | security-control-and-security | Transferable | A modeled adversary can bypass a hidden interface action through direct/background calls. |
| 5. Do bind authorization to the actual resource scope, not only the action name; a valid editor role in one team does not grant edits in another under a scoped policy. | integrity | Transferable | The same scoped editor policy protects a resource against unauthorized cross-team alteration. |
| 6. Do test changed authority at the effect boundary; an earlier allowed screen state cannot justify a later forbidden action under the confirmed revocation rule. | integrity | Transferable | Protected-state mutation after changed authority also needs the same effect-boundary validity check. |
| 7. Don't force authentication as a fix for an interaction barrier; choosing the wrong branch can add a barrier without repairing either intended acceptance question. | usability | Partly | Avoiding an added authentication barrier transfers, but choosing between this catalogue label branches is specific to its combined entry. |

Transfer counts: 6 transferable; 1 partly; 0 specific.

### 010 anonymity

**Description and boundary:** Observer, auxiliary knowledge and repeated releases distinguish Anonymity from generic data handling. Remove identity clues also fits Privacy minimization until the user states an unlinkability claim. The description correctly disclaims universal proof.

**Repository actions and design depth:** Trace mapping access and joined outputs, remove or coarsen fields, assess repeated releases and preserve utility. These are concrete review/transformation actions; there is no unsupported quantitative anonymity model.

**Worked example:** Unique role plus staff roster identifies a named subject; a stable token independently links comments. Candidate coarse totals break the particular row-level join and explicitly leave repeated-total inference open. This is a concrete worked counterexample with an honest limited improvement, not proof of anonymity.

**Three weakest passages:**

- `SKILL.md`: "Trial gate: 0 successful named-identity links" - The supported goal can instead be cross-context linkage without a name; this default gate does not explicitly test that branch.
- `references/worked-example.md`: "emits only the approved coarse total" - No concrete totals/release sequence exercises the remaining repeated-output inference question.
- `references/design-patterns.md`: "grouping, suppressing, or reducing detail" - Useful transformation families, but their utility/linkage selection procedure remains broad rather than a filled choice.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't equate a replacement identifier with unlinkability; an observer holding its mapping can still identify the subject even if the released name is absent. | privacy | Transferable | The broader personal-data handling skill also must not call a recipient-accessible identity map unlinkability. |
| 2. Do combine the observer's permitted auxiliary fields and releases during review; individually ordinary clues can jointly answer the exact identity question being claimed hidden. | confidentiality | Partly | Combined recipient knowledge matters, but learning identity through joint inference is not identical to a field disclosure permission. |
| 3. Do distinguish identity recovery from merely linking records to each other; a stable unnamed profile can violate a cross-context unlinkability goal without a recovered name. | privacy | Transferable | A privacy handling decision also needs to distinguish named identity recovery from cross-context subject linkage. |
| 4. Don't hide an identifying mapping from the reviewer while leaving it reachable by the claimed observer; the model must describe access, not the demo's chosen screen. | confidentiality | Partly | Testing actual recipient access rather than a demo transfers; the claim being disproved here is unlinkability. |
| 5. Do compare transformed outputs against the confirmed utility task; an empty release avoids links by abandoning the function, not by satisfying a useful anonymity contract. | privacy | Partly | Preserving useful output transfers, but an empty release specifically vacates the observer unlinkability/utility contract. |
| 6. Do retain inference and repeated-release gaps in the claim; a clean synthetic join test cannot establish unlinkability against unspecified future auxiliary knowledge. | privacy | Transferable | That sibling must also preserve the limits of any anonymity claim attached to personal-data handling. |

Transfer counts: 3 transferable; 3 partly; 0 specific.

### 026 confidentiality

**Description and boundary:** Disclosure to permitted recipients is clear. Private fields in responses can also be Privacy minimization; field permission versus purpose/lifecycle is the deciding fact. Action-authorization exclusion appears in the body rather than the description.

**Repository actions and design depth:** Recipient-specific views, policy-aware cache isolation, diagnostic filtering and delayed-delivery revalidation are positive implementation practices. Actual already-delivered content cannot be retroactively undisclosed, and the guide explicitly says so.

**Worked example:** Named recipient/report/team, a literal protected marker, title-only output, cache/error paths and policy transition make useful negative/positive cases. Cache keys, actual populated cached record and changed-policy timing remain unfilled; there is no worked invalidation/revalidation strategy.

**Three weakest passages:**

- `references/worked-example.md`: "Follow confirmed copy policy" - This table outcome leaves the hardest changed-policy/queued-view decision entirely unresolved.
- `references/design-patterns.md`: "policy-aware reuse can reduce cache sharing" - States the tradeoff but no concrete safe key or revalidation state is shown.
- `SKILL.md`: "Do separate a permitted field view from permission to collect or retain its data" - A necessary boundary guard that fits Privacy unchanged rather than distinct disclosure design advice.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Don't send a protected field and rely on display masking; the recipient may already learn it from the emitted payload before the page chooses to hide it. | privacy | Transferable | A personal-field minimization path also must filter before transmission rather than merely mask its display. |
| 2. Do apply the field/recipient boundary to error and diagnostic output too; fixing the success response does not close a disclosure through its failure path. | privacy | Transferable | The Privacy capture inventory already needs the same error/log recipient boundary. |
| 3. Do scope cached views by their actual permitted recipients and object context; a cache hit must not bypass the origin path's narrower disclosure decision. | accessibility-access-control | Transferable | The access-control branch also cannot let cross-scope cache reuse bypass the confirmed actor/resource policy. |
| 4. Don't require identity unlinkability to accept an approved identifiable view; a permitted recipient may learn a name while the separate anonymity claim remains false. | anonymity | Partly | Separating properties transfers, but that sibling actually evaluates unlinkability rather than accepting an identifiable authorized view. |
| 5. Do separate a permitted field view from permission to collect or retain its data; the disclosure gate can pass while purpose and lifecycle approval remain unresolved. | privacy | Transferable | Purpose and lifecycle approval remain separate from an authorized view in that sibling too. |
| 6. Do inspect delayed/export copies after policy changes; a narrowed live response cannot establish that an older queued or stored view respects the new boundary. | privacy | Transferable | Updated purpose/recipient decisions also need enforcement for queued and retained copies. |

Transfer counts: 5 transferable; 1 partly; 0 specific.

### 057 integrity

**Description and boundary:** Unauthorized/unintended alteration is explicit. Protected fields and stale edits overlap the Access Control and Consistency siblings; the body names Consistency, but the description does not distinguish either sibling. Accuracy/Confidentiality/Atomicity exclusions are useful.

**Repository actions and design depth:** Final-writer constraints, independent trust expectations and current-version checks are real practices. Much of the approval-field example is authorization, and the provenance branch lacks a filled independent anchor.

**Worked example:** Named report, old/current versions, protected approval field and a caller-supplied reference are concrete state. The table correctly rejects self-confirming provenance but does not supply an actual trusted expectation. Mismatch handling and permitted correction remain abstract policy outputs.

**Three weakest passages:**

- `references/worked-example.md`: "the actual trusted-origin source must be independently confirmed." - The central provenance mechanism is absent from the worked state, so it demonstrates why the current claim fails rather than how to repair it.
- `references/worked-example.md`: "Apply confirmed stale/conflict rule" - No filled state transition distinguishes reject, merge or approved rollback in the candidate.
- `SKILL.md`: "Do enforce protected-field and transition rules at the final writer" - The full rule moves unchanged to Access Control; noun substitution is not needed.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do distinguish an authorized correction from an unauthorized overwrite; preserving every old byte would defeat a transition policy that permits legitimate repair. | accessibility-access-control | Transferable | The authorization branch must preserve approved corrections while rejecting forbidden overwrite effects. |
| 2. Don't establish trust by comparing an artifact with a reference supplied through the same untrusted alteration path; both may agree while the protected origin is unestablished. | security-control-and-security | Transferable | An attacker-controlled reference cannot serve as trusted authority in the broader threat model either. |
| 3. Do enforce protected-field and transition rules at the final writer, including alternate import/admin paths; a restricted editor cannot constrain a bypassing mutation. | accessibility-access-control | Transferable | Final-writer enforcement and alternate mutation paths are the same action-authorization problem. |
| 4. Do bind stale-write decisions to the current approved version at mutation; a valid earlier edit must not silently replace a later state the policy protects. | consistency | Partly | Current-version conflict handling transfers, but protection from unintended alteration rather than representation agreement supplies this framing. |
| 5. Do inspect actual protected state after rejected changes; error responses do not establish alteration prevention if a side path already committed the forbidden value. | accessibility-access-control | Transferable | A denied mutation that changes the protected object also fails the access-control effect contract. |
| 6. Don't call unchanged or provenance-checked data accurate; closeness to the real-world reference is a separate acceptance question from alteration control. | accuracy | Partly | The property distinction matters to Accuracy too, but its primary acceptance question is closeness to a reference rather than preservation. |

Transfer counts: 4 transferable; 2 partly; 0 specific.

### 075 privacy

**Description and boundary:** Personal-data purpose, choices and lifecycle are explicit; the regulation/request labels are framed as supplied constraints. Disclosure-only and unlinkability-only exclusions are real. GDPR/CCPA/DSAR is grouped as labels, not a claim that DSAR is a regulation.

**Repository actions and design depth:** The most developed implementation reference in the batch: recipient allowlists, field tags, choice propagation, TTL/scheduling, delete semantics, suppression, retryable disposal and source redaction. These have real tradeoffs and checks. The complete document is substantially longer than later batch entries.

**Worked example:** Literal before/after analytics payloads, a named synthetic field inventory row and failure/retry/restore controls make concrete input/output state. A full per-destination disposal ledger, tombstone expiry versus backup horizon, and an unavailable-suppression trace are not filled. No legal deadline is asserted.

**Three weakest passages:**

- `SKILL.md`: "End/action/deadline: verified deletion request; active-store erasure within 7 days." - Properly illustrative, but it chooses a deletion-oriented fast path for handling changes that might only concern collection or choice.
- `references/data-lifecycle-contract.md`: "backups expire at the approved rotation event" - The filled row still leaves backup expiry symbolic; later prose correctly requires a concrete boundary before acceptance.
- `SKILL.md`: "never state obligations as fact." - A valid authoring/policy guard that transfers unchanged to Security; it is not a distinctive engineering practice for personal-data lifecycle.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do reject optional fields at the producer when their purpose is unconfirmed; do not collect them first on the assumption that retention can be decided later. | confidentiality | Partly | Early field filtering transfers, but recipient permission alone cannot decide whether collection purpose is approved. |
| 2. Do send even an authorized recipient only the personal fields needed for its approved purpose; permission to receive an account object does not justify forwarding unused contact fields in an analytics event. | confidentiality | Transferable | The complete purpose-limited recipient view also fits disclosure under the agreed field/recipient policy. |
| 3. Do stop optional collection at its source when the confirmed choice is withdrawn; hiding the choice control must not stand in for changing the collection path. | confidentiality | Partly | Changed-policy enforcement transfers, but stopping collection at its source is broader than restricting recipients. |
| 4. Do propagate retention and deletion decisions to indexes, caches, derived profiles, and exports; do not let a derived output escape the inventory by renaming it. | confidentiality | Partly | Inventories and copied outputs transfer, but lifecycle disposal reaches beyond disclosure-only acceptance. |
| 5. Do prevent restored or replayed data from repopulating deleted active records; retain only the suppression evidence approved for that purpose and its own expiry. | recoverability | Transferable | A recovered system with approved deletion obligations must also suppress erased records during restore/replay. |
| 6. Do give disposal evidence its own purpose, minimal personal fields, and expiry; don't recreate the erased profile in a purge log that is retained longer than the approved deletion-evidence purpose requires. | auditability | Transferable | Minimal purpose-bound disposal evidence also needs its own lifetime and cannot recreate the deleted profile. |
| 7. Don't equate encryption, masking, or a replacement identifier with permission to collect, indefinite retention, or demonstrated anonymity. | confidentiality | Transferable | That sibling must likewise avoid turning encryption or masking into unrelated collection, retention or anonymity approval. |
| 8. Do record user-named regulations or request labels as stakeholder-supplied constraints; ask what their policy or counsel requires of the system, and never state obligations as fact. | security-control-and-security | Transferable | Stakeholder-supplied policy labels must be attributed without inventing legal obligations in the security skill too. |

Transfer counts: 5 transferable; 3 partly; 0 specific.

### 089 security-control-and-security

**Description and boundary:** Explicit adversary, assets and misuse path distinguish broad coordination from a narrower disclosure/alteration property. Threat model an integration is a strong trigger; generic make this secure still lacks the intended scope.

**Repository actions and design depth:** Trace trust crossings, enforce boundary checks, distinguish detection/prevention, preserve valid use and investigate tool leads. These are genuine repository actions; the design reference remains mostly a control-placement review rather than a worked choice among distinct controls.

**Worked example:** Named report/team, approved and forbidden destinations, API and retry entrypoints give concrete source-to-effect state. The actual policy store and unavailable-policy decision remain unfilled. This single export-authorization example overlaps Confidentiality/Access Control more than it demonstrates coordination of multiple asset properties.

**Three weakest passages:**

- `references/worked-example.md`: "Confirmed team/destination check permits it" - The actual trusted policy source and how it is bound to the export effect are not supplied.
- `references/worked-example.md`: "Confirmed policy applied, not caller-supplied authority" - The control-failure branch is an open policy variable rather than a worked degraded behavior.
- `SKILL.md`: "Do preserve legitimate-use controls alongside misuse scenarios" - The complete rule transfers unchanged to Confidentiality or Integrity; useful safety against vacuous success does not make it NFR-specific.

| Rule | Nearest sibling | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Do trace each proposed control to an adversary-controlled step and protected effect; a list of security features does not establish that the misuse path is interrupted. | defensibility | Transferable | Active response also needs the causal path from adversary capability to protected effect rather than a control list. |
| 2. Don't promote caller-supplied identity, scope, destination, or policy labels into trusted authority without the confirmed boundary check; a plausible format is not that authority. | accessibility-access-control | Transferable | The authorization branch must not treat caller-supplied scope or identity as trusted authority. |
| 3. Do inspect alternate entrypoints and control-failure behavior for the same asset; an attacker path left outside the control can defeat the modeled prevention claim. | integrity | Transferable | An alternate attacker entrypoint can equally defeat an alteration-prevention claim. |
| 4. Don't report logging or alerting as prevention after the protected effect happened; separate evidence for detection from evidence that the adversary could not perform it. | defensibility | Transferable | An alert after an effect is not evidence the response prevented or interrupted that effect. |
| 5. Do preserve legitimate-use controls alongside misuse scenarios; disabling the protected capability can stop the attack by abandoning the accepted product requirement. | confidentiality | Transferable | Disabling useful approved disclosure also vacates the accepted positive-control requirement. |
| 6. Don't turn an empty scan report into a secure-system verdict; validate the modeled asset/path claims and retain unsupported attacker capabilities as explicit limits. | immunity | Transferable | A clean scan likewise cannot establish the sibling mechanism-backed exclusion claim. |

Transfer counts: 6 transferable; 0 partly; 0 specific.

## Routing probes

Manual semantic probes expose missing facts; these are not measured routing accuracy. A tentative lead does not erase a tie or authorize assumptions.

| Realistic prompt | Best fit / tie | First question and reason |
| --- | --- | --- |
| "fix access to this page" | 001 branch unresolved | Ask the user: an interaction barrier or actor/resource permission problem? The slash label intentionally combines separate meanings. |
| "make this more accessible" | 001 tentative; usability possible | Ask the user: which audience/task and input or assistive barrier prevents completion? |
| "users can edit other teams reports" | 001 / 057 unresolved | Ask the user: fix actor/resource authorization or enforce a broader protected-state transition invariant? The same mutation can need both. |
| "the API returns too much user data" | 026 / 075 unresolved | Ask the user: are fields forbidden to this recipient or unnecessary for an approved personal-data purpose? |
| "hide emails in analytics" | 075 / 026 unresolved | Ask the user: stop collecting/transmitting them for that purpose or restrict which recipients may learn them? Display masking would satisfy neither by itself. |
| "anonymize this export" | 010 tentative; 075 context needed | Ask the user: which observer, auxiliary knowledge and identity or cross-context linkage goal should be assessed? |
| "can we keep hashed user IDs" | 010 / 075 unresolved | Ask the user: are you judging linkage risk or approved purpose/retention? A transformation name supplies neither answer. |
| "our cached response contains another customers data" | 026 tentative; 001 also relevant | Ask the user: what recipient/object scope and reuse policy should govern the cached view? |
| "a valid old edit overwrites approval" | 057 tentative; consistency/001 plausible | Ask the user: which approved version/transition or authorization rule forbids the final effect? |
| "threat model the new integration" | 089 | Ask the user: which assets, attacker capabilities and authorized review scope define the misuse paths? |
| "revoke this compromised users sessions" | No exclusive batch-8 winner; defensibility tentative | Ask the user: an active response operation or a changed-authority implementation requirement, with what granted scope? |
| "implement GDPR deletion" | 075 | Ask the user: what system behavior does supplied policy or counsel require, including subject verification, copies, exceptions and deadlines? No legal obligation is inferred. |
| "the screen reader misses the error after submit" | 001 accessibility branch | Ask the user: which form/error state and supported input/assistive context should expose the error while preserving correction? |

## Cross-skill counts, evidence and limitations

Anonymity, Confidentiality and Integrity each have six rules and seven done items; Confidentiality and Integrity share 6/7/5 in full. Access has 7/8/6, Privacy 8/8/6 and Security 6/8/5. Anonymity/Confidentiality/Integrity guides are exactly 35 lines each. Different counts have content reasons: Access has independent branches, Privacy spans lifecycle mechanisms and Security separates tool findings from effects. The symmetry alone cannot establish deliberate padding.

Most done items map to distinct evidence: actor/resource scopes, received payloads, joins, trusted origin, lifecycle copies, or actual misuse effects. Access combines multiple scenarios in its changed-authority item; Privacy combines verification, isolation, failure and retry in one item. Checklist counts therefore do not measure the number of independent assertions.

The Privacy workflow and references explicitly include logs, errors, URLs/query strings, third-party SDKs/tags and replay/screenshots. It asks about sensitive/minor scope and treats legal labels as supplied constraints. No invented legal time limit or compliance conclusion was found. Anonymity also explicitly refuses universal or legal conclusions from a synthetic join test.

All descriptions have natural triggers and real catalogue sibling pointers. Boundary completeness is uneven rather than universally absent: Integrity's relation to action permission and the distinct purpose-versus-disclosure acceptance questions are not resolved by description exclusions alone. Bare access and privacy/security requests require clarification.

All 39 rules were reviewed: 29 transferable, 10 partly and 0 specific. These are editorial judgments, not empirical model evaluations.

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
