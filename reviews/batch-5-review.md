# Batch 5 findings

## Description-first routing

All seven descriptions were written and compared with the comprehension/experience
cluster before any body was authored. This is a manual semantic routing check,
not an agent execution or the later keyword-overlap evaluation. Batch-4 approval
is retained; no previous batch or approved pilot is changed. The batch-2 audit
was committed separately as `942bc57` before this batch.

| Request | Best description / ambiguity | Boundary and first missing fact |
| --- | --- | --- |
| Make the dashboard look nicer | attractiveness | Aesthetic wording; which audience and visual qualities do they dislike? |
| Make this a better experience | Tie: usability / likeability; attractiveness possible | Is the complaint an observed task obstacle, subjective response, or visual appearance? |
| People hate this form even though they finish it | likeability | Negative experience judgment remains distinct from successful completion. What do they report after using it? |
| Tell me when the export finishes | communicativeness | Completion event and delivery point; which recipient/channel and what happens if they leave? |
| Why is this action disabled? | self-descriptiveness outside batch | Current-state explanation, not necessarily a missing notification. |
| This manual ignores failure and recovery topics | comprehensiveness | Missing subject breadth; which audience tasks need those topics? |
| Every required field must appear in the export | completeness outside batch | A bounded required set is already supplied. |
| New users cannot figure out their first report | learnability, usability jointly possible | Is acceptance acquiring independent ability through use, or just completing today's task? |
| Build a lesson so operators can recover a failed import | trainability | Explicit instruction intervention; what skills and allowed practice environment? |
| Make onboarding easier | Tie: learnability / trainability / usability | Does onboarding mean product discovery, a course, or the account-setup task? |
| Our experts keep selecting the wrong recipient | usability | Current task errors without an acquisition claim; what selection outcome and context matter? |
| Use a larger font so these symbols are distinguishable | legibility outside batch | Recognition, not visual preference. |
| Users cannot understand this explanation | comprehensibility outside batch | Interpretation of a passage is not a course or missing-topic claim. |
| People need to learn it faster | learnability / trainability unresolved | Through ordinary product use or a defined training intervention? |

Triggers are natural phrases, not required query syntax. The descriptions name the
most plausible exclusions rather than claiming all cluster siblings are equivalent.
Vague experience, onboarding, and learning requests remain explicit clarification
cases. No trigger phrase is identical across the seven new descriptions.

## Full rule transfer findings

Every Rules of thumb bullet is quoted, with the nearest plausible sibling and
a judgment about moving the entire instruction unchanged. Shared test mechanisms
remain visible; merely naming the current property does not establish exclusivity.
The comparisons use repository boundaries, not unwritten sibling bodies.

### 012-attractiveness

**Bullet 1: specific; nearest sibling `likeability`.**

> Do ask about appearance before task interaction when isolating visual appeal; a frustrating task otherwise contaminates the aesthetic judgment being accepted.

A pre-interaction aesthetic judgment deliberately excludes the experienced interaction that Likeability accepts; moving it unchanged would substitute appearance for that property.

**Bullet 2: specific; nearest sibling `legibility`.**

> Don't infer visual appeal from a contrast or transcription pass; those establish recognition evidence, not whether the audience likes the composition.

This rejects recognition as sufficient visual-appeal evidence; a legibility task instead accepts recognition and would not use appeal as its verdict.

**Bullet 3: partly; nearest sibling `usability`.**

> Do compare the same populated state for aesthetic choices; empty placeholders can make a layout seem attractive while its actual content changes the composition.

Realistic populated states also matter for task trials, but the whole rule concerns how content changes an aesthetic composition rather than a task result.

**Bullet 4: specific; nearest sibling `usability`.**

> Don't choose a visual winner from completion speed; faster interaction can coexist with a less appealing style and answers a different acceptance question.

The rule explicitly rejects completion speed as an aesthetic verdict, whereas task effort is legitimate Usability evidence under its agreed outcome contract.

