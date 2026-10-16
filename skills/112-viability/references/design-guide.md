# Continued-value decisions

Use an agreed continuation model, not a generic claim that a product is worthwhile.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| An obsolete report format consumes recurring upkeep without a valued recipient | Propose retiring that format while preserving the required report path | Less output scope and possible recipient migration | Inspect recipient commitments and compare valued outcomes after removal |
| Upkeep assumptions rise beyond the declared renewal capacity | Record an adverse scenario and require a renewal decision or supported redesign | Continuation may remain conditional | Recompute the gate without treating projected work as observed fact |
| A delivered service has no owner for recurring obligations | Assign and confirm ownership before recommending unconditional continuation | Organizational dependency remains explicit | Check the owner record and unresolved duties at renewal |
| A low-maintenance service has no evidence of valued use | Preserve the value-condition failure rather than approving on cost alone | A cheap service can still require redesign or exit review | Evaluate the value gate independently of upkeep |

## Renewal recommendation sketch

Illustrative pseudocode for the supplied stakeholder model.

```text
renewal_recommendation(cycle, policy):
    if cycle.value_evidence_missing or cycle.owner_unconfirmed:
        return "decision-required"
    if cycle.valued_outcomes < policy.minimum_outcomes:
        return "redesign-or-exit-review"
    if cycle.upkeep_slots > policy.capacity_slots:
        return "redesign-or-exit-review"
    return "continuation-supported-for-this-cycle"
```

This returns evidence-based recommendations, not approval to renew or retire.
The actual horizon, outcome value, capacity, and authority require confirmation.

## Change boundary

Removing an unvalued format is only a candidate intervention.
If that format supports a real recipient commitment, its migration or exit duty
must remain in the continuation case rather than vanish from the work ledger.
