# Batch 1 audit fixes: findings

## Scope and evidence

The audit, findings-only batch review, and authoring-guide changes were committed
first as `9d7646e` (`docs: batch 1 audit`). This follow-up changes only the seven
batch-1 skills and existing references, the authoring guide, and this findings file.
The approved pilots, other batches, catalogue assignments/statuses, index, tests,
and validator code are unchanged. The rejection threshold remains 0.35.

## Description boundaries

- Additivity now requires isolated-versus-combined contribution evidence and
  excludes assembly compatibility and merely adding resources.
- Augmentability now states the separately accepted supporting result and covers
  required as well as optional support; original-role preservation is explicit.
- Enhanceability now names the implementation surface and retained acceptance
  criteria. The future-upgrade trigger is gone. Its description explicitly says
  "Not for judging output error alone (see accuracy)".
- Evolvability now accepts a sequence with prior state and obligations carried
  forward, rather than a generic promise of easier future editing.
- Expandability now names resource admission and usable capacity; the capacity-ceiling
  trigger is gone. Its description says "Not for workload growth curves (see scalability)".
- Extendability now covers building a missing hook as core work and excludes an
  addition that already fits an existing extension contract.
- Extensibility now requires a pre-existing hook that admits the behavior and points
  missing or widened hooks to extendability before claiming independent admission.

Each description has three quoted natural trigger phrases. No complete quoted
trigger phrase is duplicated between these seven descriptions. This is an exact
phrase check, not a claim of semantic separation for every possible prompt.
Descriptions range from 326 to 445 characters and all sibling names are catalogue slugs.

## Disposition of transferable rules

Original bullet numbers refer to the audit's captured version, not the revised order.

| Skill | Flagged original bullets | Findings after revision |
| --- | --- | --- |
| Additivity | 2, 3, 5, 6 | Overlap and replay were combined around a false combined-contribution gain. Metric arithmetic now targets a false preservation equation. Ordering now prevents opposite residuals being hidden by an average. |
| Augmentability | 1, 3, 4, 5 | Independent helper acceptance, promised optional independence, accepted adoption effects, and remaining original-path projection dependence now each state the supplement claim they can falsify. The old unflagged support-panel acceptance bullet was deleted because it duplicated independent helper acceptance. |
| Enhanceability | 3, 4, 5, 6 | Baseline replay and protected cases now run through the replacement surface, exposing offline-only gains or caller repair. The generic public-meaning rule was deleted; its consumer check remains verification evidence. The scoring rule now separates adopting a candidate from changing the meaning of refinement success. |
| Evolvability | 1, 3, 4, 5, 6 | Rules now expose inherited bridge/state obligations, a boundary that fails at the next stage, discarded future options, and costs hidden by a reset ledger. Original bullet 6 was deleted; no substitute was added to restore its count. |
| Expandability | 1, 2, 3, 4 | Rules now require an increased capacity boundary, tie ceilings to a specific admission step, preserve movement headroom until the addition contributes, and expose placement-only success without added capacity. |
| Extendability | 1, 2, 3, 4, 5, 6 | Dispatch, new-operation meaning, transitive fan-out, retained dispatcher behavior, and hook creation are tied to the admitted capability and approved core-change surface. Original bullet 6 was deleted; packaging gaming remains a failure case and guide warning rather than padding the rule list. |
| Extensibility | 1, 3, 4, 5, 6 | Rules now expose private-data dependence, cleanup patches needed per addition, executable per-provider dispatch, and a fixture that only passes on a widened host. The generic undocumented-access rule was deleted; its missing-contract failure is covered by the independent-fixture rule and verification. |

These changes name the failed acceptance claim rather than merely substituting
NFR nouns. Some mechanisms still serve other concerns: a capacity probe can inform
scalability, and an extension cleanup check can reveal a reliability problem.
That overlap is real; the narrower acceptance question does not make mechanisms exclusive.

## Filled reference gaps

- **Additivity:** The existing design guide now specifies repeated matched blocks
  containing baseline, isolated increments, and their combination; run order,
  raw results, per-block residuals, uncertainty method, and a preselected stopping
  rule are retained. Boundary-crossing uncertainty is inconclusive rather than
  an excuse to select favorable repeats. No universal repeat count is invented.
- **Augmentability:** The existing design guide now compares event-triggered writes
  with an approved effect ledger. Adopted draft changes are judged against adopted
  expectations; an unlisted display-triggered send fails original-role preservation.
  Required support no longer implies a promise of optional removal independence.
- **Enhanceability:** The existing parser example now requests a bounded refinement
  surface and inspects the adoption diff separately from parser error. Caller repairs
  outside that surface invalidate a narrow refinement-impact claim. It remains a
  small synthetic example, not measured engineering-effort evidence.
