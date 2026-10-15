# Batch 4 findings

## Scope and description-first routing

The approved Readability pilot is an existing batch member and is preserved,
including its frontmatter and references. Five descriptions were written as
frontmatter-only files before new bodies. The authoring guide, rubric, allowlist,
disambiguation map, and all approved pilot entrypoints supplied the contract.
Batch-3 approval did not trigger a Phase-6 reviewed-status promotion. The pre-existing
untracked batch-2 audit is outside this batch's commit.

The description test below is a manual semantic comparison with sibling criteria
and the actual Readability description, not a model-routing experiment or Phase-5
evaluation generation. Missing audience and intent facts were not invented.

| Prompt | Best route / ambiguity | Boundary finding and first question where needed |
| --- | --- | --- |
| "Explain what this requirement means" | comprehensibility | Interpretation of a particular explanation; which audience and ambiguous statement? |
| "People think this message permits actions that it doesn't" | comprehensibility | Scenario interpretation, not simply shorter wording or a nicer font. |
| "Rename confusing variables and reduce nesting" | readability, existing pilot | Following representation while retaining behavior; an absent domain concept would require comprehensibility too. |
| "Cut repeated wording but keep the exceptions" | conciseness | Avoidable repetition with retained meaning is explicit. |
| "Make this paragraph clearer" | Tie: comprehensibility / readability / conciseness | Does the reader lack a concept, struggle with structure, or face unnecessary material? |
| "These characters look alike on the display" | legibility | Symbol recognition under viewing conditions, not an inference about program meaning. |
| "Make the screen more accessible" | No unique batch-4 route; accessibility-access-control outside batch is plausible | Which interaction barrier and audience are involved? Legibility is only one possible obstacle. |
| "Make the screen more attractive" | No batch-4 winner; attractiveness | Aesthetic response does not establish symbol recognition. |
| "Why is this button disabled?" | self-descriptiveness | Current-state/action inference at the point of use; actual application state still needs inspection. |
| "Tell users at the right point that their task finished" | communicativeness outside batch, possibly self-descriptiveness jointly | Timing/delivery of feedback versus an accurate current-state cue are different acceptance questions. |
| "Help maintainers understand how these components fit together" | understandability | Whole-system responsibility and causal model, not one paragraph's interpretation alone. |
| "Add the missing architecture/security/operations topics to this manual" | No batch-4 winner; comprehensiveness | Subject coverage is the primary gap, not proof of a correct reader model. |
| "Make this easier to understand" | Tie: understandability / comprehensibility / readability | Which artifact or system task is misunderstood, and what should a reader be able to predict or explain? |
| "New users must learn the task faster" | No primary batch-4 route; learnability | Acquiring task ability differs from recognizing symbols or interpreting one explanation. |

All five proposed descriptions passed length, natural-trigger, and catalogue-pointer
checks before body authoring. The two generic clarity prompts remain unresolved;
no description was broadened merely to claim every wording containing understand.

## Full rule transfer findings

Every rule is quoted below, including every rule in the preserved Readability
pilot. The named sibling is the nearest plausible comparison from the map, not
an invented sibling body. Transferable means a plausible sibling task can use the
whole rule unchanged; partly means a shared mechanism without the full acceptance
scope; specific means the closest tested neighbor does not accept that decision.
These are reviewer judgments, not measured router performance or a self-score.

### 023-comprehensibility

**Bullet 1: transferable; nearest sibling `readability`.**

> Do bind ambiguous pronouns to the actual actor and object; an explanation that reads smoothly but assigns permission to the wrong role remains misunderstood.

Binding a pronoun to the actual actor/object can also improve following a passage without changing meaning, so the whole instruction is reusable there.

**Bullet 2: transferable; nearest sibling `understandability`.**

> Do define an unfamiliar domain distinction where this audience needs it; replacing the term with a familiar but different concept creates false understanding.

A false domain concept also produces an incorrect system model, so correcting that distinction does not belong exclusively to one explanation.

**Bullet 3: partly; nearest sibling `learnability`.**

> Do contrast an excluded case when examples could imply an unrestricted rule; positive examples alone can teach permissions the explanation was meant to limit.

Contrasting excluded examples can prevent learning the wrong rule, but the full statement tests interpretation rather than acquisition of task ability.

**Bullet 4: transferable; nearest sibling `understandability`.**

