# Batch 3 findings

## Description-first routing

Descriptions were written as frontmatter-only files and compared before bodies
were authored. Existing batch-2 descriptions and the change/tailoring map supplied
the sibling boundaries. This is manual semantic testing, not measured model routing
accuracy or Phase-5 eval generation. No missing sibling descriptions were invented.

| Prompt | Description fit | Boundary finding / first unresolved question |
| --- | --- | --- |
| "make it configurable" | configurability | Adding supported choices differs from adjusting an already exposed control. Which choices should be exposed? |
| "let admins tweak thresholds" | Tie: configurability / adjustability outside batch | Adding controls and operating existing controls are both plausible. Do those controls already exist? |
| "validate these setting combinations" | configurability | Valid option space is explicit; no live arrangement transition is requested. |
| "let users write their own report templates" | customizability | A user-authored result is explicit; existing hook adequacy may separately require extensibility. |
| "choose a supplied report preset" | configurability | Selecting a built-in result is not stakeholder-defined behavior. |
| "make this customizable" | Tie: customizability / configurability / tailorability | The adjective omits whether behavior is new, options are built in, or context fitting is the goal. What should a user be able to change? |
| "reduce recurring maintenance work" | maintainability | Repeated upkeep, not one bounded edit or one support case, is explicit. |
| "estimate the impact of this rule edit" | No batch-3 winner; modifiability | A named edit does not establish continuing maintenance sustainability. |
| "make it easier to maintain" | maintainability, provisional | Which recurring diagnosis, repair, or modification task is currently difficult? |
| "switch the pipeline while carrying queued jobs" | reconfigurability | The transition and retained state are explicit; the valid choice menu is insufficient. |
| "tune this existing batch cap" | No batch-3 winner; adjustability | The arrangement stays fixed unless contrary evidence appears. |
| "support both manual and automated routes" | No batch-3 winner; flexibility | Independent route coverage does not establish live switching. |
| "help support explain this failed export" | supportability | Case resolution is explicit; runtime evidence and a code repair may support that path without defining its acceptance. |
| "add more logs" | No justified winner; observability outside batch is plausible | Which inference or support-case action should the evidence enable? |
| "why is this change stuck at approval" | No batch-3 winner; changeability | A release handoff is not a user support encounter merely because somebody needs help. |
| "allow different workflows per team" | tailorability, provisional | Team context is explicit, but built-in fitting versus new team-authored behavior remains unknown. Which needs can existing choices satisfy? |
| "each team supplies a new executable policy" | customizability | New authored behavior crosses the supported-choice tailoring boundary. |
| "our partner changed its payload format" | No batch-3 winner; adaptability | External accommodation is not stakeholder-context fitting. |

Descriptions passed length, trigger, and known-sibling checks before any body
existed. The ambiguous prompts remained unresolved; no architecture or built-in
choice set was invented to force a winner. Contextual fit, selection, authored
behavior, and transition can coexist, so these are acceptance scopes rather than
mutually exclusive implementation mechanisms.

## Full Rules of thumb transfer test

Every final rule is quoted below in its original order, with wrapping normalized.
The nearest sibling comes from the disambiguation map, including cross-cluster
neighbors when they provide the closest actual mechanism. No sibling body is
invented. Transferable means a plausible sibling task can reuse the whole rule;
partly means its mechanism is shared but the complete acceptance claim changes;
specific means the tested neighbor does not require that claim. These are semantic
review judgments, not independent-agent results or a calibrated quality score.

### 027-configurability

**Bullet 1: partly; nearest sibling `reconfigurability`.**

> Do distinguish absent, explicit empty, and explicit false values before merging; treating them alike can remove a supported choice while the schema still accepts it.

Absence-aware merging matters before a transition too, but this rule accepts the offered choice semantics rather than retained in-progress state.

**Bullet 2: transferable; nearest sibling `conformance`.**

> Do validate dependent keys as an option combination; silently repairing a conflict makes the displayed choice differ from the supported behavior the user selected.

A configuration document subject to a selected rule set also fails conformance if conflicting choices are silently repaired into a different accepted meaning.

**Bullet 3: specific to this skill; nearest sibling `adjustability`.**

> Do bind omitted-key defaults to a declared configuration meaning; an unrelated code fallback changing that meaning silently changes the offered choice space.

Tuning an existing operating value does not establish or preserve the omitted-key meaning of the offered option space.

