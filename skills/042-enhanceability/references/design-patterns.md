# Existing-capability refinement patterns

Anchor a refinement to an existing accepted result before choosing architecture.
Use the repository's local distinction from adding or supplementing a capability.

## Replaceable internal strategy

- **Use when:** A named computation needs refinement while callers depend on its
  current result contract. Separate that computation from input and output adapters.
- **Trade-off:** An extra strategy boundary adds indirection; do not generalize it
  beyond the requested improvement merely to demonstrate architectural flexibility.
- **How to verify:** Run the original callers against both strategies and compare
  output meaning as well as the existing quality measure.

## Paired baseline and candidate evaluation

- **Use when:** A refinement's value can be judged against retained original outputs.
  Hold corpus and scoring interpretation constant during the candidate comparison.
- **Trade-off:** The corpus may miss important cases; expanding it is useful but
  must be reported separately from a gain on the original matched sample.
- **How to verify:** Inspect changed cases, protected groups, and results under
  both the old and newly added corpus where an expansion is necessary.

## Staged strategy adoption

- **Use when:** Consumers need the unchanged contract while a candidate is evaluated.
  Choose an explicit strategy-selection point and preserve a viable baseline path.
- **Trade-off:** Maintaining both strategies creates extra test and data-version
  obligations; a switch is not a safe reversal if earlier writes changed meaning.
- **How to verify:** Select, deselect, and revert the candidate with the existing
  caller inputs; inspect persistent result semantics and protected cases afterward.

## Requirement record

Record the capability, current acceptance rule, baseline, corpus revision, protected
groups, refinement surface, target, consumer invariants, and evidence owner.
As an illustrative example only, propose 10% fewer errors under the unchanged
scoring rule; confirm with the user/stakeholder. Relative improvement requires
a meaningful baseline; ask for a different target if it cannot be interpreted.

## Review checks and anti-patterns

- Preserve examples whose old result was wrong rather than deleting awkward cases.
- Separate a better original result from a new supporting result with its own purpose.
- Inspect whether an apparent gain actually comes from a changed definition of success.
- Keep caller meaning explicit when an internal field or algorithm is replaced.
