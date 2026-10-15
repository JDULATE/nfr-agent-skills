# Batch 8 findings

## Description-first routing and scope

Five new descriptions were written before their bodies. The shared authoring
contract, entire disambiguation map, allowlist, rubric, and all approved pilot
entrypoints were read; Privacy's linked references were also inspected as the
existing batch member. Its entrypoint and references remain unchanged.
Earlier approvals are preserved and do not promote draft statuses to reviewed.

Id 1 retains the original combined label while distinguishing accessible
interaction from authorization. Its category indexes the accessibility branch;
that navigation compromise does not make the branches synonyms. This manual
routing review does not establish empirical agent or keyword-overlap behavior.

| Request | Best fit / ambiguity | Boundary and first missing fact |
| --- | --- | --- |
| Make this accessible | accessibility-access-control, accessibility branch likely | Which audience/task and interaction barrier; is access actually meant as authorization? |
| Fix access | No branch selected | Interaction barriers or actor/action/resource permission decisions? |
| Keyboard users cannot submit this form | accessibility-access-control: Accessibility | Which task, input method, error path, and supported context? |
| Stop cross-team edits through the API | accessibility-access-control: Access Control | Which actor, action, resource, team state, and revocation policy? |
| Stop another team reading the export | confidentiality; Access Control may implement it | Is acceptance the disclosure boundary or the broader action-permission policy? |
| Stop returning hidden fields | confidentiality | Which recipient/field policy and alternate response paths? |
| Make analytics anonymous | anonymity / privacy unresolved | Is the concern identity linkage by a named observer or the purpose/lifecycle of handling? |
| Remove names but retain stable account tokens | anonymity if an unlinkability claim is intended | What auxiliary data and repeated releases can the recipient observe? |
| Collect less personal information | privacy, existing pilot | Which approved purpose, fields, producers, and copies? |
| Handle a GDPR deletion request | privacy, existing pilot | What system behavior does stakeholder policy/counsel require? No legal duty inferred. |
| Detect modified import content | integrity | Which provenance, trusted comparison, and allowed transformations? |
| These measurements are numerically wrong | accuracy outside batch | What real-world reference/error model, rather than an unauthorized alteration path? |
| Threat model this integration | security-control-and-security | Which assets, adversary capabilities, trust boundaries, and misuse consequences? |
| Respond to an attacker in progress | defensibility outside batch | Which active containment/response authority and controls? |
| Make the application secure | security-control-and-security, scope unresolved | Which adversary/assets and misuse paths; is a narrower property the actual goal? |
| Make the screen prettier | attractiveness outside batch | Visual appeal is not accessible interaction or permission enforcement. |

Description exclusions distinguish the nearest acceptance questions. Read and
write authorization can support Confidentiality or Integrity without making those
properties interchangeable. The broad access, anonymity, and secure requests
remain clarification cases rather than being silently assigned a mechanism.

## Full rule transfer findings

Every Rules of thumb bullet is quoted, including all eight in the unchanged
Privacy pilot. The nearest sibling is a plausible boundary comparison from the
map, not an invented sibling body. Transferable means the whole instruction can
serve that sibling unchanged; partly means shared mechanism with a different
acceptance scope; specific means the nearest tested sibling can accept a different
outcome. Shared mechanisms are reported rather than hidden by changing nouns.

### 001-accessibility-access-control

**Bullet 1: specific; nearest sibling `legibility`.**

> Do preserve an operable focus route through dialog opening, error correction, and return; reaching the initial control does not establish an accessible task path.

Character recognition can pass while dialog focus and task continuation fail; the full instruction accepts an interaction path rather than visual symbol recognition.

**Bullet 2: partly; nearest sibling `self-descriptiveness`.**

> Don't replace control meaning or error semantics with visual decoration; an audience using another interaction representation still needs the task decision.

Both expose meaningful state and errors, but making that meaning available through the named alternate interaction representation is a specific barrier question.

**Bullet 3: transferable; nearest sibling `usability`.**

> Do observe the actual accessible task with its required input/assistive context; a preferred visual style or automated pass cannot establish barrier-free completion.

An actual task trial under the specified audience/input context also fits overall task performance, so this instruction can move unchanged.

**Bullet 4: transferable; nearest sibling `security-control-and-security`.**

> Don't treat a hidden or disabled interface action as permission enforcement; direct and background calls must still satisfy the confirmed actor/resource policy.

