---
name: extendability
description: >-
  Plans bounded core changes or builds missing extension hooks when users say "we need a hook before adding plugins", "this format needs core changes", or "add an operation the core cannot handle". Not for using an existing hook (see extensibility) or admitting resources (see expandability).
---
# Extendability

## Definition and scope

Extendability means a new capability can be added by changing existing core source
or interfaces within an agreed change surface. Follow this repository's core-edit
convention, distinguishing additions through an existing hook (`extensibility`)
and greater deployment capacity (`expandability`).

## Use when / Don't use when

- Apply when the requested new operation has no usable existing attachment contract
  and a core implementation or interface must change to provide it.
- Examine the owned change surface, existing consumer behavior, and new result contract.
- Route an addition that already fits a supported hook to `extensibility`.
- Route a better result for the same accepted operation to `enhanceability`, and
  broad ongoing repair effort without a new capability to `maintainability`.

## Workflow

1. Clarify: Inspect the core code, public-interface docs, dispatch paths, existing
   hooks, dependency ownership, and consumer tests before prescribing an addition.
   Identify the requested new result and the owner modules that currently prevent it.
   If a documented extension contract already supports the request, then route
   that addition to `extensibility` instead of assuming core edits are necessary.

2. Specify: Define new inputs/results, preserved old cases, approved interface
   changes, core-edit scope, migration obligations, and evidence of bounded impact.
   If the user seeks an implementation improvement, propose this change record:

   ```text
   Illustrative core-change envelope; confirm with the user/stakeholder:
   Addition: the requested new operation with a separately stated result contract.
   Change-scope target: touch at most 2 owner modules in the example fixture.
   Counting rule: declare which production modules count; list adapters/tests/docs separately.
   Preserved cases: named existing requests, result meanings, and public caller obligations.
   Interface: explicit approval of new fields or operation choices; no silent reinterpretation.
   Evidence: dependency diff, new-operation cases, old-consumer checks, migration record.
   Open items: actual owner boundaries, accepted scope limit, and consumer coordination.
   ```

   Ask at most three groups of questions: what new behavior is required; which old
   callers or meanings must remain; and which modules or interface changes are permitted.
   If a numeric change-scope limit is missing, then offer the labeled module-count
   example above and confirm with the user/stakeholder; do not optimize that count by concealment.

3. Design/Implement: Read [core-addition patterns](./references/design-patterns.md)
   when choosing dispatch ownership; use the receipt example's owner/interface ledger
   when reconciling core edits with external coordination.
   If the addition forces unrelated consumers to understand the new operation,
   then reconsider dispatch ownership or expose that expanded impact for acceptance.
   If creating an extension point is itself requested, then record that core change
   here and separate future extension-without-core-edit claims from creating the point.

4. Verify: Exercise the new result, retained operations, unsupported choices, and
   the changed interface's real callers; inspect the complete dependency diff.
   If the addition meets its own test only after old expectations are weakened,
   then report the contract change and resolve it rather than claiming bounded extension.

5. Report: Return the owner/interface ledger, operation checks, and migration gaps.
   If impact escaped the approved surface, then name the extra owners and decisions
   instead of reporting only the modules that were convenient to count.

## Specification patterns

- **Capability addition:** The core shall support `{new_operation}` producing
  `{new_result_contract}` under `{input_conditions}`, through changes restricted
  to `{approved_owner_surface}`, verified by `{new_and_retained_operation_cases}`.
- **Impact bound:** Adding `{capability}` shall stay within `{confirmed_owner_surface}`
  under `{counting_rule}`, verified by `{full_diff}` including `{approved_exceptions}`.
- **Interface evolution:** Existing consumers of `{old_operation}` shall retain
  `{old_meaning_and_error_contract}` after `{explicit_interface_change}`, checked
  against `{consumer_and_migration_matrix}`.

Confirm the illustrative scope with the user/stakeholder; Ask the user which owners count.

## Rules of thumb

- Do trace the new core operation from selector to owning implementation and callers;
  consumer branches added to compensate for missing dispatch widen its addition surface.
- Do assign the new result an explicit operation contract; reinterpreting the old mode
  changes an existing capability instead of demonstrating that the core admits another.
- Do include transitive caller and adapter edits in the new-operation impact ledger;
  an owner-local renderer is not a bounded addition when each consumer must learn its type.
- Do exercise retained requests through the modified dispatcher; weakening those
  cases to accept the new result substitutes a replacement for the claimed addition.
- Do count hook creation in this addition's core surface and name what it admits;
  a future unchanged-core plugin path does not erase the work needed to create it.

## Verification

Use change-impact review, interface-contract tests, and consumer integration checks.
Trace new dispatch branches to their owning implementations and inspect generated
adapters or migrations that a production-only file count might omit. Run old callers
without teaching them the new operation, then exercise supported and rejected new
inputs. Record affected owners and interface meanings alongside changed files;
an isolated new-operation demonstration does not establish bounded core impact.

## Done checklist

- [ ] Confirm from hook code/docs why this result cannot use an existing contract.
- [ ] Exercise the distinct new operation and reject unsupported operation choices.
- [ ] Replay old requests through the changed dispatcher with retained expectations.
- [ ] Trace new dispatch branches to their declared owners rather than caller patches.
- [ ] Reconcile the owner/interface ledger with production, generated, and consumer diffs.
- [ ] Check any required consumer migration against its explicitly accepted contract.
- [ ] Compare actual addition impact with the confirmed surface and expose exceptions.

## Failure modes

- Editing core code although an existing attachment contract already fits the addition.
- Hiding a new capability behind an old mode with changed result meaning.
- Claiming a narrow addition while omitting generated adapters or external callers.
- Gaming module count by consolidating unrelated responsibilities before measuring.

## References

- Read [core-addition patterns](./references/design-patterns.md) when selecting
  dispatch ownership, interface changes, and a defensible change-scope measure.
- Read [receipt-operation example](./references/worked-example.md) when adding
  a core capability and comparing its owner/interface ledger with the full diff.