> Do distinguish a causal condition from mere event order; after an event does not mean because of that event unless the source establishes that implication.

A causal system explanation must also distinguish event order from source-supported causation, with no change to this rule.

**Bullet 5: partly; nearest sibling `readability`.**

> Don't repair a missing concept by formatting or renaming alone; check which inference the reader can now make that the original explanation failed to support.

Conceptual gaps can block reading too, but the rule explicitly requires an inference beyond a formatting/naming change and so crosses the representation-only acceptance boundary.

### 025-conciseness

**Bullet 1: transferable; nearest sibling `comprehensibility`.**

> Do merge only claims with the same actor, condition, and obligation strength; similar wording can encode different duties that a shorter sentence would erase.

Merging claims without changing actors, conditions, or obligation strength also preserves the meaning of a clarified explanation.

**Bullet 2: specific to this skill; nearest sibling `comprehensiveness`.**

> Do remove framing that adds no proposition before cutting domain qualifiers; deleting the exception is a meaning change, not a concise expression of the rule.

Removing non-propositional framing before qualifiers is a reduction decision, whereas the sibling accepts needed subject coverage rather than less material.

**Bullet 3: partly; nearest sibling `readability`.**

> Do count displaced definitions and cross-references when shortening a passage; moving all necessary context elsewhere can hide rather than remove representation cost.

External lookups affect reading effort, but the full rule accounts for total representation cost rather than directly accepting how readers follow a passage.

**Bullet 4: transferable; nearest sibling `readability`.**

> Do preserve repeated material when separate use contexts genuinely need it; forcing a single distant statement can make an apparently shorter artifact incomplete.

Keeping necessary local context rather than forcing distant jumps is unchanged advice for following code or prose.

**Bullet 5: transferable; nearest sibling `readability`.**

> Don't use opaque abbreviations to meet a length target; decoding instructions and a new glossary entry can exceed the redundancy supposedly removed.

Opaque abbreviations and their decoding burden can make a representation harder to follow even when its local text is shorter.

**Bullet 6: transferable; nearest sibling `correctness`.**

> Don't equate fewer code tokens with preserved semantics; a condensed expression that changes evaluation, exceptions, or observable effects is a different implementation.

A condensed executable expression that changes effects or exceptions is also a direct correctness counterexample under the retained behavior contract.

### 060-legibility

**Bullet 1: partly; nearest sibling `readability`.**

> Do test the actual confusing glyph pairs in their rendered context; a font that looks clear in a specimen may still obscure the identifier this audience must recognize.

Actual render context can block reading, but the full rule accepts glyph distinction rather than following text or code meaning.

**Bullet 2: specific to this skill; nearest sibling `readability`.**

> Do preserve the literal identifier while improving its rendering; replacing a confusing source character changes the content rather than proving it distinguishable.

Readability may permit a local rename, while this rule preserves the literal identifier specifically to test visual recognition of that content.

**Bullet 3: transferable; nearest sibling `portability`.**

> Do inspect fallback rendering as well as the requested font; missing glyph support can make the delivered symbols differ from the design specimen being accepted.

A platform-movement check can also need actual/fallback rendering to establish that required symbols reach the target environment as intended.

**Bullet 4: partly; nearest sibling `accessibility-access-control`.**

> Do retain difficult characters in the recognition set; removing them can improve an error count without repairing the visual confusion the user reported.

Retaining confusing content is relevant to the accessibility branch, but a recognition set does not establish the broader interaction barriers that skill must disambiguate.

**Bullet 5: transferable; nearest sibling `completeness`.**

> Don't accept larger text that hides required suffixes through clipping; visible glyph recognition cannot compensate for content no longer presented to the viewer.

A display required to present every character also fails completeness when scaling clips required suffix content, regardless of visible glyph quality.

### 078-readability

**Bullet 1: transferable; nearest sibling `comprehensibility`.**

> Do name a local value for its domain meaning or unit; don't shorten it merely to match an abbreviation that the intended reader does not already use.

Preserving domain meaning and avoiding unknown abbreviations can also repair interpretation of one explanation.

**Bullet 2: transferable; nearest sibling `conciseness`.**

> Do expose a meaningful intermediate result when it removes mental unpacking; don't introduce a chain of aliases that makes readers chase the same value.

Unnecessary alias chains add representation and lookup burden while a meaningful intermediate can be necessary context under conciseness too.

**Bullet 3: partly; nearest sibling `simplicity`.**