An adversary can call a hidden action directly, making this whole effect-boundary enforcement rule useful unchanged in threat/control work.

**Bullet 5: transferable; nearest sibling `integrity`.**

> Do bind authorization to the actual resource scope, not only the action name; a valid editor role in one team does not grant edits in another under a scoped policy.

Cross-team alteration is also a prohibited state transition under an integrity policy; binding the actual resource scope transfers unchanged.

**Bullet 6: transferable; nearest sibling `integrity`.**

> Do test changed authority at the effect boundary; an earlier allowed screen state cannot justify a later forbidden action under the confirmed revocation rule.

Changed authority at the mutation boundary also prevents prohibited later alterations, so the whole stale-decision rule applies unchanged.

**Bullet 7: partly; nearest sibling `usability`.**

> Don't force authentication as a fix for an interaction barrier; choosing the wrong branch can add a barrier without repairing either intended acceptance question.

Unnecessary authentication can obstruct task performance too, but the full statement prevents choosing the wrong branch of this combined catalogue label.

Count: 4 transferable, 2 partly, 1 specific.

### 010-anonymity

**Bullet 1: specific; nearest sibling `confidentiality`.**

> Don't equate a replacement identifier with unlinkability; an observer holding its mapping can still identify the subject even if the released name is absent.

A permitted recipient can legitimately hold an identity map under a disclosure policy while still defeating the anonymity claim; those acceptance decisions differ.

**Bullet 2: transferable; nearest sibling `privacy`.**

> Do combine the observer's permitted auxiliary fields and releases during review; individually ordinary clues can jointly answer the exact identity question being claimed hidden.

Personal-data handling review also needs joint clues and repeated releases when assessing identifiability, so this whole observer-review instruction transfers.

**Bullet 3: partly; nearest sibling `privacy`.**

> Do distinguish identity recovery from merely linking records to each other; a stable unnamed profile can violate a cross-context unlinkability goal without a recovered name.

A stable profile can matter to purpose/lifecycle handling too, but the rule distinguishes two explicit observer unlinkability goals rather than broader handling authority.

**Bullet 4: specific; nearest sibling `confidentiality`.**

> Don't hide an identifying mapping from the reviewer while leaving it reachable by the claimed observer; the model must describe access, not the demo's chosen screen.

Leaving an allowed mapping reachable need not violate disclosure permissions, but it invalidates a claim that this observer cannot identify the subject.

**Bullet 5: transferable; nearest sibling `privacy`.**

> Do compare transformed outputs against the confirmed utility task; an empty release avoids links by abandoning the function, not by satisfying a useful anonymity contract.

A purpose-constrained data reduction also must preserve its agreed utility rather than silently abandoning it; this full instruction applies unchanged.

**Bullet 6: partly; nearest sibling `immunity`.**

> Do retain inference and repeated-release gaps in the claim; a clean synthetic join test cannot establish unlinkability against unspecified future auxiliary knowledge.

Both must avoid an unbounded guarantee from finite tests, while the remaining uncertainty here is future observer knowledge and inference rather than exclusion of a named attack/fault class.

Count: 2 transferable, 2 partly, 2 specific.

### 026-confidentiality

**Bullet 1: transferable; nearest sibling `privacy`.**

> Don't send a protected field and rely on display masking; the recipient may already learn it from the emitted payload before the page chooses to hide it.

The Privacy pilot likewise verifies producer/recipient payload absence rather than later display masking; this whole boundary safeguard transfers.

**Bullet 2: transferable; nearest sibling `privacy`.**

> Do apply the field/recipient boundary to error and diagnostic output too; fixing the success response does not close a disclosure through its failure path.

Personal-data capture through errors/logs is explicitly in the pilot inventory too, making this full alternate-output instruction reusable.

**Bullet 3: transferable; nearest sibling `accessibility-access-control`.**

> Do scope cached views by their actual permitted recipients and object context; a cache hit must not bypass the origin path's narrower disclosure decision.

Read authorization can also be bypassed by cache reuse, so the same scoped recipient/object cache rule fits the Access Control branch unchanged.

**Bullet 4: specific; nearest sibling `anonymity`.**

> Don't require identity unlinkability to accept an approved identifiable view; a permitted recipient may learn a name while the separate anonymity claim remains false.