**Bullet 5: transferable; nearest sibling `likeability`.**

> Do retain opposing visual preferences by audience/context; averaging away a disliked variant's audience is not evidence that its appearance suits them.

Preserving conflicting audience preferences applies unchanged to a subjective interaction preference that includes appearance; this is a shared response-accounting limitation.

Count: 1 transferable, 1 partly, 3 specific.

### 018-communicativeness

**Bullet 1: transferable; nearest sibling `self-descriptiveness`.**

> Do distinguish request acceptance from task completion in user messages; an immediate receipt must not consume the later completion feedback obligation.

Truthful pending versus completed states matter both in visible context and event feedback; the later feedback obligation makes this useful here but does not make it exclusive.

**Bullet 2: partly; nearest sibling `self-descriptiveness`.**

> Do correlate visible feedback with the exact task, not just the active screen; a delayed result for an earlier task can otherwise instruct the wrong next action.

Both need the right object context, but a delayed message arriving on another task is an event-delivery problem absent from a static-state explanation alone.

**Bullet 3: transferable; nearest sibling `self-descriptiveness`.**

> Don't let late progress replace a terminal message; the user would lose the decision-relevant outcome even though every event was technically delivered.

Avoiding stale progress in place of a terminal state also preserves accurate current-state context, so this whole rule can move unchanged.

**Bullet 4: partly; nearest sibling `self-descriptiveness`.**

> Do give missed transient feedback an agreed retrieval point; a toast's lifetime is not a guarantee that a returning user can learn the outcome.

A persistent outcome can provide current context, but retrieving feedback missed during absence accepts delivery continuity rather than just state intelligibility.

**Bullet 5: partly; nearest sibling `self-descriptiveness`.**

> Don't turn duplicate delivery into duplicate next-action prompts; keep a stable outcome reference so replay does not suggest that the task itself happened again.

Stable outcome references support state context, while replayed next-action prompts arise specifically from repeated message delivery.

**Bullet 6: transferable; nearest sibling `usability`.**

> Do test what information arrives before the user must choose the next action; a correct message delivered after that choice does not satisfy its communication purpose.

A task interaction can fail because necessary information arrives after the decision; this timing check also fits overall task performance unchanged.

Count: 3 transferable, 3 partly, 0 specific.

### 024-comprehensiveness

**Bullet 1: partly; nearest sibling `understandability`.**

> Do derive subject breadth from reader decisions rather than the existing table of contents; auditing only current headings cannot reveal an omitted domain.

Audience decisions can identify missing system-model subjects, but discovering omitted explanatory domains is broader than validating a causal mental model.

**Bullet 2: specific; nearest sibling `completeness`.**

> Don't credit a topic heading as coverage when it contains no explanation for the mapped reader decision; breadth counts subjects addressed, not labels displayed.

Coverage of explanatory subjects is explicitly judged by decision-supporting discussion; counting members of a fixed required set alone does not apply this same rule.

**Bullet 3: transferable; nearest sibling `understandability`.**

> Do inspect an audience's handoff and recovery questions when the guide only describes setup; repeating setup details does not fill those missing subject areas.

A system model can also omit handoff or recovery reasoning while overexplaining setup, so the whole rule remains useful for that sibling.

**Bullet 4: partly; nearest sibling `completeness`.**

> Do preserve justified subject exclusions beside the coverage map; unexplored domains must not silently become claims that no audience needs them.

Both require honest boundaries, but an open unexplored subject domain is not automatically an omitted member of an already fixed required set.

**Bullet 5: partly; nearest sibling `conciseness`.**

> Don't use page count as breadth evidence; a long treatment of the happy path can leave every recovery and responsibility question unanswered.

Length is not evidence for either property; this rule diagnoses missing subject domains rather than deciding whether represented material is unnecessary.

Count: 1 transferable, 3 partly, 1 specific.

### 059-learnability

**Bullet 1: partly; nearest sibling `trainability`.**

> Do inspect what users discover before a walkthrough supplies the procedure; teaching the answer can conceal whether ordinary product use permits acquisition.

