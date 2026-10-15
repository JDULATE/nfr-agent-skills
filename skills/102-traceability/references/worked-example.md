# Changed approval obligation

This fictional requirement `req-slate` originally permits an editor approval.
A new revision requires the designated reviewer instead. These are supplied
scenario rules, not recommended authorization policy.

## Artifacts and edge state

Decision `decision-amber` explains the change. Function `approve-report` changes
its role check. Historical result `result-mint` covers the editor rule; a newly
created test file has no observed result for the revised obligation yet.

| Edge/input | Correct trace output | Carried verification state |
| --- | --- | --- |
| Old req-slate revision -> result-mint | Historical verifies edge | Old result retained, not current pass |
| decision-amber -> revised req-slate | motivates relationship | Rationale distinct from implementation |
| Revised req-slate -> approve-report revision | implements edge after content review | Actual role decision inspected |
| Revised req-slate -> new test file | Intended verification relationship | Current observed result still missing |
| Function removed later | Reverse impact reaches revised req-slate | Obligation orphan identified |

## Proposed trace gate

Illustrative example; confirm with the user/stakeholder:
Permit 0 unexplained orphan relationships in the agreed forward/reverse fixtures.
Confirm authoritative IDs, revisions and whether an absent edge is an intentional boundary.

## Repository output and interpretation

Create typed revisioned edges, retain historical evidence and mark current
verification pending. A valid path to result-mint cannot prove the new role rule.
A test filename can resolve while no executed relevant result exists. Removing
the function should reveal affected obligations in reverse navigation, not only
produce a broken forward URL. No real requirement, code change or test execution is claimed here.
