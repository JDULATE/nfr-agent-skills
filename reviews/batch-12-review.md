# Batch 12 authoring findings

Eight catalogue entries are now draft: 009 analyzability, 030 controllability,
033 debuggability, 064 manageability, 070 observability, 071 operability,
084 replicability, and 113 visibility. The user confirmed batch-12 review and
commit labels after the copied batch-11 labels were identified. Batch 11's review
is unchanged. No existing file in reviews/ was read.

The authoring guide, disambiguation map, allowlist, rubric, and approved pilot
entrypoints were read before authoring. Descriptions were written and compared
against sibling meanings before bodies. Each has three developer-style trigger
phrases, an explicit boundary, and catalogue-valid sibling pointers. No complete
trigger phrase occurs in another current description after case folding.

## Per-skill findings

### 009 analyzability

The worked graph has only two declared consumers and an explicit adapter. It supports the illustrated delivery-versus-schema distinction and rename impact, not exhaustive discovery of generated, dynamically registered, or external consumers. No production cause or complete repository impact set was established.

The producer-success/downstream-contract safeguard moved to Verification. Failure modes for omitted consumer populations were consolidated rather than kept as separate shape-filling items.

Post-fix transfer test on every retained bullet: 1 specific,
2 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `debuggability`, `modifiability`, `traceability`.
Adapter impact also matters to code changes, but here the deliverable is the mapped contract explanation. Reference coverage helps lineage too; this rule identifies configured consumers relevant to the impact claim.

### 030 controllability

The example assumes one ordered control owner and truthful applied-state feedback. Conflicting intents with the same order, multiple control owners, worker replacement races, and crash persistence are not implemented or proved. A real target needs an ordering/identity contract before this sketch can be used as a protocol.

The rules retain target-state command semantics, a reachable control channel, and supersession. Failed, denied, and unfinished commands remain Verification concerns rather than extra rules.

Post-fix transfer test on every retained bullet: 2 specific,
2 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `manageability`, `operability`, `observability`, `manageability`.
Adoption evidence matters at fleet scale too; the rule's acceptance predicate is one worker's intake state. Revision fences also support administration; this rule prevents a delayed per-worker command from reversing live intent.

### 033 debuggability

The parser example localizes one suffix-selection defect. Its grammar excludes duplicate keys, escaping, and missing-field semantics. Stack/source mapping is an instruction to apply to a real artifact, not evidence that an actual executable was inspected. A suppressed exception would still fail the localization claim.

A parser-specific restatement of the earlier-value capture rule was deleted. Broad parser-correctness limits remain in the report/fixture scope rather than an extra failure-mode item.

Post-fix transfer test on every retained bullet: 2 specific,
1 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `observability`, `analyzability`, `testability`.
Earlier values can help diagnosis too; the rule localizes a specific execution's first divergence.

### 064 manageability

Agent observations and the diagnostics-ended event are truthful fixture inputs. The example does not establish agent attestation, actual administration permissions, distributed convergence, or an exception-expiry deadline. Retirement changes inventory scope; it does not convert an unresolved historical target into a successful adoption.

Message acceptance versus observed adoption moved to Verification. Assignment retirement adds a distinct fleet-lifecycle decision, with an explicit inventory-change probe.

Post-fix transfer test on every retained bullet: 3 specific,
1 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `controllability`, `reconfigurability`, `controllability`, `operability`.
Control targets also need identity; here a replacement must receive a fresh policy assignment rather than inherit a name-based exception.

### 070 observability

The lifecycle states are scripted and the loss probe deliberately removes known events. A real collector's silent loss, reordering, or observation lag can leave more ambiguity than the complete fixture. The text now distinguishes state at a recorded boundary from a current-state guarantee. No archive root cause was diagnosed.

Completion-boundary and missing-collection safeguards live in Verification. The retained rules focus on state discrimination, attempt lineage, and asynchronous ownership evidence.

Post-fix transfer test on every retained bullet: 1 specific,
2 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `visibility`, `traceability`, `analyzability`.
Typed identity supports lineage too; the rule distinguishes retry attempts in runtime inference. System analysis uses ownership evidence, but this rule adds signals at live handoff boundaries.

### 071 operability

The procedure assumes reliable ownership and checkpoint inspection. It does not implement a distributed lease, prove publication atomicity, or establish live-export safety. A fresh operator walkthrough is described but no human operator was recruited. The blocked branch carries state and performs no mutation in the synthetic example.

The transferable state-bearing handoff safeguard moved to Verification. The retained rules cover the complete task's entry/exit, current-state branches, and continuation context.