A trainer could inspect product discovery as an input, but its acceptance is teaching effectiveness; the unchanged instruction warns that teaching can conceal the product-acquisition property.

**Bullet 2: transferable; nearest sibling `trainability`.**

> Don't credit a copied practice answer as transfer; change the task instance while holding the acquired skill demand stable.

Changing the assessment instance while holding skill demand stable is equally necessary for a training intervention and ordinary-use acquisition.

**Bullet 3: transferable; nearest sibling `trainability`.**

> Do record hint use against each attempt instead of erasing failed starts; the independence claim depends on what support the learner actually received.

Assistance accounting is shared evidence for independent acquisition; no word change is needed to use this in training assessment.

**Bullet 4: specific; nearest sibling `trainability`.**

> Do place discovery cues where newcomers first choose between task alternatives; a detached course is not a repair for an unexplained first-use product decision.

The rule repairs the location of a first-use product cue and explicitly rejects a detached course as that repair; a training task instead builds an instruction intervention.

**Bullet 5: transferable; nearest sibling `trainability`.**

> Don't infer retained ability from an immediate repeat; any later-use claim needs a separately agreed interval and a probe after it.

A separate delayed probe is also needed before a training intervention can claim retained ability; this is deliberately shared assessment discipline.

**Bullet 6: partly; nearest sibling `usability`.**

> Do distinguish domain knowledge from product exposure when choosing first-use trials; requiring expert inference can hide the product discovery barrier for genuine newcomers.

Audience expertise affects any task trial, but the failure named here is concealing first-use product discovery rather than current task completion.

Count: 3 transferable, 2 partly, 1 specific.

### 061-likeability

**Bullet 1: specific; nearest sibling `usability`.**

> Don't infer positive experience from repeated visits or completed tasks; required use can coexist with an explicitly disliked interaction.

This rejects behavior as positive subjective-response evidence; task completion is itself part of the Usability acceptance question rather than a sentiment proxy.

**Bullet 2: partly; nearest sibling `usability`.**

> Do preserve negative sentiment beside successful task evidence; changing a user's answer to agree with the outcome erases the property being evaluated.

A usability review should retain disagreements too, but the rule protects a user-reported feeling rather than accepting or rejecting a task result.

**Bullet 3: transferable; nearest sibling `attractiveness`.**

> Do ask about the experienced interaction before naming a proposed redesign; soliciting approval of the author's solution contaminates the sentiment baseline.

A visual-preference interview can also be biased by introducing the proposed redesign before the baseline judgment; the same instruction applies unchanged.

**Bullet 4: specific; nearest sibling `attractiveness`.**

> Don't blend screenshot preference into post-task sentiment; an attractive surface may leave the actual interaction disliked for entirely different reasons.

This rejects substituting screenshot preference for post-task sentiment; Attractiveness can deliberately use that visual judgment as its primary evidence.

**Bullet 5: partly; nearest sibling `usability`.**

> Do retain the moment and reason attached to a preference, not just its rating; changing an unrelated step cannot substantiate the proposed explanation for that preference.

A task review also benefits from locating an obstacle, but a preference-linked reason is not itself the observable task-performance oracle.

Count: 1 transferable, 2 partly, 2 specific.

### 103-trainability

**Bullet 1: partly; nearest sibling `learnability`.**

> Do map each lesson objective to a separately assessed task decision; covering slides about a concept cannot substitute for demonstrating the taught skill.

Skill probes matter to both, but mapping lesson objectives and slides to assessment is specific to an instruction intervention, not ordinary-use acquisition.

**Bullet 2: transferable; nearest sibling `learnability`.**

> Don't reuse a guided exercise's exact answer as the independent assessment; the learner can reproduce the lesson without acquiring its decision skill.

A product walkthrough can leak the same answer into a learning probe; instance separation is shared and the whole rule can move unchanged.

**Bullet 3: partly; nearest sibling `learnability`.**

