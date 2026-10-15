# Batch 2 findings: change and response boundaries

## Description-first routing evidence

The six descriptions were written as frontmatter-only files and examined before
any bodies or supporting references were written. Length, three distinct quoted
triggers per description, boundary clauses, and catalogue sibling pointers passed
structural checks at that stage. The approved pilots and the current authoring
contract were read before this pass.

The routing below is a manual semantic test against the proposed descriptions and
the cluster's disambiguation criteria. Batch-3 sibling descriptions do not exist;
their map criteria are comparators, not invented descriptions or executed skills.
This is not automatic routing accuracy, a model benchmark, or Phase-5 evaluation.
The test considers what is accepted, rather than matching the word change alone.

| Prompt | Batch-2 result / sibling comparison | Finding |
| --- | --- | --- |
| "The partner feed changed but our required output must stay the same" | adaptability | Named external conditions distinguish this from choosing supported alternatives in flexibility. |
| "Keep working when our supplier changes the event envelope" | adaptability | An environmental contract change is explicit; modifiability can later bound the adapter edit but is not the acceptance question here. |
| "Choose the manual or automated route we already support" | flexibility | No environmental delta; adaptability is excluded. |
| "Move execution to another platform" | No batch-2 skill; portability | The adaptability exclusion names this narrower execution-platform concern. |
| "Tune the batch size without changing this worker arrangement" | adjustability | Existing parameter and fixed arrangement distinguish tuning from a topology transition. |
| "Change the polling interval within its supported operating range" | adjustability | This requests applying a parameter value, not designing the setting menu. |
| "Expose all valid settings and reject invalid combinations" | No batch-2 skill; configurability | Choice schema, not tuning evidence. |
| "Move from a single stage to a staged processing arrangement" | No batch-2 skill; reconfigurability | Applying a different arrangement, rather than keeping alternatives available or adjusting a scalar. |
| "New customer feedback reverses our delivery priorities" | agility | Changed queue and displaced-work decisions distinguish delivery response from one unchanged request's progress. |
| "Replan committed work after the stakeholder changes priority" | agility | Retained delivery constraints and consequences belong to this response test. |
| "An approved unchanged request has no deployment owner" | changeability | A request handoff is stuck; no reprioritization has happened. |
| "Track this change from proposal through actual user adoption" | changeability | A shipped artifact alone cannot establish the requested lifecycle result. |
| "Approval is complete but the target team never adopted the change" | changeability | Adoption evidence is missing for the same request, rather than delivery-plan responsiveness. |
| "Keep manual and automated routes with the same accepted outcome" | flexibility | Supported alternatives are the unit being accepted, not one scalar setting. |
| "Let us choose either task arrangement without losing required outcomes" | flexibility | Alternative feasibility differs from performing a transition safely. |
| "Fit the supported workflow to this department's particular context" | No batch-2 skill; tailorability | Contextual fitting is narrower than providing alternatives in general. |
| "Let customers add their own task behavior beyond built-in options" | No batch-2 skill; customizability | User-defined behavior is not merely a supported alternative. |
| "Bound the impact of changing this existing pricing rule" | modifiability | A named edit and affected implementation surface, not request approvals or cumulative upkeep. |
| "How much code and caller work does this rule edit require?" | modifiability | Impact and effort evidence are explicit; changeability cannot answer them from handoff timestamps. |
| "Make diagnosis, repair, and modifications sustainable over the service life" | No batch-2 skill; maintainability | Continuing maintenance is excluded by the bounded-edit description. |
| "Help support investigate and resolve this reported user issue" | No batch-2 skill; supportability | The support encounter is not an estimate of a specified edit. |
| "Make it easier to change" | Tie: modifiability / changeability; maintainability outside batch also plausible | No implementation change, lifecycle bottleneck, or ongoing-maintenance scope is stated. Ask the user what evidence would count. |
| "Respond faster to changes" | Tie: agility / adaptability / changeability | Changed priorities, an external condition, and request throughput are all unstated. Ask the user what changed and what must respond. |
| "Offer another route and move existing jobs onto it safely" | flexibility plus reconfigurability outside batch | Alternative coverage and actual transition are separate acceptance questions, not an equal single-skill choice. |

The descriptions separated the stated in-scope and near-miss requests under this
reading. The two bare change requests remained unresolved; their intent was not
invented. No description was broadened to win those ties. The batch-3 constraints
were checked as boundaries without creating any batch-3 files.

## Transfer test findings by skill

