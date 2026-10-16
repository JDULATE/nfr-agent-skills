# Outcome-attainment decisions

Start with the stakeholder's goal rather than an available activity counter.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Review completion leaves an approved stock discrepancy unchanged | Add a confirmed correction step before outcome completion | More work and explicit correction authority | Compare inventory readback with the approved count result |
| A request acknowledgement is recorded as final success | Carry a pending outcome until downstream evidence arrives | Completion reporting may stay unresolved | Delay the effect and inspect the outcome report |
| Queue removal improves the apparent success count | Keep unresolved items visible under the original evaluation boundary | Less favorable but meaningful reporting | Remove a queue item without changing stock and inspect the outcome result |
| An accepted manual path reaches the same goal | Include it as an attributed alternative path under the evaluation policy | Results cannot be attributed solely to the new feature | Compare final evidence and label the actual path used |

## Completion sketch

Illustrative pseudocode for a confirmed reconciliation policy.

```text
finish_reconciliation(item, approved_count):
    if not correction_is_authorized(item, approved_count):
        return OutcomeUnresolved("approval-required")
    apply_approved_count(item, approved_count)
    observed = read_back_inventory(item)
    return "achieved" if observed == approved_count else "unachieved"
```

The approval source and allowed correction need stakeholder confirmation.
The sketch does not grant authority or establish correctness of the supplied count.

## Outcome versus cause

A filled fixture can show that a declared state matches a goal after the modeled
operation. It does not establish that interface changes improve staff behavior
or outcomes across a real operating population.
