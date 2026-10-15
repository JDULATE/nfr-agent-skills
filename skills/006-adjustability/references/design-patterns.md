# Existing-control tuning patterns

Identify the actual consumer before choosing a new operating value. Parameter
availability and parameter application are different observations.

## Effective-value trace

- **Use when:** A setting can be overridden, cached, or copied before reaching the
  running operation. Record requested value, applied value, units, scope, and revision.
- **Trade-off:** Extra trace data has upkeep; expose only what distinguishes a
  pending setting from a value already affecting work.
- **How to verify:** Exercise precedence and refresh paths, then match work output
  to the value at its consuming loop rather than the settings store.

## Work-boundary snapshot

- **Use when:** Repeated reads could change a control halfway through a batch or
  operation. Apply a value at the agreed start event and retain it for that work unit.
- **Trade-off:** New values wait for the boundary; immediate application may be
  necessary for some controls. Ask the user which running-work semantics apply.
- **How to verify:** Change the request while work is active; inspect that work's
  applied revision and the next work unit separately.

## Controlled tuning trial

- **Use when:** A desired effect needs comparison of operating values. Hold inputs,
  worker arrangement, and observation method fixed while varying the named control.
- **Trade-off:** A fixture can omit real workload variability; a useful trial does
  not promise the same performance benefit for all operations.
- **How to verify:** Repeat the baseline after the candidate value, inspect effect
  and resource trade-offs, and expose any change in held conditions.

## Reversal evidence

- **Use when:** An operator must undo an adjustment. Use the same effective-value
  path and application event, including any stale override that can defeat reversal.
- **Trade-off:** Reversal of the control need not undo results already produced.
- **How to verify:** Restore the former value, start new work at the agreed boundary,
  and inspect its applied revision and emitted behavior; retain prior-work outcomes.

For an illustrative batch-cap proposal, use 3 records only in a valid domain;
confirm with the user/stakeholder. A useful requirement still needs the real control,
application event, desired effect, and accepted resource trade-offs.