> Do reset exercise state and verify the next learner's starting conditions; inherited completed work can produce a false training pass without any learner action.

A clean practice setup also matters through product use; inherited classroom/sandbox completion is tied to a teaching fixture here, though the mechanism is reusable.

**Bullet 4: partly; nearest sibling `comprehensiveness`.**

> Do tag instruction and answer keys with the product behavior they teach; a polished obsolete lesson trains a decision the current system rejects.

Source-version fit also matters to explanations, but tagged teaching keys and a trained decision concern an instructional outcome rather than subject breadth.

**Bullet 5: transferable; nearest sibling `learnability`.**

> Don't count attendance, page views, or quiz recall alone as task-skill evidence when the objective is performing a repository or operational workflow.

Neither product-learning nor instruction effectiveness can infer practical ability from page views or recall alone, so the whole rule transfers.

**Bullet 6: transferable; nearest sibling `learnability`.**

> Do separate instructor hints from assessed unaided work; a facilitator's successful diagnosis must not be credited as the trainee's acquired skill.

A facilitator can perform the decision during a product-learning trial too; this is shared independent-acquisition evidence rather than an exclusive teaching mechanism.

Count: 3 transferable, 3 partly, 0 specific.

### 108-usability

**Bullet 1: transferable; nearest sibling `correctness`.**

> Do accept the correct task result on the intended object, not a clicked final control; a smooth flow that submits the wrong recipient is still a failed task.

The correct effect on the intended object can be specified behavior too, so this task-result safeguard is reusable unchanged in a correctness review.

**Bullet 2: partly; nearest sibling `security-control-and-security`.**

> Don't remove mandatory review or authorization to improve completion time; bypassing the task's required constraints does not improve its valid completion.

Retaining authorization is useful security work, but the whole rule judges valid task completion rather than coordination of an adversary/control model.

**Bullet 3: partly; nearest sibling `learnability`.**

> Do preserve permitted valid work after correctable input errors; forcing full re-entry adds task effort unrelated to the correction the user needs to make.

Avoiding re-entry can reduce a newcomer obstacle, but the unchanged rule accepts immediate correction effort without needing acquisition evidence.

**Bullet 4: transferable; nearest sibling `learnability`.**

> Do distinguish independent, assisted, abandoned, and incorrect task outcomes; facilitator rescue must not disappear inside a nominal completion rate.

Separating assisted, abandoned, and incorrect outcomes is equally needed for learning-through-use evidence.

**Bullet 5: transferable; nearest sibling `correctness`.**

> Do exercise correction from the mistaken selection through the final result; a visible undo affordance is insufficient if the wrong-object effect persists.

A correction operation whose wrong-object effect persists is also a specified-behavior defect; this rule can be accepted unchanged there.

**Bullet 6: specific; nearest sibling `likeability`.**

> Don't infer better task performance from a preference vote or visual refresh; inspect goal outcomes and effort under the stated interaction conditions.

This explicitly demands task outcomes instead of preference evidence; Likeability deliberately accepts subjective response rather than substituting observed performance.

Count: 3 transferable, 2 partly, 1 specific.

Across all rules: 15 transferable, 16 partly, 8 specific.
These findings expose residual sibling overlap, especially shared learning assessment and task-result checks. They are not model-routing or user-study evidence.

## Per-skill findings and limitations

- **Attractiveness:** The comparison separates appearance from task success and
  subjective experience. It preserves populated content and records changed
  dimensions, but a bundled change cannot identify which visual choice caused a
  response. The proposed anchored scale has no supplied audience or release
  cutoff; actual rendered variants and audience judgments remain unavailable.
  The opposed-preference rule also fits Likeability unchanged.
- **Communicativeness:** The event/recipient matrix, task identity, monotonic
  outcome, and retrieval path make the task implementable in message handlers,
  state storage, copy, and interaction tests. Real terminal-state precedence and
  retry permissions still require source inspection. The example assumes a
  candidate history feature rather than asserting an existing one. Several rules
  also protect Self-Descriptiveness because truthful state is shared machinery.
