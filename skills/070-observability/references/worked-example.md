# Job-state inference example

This is an illustrative controlled lifecycle, not production telemetry.
All event labels, sequences, and proposed semantics are illustrative examples;
confirm with the user/stakeholder before applying them.

## Filled inference record

| Field | Fixture value |
| --- | --- |
| Logical work | job-elm, required output artifact-elm |
| Initial state | queued, unclaimed, artifact absent |
| First attempt | attempt-ash; parent absent |
| Retry | attempt-birch; parent attempt-ash |
| Queue / owners | queue-fern / worker-ash then worker-birch |
| Dependency | archive adapter, scripted to wait then succeed |
| Candidate states | queued; claimed; waiting on archive; committed |
| Signal order | fixture sequence, not cross-host wall-clock subtraction |
| Collection | all listed events available except in the explicit loss probe |
| Inference output | state, owner when known, logical work and attempt lineage |
| Carry | first failure remains; retry identity and final artifact remain linked |

## Failing evidence before remediation

The collector exposes only:
```text
accepted
retrying
done
```

The producer emitted done after enqueue.
Those strings do not identify a job, owner, result, or waiting phase.
They cannot settle whether the missing artifact reflects queued or blocked work.

## Remediation

Emit state-bearing events from the actual fixture boundaries:
| Sequence | Attempt / parent | Phase | Owner or consequence |
| --- | --- | --- | --- |
| 10 | ash / absent | claimed | worker-ash |
| 11 | ash / absent | waiting | worker-ash, archive blocked |
| 12 | ash / absent | failed | archive unavailable; artifact absent |
| 13 | birch / ash | queued | queue-fern; artifact absent |
| 14 | birch / ash | claimed | worker-birch |
| 15 | birch / ash | waiting | worker-birch, archive blocked |
| 16 | birch / ash | committed | artifact-elm exists |

Every row also contains logical job-elm.
At sequence 11, infer a claimed attempt waiting on archive, not queued work.
At sequence 13, infer the retry is queued and link it to the failed attempt.
At sequence 15, infer the retry has an owner and is waiting.
Only sequence 16 supplies the required committed-output evidence.

These inferences match the hidden state supplied by the constructed fixture.
They describe the recorded boundaries, not an indefinitely current job state.
The instrumentation change does not itself repair archive behavior.

## Failing collection case

Remove sequences 14 and 15.
After sequence 13 and before a later result, the evidence cannot distinguish
a still-queued retry from a claimed retry whose events were lost.
Report that candidate set rather than claiming it is definitely queued.
Remove parent=ash from sequence 13 and retry lineage becomes unverified.

## Requirement example

Collected lifecycle evidence shall distinguish the named fixture states and
connect attempt-birch to attempt-ash under job-elm, while reporting ambiguity
when the ownership events are unavailable.

## Limits

Archive-blocked is a scripted fixture condition, not a diagnosed production cause.
The example validates neither collector reliability nor a particular tracing tool.
It supplies no universal telemetry retention period or observation deadline.
