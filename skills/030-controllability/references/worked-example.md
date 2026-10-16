# Worker pause and resume example

This is an illustrative ordered-worker fixture, not a production command protocol.
All values and proposed policies are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled control record

| Field | Fixture value |
| --- | --- |
| Actor | synthetic operator-elm, authorized for worker-ash only |
| Target | worker-ash incarnation moss |
| Other target | worker-birch, running throughout |
| Initial intake / active / queued | running / job-active / job-next |
| Active-work policy | finish current job; do not abort |
| Control path | separate ordered control reader |
| Pause intent | command-pause, order 7, target paused |
| Resume intent | command-resume, order 8, target running |
| Applied feedback | target incarnation, command id, order, intake state |
| Unknown rule | no applied feedback means transition unconfirmed |
| Carried state | active job completes; queued job starts only after resume |

## Failing behavior before remediation

The handler acknowledges command-pause but stores only a command receipt.
The work loop does not read a desired-intake gate:
```text
receipt = accepted(command-pause)
applied_feedback = absent
next_claim = job-next
worker_intake = running
```

Calling that result "paused" is false for this constructed fixture.
The acceptance receipt establishes only that intent arrived.

## Remediation and after sequence

Make the control reader apply an absolute intake state before publishing feedback.
| Step | Applied feedback | Intake | Work observation |
| --- | --- | --- | --- |
| command-pause | order 7, paused | paused | job-active continues; job-next unclaimed |
| duplicate command-pause | order 7, paused | paused | no new claim |
| active job finishes | order 7, paused | paused | active empty; job-next still queued |
| command-resume | order 8, running | running | job-next may now be claimed |

Worker-birch remains running and receives no command in this sequence.
The same command reader remains reachable during pause.

## Supersession failure probe

Apply command-pause-later at order 9, then deliver a delayed resume at order 8.
The old resume returns superseded and intake remains paused.
Without the ordering fence, the delayed command could undo the newer intent.

## Missing-feedback probe

Accept command-pause but suppress its applied feedback.
The operator-facing result is unconfirmed, even if inspection later finds intake paused.
Do not infer the outcome from receipt or automatically issue a reversing toggle.

## Requirement example and limits

The control shall pause new claims on worker-ash while preserving its active job,
and allow explicit resumption through a reachable control path, with applied-state
feedback and rejection of superseded intent.

This fixture assumes ordered state ownership. It does not establish distributed
command ordering, a completion deadline, or authority for any real operator.
