---
name: versatility
description: >-
  Supports distinct task roles when asked "import and audit stock", "add read-only checking", or "keep audits nonmutating". Ask the user which roles differ in outcomes, rather than input variants, before routing new uses. Not for one abstraction covering related cases (see generality) or reusing an artifact elsewhere (see reusability).
---

# Versatility

## Definition and scope

Versatility means one product or component serves multiple distinct task roles.
Define the outcome, inputs, and permitted effects of each role rather than
counting modes or menu items.
Separate task diversity from related-case abstraction coverage (`generality`)
and using an artifact in another context (`reusability`).

## Use when / Don't use when

- Apply when the same tool must perform intake and inspection tasks with
  different acceptance criteria and state effects.
- Include the role boundary, shared product identity, and transitions of task context.
- Route an existing checker used from another entrypoint to `reusability`.
- Route a common abstraction covering related input cases to `generality`.
- Route merely adding a named operation to `functionality` when no distinct-role
  acceptance question has been established.

## Workflow

1. Clarify: Read the product's commands, handlers, state model, role docs, and
   existing task evidence before specifying another role.
   Identify the materially different outcome each role serves.
   If the request is only "do more," then Ask the user which task roles must
   share the product and what makes their acceptance criteria distinct.

2. Specify: Record the product boundary, roles, inputs, outputs, permitted
   mutations, shared resources, and role-context reset behavior.
   If no target is provided, then propose a labeled illustrative default:
   the same product supports named intake and read-only audit tasks with separate
   outcome/effect checks; confirm with the user/stakeholder.
   Ask at most three questions about role outcomes, allowed effects,
   and shared context before adding a task path.

3. Design/Implement: Read [role-support decisions](./references/design-guide.md)
   when separating role handlers and mutation permissions.
   If a checking role must be read-only, then provide its own comparison path
   rather than reusing an import path that writes the expected values.
   If switching roles leaves previous task state active, then reset or explicitly
   transfer the permitted context before executing the next task.

4. Verify: Execute each role through the same declared product, checking its
   result and actual state effects independently.
   If both modes call the same behavior with different labels, then report the
   missing task distinction rather than accepting mode count as versatility.

5. Report: Return the role matrix, product entrypoints, task outcomes, mutation
   evidence, and role-context limitations.
   If only sequential import/audit operation was checked, then withhold claims
   about arbitrary workflows, concurrent roles, or reuse in another product.

## Specification patterns

- **Role outcomes:** `{product}` shall support `{distinct_roles}`, each producing
  `{role_specific_result}` under `{inputs_and_conditions}`, verified by
  `{role_matrix_and_actual_entrypoint_checks}`.
- **Effect boundary:** In role `{read_only_or_mutating_role}`, the system shall
  permit `{declared_effects}` and preserve `{protected_state}`, including after
  `{previous_role}`, checked by `{sequential_before_after_state_fixture}`.

Use the illustrative intake/audit proposal in Specify when no numbers are given;
confirm with the user/stakeholder before treating role diversity as accepted.

## Rules of thumb

- Count distinct accepted tasks, not switches or output labels; two import aliases
  do not establish an independent inventory-audit role.
- Keep a read-only role from implementing its result by performing the mutating
  role first; an audit that repairs stock has changed the task it was meant to serve.
- Verify that the roles belong to the declared product boundary; separate tools
  in a catalogue do not by themselves make either tool versatile.
- Make role-context handoff explicit; an audit must not inherit an import flag
  that authorizes writing its comparison input into the inventory.

## Verification

Use role-specific task fixtures, state-diff inspection, and sequential role checks.
Capture the product revision and actual handler reached by each entrypoint.
Check output correctness and permitted effects separately for each role.
Retain role-specific failures rather than averaging a favorable combined result.
Exercise the checking role after intake with known carried inventory state.
Inspect context flags or capabilities that may survive the role switch.
Do not infer performance or usability across roles from the presence of commands.

## Done checklist

- [ ] Define materially distinct roles and their outcomes.
- [ ] Identify the shared product or component serving those roles.
- [ ] Record each role's permitted state effects.
- [ ] Run the actual entrypoint for every named role.
- [ ] Compare each role's result with its own acceptance criteria.
- [ ] Inspect carried context and state after sequential roles.
- [ ] Report unsupported role combinations and untested concurrency.

## Failure modes

- Counting aliases of one task as different roles.
- Implementing audit by importing expected records before comparison.
- Reporting a suite of separate tools as one versatile component.
- Leaving a mutating task flag active when entering a read-only role.

## References

- Read [role-support decisions](./references/design-guide.md) when designing
  distinct task handlers and role-context boundaries.
- Read [inventory intake/audit example](./references/worked-example.md) when
  checking different outcomes and effects in the same product.