**Bullet 4: transferable; nearest sibling `observability`.**

> Do expose the winning source for an effective option; showing every supplied value without resolution cannot explain which supported choice the consumer used.

Explaining runtime state from the effective option and its winning source is a directly reusable observability practice.

**Bullet 5: partly; nearest sibling `customizability`.**

> Do keep built-in option selection separate from user-authored logic; an embedded executable script is not merely another setting when its behavior has no built-in meaning.

Separating executable authorship from built-in selection marks the sibling boundary, but the whole rule does not establish that stakeholder authoring works.

**Bullet 6: partly; nearest sibling `flexibility`.**

> Don't advertise an ignored compatibility key as effective; retaining its syntax for old documents does not make its requested behavior a currently supported choice.

Advertised alternatives also need real behavior, but retaining syntax for an ignored compatibility key is specifically an option-contract problem.

### 032-customizability

**Bullet 1: specific to this skill; nearest sibling `configurability`.**

> Do prove a result derives from stakeholder-authored content; adding a developer preset with a customer label cannot establish user-defined behavior.

Selecting developer-provided presets can fully satisfy configurability, while this rule requires a result derived from new stakeholder content.

**Bullet 2: transferable; nearest sibling `extensibility`.**

> Do supply author-visible inputs explicitly; a custom result requiring private host fields demonstrates a missing authoring capability, not a successful customization.

An independently authored extension also cannot establish admission through a public contract by secretly depending on private host fields.

**Bullet 3: partly; nearest sibling `extendability`.**

> Do separate host admission changes from the authored artifact; a per-customer source fork can conceal that stakeholders still cannot introduce their own behavior.

Separating foundational host work is useful there, but a valid core addition need not prove that ordinary stakeholders can introduce their own behavior.

**Bullet 4: transferable; nearest sibling `extensibility`.**

> Do trace save, selection, and invocation to the same artifact revision; previewing an edited draft while normal execution uses a built-in leaves the customization unproved.

A provider artifact preview using one revision while normal dispatch invokes a built-in is the same admission-evidence failure.

**Bullet 5: transferable; nearest sibling `conformance`.**

> Don't silently drop unsupported authored expressions to obtain a plausible result; a partly ignored artifact cannot be accepted as the stakeholder's intended behavior.

An artifact whose unsupported expressions are ignored does not conform to the selected authored-behavior contract merely because partial output looks plausible.

### 063-maintainability

**Bullet 1: transferable; nearest sibling `evolvability`.**

> Do replay later upkeep against retained repair fixtures; a patch that makes the next maintainer rediscover a solved defect shifts rather than reduces lifecycle work.

Retained repair fixtures can constrain later evolution work too, and rediscovering solved defects contributes to cumulative change cost.

**Bullet 2: partly; nearest sibling `modifiability`.**

> Do retain the regeneration path, not only repaired generated output; a hand-edited artifact that breaks again on regeneration creates recurring maintenance debt.

Regeneration is required work for some bounded edits, but recurring future repair debt extends beyond that single-edit impact claim.

**Bullet 3: transferable; nearest sibling `replicability`.**

> Do make diagnosis prerequisites available in the declared maintainer context; success by an expert's private remembered steps cannot establish a reusable upkeep path.

Another executor cannot reconstruct a procedure from private expert memory, so declared-context prerequisites transfer directly to replicability.

**Bullet 4: partly; nearest sibling `operability`.**

> Do charge recurring operator repair steps to upkeep after a code simplification; moving the work into an undocumented manual ritual does not make maintenance cheaper.

Manual rituals affect operator task execution, but this statement accepts continuing maintenance cost rather than the success of one operational task.

**Bullet 5: transferable; nearest sibling `evolvability`.**

> Don't accept temporary repair scaffolding as free after closing its defect; keep its owner, repeated checks, and removal condition in the continuing upkeep ledger.

An owner, retained checks, and exit condition for temporary scaffolding also belong in inherited obligations across a future change sequence.

### 079-reconfigurability

**Bullet 1: transferable; nearest sibling `recoverability`.**

> Do attach work to its arrangement identity during cutover; a target-ready signal cannot explain which semantics an old in-progress task will finish under.

Restoring unfinished work during recovery also needs its arrangement identity to preserve the semantics under which it completes.

**Bullet 2: partly; nearest sibling `fault-failure-tolerance`.**

> Do define who accepts new work while old ownership drains or transfers; changing routing first can strand accepted tasks between otherwise valid arrangements.

