# Worked example: compress repeated review obligations

Use this fictional source requirement, not a real approval policy:

> For submitted reports, the assigned reviewer must review the report. It is required that the assigned reviewer review each submitted report. For submitted reports, the assigned reviewer must not approve the report until attachments are checked.

The candidate is:

> For submitted reports, the assigned reviewer must review them and must not approve them until attachments are checked.

The first review obligation was repeated; the attachment condition was not.
Neither source nor candidate says who must check attachments, or that approval
becomes mandatory once they are checked. Keep those implications out of the rewrite.

Illustrative target only: 10% fewer whitespace-separated words;
confirm with the user/stakeholder before adopting that target or this source meaning.
The illustrative counts are 36 before and 18 after, removing 18 words;
confirm with the user/stakeholder. These are literal-text counts, not measured
reading improvement or a universal requirement for shorter explanations.

| Retained proposition | Candidate location / boundary check |
| --- | --- |
| Submitted-report scope | Opening condition; an unsubmitted report is outside this clause's stated scope |
| Assigned reviewer must review | First obligation; do not make it optional or assign it to every reviewer |
| Approval prohibited until attachments checked | Second obligation; unchecked attachments still forbid approval |
| Checked attachments are necessary, not sufficient for mandatory approval | Do not rewrite must-not-until as must-approve-when |

Propose: "The shortened `{review_requirement}` shall retain `{proposition_set}`
within `{confirmed_word_budget}`, verified by `{same_rule_word_count}` and
`{positive_negative_scope_and_obligation_cases}` without adding `{new_actor_or_duty}`."

Carry the same report scope, assigned role and attachment-state meaning into the
candidate. A tempting cut to "Reviewers approve reports when attachments are checked"
loses assignment, changes obligation strength, and changes the conditional rule.
The shorter candidate is rejected regardless of its word count.

These examples supply preservation questions. They do not show actual reader
answers, legal obligations, or an observed improvement in interpretation.
