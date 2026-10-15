# Privacy design patterns

Choose mechanisms for the approved data purpose and lifecycle, not from a regulation
label. Obtain policy or counsel-defined system constraints from the stakeholder;
present engineering behavior and evidence, not a compliance conclusion.

## Per-recipient allowlist serializers

- **Use when:** A producer shares personal fields with recipients needing different
  subsets. Build a payload from approved fields instead of serializing the full model.
- **Trade-off:** Recipient schemas and purpose decisions need coordinated updates;
  dropping a new field can affect a feature, so surface an explicit contract mismatch.
- **How to verify:** Add a synthetic nested personal field to the source model.
  Capture each recipient payload and assert only its approved subset appears,
  including failure paths and alternate serializers.

## Schema field-classification tags

- **Use when:** Fields need traceable handling across schemas, derived outputs, and
  exports. Attach owner-approved classification, purpose, recipient, and lifecycle
  metadata; identify unresolved sensitive-category or minor-related handling.
- **Trade-off:** Tags can become stale or disappear in transformations. Metadata
  alone is not enforcement or authority to choose a purpose or retention period.
- **How to verify:** Introduce a field and a derived output; inspect review or
  enforcement behavior for missing tags and trace retained metadata to actual
  serializer, retention, and redaction behavior.

## Choice/consent state propagation to producers

- **Use when:** The stakeholder's policy makes collection conditional on a choice.
  Propagate the scoped state to application producers, SDKs, tags, and capture paths
  before they collect; define how withdrawal affects queued and existing data.
- **Trade-off:** Cached state, multiple sessions, and buffered work complicate
  transitions. A choice control on screen does not establish what producers saw.
- **How to verify:** Exercise startup before choice, enablement, withdrawal, stale
  producer state, queued flushes, and another session. Inspect egress and replay or
  screenshot capture; follow the accepted policy for data already collected.

## TTL or scheduled retention

- **Use when:** A confirmed start event and expiry rule can drive a TTL mechanism
  or scheduled purge. Specify the deadline for actual removal, not just eligibility.
- **Trade-off:** Expiry marking and physical removal may differ in the chosen store;
  scheduled work needs backlog and failure handling. Inspect the store's behavior.
- **How to verify:** Use a controlled clock before and at the accepted boundary,
  delay a worker, and inspect records, indexes, caches, and completion evidence.
  Check the start event and retries do not silently extend the accepted lifetime.

## Hard vs soft delete and tombstones

- **Use when:** A feature must distinguish hiding a record from removing its active
  stored representation, or must retain a deletion marker for synchronization.
  Choose semantics explicitly; give tombstones their own minimal fields and expiry.
- **Trade-off:** Soft-deleted data or match keys can remain personal information in
  the project's scope. Active-record removal does not by itself establish removal
  from backup, telemetry, or provider copies.
- **How to verify:** Query normal, administrative, index, and export paths after
  deletion; inspect retained bytes or records where observable. Exercise synchronization
  with tombstones and verify the approved marker-access and expiry decisions.

## Restore-time suppression lists

- **Use when:** Restored backups or replayed events can reintroduce erased records.
  Apply the accepted deletion decisions before affected data becomes readable.
- **Trade-off:** Suppression keys need their own purpose, access boundary, and expiry;
  reconcile key lifetime with the backups and replays they must cover. Restores may
  need to wait for suppression state rather than serving unchecked personal records.
- **How to verify:** Restore a synthetic deleted subject from an older copy, replay
  old events, and exercise unavailable suppression state. Inspect serving and
  downstream paths; confirm an unrelated subject remains intact.

## Idempotent retryable deletion pipelines

- **Use when:** Disposal spans destinations that fail or acknowledge at different
  times. Track a verified subject-scoped job and outcomes per destination; make
  repetition safe under the destination's accepted deletion semantics.
- **Trade-off:** Job ledgers, receipts, and matching keys are retained data too;
  define their minimum fields and lifetime. Queue acceptance is not disposal evidence.
- **How to verify:** Duplicate a job, interrupt it after partial completion, and
  retry failed destinations. Check no unrelated subject changes, successful steps
  remain safe to repeat, and missing receipts keep completion appropriately scoped.

## Log and error-report redaction

- **Use when:** Personal values can enter logs, error trackers, URLs/query strings,
  third-party SDKs/tags, or session replay/screenshots outside the primary data flow.
  Filter or redact before emission or capture, including nested and error payloads.
- **Trade-off:** Less captured detail can limit debugging. Agree on minimal diagnostic
  fields and their purpose and expiry; later dashboard masking is not source removal.
- **How to verify:** Send synthetic markers through success, exception, navigation,
  SDK, and capture paths. Inspect producer output, received errors, stored URLs,
  replay frames, and screenshots; verify the approved diagnostic fields remain usable.
