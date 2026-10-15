---
name: privacy
description: >-
  Defines and verifies personal-data handling boundaries when users say "stop
  collecting this field", "set data retention", "delete my account data", or
  "review analytics tracking". Not for disclosure protection alone (see
  confidentiality) or identity-unlinkability claims alone (see anonymity).
status: draft
---
# Privacy

## Definition and scope

Limit handling of personal information to agreed purposes, people, recipients,
and lifecycle boundaries, including collection, derived data, retention, and disposal.
Distinguish `confidentiality`, which controls disclosure, from whether the handling
should occur at all; route identity-unlinkability claims to `anonymity` rather than
treating masking or a replaced identifier as proof of them.

## Use when / Don't use when

- Apply when a feature collects personal fields, creates tracking identifiers,
  changes a recipient, or needs retention, withdrawal, or deletion behavior.
- Include analytics, telemetry, exports, and derived profiles when they fall
  within the user's agreed personal-information scope.
- Route an isolated permission or disclosure defect to `confidentiality` or
  `security-control-and-security`; keep the separate purpose decision here.
- Route a claim that observers cannot identify a person to `anonymity`; do not
  promise that result merely because names have been removed.

## Workflow

1. Clarify: Read data models, collection handlers, event payloads, vendor
   configuration, retention jobs, and existing data-handling decisions first.
   Trace a synthetic person's data from collection to copies and derived outputs.
   If purpose, permitted recipients, or applicable policy is unknown, then
   Ask the user and mark the affected flow undecided before specifying it.

2. Specify: Make a field-to-purpose record with allowed operations, recipients,
   choice behavior, retention start event, disposal action, and exception owner.
   Include intermediate stores, exports, processors, and backup restoration.
   If the user provides no duration, then propose the labeled illustrative
   deletion target below and confirm with the user/stakeholder before acceptance.

3. Design/Implement: Remove unjustified collection from producers and downstream
   contracts; constrain recipient payloads and implement the confirmed lifecycle.
   If a copy cannot be erased on the active-store schedule, then specify its
   separate expiry and restore-time suppression before claiming deletion complete.

4. Verify: Follow synthetic records through capture, derived outputs, purge jobs,
   withdrawal, and a controlled restore; inspect allowed and forbidden payloads.
   If a destination or processor provides no verifiable outcome, then record that
   gap and keep the corresponding deletion or collection claim unverified.

5. Report: Return the purpose inventory, changes, denied-flow evidence, disposal
   receipts, remaining copies, exceptions, and decisions the user still owes.
   If only active stores were checked, then report that boundary explicitly and
   withhold any claim covering backups, exports, or third-party deletion.

## Specification patterns

Treat braces as decision fields; resolve them with the data owner before acceptance.

- **Collection:** For `{feature_and_purpose}`, the system shall collect only
  `{approved_fields}` after `{approved_choice_or_authority_condition}` and send
  only `{recipient_specific_fields}` to `{approved_recipients}`, verified by
  `{capture_and_negative_payload_checks}`.
- **Retention:** For `{data_class}`, the system shall apply `{disposal_action}`
  by `{confirmed_duration}` after `{defined_start_event}`, covering
  `{stores_and_derived_outputs}` with `{documented_exceptions_and_evidence}`.
- **Deletion:** After `{verified_request_or_withdrawal_event}`, the system shall
  remove `{in_scope_data}` from `{active_destinations}` within `{confirmed_deadline}`,
  track `{remaining_copy_expiry}`, and suppress reintroduction during
  `{restore_or_replay_path}`, verified by `{synthetic_subject_lifecycle_test}`.

Illustrative example only: propose deletion from inventoried active stores within
7 days of `{verified_request_event}`; confirm with the user/stakeholder.
Ask the user to confirm backup expiry, downstream recipient handling, exceptions,
and the verification event separately; do not turn that proposal into a legal rule.

## Rules of thumb

- Do reject optional fields at the producer when their purpose is unconfirmed;
  do not collect them first on the assumption that retention can be decided later.
- Do derive a separate payload for each recipient's approved purpose; do not
  reuse a full account object as an analytics or support event.
- Do stop optional collection at its source when the confirmed choice is withdrawn;
  hiding the choice control must not stand in for changing the collection path.
- Do propagate retention and deletion decisions to indexes, caches, derived
  profiles, and exports; do not let a derived output escape the inventory by renaming it.
- Do prevent restored or replayed data from repopulating deleted active records;
  retain only the suppression evidence approved for that purpose and its own expiry.
- Don't include raw personal payloads in disposal logs; retain scoped identifiers,
  actions, destinations, outcomes, and expiry under an approved evidence purpose.
- Don't equate encryption, masking, or a replacement identifier with permission
  to collect, indefinite retention, or demonstrated anonymity.

## Verification

Use data-flow review, payload capture, storage inspection, and lifecycle integration
test categories. Exercise optional-collection off, on, and withdrawn states against
the accepted policy; assert forbidden fields are absent, not merely hidden in the UI.
Check that an unverified request causes no disposal and a verified request affects
only its intended synthetic subject; retain unrelated-subject records as controls.
Use controlled-clock checks around the retention start event and disposal deadline.
Inject a purge failure and verify retry evidence without falsely recording completion.
Inspect remaining copies and derived outputs after deletion; rehearse restore or
replay to detect resurfacing. Track purge backlog, overdue records, and recipient
receipt gaps with minimal evidence fields; protect that evidence under its own policy.

## Done checklist

- [ ] Map personal fields and derived outputs to confirmed purposes and owners.
- [ ] Enumerate producers, recipients, stores, exports, and backup copies in scope.
- [ ] Record choice or authority conditions and the behavior after withdrawal.
- [ ] Confirm retention start events, deadlines, disposal actions, and exception owners.
- [ ] Check forbidden collection and recipient fields with synthetic payload evidence.
- [ ] Exercise request verification, subject isolation, disposal failure, retry, and completion.
- [ ] Record backup expiry and check that restore or replay cannot silently undo deletion.
- [ ] Limit completion claims to verified destinations and document remaining copy gaps.

## Failure modes

- Encrypting an unnecessary field and reporting that its collection is justified.
- Deleting the source row while leaving a derived profile or exported copy unexamined.
- Stopping display of tracking controls while optional collection still runs.
- Marking a failed purge complete because its request was accepted by a queue.
- Restoring a deleted subject from an older backup without applying the deletion decision.
- Logging full personal records as evidence of having deleted them.

## References

- Read [data lifecycle contract](./references/data-lifecycle-contract.md) when mapping
  collection, retention, exceptions, disposal evidence, or remaining copies.
- Read [analytics worked example](./references/analytics-example.md) when narrowing
  an event payload and specifying deletion without inventing a retention obligation.
