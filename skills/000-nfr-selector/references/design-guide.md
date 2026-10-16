# Selection decisions

Use the current index and disambiguation map for exact names and boundaries.
Treat every priority not supplied by the user as a proposal.

| Observed evidence | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Several concerns collapse to the same acceptance question | Keep the skill matching that question and explain omitted siblings | Broad labels may still hide distinct concerns | Ask for the missing distinction only if it changes coverage |
| A broad readiness request lacks a task or consequence boundary | Inspect the project and ask the highest-impact missing scope question | Selection remains provisional until the answer | Show assumptions and deferred concerns before any build |
| A downstream decision needs another skill's evidence | Sequence that evidence-producing skill first | The dependency can delay implementation | Identify the actual artifact consumed by the later decision |
| A proposed change may improve one selected quality at another's expense | Retain both acceptance requirements and propose a paired experiment | No universal priority resolves the conflict | Check both conditions under the agreed scenario; report missing evidence |
| An extension adds infrastructure without covering a requested concern | Offer it separately and keep the minimum plan | Future scope may need it later | Trace every implemented component to an agreed acceptance question |

```text
uncovered = stated_acceptance_questions
selected = []
while an uncovered question has an evidenced indexed owner:
    choose that owner using the disambiguation boundary
    record its distinct question and required evidence
    remove the questions it covers from uncovered
report remaining questions as unknown or deferred
order selected owners only by stated priority and evidence dependencies
```

The sketch is a planning aid, not a claim of mathematical set-cover optimality.
An unknown concern is not automatically covered by adding a broad umbrella skill.
For possible performance/security/maintainability conflicts, specify the concrete
mechanism and both acceptance questions before claiming there is a trade-off.
