# Status projection decisions

Use a status view to expose known state, not to invent diagnostic explanations.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| A query returns the latest job across all teams. | Filter by verified actor scope and requested subject using the existing access rule. Some requests correctly return no projection. | Supply a newer unrelated job and verify it cannot replace the requested one. |
| The page looks fresh but its source is old. | Show observation time and apply a confirmed freshness rule. Users may see stale rather than a reassuring live label. | Hold the source unchanged while advancing view time. |
| Missing records display queued by default. | Add explicit unknown and query-failure presentations. More view states need handling. | Remove the subject's projection and inspect the displayed result. |
| A progress estimate looks like confirmed completion. | Label estimate and observed counter separately. The display becomes less compact. | Change an estimate without changing committed work and verify the observed counter stays fixed. |
| A late projection overwrites a terminal result. | Use source revision/ordering semantics to select the observation. The source must define its ordering. | Deliver an older projection after the terminal one and inspect the selected state. |

## Scoped view sketch

```text
subject = resolve_requested_subject(request)
require existing_policy_allows(actor, subject)
row = read_projection(subject.identity, actor.scope)
if row is absent: return visible_unknown(subject)
if observation_time_not_comparable(row): return visible_unknown(subject)
if older_than_confirmed_freshness(row):
  return visible_stale(subject, row.state, row.observed_at)
return visible_observation(subject, row.state, row.progress, row.observed_at)
```

Do not substitute the latest global row in any missing-source branch.
The sketch consumes a confirmed access policy; it does not decide new permissions.

If a freshness budget has not been selected, expose the observation time and
ask for that decision instead of manufacturing a "live" claim.
