# Batch 9 findings

## Description-first routing and scope

Seven descriptions were written before bodies. The shared authoring contract,
rubric, allowlist, disambiguation map, and three approved pilot entrypoints were
read. Earlier skills and pilots remain unchanged. Approval of batch 8 does not
promote draft statuses to reviewed or authorize work on batch 10.

Immunity, Susceptibility, and Trustability retain the map's proposed local meanings;
none is presented as a standardized definition. This manual semantic comparison
is not an independent agent or Phase-5 keyword evaluation.

| Request | Best fit / ambiguity | Acceptance boundary and first missing fact |
| --- | --- | --- |
| Who approved this change? | accountability | Which trusted identity, delegated actor, action and outcome should the record attribute? |
| Give us an audit trail | accountability / auditability / traceability unresolved | Actor attribution, independent examination, or linked artifact history? |
| Can an independent reviewer reconstruct this approval? | auditability | What review question, scope, evidence and permitted access define an answer? |
| Trace this requirement through code and tests | traceability | Which revisions, typed relationships and reverse impact questions? |
| Logs say the service acted but not which user initiated it | accountability | What delegation/identity model can actually support attribution? |
| Stop a compromised credential continuing the action | defensibility | Which observed adversarial activity, response authority and effects are in scope? |
| Threat model the integration | security-control-and-security outside batch | Design-time adversary/asset/control coordination, not active response alone. |
| Restore after the outage | recoverability outside batch | Restored service/state, not evidence an adversary can no longer act. |
| Can this input ever reach the command interpreter? | immunity / susceptibility unresolved | A structural exclusion claim, or locating a possible path and its prerequisites? |
| Which conditions expose us to this attack? | susceptibility | Which adverse influence, entrypoints, capabilities, configurations and unknowns? |
| Make it immune to attacks | No justified universal claim; immunity scope unresolved | Which exact class, mechanism, assumptions and protected boundary? |
| Handle malicious input without crashing | robustness outside batch; Security may contribute | Controlled response is not proof the attack/fault class is excluded. |
| Show limitations before I delegate publication | trustability | Who decides, for which delegation, and which claims/limits would change that decision? |
| Can we rely on this service through failures? | dependability outside batch | Operational failure assurance rather than a broader stakeholder trust presentation. |
| Show confidence in this prediction | certainty outside batch | Warranted confidence and uncertainty, not a whole delegation/trust decision. |
| People should trust us more | trustability unresolved | Which actual decision needs better evidence, rather than more reassuring messaging? |

Broad audit, immune, and trust language remains a clarification case. Descriptions
name nearest exclusions and do not equate many logs, failed tests, or positive
sentiment with the respective property.

## Full rule transfer findings

Every Rules of thumb bullet is quoted and compared with the nearest plausible
sibling from the map. Transferable means the whole instruction can move unchanged;
partly means shared mechanism with a materially different acceptance scope;
specific means the nearest tested sibling can accept a different outcome. These
manual judgments do not establish empirical routing or formal exclusivity.

### 002-accountability

**Bullet 1: transferable; nearest sibling `auditability`.**

> Do retain initiating principal and executor separately across delegation; a service account completing the work does not identify who requested it.

An independent examiner reconstructing a delegated action also needs origin and executor separately, so this whole attribution rule transfers unchanged.

**Bullet 2: transferable; nearest sibling `security-control-and-security`.**

> Don't turn a caller-supplied actor string into trusted attribution; bind the recorded principal to the actual validated identity context at the action boundary.

A caller-controlled identity label is also an untrusted authority input in a threat model; the complete trusted-binding instruction transfers.

**Bullet 3: transferable; nearest sibling `auditability`.**

> Do preserve unknown or shared identity honestly; choosing a likely human can produce a more readable record while falsely assigning responsibility.

An independent examination must likewise preserve unknown/shared attribution instead of inventing a person, so the complete evidence-honesty rule transfers.

**Bullet 4: transferable; nearest sibling `auditability`.**

> Do separate attempted, authorized, and completed actions; an identity on the request does not establish that the actor caused the final business effect.

An examiner also must not infer final effects from request identity alone, so this whole attempt/decision/outcome distinction applies unchanged.

