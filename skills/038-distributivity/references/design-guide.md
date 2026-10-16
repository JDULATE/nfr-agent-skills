# Placement decisions

Choose the authority boundary before selecting a balancing policy.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Router moves a shard but an old worker still writes | Check owner and assignment revision at every authoritative effect | Authority lookup or enforced token validation enters the write path | Send old and current tokens after reassignment; inspect committed effects |
| Target activates with incomplete copied state | Add quiesce, copy/check, and activation stages with a visible paused state | Movement may suspend effects for that unit | Interrupt each stage and compare source checkpoint with target state |
| Balanced counts place a restricted shard on the wrong node | Filter by explicit eligibility before selecting a destination | Some eligible nodes may carry uneven counts | Enumerate allowed placements and reject an ineligible candidate |
| Replicas execute effects as though they own the shard | Separate data-copy role from active effect-owner role | More role metadata and promotion work | Attempt a mutation from a replica holding current data |

## Centralized authority sketch

Illustrative pseudocode for a checked store, not a distributed consensus algorithm.

```text
apply_effect(shard, node, revision, effect):
    in same serialized authority-and-effect operation:
        a = assignment[shard]
        if a.stage != "active":
            return "paused"
        if (a.owner, a.revision) != (node, revision):
            return "stale-owner"
        commit(effect)
        return "applied"
```

The authority check and effect must not have a gap allowing reassignment
between validation and commit. Inspect how the repository enforces this property.
If different stores cannot establish that boundary, then surface the missing
mechanism instead of treating this sketch as an implementation guarantee.

## Handoff gates

Quiesce source effects before choosing the state checkpoint.
Verify the copied checkpoint before publishing the target as active.
On a failed copy, keep the declared paused or old-owner policy explicit.
Do not infer automatic rollback from the existence of an old data copy.