Post-fix transfer test on every retained bullet: 1 specific,
2 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `controllability`, `manageability`, `recoverability`.
A control needs completion feedback, but this rule accepts the whole operational artifact rather than an applied state. Resume context also aids restoration; here it is the continuation artifact for a runtime operator task.

### 084 replicability

Aster and Bramble are constructed executor roles. No actual independent person or agent reconstructed the procedure. The example demonstrates why a semantic default belongs in the package; portability across real runtimes and independence from actual private resources remain unverified.

The rules focus on independent reconstruction: explicit semantic defaults, newly produced output, removal of author-workspace dependencies, and visible setup assistance.

Post-fix transfer test on every retained bullet: 3 specific,
1 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `repeatability`, `demonstrability`, `portability`, `repeatability`.
Undeclared workspace dependencies matter to migration too; this rule defines whether the attempt is independent.

### 113 visibility

The supplied team-access rule and same-clock freshness arithmetic are fixture assumptions. The freshness budget is explicitly illustrative, not a universal target. Terminal projection selection assumes a declared source revision order. No real customer view, exporter, cross-clock mapping, notification channel, or permission policy was verified.

Unknown-projection and estimate-label safeguards moved to Verification. The retained rules cover subject selection, source observation context, and terminal projection persistence.

Post-fix transfer test on every retained bullet: 1 specific,
2 partly shared, 0 judged transferable.
Nearest siblings in retained-bullet order: `observability`, `communicativeness`, `communicativeness`.
Runtime inference also needs subject identity; this rule accepts what the stakeholder actually sees. Message context can include time too; the rule distinguishes source freshness from page rendering.

All 27 retained rules received a nearest-sibling verdict. Partly shared
judgments remain debatable and are exposed above; zero judged transferable is an
author conclusion, not an independent audit result.

Analyzability, Debuggability, Observability, Operability, and Visibility retain
three rules each after shared or redundant items were moved or deleted. This is
below the guide's usual four-to-six range. The lists were not padded to restore
that range; these count exceptions remain visible for human review. The other
skills retain four rules each. No rule count is presented as a quality score.

## Evidence and depth findings

Every design guide has an observed-evidence/intervention/verification table,
trade-offs, and a short tool-agnostic sketch. The example records fill their
named inputs and carried state, show a failing case and before/after remediation,
and limit conclusions to the constructed fixtures.

| Skill | Description characters | Entrypoint lines | Design guide lines | Worked example lines | Combined lines |
| --- | ---: | ---: | ---: | ---: | ---: |
| `analyzability` | 278 | 116 | 37 | 81 | 234 |
| `controllability` | 301 | 116 | 36 | 69 | 221 |
| `debuggability` | 288 | 116 | 33 | 70 | 219 |
| `manageability` | 307 | 122 | 36 | 72 | 230 |
| `observability` | 303 | 123 | 32 | 77 | 232 |
| `operability` | 301 | 121 | 32 | 75 | 228 |
| `replicability` | 297 | 122 | 35 | 74 | 231 |
| `visibility` | 335 | 122 | 30 | 75 | 227 |

Combined counts include frontmatter, blank lines, and both linked references.
Each reference is below 150 lines, every design guide is below 80, and every
combined footprint lies within the 200-300 guideline. Similar lengths or item
counts do not establish either originality or sufficient depth.

Done checks are tied to different evidence per skill: grounded graph edges and
discriminating candidates; applied intake state and supersession; candidate-value
and source-location captures; inventory assignments and exception lifecycle;
known-state discrimination and loss ambiguity; task artifact and blocked-branch
inspection; independent setup/output records; and subject/freshness/projection
view checks. These are procedure checks, not claims that production evidence was gathered.

## Description routing check

This is the author's manual description check, performed before body authoring.
It is neither an independent evaluation nor an execution of the prepared blinded
routing test. The specific probes have distinct primary matches within the local
cluster conventions. Half the probes omit the distinguishing fact and require
clarification.

