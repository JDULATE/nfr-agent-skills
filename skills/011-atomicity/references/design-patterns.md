# Visibility-boundary practices

Define the operation and observer contract before selecting a commit mechanism.

## Participating-effect map

- Use when one logical operation changes multiple records or emits external effects.
- Trade-off: a wider unit may cross boundaries the implementation cannot publish
  together. An excluded effect needs its own explicit contract, not silent omission.
- Verify: enumerate writes, messages, external actions, and observers; inspect the
  actual participating commit boundary instead of assuming a function groups commits.

## Private work and publication

- Use when intermediate computation can remain invisible until a completed result is ready.
- Trade-off: staging may add state and cleanup work; publishing a pointer to
  incomplete staged data still exposes a partial operation.
- Verify: interrupt each stage and inspect the normal observer path; only the
  permitted complete before/after view may become visible under the agreed boundary.

## Coherent observer check

- Use when a reader combines several records or independently timed queries.
- Trade-off: read coherence may require a snapshot/version rule; checking only
  writers cannot explain a view assembled across different committed versions.
- Verify: capture each read's version/time and compare with actual committed state;
  distinguish a real partial commit from a mixed-time read of complete states.

## External effects and compensation

- Use when an irreversible or independently committed effect participates in the request.
- Trade-off: an event or staging mechanism may narrow the visible boundary but
  does not automatically make independent recipients observe effects simultaneously.
- Verify: inject failure after external visibility and inspect what was actually
  observed. A compensating action is a new visible effect, not erased history.
