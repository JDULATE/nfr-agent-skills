# Renewing a delivered report service

This synthetic continuation model, horizon, and thresholds are illustrative;
confirm with the user/stakeholder before adopting them.
No market forecast or financial return is inferred.

## Filled continuation record

| Input | Value |
| --- | --- |
| Offering | stock-report service, already delivered before cycle cedar |
| Horizon | renewal reviews for cycles cedar and maple |
| Valued outcome | a recipient accepts a report-backed stock decision |
| Illustrative value gate | at least 2 accepted decisions per cycle; confirm with the user/stakeholder |
| Illustrative upkeep capacity | 3 work slots per cycle; confirm with the user/stakeholder |
| Owner | report-maintainer role, confirmed for the fixture |
| Required output | local report used by stock-review recipients |
| Optional old output | unused legacy layout, no recipient or exit commitment in this fixture |
| Initial enabled outputs | required local report plus legacy layout |
| Renewal authority | product owner; the gate only recommends |
| Decision state | pending review |

## Before: delivered does not mean continuation fits

Cycle cedar evidence contains decisions [decision-a,decision-b,decision-c]
and upkeep=2 slots. Under the filled policy, continuation is supported for cedar.

The initial maple scenario assumes the same valued decisions but upkeep=4 slots,
double cedar's modeled upkeep and above capacity.
That is a scenario, not an observed future result.
Simply pointing to the completed delivery cannot establish maple continuation.

## Remediation proposal

The recurring-work ledger attributes 2 of the scenario's slots to the unused
legacy layout and 2 to the required local report.
Propose disabling the legacy layout after confirming the filled no-recipient
and no-exit-duty assumptions.
Retain the local report and its recipient workflow.

## After modeled cycle evidence

In the revised maple fixture:
enabled outputs=[required local report];
accepted decisions=[decision-d,decision-e];
upkeep=2 slots;
owner=report-maintainer confirmed.

The value and upkeep gates both pass, so the recommendation is
continuation-supported-for-this-cycle.
Decision state remains pending product-owner review, not automatically approved.

All quantities, thresholds, and effort values are illustrative;
confirm with the user/stakeholder.
The fixture supplies these outcomes; it does not prove output removal caused
the recipient decisions or predict actual future use.

## Failing and missing-evidence controls

With enabled output unchanged but accepted decisions=[] and upkeep=0,
the value gate fails even though upkeep is low.
Recommendation=redesign-or-exit-review.

With decisions=[decision-d,decision-e], upkeep=2, and owner unconfirmed,
recommendation=decision-required.
Past delivery and retained source code cannot fill that ownership gap.

## Limits

The example supports only the selected renewal model and supplied evidence.
It does not establish market viability, actual staff effort, funding continuity,
or authority to retire a service with unexamined commitments.
