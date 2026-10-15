# Worked example: a renamed partner field

Assume a fictional dispatch feed whose current field `delivery_slot` carries the
agreed label `morning`. The reported replacement sends `slot_label` with the same
meaning. No real partner protocol or compatibility guarantee is asserted here.

Read the ingestion adapter, dispatch consumer, and accepted payload docs. Confirm
that the label's meaning is unchanged and whether the old shape remains supported.
Propose: "Under `{changed_feed_shape}`, ingestion shall preserve
`{dispatch_slot_meaning}` through `{approved_mapping}`, verified by
`{old_new_and_unknown_message_fixtures}` within `{confirmed_difference_bound}`."

Illustrative bound only: 0 unexplained paired-output differences;
confirm with the user/stakeholder before using that bound or these mappings.

| Synthetic source | Expected boundary result | Reason |
| --- | --- | --- |
| `delivery_slot=morning` | `dispatch_slot=morning` | Original condition remains supported in this scenario |
| `slot_label=morning` with confirmed new-variant evidence | `dispatch_slot=morning` | Representation changes; domain meaning does not |
| `slot_label=flex` with no approved interpretation | Agreed unsupported-value outcome | Do not invent a dispatch period from the new label |
| Contradictory old/new selection evidence | Explicit ambiguity response | Do not select whichever mapping happens to parse |

Replay messages through normal dispatch ingestion, not a detached mapping function
alone. Compare the consumer's selected slot and written result. Search downstream
code for direct reads of either external field; resolve duplicated interpretations
at the boundary or document why a consumer genuinely requires a source distinction.

If the changed label actually means a different dispatch promise, stop claiming
semantic equivalence and obtain the owner-approved behavior change. Passing the
renamed-field case cannot establish support for that new meaning.

Report source evidence, condition selection, normalized outputs, and unsupported
cases. These fixtures illustrate the acceptance question; no partner was contacted
and no installed integration was verified by this example.
