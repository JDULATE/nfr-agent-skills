# Cost-fit engineering decisions

Use supplied rates and a fixed workload boundary; do not infer current prices.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| A flat per-request charge dominates the supplied ledger | Batch records only if the provider contract supports equivalent results | Larger failure unit and batching logic | Compare per-record outputs, request counts, and the modeled total |
| Retained intermediate artifacts create priced storage outside required use | Propose an approved retention scope and implement its boundary | Less retained material for other purposes | Inspect required retrieval cases and priced retained quantity |
| A request can exceed the confirmed cost allowance | Add an estimate/admission decision before priced work | Work may queue or refuse under an agreed policy | Exercise over-cap work without disguising it as completed |
| Fixed capacity appears both as a commitment and per-request charge | Separate fixed and incremental ledger entries | Cost attribution becomes explicit | Reconcile the same workload without duplicated commitment cost |

## Ledger sketch

Illustrative pseudocode; every input requires a supplied model.

```text
modeled_total(workload, rates):
    return rates.setup + rates.fixed_period_cost         + workload.priced_request_count * rates.per_request

compare(total, confirmed_cap):
    return "fits-model" if total <= confirmed_cap else "over-cap"
```

This simple formula applies only to the fixture's flat charging rule.
If the real model has tiers, minimums, taxes, or other items, Ask the user for them;
do not assume this formula covers them.

## Preserved scope

Cost admission is not permission to label unperformed work successful.
Keep the required output set beside the ledger and report delayed or refused work.
A provider's batching capability must be verified in the actual repository context.
