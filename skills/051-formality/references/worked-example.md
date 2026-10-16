# Cancellation notation example

Treat this as an illustrative specification fixture.
Its symbols and case values are example inputs, not product policy.
Confirm the proposed interpretation with the user/stakeholder.

## Source ambiguity

The source sentence says: "A job may be cancelled before completion."
A diagram shows queued -> cancelled and running -> completed.
Neither artifact says what a finish event means after cancellation.

Reader Amber interprets cancelled + finish as completed.
Reader Birch interprets cancelled + finish as rejected with state unchanged.
These are constructed conflicting readings, not measured reader-study results.

## Filled interpretation record

| Field | Example value |
| --- | --- |
| Artifact | synthetic job lifecycle note, revision cedar |
| Meaning of queued | accepted and not yet claimed |
| Meaning of running | claimed for execution |
| Meaning of cancelled | terminal cancellation outcome |
| Meaning of completed | terminal successful execution outcome |
| State domain | queued, running, cancelled, completed |
| Event domain | claim, cancel, finish |
| Initial state for disputed case | cancelled |
| Input event for disputed case | finish |
| Proposed omitted-case meaning | reject event and leave state unchanged |
| External rejection effects | event result rejected; no other effect specified |
| Reader context | source note plus the interpretation table below |
| Carried state after rejection | cancelled |
| Acceptance evidence | identical allowed-transition readings for the listed cases |

The terminal set is cancelled and completed.
No transition out of either terminal label is listed.

## Before result

Without an omitted-case rule, the disputed input has no unique interpretation.
The defect established here is in the specification's meaning, not an observed
late-completion defect in an implementation.

## Remediation

Adopt the following proposed local interpretation:
```text
queued + claim = running, accepted
queued + cancel = cancelled, accepted
running + finish = completed, accepted
any other state/event pair = same state, rejected
```

Now read the complete case set:
| Initial state | Event | Next state | Event result |
| --- | --- | --- | --- |
| queued | claim | running | accepted |
| queued | cancel | cancelled | accepted |
| running | finish | completed | accepted |
| cancelled | finish | cancelled | rejected |
| completed | cancel | completed | rejected |
| running | cancel | running | rejected |

The last row exposes another policy decision: running cancellation is not allowed
by this proposed table. If the stakeholder intends it, change the table and its
examples together instead of treating the missing row as implicit permission.

## Requirement example

The job-lifecycle specification shall define every state/event pair using the
listed transitions and the reject-and-preserve omitted-case policy, with the
case record yielding the unique next state and event result above.

## After finding and limits

The notation resolves the conflicting readings for the stated domains.
It does not prove that deployed workers obey the table, cover concurrency, or
decide whether running cancellation should be supported.
Resolve those needs separately without calling syntax validation a product proof.
