# Export acceptance hides completion latency

The fictional export contract requires the completed artifact, not just queue acceptance.
Its response can acknowledge a request before that artifact exists.

## Illustrative latency fixture

Illustrative values and target; confirm with the user/stakeholder:
An eligible set has 100 completed exports: 90 take 100 ms and 10 take 500 ms.
For this example only, define p95 as the sorted sample at rank ceil(0.95 * count).
That rank is 95, giving 500 ms, so it fails the illustrative 300 ms budget.
A 20 ms queue-acceptance response does not replace the completion measurement.

| Checkpoint | Required observation | Carried result state |
| --- | --- | --- |
| Request accepted | Queue receipt | Artifact pending, timing continues |
| Artifact completed | Required content and completion time | Raw eligible result retained |
| Slow export | Retained in full sample | No favorable completed-only subset selected |
| Rejected/unfinished export in another case | Separate outcome and elapsed/censoring evidence | Cannot invent true completion time |

## Statistic counterexample

Illustrative sample calculation; confirm with the user/stakeholder:
If one instance completes 1 export at 500 ms and another completes 99 at 100 ms,
their separate p95 values are 500 and 100 ms. Their unweighted average is 300 ms;
the pooled sample's declared rank rule gives 100 ms. The methods answer different
questions, so apply the confirmed observation-set rule rather than averaging summaries.

## Verification boundary

Trace queue and required completion, generate the declared workload and inspect
space under its actual concurrency/data. Record errors, rejects and unfinished
work even when not part of a finite completed sample; resolve their acceptance
policy before claiming the whole offered-work envelope passed.
No export, timing distribution or memory peak was measured in a real system here.