Three actual Rules of thumb bullets per skill were challenged against plausible
siblings, including Security and Reliability where the mechanism overlaps. Quotes
below are complete bullets with wrapping normalized. A shared mechanism is not
proof of generic filler, and a low similarity score cannot establish NFR specificity.
The comparison is a reviewer judgment against the repository conventions, not an
independent agent execution of either skill.

### 004-adaptability

**Bullet 1; unchanged-transfer challenge: modifiability.**

> Do name the external assumption an adapter removes; internal cleanup alone cannot demonstrate accommodation of the reported environmental delta.

The external assumption and accommodation claim are the decision; an edit-impact bound alone cannot accept them.

**Bullet 2; unchanged-transfer challenge: compatibility / correctness.**

> Do compare normalized meanings, not accepted payload shapes; parsing both variants with different downstream interpretations fails the retained-result claim.

Shared semantic checks remain useful there, but this rule requires meaning agreement across a named environment delta, rather than accepting shape compatibility alone.

**Bullet 3; unchanged-transfer challenge: robustness.**

> Do select variants from agreed evidence; guessing a condition from missing fields can disguise unsupported input as a successful adaptation.

Unknown-input handling is shared; the variant-selection failure here specifically invalidates the accommodation evidence.

### 006-adjustability

**Bullet 1; unchanged-transfer challenge: configurability.**

> Do trace the applied value at the consuming loop; a writable settings record does not establish that the running operation can be tuned through it.

The menu/schema can be valid while the running control is never applied; the rule accepts actual tuning, not option availability.

**Bullet 2; unchanged-transfer challenge: reconfigurability.**

> Do bind each affected work unit to its applied value; mid-batch rereads can make a tuning result uninterpretable even though each read is individually valid.

Work-boundary consistency is shared, but this rule binds emitted work to a parameter adjustment in an unchanged arrangement.

**Bullet 4; unchanged-transfer challenge: accuracy.**

> Do reconcile requested and applied units before comparing tuning trials; an implicit conversion can make a control-effect claim describe a different adjustment.

Unit correctness is shared. The rewritten rule now prevents attributing a different applied adjustment to the requested tuning trial.

### 008-agility

**Bullet 1; unchanged-transfer challenge: changeability.**

> Do compare the plan before and after a priority event; finishing work already first in the queue cannot demonstrate response to changed priorities.

An unchanged request can progress without any reordered priority; this rule demands before/after priority response.

**Bullet 3; unchanged-transfer challenge: maintainability.**

> Do carry displaced commitments into the revision; deleting them makes a reprioritization look cheap by erasing the work it interrupted.

Retaining work is shared, but deleting displaced commitments specifically falsifies the claimed cost of reprioritization.

**Bullet 4; unchanged-transfer challenge: security-control-and-security / reliability.**

> Do replay the new-priority slice against the prior plan's retained gates; faster response bought by deleting a gate changes the constraint, not delivery responsiveness.

Release gates can support these NFRs, but the rewrite compares prior/new priority paths under retained constraints; it does not assert gate adequacy or failure-free operation.

### 017-changeability

**Bullet 2; unchanged-transfer challenge: accountability.**

> Do distinguish ready, offered, and accepted handoffs; the sender's timestamp cannot establish that the receiving owner can progress the request.

Actor attribution does not establish receiver acceptance; ready/offered/accepted states distinguish this request handoff.

**Bullet 3; unchanged-transfer challenge: observability.**

> Do separate implemented, deployed, enabled, and adopted where they differ; collapsing these states hides the lifecycle bottleneck this skill evaluates.

Visible state is helpful there, but the rule prevents a deployed request from being counted as adopted when its lifecycle still has a bottleneck.

**Bullet 6; unchanged-transfer challenge: auditability.**

> Don't backfill earlier approval from a later state; missing decision evidence leaves the request's path unverified even when the artifact happens to run.

Authority evidence is shared. The acceptance consequence here is an unproved path for this request, not a general independent-audit claim.

### 050-flexibility

**Bullet 1; unchanged-transfer challenge: functionality.**

> Do identify the result shared by alternatives; unrelated features under a mode selector do not establish different ways to accomplish the same task.

A set of unrelated features can meet capability coverage but cannot establish alternative ways to do the same task.

**Bullet 2; unchanged-transfer challenge: availability.**

> Do trace each choice to actual work; aliases for the same blocked implementation cannot satisfy independent alternative coverage.

A blocked path affects service use, but several labels reaching that path cannot demonstrate an independent alternative arrangement.

**Bullet 6; unchanged-transfer challenge: reconfigurability.**

> Don't turn independent route starts into a live-switching promise; coverage of both arrangements does not establish transfer of in-progress task state.

