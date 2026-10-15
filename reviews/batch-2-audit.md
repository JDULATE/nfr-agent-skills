# Batch 2 skeptical audit

## Overall findings and source boundary

The strongest distinctions are the declared acceptance questions, not the rules.
Many whole rules remain usable in neighboring skills without changing a word.
Adding the current concern's vocabulary does not establish exclusivity. Agility
and Changeability are principally delivery/process-evidence skills in their current
form; their coding-agent implementation work is underspecified.

This audit used the authoring guide, rubric, disambiguation map, and the SKILL.md,
design guide, and worked example for ids 4, 6, 8, 17, 50, and 68. No file in
reviews/ was opened or used as evidence. This findings file is the only output;
source files remain unchanged. The distinctions assessed are local repository
conventions, not standardized terminology or claims about a target project.

## Full Rules of thumb transfer test

Every top-level bullet is included below in its original order. Quotes normalize
line wrapping only. The named destination is the closest candidate in the map:
for a partly or specific verdict it is a tested neighbor, not an assertion that
the whole bullet transfers. Destinations are not restricted to batches 2-3 because
the map also makes evidence, control, and interoperability overlaps explicit.

- **transferable:** a plausible task under the sibling can use the whole rule
  unchanged, including its stated rationale.
- **partly:** a shared practice is reusable, but the full acceptance claim needs
  changed scope or wording to belong to that sibling.
- **specific to this skill:** the tested nearest neighbor does not accept the
  distinguishing claim as written, or the rule would undermine its stated purpose.

Transferable does not mean false, worthless, or applicable to every NFR. These
counts measure lack of exclusive differentiation under this test. The map contains
nested and overlapping concerns, so transfer alone is not proof every such rule
should be removed. No sibling body was invented or assumed to contain this prose.

### 004-adaptability

**Bullet 1 ? transferable; nearest candidate: `portability`.**

> Do name the external assumption an adapter removes; internal cleanup alone cannot demonstrate accommodation of the reported environmental delta.

A platform adapter also removes external environment assumptions, so the unchanged statement can test whether a platform move was accommodated rather than merely refactored.

**Bullet 2 ? transferable; nearest candidate: `interoperability`.**

> Do compare normalized meanings, not accepted payload shapes; parsing both variants with different downstream interpretations fails the retained-result claim.

Interoperability directly requires exchanged variants to retain agreed downstream meaning rather than merely parse successfully.

**Bullet 3 ? partly; nearest candidate: `robustness`.**

> Do select variants from agreed evidence; guessing a condition from missing fields can disguise unsupported input as a successful adaptation.

Evidence-based variant selection supports controlled unexpected-input handling, but the whole bullet claims adaptation success rather than defining the robust response itself.

**Bullet 4 ? transferable; nearest candidate: `portability`.**

> Do pair retained old conditions with the changed condition under the same domain obligation; a new-condition-only suite cannot show what adaptation preserved.

Comparing old and changed execution environments under the same domain obligation is an unchanged portability preservation check.

**Bullet 5 ? transferable; nearest candidate: `interoperability`.**

> Don't propagate vendor-shape branches into unrelated consumers; inspect the boundary output so the same external change cannot acquire conflicting mappings.

Keeping vendor representations behind one mapping boundary prevents conflicting exchange interpretations under interoperability too.

### 006-adjustability

**Bullet 1 ? transferable; nearest candidate: `controllability`.**

> Do trace the applied value at the consuming loop; a writable settings record does not establish that the running operation can be tuned through it.

An operator control must reach the actual consumer to drive an intended operating state, so the saved-versus-applied distinction needs no tuning-specific rewrite.

**Bullet 2 ? partly; nearest candidate: `reconfigurability`.**

> Do bind each affected work unit to its applied value; mid-batch rereads can make a tuning result uninterpretable even though each read is individually valid.

Per-work value snapshots are useful during configuration transitions, but the text concerns a scalar tuning trial rather than the arrangement/state transition that sibling accepts.

**Bullet 3 ? transferable; nearest candidate: `measurability`.**

> Do keep arrangement identity fixed in trials; adding workers with a cap change prevents attributing the observed effect to that cap.

