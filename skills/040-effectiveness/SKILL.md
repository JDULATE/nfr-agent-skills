---
name: effectiveness
description: >-
  Checks attained outcomes when asked "count resolved issues", "verify stock was reconciled", or "stop counting clicks as success". Ask the user if outcomes vs task fit is unclear. Not for capability presence (see functionality) or task fit alone (see suitability).
---

# Effectiveness

## Definition and scope

Effectiveness means use of the system achieves the stakeholder's intended
outcome in the stated context. Establish the final outcome independently of
feature use, button clicks, or a completed workflow label.
Separate attained outcomes from capability presence (`functionality`) and
fit of available capabilities to a particular task (`suitability`).

## Use when / Don't use when

- Apply when the product reports completion but the intended reconciliation,
  correction, or other stakeholder result remains unachieved.
- Define whose outcome matters and what evidence establishes it.
- Route a missing operation to `functionality`.
- Route a mismatch between available capability and task constraints to
  `suitability`.
- Route reading effort or interaction obstacles to `usability` when the
  question is task interaction rather than the achieved stakeholder outcome.

## Workflow

1. Clarify: Read the relevant workflow, downstream state changes, outcome docs,
   operational evidence, and stakeholder decisions before specifying success.
   Trace what happens after the interface reports done.
   If the intended result is missing or disputed, then Ask the user what final
   state establishes success and which constraints must remain true.

2. Specify: Record outcome, population/context, eligible attempts, success evidence,
   observation boundary, accepted assistance, and owner.
   If no target exists, then propose a labeled illustrative default:
   report achieved and unachieved outcomes for the declared fixture tasks without
   inferring a wider success rate; confirm with the user/stakeholder.
   Ask at most three questions about the goal, evaluation context, and constraints
   before proposing a workflow change.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [outcome decisions](./references/design-guide.md)
   when connecting a completion signal to the required downstream result.
   If the current workflow stops at review but the goal requires an approved
   correction, then add or expose that correction path under the confirmed policy.
   If success can increase by weakening the goal, then preserve the original
   outcome definition and report the trade-off rather than relabeling success.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Follow eligible attempts to the actual outcome boundary, recording
   initial state, assistance, failure, and unresolved cases.
   Keep the denominator, exclusions, and observation conditions declared in advance.
   If only engagement or completion events were observed, then leave outcome
   attainment unverified instead of equating those proxies with effectiveness.

5. Report: Return outcome definitions, changes, per-attempt results, remaining
   unresolved work, and limits of attribution.
   If a synthetic trace is the only evidence, then describe its modeled result
   without claiming that a real population's outcomes improved.

## Specification patterns

- **Outcome attainment:** For `{stakeholder_tasks_and_context}`, use of
  `{workflow}` shall yield `{defined_final_outcome}` under
  `{preserved_constraints}`, verified by `{downstream_state_or_recipient_evidence}`.
- **Evaluation:** `{outcome_report}` shall distinguish
  `{achieved_unachieved_and_unobserved_attempts}` using `{predeclared_rules}`
  without treating `{feature_activity_proxy}` as the outcome.

Use the illustrative fixture-outcome proposal in Specify when no numeric target
is given; confirm with the user/stakeholder before accepting any wider criterion.

## Rules of thumb

- Keep stakeholder success separate from feature completion; a reviewed mismatch
  is not reconciled stock merely because the review screen closes.
- Allow an agreed alternative path to count when it achieves the same outcome;
  requiring use of a particular button measures adoption instead of the goal.
- Reject an outcome shortcut that merely hides unresolved work; deleting a
  discrepancy from the queue does not establish that its stock was corrected.

## Verification

Use outcome-state inspection, recipient confirmation, and task-observation categories.
Retain every eligible attempt, including failures and missing downstream evidence.
Record assistance and alternative paths under the approved evaluation rules.
Check that success evidence refers to the stakeholder's result, not an internal
activity counter. Compare initial and final state for the named task.
Confirm all required downstream effects; an accepted correction request alone
does not establish the final stock outcome.
Separate observed change from causal attribution; a before/after fixture cannot
establish population impact, adoption, or a general intervention effect.
Do not discard difficult attempts after seeing their outcomes.

## Done checklist

- [ ] Define the stakeholder's final outcome and preserved constraints.
- [ ] Bound the task population, attempts, and observation window.
- [ ] Identify downstream evidence that establishes attainment.
- [ ] Trace attempts beyond the interface completion event.
- [ ] Record achieved, unachieved, and unobserved results separately.
- [ ] Check accepted assistance and alternative paths.
- [ ] Report attribution limits and unresolved outcome evidence.

## Failure modes

- Counting a clicked completion control as the stakeholder's achieved result.
- Improving a success rate by removing unresolved work from the evaluation.
- Hiding a discrepancy rather than producing the required corrected state.
- Claiming real-world improvement from a synthetic workflow trace.

## References

- Read [outcome decisions](./references/design-guide.md) when selecting
  downstream success evidence and an outcome-producing change.
- Read [reconciliation example](./references/worked-example.md) when separating
  reviewed work from the final inventory result.