A permitted identifiable view can satisfy this disclosure policy while failing the stated anonymity goal, so moving the acceptance rule unchanged would substitute the wrong property.

**Bullet 5: specific; nearest sibling `privacy`.**

> Do separate a permitted field view from permission to collect or retain its data; the disclosure gate can pass while purpose and lifecycle approval remain unresolved.

A disclosure-only verdict can be positive with broader handling authority unresolved; a Privacy completion verdict would still require those purpose/lifecycle decisions rather than accepting the disclosure result as sufficient.

**Bullet 6: transferable; nearest sibling `privacy`.**

> Do inspect delayed/export copies after policy changes; a narrowed live response cannot establish that an older queued or stored view respects the new boundary.

A choice/recipient handling change can likewise leave older queued or exported personal-data copies, so this whole delayed-copy check transfers.

Count: 4 transferable, 0 partly, 2 specific.

### 057-integrity

**Bullet 1: transferable; nearest sibling `correctness`.**

> Do distinguish an authorized correction from an unauthorized overwrite; preserving every old byte would defeat a transition policy that permits legitimate repair.

Specified state behavior can permit correction while forbidding an overwrite; this complete transition-policy distinction also fits correctness unchanged.

**Bullet 2: transferable; nearest sibling `security-control-and-security`.**

> Don't establish trust by comparing an artifact with a reference supplied through the same untrusted alteration path; both may agree while the protected origin is unestablished.

An adversary controlling content and its claimed reference creates the same trust-boundary problem; the independent-authority instruction transfers.

**Bullet 3: transferable; nearest sibling `accessibility-access-control`.**

> Do enforce protected-field and transition rules at the final writer, including alternate import/admin paths; a restricted editor cannot constrain a bypassing mutation.

The Access Control branch also needs final write enforcement and alternate-entrypoint checks, so this whole protected-field rule applies unchanged.

**Bullet 4: partly; nearest sibling `consistency`.**

> Do bind stale-write decisions to the current approved version at mutation; a valid earlier edit must not silently replace a later state the policy protects.

A versioned agreement policy can also reject stale writers, but the full instruction protects an approved transition at mutation rather than simply checking representational agreement.

**Bullet 5: partly; nearest sibling `atomicity`.**

> Do inspect actual protected state after rejected changes; error responses do not establish alteration prevention if a side path already committed the forbidden value.

An error after committed effects also matters to all-or-none visibility, but this rule rejects a prohibited alteration even when every participating effect committed together.

**Bullet 6: transferable; nearest sibling `accuracy`.**

> Don't call unchanged or provenance-checked data accurate; closeness to the real-world reference is a separate acceptance question from alteration control.

Accuracy review also cannot accept preserved bytes or checked provenance as closeness to a real-world reference; this complete evidence-boundary warning transfers.

Count: 4 transferable, 2 partly, 0 specific.

### 075-privacy

**Bullet 1: specific; nearest sibling `confidentiality`.**

> Do reject optional fields at the producer when their purpose is unconfirmed; do not collect them first on the assumption that retention can be decided later.

An optional field can be perfectly restricted yet unjustified for collection; this rule requires a confirmed handling purpose, not merely permitted readers.

**Bullet 2: transferable; nearest sibling `confidentiality`.**

> Do send even an authorized recipient only the personal fields needed for its approved purpose; permission to receive an account object does not justify forwarding unused contact fields in an analytics event.

A field-specific disclosure policy can likewise allow only a subset to an authorized recipient; the whole per-purpose payload-minimization instruction can serve that case unchanged.

**Bullet 3: partly; nearest sibling `accessibility-access-control`.**

> Do stop optional collection at its source when the confirmed choice is withdrawn; hiding the choice control must not stand in for changing the collection path.

Authority changes also affect permitted actions, but stopping optional collection at its producer follows handling choice rather than a generic action permission alone.

**Bullet 4: partly; nearest sibling `confidentiality`.**

> Do propagate retention and deletion decisions to indexes, caches, derived profiles, and exports; do not let a derived output escape the inventory by renaming it.

Copies matter to disclosure too, but propagating retention/deletion decisions concerns lifecycle rather than who can read the copies.

**Bullet 5: transferable; nearest sibling `recoverability`.**

> Do prevent restored or replayed data from repopulating deleted active records; retain only the suppression evidence approved for that purpose and its own expiry.

A restore procedure honoring deletion constraints must also apply approved suppression and its evidence lifetime, so this whole restore safeguard transfers.

