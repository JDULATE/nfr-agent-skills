# Batch 1 review: Maintainability & Evolvability

Author only ids 5, 14, 42, 43, 44, 46, and 47 from the batch assignment.
The user approved the availability, privacy, and readability pilots before this
batch. Read the authoring guide, complete disambiguation map, standards allowlist,
rubric, and all three pilot entrypoints before authoring. Preserve the approved
pilot files; their approval does not require changing catalogue status in this phase.

Create seven skills and two directly linked reference files per skill. Keep these
new entries at `draft`, regenerate the index, and stop after the batch commit.
Use minimal name/description frontmatter as in the approved privacy pilot;
keep authoring status in the catalogue. Do not edit the template or generator.

## Rubric self-audit

Use the exact criteria in `references/quality-rubric.md`, scored 0-2. Require at
least 17/20 and no zeros. These scores are author judgments, not independent proof.

| Criterion | Additivity | Augmentability | Enhanceability | Evolvability | Expandability | Extendability | Extensibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1. WHAT, WHEN, triggers, Not-for pointer | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 2. Definition and sibling boundaries | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 3. Executable workflow | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 4. Measurable, testable specification patterns | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 5. NFR-specific rules of thumb | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 6. Concrete verification checks | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 7. Objectively checkable done items | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 8. Grounded claims and labeled numeric examples | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 9. Concision, imperative voice, original wording | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 10. Progressive disclosure and reference guidance | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| **Provisional total** | **19/20** | **19/20** | **19/20** | **19/20** | **19/20** | **19/20** | **19/20** |

Withhold full workflow confidence because no independent agent has executed these
fast paths on incomplete requests. Inspection confirms explicit code/docs reading,
conditional steps, complete starting records, and bounded initial questions; it
does not demonstrate actual question-limit adherence or project-specific execution.
No skill scores below 17/20 or contains a zero after revision.

## Distinct acceptance questions and evidence

| Skill | Acceptance question | Worked example and concrete verification |
| --- | --- | --- |
| [Additivity](../skills/005-additivity/SKILL.md) | Does the combination preserve declared baseline-relative contributions under an explicit aggregation rule? | Reconstruct the baseline/increment ledger, expose repeated baseline counting, and challenge overlap and replay identity. |
| [Augmentability](../skills/014-augmentability/SKILL.md) | Does a separately accepted helper attach without replacing the original role? | Display a synthetic support suggestion without changing the original draft; inspect explicit adoption and manual sending with the helper removed. |
| [Enhanceability](../skills/042-enhanceability/SKILL.md) | Can the existing result be refined under its retained criteria and consumer meaning? | Compare concrete date-parser input/reference/baseline/candidate cases; expose a protected-case regression despite another corrected result. |
| [Evolvability](../skills/043-evolvability/SKILL.md) | Can the next named change follow earlier changes with their state and obligations retained? | Carry named invoice records through currency representation, reader retirement, and a later rule change without rewriting historical meaning. |
| [Expandability](../skills/044-expandability/SKILL.md) | Does an admitted resource become usable capacity in the existing installation? | Trace a named export job to an added worker, diagnose a placement-group mismatch, and separate registration from completed work. |
| [Extendability](../skills/046-extendability/SKILL.md) | Can a new core capability fit an agreed ownership and interface change surface? | Add an explicit structured-receipt operation while retaining the text operation; inspect the concrete result shape and downstream fan-out. |
| [Extensibility](../skills/047-extensibility/SKILL.md) | Does an independent implementation fit a pre-existing contract without per-addition core edits? | Register a bracketed formatter for a concrete report model, reject an invalid result type, and inspect host branches and private-state dependencies. |

Each entry contains four natural trigger phrases and valid catalogue exclusions,
the five workflow steps with If/then decisions, three specification patterns,
six focused rules, seven done checks, and four failure modes. Each links directly
to a design-pattern guide and a worked example with Read/when guidance.
References do not chain to further references. No external standard or URL is cited.

## Transferability audit and fixes

Ask whether sampled rules could be moved unchanged into Security or Reliability.
Retain the acceptance-specific decisions, not generic instructions to test or document.

| Skill | Three sampled rule subjects | Why they belong to this acceptance question |
| --- | --- | --- |
| Additivity | Shared baseline; overlapping members; interaction residual | They determine how contributions count and combine, not whether an arbitrary service is secure or failure-free. |
| Augmentability | Helper authority labeling; original-only route; helper-owned projections | They separate the supplementary result and removal boundary from the original capability. |
| Enhanceability | Same result meaning; protected corpus groups; unchanged scoring rule | They distinguish refining an accepted result from changing the task or measurement to manufacture a gain. |
| Evolvability | Retained intermediate state; bridge exit tied to the next scenario; cumulative transition cost | They assess the ordered future path rather than an isolated rollback or successful release. |
| Expandability | Usable versus allocated capacity; admission ceiling; redistribution headroom | They decide whether a resource addition is actually usable, not just whether current work completes. |
| Extendability | New-operation dispatch owner; interface fan-out; resistance to module-count gaming | They bound adding a core capability while exposing the actual changed ownership surface. |
| Extensibility | Independent fixture; registration versus concrete host branch; executable configuration accounting | They establish whether the pre-existing contract truly admits another implementation. |

