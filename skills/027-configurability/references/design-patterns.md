# Supported-choice and resolution patterns

Establish actual option meanings from the reader and owner before applying these
choices. A schema is not evidence of live transition behavior.

## Establish a missing runtime setting surface

| Observed evidence | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| A hardcoded value has no supported change path | Give it a scoped location, the existing value as default, a domain check, and a point-of-use reader | An in-memory choice is lost on restart; persistence is an offered extension | Check default behavior, rejection without mutation, and the actual consumer's resolved value |
| No caller or interface is specified | Reuse the existing authorized invocation path, or propose an in-process setter under the same privileges | It offers no new remote administration interface | Invoke through that boundary and check that no new server or external endpoint was added |
| The surface exists but new values must affect active processing | Hand application timing and running-work semantics to `adjustability`; use `reconfigurability` if ownership or arrangement changes | Valid options alone cannot establish safe application | Compare resolved choice with affected work at the chosen boundary |

Settle the location and who may change it before implementation. Keep any new
authentication, persistence, server, or response headers as offered extensions
requiring the user's yes unless already requested. Use applied-value readback
for an unambiguous synchronous consumer; require an applied revision only when
asynchronous or partial application needs change identity across consumers/work.

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