**Bullet 5: transferable; nearest sibling `privacy`.**

> Don't retain bearer credentials merely to identify the actor later; use the approved non-secret identity/evidence reference and its access/lifetime policy.

An approved minimal identity reference instead of retained live credentials also fits purpose-limited evidence handling unchanged.

Count: 5 transferable, 0 partly, 0 specific.

### 013-auditability

**Bullet 1: partly; nearest sibling `traceability`.**

> Do start with the review question, not log volume; many unrelated events cannot establish the specific control or exception the examiner must evaluate.

A typed artifact walk also begins with a question, but whether records support an examiner control/exception judgment goes beyond navigable lifecycle relationships.

**Bullet 2: transferable; nearest sibling `accountability`.**

> Don't treat missing evidence as evidence of no action; retention expiry and collection gaps can make the same empty query mean something entirely different.

Missing attribution evidence also cannot prove no actor action occurred; the same expiry/collection-gap distinction applies unchanged.

**Bullet 3: transferable; nearest sibling `traceability`.**

> Do preserve provenance and decision context with the approved evidence view; a detached event export can be readable yet impossible to evaluate independently.

Provenance and decision context also make connected lifecycle evidence interpretable, so the whole instruction can move unchanged.

**Bullet 4: partly; nearest sibling `confidentiality`.**

> Do test examination under the reviewer's actual access and redaction constraints; an author's privileged query is not proof that the intended examiner can answer.

Approved access/redaction constraints matter to disclosure too, but the acceptance question here is whether an independent reviewer can answer within that permitted view.

**Bullet 5: specific; nearest sibling `traceability`.**

> Don't call a connected artifact chain an audit conclusion; the reviewer must still assess whether those records support the particular question.

A connected artifact chain can satisfy a typed navigation question while leaving an examiner conclusion unsupported; this rule explicitly rejects substituting the former for the latter.

**Bullet 6: transferable; nearest sibling `trustability`.**

> Do keep contradictory and exception evidence retrievable beside favorable cases; a curated success-only export cannot support an independent control examination.

A trust decision also needs contrary evidence alongside favorable claims; a curated success-only package can mislead it unchanged.

Count: 3 transferable, 2 partly, 1 specific.

### 035-defensibility

**Bullet 1: specific; nearest sibling `observability`.**

> Don't equate an alert with containment; inspect whether the adversary can still produce the protected effect after the response control reports completion.

Passive state inference can legitimately stop at an observed signal; this rule demands capability interruption and rejects detection alone as containment.

**Bullet 2: transferable; nearest sibling `security-control-and-security`.**

> Do distinguish credential revocation, session interruption and queued-work cancellation; removing one capability does not establish that the others stopped.

Design-time control coordination also needs distinct credential/session/job capabilities rather than assuming revocation covers them all; the whole rule transfers.

**Bullet 3: partly; nearest sibling `safety`.**

> Do scope the response to the confirmed adversarial path and granted authority; stopping unrelated essential work can exceed the permitted containment contract.

Collateral essential-work effects can be a harmful outcome too, but the whole rule bounds an active intervention by granted response authority.

**Bullet 4: transferable; nearest sibling `auditability`.**

> Do retain the activity and response evidence needed to evaluate the intervention; destroying it during cleanup can prevent checking what capability actually persisted.

Preserving intervention evidence also supports independent examination of what persisted, so the complete evidence-preservation instruction transfers.

**Bullet 5: specific; nearest sibling `recoverability`.**

> Don't release containment because a health probe is green; restored service does not show that the adversarial identity, session or alternate path is gone.

Recoverability can accept restored healthy service after a gap; this rule rejects health as clearance of adversarial capability and therefore accepts a different endpoint.

**Bullet 6: transferable; nearest sibling `security-control-and-security`.**

> Do verify reversal against its clearance conditions; reopening the capability before those conditions hold can undo the very containment being accepted.

A design review of containment controls also needs conditional reversal to avoid restoring a modeled adversarial path; this full rule applies unchanged.

Count: 3 transferable, 1 partly, 2 specific.

### 054-immunity

**Bullet 1: specific; nearest sibling `robustness`.**

