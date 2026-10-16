# Agreement decisions

Choose the coordination contract before repairing a disagreement.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| List cache returns an older state than the requested revision | Include the revision requirement in cache validation; fetch qualifying authority state or report unresolved | More authority reads or visibly unavailable state | Update authority while holding the old cache and inspect returned values plus revisions |
| A response joins fields from different revisions | Read a supported common snapshot or expose the mixed boundary explicitly | Snapshot support or a weaker advertised result | Interleave field updates and inspect the assembled revision provenance |
| Views use different names for the same domain state | Compare through an explicit equivalence mapping | Mapping changes require domain review | Test equivalent aliases and a genuinely distinct state |
| Cache code updates metadata before updating values | Store state and its revision as one read-model entry under the actual storage mechanism | Requires a suitable update boundary | Inject an interrupted refresh and inspect whether old values can acquire the new revision |

## Revision-qualified read sketch

Illustrative pseudocode for exact-revision fixture reads.

```text
read_view(entity, requested_revision):
    entry = cache.get(entity)
    if entry exists and entry.revision == requested_revision:
        return entry
    source = authority.read_at(entity, requested_revision)
    if source unavailable:
        return Unresolved(requested_revision)
    cache.replace(entity, {revision: source.revision, state: source.state})
    return source
```

Do not assume a real authority supports read_at.
If it cannot retrieve the requested revision, choose a supported contract with
the stakeholder instead of fabricating historical or current data.
The replacement operation needs the repository's real state/metadata boundary.

## Meaning versus freshness

Use the equivalence map only after deciding which revisions may be compared.
A label alias must not excuse an older business state.
An unresolved result records the inability to meet the requested read contract;
it is not a successful agreement sample.
