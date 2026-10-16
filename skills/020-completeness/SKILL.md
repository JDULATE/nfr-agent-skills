---
name: completeness
description: >-
  Checks required members when asked "find omitted order IDs", "check every attachment", or "duplicates hide missing rows". Ask the user if missing items vs missing topics is unclear. Not for breadth of explanations (see comprehensiveness) or wrong computed values (see correctness).
---

# Completeness

## Definition and scope

Completeness means every required member or case in an explicitly bounded set is
represented or handled. Define that set before counting coverage.
Separate missing required members from broad explanatory coverage
(`comprehensiveness`) and from incorrect computed values (`correctness`).

## Use when / Don't use when

- Apply when an export, migration, response, or case handler omits required
  members even though the total count appears plausible.
- Establish identity, conditional membership, and the revision or snapshot
  that bounds the required set.
- Route missing subject matter in a guide to `comprehensiveness`.
- Route a present item's wrong computed value to `correctness` or `accuracy`
  according to the stated comparison.
- Do not imply that covering a set proves the contents are correct.

## Workflow

1. Clarify: Read source inventories, query predicates, pagination, case dispatch,
   export code, and requirements before specifying coverage.
   Identify how a required member receives a stable identity.
   If "everything" has no bounded universe, then Ask the user which members,
   conditions, and snapshot constitute the required set.

2. Specify: Record the required-set source and revision, membership predicate,
   identity rule, represented/handled criterion, and treatment of duplicates
   and unexpected members.
   If no target is given, then propose a labeled illustrative default:
   every member of the declared fixture set represented, missing identities
   reported separately from duplicates; confirm with the user/stakeholder.
   For a fix, ask at most three questions about the universe, member identity,
   and what evidence counts as representation or handling.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [coverage decisions](./references/design-guide.md)
   when changing pagination, identity tracking, or conditional case enumeration.
   If row counts match but identities differ, then compare required and observed
   identities directly rather than accepting the count.
   If the universe changes during traversal, then establish an agreed snapshot
   or reconciliation rule before claiming complete coverage.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Enumerate required and observed identities under the declared boundary;
   calculate missing members, duplicates, and unexpected members separately.
   Retain failed pages, unfinished traversal, and exclusions with reasons.
   If a required-set source is itself incomplete, then report the resulting
   evidence limit rather than treating the enumerated subset as the whole universe.

5. Report: Deliver the bounded-set definition, omission fixes, member-level
   differences, conditional cases, and unverified regions.
   If all present values were tested but enumeration was not, then withhold a
   completeness conclusion; value checks cannot discover absent identities alone.

## Specification patterns

- **Inventory coverage:** For `{required_set_at_revision}`, `{output}` shall
  represent every identity meeting `{membership_predicate}`, verified by
  `{required_minus_observed_comparison}` with `{duplicate_and_extra_reporting}`.
- **Case coverage:** For each `{required_case_and_condition}`, `{handler}`
  shall produce `{evidence_of_handling}`, verified by
  `{enumerated_case_to_execution_mapping}`.

Use the illustrative bounded-set coverage proposal in Specify when numbers are
absent; confirm with the user/stakeholder and keep unknown membership unresolved.

## Rules of thumb

- Compare required identities, not only totals; duplicate rows can replace a missing
  member without changing the observed count.
- Keep conditional members in the universe when their stated condition holds;
  filtering them out before comparison erases the omission being checked.
- Accept a member as covered only at its required representation boundary;
  a source row does not prove that the corresponding export row exists.
- Keep missing identities separate from unexpected identities; extra output cannot
  compensate for a required member that never appeared.

## Verification

Use set-difference checks, traversal fixtures, and case-to-handler inspection.
Capture the required-set revision and the actual membership predicate.
Exercise page boundaries, duplicate identities, empty pages with continuation,
and interrupted traversal when those mechanisms exist.
Check that representation evidence refers to the required output boundary.
Retain raw identity lists and predeclared exclusions to make coverage reproducible.
Inspect output values separately if correctness is also requested.
Do not silently remove duplicates before reporting their effect on naive counts.

## Done checklist

- [ ] Bound the required universe and its source revision.
- [ ] Validate member identity and conditional membership.
- [ ] Observe representation at the required output boundary.
- [ ] Compute missing, duplicate, and unexpected identities separately.
- [ ] Exercise traversal or dispatch boundaries that can omit members.
- [ ] Record interrupted or unknown portions without accepting them.
- [ ] Separate completeness evidence from value-correctness evidence.

## Failure modes

- Accepting equal counts while a duplicate hides an omission.
- Comparing against a filtered required list that already drops the missing case.
- Counting source presence instead of required output representation.
- Treating an unfinished traversal as an intentionally smaller universe.

## References

- Read [coverage decisions](./references/design-guide.md) when choosing identity
  comparison, snapshot boundaries, or traversal fixes.
- Read [export coverage example](./references/worked-example.md) when proving
  a missing-member failure despite matching row counts.