Holding competing variables fixed is equally a requirement of an interpretable measurement procedure for the same control-effect experiment.

**Bullet 4 ? transferable; nearest candidate: `measurability`.**

> Do reconcile requested and applied units before comparing tuning trials; an implicit conversion can make a control-effect claim describe a different adjustment.

Requested/applied unit reconciliation can appear unchanged in a measurement contract because it prevents attributing observations to the wrong independent variable.

**Bullet 5 ? transferable; nearest candidate: `controllability`.**

> Do reverse at the agreed application boundary; restoring a settings file does not show when newly admitted work returns to its former operating value.

Restoring a file rather than the effective state is the same false-positive control-action claim under controllability.

**Bullet 6 ? partly; nearest candidate: `performance-efficiency-time-or-space-bounds`.**

> Don't declare a value better from its requested setting alone; correlate applied value with desired effect and expose compensating resource changes.

A performance-tuning trial uses this correlation and resource accounting, but the current bullet deliberately allows non-performance effects and so is not a complete performance rule.

### 008-agility

**Bullet 1 ? specific to this skill; nearest candidate: `changeability`.**

> Do compare the plan before and after a priority event; finishing work already first in the queue cannot demonstrate response to changed priorities.

The counterexample requires a changed priority order, which the map explicitly separates from an unchanged individual request moving through its lifecycle.

**Bullet 2 ? transferable; nearest candidate: `effectiveness`.**

> Do slice by an accepted outcome of the new priority; smaller tickets without a deliverable result can improve planning statistics while leaving that priority unmet.

Judging a priority slice by an accepted useful result rather than ticket statistics is also an unchanged outcome-attainment rule.

**Bullet 3 ? partly; nearest candidate: `evolvability`.**

> Do carry displaced commitments into the revision; deleting them makes a reprioritization look cheap by erasing the work it interrupted.

Inherited commitments resemble accumulated change obligations, but interrupted delivery work is not itself the system-state sequence that evolvability accepts.

**Bullet 4 ? transferable; nearest candidate: `changeability`.**

> Do replay the new-priority slice against the prior plan's retained gates; faster response bought by deleting a gate changes the constraint, not delivery responsiveness.

An urgent request can traverse its delivery path under retained gates, and deleting those gates cannot demonstrate a faster valid lifecycle under changeability either.

**Bullet 5 ? transferable; nearest candidate: `changeability`.**

> Do charge dependency waits to the changed priority's elapsed timeline; pausing its clock while another owner is needed conceals the bottleneck being assessed.

Counting another owner dependency on the same request timeline applies unchanged to request handoff timing as well as reprioritized delivery.

### 017-changeability

**Bullet 1 ? transferable; nearest candidate: `traceability`.**

> Do bind reached lifecycle states to the same accepted behavior decision; a later artifact with different behavior leaves this request's path incomplete despite its links.

Links whose artifact implements a different accepted behavior fail lifecycle evidence relationships under traceability without any wording change.

**Bullet 2 ? transferable; nearest candidate: `transferability`.**

> Do distinguish ready, offered, and accepted handoffs; the sender's timestamp cannot establish that the receiving owner can progress the request.

Responsibility has not been transferred merely because the sender offered it, which is the same receiving-recipient distinction in the map.

**Bullet 3 ? transferable; nearest candidate: `agility`.**

> Do separate implemented, deployed, enabled, and adopted where they differ; collapsing these states hides the lifecycle bottleneck this skill evaluates.

A reprioritized delivery slice can also stall between implemented, enabled, and adopted, and the unchanged rule identifies that delivery bottleneck.

**Bullet 4 ? transferable; nearest candidate: `operability`.**

> Do retain blocked and rejected outcomes; labeling them complete makes a request path look traversable without the decision required to advance it.

An operator task flow also becomes falsely successful if blocked or rejected steps are reported as completed rather than handled outcomes.

**Bullet 5 ? transferable; nearest candidate: `usability`.**

> Do test the target audience's changed journey; an operator seeing deployment success cannot establish that the audience crossed the adoption endpoint.

A privileged operator success cannot establish intended-audience task completion in the stated context under usability either.

**Bullet 6 ? transferable; nearest candidate: `auditability`.**

