---
name: structuredness
description: >-
  Enforces dependency organization when tickets say "domain code imports the web layer", "these imports violate our layer rules", or "the package layout hides a cycle". Not for finding separable responsibilities (see decomposability) or matching peer conventions (see uniformity).
---

# Structuredness

## Definition and scope

Structuredness means elements and dependencies follow an explicit organization
that can be inspected. Express the organizing rule as actual responsibilities,
allowed relationships, and checked boundaries.
Separate organization from establishing separable parts (`decomposability`)
and consistent presentation among peers (`uniformity`).

## Use when / Don't use when

- Apply when imports, runtime calls, or ownership relationships violate a chosen
  layer or package organization.
- Include source organization and the actual dependency graph, not folder names alone.
- Route discovering independent responsibilities to `decomposability`.
- Route removing unnecessary mechanisms to `simplicity`.
- Route matching naming style across otherwise valid peers to `uniformity`.

## Workflow

1. Clarify: Read architecture docs, package responsibilities, imports,
   composition roots, and runtime dependencies before selecting checks.
   Identify the intended direction of relationships and evidence of violations.
   If no organization has been chosen, then Ask the user which responsibilities
   and dependency rules the system should follow rather than imposing a favorite style.

2. Specify: Record elements, role membership, allowed edge types and directions,
   exceptions, and the graph boundary being checked.
   If no target exists, then propose a labeled illustrative default:
   the named graph obeys its confirmed dependency rules with exceptions exposed;
   confirm with the user/stakeholder.
   Ask at most three questions about intended roles, permitted relationships,
   and exceptional dependencies before reorganizing source.

3. Design/Implement: Read [organization decisions](./references/design-guide.md)
   when relocating translation, changing dependency direction, or checking cycles.
   If domain code imports a delivery adapter, then place delivery translation
   at the boundary or introduce an appropriate domain-owned abstraction.
   If only directories move while forbidden edges remain, then continue to
   repair or report the dependency violation instead of accepting the layout.

4. Verify: Reconstruct imports and relevant runtime edges after the change,
   checking the declared direction rules and any prohibited cycles.
   If extraction misses dynamic edges, then mark that coverage gap and inspect
   the relevant composition or registration code manually.

5. Report: Return the role map, allowed relationships, graph findings, actual
   edge changes, exceptions, and behavior-preservation evidence.
   If source imports comply but runtime organization was not checked, then
   limit the claim to the inspected graph.

## Specification patterns

- **Dependency organization:** Within `{graph_scope}`, elements assigned to
  `{roles}` shall follow `{allowed_edge_rules}`, verified by
  `{source_and_runtime_dependency_inspection}`.
- **Boundary repair:** Moving `{responsibility}` to `{intended_role}` shall
  remove `{forbidden_relationship}` while preserving `{required_behavior}`,
  checked by `{edge_comparison_and_focused_contract_fixture}`.

Use the illustrative explicit-graph proposal in Specify when no numeric budget
is supplied; confirm with the user/stakeholder before accepting an organization.

## Rules of thumb

- Place boundary translation in the role that owns the external representation;
  domain code must not import delivery code merely to format its own result
  when the chosen direction rule forbids that dependency.
- Judge cycles against the declared edge types; removing an import cycle does not
  remove a runtime callback cycle hidden by registration.
- Keep exceptions on the actual forbidden relationship; a broadly exempt package
  can conceal new violations outside the approved organizational exception.

## Verification

Use dependency-graph inspection, architecture-rule checks, and focused behavior
regression. Verify role membership for every checked element.
Distinguish imports, calls, inheritance, and runtime registrations in the evidence.
Retain excluded modules and unknown dynamic edges instead of accepting an
incomplete graph as full coverage.
Compare allowed/forbidden edges before and after the reorganization.
Inspect actual imports and calls after file moves; directory labels alone do not
establish the changed dependency graph.
Exercise the result through its actual entrypoint to detect misplaced translation.
Do not infer independent deployability from compliant layer direction.

## Done checklist

- [ ] Name organizing roles and their assigned elements.
- [ ] State allowed edge types and dependency directions.
- [ ] Identify actual violating relationships and any prohibited cycle.
- [ ] Inspect edge changes independently of file moves.
- [ ] Check runtime registrations where static inspection is insufficient.
- [ ] Attribute exceptions to their precise relationships.
- [ ] Preserve required entrypoint behavior after relocation.
- [ ] Bound the conclusion to the inspected dependency graph.

## Failure modes

- Treating tidy directories as evidence of compliant dependencies.
- Keeping external formatting inside domain logic under a renamed module.
- Removing static imports while retaining the same forbidden runtime dependency.
- Exempting a package so broadly that new violations become invisible.
- Claiming compliant layering proves responsibilities can run independently.

## References

- Read [organization decisions](./references/design-guide.md) when repairing
  forbidden dependencies or choosing precise relationship checks.
- Read [delivery/domain example](./references/worked-example.md) when verifying
  that relocation changes actual edges while preserving the entrypoint result.
