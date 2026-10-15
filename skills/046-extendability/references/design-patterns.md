# Bounded core capability additions

Inspect existing extension seams before choosing any core edit. The distinction
here follows the repository convention, not an externally standardized naming rule.

## Owner-local dispatch

- **Use when:** A new operation belongs to a known core responsibility. Add the
  operation's dispatch and implementation at that boundary rather than at every caller.
- **Trade-off:** Central ownership can become overloaded; reassess the responsibility
  if the new operation has different data or lifecycle obligations.
- **How to verify:** Inspect which consumers now branch on the new operation and
  whether original callers can continue using their existing request form.

## Explicit interface addition

- **Use when:** New behavior requires a new operation selector, result variant,
  or input field. Make the new meaning explicit and preserve old selections.
- **Trade-off:** New variants may require consumer coordination; defaulting an
  old request into the new variant can conceal a breaking meaning change.
- **How to verify:** Run existing requests unchanged, add the new form, and inspect
  old consumers' parsing, errors, and any migration the added variant requires.

## Implementation seam before general platform

- **Use when:** The named addition benefits from separating an internal computation.
  Add only the seam needed to keep the new responsibility and old behavior distinct.
- **Trade-off:** A speculative plug-in framework adds contracts beyond the requested
  addition; a one-off branch may instead make a later known addition unnecessarily broad.
- **How to verify:** Trace the requested result through the seam and inspect the
  actual next named addition, if any, rather than assuming an unlimited future.

## Change-surface ledger

- **Use when:** Stakeholders need a bounded addition cost or ownership footprint.
  Define counted production modules and show consumer, generated, test, and doc impact.
- **Trade-off:** Counts depend on packaging; use them alongside responsibility
  and interface review instead of treating fewer files as intrinsically better.
- **How to verify:** Compare the complete dependency diff with the ledger and
  record extra owners or migrations before accepting the declared surface.

Illustrative scope only: at most 2 owner modules for the selected example;
confirm with the user/stakeholder. Establish the actual limit from the existing
architecture; do not consolidate unrelated code to meet a synthetic count.

## Review failures

- Reject counting hook creation as an addition through a pre-existing hook.
- Record an old field's changed meaning as an interface change, not merely a new option.
- Mark old-consumer preservation unverified if only the new operation was exercised.