> Don't backfill earlier approval from a later state; missing decision evidence leaves the request's path unverified even when the artifact happens to run.

Missing prior authority evidence cannot be reconstructed from later activity when independently examining actions and controls.

### 050-flexibility

**Bullet 1 ? specific to this skill; nearest candidate: `functionality`.**

> Do identify the result shared by alternatives; unrelated features under a mode selector do not establish different ways to accomplish the same task.

Capability coverage may legitimately include unrelated features, whereas this rule requires alternatives for the same task rather than a list of capabilities.

**Bullet 2 ? partly; nearest candidate: `functionality`.**

> Do trace each choice to actual work; aliases for the same blocked implementation cannot satisfy independent alternative coverage.

Real implementation rather than menu labels matters for capability coverage, but independent alternative coverage is an additional acceptance condition in the whole bullet.

**Bullet 3 ? transferable; nearest candidate: `usability`.**

> Do list each route's eligibility before counting it; an administrator-only route is not a usable alternative for an audience without that authority.

A task route unavailable to the intended audience is not usable in that audience context, even when it works for an administrator.

**Bullet 4 ? transferable; nearest candidate: `correctness`.**

> Do compare required writes as well as displayed results; a manual route omitting the task's commit is not an equivalent alternative to the automated route.

For the same manual/automatic task contract, missing the required write is equally a correctness failure despite matching displayed output.

**Bullet 5 ? specific to this skill; nearest candidate: `uniformity`.**

> Do state deliberate route differences; forcing identical intermediate steps can erase the different way of working the stakeholder actually requested.

Deliberately preserving different intermediate routes may conflict with a request for consistent peer conventions, so the warning is not an unchanged uniformity rule.

**Bullet 6 ? transferable; nearest candidate: `reconfigurability`.**

> Don't turn independent route starts into a live-switching promise; coverage of both arrangements does not establish transfer of in-progress task state.

Rejecting successful independent starts as evidence of live-state transfer is directly usable unchanged in a transition-verification skill.

### 068-modifiability

**Bullet 1 ? transferable; nearest candidate: `analyzability`.**

> Do map semantic consumers as well as imports; stored rule results can spread this edit's impact to code with no dependency on the edited function.

Determining change impact from semantic consumers rather than imports is explicitly within analyzability in the map.

**Bullet 2 ? transferable; nearest candidate: `maintainability`.**

> Do include investigation and verification in edit-effort accounting; a tiny patch can require broad reasoning work that changed-line counts conceal.

Ongoing modification effort also includes investigation and verification regardless of patch size, so this accounting rule transfers unchanged.

**Bullet 3 ? transferable; nearest candidate: `analyzability`.**

> Do separate predicted from observed impact; a plausible dependency diagram cannot prove this particular implementation stayed inside its envelope.

Distinguishing a predicted dependency analysis from observed impact is equally an analyzability evidence rule.

**Bullet 4 ? transferable; nearest candidate: `extendability`.**

> Do charge generated adapters and migrations to the edit requiring them; excluding them from a production source count does not remove their change cost.

A new core capability addition must also charge required generated adapters and migrations to its bounded change surface.

**Bullet 5 ? transferable; nearest candidate: `extendability`.**

> Do choose seams from the named edit's fan-out; a generic platform that does not reduce that fan-out can add modification work instead of bounding it.

Choosing a seam by the named addition fan-out rather than adding an unhelpful platform is unchanged advice for bounding a core capability addition.

### Counts

| Skill | All rules | Transferable | Partly | Specific to this skill |
| --- | --- | --- | --- | --- |
| 004-adaptability | 5 | 4 | 1 | 0 |
| 006-adjustability | 6 | 4 | 2 | 0 |
| 008-agility | 5 | 3 | 1 | 1 |
| 017-changeability | 6 | 6 | 0 | 0 |
| 050-flexibility | 6 | 3 | 1 | 2 |
| 068-modifiability | 5 | 5 | 0 | 0 |
| **Total** | **33** | **25** | **5** | **3** |

