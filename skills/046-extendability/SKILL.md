---
name: extendability
description: >-
  Plans bounded core changes for added capabilities when users say "add a new
  operation here", "extend the core behavior", "support another result type", or
  "add this without rewriting unrelated modules". Not for additions through an
  already available extension contract (see extensibility) or deployment capacity
  additions (see expandability).
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
   Continue with a scoped design using inspected boundaries, not a fictitious module count.
   If a numeric change-scope limit is missing, then offer the labeled module-count
   example above and confirm with the user/stakeholder; do not optimize that count by concealment.

3. Design/Implement: Read [core-addition patterns](./references/design-patterns.md)
   when choosing an owned branch, internal strategy, or explicit interface evolution.
   If the addition forces unrelated consumers to understand the new operation,
   then reconsider dispatch ownership or expose that expanded impact for acceptance.
   If creating an extension point is itself requested, then record that core change
   here and separate future extension-without-core-edit claims from creating the point.

4. Verify: Exercise the new result, retained operations, unsupported choices, and
   the changed interface's real callers; inspect the complete dependency diff.
   If the addition meets its own test only after old expectations are weakened,
   then report the contract change and resolve it rather than claiming bounded extension.

5. Report: Explain the added capability, touched owner modules, downstream impact,
   old-contract evidence, and outstanding migrations or untested callers.
   If impact escaped the approved surface, then name the extra owners and decisions
   instead of reporting only the modules that were convenient to count.

## Specification patterns

- **Capability addition:** The core shall support `{new_operation}` producing
  `{new_result_contract}` under `{input_conditions}`, through changes restricted
  to `{approved_owner_surface}`, verified by `{new_and_retained_operation_cases}`.
- **Impact bound:** Adding `{capability}` shall require no more than
  `{confirmed_change_scope}` under `{declared_counting_rule}`, measured from
  `{full_dependency_and_consumer_diff}` including `{approved_exceptions}`.
- **Interface evolution:** Existing consumers of `{old_operation}` shall retain
  `{old_meaning_and_error_contract}` after `{explicit_interface_change}`, checked
  against `{consumer_and_migration_matrix}`.

Treat the example module limit as illustrative scope negotiation; confirm with the
user/stakeholder. Ask the user when ownership or compatibility obligations are unknown.

## Rules of thumb

- Do place the new operation's dispatch decision with its owning core boundary;
  don't spread new result-type checks into every unrelated consumer.
- Do make an added operation explicit in its input and result contract; don't
  overload an existing mode so that old callers unknowingly request new behavior.
- Do price the new operation's interface fan-out, including old callers it would
  require to branch; don't equate an owner-local implementation with a narrow addition.
- Do preserve original-operation cases alongside new ones; don't redefine the old
  result to avoid implementing a genuinely distinct capability.
- Do separate creating a hook from using it later; don't count the hook-creation
  core edits as evidence that the first addition required no core change.
- Don't merge unrelated responsibilities into a large module to satisfy a module
  count; keep owner impact and semantic changes visible under the counting rule.

## Verification

Use change-impact review, interface-contract tests, and consumer integration checks.
Trace new dispatch branches to their owning implementations and inspect generated
adapters or migrations that a production-only file count might omit. Run old callers
without teaching them the new operation, then exercise supported and rejected new
inputs. Record affected owners and interface meanings alongside changed files;
an isolated new-operation demonstration does not establish bounded core impact.

## Done checklist

- [ ] Establish that the requested addition needs a core or interface change.
- [ ] Name the new operation and its result contract separately from old behavior.
- [ ] Identify approved owner boundaries and a transparent scope-counting rule.
- [ ] Map transitive callers and any required interface migration.
- [ ] Verify retained operations without weakening their old meaning.
- [ ] Exercise the new operation and unsupported operation choices.
- [ ] Report all actual owner impact, exceptions, and remaining consumer evidence.

## Failure modes

- Editing core code although an existing attachment contract already fits the addition.
- Hiding a new capability behind an old mode with changed result meaning.
- Claiming a narrow addition while omitting generated adapters or external callers.
- Gaming module count by consolidating unrelated responsibilities before measuring.

## References

- Read [core-addition patterns](./references/design-patterns.md) when selecting
  dispatch ownership, interface changes, and a defensible change-scope measure.
- Read [receipt-operation example](./references/worked-example.md) when adding
  an explicit core capability while retaining the original callers' result meaning.
