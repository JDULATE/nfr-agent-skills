# Deferred export feedback

This fictional trace declares event semantics only for the example.

## Inputs and event contract

User `user-slate` requests export `export-amber`. The accepted event means queued;
only a committed ready result means the export is downloadable. Task history is
an assumed candidate feature, not an existing repository capability.

| Input/event | Message output | Carried task state |
| --- | --- | --- |
| Request accepted | Export requested; preparing result | export-amber pending |
| User leaves screen | No assumed visible toast | Pending task retained |
| Ready result committed | Export ready; retrieve result | export-amber completed with result reference |
| Old progress arrives | Must not replace ready message | Completed outcome remains current |
| User returns | History exposes the ready result | Same task and result reference |
| Delivery retry | Same outcome reference | No new export execution |

## Requirement example

Illustrative timing example; confirm with the user/stakeholder:
For a connected initiating user, show the completion message within 5 seconds
of the committed ready event, measured to the agreed rendered-message observation.
Measure the return-to-history case separately when the user was absent.

## Negative trace and verification

Replace ready with a committed failure. The user receives the known failure and
permitted next action, never a download link from a different export. Replay old
progress and inspect that it cannot erase the failure explanation.

If only the outbound transport receipt exists, the result is sent, not proven
rendered or read. If the ready event is absent, retain pending/unknown rather
than inferring completion because a timer elapsed.
These are proposed trace assertions; no real event delivery was measured.
