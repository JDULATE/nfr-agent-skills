# Runtime inference decisions

Start with a question about hidden state, not a target count of logs.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| Queued and blocked work both emit "working". | Emit semantic ownership and wait-phase transitions. Additional lifecycle contracts require maintenance. | Infer each known fixture state from the resulting signals. |
| Retries appear as unrelated requests. | Carry logical work id, fresh attempt id, and parent attempt id. More identities must be stored. | Reconstruct a failed attempt followed by its retry without merging their outcomes. |
| The producer reports done after enqueue. | Separate accepted, claimed, and committed-result events. Dashboards may show a longer incomplete path. | Hold the consumer and verify no committed result is inferred. |
| A queue boundary drops request context. | Propagate minimal correlation metadata and report the receiving owner. Payload changes need compatibility review. | Match send, receive, and current-owner observations for the same attempt. |
| A missing collection interval looks successful. | Produce an ambiguity state when required evidence is unavailable. Some explanations remain unresolved. | Drop a required event and inspect the resulting candidate set. |

## Semantic event sketch

```text
emit(job, attempt, parent_attempt, phase="queued", owner=queue)
emit(job, attempt, parent_attempt, phase="claimed", owner=worker)
emit(job, attempt, parent_attempt, phase="waiting", dependency=archive)
emit(job, attempt, parent_attempt, phase="committed", result=artifact_id)
```

Emit each event at the boundary it names, not as a precomputed expected lifecycle.
A retry has a new attempt id and a link to its predecessor.

## State versus explanation

A waiting event can establish that the worker reports a wait.
It does not, alone, establish why the dependency is unavailable.
Use additional discriminating evidence for that causal question.

If collection may reorder events, declare how identities and ordering are resolved.
Do not subtract clocks or infer ownership from arrival order without that contract.
