# Supported-choice and resolution patterns

Establish actual option meanings from the reader and owner before applying these
choices. A schema is not evidence of live transition behavior.

## Combination contract

- **Use when:** Individually valid keys can express an unsupported combination.
  Validate the resolved document as a whole and identify the conflicting choices.
- **Trade-off:** Rejecting old combinations can break existing documents; retaining
  ignored legacy keys needs an explicit compatibility policy, not silent effectiveness.
- **How to verify:** Pair valid documents with conflicting keys, unknown keys, and
  compatibility inputs; compare accepted meaning with the consumer's observed choice.

## Absence-aware resolver

- **Use when:** Defaults and overrides differ from explicit empty or false values.
  Preserve whether a value was supplied before applying the declared precedence.
- **Trade-off:** More explicit semantics may expose previously ambiguous inputs;
  changing their interpretation needs an owner decision and compatibility evidence.
- **How to verify:** Resolve omitted, empty, false, and competing-source fixtures;
  retain the winning source and reject combinations made invalid by the merge.

## Effective-choice inspection

- **Use when:** Users can supply a valid key that its consumer ignores or overrides.
  Expose the selected value/source at the declared scope without exposing disallowed data.
- **Trade-off:** Resolution evidence has its own access boundary; a diagnostic view
  must not become an unrestricted dump of configuration contents.
- **How to verify:** Change a supported choice, follow it to the actual consumer,
  and compare behavior with the resolved meaning; parsing success alone is insufficient.

An illustrative schema-fixture target is 0 silently accepted unknown keys;
confirm with the user/stakeholder. Some real systems intentionally retain unknown
extension keys; obtain that policy rather than imposing this example universally.
Record supported domains, dependencies, defaults, precedence, scope, effective
observation, compatibility handling, and the owner for each unresolved meaning.
