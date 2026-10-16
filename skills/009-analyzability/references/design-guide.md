# Analysis design decisions

Use this guide for system-level explanations and change-impact reasoning.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| A component map omits which fields are consumed. | Add producer/adapter/consumer contract edges. Maintaining the map costs review work. | Follow each field from its producer to actual configured readers. |
| Several causes explain a missing output. | Add a hypothesis ledger with a discriminating check per candidate. Diagnosis may remain open. | Compare predicted outcomes with the retained fixture result. |
| Search finds direct imports but misses a scheduled reader. | Include configured job and generated-consumer references. The analysis boundary expands. | Inspect registration/configuration paths and exercise the named reader contract. |
| An adapter renames the field before downstream use. | Record the transformation on the edge. Extra detail can complicate a simple graph. | Apply the proposed change through the adapter and compare downstream input. |
| A source-backed graph is mistaken for exhaustive runtime coverage. | Mark unknown or dynamically supplied edges separately. The result may be a partial impact list. | Trace each completeness claim to the boundary actually inspected. |

## Contract-edge sketch

```text
publisher -> event.amount
event -> csv_reader.requires(total)
event -> dashboard.requires(amount)
hypothesis schema_mismatch:
  predict csv_missing_total and dashboard_success
hypothesis event_not_delivered:
  predict no_consumer_receipt
```

The sketch is a synthetic graph, not a repository architecture claim.
A candidate that matches the observed result still needs the distinguishing
contract evidence; a plausible story alone does not establish a cause.

## Selecting a repair

Repair the violated contract or introduce a reviewed adapter.
Do not remove a consumer from the map just because its ownership is inconvenient.
If the proposed repair changes another consumer's input, report that new impact.

Keep the analysis deliverable separate from a particular stack trace.
A stack trace may supply evidence, but the deliverable here explains the relevant
boundaries and competing system-level causes.
