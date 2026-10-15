# Worked example: manual and automated dispatch

Assume a fictional dispatch tool supports guided manual assignment and automatic
assignment for a shipment. Both must commit an accepted destination to the same
shipment record; manual review notes are an explicitly permitted difference.

Inspect assignment code, route selection, task docs, authority requirements, and
commit tests. Confirm that the intended operator can actually use both routes.
Propose: "For `{shipment_task}`, `{chooser}` shall independently complete
`{confirmed_routes}` with `{shared_destination_commit}` under `{route_prerequisites}`,
verified by `{selection_trace_and_committed_outcome_matrix}`."

Illustrative scope only: 2 arrangements, manual and automated;
confirm with the user/stakeholder. These fictional routes are not assumed to exist
in an actual dispatch product or to be equally useful for every shipment.

| Fixture | Shared result / route evidence |
| --- | --- |
| Manual selection for shipment `parcel-amber` | Operator chooses `depot-east`; destination is committed |
| Automated selection from matched starting state | Candidate rule selects the accepted destination; commit is inspected |
| Manual panel displays `depot-east` without writing | Fails shared result despite matching displayed text |
| Selector labels both call unavailable auto-assignment | No independent manual arrangement demonstrated |
| Operator lacks the manual route's required authority | Option cannot count as available to that chooser |

Use fresh matched state for each independent task so prior writes cannot make the
other route appear successful. Compare the accepted destination and required
recorded effects; do not require identical intermediate interactions or notes.
Inspect route-specific inputs and rejection explanations before concluding an
option is genuinely available to the intended audience.

Do not switch the in-flight `parcel-amber` job between routes as implicit evidence
of independent coverage. That is a separate transition question needing state
semantics. Report route coverage, chooser restrictions, and any missing commit.
This example demonstrates a comparison protocol, not verified dispatch behavior.
