# Supplementary capability attachment patterns

Choose an attachment only after naming the original and supplementary results.
These are proposed design choices, not claims about a specific installed system.

## Separate result surface

- **Use when:** Recommendations or annotations assist a workflow without becoming
  its authoritative output. Keep source, freshness, and adoption action visible.
- **Trade-off:** A separate surface can require extra navigation; combining the
  surfaces may make authority and provenance harder to distinguish.
- **How to verify:** Present contradictory original and helper results in a fixture.
  Check which result the UI labels authoritative and whether application is explicit.

## Read-only projection

- **Use when:** The helper needs context but not permission to modify original state.
  Supply a bounded projection rather than exposing the entire mutable domain object.
- **Trade-off:** The projection may be stale or omit a needed field; a helper must
  not compensate by silently reaching around the boundary to read or write more.
- **How to verify:** Change the original record while helper work is pending and
  inspect stale-output handling, available fields, and any attempted mutation.

## Explicit adoption command

- **Use when:** Users may apply a helper suggestion to the original workflow.
  Make adoption a separate command with the original state's current preconditions.
- **Trade-off:** Adoption needs conflict handling; automatically applying suggestions
  is a different authority contract and must be requested explicitly.
- **How to verify:** Display without adoption, adopt after the original changes,
  reject an obsolete suggestion, and inspect the original write ledger.

## Removal boundary

- **Use when:** The supplement is optional or replaceable independently of the original.
  Identify registration, subscriptions, projections, and pending work to detach.
- **Trade-off:** Removing a helper may discard helper-only history; preserve only
  what the agreed purpose requires rather than indefinitely retaining its copies.
- **How to verify:** Disable and remove the helper, replay the original journey,
  and inspect for required helper reads or writes still occurring in the background.

## Acceptance record and anti-patterns

Record original invariants, helper result, attachment inputs, mutation authority,
activation, removal, observation cases, and separate owners. For a preservation
fixture, offer an illustrative bound of 0 changes to original results;
confirm with the user/stakeholder. Do not assume every augmentation is side-effect free.

- Reject a helper whose own success test is the only test of the original journey.
- Mark original-only behavior unverified when the helper was never disconnected.
- Revisit the scope if the addition replaces the original actor or decision entirely.
