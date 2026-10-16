---
name: wrappability
description: >-
  Wraps retained behavior when asked "keep an engine behind an API", "translate native errors", or "expose an old function". Ask the user whether the implementation and required behavior stay unchanged before routing adapter work. Not for substituting the engine (see replaceability) or just wiring components (see integratability).
---

# Wrappability

## Definition and scope

Wrappability means an adapter can expose an existing implementation through a new
boundary while preserving the required original behavior. Identify what remains
unchanged and what the adapter translates.
Separate wrapping the retained implementation from substituting it
(`replaceability`) and the effort of wiring components (`integratability`).

## Use when / Don't use when

- Apply when a retained legacy engine needs a structured entrypoint or interface
  without rewriting its implementation.
- Include input translation, original outcomes, native effects, and unsupported
  capabilities at the new boundary.
- Route retirement of the old implementation to `replaceability`.
- Route overall connection work without a boundary-preservation question to
  `integratability`.
- Route new behavior admitted by a supplied hook to `extensibility`.

## Workflow

1. Clarify: Read the native public entrypoint, result/error handling, state
   effects, callers, and proposed boundary docs before specifying a wrapper.
   Identify required native behavior and any unsupported new-boundary promises.
   If the user only asks for an adapter, then Ask the user whether the original
   implementation remains in place and which obligations must survive.

2. Specify: Record native implementation identity, supported operations,
   input/output mapping, error distinctions, effect equivalence, and refusal rules.
   If no target exists, then propose a labeled illustrative default:
   mapped requests preserve native results and effects with no implicit replay;
   confirm with the user/stakeholder.
   Ask at most three questions about retained behavior, new-boundary semantics,
   and forbidden changes before designing translation.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [wrapper decisions](./references/design-guide.md)
   when choosing public-operation mapping and result envelopes.
   If the native component cannot supply a requested capability, then expose
   that limitation instead of fabricating success.
   If a call can mutate state and repetition is not established as safe, then
   avoid automatic replay and preserve an indeterminate result when appropriate.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Compare native and wrapped calls from equivalent initial states,
   checking results, failures, call counts, and actual state effects.
   If the wrapper changes the native source or invokes private internals, then
   disclose that change and reassess the unchanged-implementation boundary.

5. Report: Return the native/wrapper identity map, translations, comparison
   evidence, unsupported requests, and remaining effect risks.
   If only direct local calls were checked, then withhold claims about remote
   delivery guarantees or safe recovery from ambiguous completion.

## Specification patterns

- **Behavior preservation:** For `{native_operation_and_supported_inputs}`,
  `{new_boundary}` shall preserve `{mapped_results_and_state_effects}` while
  retaining `{native_implementation_revision}`, verified by
  `{equivalent_state_native_and_wrapper_comparison}`.
- **Failure/refusal:** `{native_outcomes_and_unsupported_requests}` shall become
  `{distinct_boundary_outcomes}` without `{extra_native_effects}`, checked by
  `{negative_cases_and_call_trace}`.

Use the illustrative no-replay preservation proposal in Specify when numbers
are absent; confirm with the user/stakeholder before accepting the mapping.

## Rules of thumb

- Translate native outcomes by their actual meaning; a missing item and a failed
  engine call must not collapse into a successful structured response.
- Invoke the retained public operation rather than duplicating its business
  logic in the wrapper; duplicated behavior can diverge while the engine remains idle.
- Keep wrapper retries from repeating an unproven-safe native mutation;
  an attractive new interface must not silently reserve the same stock again.
- Refuse unsupported boundary requests before invoking the engine; inventing an
  asynchronous or bulk success does not expose a capability the native operation lacks.

## Verification

Use native-versus-wrapper contract fixtures, source identity inspection, and
effect/call tracing. Reset state between comparison cases.
Check valid requests, native rejection, invalid boundary inputs, and unsupported
options. Retain failed and ambiguous outcomes.
Inspect serialization and result mapping through the actual new entrypoint.
Count native invocations alongside state changes to detect hidden replay.
Confirm native-source identity from the repository diff.
Do not equate a new envelope with preserved behavior or remote safety.

## Done checklist

- [ ] Identify the retained implementation and native public operation.
- [ ] Map supported inputs and distinct native outcomes.
- [ ] Compare native and wrapped success effects from equivalent state.
- [ ] Exercise rejection without fabricating success.
- [ ] Check invalid and unsupported requests before native invocation.
- [ ] Inspect call traces for duplicate mutations.
- [ ] Confirm the stated unchanged-source boundary.
- [ ] Record untested remote or ambiguous-completion behavior.

## Failure modes

- Reimplementing native business logic inside an apparently thin wrapper.
- Mapping every native response to a generic success envelope.
- Replaying a mutating native call without an established replay contract.
- Promising a capability absent from the retained implementation.
- Editing private native logic while reporting an unchanged engine.

## References

- Read [wrapper decisions](./references/design-guide.md) when translating public
  operations, distinct failures, and unsupported requests.
- Read [reservation-wrapper example](./references/worked-example.md) when comparing
  effects of a retained engine and a new structured entrypoint.