Tighten five initially transferable rules during self-review: connect evolvability's
bridge exit and irreversible-decision rules to later scenarios; connect partial
capacity admission to owned work and the serving set; connect core change impact
to the new operation's fan-out; and replace a generic plugin-isolation warning
with the distinction between missing host capability and contract conformance.

Make enhanceability explicitly read implementation code as well as docs. Repair
a wrapped placeholder in extensibility's lifecycle pattern. Strengthen six worked
examples with named drafts, concrete parser outcomes, carried record identities,
worker placement labels, a structured receipt object, and a formatter result.
Do not claim these fictional artifacts were discovered in a real application.

## Validation record

- `python scripts/validate_skills.py --only 5,14,42,43,44,46,47`: seven skills checked,
  zero errors, no missing selected files.
- `python scripts/validate_skills.py`: ten skills checked, zero errors, and 104
  absent `todo` entries. Batch bodies are compared against the approved pilots too.
- `python -m unittest discover -s tests -v`: all 19 foundation tests passed.
- `python scripts/build_index.py`: refreshed all 114 entries with this batch's
  seven status changes. Preserve names, aliases, ids, categories, and batch assignments.
- Highest body word-five-gram Jaccard score involving this batch: 0.008767,
  between additivity and extensibility, below 0.35.
- An additional textual check found no repeated long body sentences across the
  seven new skills. This supports originality; it is not a semantic duplicate detector.
- Recomputed the illustrative additivity baseline and residual arithmetic. The
  calculation is a demonstration, not measured application behavior.

| Skill | Body lines | Description characters | Design / example reference lines |
| --- | --- | --- | --- |
| Additivity | 124 | 305 | 47 / 42 |
| Augmentability | 125 | 334 | 51 / 48 |
| Enhanceability | 126 | 350 | 46 / 54 |
| Evolvability | 125 | 334 | 51 / 44 |
| Expandability | 125 | 301 | 51 / 45 |
| Extendability | 126 | 342 | 50 / 52 |
| Extensibility | 127 | 331 | 48 / 47 |

All bodies meet the target length range; every reference is under 150 lines.
Numeric acceptance proposals are labeled illustrative with stakeholder confirmation
in their blocks or adjacent text. Parser digits are fictional input/output examples,
not unlabeled numeric requirements. No tool flags, library versions, clause numbers,
standards characteristic lists, legal obligations, or external statistics are asserted.

## Uncertain claims

These distinctions follow the repository's proposed conventions. They are not
standardized definitions or verified claims about an installed project. The following
applicability questions and scenario assumptions remain less than fully established:

- **Additivity:** Ask the user which aggregation, baseline, units, overlap identity,
  tolerance, and ordering policy apply. Exact-count arithmetic does not establish
  that real gains add or explain residual causes; noise, contention, and drift need
  matched observations. The synthetic increment counts are illustrative only.
- **Augmentability:** Ask the user whether the helper can read, mutate, delay, or
  replace any original behavior. No actual attachment, removal, projection cleanup,
  stale-response behavior, or user adoption was exercised. The support text and
  independent manual route are invented scenario assumptions.
- **Enhanceability:** Ask the user for an unchanged acceptance rule, representative
  corpus, protected groups, and allowable trade-offs. The parser interpretations are
  explicitly fictional, not a universal date grammar. No real quality improvement or
  relative-error target was measured; the corpus and reference answers are unknown.
- **Evolvability:** Ask the user which roadmap scenarios are credible, who can retire
  consumers, and which historical meanings must survive. Invoice representations and
  rule labels are synthetic, not accounting guidance. No sequential migration,
  cumulative effort forecast, or actual reversibility was established.
- **Expandability:** Ask the user for the installation's supported resource unit,
  placement rules, actual controller limits, headroom, and disruption policy. No
  scheduler behavior, capacity delta, throughput curve, or commercial limit was
  verified. The named worker/group mismatch illustrates a possible failure path.
- **Extendability:** Ask the user whether a suitable hook already exists, what owns
  the core responsibility, which consumers must migrate, and how scope is counted.
  Receipt fields and module boundaries are invented; no actual bounded core addition
  or consumer-preservation result was executed. Counts are not universal design limits.
- **Extensibility:** Ask the user which hook predates the request, which host revision
  supports it, and what registration, lifecycle, and authority are allowed. No real
  independent extension was loaded. The formatter model and result type are fictional;
  the unchanged-core target does not establish safety, hot removal, or future compatibility.

## Remaining weaknesses and human review

- No independent agent has tried the new workflows with missing answers, unexpected
  code structure, or a mismatched user meaning. Fast paths and scope routing need
  behavioral confirmation beyond the structural checks and this self-audit.
- Worked examples cover a deliberately narrow case each. They are useful counterexamples
  and requirement records, not empirical evidence that their proposed mechanisms work
  in an arbitrary codebase. Apply the named checks in the target project before claiming success.
- Catalogue-valid sibling pointers may still name skills not yet authored. Do not
  create those skills while running this batch or pretend a routing name is a loadable file.
- Trigger phrases were reviewed for natural wording, but trigger evaluations belong
  to Phase 5. No keyword-overlap scores or automatic routing accuracy are claimed here.
- Ask the user to review the growth-term conventions and the seven drafts. Keep
  these batch entries distinct from the previously approved pilots and do not
  promote anything to `reviewed` as part of this batch.

Commit `phase 4: batch 1 Maintainability & Evolvability`, report, and stop.
