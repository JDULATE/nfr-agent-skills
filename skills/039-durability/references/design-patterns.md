# Acknowledged-state practices

Verify the actual persistence promise rather than selecting a storage label.

## Write-to-acknowledgement map

- Use when an API response or UI confirmation claims a completed save.
- Trade-off: waiting for the required persistence condition can affect latency;
  a weaker early acknowledgement must not retain a stronger confirmed-save meaning.
- Verify: trace state identity, persistence condition, and response ordering;
  inspect the implementation/config rather than assuming a flush or replica label suffices.

## Event-scoped copy dependencies

- Use when replicas, journals, snapshots, or backups support the preservation claim.
- Trade-off: more copies can add recovery options while sharing a loss boundary
  or lacking the latest acknowledged state. Copy quantity does not resolve either issue.
- Verify: map copy content/version, confirmation state, and dependencies against
  the named event; disclose loss models not exercised by the trial.

## Independent acknowledged oracle

- Use when testing loss could remove the tested component's own expected-state record.
- Trade-off: an external ledger adds observation work and may have incomplete
  acknowledgement visibility; ambiguous responses need their own classification.
- Verify: record acknowledged identity/version/contents outside the loss boundary,
  then compare authoritative post-event retrieval with the confirmed expected set.

## Supersession and retrieval authority

- Use when valid later writes or stale readers can resemble lost acknowledged data.
- Trade-off: a latest-value contract need not preserve queryable historical versions;
  do not add version-history retention unless the user requires it.
- Verify: track legitimate supersession and read authority; compare the required
  current contents or historical versions according to the actual promise.