**Bullet 6: partly; nearest sibling `auditability`.**

> Do give disposal evidence its own purpose, minimal personal fields, and expiry; don't recreate the erased profile in a purge log that is retained longer than the approved deletion-evidence purpose requires.

Audit evidence needs appropriate scope too, but this rule specifically prevents recreating personal profiles through deletion evidence retained beyond its purpose.

**Bullet 7: partly; nearest sibling `anonymity`.**

> Don't equate encryption, masking, or a replacement identifier with permission to collect, indefinite retention, or demonstrated anonymity.

Anonymity also rejects identifier substitution as proof, but the whole rule spans collection permission and retention, which remain broader personal-data handling decisions.

**Bullet 8: transferable; nearest sibling `conformance`.**

> Do record user-named regulations or request labels as stakeholder-supplied constraints; ask what their policy or counsel requires of the system, and never state obligations as fact.

A selected-rule conformance task must likewise distinguish stakeholder-provided regulation labels from unverified obligations, so this attribution instruction moves unchanged.

Count: 3 transferable, 4 partly, 1 specific.

### 089-security-control-and-security

**Bullet 1: partly; nearest sibling `defensibility`.**

> Do trace each proposed control to an adversary-controlled step and protected effect; a list of security features does not establish that the misuse path is interrupted.

Active defense also benefits from causal paths, but design-time interruption of an adversary-to-asset path is broader than an operator detecting/containing an ongoing action.

**Bullet 2: transferable; nearest sibling `accessibility-access-control`.**

> Don't promote caller-supplied identity, scope, destination, or policy labels into trusted authority without the confirmed boundary check; a plausible format is not that authority.

The authorization branch must also reject caller-supplied policy labels as trusted entitlement, so the whole boundary instruction transfers.

**Bullet 3: transferable; nearest sibling `integrity`.**

> Do inspect alternate entrypoints and control-failure behavior for the same asset; an attacker path left outside the control can defeat the modeled prevention claim.

An alternate mutation entrypoint or failed control can defeat alteration protection too; this whole bypass/effect rule can move unchanged.

**Bullet 4: partly; nearest sibling `defensibility`.**

> Don't report logging or alerting as prevention after the protected effect happened; separate evidence for detection from evidence that the adversary could not perform it.

Incident response also distinguishes detection from containment, while this instruction specifically bounds a design claim that an effect could not occur.

**Bullet 5: transferable; nearest sibling `confidentiality`.**

> Do preserve legitimate-use controls alongside misuse scenarios; disabling the protected capability can stop the attack by abandoning the accepted product requirement.

An allowed information-view positive control also prevents claiming protection merely by disabling the capability; the complete valid-use rule applies unchanged.

**Bullet 6: transferable; nearest sibling `dependability`.**

> Don't turn an empty scan report into a secure-system verdict; validate the modeled asset/path claims and retain unsupported attacker capabilities as explicit limits.

A reliance argument also cannot treat an empty scan as comprehensive assurance; this whole modeled-claim/evidence-limit instruction transfers.

Count: 4 transferable, 2 partly, 0 specific.

Across all rules: 21 transferable, 12 partly, 6 specific.
Confidentiality accepts a narrower disclosure property using mechanisms also required by Privacy and read authorization. Its identifiable-view and unresolved-purpose rules expose decisions where those acceptance questions differ. Integrity and broad Security likewise share enforcement and provenance work. Description and specification boundaries, rather than exclusive techniques, carry much of the routing distinction; that remains a real specificity weakness.

## Per-skill findings and remaining weaknesses

- **Accessibility/Access Control:** Branch selection, independent requirement rows,
  and paired examples prevent the combined label from pretending that accessible
  interaction and authorization are synonyms. The Accessibility example has a
  concrete opening/error/correction/return path, but no actual assistive session,
  supported-context inventory, or conformance criteria are supplied. It does not
  cover every type of interaction barrier. Access Control records actor/action/
  resource and changed authority, but actual policy precedence and revocation timing
  still need the user. Cross-team/final-effect checks also fit Integrity and Security.
- **Anonymity:** The observer model includes mappings, context, repeated releases,
  and separate named-identity versus profile linkage goals. The feedback example
  demonstrates why a removed name is insufficient under its declared roster view.
  Its coarse-total candidate has no remaining role/key for that particular join,
  but repeated totals and other inference paths remain unassessed. No quantitative
  anonymity model, utility acceptance, or universal guarantee is established.
