# Required-capability decisions

Tie each claimed operation to an actor-visible result.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Cancellation is listed but has no handler | Add an invocable service operation and declared result | New public capability needs a maintained contract | Invoke through the same boundary available to the actor |
| Cancel acknowledges but queued work still executes | Implement the supported state transition and have the consumer honor it | Queue/consumer coordination must be explicit | Cancel a queued fixture job, then attempt consumption |
| Operation claims all states but only queued cancellation exists | Restrict or extend the capability contract explicitly | Narrower supported scope or more implementation work | Exercise queued and running cases separately |
| Status calls a helper but the public route is unwired | Connect the actual entrypoint rather than accepting internal helper coverage | Additional service-path work | Run the operation through its shipped invocation path |

## Sequential cancellation sketch

Illustrative pseudocode; no concurrent queue guarantee is implied.

```text
cancel(job):
    if job.state != "queued":
        return UnsupportedState(job.state)
    job.state = "cancelled"
    return Cancelled(job.id)

consume(job):
    if job.state != "queued":
        return NotRunnable
    job.state = "running"
    return Started(job.id)
```

The real implementation needs an established state boundary if claim and cancel
can race. This sketch covers a deliberately sequential capability fixture.

## Presence boundary

An invocable operation with the declared effect establishes the named capability.
It does not establish that the operation is fast, suitable for a particular task,
or effective at achieving a downstream stakeholder goal.
