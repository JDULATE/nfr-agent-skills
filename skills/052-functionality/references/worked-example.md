# Export capability catalogue

This synthetic service uses illustrative capability and state defaults;
confirm with the user/stakeholder before adopting them.

## Filled catalogue

| Operation | Actor / input | Supported precondition | Required result and effect |
| --- | --- | --- | --- |
| start export | fixture operator, rows=[cedar] | no job exists | Queued(job-cedar); job state queued |
| get status | same operator, job-cedar | job exists | return actual current job state |
| cancel export | same operator, job-cedar | job queued | Cancelled(job-cedar); state cancelled |

Initial state is jobs={}, output=[], worker trace=[].
The actor is supplied as authorized by the fixture; no real authorization mechanism
is established here.
Running-job cancellation is outside the required capability and returns UnsupportedState.
The owner is the export-service maintainer role.

## Before: missing operation

Start creates job-cedar with rows=[cedar], state=queued.
Status returns queued.
Cancel returns UnsupportedOperation because no public handler is wired.
A worker can then start the still-queued job.
The required cancellation capability is absent even though export and status exist.

## Remediation

Wire cancellation through the same service boundary.
Implement its queued-state result and make the sequential worker honor cancelled state.
Do not expand the advertised capability to running-job cancellation.

## After actual operation sequence

Reset jobs={}, output=[], worker trace=[].

```text
start([cedar]):
  result=Queued(job-cedar)
  jobs={job-cedar:{rows:[cedar], state:queued}}
status(job-cedar):
  result=queued
cancel(job-cedar):
  result=Cancelled(job-cedar)
  jobs={job-cedar:{rows:[cedar], state:cancelled}}
consume(job-cedar):
  result=NotRunnable
  output=[]
  worker trace=[]
status(job-cedar):
  result=cancelled
```

The operation is invocable and its declared effect is observable.

## Unsupported-state and placeholder controls

Reset with job-cedar state=running, rows=[cedar].
Cancel returns UnsupportedState(running); state remains running.
No running-job cancellation is claimed.

A placeholder cancel handler returns Cancelled but leaves queued state unchanged.
A following consume returns Started and appends job-cedar to worker trace.
The result/effect check rejects that implementation despite the operation name.

## Limits

The fixture establishes the named sequential capability cases only.
It does not prove concurrency safety, export completion time, recipient task fit,
or business outcome attainment.
