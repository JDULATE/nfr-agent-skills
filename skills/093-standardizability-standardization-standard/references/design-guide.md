# Common-convention adoption decisions

These are repository-local design choices, not invented external standards.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Two event producers use different names for the same confirmed concept | Define a canonical field with meaning and a named selection owner | Producers and documentation need coordinated changes | Compare actual emitted artifacts with the selected concept mapping |
| A shared name represents different concepts | Split or qualify the fields before selecting vocabulary | Larger vocabulary instead of superficial uniformity | Use fixtures where the concepts differ and confirm both remain expressible |
| Legacy consumers depend on old field names | Translate at a declared adoption boundary and register its retirement condition | Transitional mappings must be owned and maintained | Feed canonical output through the mapping and compare the legacy result |
| Some producers cannot migrate yet | Keep explicit scoped exceptions with an owner and condition for revisiting | Adoption remains partial | Enumerate adopted and excepted outputs without claiming universal coverage |

## Adoption sketch

Illustrative pseudocode for a proposed local event convention.

```text
emit_task_started(task_key):
    return {kind: "task_started", task_key: task_key}

to_legacy_board(event):
    if event.kind == "task_started":
        if not event.contains("task_key"):
            return MissingTaskIdentity
        return {event_name: "task.begin", job: event.task_key}
    return UnsupportedEvent
```

Choose names only after confirming task_key and the legacy job field denote
the same task identity in this boundary.
A similarly spelled field for a scheduled job definition may require a separate
concept; do not erase that distinction for a shorter mapping.

## Approval and maintenance

Record the selecting role and current decision state with the convention.
When a producer is excepted, specify the migration condition and owning role.
A local checker can identify departures after selection; it cannot approve the
selection or prove that every consumer agrees with its meaning.
