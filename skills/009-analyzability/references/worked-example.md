# Event-contract analysis example

This is an illustrative synthetic graph and fixture, not a repository observation.
All values and proposed contracts are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled analysis record

| Field | Fixture value |
| --- | --- |
| Question | Explain absent CSV output and assess renaming the amount field. |
| Producer revision | publisher-fern emits event-elm with amount=7 |
| Event delivery | event-elm delivered to both configured consumers |
| CSV contract / state | requires total; no output row initially |
| Dashboard contract / state | requires amount; no tile initially |
| Adapter | none |
| Configured consumers | csv-reader and dashboard-reader only in this fixture |
| Candidate explanations | missing delivery; consumer schema mismatch |
| Evidence | consumer receipts, required-field checks, output stores |
| Carry after execution | retained receipts, CSV refusal, dashboard tile |
| Excluded boundary | unknown consumers or runtime configuration outside this graph |

## Before analysis

The initial report says "the queue is broken" because CSV output is absent.
It contains no input contracts or delivery evidence.

The fixture supplies:
```text
csv_receipt = event-elm
csv_required_field = total
csv_result = missing_total
csv_rows = empty
dashboard_receipt = event-elm
dashboard_result = accepted amount 7
dashboard_tile = 7
```

Missing delivery predicts absent receipts, which contradicts this fixture.
Schema mismatch predicts a CSV refusal alongside dashboard success, matching
both the payload and the required-field check.

## Remediation of the analysis gap

Add contract edges and the hypothesis ledger.
For the discriminating contract check, supply CSV with
event-elm-compatible = {total: 7}; it produces a row containing 7.
No other fixture input changes.

This supports a missing-total input-contract explanation in the synthetic graph.
It does not establish a queue failure, a production defect, or a universal cause.

## Change-impact branch

Now propose replacing amount with value.
The current publisher output is {amount: 7}; dashboard consumes amount directly.
An unchanged dashboard rejects {value: 7} as missing_amount.
CSV already requires total and is not repaired by that rename.

Introduce an explicit adapter producing:
```text
dashboard_input = {amount: source.value}
csv_input = {total: source.value}
```

With source {value: 7}, both readers accept and store 7.
The mapped impact differs from blindly renaming every consumer reference.

## Requirement example

For the amount-to-value proposal, the analysis shall identify both configured
consumers, their required fields, and the adapter-dependent effects, while
classifying delivery and schema explanations against the recorded evidence.

## After finding and limits

The completed record replaces an unsupported queue diagnosis with a bounded
contract explanation and an actionable impact map.
Only the declared consumers and mappings were checked.
No claim of exhaustive discovery, production causality, or expression-level
defect localization follows from this constructed fixture.
