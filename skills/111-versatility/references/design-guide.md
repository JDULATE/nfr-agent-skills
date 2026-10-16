# Distinct-role support decisions

Use task-specific acceptance criteria instead of counting modes.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Audit mode calls import before comparing expected values | Introduce a read-only discrepancy handler | Separate task logic must be maintained | Compare inventory before/after audit with a known discrepancy |
| Command aliases share one outcome but are called separate roles | Define roles by user task and expected effects | Fewer claimed roles than menu entries | Map each command to a materially different acceptance question |
| Import context leaves a write flag active for the next task | Construct role-scoped execution context or clear carried capabilities | Context handoff becomes explicit | Run audit immediately after import and inspect writes |
| Claimed roles live in different standalone products | Bound the claim to the actual shared product or integrate supported entrypoints | Product scope may need clarification | Trace each task through the declared product revision |

## Role-dispatch sketch

Illustrative pseudocode for a local inventory tool.

```text
run(task, input, inventory):
    if task == "import":
        return import_records(input, inventory)
    if task == "audit":
        snapshot = inventory.read_snapshot()
        return compare_expected(input, snapshot)
    return UnsupportedTask
```

The audit path must not pass its expected records into the import handler.
The snapshot's actual read-only behavior still needs implementation evidence.

## Role boundary

Import accepts a state change; audit accepts a discrepancy report without that
change. Reusing low-level helpers may be appropriate, but it does not eliminate
the distinction between the tasks' contracts.
Keep concurrency and privileged write access outside the claim unless checked.
