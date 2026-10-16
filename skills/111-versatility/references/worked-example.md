# Inventory intake and discrepancy audit

This synthetic product uses illustrative role and effect criteria;
confirm with the user/stakeholder before adopting them.

## Filled role record

| Input | Value |
| --- | --- |
| Product | inventory-tool revision birch |
| Role entrypoints | import and audit in the same product |
| Initial inventory | {cedar:5} |
| Import input | {maple:3} |
| Import semantics | upsert supplied quantities; preserve other keys |
| Import expected result | Imported(maple), inventory {cedar:5,maple:3} |
| Audit input | expected {cedar:5,maple:4} |
| Audit semantics | compare the exact supplied key set without mutating inventory |
| Audit expected report after import | [{key:maple, expected:4, actual:3}] |
| Carried role context | import may write; audit must construct a read-only context |
| Initial report state | absent |
| Owner | inventory-tool maintainer role |

Quantities are illustrative fixture values;
confirm with the user/stakeholder before using them as acceptance cases.

## Before: audit is an import alias

After a valid import, inventory is {cedar:5,maple:3}.
The old audit path calls import_records(expected) before comparing.
It changes maple to 4, then reports [].
The result both hides the discrepancy and violates the read-only role contract.

A renamed command alone has not added a valid checking role.

## Remediation and after carried state

Use separate import and discrepancy handlers with explicit role context.

```text
start inventory: {cedar:5}
run import({maple:3}):
  result = Imported(maple)
  inventory = {cedar:5,maple:3}
  role context ends

run audit(expected={cedar:5,maple:4}):
  context = read-only
  report = [{key:maple, expected:4, actual:3}]
  inventory = {cedar:5,maple:3}
```

The audit uses the inventory carried from import but does not inherit write
permission or modify that state.
Both tasks run through inventory-tool revision birch.

## Failing role-context control

Keep the new audit handler, but let a stale import flag trigger an upsert
before comparison.
Inventory again becomes {cedar:5,maple:4}, so the state-diff check fails even
if the output formatter displays an audit label.

## Separate-task acceptance

Import is accepted by its upsert result and preserved cedar value.
Audit is accepted by the maple discrepancy and unchanged inventory.
The same output file format or shared helper would not establish those distinct
outcomes by itself.

## Limits

The example covers a declared key set and sequential tasks only.
It does not define missing-key behavior, parallel import/audit operation,
access-control enforcement, or every inventory workflow.
