# Held worker-loss example

This synthetic model has workers `worker-slate` and `worker-amber` using a shared
store. The scoped injected fault is fail-stop of worker-slate; store failure and
network partition are excluded. Excluding them is not evidence they are tolerated.

## Input and state contract

Operation `op-mint` must create its required business result under stable identity.
A candidate ownership record identifies the currently permitted committing worker.
That ownership check and the effect must enforce the intended contract together;
no actual datastore primitive or atomicity property is assumed here.

| Event | Expected output | Carried state |
| --- | --- | --- |
| op-mint admitted | Result pending, operation identity retained | worker-slate initially owns work |
| worker-slate fails | Alternate path takes eligible work | Failure held during exercise |
| worker-amber handles op-mint | Required business result within agreed deadline | Commit identity and owner checked |
| Replayed op-mint | Same logical result, no duplicate effect | Original identity retained |
| Fault clears | No stale owner commits conflicting result | Return-to-normal state inspected |

## Requirement proposal

Illustrative fault scope; confirm with the user/stakeholder:
Inject 1 fail-stop worker fault while the stated alternate path and store remain
available. Preserve the confirmed required result and state rules during the held
fault; ask for the deadline, exposure duration, and accepted degraded behavior.

## Negative controls

If service stops until the failed worker restarts, record interruption/restoration,
not successful continued service. If all work depends on the failed worker's local
state, the alternate path premise is false even though another process is healthy.

A delayed old-worker commit is a separate handoff exercise, not a claim that the
fail-stop model resumes execution while stopped. Test it by changing the model
explicitly to delayed/overlapping ownership, then disclose that extra scope.
These traces are design assertions; no fault injection was performed on a real service.