Admission and retained owners can preserve service during faults, but this rule describes a planned arrangement change without a modeled component fault.

**Bullet 3: transferable; nearest sibling `recoverability`.**

> Do checkpoint actual accepted ownership, not just a saved target configuration; resuming from a file revision alone can skip work never admitted by the new owner.

Recovery from a checkpoint cannot infer accepted task ownership from a target file alone; the same receiver-admission gap applies.

**Bullet 4: transferable; nearest sibling `recoverability`.**

> Do test reversal against state written after partial application; restoring the old selector cannot make that state readable under old arrangement semantics.

Restoring an old selector without checking readability of new state is also an invalid usable-state restoration claim.

**Bullet 5: partly; nearest sibling `flexibility`.**

> Do finish representative work through the target after cutover; validating its document or starting an empty target does not prove the running arrangement changed.

Each alternative needs representative work, but processing after cutover additionally claims a carried-state transition that independent alternative coverage does not accept.

**Bullet 6: transferable; nearest sibling `recoverability`.**

> Don't hide mixed old/target ownership behind a single applied flag; partial application needs a recoverable owner for each retained task before completion.

A mixed-state recovery also needs an owner for every retained task before its recovery can be called complete.

### 096-supportability

**Bullet 1: transferable; nearest sibling `debuggability`.**

> Do bind a diagnostic bundle to the reported case's revision and actor context; explaining a current build under admin access can misresolve an older customer symptom.

Localizing a failing execution also requires the correct revision and actor context rather than a current privileged reproduction.

**Bullet 2: partly; nearest sibling `privacy`.**

> Do collect fields that distinguish a runbook decision; a larger bundle with no action-bearing difference increases collection without making that case resolvable.

Purpose-limited field collection is shared, but a case bundle can contain only nonpersonal technical data and this rule specifically requires an action-bearing support distinction.

**Bullet 3: transferable; nearest sibling `operability`.**

> Do test each remedy's case preconditions; a generic retry or reset can hide the symptom while leaving the reported user's underlying outcome unresolved.

An operator remedy with unmet preconditions or an unresolved required task result is likewise not a successful operational action.

**Bullet 4: transferable; nearest sibling `usability`.**

> Do verify resolution through the affected actor's journey; an operator-only success cannot close a case whose user still cannot complete the task.

Operator-only success cannot establish task completion for the intended user in the stated context under usability either.

**Bullet 5: partly; nearest sibling `changeability`.**

> Do retain the minimum missing evidence and authority in an escalation proposal; forwarding an unexplained log dump does not establish a usable next support action.

A useful handoff also needs missing evidence and authority, but the whole rule proposes the next user-case investigation rather than accepting a release-request lifecycle.

**Bullet 6: partly; nearest sibling `observability`.**

> Don't label a new log statement a support improvement until the case decision and permitted action can be followed from it by the declared support provider.

New signals can enable inference, but this rule additionally requires a declared support provider to reach a case decision and permitted action.

### 100-tailorability

**Bullet 1: partly; nearest sibling `flexibility`.**

> Do link each selected option to a named context need and task result; a long preset list cannot demonstrate that this stakeholder's operating constraints fit.

Routes need useful outcomes there too, but one stakeholder context constraint is narrower than coverage of alternatives for a shared task.

**Bullet 2: specific to this skill; nearest sibling `configurability`.**

> Do retain unmet must-haves as fit gaps; relabeling them preferences makes an unsupported context appear accommodated without changing the available behavior.

A valid option menu can leave contextual must-haves unmet without failing the option-space contract; relabeling those needs specifically falsifies contextual fit.

**Bullet 3: partly; nearest sibling `customizability`.**

> Do keep a reproducible recipe of supported choices; an undocumented source patch turns contextual fitting into new behavior without exposing that scope change.

The supported-choice versus new-source boundary is shared, but new stakeholder behavior may be a valid customization rather than a failed fitting recipe.

**Bullet 4: transferable; nearest sibling `correctness`.**

> Do test shared outcomes as well as local preferences; a team-friendly route that omits a required common commit is not an acceptable fit under that shared obligation.

A task required to make a common commit is incorrect when that commit is omitted, regardless of whether contextual fitting motivated the route.

**Bullet 5: transferable; nearest sibling `configurability`.**

> Don't change a global default merely to fit one team unless its wider effects are accepted; local fit is unproved if other declared contexts silently lose theirs.

