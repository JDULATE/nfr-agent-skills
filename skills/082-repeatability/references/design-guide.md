# Rerun design decisions

Use this guide for the same executor and held setup, not independent reconstruction.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| A fixture loader restores rows but leaves a consumed counter behind. | Include the counter in per-run initialization if the run contract requires reset. This does not test continuous production use. | Compare the manifest's initial counter and resulting identifier for every rerun. |
| Background work from one run changes the next run. | Give each run an isolated state namespace or wait for the defined quiescence point. Isolation may hide intended shared-state behavior. | Inspect remaining work at the next run boundary and reject undeclared carry. |
| A time or random input changes a supposedly fixed procedure. | Supply explicit clock/random inputs through supported test seams. A fixed sequence covers only that sequence. | Record the supplied values and verify the same input sequence reaches each rerun. |
| Result order varies but the requirement compares content. | Declare an order-insensitive comparison preserving duplicate counts. This cannot validate an ordering requirement. | Reorder equivalent outputs and introduce a missing duplicate; only the first comparison should pass. |
| Real carry is erased just to obtain equal output. | Compare the required relationship between successive states instead of demanding identical snapshots. The result may be a transition relation rather than byte equality. | Check the carry value and expected next result for each invocation. |

## Same-setup sketch

```text
for label in planned_run_labels:
  restore_fixture_state(rows=invoice_fixture, next_id=40)
  start = inspect_run_state()
  result = execute_invoice(quantity=3, unit_price=10)
  record(label, start, result)
compare_required_fields(all_recorded_runs)
```

The quantities above are illustrative fixture values, not system targets;
confirm with the user/stakeholder before adopting this example's reset contract.
The procedure must inspect that restoration actually occurred.

## Comparison choices

Exact comparison is appropriate only for fields the contract fixes.
A tolerance needs a stated unit and stakeholder-confirmed meaning.
Ignoring order needs a content and multiplicity rule.

Keep the first differing run in the evidence.
Do not automatically widen tolerance until the collected outputs fit.
If intended state carries, publish that state transition as part of the procedure
instead of calling unequal outputs a repeatability failure by definition.
