---
name: uniformity
description: >-
  Aligns conventions across comparable peers when tickets say "list routes name the same limit differently", "use the same paging fields on these routes", or "why does only this list take pageSize". Not for selecting a common convention (see standardizability-standardization-standard) or value agreement (see consistency).
---

# Uniformity

## Definition and scope

Uniformity means comparable elements follow deliberately consistent conventions.
Establish which peers and operations should follow the same pattern, while
retaining justified differences in meaning.
Separate peer convention alignment from selecting that convention
(`standardizability-standardization-standard`) and agreement about values
(`consistency`).

## Use when / Don't use when

- Apply when comparable list routes expose different names or interaction
  patterns for the same operation under an already chosen convention.
- Include the caller-visible surface and documentation together.
- Route choosing a shared convention to
  `standardizability-standardization-standard`.
- Route conflicting state values at a defined revision to `consistency`.
- Route one artifact's pass against supplied rules to `conformance`; this
  skill compares a declared peer set and justified variation across it.

## Workflow

1. Clarify: Read peer interfaces, handlers, callers, convention docs, and
   known exceptions before specifying alignment.
   Verify that the apparently similar options actually mean the same thing.
   If the peer set or convention is missing, then Ask the user which comparable
   surfaces should follow which existing pattern.

2. Specify: Record peer membership, equivalent operations, selected convention,
   canonical surface, compatibility aliases, and justified exceptions.
   If no target exists, then propose a labeled illustrative default:
   equivalent paging operations accept the same canonical fields and meaning,
   with aliases and exceptions visible; confirm with the user/stakeholder.
   Ask at most three questions about comparability, convention authority,
   and caller compatibility before changing interfaces.

3. Design/Implement: Read [peer-alignment decisions](./references/design-guide.md)
   when normalizing equivalent surfaces or retaining exceptions.
   If peer parameters have different units or effects, then keep the distinction
   explicit rather than renaming them into false equivalence.
   If existing callers require an old name, then define its alias and conflict
   behavior while implementing the canonical path on every in-scope peer.

4. Verify: Apply the same equivalent request to each comparable peer and inspect
   actual handling, docs, aliases, and differences.
   If only examples were renamed while handlers still diverge, then fail the
   peer-alignment claim and report the remaining surface inconsistency.

5. Report: Return the peer/convention map, changed surfaces, common behavior
   evidence, aliases, and justified differences.
   If an exception is semantically distinct, then state why it is outside the
   comparable operation instead of claiming universal uniformity.

## Specification patterns

- **Peer convention:** For `{comparable_peers_and_operation}`, each surface
  shall expose `{canonical_fields_and_meanings}`, verified by
  `{same_request_across_peer_handlers}`.
- **Allowed variation:** `{alias_or_exception}` shall follow
  `{declared_mapping_or_semantic_difference}` without obscuring
  `{canonical_peer_pattern}`, checked by `{alias_conflict_and_exception_cases}`.

Use the illustrative canonical-paging proposal in Specify when numbers are
absent; confirm with the user/stakeholder rather than imposing a universal style.

## Rules of thumb

- Group peers by equivalent operation before aligning their surface; a byte budget
  and an item count must not acquire the same meaning merely by sharing a name.
- Apply the canonical convention to actual handlers as well as examples;
  documentation-only alignment leaves callers facing different peer contracts.
- Keep compatibility aliases subordinate to one declared canonical surface;
  conflicting alias values need an explicit resolution or refusal on every peer.

## Verification

Use cross-peer request fixtures, interface inspection, and documentation review.
Retain the peer inventory and the meaning of each compared field.
Exercise the canonical path, accepted aliases, and conflicting alias inputs.
Check common expected outcomes independently for each handler.
Keep failures and exceptions visible instead of excluding inconvenient peers
after seeing the results.
Distinguish cosmetic agreement from equivalent caller interaction.
Do not infer value consistency or system-wide convention adoption from aligned names.

## Done checklist

- [ ] Define comparable peers and equivalent operations.
- [ ] Identify the selected canonical convention.
- [ ] Check parameter meaning and units before renaming.
- [ ] Exercise the canonical request on every in-scope handler.
- [ ] Verify documented aliases and conflicting-value behavior.
- [ ] Attribute semantic exceptions without hiding peer failures.
- [ ] Compare documentation with the actual caller-visible surfaces.

## Failure modes

- Renaming unlike quantities into a misleading common field.
- Updating examples while one handler still accepts only its old spelling.
- Letting peers resolve conflicting aliases differently.
- Calling aligned names evidence that their returned state values agree.

## References

- Read [peer-alignment decisions](./references/design-guide.md) when deciding
  comparability, canonical fields, aliases, and exceptions.
- Read [paging-peer example](./references/worked-example.md) when checking
  equivalent requests across actual peer surfaces.