Changing a global default to emulate a local override can violate the declared scoped meanings of existing configurations, so the same warning fits their resolution contract.

### Transfer counts

| Skill | All rules | Transferable | Partly | Specific to this skill |
| --- | --- | --- | --- | --- |
| configurability | 6 | 2 | 3 | 1 |
| customizability | 5 | 3 | 1 | 1 |
| maintainability | 5 | 3 | 2 | 0 |
| reconfigurability | 6 | 4 | 2 | 0 |
| supportability | 6 | 3 | 3 | 0 |
| tailorability | 5 | 2 | 2 | 1 |
| **Total** | **33** | **17** | **13** | **3** |

The test found actual unchanged reuse; different NFR vocabulary was not treated
as a defense. Recovery/ownership, revision evidence, cost accounting, and context
checks are shared mechanisms. They are retained where their failure directly
invalidates the stated acceptance record, not as free-standing advice to test,
document, or make code clean. This does not make those rules exclusive, and their
continued transferability is a real human-review weakness under rubric specificity.

## Per-skill findings and remaining weaknesses

- **Configurability:** A resolved two-key choice space has explicit valid pairs,
  absence/false distinction, source precedence, and consumer oracles. The example
  does not implement a real resolver, compatibility rollout, or exhaustive combination
  generation. The unknown-key rejection is explicitly illustrative; actual extension
  keys may require another policy. The report-only transition checklist item was
  removed because it was not a separate configuration verification.
- **Customizability:** Saved draft, selected revision, public inputs, concrete text,
  unsupported token, and invalid syntax have separate outputs. Grammar is explicitly
  invented for the fixture, not a claim about any real renderer. It does not establish
  execution isolation, author authorization, or compatibility with an installed host.
  The host-change done item was made a diff comparison rather than mere disclosure.
- **Maintainability:** The carried stale-cache repair fixture, later rule extension,
  regeneration path, and worked active-effort ledger distinguish recurring upkeep
  from one patch. The minutes are invented illustrative arithmetic, not observed
  maintainer performance. One component and a tiny task set do not establish
  organization-wide sustainability, future defect rates, or a universal effort budget.
- **Reconfigurability:** Named pending/running tasks retain arrangement, phase,
  and ownership through interruption. A missing-owner counterexample and unreadable
  old-selector reversal make state loss visible. The example assumes acknowledgement
  and checkpoint semantics; it cannot prove them for an unspecified queue/storage
  implementation. Its rules overlap recoverability heavily even though its trigger
  and primary acceptance question are a planned arrangement change.
- **Supportability:** Case revision, context, requested job, permitted bundle,
  missing-data marker, runbook branch, and affected-user report result are concrete.
  Diagnosis is not reported as an executed remedy. This remains a synthetic support
  policy, not permission to expose those fields in a real case. The code/runbook
  path is scoped, but support authority, production access, and acceptance by another
  owner cannot be supplied by an autonomous repository change.
- **Tailorability:** The night task carries pre-review state into release and a
  saved manifest, with an unaffected day-context control. Unsupported new behavior
  remains a gap rather than being relabeled a preference. Coverage is limited to
  the supplied context tasks; it does not establish every team's needs or live
  migration. Scoped-default and shared-result checks remain useful to siblings too.

## Concrete evidence and counts

Done items are observed comparisons, tests, or artifact inspections rather than
proof that Clarify/Specify/Report headings were followed. Counts follow the content;
matching totals were neither filled to a target shape nor varied for appearances.

| Skill | Distinct done evidence |
| --- | --- |
| Configurability | Key/combination reader cases; absent/empty/false resolution; precedence; actual consumer/scope; defaults; unknown/compatibility policy |
| Customizability | Non-preset authored result; normal saved-artifact invocation; revision/input/output match; unsupported expression; invalid syntax; host/core diff |
| Maintainability | Recurring task completion; clean maintainer prerequisites; retained repair replay; regeneration; full work accounting; temporary-path obligations; measured-versus-synthetic provenance |
| Reconfigurability | Checkpoint identities/owners; new admission boundary; old-work semantics; interrupted recovery; result duplication/loss; target-processed work; reversal compatibility; mixed-state reconciliation |
| Supportability | Affected-context reproduction; permitted bundle generation; excluded-marker check; decision branches; remedy preconditions; user's result; actionable unresolved branch |
| Tailorability | Need/choice/task links; retained gaps; reproducible supported recipe; shared results; unaffected context; accepted priority/difference comparison |

