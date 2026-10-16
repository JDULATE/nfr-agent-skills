# Bounded coverage decisions

Choose the universe and identity rule before changing the traversal.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Output count matches but required identities are absent | Compare identity sets and report duplicate frequencies separately | Requires stable identity and memory or an equivalent comparison procedure | Insert a duplicate plus an omission and inspect both findings |
| Traversal drops the item at a page boundary | Advance the cursor under the documented inclusive/exclusive rule | Cursor changes must preserve ordering assumptions | Exercise the exact boundary with a filled source and expected identities |
| Conditional cases disappear from the expected list | Derive expected membership from the approved condition table, independently of the handler | Expected-set maintenance becomes explicit | Supply a condition-active case the handler currently skips |
| Source changes while pages are read | Use an available snapshot or an agreed reconciliation pass | Snapshot cost or additional reconciliation work | Mutate membership during traversal and check the chosen boundary |

## Coverage sketch

Illustrative pseudocode for stable fixture identities.

```text
counts = frequency(observed_ids)
missing = required_ids - set(counts.keys())
unexpected = set(counts.keys()) - required_ids
duplicates = {id: n for id, n in counts if n > 1}
return {missing: missing, unexpected: unexpected, duplicates: duplicates}
```

Do not let duplicates or unexpected output offset missing identities.
If duplicate output is permitted, keep its count visible but apply the confirmed
duplicate policy separately.

## Representation boundary

For an export, inspect emitted rows rather than only database selection.
For a required case, inspect the specified handling evidence rather than merely
the presence of a branch name.
Completeness of a fixture set does not establish completeness of its source.
