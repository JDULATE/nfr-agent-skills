# Alternative task arrangements

Judge alternatives against a shared task result, not against identical internal
steps. These patterns do not establish support for arbitrary user-defined behavior.

## Shared obligation matrix

- **Use when:** Routes have different interactions or intermediate artifacts but
  promise the same task result. List common writes, result meanings, and exceptions.
- **Trade-off:** Excessive uniformity can remove useful route differences; allowing
  every difference can leave no meaningful shared task to accept.
- **How to verify:** Start matched tasks independently through each route and compare
  the common obligations, then inspect explicitly permitted differences separately.

## Eligibility before selection

- **Use when:** Some arrangements require different inputs, authority, resources,
  or prerequisites. Make each restriction part of the advertised alternative.
- **Trade-off:** Hiding an option can obscure why it is unavailable; displaying it
  without an explanation can advertise a route the chooser can never complete.
- **How to verify:** Try eligible and ineligible chooser contexts through the actual
  selector, checking both offered choices and the accepted rejection/explanation.

## Distinct dispatch evidence

- **Use when:** Multiple labels might reach the same implementation or dependency.
  Record which task route each selector invokes and what makes it an alternative.
- **Trade-off:** Routes may legitimately share helpers; shared code does not by itself
  invalidate flexibility. Distinguish shared utilities from an identical blocked path.
- **How to verify:** Trace selected route and completed work, then disable a
  route-specific prerequisite to see whether another promised route still works.

## Boundary of the claim

A manual and automated pair is an illustrative scope of 2 alternatives;
confirm with the user/stakeholder. Route coverage may need a different set.
Independently starting either arrangement does not establish switching a live task.
If switching is requested, specify state identity, incomplete work, and transition
semantics separately under the repository's reconfigurability convention.
