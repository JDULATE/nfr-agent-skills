# Cleanup of retained operational records

This fictional stakeholder defines irreversible loss of retained operational
records as harm. The example makes no legal claim about retention and supplies
no rule for the user's data. Ask the user which harm and retention policy apply.

## Inputs and causal path

Dataset `set-slate` is eligible for cleanup only when its retention state is
`released`. A stale preview says released; before commitment the state becomes
`held`. Deleting from the preview without checking the current condition is the
unsafe action leading to the named harmful loss.
The stakeholder's example policy forbids deletion when state is held or unknown.
This policy is not a general claim that refusal or delay is always safe.

| Scenario input | Required output under this example policy | Carried state/evidence |
| --- | --- | --- |
| Current state held | No deletion | Retained set-slate remains readable |
| Preview released, current held | No stale-preview deletion | Checked/current revision and actual effect |
| Current state unknown | No deletion; unresolved action visible | Policy decision and unchanged records |
| Current released with valid commitment check | Only the permitted cleanup | Effect bound to checked state |
| Direct command bypasses preview UI | Same constraint at deletion boundary | No alternate route to held-record deletion |

## Requirement proposal

Illustrative scenario gate; confirm with the user/stakeholder:
Permit 0 prohibited deletion actions across the agreed held, changed, unknown,
and bypass scenarios. Ask for any competing harm from delayed cleanup and the
required behavior in that context before adopting this gate or its state policy.

## Control and verification boundary

A candidate connects the state decision to the actual deletion commitment, using
whatever concurrency mechanism the real implementation supports. Merely checking
again earlier still leaves a race if state can change after that check.
Observe actual retained/deleted state and every in-scope entrypoint; a warning
alone cannot establish prevention. Do not run destructive real-data exercises
under this synthetic example or claim an assumed transaction protects the effect.
This is a proposed engineering constraint, not risk acceptance or a safety certification.
