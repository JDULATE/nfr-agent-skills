# Assignment visibility example

This fictional operation assigns `job-slate` to `team-amber` and adds that job
to the team's membership index. The example contract makes both participating
effects visible together to an authorized coherent observer.

## Concrete before/after state

| State | job-slate owner | team-amber membership | Contract result |
| --- | --- | --- | --- |
| Before | unassigned | job-slate absent | Allowed complete before view |
| After | team-amber | job-slate present | Allowed complete after view |
| Owner changed, membership absent | team-amber | job-slate absent | Forbidden partial committed view |
| Membership present, owner unassigned | unassigned | job-slate present | Forbidden partial committed view |

## Proposed interruption gate

Illustrative example; confirm with the user/stakeholder:
Allow 0 partial participating-effect views in the agreed between-write, abort,
and lost-response scenarios. Confirm the actual observer and visibility rules
rather than inferring atomicity from the table or a transaction label.

## Carried state and negative trace

The faulty path commits the owner, then fails before committing membership.
An observer sees the forbidden subset. A later cleanup resets the owner, but
that does not erase the earlier partial view. A candidate must change the real
commit/publication mechanism; putting both calls in one function is insufficient.

For a candidate using private staged work, interrupt before publication and
inspect that observers still see complete Before. After publication they see
complete After. No actual storage primitive is assumed to provide those outcomes.

## Reader artifact and external boundary

A reader that reads owner before commitment and membership after commitment can
assemble a mixed-time view even if the write unit committed together. Check its
snapshot/version rule separately from stored partial state.
If an external email is added, do not assume the local boundary covers its reader;
exclude it explicitly or obtain and verify the required broader effect contract.
No real commit, observer, or interruption experiment was executed here.