- **Evolvability:** The existing invoice example now includes stage costs, inherited
  bridge upkeep, retirement cost, and cumulative arithmetic. Task identity prevents
  double charging; planned retirement does not erase upkeep before actual exit.
  The person-hour entries are explicitly illustrative and require confirmation.
- **Expandability:** The existing worker example now holds baseline export slots,
  compares the same probe before/after admission, and checks extra work starts
  without eviction before all fixture jobs complete. The probe tests a named
  concurrency boundary, not a scaling curve or proportional-throughput claim.
- **Extendability:** The existing receipt example now has an owner/interface ledger
  for dispatch, renderer, generated schema, old client, and new client. Interface
  coordination and caller work remain visible outside the illustrative core count.
  The old change-surface table was removed because the ledger supersedes it.
- **Extensibility:** The existing formatter example now fails activation after
  acquiring a subscription and output handle, checks cleanup and retained formatter
  behavior, and retries while inspecting duplicate state. The lifecycle is explicitly
  hypothetical and must exist in the original contract for admission to count.

No reference file was added. Added depth stays in directly linked existing files.

## Counts and distinct done evidence

| Skill | Rules | Done items | Failure modes | Done-item evidence in checklist order |
| --- | --- | --- | --- | --- |
| Additivity | 5 | 8 | 5 | Baseline reconstruction; matched fixtures; identity reconciliation; residual arithmetic; supported orders; counterexample; repeated-block uncertainty or exact-count justification; confirmed tolerance decision |
| Augmentability | 5 | 8 | 5 | Helper acceptance; display-only state; adopted effects; obsolete suggestion; optional/required dependency behavior; attachment scope; removal leftovers; original commit/send semantics |
| Enhanceability | 5 | 6 | 5 | Matched replay; adoption impact diff; protected groups; caller meanings; strategy reversal with stored state; unchanged scoring and applicable baseline |
| Evolvability | 5 | 6 | 4 | State carried between stages; intermediate consumer combinations; discarded future information; bridge exit; cumulative cost reconciliation; first unproved stage |
| Expandability | 6 | 8 | 4 | Valid/invalid admission; work placement; before/after boundary; genuine capacity delta; service interruption; headroom; partial-admission ownership; installation limit |
| Extendability | 5 | 7 | 4 | Existing-hook inadequacy; new/rejected operations; old dispatcher cases; branch ownership; complete ledger/diff; consumer migration; approved envelope and exceptions |
| Extensibility | 5 | 8 | 5 | Starting-host fixture; host/configuration diff; nonconformance; failed activation cleanup; retry duplicates; retained extensions; removal state; requested-data/authority coverage |

Counts followed retained evidence and the identified gaps. Several totals still
coincide: five rules recur, and Additivity, Augmentability, and Extensibility
share all three totals. Counts were not varied solely for visual difference. The removed generic/duplicate rules were
not replaced to restore six rules; added checks/failures cover the noisy result,
accepted side effect, refinement impact, boundary probe, and failed activation gaps.
Done items now identify observable comparisons or artifacts rather than just
requiring Clarify, Specify, Design, and Report to have happened. Paired cases in a
single item test the same acceptance distinction; the table exposes those groupings.

## Footprint

The authoring guide now records the 150-250 combined-line guideline as complete
SKILL.md plus directly linked references, including frontmatter and blank lines.
It also states that the lower bound is not a padding target and line counts do
not establish quality. Each reference remains below its separate 150-line limit.

| Skill | Description characters | Body lines | Complete SKILL lines | Design guide | Worked example | Combined lines |
| --- | --- | --- | --- | --- | --- | --- |
| Additivity | 341 | 127 | 136 | 66 | 42 | 244 |
| Augmentability | 428 | 127 | 137 | 65 | 48 | 250 |
| Enhanceability | 444 | 129 | 140 | 46 | 57 | 243 |
| Evolvability | 403 | 123 | 133 | 51 | 63 | 247 |
| Expandability | 326 | 126 | 135 | 51 | 64 | 250 |
| Extendability | 406 | 121 | 131 | 50 | 65 | 246 |
| Extensibility | 445 | 129 | 139 | 48 | 63 | 250 |

## Ten-prompt routing findings

This is a manual semantic test against the revised descriptions, including their
exclusions, with no invented codebase or host contract. It is not a model-router
benchmark, automatic keyword result, or the Phase-5 eval suite. A tie means that
architecture or intent is missing; it is not resolved by counting matching words.

