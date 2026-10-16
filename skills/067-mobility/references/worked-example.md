# Active upload path handoff

This is an illustrative overlapping-path client fixture, not a network protocol guarantee.
All chunk values and proposed continuity rules are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled movement record

| Field | Fixture value |
| --- | --- |
| Moving subject | client-elm changing network path |
| Logical task | upload-fern, active throughout the accepted case |
| Payload | chunks ash=A, birch=B, cedar=C |
| Initial committed prefix | ash only |
| Pending input | birch then cedar |
| Old path / owner | path-old, generation fern |
| New path / owner | path-new, generation moss after readiness |
| Allowed handoff | old/new overlap until declared new-path readiness |
| Completion | one upload-fern artifact with content ABC |
| Forbidden result | a replacement logical upload or user restart |
| Authorization | existing client-elm task permission remains valid in the fixture |
| Time budget | unresolved; no numeric continuity claim |
| Carry | same task, committed prefix, pending chunks, completion identity |

## Before remediation

The client stores task id under its connection object.
Changing to path-new constructs upload-moss from the beginning.
The replacement task may finish, but upload-fern did not preserve its active lifecycle.
The fixture therefore fails the stated mobility contract even with eventual content ABC.

## Remediation and handoff sequence

Keep upload-fern outside path construction and advance only its path owner.
| Step | Logical task | Current path generation | Committed prefix | Activity |
| --- | --- | --- | --- | --- |
| before move | upload-fern | fern | ash | active |
| prepare path-new | upload-fern | fern | ash | active |
| new path ready, assign owner | upload-fern | moss | ash | active |
| send pending birch | upload-fern | moss | ash, birch | active |
| send pending cedar | upload-fern | moss | ash, birch, cedar | completed |

The completed artifact is ABC and belongs to upload-fern.
No suspend/reopen action or replacement task occurred.

## Delayed old-path probe

After generation moss owns the task, deliver an acknowledgment from generation fern.
Its acknowledged chunk is ash, already in the committed prefix.
It must not move the current prefix or create another completion.
The actual current-owner acknowledgments remain the progress authority.

## Unavailable-path probe

Prevent path-new from reaching readiness.
The fixture cannot complete the declared handoff.
Retain task context and report handoff pending/continuity unverified;
do not manufacture new-path success or claim that physical old-path availability
can be guaranteed indefinitely.

## Requirement example and limits

For the declared overlapping-path movement, upload-fern shall preserve its active
identity and committed prefix and finish through the new path without user restart.

This fixture does not prove zero interruption, arbitrary roaming support,
transport-level continuity, or a distributed fencing implementation.
The ordering and readiness mechanism must be established for a real client.