The clearest shared clusters are Adaptability/Interoperability, Adjustability/Control
and Measurement, Changeability/Evidence and Task Use, and Modifiability/Analyzability
and Extendability. The transfer results are reviewer judgments with concrete
candidate contexts, not measured classifier performance or a numeric quality score.

## Agility and Changeability as repository work

The paths below are artifact categories, not invented files in a target project.
No target application repository was supplied or executed for these examples.

| Work category | Agility: what the current text gives the coding agent | Changeability: what the current text gives the coding agent |
| --- | --- | --- |
| Files / docs | Read delivery records, backlog history, retained decisions and paused work; produce a revised outcome plan and interruption record | Read change request, decision records, released-artifact identity and state evidence; produce a request-to-use trace and blocker record |
| Code | Inspect release code and relevant slice; no specific implementation transformation is described by Design/Implement | Inspect implementation/release path; no concrete handler or lifecycle code transformation is specified by Design/Implement |
| Configuration | Inspect release constraints; the text does not define a necessary configuration change caused by reprioritization | Inspect rollout/audience settings; the preview example exposes a disabled target-team switch, but inspection does not itself authorize enablement |
| Tests | Rehearse urgent-slice acceptance and retained gates, then resume paused work; the exact test inputs and restart artifact are missing | Check deployed-but-disabled and wrong-artifact counterexamples, then run the target-audience journey; concrete switch values and reply fixtures are missing |
| Outputs mainly produced | Plan, timeline, displaced commitments, owners, constraints and missing decisions | State evidence, handoff timing, blockers, artifact links and adoption/enablement findings |
| Outside autonomous repository control | Priority authority, another owner's response, accepted commitments and working-day delivery performance | Approval, receiver acceptance, production enablement and evidence of real user adoption |

**Agility verdict:** mostly planning and delivery-process work. Its narrowest honest
repository scope is handling a user-specified reprioritization within one checkout:
preserving the interrupted patch/context, defining and implementing the newly
accepted slice under existing test/release constraints, and exposing displaced
work. Organizational response-time improvement is a separate process claim, not
something a code edit or synthetic plan rehearsal establishes. The current text
strongly specifies records but weakly specifies the patch/context preservation or
implementation part of that narrower scope.

**Changeability verdict:** mostly request-lifecycle tracking and evidence work, with
a useful repository subset around release identity, audience enablement, and task
acceptance. Its narrowest honest scope is acceptance-readiness analysis for one
named change: matching approved behavior to the actual artifact, identifying
repository-local rollout/configuration blockers, and checking the intended audience's
journey. A controlled fixture can prove a usable path under stated conditions;
it cannot prove organizational approval, handoff acceptance, or production uptake.
The skill's description promises actual adoption more broadly than its example proves.

## Vague-prompt routing

This is a manual description-level fit test. The distinguishing fact was not
silently supplied from a worked example. A lexical favorite is not a verified
route; equal fit refers to missing intent under the available descriptions, not
an automatic keyword tie. Questions below are candidate first clarification,
not questions being asked of the repository owner during this audit.

| Prompt | Best batch-2 description | Equal fit / competing route | First question |
| --- | --- | --- | --- |
| "make this more flexible" | flexibility, provisional word-level favorite | flexibility/adaptability cannot be resolved semantically without knowing whether the user wants supported alternatives or accommodation of an outside change; code-structure intent could instead favor modifiability | "What should become possible: choosing supported task routes, coping with changed external conditions, or editing the implementation more easily?" |
| "make it configurable" | No honest batch-2 winner; adjustability is closest vocabulary but explicitly excludes defining the setting menu | configurability outside batch 2 is the direct map route; no second batch-2 description is an equal justified winner | "Which choices should be exposed, and are we adding controls or adjusting controls that already exist?" |
| "this needs to be adaptable" | adaptability, provisional word-level favorite | adaptability/flexibility are equally unproved because neither external delta nor supported alternatives is specified | "What specific change must it accommodate: an external condition, a user's choice of task arrangement, or a later implementation edit?" |
| "let admins tweak the thresholds" | adjustability, conditional on an existing operating control | No equal batch-2 candidate; configurability outside this batch is equally plausible if the request is to build the administrative control | "Do those admin controls already exist, or should we add a validated way to set the thresholds?" |
| "we need to be more agile" | agility, provisional label match | agility/changeability fit equally until changed priorities are distinguished from slow unchanged request handoffs | "Are priorities changing during delivery, or are individual requests getting stuck along their existing approval-to-use path?" |
| "support new partner formats" | adaptability has the strongest batch-2 surface fit, but its named-environment-change condition remains unproved | No equally strong batch-2 description; interoperability or a new capability/hook outside this batch may fit adding formats alongside unchanged ones | "Is an existing partner changing its contract, or are we adding another format alongside unchanged supported ones?" |
| "make this easier to modify" | modifiability, conditional on a representative implementation edit | No equal batch-2 fit on this wording; maintainability outside this batch remains plausible for a continuing maintenance burden | "Which representative edit should become easier, and is the concern its code impact or ongoing diagnosis and repair?" |
| "allow different workflows per team" | flexibility is the nearest batch-2 surface match, but not a justified full-cluster winner | tailorability is the stronger contextual-fit candidate; configurability or customizability depends on selecting built-ins versus supplying new behavior | "Will teams select existing arrangements, fit a supported workflow to their context, or define new workflow behavior?" |

