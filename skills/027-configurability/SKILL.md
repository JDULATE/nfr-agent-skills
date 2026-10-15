---
name: configurability
description: >-
  Defines supported settings and valid combinations when users say "make it
  configurable", "expose the available settings", or "validate this
  configuration file". Covers defaults, precedence, scope, and effective
  choice without source edits. Not for tuning an existing control (see
  adjustability), applying a stateful arrangement change (see
  reconfigurability), or adding user-defined behavior (see customizability).
---
# Configurability

## Definition and scope

Configurability means offering explicit valid choices without requiring source
edits. Specify option meanings, defaults, precedence, scope, and effective results;
separate tuning an exposed control (`adjustability`), applying another arrangement
(`reconfigurability`), and stakeholder-authored behavior (`customizability`).

## Use when / Don't use when

- Apply when supported settings are hidden, ambiguous, silently ignored, or allow
  combinations that do not express a supported operating choice.
- Route selecting values to fit a named team's needs to `tailorability`.
- Route application timing or running-state migration to `reconfigurability`;
  accepting a configuration document does not prove that transition succeeded.

## Workflow

1. Clarify: Read setting readers, default/override code, schema docs, sample
   configurations, and consumers before defining a supported option space.
   If the requested behavior cannot be expressed by existing meanings, then Ask
   the user whether a new built-in option or `customizability` is intended.

2. Specify: Record each key's type, units, allowed values, dependencies, absence
   meaning, precedence, scope, effective observation, and invalid-input response.
   If a practical settings improvement is requested, then propose this record:

   ```text
   Illustrative choice contract; confirm with the user/stakeholder:
   Scope: inspected keys and documented combinations; no invented production ranges.
   Defaults: explicit absent-key meaning at the recorded configuration revision.
   Resolution: existing precedence made visible; conflicts lacking policy stay open.
   Example bound: 0 silently accepted unknown keys in the selected schema fixture.
   Invalid input: reject with key/reason under the proposed fixture policy.
   Evidence: valid/invalid documents, resolved values and their winning sources.
   Open items: real domains, compatibility exceptions, owner and accepted defaults.
   ```

   Ask at most three questions about needed choices; defaults/precedence/scope;
   and invalid combinations or compatibility exceptions. Proceed to a schema and
   resolver design while unconfirmed option meanings remain proposals.
   If no target is provided, then offer the illustrative unknown-key bound and
   confirm with the user/stakeholder before treating it as the accepted policy.

3. Design/Implement: Read [choice patterns](./references/design-patterns.md) when
   defining combinations, absence semantics, or effective-choice evidence.
   If values merge across sources, then resolve them with one stated rule rather
   than relying on which consumer reads which file first.
   If applying a valid value moves running work, then separate the transition
   contract under `reconfigurability` from schema validity here.

4. Verify: Exercise supported documents, invalid combinations, omitted keys,
   explicit empty values, and competing sources through the actual reader.
   If a setting is accepted but never influences its declared consumer, then
   report that unsupported or misleading choice rather than claiming configurability.

5. Report: Return the option contract, winning-source evidence, rejection cases,
   compatibility exceptions, and choices whose effective result is unverified.
   If only schema validation ran, then distinguish it from observed consumer
   behavior and withhold live-application claims.

## Specification patterns

- **Choice space:** `{configuration_surface}` shall express `{supported_choices}`
  under `{domains_and_dependencies}`, rejecting `{invalid_combinations}` with
  `{accepted_response}`, verified by `{reader_and_combination_cases}`.
- **Resolution:** For `{competing_sources}`, `{keys}` shall resolve according to
  `{precedence_and_absence_rules}`, evidenced by `{effective_value_source_trace}`
  and `{consumer_behavior_probe}` at `{declared_scope}`.

Use the illustrative unknown-key proposal only with stakeholder confirmation;
confirm with the user/stakeholder. Ask the user for unknown domains or precedence.

## Rules of thumb

- Do distinguish absent, explicit empty, and explicit false values before merging;
  treating them alike can remove a supported choice while the schema still accepts it.
- Do validate dependent keys as an option combination; silently repairing a conflict
  makes the displayed choice differ from the supported behavior the user selected.
- Do bind omitted-key defaults to a declared configuration meaning; an unrelated
  code fallback changing that meaning silently changes the offered choice space.
- Do expose the winning source for an effective option; showing every supplied
  value without resolution cannot explain which supported choice the consumer used.
- Do keep built-in option selection separate from user-authored logic; an embedded
  executable script is not merely another setting when its behavior has no built-in meaning.
- Don't advertise an ignored compatibility key as effective; retaining its syntax
  for old documents does not make its requested behavior a currently supported choice.

## Verification

Use schema/combination tests, resolver inspection, and consumer integration checks.
Compare omitted, empty, false, conflicting, and overridden values at the declared
scope. Inspect accepted-but-unused settings and resolution mismatches; successful
parsing alone cannot establish that the documented choice is actually available.

## Done checklist

- [ ] Exercise each agreed key domain and a rejected combination through the reader.
- [ ] Distinguish absent/empty/false inputs in resolved results.
- [ ] Resolve competing sources under the confirmed precedence rule.
- [ ] Observe the selected value at its declared consumer and scope.
- [ ] Compare omitted-key behavior with the declared default meaning.
- [ ] Inspect unknown and compatibility keys under their explicit policy.

## Failure modes

- Offering settings that parse but are ignored by their claimed consumers.
- Silently changing a default while calling the option contract unchanged.
- Repairing an invalid combination without exposing the changed effective choice.
- Treating a source-precedence accident as the documented resolution rule.
- Claiming a valid configuration proves its stateful application succeeded.

## References

- Read [choice patterns](./references/design-patterns.md) when defining supported
  combinations, source resolution, absence, or consumer evidence.
- Read [resolver example](./references/worked-example.md) when checking concrete
  omitted, overridden, and conflicting choices without inventing an option domain.