| Skill | Description chars | Body | Full SKILL | Design guide | Example | Combined | Rules | Checks | Failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| configurability | 414 | 119 | 129 | 37 | 37 | 203 | 6 | 6 | 5 |
| customizability | 442 | 119 | 130 | 35 | 33 | 198 | 5 | 6 | 4 |
| maintainability | 471 | 123 | 134 | 38 | 41 | 213 | 5 | 7 | 5 |
| reconfigurability | 444 | 121 | 131 | 36 | 35 | 202 | 6 | 8 | 4 |
| supportability | 477 | 123 | 134 | 37 | 37 | 208 | 6 | 7 | 5 |
| tailorability | 485 | 118 | 129 | 36 | 33 | 198 | 5 | 6 | 4 |

The combined count includes complete SKILL.md, frontmatter and blank lines, plus
both direct references. Bodies meet the target range, each reference stays below
150 lines, and combined footprints meet the 150-250 guideline. Design guides contain
filled use-when/trade-off/verification practices. No external citations or URLs
were added. Numeric proposals and worked arithmetic are labeled illustrative and
paired with stakeholder confirmation; no synthetic number is an observed result.

## Final routing consistency

The pre-body routing table was reread against the completed workflows and examples.
Selecting valid settings is not operating a scalar control; a new authored layout
is not a supplied preset; a fitted recipe is not a proved live transition. The
support case path produces repository-backed diagnostic/remedy evidence, and
maintenance evidence uses recurring upkeep tasks rather than an organizational SLA.
The ambiguous wording remains conditional on existing options, authoring needs,
actual task contexts, and retained work. No surrounding architecture was invented
to force a unique description-level winner.

## Uncertain claims

- **Configurability:** Ask the user for actual key domains, defaults, precedence,
  compatibility/unknown-key policy, scope, and consumer meanings. The example's
  route/review pairs and override order are hypothetical.
- **Customizability:** Ask the user for authoring rights, actual grammar, allowed
  inputs/operations, selection lifecycle, and needed host changes. The delimiter
  syntax and rejection rules do not describe any verified template engine.
- **Maintainability:** Ask the user which tasks and maintainer contexts represent
  continuing upkeep, what effort includes, and who owns temporary/manual work.
  The fixture's freshness contract and active-minute numbers are synthetic.
- **Reconfigurability:** Ask the user for real admission/checkpoint guarantees,
  interruption/loss/duplicate policy, recoverable state, and reversal semantics.
  The A/B state machine does not assert real queue or persistence guarantees.
- **Supportability:** Ask the user for permitted case fields, collection context,
  remedy authority, result oracle, and escalation owner. The bundle policy, reason
  mapping, and reported job ownership are fictional case assumptions.
- **Tailorability:** Ask the user for actual must-haves/preferences, available
  supported choices, context scope, preserved shared outcomes, and accepted gaps.
  The night/day recipes are not verified facts about an installed workflow.

The rubric was assessed internally without a self-score table. Structural validity
and this author review are not independent behavioral proof. No target application,
customer, maintenance session, or live transition was executed; initial question
limits and evidence gathering were not forward-tested by another agent. Full-rule
transfer labels are reviewer judgments and the strongest unresolved quality concern
is shared advice that remains useful under a sibling's acceptance question.

## Validation evidence

- `python scripts/validate_skills.py --only 27,32,63,79,96,100`: six checked, zero errors.
- `python scripts/validate_skills.py`: twenty-two checked, 92 absent todo entries, zero errors.
- `python -m unittest discover -s tests -v`: all 19 foundation tests passed.
- `python scripts/build_index.py`: regenerated 114 entries with only batch-3 status changes.
- Maximum batch-involving body five-gram Jaccard: 0.012672811059907835,
  reconfigurability/tailorability, below the unchanged 0.35 threshold; this is not a semantic transfer detector.
- Skill-creator `quick_validate.py`: all six authored skills passed.
- `git diff --check`: passed.
- Additional scope/contract guards passed: only batch-3 folders, its review, six
  catalogue status changes, and regenerated index belong to this commit; prior
  skills, shared contracts, tooling, and the pre-existing untracked batch-2 audit
  were preserved. All 33 rules have named sibling transfer findings.
- Numeric labeling/confirmation, valid direct reference paths, synthetic JSON,
  per-step decisions, description triggers, and body/combined budgets passed checks.
