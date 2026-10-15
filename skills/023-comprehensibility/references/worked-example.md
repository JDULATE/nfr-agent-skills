# Worked example: who can see a submitted report?

Assume a fictional report tool has this source-backed contract for the fixture:
a draft is visible to its author; submission adds its assigned reviewer; approval
adds the whole team. Unassigned reviewers are not automatically added by submission.
These are invented permission semantics to verify against a real project's sources.

The original explanation says: "Approval expands visibility." It omits the initial
and intermediate audiences, so a reader might infer reviewers must wait for approval.
A candidate says: "A draft is visible to its author. Submitting it also makes it
visible to its assigned reviewer. Approval then makes it visible to the whole team."

Propose: "After reading `{visibility_explanation}`, `{audience}` shall distinguish
`{draft_submitted_and_approved_visibility}` under `{allowed_context}`, verified by
`{included_excluded_role_state_questions}` against `{source_permission_key}`."
Illustrative acceptance only: 0 wrong interpretations on these selected scenarios;
confirm with the user/stakeholder before adopting that bound or the fixture rules.

| Input role/state question | Source-key answer |
| --- | --- |
| Can the assigned reviewer see a submitted, not-yet-approved report? | Yes, submission adds that reviewer |
| Can an unassigned reviewer see it merely by being a reviewer? | No, that role alone is not included by submission |
| What does approval add relative to submission? | Visibility for the whole team |
| Is the original author removed when the reviewer is added? | No, the stated fixture adds visibility rather than replacing the audience |

Keep report identity and cumulative audience membership through draft, submission,
and approval. Compare the explanation with those states; do not change access code
to make an appealing sentence become true. If actual sources contradict the example,
report the conflict before choosing the explanation's intended meaning.

Give the passage and fresh role/state questions to intended readers without the
answer column. Record wrong implications even if they paraphrase the words fluently.
The table is an interpretation oracle, not an observed audience result, a real
permission policy, or evidence that the candidate is universally comprehensible.
