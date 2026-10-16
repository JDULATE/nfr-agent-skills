# Notation decisions

Use this table when competing interpretations change the meaning of a requirement.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| "Done" includes both completed and cancelled work in different files. | Introduce distinct terminal labels and an explicit terminal-set definition. Updating references costs review effort. | Interpret completion and cancellation examples without relying on local aliases. |
| A table omits an event but code accepts it. | Declare the missing-cell policy and fill any intended exception. More explicit rows make edits larger. | Read the omitted case under both the prose and table policy. |
| "Before expiry" disagrees at the endpoint. | Define the comparison and clock-event meaning. This exposes a product decision that syntax alone cannot settle. | Evaluate just-before, equal, and after cases using the stated order. |
| A diagram hides the event that causes a transition. | Pair each edge with event, guard, and next-state meanings. The diagram becomes denser. | Reconstruct each allowed transition from the edge record alone. |

## Representation sketch

```text
States = {queued, running, cancelled, completed}
Terminal = {cancelled, completed}
Allowed =
  (queued, claim) -> running
  (queued, cancel) -> cancelled
  (running, finish) -> completed
Unlisted = reject_event_and_keep_state
```

This is a local notation proposal, not a standard language.
Specify separately whether rejected events produce an error, an audit entry,
or another externally visible effect; the transition table alone does not say.

## Precision ladder

Start with explicit vocabulary and conditions if that resolves the disagreement.
Use a table when state/event combinations are the disputed unit.
Introduce a grammar or executable model only if its additional checking resolves
a stated need and the author can explain its semantics.

A machine-readable artifact still needs a defined interpretation.
If the source requirement says both "cancelled is terminal" and "finish may revive
any job", present that conflict rather than encoding a convenient compromise.
