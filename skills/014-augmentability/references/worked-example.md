# Worked example: suggestions beside a support reply

Imagine a support application with an existing manual reply-and-send workflow.
The user asks to add suggested reply text without replacing that workflow.
Treat the application and all behavior below as synthetic scenario conditions.

## Establish distinct results

Read the reply handler, ticket state model, send action, and support workflow docs.
Take the original result to be the agent's chosen reply being sent and recorded.
Give the helper a separate result: suggested text displayed for that ticket.
Ask the user what ticket fields the helper may read and whether adopting its text
requires an explicit action. Do not infer write authority from the word assistant.

## Requirement and design

Propose: "The system shall display `{accepted_suggestion_result}` in a separate
support panel for `{ticket_scope}` while the existing manual send route retains
`{original_reply_contract}`. The panel shall alter the reply draft only through
`{confirmed_adoption_action}` and shall not be required for manual sending."

Illustrative preservation target only: 0 original reply-result changes in the
agreed absent-helper fixture; confirm with the user/stakeholder. Establish the
helper's own quality criteria separately rather than borrowing this preservation target.

Use a read-only ticket projection and an explicit copy-to-draft action as candidate
boundaries. If the ticket changes while a suggestion is pending, show or reject
the stale suggestion under the user's agreed rule. Keep the original send action
responsible for sending, whether the text was typed or deliberately adopted.

For a concrete synthetic case, set the original draft to "I will check your order"
and let the helper display "Please confirm the order reference". Before adoption,
the original draft must still contain the agent's text. After explicit adoption,
only that ticket's draft may contain the suggested text; nothing has been sent
until the original send action runs. Disable the helper and repeat manual sending.

## Inspect concrete cases

| Scenario | Original-path check | Supplement check |
| --- | --- | --- |
| Helper disabled | A typed reply can still be sent and recorded | No panel dependency remains |
| Suggestion merely displayed | The draft and send ledger remain unchanged | Ticket and suggestion provenance are visible |
| Suggestion adopted | Only the chosen draft changes before ordinary send | Adoption is linked to the current ticket |
| Helper stalls or is removed | Manual send follows its original contract | Pending helper output cannot overwrite another ticket |

Report observed evidence only after running these cases in the actual application.
This example defines a testable separation; it does not establish the usefulness
of suggestions, legal permission to send ticket data, or production independence.
