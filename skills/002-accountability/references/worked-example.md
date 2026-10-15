# Delegated approval with an unknown outcome

This fictional identity model authenticates principal `user-slate` and permits a
worker `service-amber` to act under recorded delegation `grant-mint`.
It does not establish the real person behind a shared credential.

## Inputs and carried attribution

Operation `approval-coral` targets `report-violet`. A caller-supplied actor field
says `user-other`; it is untrusted and must not replace the authenticated origin.

| Checkpoint | Record/output | Carried state |
| --- | --- | --- |
| Authenticated request | Origin user-slate, claimed actor separate | approval-coral targets report-violet |
| Queued delegation | Origin user-slate; executor service-amber; grant-mint | Validated delegation reference |
| Worker attempt fails | Attempt attributed, completion not claimed | Actual report state inspected |
| Retry completes approval | Same origin with observed executor/result | Retry and final outcome distinct |
| Origin missing in another job | Unknown initiating principal | No guessed human from nearby timestamps |

## Proposed attribution criterion

Illustrative example; confirm with the user/stakeholder:
Permit 0 falsely attributed actions in the agreed delegated, forged-label and
unknown-origin cases. Confirm which principal claims and delegation validity apply.

## Concrete checks and limits

Inspect the request-to-job binding and the final report update. A service-only
record loses the initiating identity; a request-only record cannot establish a
completed approval. Retain the accepted non-secret identity references rather
than a bearer credential. If grant-mint was invalid, preserve that policy result
without silently rewriting the origin or treating the attempted approval as completed.
No actual identity assertion, job execution or human-responsibility conclusion was observed here.