> Do use guard clauses when they let intended readers trace branch outcomes with less backtracking; preserve effect and exit order, and keep the nesting when flattening merely moves the reading burden to scattered early returns.

Guard clauses and side-effect preservation can support simpler reasoning, but the rule accepts reader backtracking rather than the design machinery or concept count itself.

**Bullet 4: transferable; nearest sibling `comprehensibility`.**

> Do keep a condition and its consequence visibly connected; don't scatter a short explanation across helpers or references just to reduce local line count.

Keeping a condition connected to its consequence also prevents wrong implications in a particular explanation.

**Bullet 5: transferable; nearest sibling `compatibility`.**

> Do clarify an opaque external key with a meaningful local name at its use site, so readers can follow the value without changing the wire contract; don't rename a serialized key or public parameter merely to improve its spelling.

A local alias preserving the external serialized key can also let old and new consumers coexist without a wire-contract change.

**Bullet 6: transferable; nearest sibling `conformance`.**

> Do retain an obligation's actor, condition, exception, and strength when splitting a sentence; don't turn a conditional requirement into an unconditional instruction.

A rewritten requirement must retain the selected source obligations and qualifiers to conform to that agreed rule set.

**Bullet 7: transferable; nearest sibling `comprehensibility`.**

> Don't replace a domain-specific expression with a supposedly simpler synonym until the intended readers confirm that it carries the same meaning.

Replacing a project concept with a supposedly simpler but different synonym is directly an interpretation failure under the sibling.

### 090-self-descriptiveness

**Bullet 1: transferable; nearest sibling `observability`.**

> Do derive status wording from the state that authorizes its available actions; an optimistic label can tell users a draft is saved while the action still uses unsaved data.

Inferring current state from runtime UI evidence also fails when an optimistic label conflicts with the state actually used by the action.

**Bullet 2: partly; nearest sibling `communicativeness`.**

> Do show a disabled action's actual unmet precondition nearby; a generic unavailable label cannot tell the user what the current state permits them to change.

A reason at the appropriate point can be needed feedback, but the full rule explains a current guard rather than specifying message exchange or delivery timing.

**Bullet 3: transferable; nearest sibling `usability`.**

> Do identify the affected object or scope where actions appear; a clear action verb attached to stale record context can explain the wrong operation to the user.

An action shown in stale object context can also prevent the intended user from completing the correct task in context.

**Bullet 4: partly; nearest sibling `comprehensibility`.**

> Do name the effect users are choosing, not just the navigation step; a Continue label cannot explain a commit or submission that changes the object's state.

Action wording needs a clear effect, but this rule accepts inference from an interface control at use time rather than the meaning of a standalone explanation.

**Bullet 5: transferable; nearest sibling `communicativeness`.**

> Do distinguish initiated, pending, and confirmed results in the view; a click alone cannot supply the completion evidence that a success label implies.

Feedback must also distinguish pending from actual completion rather than communicating a click as a completed business result.

**Bullet 6: transferable; nearest sibling `conciseness`.**

> Don't collapse states with different next actions under one friendly label; apparent simplicity can hide the condition needed to infer a permitted next step.

Compressing distinct state meanings into one friendly label loses necessary action conditions, an unchanged meaning-loss warning for shorter representation.

### 106-understandability

**Bullet 1: transferable; nearest sibling `comprehensibility`.**

> Do separate accepted requests from completed business results in the model; merging them teaches a false prediction at every asynchronous handoff.

A particular explanation of an asynchronous path also needs the accepted-versus-completed distinction to avoid a false inference.

**Bullet 2: transferable; nearest sibling `analyzability`.**

> Do connect each important state change to its actual writer and consumer; component names alone cannot explain who makes an outcome authoritative.

Tracing actual writers/readers and state authority also supports dependency and cause analysis instead of merely recognizing component names.

**Bullet 3: partly; nearest sibling `observability`.**

> Do include a failure or interrupted edge for the selected path; a success-only story can leave readers predicting completion after work never reached its owner.

Failure paths inform runtime reasoning, but a reader prediction from a static model is not yet an inference established from actual runtime evidence.

**Bullet 4: transferable; nearest sibling `correctness`.**

> Do reconcile narrative and diagram against the same source revision; explaining proposed ownership as current behavior produces a coherent but false mental model.

A diagram or narrative represented as current behavior is also incorrect when it describes a different source revision or only a proposed design.

