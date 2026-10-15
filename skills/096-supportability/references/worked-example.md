# Worked example: an export looked up in the wrong context

Assume a fictional export service reports `Export not ready` for `job-lilac` queried
in `team-cedar`. The user's task is to obtain their own completed report. In this
fixture lilac belongs outside that context, while `job-moss` is team-cedar's completed
job producing `report-cedar`. No real export service behavior is asserted.

The hypothetical support policy permits case id, revision, requested context/job,
and a diagnostic reason. It excludes raw payload and `account_note`. Confirm that
boundary in a real project; it is not a universal support data policy.
Illustrative scope only: 1 synthetic case bundle; confirm with the user/stakeholder.

Propose: "For `{missing_export_case}`, support shall distinguish `{reason_branches}`
from `{permitted_bundle}` and check `{authorized_remedy}` against
`{affected_actor_report_result}`, escalating `{missing_evidence_or_authority}`."

```json
{"case":"case-amber","revision":"build-cedar","context":"team-cedar",
 "requested_job":"job-lilac","reason":"context_mismatch"}
```

| Case state / diagnostic branch | Action and concrete result oracle |
| --- | --- |
| Current revision, reason `context_mismatch` | Confirm intended context/id; do not grant cross-context access |
| User selects their own `job-moss`, same context | User lookup returns `report-cedar`; original required task succeeds |
| Admin bypass fetches lilac's foreign artifact | Not valid user-case resolution under the fixture's access/task contract |
| Reason `pending` for a context-owned job | Follow the documented pending-job branch, not the mismatch remedy |
| Unknown reason or unverified old revision | Proposed escalation includes missing reason mapping/revision evidence; resolution unproved |

Place `SECRET_MARKER` in the synthetic account note and raw payload. Check neither
appears in the generated bundle, runbook output, or case evidence intended for the
declared support actor. Inspect the collector and reason-to-action mapping together.

Carry case identity, revision, requested context/job, and actor scope through the
before/after lookup. A new ticket status without the `report-cedar` result does not
satisfy resolution. The fixture does not contact a customer, grant permission,
or demonstrate any actual production case outcome.