This is an explicit boundary: independent route starts cannot establish transfer of live work, which belongs to the sibling.

### 068-modifiability

**Bullet 1; unchanged-transfer challenge: traceability.**

> Do map semantic consumers as well as imports; stored rule results can spread this edit's impact to code with no dependency on the edited function.

Connected artifacts alone do not bound an edit. The rule includes semantic consumers missed by an import-only impact map.

**Bullet 3; unchanged-transfer challenge: measurability.**

> Do separate predicted from observed impact; a plausible dependency diagram cannot prove this particular implementation stayed inside its envelope.

Evidence versus forecast is shared; the test here is whether this named implementation stayed within its predicted impact envelope.

**Bullet 4; unchanged-transfer challenge: maintainability.**

> Do charge generated adapters and migrations to the edit requiring them; excluding them from a production source count does not remove their change cost.

Lifecycle cost can include these categories too, but the rule charges generation and migration to the particular edit requiring them.

Four initially transferable candidates were tightened during this pass: retaining
old-condition tests became paired accommodation evidence; preserving units became
a requested/applied tuning-trial comparison; retaining gates became a prior/new
priority comparison; request identity became behavior-specific state evidence.
These were decision changes, not simply substitutions of NFR names.

No sampled final rule was accepted solely because its vocabulary differed. The
unit conversion, gate, authority, and forecast rules still share mechanisms with
neighbors; they are retained because their stated failed acceptance claim differs.
That judgment remains a human-review point, especially for Adjustability versus
Configurability and Changeability versus Auditability. No claim of NFR-exclusive
mechanisms or perfect transfer resistance is made.

## Per-skill evidence and remaining weaknesses

- **Adaptability:** The fictional old/new feed fields normalize to the same domain
  slot, while unmapped meaning and conflicting condition evidence remain negative
  cases. The worked example is a representation change, not evidence for resource,
  network, or other operating-environment adaptation. Source-version selection and
  mapping authority require actual partner evidence. No real environment was tested.
- **Adjustability:** Concrete batch memberships distinguish a saved control from
  an applied value; the example also separates current and next-batch semantics,
  reversal, and resource effects. It does not establish any speed improvement or
  a valid production range. Immediate controls and gradual convergence may require
  a different application event than this example's next-batch snapshot.
- **Agility:** The priority reversal retains an unfinished export commitment and
  a blocking owner decision; accepted-plan response is separated from delivery.
  The example has no measured calendar timestamps or repeated priority churn.
  It cannot show sustained team responsiveness, optimal prioritization, or an
  empirical interruption cost. Real owners must accept any displaced commitment.
- **Changeability:** The approved, deployed, disabled change demonstrates why
  target-audience use is separate from code or deployment completion. The fixture
  is controlled adoption evidence, not real audience uptake. Some processes have
  different states or approval boundaries; adding the example's states everywhere
  would introduce needless ceremony. The handoff response is not guaranteed approval.
- **Flexibility:** Manual and automatic task routes must both commit the shared
  destination; display-only success, label aliases, and audience restrictions are
  explicit counterexamples. The route coverage example does not exercise live
  transitions or prove how useful either alternative is to real users. Shared code
  does not disqualify alternatives if their actual work arrangements are meaningful.
- **Modifiability:** The stored-label consumer exposes a dependency outside the
  original import/owner prediction. The example includes a work-category ledger,
  but no invented hours or actual effort measurements. A source-count envelope
  remains packaging-dependent; the real owner/contract map and measured coordination
  are necessary before asserting bounded change effort. Historical-data policy is open.

## Done evidence and content-driven counts

Done items test distinct observations rather than requiring that workflow steps
were merely performed. Counts follow the identified evidence and failure cases;
matching counts were neither a target nor artificially varied to look original.

| Skill | Done evidence in checklist order |
| --- | --- |
| Adaptability | Reproduced external delta; paired domain outcomes; condition selection; unsupported case; retained old condition; downstream mapping leakage |
| Adjustability | Applied value/unit; invalid-domain rejection; application boundary; override scope; controlled effect; reversal; resource trade-off |
| Agility | Actual priority revision; response clock; accepted new outcome; retained gates; displaced artifacts; restart rehearsal |
| Changeability | Behavior identity across states; gate authority; refused/unaccepted handoff; waiting clock; deployed-versus-enabled distinction; audience use; truthful terminal state |
| Flexibility | Independent route completion; shared writes/results; distinct dispatch; unavailable choice; non-elevated prerequisites; allowed result differences |
| Modifiability | Actual owner map; semantic consumers; public changed-rule case; retained cases; generation/migration work; effort ledger; out-of-envelope gaps |

