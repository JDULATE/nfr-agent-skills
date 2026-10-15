# Restoration practices

Choose the recovered journey/state endpoint before optimizing restore commands.

## Recovery dependency bootstrap

- Use when credentials, keys, runtime artifacts, schemas, routing, or operators
  are prerequisites for the restore path.
- Trade-off: independent bootstrap adds operational work and its own protection
  decisions; copying data alone cannot supply missing decryption or execution context.
- Verify: start with only resources declared to survive the disruption and prove
  the needed prerequisites can be obtained through the authorized recovery route.

## Coherent snapshot and replay boundary

- Use when restoration combines snapshots, logs, queues, or exported records.
- Trade-off: selecting a boundary can leave gaps or overlap; an import success
  message does not establish that the combined state represents the required work.
- Verify: identify included work, replay start, ordering, and deduplication scope;
  inspect actual effects around the boundary instead of assuming filenames align.

## In-flight and external-effect reconciliation

- Use when work may have committed before its completion response was lost.
- Trade-off: replaying all work can duplicate effects, while skipping uncertain
  work can lose required results. The effect boundary and authority must be explicit.
- Verify: classify completed, pending, duplicate, and unknown operations using real
  state/effect evidence before resumption; retain unresolved work for owned decisions.

## Recovery milestone and journey validation

- Use when data import or process startup is proposed as the recovery endpoint.
- Trade-off: full state/business checks add elapsed time but distinguish a running
  process from a service that actually produces the required recovered result.
- Verify: timestamp disruption, bootstrap, restore, replay, validation, and usable
  journey; compare loss and elapsed time with confirmed requirements independently.

## Interrupted rehearsal and warm shortcuts

- Use when the procedure may be interrupted or exercise inputs are prewarmed.
- Trade-off: resumable recovery needs progress/ownership handling; a warm exercise
  can be useful diagnostically but does not test cold bootstrap work it bypasses.
- Verify: inspect intermediate state, retry/resume effects, and all shortcuts;
  use an isolated target and disclose dependencies not actually removed by the exercise.
