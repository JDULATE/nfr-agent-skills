---
name: generality
description: >-
  Covers related cases with one abstraction when asked "unify these range checkers", "cover quantities and durations", or "stop field-specific branches". Ask the user which case family and common rule are intended if unstated. Not for different task roles (see versatility) or moving an artifact to another context (see reusability).
---

# Generality

## Definition and scope

Generality means one abstraction represents an explicitly defined family of
related cases without redesign for each named case. State the family's common
operations, invariants, and legitimate variation.
Separate family coverage from using an artifact in another context (`reusability`)
and performing distinct task roles (`versatility`).

## Use when / Don't use when

- Apply when an abstraction handles named special cases but should cover a
  specified family through the same model and operations.
- Identify what makes the cases members of the same family.
- Route moving an existing artifact into a CLI or other context to `reusability`.
- Route a product performing unrelated task types to `versatility`.
- Route a missing distinction in notation to `expressiveness` when no broader
  family-coverage question has been established.

## Workflow

1. Clarify: Read the abstraction, caller branches, domain models, tests, and
   proposed family examples before specifying a generalization.
   Identify common operations and the dimensions that vary.
   If the user only says "make it generic," then Ask the user which related
   cases belong to the family and which must remain outside it.

2. Specify: Record family membership, invariant operation meanings, variation
   parameters, unsupported cases, and what counts as case-specific redesign.
   If no target is supplied, then propose a labeled illustrative default:
   named family members use the same operation through declared variation data,
   without adding a branch per member; confirm with the user/stakeholder.
   Ask at most three questions about the family, invariants, and allowed
   variation before changing the abstraction.

3. Design/Implement: Read [family-model decisions](./references/design-guide.md)
   when replacing named-case dispatch with a common representation.
   If cases differ only in a declared dimension, then carry that dimension as
   model data rather than hard-code a new member name.
   If a case violates the common operation's assumptions, then exclude it or
   revise the family explicitly instead of forcing it through a misleading default.

4. Verify: Exercise contrasting family members through the same operation and
   inspect both the abstraction and callers for hidden named-case branches.
   Retain unsupported and failing cases beside the declared family.
   If only the original member was tested, then leave broader family coverage
   unverified rather than inferring it from a type parameter or generic name.

5. Report: Return the family definition, common operation, removed special cases,
   coverage evidence, and exclusions.
   If the model covers only the stated numeric intervals, then do not claim
   arbitrary data types, every future range, or universal reuse.

## Specification patterns

- **Family coverage:** `{abstraction}` shall represent `{family_members}`
  using `{variation_parameters}` while preserving `{common_invariants}`,
  verified by `{contrasting_cases_and_branch_inspection}`.
- **Common operation:** Applying `{operation}` to `{supported_member}`
  shall produce `{family_defined_result}` without `{member_specific_redesign}`,
  and `{outside_family_case}` shall receive `{explicit_unsupported_result}`.

Use the illustrative common-model proposal in Specify when no numerical goal
exists; confirm with the user/stakeholder before accepting family coverage.

## Rules of thumb

- Represent a family's varying field as data when its operation is unchanged;
  a growing switch on member names preserves special cases rather than generality.
- Keep invariant operation meanings stable across members; inclusive bounds must
  not silently become exclusive merely because the field name changes.
- Exclude cases that lack the common operation's assumptions; treating unordered
  values as ordered intervals does not broaden a valid interval abstraction.
- Check callers for case-specific reconstruction of the supposed common model;
  moving member branches outside the abstraction does not remove redesign.

## Verification

Use family-case fixtures, source inspection, and invariant checks.
Record family membership and expected results independently of implementation.
Exercise different fields, boundary modes, and unsupported value kinds when in scope.
Keep evaluation inputs, failures, exclusions, and the same declared operation.
Inspect adapters and callers as well as the common function.
Distinguish tested coverage from a proof over all family members.
Do not use line count, generic syntax, or reuse in another executable as the
sole evidence of family generality.

## Done checklist

- [ ] Define the family and explicit exclusions.
- [ ] Identify common operations and invariant meanings.
- [ ] Make legitimate variation visible in the model.
- [ ] Exercise contrasting family members through the same operation.
- [ ] Inspect callers for displaced named-case branches.
- [ ] Check boundary behavior and an outside-family case.
- [ ] Limit the coverage claim to the declared evidence.

## Failure modes

- Renaming a special-case switch to a generic-sounding function.
- Moving the member-name dispatch into callers and claiming it disappeared.
- Broadening accepted inputs without a coherent common operation.
- Assuming a successful original case establishes a whole family's behavior.

## References

- Read [family-model decisions](./references/design-guide.md) when choosing
  invariants, variation data, and legitimate exclusions.
- Read [interval-family example](./references/worked-example.md) when checking
  one abstraction across related cases without named-case branches.
