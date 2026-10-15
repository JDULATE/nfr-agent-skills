# Worked example: a report submission view

Assume a fictional report requires an attachment before Submit is available.
Starting draft `report-amber` has no attachment and is not submitted. Submission
is confirmed only by the accepted completion response; failure retains the draft.
These state rules are example assumptions, not verified application behavior.

Illustrative acceptance only: 0 wrong state/action inferences on these fixtures;
confirm with the user/stakeholder before adopting the state set or error bound.
Propose: "For `{report_state}`, `{submission_view}` shall expose
`{current_state_real_prerequisite_and_next_action}`, verified by `{guard_view_and_reader_key}`
without changing `{submission_permission_or_effect}`."

| Source state / event | View output | Available action and expected inference |
| --- | --- | --- |
| Draft, attachment absent | `Draft -- add an attachment to enable Submit` | Submit disabled; draft has not been submitted |
| Draft, attachment present | `Draft -- ready to submit` | Submit enabled; enabling alone did not submit it |
| Submit initiated, response pending | `Submitting -- waiting for confirmation` | Pending, not submitted; any further action follows the inspected contract |
| Confirmed completion | `Submitted` | Completion evidenced; available actions reflect submitted state |
| Failed submission, draft retained | `Submission failed; report remains a draft` | Retry only under the real retry policy; no success implied |

Carry report identity and attachment/submission state through the view. A stale
label for another report is not rescued by correct wording; check object context
and guard inputs together. Show a disabling reason only while that prerequisite
is actually unmet.

Ask the audience whether the report is submitted and what they can do next at
fresh equivalent states, without supplying the table's answer column. Static tests
of label text support the mapping but do not show what users infer.
This example does not establish response timing, safe retry semantics, or actual
reader success. Missing authoritative action behavior remains a question for the owner.