> Don't call rejected examples class exclusion; a handler that accepts the same dangerous interpretation elsewhere defeats the structural claim despite those passes.

Robustness can accept declared rejection of tested adverse inputs; this rule instead requires exclusion of the enabling class across the stated structural boundary.

**Bullet 2: specific; nearest sibling `robustness`.**

> Do name the mechanism that removes the enabling path; retry, timeout or cleanup after exposure may bound damage without excluding the class from occurring.

Timeout or cleanup can satisfy a controlled-response contract after exposure, while this exclusion claim rejects that as evidence the class cannot occur.

**Bullet 3: transferable; nearest sibling `susceptibility`.**

> Do include alternate loaders and entrypoints in the reachability argument; removing the normal path is insufficient if another supported path still enables it.

Alternative loaders and invocation paths also determine exposure, so this complete reachability obligation transfers unchanged.

**Bullet 4: transferable; nearest sibling `susceptibility`.**

> Don't silently move a configuration assumption into an unconditional claim; changing that condition must reopen the stated exclusion argument.

A changed configuration can reopen a blocked exposure path too, making the conditional-claim instruction reusable unchanged.

**Bullet 5: transferable; nearest sibling `provability`.**

> Do distinguish a conditional exclusion argument from absence of observed failures; more clean examples cannot repair an unexamined enabling path.

A formal argument also cannot repair an unexamined enabling case with more passing examples; the whole argument-versus-observation warning transfers.

Count: 3 transferable, 0 partly, 2 specific.

### 098-susceptibility

**Bullet 1: transferable; nearest sibling `immunity`.**

> Do keep unknown separate from blocked; missing configuration evidence cannot establish that the adverse influence lacks a route to the affected operation.

An unknown assumption cannot support a class-exclusion claim either, so keeping unknown different from blocked is shared evidence discipline.

**Bullet 2: transferable; nearest sibling `security-control-and-security`.**

> Don't infer exposure solely from a dependency name; the relevant capability, configuration and reachable invocation must fit the specified influence.

Threat/control work also needs capability, configuration and actual invocation rather than a dependency name alone; the full path-relevance rule transfers.

**Bullet 3: transferable; nearest sibling `security-control-and-security`.**

> Do distinguish reachable operation from demonstrated adverse effect; locating an input path does not establish that exploitation actually succeeded.

A security finding likewise must separate reachable input from demonstrated effect; this complete exploitability-evidence distinction applies unchanged.

**Bullet 4: transferable; nearest sibling `immunity`.**

> Do preserve each blocking precondition and its evidence; changing that condition can reopen exposure even when no application source changed.

An exclusion argument also depends on its blocking assumptions remaining true, so this full condition/evidence change rule transfers.

**Bullet 5: transferable; nearest sibling `immunity`.**

> Don't promote a blocked current path to permanent class exclusion; alternate entrypoints and future configuration changes remain separate evidence obligations.

A sound exclusion review must also reject a permanent claim based on one blocked path and inspect alternatives/configuration, so this entire evidence-boundary rule transfers.

**Bullet 6: transferable; nearest sibling `security-control-and-security`.**

> Do trace internal and background paths for the declared influence as well as public routes; absence from the visible interface does not establish non-exposure.

Internal and background entrypoints can carry the same modeled threat, so the entire alternative-path instruction fits broader security work unchanged.

Count: 6 transferable, 0 partly, 0 specific.

### 102-traceability

**Bullet 1: partly; nearest sibling `auditability`.**

> Do type the relationship instead of using related as a verification claim; a rationale edge and a passing-evidence edge support different trace questions.

An examiner also distinguishes rationale from evidence, but typed edge semantics directly accept different lifecycle navigation questions rather than the final examination judgment.

**Bullet 2: transferable; nearest sibling `conformance`.**

> Do bind evidence to the requirement meaning and artifact revision it assessed; a valid historical result must not silently verify a changed obligation.

A check against selected obligations also needs evidence for the current meaning/revision, so this whole old-versus-current evidence rule transfers.

**Bullet 3: transferable; nearest sibling `auditability`.**