**Bullet 5: partly; nearest sibling `comprehensiveness`.**

> Don't add every module merely to make the diagram comprehensive; retain the boundaries needed for the audience's causal questions instead of hiding them in box count.

Audience needs can limit relevant coverage too, but this rule selects causal boundaries for a model rather than accepting coverage of all needed subject areas.

### Transfer totals

| Skill | Rules | Transferable | Partly | Specific to this skill |
| --- | --- | --- | --- | --- |
| comprehensibility | 5 | 3 | 2 | 0 |
| conciseness | 6 | 4 | 1 | 1 |
| legibility | 5 | 2 | 2 | 1 |
| readability | 7 | 6 | 1 | 0 |
| self-descriptiveness | 6 | 4 | 2 | 0 |
| understandability | 5 | 3 | 2 | 0 |
| **Total** | **34** | **22** | **10** | **2** |

Unchanged transfer is real, especially for semantic preservation, context, and
state truthfulness. Those mechanisms support multiple map properties. Their
inclusion is tied to a concrete acceptance failure, not a claim that changing
NFR vocabulary makes advice unique. This remains the main rubric-specificity
weakness and a human-review question. The approved pilot was not rewritten to
hide or reduce its transfer results.

## Per-skill evidence and weaknesses

- **Comprehensibility:** The role/state table distinguishes draft, submitted,
  approved, assigned reviewer, and unassigned reviewer; it exposes a wrong implication
  the original short explanation could invite. The permission model is fictional,
  not authority to change real access behavior. A scenario answer key and a clearer
  candidate do not demonstrate that an actual audience interpreted it correctly.
- **Conciseness:** The source and candidate have actual whitespace word counts
  of 36 and 18, with scope, reviewer assignment, negation, and attachment condition
  retained. The tempting short alternative changes obligations and is rejected.
  This proves literal counts and supplies preservation cases, not measured reading
  benefit. The prose example does not exercise executable condensation or all
  possible linguistic readings; needed context still depends on the artifact owner.
- **Legibility:** The literal identifier has explicit character-level confusion
  outputs, clipping and content-substitution counterexamples. Real rendering,
  target font/fallback, display, scaling, and viewers were not tested. The artifact
  defines a transcription oracle without a universal font/contrast threshold,
  visual-design claim, or accessibility-conformance conclusion.
- **Readability (approved existing pilot):** The calculation exposes an intermediate
  subtotal while preserving external keys, public names, and arithmetic order.
  Its source-grounded questions and reader protocol remain useful tone/depth
  references. Its description's broad simplify-this-paragraph trigger also fits
  conciseness or comprehensibility until the actual obstacle is known. No representative
  reader outcome was produced by this batch. All pilot files remain unchanged.
- **Self-Descriptiveness:** Draft, eligible draft, pending submission, success, and
  retained-draft error have concrete source/view/action distinctions. The example
  refuses to infer submission from enabling a control or initiating work. It does
  not establish actual audience inference, delivery timing, or safe retries;
  current action semantics and state authority need project evidence.
- **Understandability:** Job phase, queue handoff, artifact existence, and authoritative
  ready state are carried through explicit checkpoints and causal questions. It
  demonstrates why a direct success arrow can teach a wrong model. The path is
  fictional and narrow; actual transaction/recovery behavior, other system paths,
  and audience predictions remain unverified.

## Check evidence and footprint

The new done items correspond to source/proposition maps, render/recognition checks,
state/action comparisons, causal predictions, or preserved-meaning cases. They do
not merely require that the workflow headings were followed. Identical counts
were not restored after selecting content, and a fixed count was not used to
claim equal quality. Readability retains its existing checklist without edits.

| Skill | Distinct done evidence in checklist order |
| --- | --- |
| Comprehensibility | Proposition source; source conflict; role/condition/obligation preservation; included/excluded cases; concept definition; unaided answers; remaining wrong inference |
| Conciseness | Same-rule counts; retained proposition map; boundary cases; merge scope; displaced context; code behavior when applicable |
| Legibility | Exact source/render content; reported confusion pairs; actual/fallback glyphs; clipping; unaided transcription; missing audience evidence |
| Readability | Audience/obstacle; source-key questions; agreed reading context; preserved meanings; external names/effects; regression or prose mapping; unaided answers; concern separation |
| Self-Descriptiveness | State/object source; guard agreement; disabled reason; action effect; pending/confirmed states; failed-action retained state; unaided inference |
| Understandability | Owners/readers; same source revision; acknowledgement versus result; interrupted handoff; audience prediction; causal key; intended/actual gaps |

