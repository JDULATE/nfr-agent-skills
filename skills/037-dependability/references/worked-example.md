# Dispatch reliance example

This hypothetical mission is dispatching synthetic work orders. The stakeholder
requires usable dispatch, correct order ownership, and prevention of a specified
harmful duplicate dispatch. These are example conditions, not universal obligations.

## Inputs and claim state

Work order `order-slate` belongs to `team-amber`. Existing evidence is a normal
journey trace and a scenario in which repeated submission creates duplicate work.
A retry patch is proposed, but its actual duplicate-effect semantics are unknown.

| Subclaim | Available input evidence | Current output | Carried condition |
| --- | --- | --- | --- |
| Ordinary dispatch usable | Normal journey completes | Supported only for observed context | Revision/workload limits retained |
| Ownership preserved | No ownership assertion in trace | Unsupported | Need actual owner/result check |
| Harmful duplicate prevented | Repeated submission duplicates work | Counterexample retained | No positive umbrella recommendation |

## Proposed decision gate

Illustrative example; confirm with the user/stakeholder:
Recommend reliance only with 0 unresolved critical counterexamples in the agreed
scope, with criticality and all required subclaims confirmed by the decision owner.
The normal journey does not compensate for a defeated harmful-duplicate condition.

## Concrete repair and interpretation

Inspect the submission identity and commit path. A candidate may enforce stable
operation identity and verify repeated submissions against the actual result.
That becomes new supporting evidence only after the changed path is exercised.
Add an ownership assertion instead of inventing ownership support from the same
normal response. Reusing that response in another report adds no new coverage.

If the candidate simply blocks all dispatch, inspect the mission condition too:
it may prevent duplicates while defeating usable dispatch. Record the conflict;
do not approve the combined claim from the improved duplicate metric alone.
No real dispatch code, reliance decision, or experiment was evaluated here.