> Don't equate a resolving path with a correct trace; the linked function or test can exist while addressing a different requirement than the edge asserts.

An examiner likewise cannot accept a resolving but irrelevant target as supporting evidence; this full semantic-link instruction transfers.

**Bullet 4: transferable; nearest sibling `analyzability`.**

> Do walk from changed code back to affected requirements as well as forward; a forward-only index can hide obligations whose implementation was removed.

Reverse change-impact analysis also follows changed/removed code to affected obligations, so the whole backward-walk practice applies unchanged.

**Bullet 5: transferable; nearest sibling `auditability`.**

> Do retain superseded lineage separately from current coverage; deleting old relationships can erase why a decision changed without repairing the new evidence gap.

An examination of why a decision changed can need superseded relationships and current gaps, making the full historical-lineage instruction reusable.

**Bullet 6: transferable; nearest sibling `verifiability`.**

> Don't mark an obligation satisfied because its test file is linked; the edge needs relevant result status and does not itself establish behavioral success.

Acceptance-method design likewise cannot infer behavior from a test pathname without relevant results; this entire result-status distinction transfers.

Count: 5 transferable, 1 partly, 0 specific.

### 105-trustability

**Bullet 1: transferable; nearest sibling `dependability`.**

> Don't improve trust by hiding a counterexample; a more favorable response to incomplete evidence can worsen the basis for the actual reliance decision.

A combined failure-reliance case also becomes less justified if a counterexample is hidden, so this full adverse-evidence rule applies unchanged.

**Bullet 2: partly; nearest sibling `certainty`.**

> Do scope capability claims to the context and revision their evidence supports; an unqualified badge can imply permission to rely on untested uses.

A warranted output-confidence statement also needs scoped evidence, but capability/reliance badges imply a broader delegation decision than one output uncertainty claim.

**Bullet 3: partly; nearest sibling `privacy`.**

> Do place material limits where delegation is decided; a discoverable appendix alone may leave the relevant decision using an unsupported promise.

Material handling choices may need visible decision context too, but this rule accepts informed delegation about capability evidence rather than a personal-data purpose or choice policy.

**Bullet 4: transferable; nearest sibling `accessibility-access-control`.**

> Don't treat an evidence display as granted authority; an informed stakeholder decision and the system's actual permission boundary remain distinct conditions.

The Access Control branch likewise must enforce actual authority rather than a favorable evidence display, so this complete separation-of-conditions instruction transfers.

**Bullet 5: transferable; nearest sibling `dependability`.**

> Do keep unknowns different from favorable evidence; confident wording cannot convert an untested capability into a supported delegation premise.

Unknown operational capability also cannot become a supported reliance premise through confident wording, so this whole evidence-calibration rule transfers.

**Bullet 6: specific; nearest sibling `likeability`.**

> Don't use preference or trust ratings as a substitute for evidence calibration; a reassuring presentation can be liked while overstating what may be relied on.

Likeability deliberately accepts subjective response after use; this rule rejects preference/trust ratings as sufficient evidence of justified reliance and accepts a different outcome.

Count: 3 transferable, 2 partly, 1 specific.

Across all rules: 28 transferable, 6 partly, 6 specific.
Evidence provenance, identity, alternate-path, assumption and result-status safeguards remain substantially transferable. Traceability in particular uses techniques an examiner can reuse, while accepting a different navigation result. These limitations are not erased by low literal similarity or by adding the skill name to a rule.

## Per-skill findings and weaknesses

- **Accountability:** Trusted origin, delegated executor and actual outcome are
  explicit, with shared/unknown identities retained honestly. The job example
  cannot establish the human behind a credential, real delegation validity or
  actual grant propagation. All attribution rules in the selected comparison can
  also support examination, threat control or purpose-limited evidence; identity
  attribution is the distinct acceptance result, not an exclusive technique.
- **Auditability:** A question/evidence map, permitted reviewer view, provenance,
  exceptions and collection gaps make examiner sufficiency inspectable. A gap
  correctly prevents an affirmative no-exception conclusion. The example supplies
  no real retention policy, reviewer access or independent examination outcome.
  Evidence context remains transferable to Traceability and Trustability, while
  connected files alone cannot establish an audit answer.
