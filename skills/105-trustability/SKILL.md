---
name: trustability
description: >-
  Supports scoped trust decisions with evidence and limits when users ask "can this tool publish without my review", "show the limits before I delegate", or "this confidence badge promises too much". Not for operational assurance (see dependability), feelings after use (see likeability), or confidence in one output (see certainty).
---
# Trustability

## Definition and scope

Trustability means a stakeholder's stated trust decision can be supported by
inspectable claims, limits and evidence. Keep that local meaning tied to a
particular decision and authority; distinguish operational failure assurance
(`dependability`), subjective liking (`likeability`) and warranted confidence
in a particular output (`certainty`).

## Use when / Don't use when

- Apply when delegation, reliance or adoption depends on understanding what a
  system's claims actually support and where evidence or authority stops.
- Route a service's combined operational failure case to `dependability`.
- Route a prediction's uncertainty expression to `certainty` or a favorable
  interaction feeling to `likeability`; neither alone establishes justified delegation.

## Workflow

1. Clarify: Read claimed behavior in code, product/docs messages, evidence,
   limitations and the actual stakeholder decision before changing trust presentation.
   If the intended decision or decision owner is unknown, then Ask the user;
   do not optimize for reassurance or higher trust ratings without an evidence context.

2. Specify: Record stakeholder, decision, permitted reliance/delegation, claims,
   evidence scope, material limits, unknowns, fallback and decision authority.
   If the user wants a claim/delegation review, then propose this record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Decision: named stakeholder considering a particular reliance or delegation.
   Claims: supported capability and actual evidence/context/revision, not broad confidence language.
   Limits: known exclusions, counterexamples and unknowns that could change the decision.
   Trial gate: 0 hidden material limitations in the agreed decision-review fixtures.
   Presentation: evidence and limits available at the decision, with unsupported scope explicit.
   Authority: stakeholder confirms whether delegation is granted; a favorable card grants nothing.
   Output: conditional decision support and fallback, not a universal trust or safety verdict.
   ```

   Ask at most three groups about decision/owner and consequence; claims,
   evidence/limits; and materiality, authority, fallback or acceptance criteria.
   Continue to a claim/decision map without inventing supporting evidence.
   If no criterion exists, then offer the illustrative material-limit gate and
   confirm with the user/stakeholder before adopting its decision/model scope.

3. Design/Implement: Read [decision-support practices](./references/design-patterns.md)
   when placing claims, evidence, limits or a delegation boundary.
   If presentation claims more than the evidence supports, then narrow the
   claim and expose the gap instead of adding reassuring badges or stronger wording.
   If a known limit changes the permitted action, then show it at the relevant
   decision and preserve the actual authority boundary rather than burying it elsewhere.

4. Verify: Walk the stated decision using the intended stakeholder's evidence
   view; inspect support, counterexamples, unknowns and actual granted authority.
   If a stakeholder expresses confidence while a material limit is hidden,
   then treat that as unsupported decision support, not a successful trust improvement.

5. Report: Return the decision/claim map, changed presentation or delegation
   checks, evidence limits, stakeholder outcomes and unresolved authority.
   If no stakeholder review occurred, then report the artifact review only;
   do not infer informed reliance, appropriate trust or accepted residual consequences.

## Specification patterns

- **Decision support:** At `{stakeholder_decision}`, expose `{scoped_claims}` with
  `{supporting_evidence_and_material_limits}`, enabling `{confirmed_reliance_boundary}`
  as verified by `{decision_walk_and_unsupported_scope_checks}`.
- **Delegation boundary:** Permit `{delegated_action}` only under
  `{actual_granted_authority_and_claim_conditions}`, with `{fallback_or_open_decision}`
  for unsupported scope, verified by `{limit_counterexample_and_effect_cases}`.

Use the illustrative material-limitation gate if no criterion exists; confirm
with the user/stakeholder. Ask the user which unknowns change the actual decision instead of guessing materiality.

## Rules of thumb

- Don't improve trust by hiding a counterexample; a more favorable response to
  incomplete evidence can worsen the basis for the actual reliance decision.
- Do scope capability claims to the context and revision their evidence supports;
  an unqualified badge can imply permission to rely on untested uses.
- Do place material limits where delegation is decided; a discoverable appendix
  alone may leave the relevant decision using an unsupported promise.
- Don't treat an evidence display as granted authority; an informed stakeholder
  decision and the system's actual permission boundary remain distinct conditions.
- Do keep unknowns different from favorable evidence; confident wording cannot
  convert an untested capability into a supported delegation premise.
- Don't use preference or trust ratings as a substitute for evidence calibration;
  a reassuring presentation can be liked while overstating what may be relied on.

## Verification

Use claim/evidence comparison, stakeholder decision walks and authority/effect
checks. Inspect the actual decision view for relevant limits, scope, evidence
revision, counterexamples and unknowns. Exercise unsupported cases and fallback;
compare actual granted actions with the stated reliance boundary. Record missing
stakeholder review; polished messages or positive ratings alone do not establish justified trust.

## Done checklist

- [ ] Define the stakeholder, decision, consequences and decision authority.
- [ ] Map each capability claim to relevant scoped evidence and revision.
- [ ] Retain material counterexamples, unknowns and unsupported uses explicitly.
- [ ] Inspect the evidence/limit view at the actual reliance or delegation decision.
- [ ] Check actual delegated effects remain within granted authority.
- [ ] Exercise unsupported cases and the agreed fallback or unresolved decision.
- [ ] Separate artifact checks, stakeholder review and authority grants in the report.

## Failure modes

- Raising confidence by removing or hiding material adverse evidence.
- Using an unqualified badge for context-limited capability evidence.
- Burying a decision-changing limitation away from the delegation point.
- Treating an evidence card as permission to perform the action.
- Declaring appropriate trust from positive sentiment or an unobserved stakeholder review.

## References

- Read [decision-support practices](./references/design-patterns.md) when narrowing
  claims, exposing material limits or separating trust support from authority.
- Read [publication-delegation example](./references/worked-example.md) when evidence
  for drafting a report does not establish permission or support for unattended publication.