| Prompt | Winning batch-1 skill or tie | Finding |
| --- | --- | --- |
| "make this extensible" | Tie: extensibility / extendability | Existing-hook admission and creation of a missing seam remain different tasks. The bare adjective supplies neither fact. Ask the user whether a usable hook exists, then inspect it. |
| "let people add plugins" | Tie: extensibility / extendability | Existing hook means extensibility; building the plugin facility means extendability. Both descriptions now disclose this condition, so there is no honest unconditional winner. |
| "add a new export format" | Tie: extensibility / extendability | An existing formatter contract may admit it; otherwise core/interface work is required. The format request does not establish which surface exists. |
| "add more workers" | expandability | Resource admission is explicit. Nothing in this prompt requests a workload-response curve. |
| "make this easier to change over time" | evolvability, provisional | The sequence/path description fits best within batch 1. The prompt still lacks actual scenarios; a continuing maintenance-effort request could belong to maintainability outside this batch. Ask the user which successive changes matter. |
| "improve the accuracy of this parser" | No batch-1 skill fits | Enhanceability now excludes judging output error alone. Accuracy is the catalogue destination for error against an agreed reference; no refinement-surface objective is supplied. |
| "let users write their own report templates" | Tie: extensibility / extendability | Existing template registration could admit user implementations; creating that facility is a core addition. The prompt names neither a contract nor a missing seam. Customizability outside this batch may describe the stakeholder goal; no template engine behavior is inferred. |
| "support a new payment provider" | Tie: extensibility / extendability | A provider may fit an existing adapter contract or require new core meaning. The provider's actual contract and current hook capability are unknown. No payment protocol or provider fact is assumed. |
| "our parser gets dates wrong" | No batch-1 skill fits | This reports output error, not the ability to admit refinements. Accuracy is the likely catalogue route; correctness may instead apply if the issue is violating a specified grammar. Ask the user for expected results/reference. |
| "we need to handle ten times the users" | No batch-1 skill fits | This is workload growth, explicitly excluded by expandability. Scalability is the catalogue route. The quoted growth factor is supplied test-prompt text, not an accepted engineering target or a measured result. |

Five prompts remain tied because the supplied words do not reveal hook availability.
The parser prompts no longer select enhanceability solely from parser terminology.
The growth prompt no longer selects resource admission solely from capacity language.
No claim of measured routing accuracy follows from this manual pass.

## Uncertain claims and remaining weaknesses

- Local growth-term conventions remain editorial boundaries, not standardized
  definitions. The Additivity definition now foregrounds isolated-versus-combined
  evidence, but an aggregation rule such as union still needs an agreed meaning
  of preserved contribution. Ask the user rather than assuming arithmetic additivity.
- No actual target codebase, noisy-measurement experiment, worker-capacity probe,
  migration cost log, or plugin lifecycle was executed. The procedures and values
  describe fictional cases; concrete applicability remains unverified.
- The repeated-measurement procedure delegates repetition/stopping and uncertainty
  decisions to the stakeholder. It deliberately does not prescribe an unsupported
  statistical method, so a project may need a more detailed measurement contract.
- The worker probe assumes held export slots can be observed and released. Another
  platform or resource measure needs a different probe and an agreed usable boundary.
- The cost ledger shows inherited upkeep but is not a forecast; the receipt ledger
  exposes owner coordination but does not predict effort from module count.
- Failed-activation cleanup depends on a documented lifecycle promise. Some real
  hosts may require restart or operator cleanup; the example establishes neither
  hot removal nor authority isolation for an arbitrary extension system.
- Shared safeguards remain useful in siblings; explicit failure attribution is
  stronger than word substitution but does not prove NFR-exclusive advice. No
  independent agent executed the workflows or tested the initial question limits.
- The review is findings-only and contains no self-score table. Structural validation
  and an internal rubric assessment are not independent review or pilot-level approval.

## Validation evidence

- `python scripts/validate_skills.py --only 5,14,42,43,44,46,47`: seven checked, zero errors.
- `python scripts/validate_skills.py`: ten checked, 104 absent todo entries, zero errors.
- `python -m unittest discover -s tests -v`: all 19 foundation tests passed.
- `git diff --check`: passed.
- Skill-creator `quick_validate.py`: all seven skills passed.
- Scope guard: only the seven batch-1 folders, authoring-guide budget addition,
  and this findings file changed after the audit commit. Original flagged rule
  sentences no longer survive unchanged in their Rules of thumb sections.
- Body/reference budgets, real sibling pointers, distinct quoted triggers,
  code/docs inspection, per-step If/then decisions, and synthetic JSON shapes passed checks.
- Maximum body word-five-gram Jaccard involving batch 1: 0.008452192287374538,
  Additivity/Extensibility, below the unchanged 0.35 threshold. This does not
  establish semantic originality or eliminate the shared mechanisms noted above.
