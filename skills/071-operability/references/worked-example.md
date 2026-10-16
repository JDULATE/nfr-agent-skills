# Partial export operator task

Treat this as an illustrative synthetic export workflow.
All chunk counts and proposed actions are illustrative examples;
confirm with the user/stakeholder before applying them to a project.

## Filled task record

| Field | Fixture value |
| --- | --- |
| Operator / target | export-operator / export-elm |
| Authority | read state and resume only this synthetic export |
| Desired outcome | published artifact with rows A, B, C once each, in that order |
| Required chunks | chunk-ash -> A; chunk-birch -> B; chunk-cedar -> C |
| Initial owner | none active |
| Initial committed manifest | chunk-ash only |
| Initial partial output | A, not published |
| Initial staging | chunk-birch temporary data B, not committed |
| Resume rule | preserve committed chunks; discard verified uncommitted staging and regenerate remaining chunks |
| Completion evidence | committed manifest plus published artifact content |
| Handoff owner | export-duty-owner |
| Carry | existing chunk-ash and committed manifest remain through resumption |

## Failing task before remediation

The runbook says "rerun the export" and checks only the command return value.
Its fixture command starts at the first chunk and appends to existing output.
It produces A, A, B, C and returns success.

The command succeeded but the required operator outcome failed.
This constructed behavior establishes a missing task branch and exit check,
not a production exporter defect.

## Remediation and after walkthrough

Inspect export-elm: no active owner, chunk-ash committed, Birch staging uncommitted.
Emit resume context identifying that state and the remaining Birch/Cedar work.
Remove only the verified uncommitted Birch staging.
Generate and commit chunk-birch, then chunk-cedar, preserving chunk-ash.
Assemble the committed chunks in the required order and publish the artifact.

The after record is:
```text
committed = [chunk-ash, chunk-birch, chunk-cedar]
staging = empty
published_rows = [A, B, C]
publication = complete
owner = none active after completion
```

A fresh operator can verify this outcome without the prior operator's memory.

## Blocked starting-state case

Use the same target, partial manifest, and staging, but set active owner=worker-moss.
Preflight returns blocked and emits:
```text
target = export-elm
observed_owner = worker-moss
committed = [chunk-ash]
blocked_action = resume would start a competing writer
handoff_owner = export-duty-owner
```

The procedure performs no staging deletion, chunk generation, or publication.
If ownership evidence is absent rather than none-active, keep the task unresolved.

## Requirement example and limits

The operator procedure shall select resume or handoff from the declared export
state and verify the required published content before declaring task completion.

The example assumes truthful checkpoint and ownership inspection. It does not
supply a distributed lease protocol, recovery-time objective, or authorization
to rerun an actual production export.