The hardest false-positive is team-specific workflows: the Flexibility description
omits the tailoring/customization boundary that its body later supplies. The
threshold prompt similarly withholds the existing-control fact Adjustability needs.
The adjective-only prompts cannot establish the deliberately narrow distinctions
merely by repeating the skill names back to the user.

## Description checks

Character counts are for the folded description value: continuation lines joined
with a space, excluding indentation, frontmatter keys, and the folding marker.
All six satisfy the 60-1024 character length rule. Length compliance does not
establish natural discovery or complete boundary coverage.

| Skill | Characters |
| --- | --- |
| 004-adaptability | 451 |
| 006-adjustability | 380 |
| 008-agility | 398 |
| 017-changeability | 385 |
| 050-flexibility | 458 |
| 068-modifiability | 434 |

### Trigger overlap

The following evaluates whole quoted triggers, not just identical-word overlap.
A trigger may fit a sibling even if no other authored description duplicates it.
The whole description sometimes narrows that overlap; the trigger alone does not.

| Description | Actual trigger phrase | Sibling fit or limitation |
| --- | --- | --- |
| 004-adaptability | "the partner feed changed" | Interoperability also covers interpreting a changed feed; external change alone does not distinguish exchange semantics from accommodation. |
| 004-adaptability | "support new operating conditions" | Portability or reconfigurability can also involve new operating conditions; the description exclusions matter more than the trigger. |
| 004-adaptability | "keep this working after the environment changes" | Portability can preserve operation after an execution-environment move; the description excludes that narrower case but the trigger does not. |
| 006-adjustability | "tune the batch size" | Performance tuning can use this exact request; the existing-control and fixed-arrangement clauses are needed to choose the acceptance scope. |
| 006-adjustability | "change the polling interval" | Configurability fits if the user wants the interval exposed as a choice; controllability fits an operational control action. |
| 006-adjustability | "adjust this operating threshold" | Configurability fits exposing a threshold control, while adjustability requires that control already exist. |
| 008-agility | "replan after feedback" | Changeability or supportability can respond to feedback without any changed priority; the trigger omits the fact supplied by the leading description sentence. |
| 008-agility | "respond to new priorities" | This explicitly names priorities and is the strongest distinctive trigger; following one newly urgent request can still involve changeability as a separate concern. |
| 008-agility | "shorten the path from reprioritization to delivery" | This explicitly names reprioritization and is not equally a pure code-edit trigger; changeability overlaps the downstream delivery segment, not necessarily the priority response. |
| 017-changeability | "why is this approved change stuck" | Supportability can investigate why the requester cannot use an approved change; the lifecycle versus support-encounter goal is unstated in the trigger. |
| 017-changeability | "get this change into use" | Agility can deliver a newly prioritized change into use; this phrase alone says nothing about whether priorities changed. |
| 017-changeability | "track this request through approval and rollout" | Traceability covers connecting request/approval/rollout artifacts, and reconfigurability may cover the rollout transition; traversal rather than links or transition state is the claimed distinction. |
| 050-flexibility | "keep manual and automated routes" | Configurability can expose a built-in manual/automatic setting; separate arrangement coverage, not the selector, must be the acceptance target. |
| 050-flexibility | "let us choose another way to do this" | Tailorability or customizability can mean another way for a specific stakeholder; this is a broad overlap with missing description exclusions. |
| 050-flexibility | "support both task arrangements" | Reconfigurability fits if the user means moving between the arrangements, while configurability fits selecting supported modes. |
| 068-modifiability | "how much code must this edit touch" | Analyzability explicitly covers determining change impact, so this can request analysis without an accepted modification bound. |
| 068-modifiability | "limit the ripple effects of this change" | Maintainability and analyzability can both address ripple effects; a particular edit and bounded impact must remain the acceptance scope. |
| 068-modifiability | "estimate the work of changing this rule" | Analyzability can estimate the work from dependencies, and maintainability can judge repeated rule-edit burden; this phrase alone does not demand an observed implementation bound. |

