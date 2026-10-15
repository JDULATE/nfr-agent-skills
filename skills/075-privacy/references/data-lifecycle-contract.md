# Personal-data lifecycle contract

Build the purpose inventory from project artifacts and stakeholder-approved policy.
Record named regulations or request labels as stakeholder-supplied constraints;
ask what their policy or counsel requires of the system. Attribute that behavior
to the supplied policy rather than stating legal obligations as fact. Produce an
engineering requirement, not a compliance conclusion; a schema is not permission.

## Inventory record

Use a row per field group and purpose; split a row when recipients or lifecycle
rules differ. Treat inferred or derived personal outputs as inventory candidates.
Resolve uncertain personal-information scope or identifiability with the owner.
Ask whether sensitive categories or minors are included; if yes, ask what stricter
handling the stakeholder requires, without inferring duties from the category.

| Record field | Decision to capture |
| --- | --- |
| Data and subjects | Fields, derived outputs, and whose information they describe |
| Producer and start event | Collection path and the event that begins retention |
| Purpose and owner | Accepted use and the person accountable for that decision |
| Choice or authority | Condition that permits handling and what withdrawal changes |
| Recipients and operations | Allowed destinations, fields, reads, joins, and transformations |
| Copies | Primary stores, queues, caches, search indexes, exports, processors, backups; logs, error trackers, URLs and query strings, third-party SDKs/tags, session replay or screenshots |
| End condition | Retention deadline, deletion request, withdrawal, or another accepted event |
| Disposal | Erasure, expiry, or another specifically accepted action and its evidence |
| Exceptions | Approved reason, scope, access restriction, decision owner, and review event |
| Reintroduction | Restore or replay handling that reapplies the disposal decision |

Do not label a transformed dataset anonymous without a separate agreed observer
and linkage assessment. Route that question to the anonymity sibling.

### Filled illustrative inventory row

Illustrative example only; confirm with the user/stakeholder. Use this synthetic
support-contact scenario as an example record, not a finding or required policy.

| Data / subjects / producer / start | Purpose / owner / choice or authority | Recipients / operations / copies | End / disposal | Exceptions / reintroduction | Evidence |
| --- | --- | --- | --- | --- | --- |
| SYNTHETIC_CONTACT; adult test account; support form; case closure starts retention | Reply to submitted support case; example support owner; hypothetical owner-approved support use | Support worker reads contact; case store, queue, backup; omit contact from logs/errors, URLs/query strings, SDKs/tags, replay/screenshots | Verified deletion request; active contact erased within 7 days (illustrative; confirm with the user/stakeholder) | No exception in this example; backups expire at the approved rotation event; apply suppression before serving restored contact | Synthetic egress/capture checks, per-copy ledger, disposal receipts |

Keep retention after case closure as a separate owner-confirmed rule; the deletion
deadline above is not a default retention duration. Bind the example's rotation
event to a concrete expiry boundary before accepting a real backup requirement.

## Requirement-spec record

Write the subject class, purpose, field and recipient allowlists, start event,
deadline, disposal action, copy coverage, exception process, and evidence location.
Keep unresolved policy items visible and distinguish a proposed requirement from
an observed disposal outcome.

If the user gives no number, offer this illustrative example only: deletion of
inventoried active-store data within 7 days of `{verified_request_event}`;
confirm with the user/stakeholder. Ask the user for the backup expiry and processor
response boundary separately. Do not imply this duration comes from a law or standard.

## Lifecycle verification matrix

Use synthetic subjects and distinguishable marker values, not real user records.

| Scenario | Observe | Reject completion when |
| --- | --- | --- |
| Optional collection disabled | Producer and outgoing recipient payloads | A forbidden field appears even if no screen displays it |
| Approved collection enabled | Only purpose-allowed fields reach allowed recipients | A broad account object is forwarded |
| Choice withdrawn | Subsequent collection plus handling of existing copies | Only the interface state changes |
| Unverified disposal request | Request rejection and absence of data changes | A purge starts before the accepted verification condition |
| Verified subject-scoped request | Target subject changes and unrelated-subject controls | Another subject is removed or the target scope is silently broadened |
| Retention deadline reached | Data presence and disposal outcome at every mapped destination | The job ran but records remain past the accepted boundary |
| Disposal worker fails | Retry record and unresolved destination status | An accepted queue item is treated as an erasure receipt |
| Deletion requested | Derived outputs, indexes, exports, and processor receipts | Only the primary row has been inspected |
| Backup restored or events replayed | Disposal decisions applied before affected data is served | A previously deleted active record reappears |
| Telemetry, navigation, SDKs/tags | Logs, error trackers, URLs and query strings, outgoing third-party payloads | A synthetic personal marker escapes an approved purpose or field allowlist |
| Replay or screenshot capture | Stored frames, images, and their recipient copies in off/on/withdrawn states | A blocked field was captured before a later display mask was applied |

For controlled-clock tests, exercise just before the accepted deadline and at
the disposal boundary under the agreed scheduling policy. Ask the user whether
the deadline includes processing delay; never add an unstated grace period.

## Remaining-copy ledger

Record destination, data class, action requested, result observed, evidence time,
remaining availability, expiry event, and responsible owner. Mark unknown outcomes
unknown. A configured expiry is a plan; an observed expired copy is evidence.
If a destination cannot erase data on request, ask whether its documented expiry
and restricted restore handling satisfy the agreed requirement. Do not silently
weaken the requirement to fit that destination's capability.

Give disposal evidence its own field minimization and expiry decision. Avoid a
global subject identifier when a scoped job reference can support the agreed audit
question. If restore suppression needs a subject match key, ask for the minimal
key, access boundary, and retention policy rather than promising no retained data.

## Anti-pattern catalog

- **Security substitution:** Reject a purpose decision justified only by encryption.
- **Source-only purge:** Trace derived and recipient copies before claiming coverage.
- **Unbounded archive:** Ask for an expiry instead of accepting "keep for support".
- **Invisible collection:** Inspect producers and egress even when a control is absent.
- **Unverifiable processor:** Report missing receipt evidence rather than total erasure.
- **Deletion evidence as new collection:** Remove raw payloads from purge traces.