- **Comprehensiveness:** The open question-to-subject map distinguishes discovery
  of absent domains from a closed-set inventory. Most repository work is source
  investigation and documentation/navigation editing; code changes are warranted
  only where the actual requested explanation or documentation mechanism needs them.
  Selecting representative reader journeys is a judgment, not evidence of exhaustive
  subject discovery. Restart semantics and handoff ownership in the example remain
  deliberately unresolved instead of invented recovery instructions.
- **Learnability:** Product-first discovery is explicit and the changed-instance
  probe carries assistance and task predicates. Independent assessment, hint
  accounting, and delayed retention checks still transfer to Trainability; those
  shared checks alone cannot route a vague learning request. The example fixes status/owner records and expected
  saved predicates, but supplies no executable application fixture. No observed beginner acquisition or
  next-session retention result exists.
- **Likeability:** The response belongs to users who experienced the interaction;
  successful completion never overwrites a negative judgment. Neutral questions,
  exposure order, and a dual evidence ledger limit obvious confounds, but a stated
  reason does not prove a causal explanation. Removing repeated confirmations is
  only a candidate: the stakeholder must confirm which are mandatory. The skill
  does not establish that any intended audience actually prefers that candidate.
- **Trainability:** Objectives map to practical assessment, the sandbox reset has
  an explicit next-learner check, and keys are bound to product behavior. Creating
  lessons and fixtures is concrete repository work, while effective instruction
  still requires learner evidence. The example's category-validation contract is
  fictional and cannot justify real recovery advice. Instance separation, assistance
  accounting, and practical assessment overlap strongly with Learnability.
- **Usability:** The actual recipient/result, valid-work retention, and end-to-end
  correction path provide testable changes beyond finish-button counting. The
  error trial needs stakeholder definitions of critical errors, usage context,
  assistance, and representative scenarios. Its synthetic dispatch-before/after
  review assumptions must be replaced from the target code. Correct-result and
  undo-effect checks also fit Correctness; the user interaction context establishes
  the intended acceptance question rather than exclusive test mechanics.

Internal rubric review found no absent criterion and did not treat static
validation as behavioral proof. The remaining weaknesses are semantic overlap,
limited hypothetical examples, and unobserved audience outcomes. No perfect-score
claim, certification, participant study, or forward-tested routing is implied.

## Distinct verification evidence

- Attractiveness checks matched populated renders, changed visual dimensions,
  functional preservation, the visual question/anchors, disagreement/missingness,
  and separation from task/sentiment evidence.
- Communicativeness checks event/message semantics, timing anchors, task identity,
  ordering/replay, return retrieval, delivery-stage evidence, and truthful next action.
- Comprehensiveness checks question sources, actual explanation locations,
  neglected subject domains, substantive/findable discussion, owned exclusions,
  and unreviewed audience/journey limits.
- Learnability checks exposure/background, initial attempts, hint leakage,
  assistance history, changed-instance demand, actual task result, and retention limits.
- Likeability checks real exposure, question framing, moment-linked reasons,
  independent task evidence, response categories, comparison confounds, and scope.
- Trainability checks objective alignment, revision fit, starting-to-output rehearsal,
  reset, assessment leakage, assistance/outputs, unassessed skills, and authorization limits.
- Usability checks authoritative goal, blocker/change relationship, correct-object
  success, valid-work preservation, full correction, outcome classes, effort/support,
  and audience/context scope.

The checklists map to different evidence rather than repeating the five workflow
steps. Rule/check/failure-mode counts follow these decisions, not a fixed count:
Attractiveness 5/6/4; Communicativeness 6/7/5; Comprehensiveness 5/6/4;
Learnability 6/7/5; Likeability 5/7/4; Trainability 6/8/5; Usability 6/8/6.
Matching counts are disclosed; they do not establish equivalent content or quality.

## Reference depth and line counts

