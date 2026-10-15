# Worked example: approved and deployed, but not adopted

Suppose a fictional support tool has an approved request `reply-preview` that adds
an editable preview before sending. The released revision includes the preview,
but its audience switch still excludes the target support team.

Read the request, its accepting decision, implementation/release path, switch
configuration, and the target team's documented journey. Do not assume adoption
from a successful deployment shown to an administrator.

Propose: "The `{reply_preview_request}` shall reach `{team_preview_then_send}`
after `{required_decisions}`, verified by `{request_artifact_switch_and_journey_trace}`.
Each ready handoff shall receive `{owner_acceptance_or_blocker}` within
`{confirmed_handoff_bound}` under `{working_calendar}`."

Illustrative bound only: handoff response within 1 working day;
confirm with the user/stakeholder. The example supplies no actual timestamps,
authority to enable the switch, or mandatory state sequence.

| Synthetic evidence | Reached state / remaining gap |
| --- | --- |
| Accepted request describes preview before send | Decision evidenced, not implemented by the record alone |
| Implementation revision contains preview handler | Implementation evidenced; deployed revision still needs matching |
| Matching artifact is deployed | Deployment evidenced; target audience cannot yet use it |
| Enablement handoff offered without a receiving owner | Handoff remains unaccepted; decision needed |
| Target-team switch enabled through the authorized process | Enablement evidenced; use still needs a journey check |
| Team-context fixture previews, edits, then sends | Controlled adoption endpoint evidenced, not proof of production usage |

Try a mismatch: link an older artifact that only sends directly. Labels and an
issue closure cannot make it satisfy the preview request. Try an audience mismatch:
an administrator can see preview while the team cannot; adoption remains unproved.

Report the actual stopping state and missing receiver or switch decision. Use
existing records and test contexts; do not send notifications or enable production
access without the user's authorization. A rehearsal finding is engineering evidence,
not permission to advance gates on behalf of their owners.
