# Malformed import and retained reservations

This synthetic import path accepts a list of records. The example contract rejects
malformed structure without business writes and must preserve unrelated valid work.
Actual size/depth limits and cleanup ownership must come from the target project.

## Inputs and candidate behavior

Bad input `bad-slate` contains a truncated nested record after an otherwise valid
prefix. Valid control `good-amber` has a complete record with its required fields.
The candidate validates bounded structure before mutation and releases its task
reservation when rejecting; its actual mechanism must be verified in source.

| Event | Response/output | Carried state to inspect |
| --- | --- | --- |
| Submit bad-slate | Declared malformed-input rejection | No prefix business row committed |
| Error path finishes | No abandoned import still running | Reservation released or visibly reconciled |
| Submit good-amber during exposure | Correct accepted result | Unrelated work and state preserved |
| Repeat bad-slate | Same bounded rejection contract | No accumulating reservations or background tasks |
| Exposure ends | Normal valid work continues | Resource/work state compared with baseline |

## Proposed response requirement

Illustrative timing example; confirm with the user/stakeholder:
Reject bad-slate within 2 seconds from admission, with no forbidden mutation or
orphaned work. Ask for permitted resource peaks, structural limits, valid-work
criteria, and repeated-exposure scope before claiming a complete bound.

## Counterexample and interpretation

If the response returns promptly while a queued expansion continues, the response
check passes but the controlled-work claim fails. If the prefix record was already
committed, an error response does not satisfy this example's no-mutation contract.

If good-amber cannot complete during bad-input exposure, record the unaffected-work
failure even when the process stays alive. No actual parser run, resource result,
or attack-resistance claim is supplied by this example.