Each design guide contains concrete use-when, trade-off, and verification material,
not empty practice headings. Each has four practices and 35 lines: this is a shared
presentation structure, while the decisions differ. The worked examples carry
synthetic inputs, observable outputs, unresolved facts, and state/evidence across
checkpoints. No reference nests links to another reference.

| Skill | Description characters | Body lines | Complete SKILL.md | Design guide | Worked example | Combined |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| attractiveness | 381 | 115 | 120 | 35 | 36 | 191 |
| communicativeness | 380 | 122 | 127 | 35 | 36 | 198 |
| comprehensiveness | 441 | 117 | 122 | 35 | 36 | 193 |
| learnability | 415 | 122 | 127 | 35 | 40 | 202 |
| likeability | 410 | 118 | 123 | 35 | 42 | 200 |
| trainability | 461 | 123 | 128 | 35 | 41 | 204 |
| usability | 420 | 128 | 133 | 35 | 37 | 205 |

Every new reference is under 150 lines and every combined footprint is within
the 150-250 guideline. These are repository authoring counts, not system targets.

## Final routing consistency

The description-first table remains the final routing result after body review.
Aesthetic viewing, event delivery, absent explanatory subjects, ordinary-use
acquisition, post-experience response, explicit instruction, and task completion
remain different acceptance questions. The three vague families remain unresolved
without clarification: general experience, onboarding, and faster learning.
No model or keyword-overlap score was computed, and no Phase-5 eval files were created.

## Uncertain claims

- **Attractiveness:** Audience taste, applicable viewing/brand constraints, actual
  recognition performance, and response decision rules are unknown. The queue-screen
  example asserts no observed preference or universally attractive visual choice.
- **Communicativeness:** Real event meanings, terminal precedence, channel rights,
  delivery/read visibility, retrieval persistence, and delivery timing are unknown.
  The export trace and its candidate history mechanism require source confirmation.
- **Comprehensiveness:** Audience needs, topic sufficiency, handoff ownership, and
  import restart behavior are unknown. Subject coverage is a proposed repository
  convention, not an exhaustive external documentation rule.
- **Learnability:** Newcomer background, permitted help, practice dose, representative
  skill demand, independent acquisition, and delayed retention are unknown. The
  filter example supplies no actual beginner observations or saved-filter implementation.
- **Likeability:** No audience sentiment, preferred confirmation boundary, compulsory
  use context, or causal effect of a candidate interaction is established. The
  hypothetical response protocol never supplies invented participant ratings.
- **Trainability:** Prerequisites, safe sandbox behavior, material/product revision,
  assessment validity, learner outcomes, and retention remain target-project decisions.
  Fictional import correction cannot establish real retry or authorization semantics.
- **Usability:** Task criticality, intended users, correct-object dispatch contract,
  correction permissions, valid input retention, effort criteria, and audience task
  outcomes need source/stakeholder confirmation. No preference or backend check alone
  establishes successful intended-user interaction.

No external standards, legal obligations, publisher URLs, library versions, or
population statistics are asserted in these skills. All numeric trial proposals
are explicitly illustrative and paired with stakeholder confirmation. Unknowns
are engineering decisions to ask the user about, not omissions silently filled
from general knowledge.

## Validation evidence

- Batch validation (`--only 12,18,24,59,61,103,108`): seven skills, zero errors.
- Full validation: 34 skills checked, 80 absent todo entries, zero errors.
- Foundation tests: all 19 tests passed.
- Skill-creator frontmatter validation: all seven new skills valid.
- Catalogue/scope checks: only the seven authorized todo statuses changed to draft;
  approved pilots, previous skills, shared contracts, validator threshold, and tests
  remain unchanged. All 39 rule bullets have named-sibling transfer findings.
- Workflow, numeric-label, description-trigger, link, and line-budget checks passed.
- Maximum batch-involving body five-gram Jaccard is 0.015428571428571429 for
  likeability/usability, below the unchanged 0.35 limit. This is a literal-copy
  detector and does not resolve the semantic transfers reported above.
