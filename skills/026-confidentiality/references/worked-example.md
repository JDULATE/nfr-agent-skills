# Cross-team report export

This fictional policy permits `reader-slate` to read report titles in `team-amber`,
but not internal notes. Another team's reports are forbidden to that recipient.
The export operation itself is allowed only for the approved view.

## Inputs, observations, and carried policy

Report `report-mint` has title `daily status` and protected note `SYNTHETIC_NOTE`.
A candidate view emits the title only. The same report can also appear in previews,
cached exports, and error details, which remain separate disclosure paths.

| Path/input | Approved recipient output | State/evidence to retain |
| --- | --- | --- |
| Normal export of report-mint | Title only | No SYNTHETIC_NOTE in emitted/received payload |
| Interface hides note, response still includes it | Forbidden marker reached recipient | Disclosure failure despite display mask |
| Cached export from another scope | No forbidden report contents | Actual cache view and scope policy |
| Export error | Only approved diagnostic fields | No marker in error/log recipient view |
| Narrowed policy with old queued view | Follow confirmed copy policy | Delayed-copy observation, not live-page assumption |

## Proposed disclosure gate

Illustrative example; confirm with the user/stakeholder:
Allow 0 protected-field disclosures in the agreed recipient/channel cases.
Keep an allowed title-only export as a positive control, rather than disabling
all exports and claiming the approved useful view still works.

## Interpretation and unknowns

An operation-level allow decision does not answer which fields may be learned.
If the marker reaches a log destination that cannot be inspected, report the gap;
do not infer absence from the now-redacted normal response.
Previously delivered contents cannot be declared undisclosed by editing the UI.
No real exports, cache retrievals, or recipient observations were executed here.