| Skill | Description chars | Body | Full SKILL | Guide | Example | Combined | Rules | Checks | Failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| comprehensibility | 445 | 118 | 129 | 35 | 34 | 198 | 5 | 7 | 4 |
| conciseness | 456 | 120 | 131 | 35 | 38 | 204 | 6 | 6 | 5 |
| legibility | 473 | 119 | 130 | 35 | 31 | 196 | 5 | 6 | 5 |
| readability | 314 | 152 | 162 | 76 | 72 | 310 | 7 | 8 | 5 |
| self-descriptiveness | 462 | 123 | 134 | 35 | 31 | 200 | 6 | 7 | 4 |
| understandability | 468 | 120 | 131 | 36 | 40 | 207 | 5 | 7 | 5 |

Every reference is below 150 lines and every body meets the 80-180 target. The five
new combined footprints are within the 150-250 guideline. The approved Readability
pilot totals 310 combined lines, an existing exception to the later combined-budget
guideline; its body and per-reference sizes still comply. Its approved content and
frontmatter were preserved rather than silently changing the pilot during this batch.
All new references are direct skill-local links with read-when guidance and populated
practice/trade-off/verification material. No standards or external URLs are cited.

## Routing after body authoring

The pre-body routing cases were reread against actual workflows and examples.
Comprehensibility answers a passage's intended inference; Understandability tests a
cross-component model. Legibility transcribes characters; Readability follows their
representation. Conciseness deletes unnecessary material without using word count
as semantic proof. Self-Descriptiveness exposes actual state/action context without
claiming communication timing. The generic clarity/understanding prompts still
need their first question; the existing pilot's broad wording was not edited to
force routing exclusivity.

## Uncertain claims

- **Comprehensibility:** Ask the user for authoritative behavior/policy, intended
  audience, missing concepts, and acceptance scenarios. The example's cumulative
  report audience rules are supplied fiction, not a verified permission model.
- **Conciseness:** Ask the user which propositions, required context, external names,
  and obligations must stay. The illustrative word target is not a universal style
  rule; a valid shorter passage does not by itself establish easier interpretation.
- **Legibility:** Ask the user for target audience/viewing conditions, actual render,
  and allowed style changes. No font, display, contrast result, or user recognition
  score was observed. The numeral in the synthetic identifier is literal content,
  not an unlabeled numeric performance requirement.
- **Readability:** Ask the user for actual reader context, preserved source meanings,
  and unaided responses in the target project. Pilot approval does not supply a
  runtime or reader outcome for this batch; its combined footprint remains a known
  authoring-guideline exception.
- **Self-Descriptiveness:** Ask the user for the authoritative state, guards, actual
  effects, and permitted pending/error behavior. The submission states and retry
  boundaries are hypothetical, not proof of any installed interface contract.
- **Understandability:** Ask the user for actual component ownership, source revision,
  state authority, handoff behavior and model questions. The queue/report outline
  establishes neither real persistence guarantees nor an exhaustive system model.

Internal rubric assessment did not replace independent reader evidence. The shared
rules and existing pilot footprint are explicit human-review limitations; no
self-score table is used to imply objective quality. No participant study, actual
render test, target application execution, or agent forward-test was performed.

## Validation evidence

- `python scripts/validate_skills.py --only 23,25,60,78,90,106`: six checked, zero errors.
- `python scripts/validate_skills.py`: twenty-seven checked, 87 absent todo entries, zero errors.
- `python -m unittest discover -s tests -v`: all 19 foundation tests passed.
- `python scripts/build_index.py`: regenerated all 114 entries; five todo statuses became draft and the pilot stayed draft.
- Maximum batch-involving body five-gram Jaccard: 0.014585764294049008,
  legibility/understandability, below unchanged 0.35; this does not detect semantic transfer.
- The quoted compression fixture was counted directly: 36 words to 18, with 18 removed; its illustrative reduction target arithmetic passed.
- Additional scope checks passed: catalogue changes are limited to five draft statuses; all 34 rules have transfer findings; approved skills and shared tooling remain unchanged. New workflows explicitly inspect code/docs and contain a decision rule in each step.
