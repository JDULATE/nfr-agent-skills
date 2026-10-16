# Acceptance route design

Use this guide when a requirement has no executable, discriminating acceptance route.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| The gate checks only a response code, but the claim concerns dispatch absence. | Add the dispatch consequence to the evidence contract. Obtaining it may require a test seam or authorized artifact access. | Rehearse a successful response with a forbidden dispatch; the gate must fail. |
| A check needs an environment the reviewer cannot access. | Find an authorized equivalent evidence route or keep feasibility open. A simulation may establish only model behavior. | Demonstrate access to each input and label any narrower evidence scope. |
| A metric is named but has no defined unit or population. | Resolve measurement with measurability before choosing the gate. This can postpone a numeric verdict. | Recompute the measure from its agreed observation record before comparing it with a target. |
| A universal claim is supported only by selected examples. | Narrow the acceptance claim with approval or require an appropriate argument. A stronger claim may be expensive or unsupported. | Inspect the claim's quantifiers and the argument scope; do not infer coverage from examples. |
| Missing artifacts silently produce a green result. | Add a separate inconclusive path for absent decisive evidence. More attempts may remain unresolved. | Remove that artifact from a rehearsal and inspect the verdict. |

## Verdict sketch

```text
judge_cancel(evidence):
  if evidence.cancel_receipt is absent:
    return inconclusive
  if evidence.claim_order is absent or evidence.dispatch_log is absent:
    return inconclusive
  if evidence.final_state is absent:
    return inconclusive
  if evidence.cancel_before_claim != true:
    return outside_claim_scope
  if evidence.cancel_result != accepted:
    return fail
  if evidence.final_state != cancelled:
    return fail
  if evidence.dispatched_job_ids contains evidence.job_id:
    return fail
  return pass
```

An empty collected dispatch log differs from a missing dispatch log.
The collection boundary must establish which one is present.

## Acceptance record

Bind claim, condition, method, environment, evidence inputs, decision rule,
reviewer, and scope gaps in the same record.
A method may combine inspection, test, or a formal argument; choosing the method
does not perform all of those activities.

If an input is unavailable, make its owner and consequence visible.
Do not automatically ask for broader production access when a scoped synthetic
rehearsal is enough to establish procedure feasibility.