- **Confidentiality:** Recipient views, errors/logs, scope-aware cache reuse, and
  delayed output make disclosure checks concrete. The boundary rules explicitly
  permit an approved identifiable view without treating it as anonymous, and leave
  broader purpose/retention authority unverified after a disclosure-only pass.
  Field policy and old-copy handling are still stakeholder choices; a current
  response fix cannot retract earlier disclosure. Most mechanisms also belong in
  Privacy and read authorization, so technique overlap remains substantial.
- **Integrity:** Permitted correction, independent trusted expectation, version
  policy, alternate writers, and actual rejected effects distinguish alteration
  protection from factual accuracy. The report example supplies no real trust
  anchor, signature mechanism, conflict policy, or concurrency primitive. It
  deliberately does not infer origin from two attacker-controlled values agreeing.
  Final-write and stale-decision checks remain usable unchanged in authorization
  and Security, and artifact equality alone does not prove freshness or correctness.
- **Privacy, preserved pilot:** Purpose/recipient/copy/lifecycle inventory,
  choice propagation, deletion retries, restore suppression, and capture redaction
  provide detailed engineering decisions. Regulation/request labels remain
  stakeholder-supplied constraints, not legal facts. Sensitive-category/minor
  handling and uninspectable copies still require stakeholder evidence. Its full
  footprint is 455 lines, above the later 150-250 combined guideline; each body and
  reference passes its individual limit. Existing approval is preserved without
  silently editing that exception. Retention/suppression mechanics overlap with
  recovery and disclosure, while handling authority remains a distinct gate.
- **Security/Control and Security:** The asset/adversary/path/control record and
  export-destination example connect implementation points to actual protected
  effects, valid-use controls, and residual exposure. No actual target environment,
  attacker capabilities, scanner output, or unavailable-policy behavior is known.
  The example covers a bounded caller-controlled destination path, not arbitrary
  exploitability or an ongoing incident. Most control mechanics also serve the
  narrower properties; the explicit adversary and causal misuse scope establish
  the broader coordination task rather than exclusive implementation techniques.

Internal rubric assessment found each criterion represented and retained rule
specificity, unobserved audience/security outcomes, and the legacy pilot footprint
as review limitations. No perfect self-score, independent behavioral evaluation,
compliance conclusion, or evidence of an executed attack is asserted.

## Check diversity and count rationale

- Accessibility/Access Control checks branch choice, task/error/return behavior,
  semantic/focus state, policy matrix, alternate entrypoints, scope/revocation
  effects, evidence type, and branch-specific limits.
- Anonymity checks observer scope, release/mapping/copy view, identity versus
  cross-context joins, combined releases, utility, knowledge gaps, and claim limits.
- Confidentiality checks field/recipient policy, channel/copy map, actual negative
  recipient views, positive views, cache/error paths, policy transitions, and visibility gaps.
- Integrity checks allowed transition, independent authority, current-version rule,
  tamper/stale inputs, actual effects, legitimate repair, and alternate writers.
- Privacy checks purpose, copy inventory, choice, lifecycle, forbidden payload,
  subject-scoped disposal/retry, restore suppression, and destination completion scope.
- Security checks assets/adversary/scope, causal path, control location, actual
  misuse effects, bypass/failure behavior, valid use, detection evidence, and residual owners.

Rule/check/failure counts are Accessibility/Access Control 7/8/6; Anonymity 6/7/6;
Confidentiality 6/7/5; Integrity 6/7/5; Privacy 8/8/6; Security/Control and Security
6/8/5. Matching counts are disclosed; the done checks follow different evidence
needs rather than restating the five workflow steps or imposing a fixed item count.

## Reference depth and footprint

The branch guide has separate interaction and permission practices. Anonymity
covers observer/mapping access, combined output, utility, and knowledge limits.
Confidentiality covers recipient views, cached copies, diagnostic output, and
policy transitions. Integrity covers final writes, independent provenance,
version/replay, and mismatch repair. Security covers adversary-to-asset paths,
bypasses, prevention/detection, valid use, and tool findings. Each practice has
concrete use-when, trade-off, and verification guidance, not just a heading.

