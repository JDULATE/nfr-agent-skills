---
name: reusability
description: >-
  Reuses a shared artifact when asked "decouple the checker from HTTP", "run one validator in web and CLI", or "remove the copied helper". Ask the user if reuse vs broader cases or joined stages is unclear. Not for broadening an abstraction family (see generality) or joining stage contracts (see composability).
---

# Reusability

## Definition and scope

Reusability means an artifact can serve another specified context with bounded
adaptation. Identify the artifact that remains shared, the new consumer, and
the dependencies or assumptions that prevent its use there.
Separate contextual reuse from family-wide abstraction coverage (`generality`)
and preservation of behavior when stages are joined (`composability`).

## Use when / Don't use when

- Apply when an existing checker or helper is copied because another entrypoint
  cannot use it without the original framework or ambient request.
- Include the consuming context's adapter, dependency setup, and allowed edits
  to the shared artifact.
- Route one abstraction's coverage of related cases to `generality`.
- Route a product's distinct task roles to `versatility`.
- Route the behavior of an assembled component chain to `composability`.

## Workflow

1. Clarify: Read artifact code, original callers, imports, ambient state,
   packaging, and consumer docs before specifying reuse.
   Name the existing artifact and the concrete new context.
   If "reuse this" names no consumer or permitted adaptation, then Ask the user
   where it must run and what changes or dependencies are acceptable.

2. Specify: Record artifact identity, preserved contract, new-context inputs,
   adapter responsibilities, dependency assumptions, and adaptation boundary.
   If no budget exists, then propose a labeled illustrative default:
   both contexts call the same shared checker through context-owned adapters,
   without copying its logic; confirm with the user/stakeholder.
   Ask at most three questions about consumer needs, context policy, and allowed
   shared/adapter edits before extracting dependencies.

3. Design/Implement: Read [context-reuse decisions](./references/design-guide.md)
   when removing ambient request access or separating adapters.
   If the artifact reads framework state, then expose only the needed data or
   dependency through a confirmed contract.
   If the new consumer needs different policy, then keep that policy at its
   boundary rather than silently changing the old consumer's behavior.

4. Verify: Invoke the shared artifact from both actual context paths, checking
   outputs, dependencies, and changed files under the declared adaptation boundary.
   If the new path runs a copied implementation, then report duplication rather
   than successful reuse even when outputs happen to match.

5. Report: Return artifact identity, dependency changes, consumer adapters,
   observed results, and adaptation work that remains.
   If only synthetic web/CLI inputs were exercised, then limit the conclusion to
   those contexts rather than promising reuse in arbitrary frameworks.

## Specification patterns

- **New context:** `{artifact_revision}` shall perform `{preserved_operation}`
  in `{new_context}` using `{declared_dependencies}`, verified by
  `{actual_consumer_path_and_contract_fixture}`.
- **Adaptation boundary:** Reusing `{artifact}` across `{contexts}` shall require
  only `{permitted_shared_and_adapter_changes}` while preserving
  `{original_context_contract}`, checked by `{diff_and_identity_inspection}`.

Use the illustrative shared-checker proposal in Specify when no numeric budget
is given; confirm with the user/stakeholder before accepting the adaptation scope.

## Rules of thumb

- Replace ambient context reads with the artifact's actual input needs; passing
  a whole web request into the CLI merely recreates the original dependency.
- Keep input decoding and output presentation in consumer-owned adapters so the
  shared artifact does not accumulate every entrypoint's conventions.
- Treat copied checker logic as a fork, not shared reuse; identify the executable
  artifact each consumer really invokes.

## Verification

Use consumer-path execution, dependency inspection, and source identity review.
Capture both consumers' inputs, outputs, and environment assumptions.
Run the new context without constructing the original framework state.
Check original-context regression cases after shared-boundary changes.
Record actual edited paths and unresolved dependencies rather than inferring
adaptation cost from file count.
Keep failures and original fixture inputs; do not omit hard-to-adapt behavior.
Verify context policy separately from the shared validation operation.
Check that reuse does not grant the new caller unrelated original-context privileges.

## Done checklist

- [ ] Identify the exact artifact and the new consumer context.
- [ ] Define the operation and adaptation boundary.
- [ ] Inventory framework, ambient-state, and policy dependencies.
- [ ] Invoke the shared artifact through both consumer paths.
- [ ] Check new-context execution without original-context setup.
- [ ] Confirm original-context behavior after extraction.
- [ ] Inspect adapters for copied logic and unexpected shared edits.
- [ ] Report remaining dependencies and unmeasured adaptation effort.

## Failure modes

- Copying a function and calling the duplicate reusable.
- Creating a fake web request solely to run a CLI checker.
- Moving every entrypoint convention into the shared module.
- Borrowing the original context's authority as an undeclared reuse dependency.

## References

- Read [context-reuse decisions](./references/design-guide.md) when separating
  ambient dependencies from a reusable artifact.
- Read [web/CLI validator example](./references/worked-example.md) when checking
  shared identity and bounded consumer adaptation.