- **Defensibility:** The signal/activation/control/effect chain separates detection
  from containment. Credential, session and queued-work capabilities are distinct,
  and the example does not assume permission to interrupt the job. The timing
  proposal starts at confirmed activation, not first occurrence or detection;
  broader response-latency claims need different anchors. No actual operator
  authority, control behavior or adversarial event is established.
- **Immunity:** The class, enabling path, assumptions, alternate routes and claim
  invalidation are explicit. The fixed-handler example is a conditional argument
  to inspect, not a demonstrated property of any language or dispatch library.
  Loader/dependency closure is unresolved until actual source/config are reviewed.
  Finite tests can expose counterexamples but do not supply universal exclusion
  or a formal proof. This unusual local meaning still needs stakeholder confirmation.
- **Susceptibility:** The source/config/capability map distinguishes reachable,
  verified blocked and unknown paths, plus invocation from actual adverse effects.
  The background scheduler remains unknown instead of being declared safe from
  unavailable permission evidence. Every rule transfers to a broader security or
  exclusion review; exposure classification is the distinct output. The example
  establishes neither an actual vulnerability nor successful exploitation or severity.
- **Traceability:** Typed revisioned edges, semantic targets, reverse impact and
  superseded evidence make lifecycle navigation concrete. A new test file does
  not become a current verification result, and old evidence remains historical.
  The example is a fictional graph, not generated links to this repository's own
  requirements. It supplies no actual automated synchronization or result provenance;
  many semantic-evidence checks remain reusable in audit/examination work.
- **Trustability:** The stakeholder decision, claim scope, material limits,
  fallback and actual authority are separate. The publication example correctly
  keeps draft evidence from granting unattended publication. No informed user
  review or granted authority is observed, and materiality depends on the actual
  decision owner. This local meaning spans evidence presentation and permission
  context; it neither predicts subjective trust nor replaces domain-specific assurance.

Internal rubric review retained rule specificity and unexecuted behavioral evidence
as limitations rather than claiming perfect scores. Mechanism, evidence and
question boundaries are present, but no independent agent or stakeholder has
forward-tested these skills. Local labels do not establish standardized definitions.

## Distinct verification needs and count rationale

- Accountability checks identity model, trusted binding, delegation propagation,
  attempt/effect distinction, false origin, retained-secret boundaries and unknowns.
- Auditability checks question scope, provenance/context, permitted independent
  retrieval, contradictions, missing records, supplied lifetime/access and supported answers.
- Defensibility checks activity/authority, signal correlation, actual activation
  effects, continuation paths, collateral/evidence preservation, stage distinction and reversal.
- Immunity checks class/boundary, actual mechanism/premises, alternate enabling
  paths, configuration challenges, argument/test distinction and invalidation.
- Susceptibility checks influence/environment, prerequisites, evidence state,
  alternative paths, effect distinction, changed conditions and scoped exposure reduction.
- Traceability checks IDs/types/revisions, semantic relevance, forward navigation,
  reverse impact, historical lineage, actual result status and orphan decisions.
- Trustability checks decision/owner, evidence scope, material limits, actual
  decision view, authority effects, unsupported cases and observed-review boundaries.

Rule/check/failure-mode counts are Accountability 5/7/5; Auditability 6/7/4;
Defensibility 6/7/5; Immunity 5/6/6; Susceptibility 6/7/5; Traceability 6/7/5;
Trustability 6/7/5. Counts follow the distinct evidence above, not the five workflow
steps. Auditability's generic compliance failure was removed as redundant, while
Immunity retains a distinct false-formal-proof failure. Repeated counts elsewhere
do not establish equivalent depth or quality.

## References and footprint

Each guide has concrete use-when, trade-off and verification content. The recurring
four-practice presentation is shared structure, not four empty headings. The
practices address different decisions: trusted actor/delegation, independent
examination, scoped intervention, exclusion arguments, exposure prerequisites,
revisioned artifact edges and evidence-calibrated delegation respectively.

Worked examples carry explicit synthetic inputs, expected outputs, evidence or
state across checkpoints, negative cases and unresolved facts. None is a restated
done checklist or a reported target-system test. All reference links are direct
and include read-when guidance; references do not nest further links.