## Footprint and structure

All references are direct skill-local links with read-when guidance, populated
practice/condition/trade-off/verification content, and an explicitly synthetic
worked example. No external standard, URL, tool flag, or version is cited.
The total includes complete SKILL.md, frontmatter and blank lines, plus both refs.

| Skill | Description chars | Body | Full SKILL | Design guide | Example | Combined | Rules | Checks | Failure modes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adaptability | 451 | 116 | 127 | 41 | 34 | 202 | 5 | 6 | 4 |
| adjustability | 380 | 123 | 133 | 43 | 36 | 212 | 6 | 7 | 5 |
| agility | 398 | 120 | 130 | 40 | 34 | 204 | 5 | 6 | 4 |
| changeability | 385 | 122 | 132 | 44 | 36 | 212 | 6 | 7 | 5 |
| flexibility | 458 | 121 | 132 | 39 | 34 | 205 | 6 | 6 | 4 |
| modifiability | 434 | 123 | 133 | 40 | 41 | 214 | 5 | 7 | 5 |

All bodies meet the 80-180 target and every reference is under 150 lines. Combined
footprints meet the 150-250 guideline without padding them to the same total.
Every workflow begins with code/docs inspection and has If/then decisions in each
step. The improvement paths offer complete proposed records and at most three
initial questions, with unknown acceptance choices left open.

## Routing after body authoring

The pre-body routing table was reread against the completed Use when sections and
workflows. No description silently delegates a request it had claimed unconditionally.
The environmental-delta, fixed-arrangement tuning, changed-priority, request-handoff,
alternative-route, and bounded-edit distinctions remain consistent with the table.
The two underspecified change prompts remain ties; the mixed-route/transition prompt
remains a combined concern. Batch-3 siblings are routing names, not available authored
skills. No batch-3 body was written to make the comparison appear executable.

## Uncertain claims

These are proposed repository meanings, not standardized definitions. Unverified
context is material to each skill's applicability:

- **Adaptability:** Ask the user which source conditions are authoritative, what
  changed meaning versus representation, which old conditions remain supported,
  and what loss or rejection is accepted. The slot mapping is fictional.
- **Adjustability:** Ask the user for control domain, units, actual application
  event, desired effect, override rules, and acceptable resource trade-offs. The
  numeric caps and memberships are labeled illustrative, not measured tuning results.
- **Agility:** Ask the user who can reprioritize, which commitments and gates stay,
  what calendar and waits count, and what outcome constitutes delivered response.
  No real team's event-to-plan or event-to-delivery duration was measured.
- **Changeability:** Ask the user for the request's actual gates, receiving owners,
  approved behavior, audience, and adoption meaning. The example's switch and
  request states are assumptions, not facts about a deployed workflow.
- **Flexibility:** Ask the user which alternatives are useful, who can choose,
  what results/side effects are shared, and what differences are allowed. Neither
  route independence nor real user eligibility was exercised in a target project.
- **Modifiability:** Ask the user which edit, ownership map, contracts, work units,
  scope/effort limits, and historical-state meanings apply. The ledger shows types
  of work, not measured effort or proof that a production component bound is feasible.

The structural checks and internal rubric review do not replace independent use
of these workflows. Initial question limits, handoff behavior, usefulness of choices,
and end-to-end evidence gathering were not exercised by another agent. The shared
mechanisms and sparse real-project evidence remain human-review concerns. No self-score
table or authoring task instructions are included in this review.

## Validation evidence

- `python scripts/validate_skills.py --only 4,6,8,17,50,68`: six checked, zero errors.
- `python scripts/validate_skills.py`: sixteen checked, 98 absent todo entries, zero errors.
- `python -m unittest discover -s tests -v`: all 19 foundation tests passed.
- `python scripts/build_index.py`: regenerated all 114 entries with only batch-2 draft status changes.
- Maximum word-five-gram body Jaccard involving batch 2: 0.013173652694610778,
  adaptability/additivity, below the unchanged 0.35 threshold.
  That score does not detect paraphrased filler or prove distinct acceptance decisions.
- Skill-creator `quick_validate.py`: all six skills passed.
- `git diff --check`: passed.
- Scope guards: only six batch-2 folders, this review, the six catalogue status
  changes, and regenerated index changed; pilots, batch 1, other batches, shared
  contracts, scripts, tests, and validator threshold were preserved.
- Additional checks passed for illustrative numeric labels and stakeholder
  confirmation, direct existing references, unique quoted triggers, body/reference
  budgets, and eighteen sampled transfer-test entries.