### Boundary against every other member of the change/tailoring cluster

Legend: **E** is an explicit description exclusion naming that sibling; **P** is
only a positive-scope contrast from which a reader can infer different intent;
**M** is an unresolved material overlap with no description-level boundary; **--**
is self. P and M both mean there is no explicit exclusion against that sibling.
These are reviewer judgments, not a requirement to add eleven exclusion clauses.

AD adaptability; AJ adjustability; AG agility; CH changeability; FL flexibility;
MA maintainability; MO modifiability; RC reconfigurability; TA tailorability;
CU customizability; CF configurability; SU supportability.

| Description | AD | AJ | AG | CH | FL | MA | MO | RC | TA | CU | CF | SU |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adaptability | -- | M | P | P | E | P | M | E | M | M | M | P |
| Adjustability | M | -- | P | P | M | P | P | E | M | M | E | P |
| Agility | P | P | -- | E | P | M | E | P | P | P | P | M |
| Changeability | P | P | E | -- | P | P | E | M | P | P | P | M |
| Flexibility | E | E | P | P | -- | P | M | E | M | M | M | P |
| Modifiability | M | P | P | E | M | E | -- | M | M | M | P | P |

Adaptability additionally excludes Portability, and Modifiability additionally
excludes Evolvability; neither is a member of this change/tailoring cluster.

Material gaps are not all equally costly:

- Adaptability does not say when a changed condition is handled by an existing
  scalar control, supported choices, stakeholder fitting, or an implementation edit.
- Adjustability does not name Flexibility even though its body does; an existing
  numeric control can represent a mode/alternative rather than the fixed-arrangement
  operating scalar that the skill actually accepts.
- Agility's descriptions distinguish the two closest process/code siblings, but
  ongoing maintenance responsiveness and support feedback are not explicitly bounded.
- Changeability does not distinguish a support encounter or a stateful rollout
  transition in its description, although those are plausible reasons a request stalls.
- Flexibility lacks Tailorability, Customizability, and Configurability boundaries
  where the realistic team-workflow prompt needs them; the body has some of those
  distinctions, which is too late for description-only selection.
- Modifiability omits Analyzability outside the cluster despite that map criterion
  explicitly including change-impact analysis, and it does not resolve an edit that
  enables alternatives or environmental accommodation inside this cluster.

## Worked-example substance and line counts

No example is a blank scaffold. Concreteness differs substantially; named tasks
and an evidence table alone do not constitute executable input/output/state cases.
Carried state is judged according to the example's purpose: independent routes
should not inherit prior route writes, whereas interrupted work needs an actual
preserved artifact and running tuning needs a work-boundary state.

