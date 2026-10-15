# A retry does not erase the failed run

This fictional worker records job results under a required completion contract.
Its documented example profile is serial valid jobs using an unchanged worker.
The trace is an illustrative fixture, not observed production failure data.

## Input, output, and carried exposure

Illustrative timing example; confirm with the user/stakeholder:
Propose a 10-minute continuous trial. At minute 4, job `job-amber` fails its required
result and the worker restarts. The same logical job then succeeds after retry.
The failure ledger preserves original event `failure-slate` and both attempt results.

| Trace checkpoint | Required result / observation | Trial interpretation |
| --- | --- | --- |
| job-mint completes before failure | Result observed | Exercised operation under original trial |
| job-amber violates required result | failure-slate retained | Original continuous trial failed |
| Worker restarts | New lifecycle boundary | Restoration does not delete failure |
| Retry of job-amber succeeds | Retried result observed | Restored completion, not original success |
| Later jobs complete | New exposure retained | A later clean segment, not an uninterrupted combined run |

## Requirement record and ledger decision

Use the operating profile, event unit, and observation contract from the skill.
The agreed unit here is the original operation attempt, so its failure remains.
If the stakeholder instead accepts a complete retried interaction, define that
unit and its result/deadline before classifying the trace; preserve attempt history.

## Defect-oriented implementation and verification

Suppose source inspection reveals a stale per-job handle surviving completion.
A candidate fix closes the handle on the real lifecycle path and adds a focused
check for the violated state. In a real repository this cause must be verified,
not inferred merely because a restart temporarily improves behavior.

Rerun the sustained workload and retain its full trace. Losing observation or
ending early prevents a full clean-interval claim. Even a clean rerun establishes
only its declared profile and interval, not a future production failure probability.
