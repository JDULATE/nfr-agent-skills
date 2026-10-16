# Cancellation acceptance route example

Treat this as an illustrative sequential queue fixture, not evidence of a real queue.
Its event order and proposed handling are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled acceptance record

| Field | Fixture value |
| --- | --- |
| Requirement / revision | accepted queued cancellation prevents dispatch / cancel-note alder |
| Claim condition | cancellation accepted while queued, before the worker claim |
| Model ordering | one serialized cancel/claim sequence; concurrency excluded |
| Initial state | job-elm queued; cancellation receipt absent; dispatch log collected and empty |
| Input sequence | cancel job-elm; then worker attempts to claim job-elm |
| Expected cancellation | accepted receipt for job-elm |
| Expected state | cancelled |
| Expected consequence | job-elm absent from the collected dispatch log |
| Evidence inputs | cancellation receipt, ordered cancel/claim record, final state, complete fixture dispatch log |
| Method / environment | integration-style acceptance rehearsal / synthetic in-memory queue |
| Reviewer | queue feature owner with read access to the fixture artifacts |
| Missing-input result | inconclusive |
| Out-of-order result | outside claim scope |
| Carried state | cancelled job and receipt remain; dispatch log remains empty in the passing case |
| Excluded claims | live concurrency, production log completeness, response-time deadline |

## Failing gate before remediation

The original gate passes whenever cancel returns accepted.
A constructed defective worker claims even cancelled jobs.

Its artifacts are:
```text
cancel_receipt = accepted(job-elm)
order = cancel accepted before worker claim
final_state = dispatched
dispatch_log = [job-elm]
```

The gate passes despite the forbidden dispatch.
This proves the gate is insufficient for the stated predicate in this fixture;
it is not an observation about this repository's worker code.

## Remediation

Require the accepted receipt, condition evidence, final cancelled state, and
absence from the collected dispatch log. Keep missing collection distinct from
an empty collected log.

| Rehearsal | Receipt | Order | Final state | Dispatch log | Verdict |
| --- | --- | --- | --- | --- | --- |
| defective worker | accepted | cancel before claim | dispatched | [job-elm] | fail |
| corrected worker | accepted | cancel before claim | cancelled | empty, collected | pass |
| collection missing | accepted | cancel before claim | cancelled | absent | inconclusive |
| already claimed | refused | claim before cancel | running | [job-elm] | outside claim scope |

Each row starts from its declared case state: the first three use the initial
queued state above; already-claimed starts with job-elm running and a collected
dispatch log containing job-elm before the cancellation request.

The corrected fixture worker refuses to claim a cancelled job.
That local change supplies the constructed passing artifact; production behavior
is still unverified.

## Requirement example

The acceptance route for queued cancellation shall distinguish forbidden dispatch
from a preserved cancelled state, using the ordered receipt/state/dispatch artifacts,
and return inconclusive when a decisive artifact is missing.

## Limits

The rehearsal establishes a feasible, discriminating evidence route only in the
fixture. It does not prove every queue interleaving, authenticate a production
log, or establish that the real cancellation requirement has passed.