| Skill | Example lines | Concrete inputs | Concrete outputs | State carried or preserved | Finding |
| --- | --- | --- | --- | --- | --- |
| Adaptability | 34 | `delivery_slot=morning`, `slot_label=morning`, unmapped `flex` | `dispatch_slot=morning`; negative responses remain unnamed policies | Same domain label is preserved; no stored-record before/after or selection discriminator is filled | Concrete positive mapping, partially specified negative cases; substantially better than a checklist, but narrow |
| Adjustability | 36 | Records A-E and illustrative old/new caps | Explicit old/new batch membership lists | Running batch retains old cap in prose; exact partial-batch timeline and effective revision identities are not instantiated | Strongest concrete input/output example; carried running-work state is only partly worked through |
| Agility | 34 | Priority changes from export summary to recipient-filter correction | Accepted plan and passing recipient checks are asserted as event labels, not filled artifacts or result data | Export draft, unresolved decisions and restart condition are named categories without actual contents | Mostly a scenario-shaped process checklist; no concrete repo rehearsal or restart witness |
| Changeability | 36 | Named `reply-preview` request and excluded target team | Preview/edit/send journey is described; no concrete reply payload/result or enablement config values | Request moves through decision/deployment/enablement narrative; artifact revision, audience identity and state records remain unfilled | Partially concrete lifecycle counterexample, not a worked implementation or proof of actual uptake |
| Flexibility | 34 | Shipment `parcel-amber`, selected `depot-east`, manual/automatic modes | Manual commit is explicit; automated output is described as the accepted destination without a worked rule | Fresh matched initial state is required, correctly avoiding cross-route contamination; actual initial record is not filled | Concrete result/side-effect contrast, but weaker automated input/output and no full state fixture |
| Modifiability | 41 | Stored label changes from `ready` to `dispatchable`; reporting reader still filters old label | Intended preserved eligibility, not concrete selected/rejected parcel results | Historical rows and consumer dependence are acknowledged, but no row fixture or final reader/migration state is shown | Concrete dependency surprise; ledger and retained-state evidence remain a categorized plan rather than a completed worked result |

All reference files meet the per-file limit, but their shortness does not resolve
the incomplete examples:

| Skill | Design guide lines | Worked example lines | Full SKILL lines | Combined lines |
| --- | --- | --- | --- | --- |
| 004-adaptability | 41 | 34 | 127 | 202 |
| 006-adjustability | 43 | 36 | 133 | 212 |
| 008-agility | 40 | 34 | 130 | 204 |
| 017-changeability | 44 | 36 | 132 | 212 |
| 050-flexibility | 39 | 34 | 132 | 205 |
| 068-modifiability | 40 | 41 | 133 | 214 |

Each design guide has populated use-when, trade-off and verification practices,
not headings alone. The combined footprints satisfy the guide's 150-250 line
budget; the missing concrete evidence is a depth problem, not a line-limit failure.

## Three weakest passages per skill

These are source quotes with wrapping normalized, followed by the reason for the
finding. Quoted numeric defaults are illustrative examples in their sources and
are paired there with "confirm with the user/stakeholder"; their weaknesses below
concern relevance or evidence, not an invented claim that their labels are missing.
The eighteen passages are not assigned author self-scores.

### 004-adaptability

**Passage 1, `SKILL.md`:**

> support new operating conditions

This trigger can mean a platform move, a supported setting, or another operating arrangement; it supplies no named external delta and cannot carry the intended route on its own.

**Passage 2, `SKILL.md`:**

> Example bound: 0 unexplained semantic differences on paired supported fixtures.

The record supplies a count without defining a general semantic-difference oracle; the field-renaming example gives a narrow mapping, not an executable oracle for the broader operating-environment definition.

**Passage 3, `SKILL.md`:**

> If representations differ but meanings agree, then normalize at that boundary.

This is ordinary interoperability/adapter guidance and covers only representation changes; it is not a general design decision for accommodating other changed operating conditions.

### 006-adjustability

**Passage 1, `SKILL.md`:**

> Example target: cap of 3 records only if valid for the current implementation.

Even with its valid-domain guard and illustrative label, the default presupposes a batch control and units that do not serve polling intervals or thresholds; it risks anchoring an unrelated tuning request to this one example.

**Passage 2, `SKILL.md`:**

> Do reconcile requested and applied units before comparing tuning trials; an implicit conversion can make a control-effect claim describe a different adjustment.

The failure is useful but the whole rule transfers to measurability; control-specific application semantics would distinguish this skill more than restating correct experimental units.

**Passage 3, `SKILL.md`:**

> Compare resource effects against the accepted trade-off boundary.

This done item is checkable only after a resource measure, observation procedure, and boundary are supplied; the worked example demonstrates emitted membership but never fills that separate resource/effect comparison.

