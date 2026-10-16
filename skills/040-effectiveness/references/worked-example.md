# Review completion versus reconciled stock

This synthetic workflow and outcome criteria are illustrative;
confirm with the user/stakeholder before adopting them.

## Filled outcome record

| Input | Value |
| --- | --- |
| Stakeholder goal | resolve discrepancies in count round amber by matching approved counts |
| Eligible tasks | cedar and maple in this fixture round |
| Initial inventory | {cedar:5, maple:3} |
| Approved count record | {cedar:5, maple:4} |
| Correction authority | fixture policy permits applying these approved counts only |
| Old workflow | mark reviewed and close the task without applying corrections |
| Outcome boundary | inventory readback after review and any approved correction |
| Success per item | readback equals that item's approved count |
| Initial review state | cedar=open, maple=open |
| Assistance | none |
| Owner | inventory-reconciliation maintainer role |

All quantities and acceptance cases are illustrative;
confirm with the user/stakeholder.

## Before: the screen reports done

Review both tasks with the old workflow.
Review state becomes cedar=closed, maple=closed.
Inventory remains {cedar:5, maple:3}.
Cedar meets its outcome; maple does not.
A report of both reviews completed would conceal the unresolved stock mismatch.

## Remediation and after state

Require approved correction where the readback differs from the approved count.
Reset inventory and review state to the filled initial values.

```text
cedar:
  reviewed -> already matches approved 5
  readback=5, outcome=achieved, review=closed
maple:
  reviewed -> apply approved 4
  readback=4, outcome=achieved, review=closed
final inventory={cedar:5,maple:4}
```

The modeled correction changes the state that defines the goal.
This does not demonstrate that a real team will use the workflow effectively.

## Pending-effect failing case

Reset maple to 3 and make the correction path acknowledge without applying.
The screen may show correction accepted, but readback remains 3.
Outcome=unachieved; the pending or failed effect cannot be counted as achieved.
Review completion and acknowledgement remain separate observations.

## Missing-authority control

With maple=3 and no approved count record for maple,
return OutcomeUnresolved(approval-required), leaving maple=3.
Do not invent a stock value to make the outcome appear successful.

## Alternative-path boundary

Under a separately accepted fixture path, an authorized manual adjustment sets
maple=4 and readback confirms it.
That achieves the same stock goal, but the report attributes the manual path.
It does not count as evidence of the new correction feature's causal impact.

## Limits

This trace concerns only the supplied count round and assumed approved counts.
It does not establish physical-count accuracy, population success rates,
or causal improvements in staff performance.
