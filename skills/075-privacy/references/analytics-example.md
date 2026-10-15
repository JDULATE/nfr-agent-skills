# Worked example: an analytics event contains an account profile

Use this invented scenario as an illustration, not a finding about the repository.

## Inspect the flow

Take the request: "Stop collecting these account fields in analytics, and make
account deletion cover the analytics copies."
Read the event producer, account serializer, recipient configuration, warehouse
ingestion, and existing disposal worker before drafting a requirement.
Suppose the producer forwards the whole account object and a derived campaign
profile outlives its source row. Treat those as hypothetical facts for this example.

Ask the user which event fields the feature needs, what purpose permits them,
whether optional collection requires a choice, and who may receive them. Ask for
the active-store deletion event, required deadline, backup expiry, and processor
receipt capability. Do not infer any of these from the event name.

## Narrow the payload

Suppose the stakeholder proposes retaining the event type and feature context
while removing contact fields and cross-purpose account identifiers. Build a
recipient-specific allowlist instead of serializing the account object.
For this hypothetical approved purpose, compare these synthetic payloads:

Before:

```json
{"event_type":"help_opened","feature":"order_help","account":{"contact_email":"SYNTHETIC_CONTACT","account_key":"SYNTHETIC_SUBJECT"}}
```

After:

```json
{"event_type":"help_opened","feature":"order_help"}
```

Keep only `event_type` and `feature` for this example's aggregate feature-use
question. Test that `account`, `contact_email`, and `account_key` are absent at
both producer egress and the recipient. This is a purpose-specific proposal,
not a universal analytics schema.

If the analytics use cannot work without an identifier, return that conflict to
the user; do not introduce an undisclosed replacement identifier as a workaround.

Propose this collection requirement: "The analytics producer shall emit only
`{approved_event_fields}` for `{confirmed_feature_purpose}` to
`{approved_recipient}` under `{confirmed_collection_condition}`. Payload-capture
checks shall reject contact fields and any identifier outside that allowlist."

## Specify disposal

Propose: "After `{verified_account_deletion_event}`, the system shall erase
`{in_scope_subject_records}` from the event store and derived campaign profile
within `{confirmed_active_store_deadline}`, record destination-specific outcomes,
and apply the disposal decision before a backup restore or replay serves those
records again. Track `{remaining_backup_expiry}` and `{processor_receipt_boundary}`
separately, with `{approved_exceptions}` visible in the completion report."

Illustrative example only: offer 7 days for the active-store deadline;
confirm with the user/stakeholder. Keep backup expiry and processor outcomes
unresolved until the user confirms them; do not promise total erasure meanwhile.

## Exercise and report

Insert a synthetic subject marker into the hypothetical flow. Inspect producer
and recipient payloads with optional collection disabled and withdrawn. Confirm
the removed fields are absent on the wire, not merely omitted from a dashboard.

Trigger a verified disposal request in a controlled environment. Query the event
store and derived profile after the agreed boundary. Include an unrelated synthetic
subject as a control and check that its records remain intact. Attempt an unverified
request separately and confirm it starts no disposal. Fail a destination worker,
then inspect its retry and incomplete outcome before retrying. Rehearse an older
backup restore and event replay; check the disposal decision is reapplied before
the restored subject data becomes available to normal consumers.

Report separately: verified active-store removal, verified derived-output removal,
remaining backup copies and expiry, and any unverified recipient action. Keep the
request open for unresolved destinations unless the accepted contract explicitly
allows a scoped completion. This example describes a plan, not executed results
or a legal compliance conclusion.