| Skill | Description characters | Body | Complete SKILL.md | Design guide | Worked example | Combined |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| accountability | 467 | 118 | 123 | 35 | 33 | 191 |
| auditability | 477 | 119 | 124 | 35 | 32 | 191 |
| defensibility | 540 | 121 | 126 | 35 | 34 | 195 |
| immunity | 535 | 119 | 124 | 36 | 34 | 194 |
| susceptibility | 491 | 121 | 126 | 35 | 32 | 193 |
| traceability | 454 | 121 | 126 | 35 | 33 | 194 |
| trustability | 517 | 122 | 127 | 35 | 33 | 195 |

Every reference is under 150 lines and every combined footprint is within the
150-250 guideline. These authoring counts are not system requirements and do not
resolve the transfer weaknesses or establish empirical utility.

## Final routing consistency

The description-first table remains the final manual routing result after bodies.
Broad audit-trail, universal-immunity and vague trust requests still require the
listed first question. Attribution, independent examination, active capability
intervention, bounded exclusion, exposure classification, lifecycle navigation
and evidence-backed trust decisions remain separate acceptance questions.
No Phase-5 evals, keyword scores, live-agent routing, incident action, external
notification or batch-10 skill was produced.

## Uncertain claims

- **Accountability:** Actual principal assertions, human/shared identity limits,
  delegation validity, propagation, operation correlation and evidence lifetime
  need source/user confirmation. No synthetic record proves a human's intent or legal responsibility.
- **Auditability:** Review question, expected evidence, examiner view, provenance,
  collection coverage, retention/redaction policy and independent answer sufficiency
  are unknown. The example establishes no audit outcome or legal compliance.
- **Defensibility:** Active activity, granted control scope, credential/session/job
  semantics, activation anchors, evidence needs, collateral constraints and reversal
  conditions require confirmation. No actual capability interruption or response latency was measured.
- **Immunity:** Exact class, enabling operations, handler/loader/dependency closure,
  deployment premises, enforceability and change invalidation are unresolved target
  facts. No finite fixture result establishes a universal exclusion or formal proof.
- **Susceptibility:** Actual deployed capabilities, configuration, background
  permissions, relevant invocation and adverse effects are unknown. The model
  invents no package vulnerability, exploit result or numeric severity score.
- **Traceability:** Authoritative identities, versions, edge semantics, current
  relevance, observed test results and orphan boundaries need confirmation. The
  fictional approval graph establishes no current behavioral requirement pass.
- **Trustability:** Real stakeholder decision, material limitations, evidence scope,
  review outcome, granted authority and fallback require user evidence. Neither
  the draft-tool card nor a preference rating establishes informed appropriate trust.

Ask the user for context-dependent decisions. New skills cite no external standard,
URL, clause, legal duty, tool flag, version or population statistic. Numeric gates
are illustrative and paired with stakeholder confirmation. These are proposed
repository conventions and target-project engineering procedures, not unsupported
claims of actual mechanism guarantees or observed outcomes.

## Validation evidence

- `python scripts/validate_skills.py --only 2,13,35,54,98,102,105`: seven skills, zero errors.
- `python scripts/validate_skills.py`: 57 skills checked, 57 absent todo entries, zero errors.
- `python -m unittest discover -s tests -v`: all 19 foundation tests passed.
- Skill-creator frontmatter validation: all seven new skills valid.
- Scope/catalogue checks passed: only the seven authorized todo statuses became
  draft; earlier skills, approved pilots, shared contracts, scripts, tests and
  similarity threshold remain unchanged. Traceability retains its catalogue category.
- Description triggers, workflow decisions and code/docs inspection, numeric labels,
  direct references, individual limits and combined footprints passed scoped checks.
- Every current rule matches its quoted review: all 40 have named-sibling findings,
  with 28 transferable, 6 partly and 6 specific against the selected nearest sibling.
- Maximum batch-involving body five-gram Jaccard is 0.019241652518392757 for
  integrity/trustability, below unchanged 0.35. Literal-copy detection does not
  resolve the semantic transfer findings or demonstrate behavioral quality.
