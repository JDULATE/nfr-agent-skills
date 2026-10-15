# Learning a saved filter through use

This example defines a synthetic product task, not a measured acquisition result.

## Inputs and states

The synthetic record fixture is fixed for this example:

| Record | Status | Owner |
| --- | --- | --- |
| item-slate | pending | self |
| item-amber | completed | teammate-mint |
The task skill is combining status and owner conditions, then saving the filter.
The candidate product exposes a cue explaining that both conditions must match.
No lesson package or instructor intervention is part of this candidate.

| Attempt | Task input | Help/state carried | Expected output |
| --- | --- | --- | --- |
| Initial | Select pending items owned by self | Prior exposure recorded; no hint yet | item-slate; pending AND self saved |
| Practice | Same decision on synthetic set | Record whether the cue was opened | Correct conjunction, not all pending items |
| Probe | Select completed items owned by a named teammate | Different values; same condition-combination skill | item-amber; completed AND teammate-mint saved |
| Assisted probe | Facilitator supplies the owner condition | Assistance retained | Result may be correct; independence unverified |

## Trial proposal

Illustrative scope; confirm with the user/stakeholder:
Offer 2 practice opportunities before the unaided changed-instance probe. Verify
actual saved predicates and selected rows, not merely the save confirmation.
Ask whether ordinary in-product help remains allowed during the probe.

## Failure and evidence boundary

If the overlay preselects both predicates, the user has not demonstrated choosing
them. Remove the preselection from the probe, while preserving the same task demand.
If the new probe adds an unfamiliar logical operator, it no longer isolates the
original skill; mark that changed demand rather than declaring learning failure.

Retain wrong starts and assistance. An immediate correct probe supports only
that acquisition trial; no claim about next-session retention is available here.
There are no actual newcomer observations in this example.
