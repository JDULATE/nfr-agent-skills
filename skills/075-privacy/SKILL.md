---
name: privacy
description: >-
  Defines personal-data purpose and lifecycle when tickets say "we keep storing data we never use", "stop sending emails to analytics", or "deleted accounts return after restore". Not for read permissions alone (see confidentiality) or preventing identity linkage (see anonymity). Treats policy labels as supplied constraints.
---
# Privacy

## Definition and scope

Privacy means controlling how information about people is collected, used, shared,
kept, and removed. Bind those activities, including derived data, to the agreed
purpose, subject, recipient, choice, and lifecycle. Separate that handling decision
from disclosure control (`confidentiality`) and identity unlinkability (`anonymity`);
masking a name establishes neither an approved purpose nor an unlinkability result.

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

1. Clarify: Read collection code, schemas, docs, payloads, logging and capture paths,
   SDK/tag configuration, retention jobs, and existing policy decisions first.
   Trace synthetic subject data through copies and derived outputs.
   If sensitive categories or minors are in scope, then ask what stricter handling
   the stakeholder requires; include this follow-up in the first fast-path question.
   If the request is a practical change, then use the fast path below; otherwise
   establish purpose, recipients, choice, and stakeholder-supplied policy before specifying.

2. Specify: Make a field-to-purpose record with allowed operations, recipients,
   choice behavior, retention start event, disposal action, and exception owner.
   Include the collection and capture copies listed below, not just primary stores.
   If a formal deadline is missing, then propose the illustrative duration below and
   confirm with the user/stakeholder. For a change request, present this single block:

   ```text
   Illustrative defaults — confirm with the user/stakeholder:
   Inventory row:
     Data/subjects: feature fields and derived outputs; sensitive/minor scope unresolved.
     Producer/start: discovered source; retention starts at the documented policy event.
     Purpose/owner: existing approved use and named data owner; missing authority stays open.
     Constraints: user-named labels plus policy/counsel-defined system behavior, attributed.
     Choice: documented consent/choice condition; no new optional collection while undecided.
     Recipients/operations: approved destinations and needed fields; no new cross-purpose joins.
     Copies: stores, queues, caches, indexes, exports, processors, backups; logs/error trackers;
       URLs/query strings; third-party SDKs/tags; session replay/screenshots.
   Lifecycle record:
     End/action/deadline: verified deletion request; active-store erasure within 7 days.
     Retention: existing documented duration/start event; unspecified retention remains open.
     Backups/replay: separate expiry and suppression before restored data becomes readable.
     Exceptions/tombstones: only approved scope, minimal match key, access boundary, and expiry.
     Evidence/owner: synthetic captures, per-copy outcomes, retry state, and the named owner.
     Status: design assumptions, not permission to erase or an accepted policy or legal duty.
   ```

   Ask at most three grouped questions total: which data/purpose is in scope,
   whether sensitive categories or minors are involved and, if so, what stricter
   handling applies; what policy or counsel requires for named constraints,
   recipients, retention, backups, and exceptions; and what choice behavior or
   defaults need changing. Proceed to reversible design with available answers.
   If policy is unresolved, then present alternatives and keep affected decisions open.

3. Design/Implement: Read [design patterns](./references/design-patterns.md) when
   choosing field controls, choice propagation, expiry, deletion, or capture redaction.
   If fields cross recipients or schemas change, then use serializers and classification
   tags; if choice gates collection, then propagate that state to every producer.
   If retention or deletion applies, then choose TTL or scheduling, hard/soft-delete
   semantics, tombstone expiry, and a retryable pipeline against the approved lifecycle.
   If backups or replay can reintroduce data, then design restore-time suppression;
   if telemetry or capture retains it, then redact at the source and verify recipients.
   Implement confirmed handling; keep unresolved policy choices as design alternatives.

4. Verify: Follow synthetic records through capture, derived outputs, purge jobs,
   withdrawal, and a controlled restore; inspect allowed and forbidden payloads.
   If a destination or processor provides no verifiable outcome, then record that
   gap and keep the corresponding deletion or collection claim unverified.

5. Report: Return the purpose inventory, changes, denied-flow evidence, disposal
   receipts, remaining copies, exceptions, and decisions the user still owes.
   If only active stores were checked, then report that boundary explicitly and
   withhold any claim covering backups, exports, or third-party deletion.
   Produce an engineering requirement, not a compliance conclusion.

## Specification patterns

Fill each pattern from the inventory and its approved lifecycle.

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

For a missing deletion deadline, use the illustrative active-store default in
Specify and confirm with the user/stakeholder. Keep backup expiry, recipient
handling, and policy exceptions separate from that illustrative duration.

## Rules of thumb

- Do reject optional fields at the producer when their purpose is unconfirmed;
  do not collect them first on the assumption that retention can be decided later.
- Do send even an authorized recipient only the personal fields needed for its
  approved purpose; permission to receive an account object does not justify
  forwarding unused contact fields in an analytics event.
- Do stop optional collection at its source when the confirmed choice is withdrawn;
  hiding the choice control must not stand in for changing the collection path.
- Do propagate retention and deletion decisions to indexes, caches, derived
  profiles, and exports; do not let a derived output escape the inventory by renaming it.
- Do prevent restored or replayed data from repopulating deleted active records;
  retain only the suppression evidence approved for that purpose and its own expiry.
- Do give disposal evidence its own purpose, minimal personal fields, and expiry;
  don't recreate the erased profile in a purge log that is retained longer than
  the approved deletion-evidence purpose requires.
- Don't equate encryption, masking, or a replacement identifier with permission
  to collect, indefinite retention, or demonstrated anonymity.
- Do record user-named regulations or request labels as stakeholder-supplied constraints;
  ask what their policy or counsel requires of the system, and never state obligations as fact.

## Verification

Use data-flow review, payload capture, storage inspection, and lifecycle integration
test categories. Inspect logs, error trackers, URLs and query strings, third-party
SDKs/tags, and session replay or screenshots alongside stores, exports, and backups.
Exercise initial SDK/tag loading, queued events, navigation, and off/on/withdrawn
choice states; verify forbidden fields are absent before transmission or capture.
Inspect replay frames and screenshots as well as structured payloads and error reports.
Check that an unverified request causes no disposal and a verified request affects
only its intended synthetic subject; retain unrelated-subject records as controls.
Use controlled-clock checks around the retention start event and disposal deadline.
Inject a purge failure and verify retry evidence without falsely recording completion.
Inspect remaining copies and derived outputs after deletion; rehearse restore or
replay to detect resurfacing. Track purge backlog, overdue records, and recipient
receipt gaps with minimal evidence fields; protect that evidence under its own policy.

## Done checklist

- [ ] Map personal fields and derived outputs to confirmed purposes and owners.
- [ ] Inventory storage, telemetry, URL, SDK/tag, replay, screenshot, and backup copies.
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
- Read [design patterns](./references/design-patterns.md) when implementing recipient
  serializers, classification, choice propagation, retention, deletion, or redaction.
