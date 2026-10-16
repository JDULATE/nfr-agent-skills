---
name: analyzability
description: >-
  Maps system causes and change impact when tickets say "which layer could explain these failures", "what depends on this schema", or "what breaks if we remove this field". Not for localizing one failing execution (see debuggability) or adding runtime signals (see observability).
---

# Analyzability

## Definition and scope

Analyzability means available structure and evidence let an engineer reason about
causes, dependencies, and change impact. Build an evidence-backed explanation
across relevant boundaries; distinguish localizing one failing execution
(`debuggability`) and adding runtime inference signals (`observability`) from
the analysis those artifacts support.

## Use when / Don't use when

- Apply when a schema change's consumers or a failure's responsible layer are unclear.
- Apply when ownership labels substitute for a dependency or causal explanation.
- Route one captured execution needing expression-level localization to `debuggability`.
- Route absent runtime evidence needed to distinguish states to `observability`.
- Route navigating artifact relationships without interpreting impact to `traceability`.

## Workflow

1. Clarify: Read producer and consumer code, schemas, build configuration, tests,
   architecture notes, and available failure evidence before specifying an analysis.
   Identify the decision: explain a class of failures or assess a concrete change.
   If that decision or boundary is unclear, then Ask the user which outcome the
   analysis must support before treating a component list as an answer.

2. Specify: Record the question, relevant revisions, dependency edges, competing
   explanations, discriminating evidence, and unresolved paths.
   If no analysis criterion is supplied, then propose labeled illustrative defaults:
   map the named change through known consumers and give each causal candidate a
   supporting or contradicting check; confirm with the user/stakeholder.
   Leave unsupported edges and unexamined consumers explicitly open.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [analysis design](./references/design-guide.md) when
   selecting boundary maps, consumer inventories, or hypothesis checks.
   If a schema adapter changes meaning, then model the mapping rather than drawing
   an unqualified edge. If several explanations fit the symptom, then choose a
   check whose outcomes discriminate them before selecting a repair.
   Add focused contract checks or missing dependency documentation as warranted;
   do not rewrite an implementation merely because it appears in the graph.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Follow each reported impact through an actual reference or configured
   interaction. Compare causal candidates with the discriminating fixture.
   If evidence supports only a possible path, then retain it as possible instead
   of calling it the cause. Preserve contradictory results and incomplete checks.
   Read [event-contract example](./references/worked-example.md) when connecting
   a schema failure explanation to a separately bounded change-impact finding.

5. Report: Return the boundary map, candidate verdicts, affected contracts,
   evidence locations, and next discriminating checks.
   If a dependency or causal path remains unexamined, then name that gap rather
   than declaring the change safe or the root cause established.

## Specification patterns

- **Impact:** For `{proposed_change}`, identify `{direct_and_mapped_consumers}`
  within `{repository_boundary}`, with `{contract_effect}` and
  `{grounded_reference_or_unknown}` for every reported path.
- **Cause analysis:** For `{failure_class}`, distinguish `{candidate_explanations}`
  using `{discriminating_checks}`, reporting `{supported_contradicted_open}`
  verdicts under `{evidence_scope}`.

Use the illustrative analysis criterion in Specify when no numeric target exists
and confirm with the user/stakeholder. Do not invent a universal analysis-duration limit.

## Rules of thumb

- Do model actual consumption, not component co-location; sharing a deployment
  does not establish that a component reads the changed field.
- Do propagate meaning through adapters before declaring transitive impact;
  a field rename can be absorbed by a mapping without changing its consumers.
- Do include configured asynchronous and generated readers when their consumption
  is grounded in repository evidence; request routes alone do not bound impact.

## Verification

Use reference search, dependency review, contract fixtures, and controlled
hypothesis checks. Inspect runtime configuration for consumers omitted from static
imports, and check whether adapters preserve or transform the relevant meaning.
Contrast a candidate cause with an observation it cannot explain.
Do not use producer acceptance alone to eliminate a downstream contract explanation.
Keep raw observations, failed checks, exclusions, and revision mismatches in the
analysis record rather than discarding them to fit a preferred explanation.
Label correlation, a reachable dependency, and a demonstrated contract violation
as different strengths of finding.
Separate a source-backed impact list from a claim of exhaustive runtime coverage.

## Done checklist

- [ ] State the cause or impact question and its repository boundary.
- [ ] Ground each reported dependency edge in code or configuration.
- [ ] Track value transformations through relevant adapters.
- [ ] Inspect configured readers outside synchronous request paths.
- [ ] Record a discriminating check for each retained causal candidate.
- [ ] Separate supported findings from possible paths and missing evidence.
- [ ] Tie proposed repairs to the contract the evidence actually implicates.

## Failure modes

- Calling every component in a diagram affected because it shares a deployment.
- Blaming the last service that logged an error without inspecting its input contract.
- Missing a configured, generated, scheduled, or other-language consumer during schema analysis.
- Claiming causality from a graph edge or a timestamp correlation alone.

## References

- Read [analysis design](./references/design-guide.md) when choosing dependency
  boundaries and checks that separate competing explanations.
- Read [event-contract example](./references/worked-example.md) when bounding
  both a causal explanation and the impact of a subsequent schema change.
