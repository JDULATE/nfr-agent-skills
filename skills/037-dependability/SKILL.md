---
name: dependability
description: >-
  Builds an evidence-backed basis for relying on a system across stated failure concerns when users say "can we rely on this service for this mission", "review our combined failure assurance", or "show which reliance claims lack evidence". Connects claims, assumptions, evidence, and unresolved counterexamples. Not for uptime alone (see availability), failure-free operation alone (see reliability), or a hazard analysis alone (see safety).
---
# Dependability

## Definition and scope

Dependability means stakeholders have an evidence-backed basis to rely on the
system across their stated failure concerns. Build a scoped argument across those
concerns; keep single-property acceptance with `reliability`, `availability`, or
`safety` rather than replacing their evidence with a general confidence label.

## Use when / Don't use when

- Apply when a reliance decision spans service interruption, incorrect outcomes,
  harmful effects, recovery, or other explicitly selected failure consequences.
- Route only failure-free operation to `reliability` and only usable-time
  accounting to `availability`; do not require an umbrella review for every bug.
- Route a general stakeholder trust decision beyond operational failure concerns
  to `trustability`; enthusiasm or reputation is not failure-assurance evidence.

## Workflow

1. Clarify: Read relevant code, architecture docs, incident records, acceptance
   evidence, and existing failure assumptions before assembling reliance claims.
   If the request names only a single failure property, then bound the work to
   that property instead of inventing a cross-property assurance program.

2. Specify: Record the reliance decision, operating context, unacceptable effects,
   subclaims, assumptions, evidence relevance, counterexamples, and decision owner.
   If the user requests a practical assurance review, then propose this record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Decision/scope: named system use and the stakeholder's stated failure concerns.
   Claim map: required behavior -> failure concern -> subclaim -> relevant evidence.
   Context: actual versions, workload, dependencies, operators, and known assumptions.
   Review trial: 0 unresolved critical counterexamples before recommending reliance.
   Criticality: stakeholder decision; unknown severity is not automatically acceptable.
   Evidence: source, observed result, coverage limits, freshness, and supporting scope.
   Conflicts: retain competing obligations and explicit stakeholder priority decisions.
   Output: supported/unsupported subclaims and a conditional recommendation, not a guarantee.
   ```

   Ask at most three groups about reliance/use and unacceptable effects; existing
   claims/evidence/assumptions; and criticality, trade-offs, and decision authority.
   Continue to an evidence-gap map without asserting that the system is dependable.
   If no decision threshold exists, then propose the illustrative counterexample
   gate and confirm with the user/stakeholder before treating it as binding.

3. Design/Implement: Read [assurance practices](./references/design-patterns.md)
   when linking evidence, finding invalid assumptions, or prioritizing concrete gaps.
   If a subclaim lacks evidence, then identify the smallest relevant code/config,
   test, operational, or documentation change; an argument rewrite alone cannot supply it.
   If one mitigation weakens another reliance condition, then expose the conflict
   and seek its owner decision rather than averaging the subclaims into approval.

4. Verify: Challenge each claim against its evidence, operating scope, shared
   assumptions, known incidents, and the actual implementation revision.
   If a counterexample defeats a critical subclaim, then mark that reliance
   condition unsupported even when other subclaims have favorable results.

5. Report: Deliver the claim/evidence map, tested and untested assumptions,
   concrete changes, counterexamples, residual conditions, and decision owners.
   If the combined claim exceeds the evidence scope, then narrow the recommendation
   or leave it unsupported; never turn local tests into an unconditional reliance guarantee.

## Specification patterns

- **Reliance case:** For `{intended_use_and_context}`, support `{reliance_claim}`
  through `{failure_specific_subclaims}`, each linked to `{relevant_evidence}`,
  `{assumptions_and_limits}`, and `{confirmed_counterexample_decision_rule}`.
- **Mitigation conflict:** For `{change}`, preserve `{nonnegotiable_reliance_conditions}`
  while addressing `{failure_concern}`, verified by `{per_condition_evidence}`
  with `{explicit_unresolved_conflicts_and_owners}`.

Use the illustrative critical-counterexample gate to start a missing decision
rule; confirm with the user/stakeholder. Ask the user to define criticality and acceptance authority.

## Rules of thumb

- Don't average strong uptime evidence with an unsupported harmful-outcome claim;
  compensating scores cannot establish a reliance condition that must independently hold.
- Do attach operating assumptions to every supporting subclaim; a favorable test
  outside the intended use cannot justify the umbrella reliance decision by proximity.
- Do keep contrary incidents beside supporting evidence; deleting a defeating
  case makes the assurance story cleaner without repairing the broken reliance premise.
- Don't count repeated reports of the same experiment as independent assurance;
  shared provenance leaves the same untested assumptions in the combined argument.
- Do compare mitigations across the selected reliance conditions before recommending
  them; disabling a needed function may improve a local failure metric while defeating the mission.

## Verification

Use claim/evidence review, incident challenge, source revision tracing, and
failure-scenario rehearsal categories. Check each artifact actually bears on its
subclaim, including environment, workload, version, and observation limits.
Inspect shared provenance and assumptions before combining results. Retain
counterexamples and conflicting conditions; evidence volume is not evidence coverage.

## Done checklist

- [ ] Bound the reliance claim to the intended use and selected failure concerns.
- [ ] Link every accepted subclaim to relevant evidence and its observation scope.
- [ ] Inspect shared evidence provenance and untested common assumptions.
- [ ] Reconcile contrary incidents with supporting results instead of dropping them.
- [ ] Check mitigations against each independently required reliance condition.
- [ ] Assign owners to unsupported subclaims and unresolved acceptance conflicts.
- [ ] Limit the recommendation to supported conditions and current evidence revisions.

## Failure modes

- Labeling the system dependable because a dashboard reports high uptime.
- Combining unrelated tests into an assurance claim outside their operating scope.
- Hiding a critical counterexample behind an overall favorable score.
- Counting duplicate reports as independent evidence for a shared assumption.
- Rewriting the assurance narrative without fixing or evidencing its failed premise.

## References

- Read [assurance practices](./references/design-patterns.md) when constructing
  a claim map, challenging assumptions, or choosing a concrete evidence-gap repair.
- Read [dispatch reliance example](./references/worked-example.md) when combined
  failure concerns require a conditional decision rather than one aggregate metric.