All worked examples carry synthetic inputs, outputs, and state/evidence through
checkpoints. Id 1 has a worked case for each branch. The approved Privacy example
is retained as written; no example is reported as a measured target-system result.
Every reference is directly linked with read-when guidance, with no nested reference chain.

| Skill | Description characters | Body | Complete SKILL.md | References | Combined |
| --- | ---: | ---: | ---: | --- | ---: |
| accessibility-access-control | 620 | 140 | 145 | design 37; example 38 | 220 |
| anonymity | 481 | 123 | 128 | design 35; example 36 | 199 |
| confidentiality | 449 | 122 | 127 | design 35; example 34 | 196 |
| integrity | 478 | 124 | 129 | design 35; example 34 | 198 |
| privacy | 480 | 170 | 180 | lifecycle 101; design 92; example 82 | 455 |
| security-control-and-security | 484 | 124 | 129 | design 43; example 36 | 208 |

Each reference is under 150 lines. New combined footprints meet the 150-250
guideline; the unchanged approved Privacy pilot is the existing exception.
Line compliance and a low copy score cannot establish property-specific decisions.

## Final routing consistency

The description-first table remains the final manual routing result. Bare access,
analytics anonymity, broad security, and disclosure-versus-action policy still
need their listed first question. Accessibility and Access Control remain separate
branches; recipient permissions, identity linkage, handling purpose, alteration,
and adversarial misuse remain separate acceptance questions even where controls overlap.
No Phase-5 eval artifacts, keyword rankings, live-agent routing, external probing,
or batch-9 skills were produced.

## Uncertain claims

- **Accessibility/Access Control:** Audience/input/assistive support, task barriers,
  policy authority, trusted scope, revocation semantics, and applicable source
  criteria are unknown. The paired examples establish no universal accessibility,
  real permission decision, standards pass, or legal obligation.
- **Anonymity:** Observer access, auxiliary knowledge, release sequence, utility,
  identity inference, and model sufficiency need confirmation. The synthetic roster
  join and coarse-total candidate cannot establish real anonymization or legal status.
- **Confidentiality:** Protected fields, allowed views, recipient scopes, cache/copy
  policy, diagnostic recipients, and observation of delayed/third-party output are
  unresolved target decisions. No actual disclosure-free channel or past-data
  retraction is claimed.
- **Integrity:** Permitted alterations, independent provenance anchor, freshness,
  version/conflict policy, final enforcement, and mismatch response require evidence.
  The fictional report state supplies no real cryptographic or concurrent-write guarantee.
- **Privacy:** Actual purposes, choices, sensitive/minor handling, policy/counsel
  requirements, retention/deletion boundaries, copy coverage, and disposal receipts
  remain stakeholder/project decisions. Approved illustrative deadlines create no
  law or measured disposal result, and uninspectable copies remain gaps.
- **Security/Control and Security:** Asset ownership, adversary capabilities,
  preconditions, real trust boundaries, authorized validation scope, control-failure
  policy, and residual acceptance need source/user confirmation. No scanner,
  exploitability result, prevented attack, live target, or incident action was executed.

Ask the user for these context-dependent decisions. No external standards,
URLs, clause numbers, algorithm prescriptions, legal duties, library versions,
or population statistics are added by the new skills. Numeric acceptance gates
are illustrative and paired with stakeholder confirmation; engineering evidence
must be established in the actual project rather than inferred from a mechanism label.

## Validation evidence

- `python scripts/validate_skills.py --only 1,10,26,57,75,89`: six skills, zero errors.
- `python scripts/validate_skills.py`: 50 skills checked, 64 absent todo entries, zero errors.
- `python -m unittest discover -s tests -v`: all 19 foundation tests passed.
- Skill-creator frontmatter validation: all five new skills valid.
- Scope/catalogue guards passed: only five authorized todo statuses became draft;
  Privacy, previous skills, shared contracts, scripts, tests, and similarity limit
  remain unchanged. Id 1 retains its original category, label, aliases, and slug.
- New workflow/code/docs, trigger, numeric-label, direct-link, individual-limit,
  and combined-budget checks passed. Every reviewed quote matches the current rule.
- All 39 rule bullets have named-sibling findings: 21 transferable, 12 partly,
  and 6 specific against their selected nearest comparison.
- Maximum batch-involving body five-gram Jaccard is 0.017467248908296942 for
  anonymity/integrity, below unchanged 0.35; literal similarity does not resolve
  the semantic transfer weaknesses listed above.
