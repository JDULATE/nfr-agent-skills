# Constrained-delivery decisions

Keep deliverable scope and hard constraints fixed while comparing candidates.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Rendering depends on an unavailable external service | Probe a permitted local renderer with the actual required template | Local integration and unsupported templates may add work | Render the supplied case with external networking disabled |
| A spike succeeds but only through manual setup | Turn that setup into a declared delivery prerequisite or repository task | Remaining work becomes visible | Reconstruct the probe and inspect the dependency/task ledger |
| Estimated work exceeds available delivery capacity | Propose a constrained alternate implementation or revised scope for approval | Fewer implementation choices or a changed agreement | Reconcile required tasks with supplied capacity and preserved output |
| A successful sample omits the required hard case | Add the blocking case to the probe before selecting the path | More evidence work before commitment | Compare full required output, not the placeholder success flag |
| Required components and capacity exist only in disjoint windows | Reconcile prerequisite availability with the actual delivery window | A candidate may remain blocked despite individually available resources | Supply nonoverlapping windows and inspect the candidate decision |

## Candidate gate sketch

Illustrative pseudocode for an evidence summary.

```text
assess(candidate):
    if candidate.violates_hard_constraint:
        return "blocked"
    if candidate.missing_prerequisite or candidate.blocking_probe_unresolved:
        return "conditional"
    if not candidate.remaining_work_fits_supplied_capacity:
        return "blocked"
    return "supported-under-recorded-assumptions"
```

This is not a scheduling algorithm or authority to commit a delivery date.
The ledger's capacity and availability inputs require stakeholder confirmation.

## Probe boundary

Use the same required template and output contract for local and remote options.
A local renderer that produces only a placeholder is not a feasible substitute.
Expose production integration work separately from the probe.
