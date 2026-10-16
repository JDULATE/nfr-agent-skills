# Substitution decisions

Use surrounding obligations as the comparison surface, not provider API similarity.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| New provider throws where old caller expects a missing result | Translate provider outcomes in the replacement adapter | Adapter must preserve distinctions without hiding real faults | Compare hit, missing, and actual-fault caller outcomes |
| Old records have keys the replacement does not resolve | Convert keys with a checked mapping and reconcile through caller reads | Migration needs conflict and unmapped-record handling | Read named old keys through the new path; reject ambiguous mappings |
| New path silently falls back to the old provider | Add a retirement gate and test with the old dependency absent | Some formerly masked gaps now block cutover | Remove old binding and execute every named preserved operation |
| Old code cannot read new-format writes | Restrict rollback or supply a verified reverse mapping before enabling writes | Less reversible cutover or extra migration work | Produce a post-cutover record and attempt the actual reverse path |

## Outcome adapter sketch

Illustrative pseudocode for a local caller contract.

```text
get(key):
    result = new_provider.lookup(convert_key(key))
    if result.kind == "found":
        return Present(result.value)
    if result.kind == "absent":
        return Missing
    return BackendFault(result.reason)
```

Do not catch every failure and convert it to Missing.
An unavailable provider and an absent record are different obligations here.
Inspect the old caller contract before choosing any mapping.

## Cutover evidence

Require the named contract cases, old-state reconciliation, and dependency-removal
run to pass before recommending retirement.
Use shadow comparisons without duplicate business effects when possible.
If writes are involved, then specify the actual write authority and state boundary;
this sketch does not establish an atomic migration.
