# Recipient-selection form example

This fictional task sends a report to a selected approved team. Assume dispatch
happens only after final validation; real cancellation semantics need source evidence.

## Inputs and task result

User intends `team-slate`, chooses `team-amber` by mistake, and leaves the required
subject empty. Report `report-mint` and its body are valid synthetic work.
The candidate shows the chosen team at final review and retains permitted input
when subject validation fails. It does not remove recipient or subject checks.

| Event | Candidate output | Carried state / oracle |
| --- | --- | --- |
| Submit invalid form | Subject error, retained report body and selected team | Nothing dispatched |
| Notice wrong team | Editable review selection | team-amber not silently accepted |
| Correct team and subject | Review shows team-slate and corrected subject | Valid work retained |
| Confirm | Dispatch request for team-slate | Inspect authoritative recipient/result |
| Check outcome | Submitted report for intended team | No report dispatched to team-amber |

## Proposed requirement

Illustrative scenario target; confirm with the user/stakeholder:
Allow 0 unrecovered critical task errors for the agreed recipient-correction
scenarios. Record time, backtracking, errors, help, and lost input separately.
Ask which errors and effort costs govern the real task acceptance rule.

## Rejected shortcuts and evidence

Removing the required subject or recipient check would make the flow shorter
without demonstrating valid task completion. A success toast alone cannot show
which team received the report. If a facilitator points out the wrong team,
keep the resulting completion assisted even when the final result is correct.

If the real system dispatches before review, do not assume changing the visible
selection reverses the earlier effect; inspect the actual correction contract.
No intended-user task trial or real dispatch was performed for this example.