### 008-agility

**Passage 1, `SKILL.md`:**

> Proceed to a reversible plan alternative without approving commitments yourself.

The specified output is a plan, while the skill is offered to a coding agent; no corresponding repository patch, interruption snapshot, or code/config change is identified.

**Passage 2, `SKILL.md`:**

> Example bound: accepted revised plan within 2 working days of that event.

This organizational planning-response target is outside a repository agent's sole control and can be met without delivery; its illustrative label prevents a universal claim but does not make it useful evidence of coding-agent agility.

**Passage 3, `SKILL.md`:**

> Rehearse restarting interrupted work without rebuilding unrecorded decisions.

The text names no concrete paused patch, failing test, checkout state, or restart record; the example repeats the desired preservation instead of showing what survives and what successfully resumes.

### 017-changeability

**Passage 1, `SKILL.md`:**

> Adoption: named audience performs the changed journey in a controlled check.

This demonstrates a usable audience path under test conditions, whereas the description promises actual adoption; the source example acknowledges that production uptake is not proved.

**Passage 2, `SKILL.md`:**

> Example handoff bound: owner accepts or records a blocker within 1 working day.

Recording a blocker can satisfy this proposed response bound indefinitely without advancing the change, so this metric is acknowledgement responsiveness rather than lifecycle traversability.

**Passage 3, `SKILL.md`:**

> If no receiver owns the next step, then propose that owner decision and its ready evidence; a sent notification cannot establish an accepted handoff.

The honest output is an organizational ownership decision pending a human, not a repository implementation; without a narrower readiness scope this step primarily documents the reason the agent cannot progress.

### 050-flexibility

**Passage 1, `SKILL.md`:**

> support both task arrangements

The trigger also describes configuration choice or changing arrangements, and it does not distinguish supported alternatives from team-specific fitting or custom behavior.

**Passage 2, `SKILL.md`:**

> Do trace each choice to actual work; aliases for the same blocked implementation cannot satisfy independent alternative coverage.

The blocked-path counterexample is valid but weak: a menu of aliases to one healthy implementation can still fail to offer meaningful alternatives, and shared healthy code can legitimately implement distinct arrangements.

**Passage 3, `SKILL.md`:**

> Do compare required writes as well as displayed results; a manual route omitting the task's commit is not an equivalent alternative to the automated route.

This is a correctness check for a state-changing example rather than a distinctive flexibility design rule, and it says little about alternatives for tasks with no required writes.

### 068-modifiability

**Passage 1, `SKILL.md`:**

> Example bound: 2 production owner components under an agreed ownership map.

The proposed number still depends on packaging and ownership choices rather than demonstrated effort; the narrative example expands the owner surface but does not establish a justified bound.

**Passage 2, `SKILL.md`:**

> Do separate predicted from observed impact; a plausible dependency diagram cannot prove this particular implementation stayed inside its envelope.

This is unchanged analyzability/evidence guidance rather than an architecture decision that reduces the named edit's impact or effort.

**Passage 3, `references/worked-example.md`:**

> Keep measured time in a stakeholder-agreed unit; these task entries are not invented hours or observations of a real team.

The honesty is appropriate, but the surrounding ledger only lists work categories and possible evidence; it never works through an observed or explicitly illustrative effort total, so the example covers impact discovery rather than the stated effort-bound acceptance.

## Evidence limits

The full-rule test covers 33 actual bullets, the description test covers all six
descriptions and every other change/tailoring cluster member, and the routing test
covers the eight supplied vague prompts. No prior review was consulted, no sibling
body was invented, and no real project workflow or routing model was executed.

The transfer labels and boundary matrix are skeptical reviewer judgments based on
the local map. They establish plausible unchanged reuse, not that every transferable
rule is useless or that a shared mechanism must be omitted. Missing source facts
remain unknown: Ask the user about the external delta, existing controls, priority
event, adoption endpoint, alternative set, or representative edit before choosing
an implementation path from a vague request.

Source files were left unchanged. No validators, implementation tests, commits, or
new batch authoring were performed as part of this read-only source audit. The sole
file created is this requested findings report.