| Prompt | Match or clarification result | Boundary / first question |
| --- | --- | --- |
| Map which consumers would break if we remove this event field. | `analyzability` | Change-impact graph, not a particular failing execution. |
| Pause this worker's intake and confirm that no new job starts. | `controllability` | Verified commanded state transition, not a fleet rollout or complete runbook. |
| Replay this parser input and find the expression that selects the wrong value. | `debuggability` | One concrete execution and a localization target. |
| Apply this policy to the selected nodes while retaining one approved node exception. | `manageability` | Fleet assignment, reconciliation, and exception scope. |
| Distinguish a queued job from a claimed job waiting on a dependency. | `observability` | Internal-state inference from evidence, not just a displayed label. |
| Give on-call a complete procedure for resuming this partially exported job. | `operability` | End-to-end operator outcome including partial-state handling. |
| Have a different engineer rebuild the experiment from the supplied package. | `replicability` | Independent reconstruction, not reruns by the original executor. |
| Let the customer see only their export's status and the observation time. | `visibility` | Audience-scoped status exposure with freshness. |
| Make this easier to investigate. | ask; unresolved sibling concerns | Is a specific failing execution available, or do we need system-level causes or new runtime evidence? |
| We need more control. | ask; unresolved sibling concerns | One state transition, a whole operator task, or policy across installations? |
| It works for me. | ask; unresolved sibling concerns | Are we replaying one failure, rerunning the same setup, or reconstructing it elsewhere? |
| Make the workers easier to manage. | ask; unresolved sibling concerns | Fleet membership/policy, a runtime control, or an operator task? |
| Tell us what is going on. | ask; unresolved sibling concerns | Which audience needs visible status, and is internal-state inference also required? |
| Improve the runbook. | ask; unresolved sibling concerns | What operator outcome must it achieve, or is this a support investigation? |
| Can someone else check this? | ask; unresolved sibling concerns | Independent reconstruction, audience demonstration, or acceptance evidence review? |
| Show progress. | ask; unresolved sibling concerns | Who needs which status, where, and is a notification or a diagnostic explanation intended? |

The unresolved prompts expose actual boundaries rather than unconditional winners.
Investigation can mean a captured defect, broader cause/impact analysis, or new
runtime signals. Management can mean fleet policy, an individual control, or a
whole operator task. Progress can mean a visible view, notification, or diagnosis.
Independent reconstruction requires a different executor/setup boundary, not
merely a rerun or another person inspecting an already produced artifact.

Description promises are supported by their examples: the analysis fixture
covers both causal candidates and schema impact; the worker fixture covers pause,
resume, and false acknowledgment; the parser fixture covers a concrete crash
and selected value; fleet settings include local exceptions and unresolved nodes;
runtime signals include waiting and retry lineage; the export task covers partial
and blocked states; reconstruction exposes a hidden default; and the status view
covers subject scope, freshness, missing data, and terminal revision selection.

## Validation findings

- Batch validator: eight checked, zero errors.
- Full validator: 78 authored skills checked, 36 absent todo skills, zero errors.
- Existing test suite: all 34 tests pass. No test or tool file changed.
- Skill-creator quick validation passes all eight entrypoints.
- Read-only assertions check description length, trigger count and uniqueness,
  per-step conditional decisions, and body/reference budgets.
- The maximum word-five-gram body similarity involving this batch is
  0.014877, between `controllability` and `visibility`.
  The validator's 0.35 limit is unchanged. Low literal overlap is not semantic proof.
- Constructed checks cover parser candidate selection, schema adapter values,
  pause/resume supersession, fleet exception assignment, retry parent linkage,
  export content, independent-ledger arithmetic, and scoped/fresh/terminal views.
  These checks do not execute real services or constitute independent reconstruction.
- Catalogue changes are only these eight todo-to-draft transitions. The index was
  regenerated. Previous skills, reviews, tools, tests, and evals are unchanged.

No Phase 5 evals were added. The prepared blinded catalog/key remains the earlier
63-skill snapshot and the blinded test remains unrun. The automatic description
checker does not have complete eval coverage for batches 11-12; this manual
description check is not a replacement for that future coverage.

## Uncertain claims

The repository's term boundaries remain proposed conventions. In particular,
Analyzability versus Debuggability, Controllability versus Operability versus
Manageability, and Visibility versus Observability can overlap in actual requests.
The partly shared rule judgments above require independent review.

Applicability depends on actual consumer registration, source/build correspondence,
control ownership and command ordering, target identity, truthful fleet observations,
exception authority, telemetry coverage, operational checkpoint truth, independent
setup capabilities, supplied access policy, and clock/revision comparability.
No concrete real-world value for any of those was inferred from the synthetic fixtures.

No external standards, legal obligations, invented library versions, tool flags,
or empirical statistics were introduced. Numerical fixture values and the proposed
freshness budget are illustrative and paired with stakeholder confirmation.
The examples provide no production root-cause proof, distributed protocol guarantee,
actual operator outcome, or real independent executor result.
