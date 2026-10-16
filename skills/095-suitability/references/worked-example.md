# Existing export fitted to an offline importer

This synthetic task, local format, and fit criteria are illustrative;
confirm with the user/stakeholder before adopting them.

## Filled handoff record

| Input | Value |
| --- | --- |
| Task | move inventory rows into the existing offline stock importer |
| Source rows | [{sku:pen, units:2}, {sku:book, units:0}] |
| Existing export capability | emit a structured object behind a remote retrieval token |
| Existing output | RemoteArtifact(cedar), containing the source rows |
| Receiver | fixture line importer, network unavailable |
| Required local format | header sku|units; each following line has sku then integer units |
| Separator/line contract | pipe separator, newline terminator, no escaping supported |
| Accepted source domain | nonempty sku without pipe/newline; units are nonnegative integers |
| Manual workarounds | no re-entry; receiver replacement not accepted |
| Receiver initial state | staged_rows=[] |
| Required received rows | exactly the source rows, preserving zero |
| Owner | inventory-handoff maintainer role |

All quantities are illustrative fixture values;
confirm with the user/stakeholder.

## Before task-fit failure

Export returns RemoteArtifact(cedar) successfully.
The offline importer cannot retrieve it and returns LocalArtifactRequired.
staged_rows remains [].
Capability presence does not fit the declared handoff.

Manually typing the rows into a file would change the accepted workflow.
That workaround is not evidence that the original capability met the fit criterion.

## Remediation and after state

Add the constrained local adapter and retain the existing receiver.

```text
local artifact:
  sku|units
  pen|2
  book|0
  [final newline present]

receiver output:
  [{sku:pen, units:2}, {sku:book, units:0}]
staged_rows:
  [{sku:pen, units:2}, {sku:book, units:0}]
network calls: []
manual re-entry: none
```

The named task now has a compatible artifact path and preserved field meaning.
This is not evidence of real-world adoption or reconciliation success.

## Failing value and separator controls

A mutant omits rows whose units evaluate as false.
It emits only pen|2; the importer stages only pen, so the task-essential book row
and its valid zero value are lost despite parse success.

Reset staged_rows=[] and supply [{sku:"pen|blue", units:2}].
The adapter returns UnsupportedField before emitting an artifact.
staged_rows stays []; no silent renaming or guessed escaping occurs.

## Limits

The example covers the filled receiver and restricted source domain.
It does not define arbitrary text encoding, general delimited-file support,
missing fields, or suitability for other receiving tools.
