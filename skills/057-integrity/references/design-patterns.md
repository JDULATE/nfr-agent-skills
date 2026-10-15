# Alteration-control practices

Protect permitted state transitions and provenance without assuming all existing values are accurate.

## Final-write constraints

- Use when fields, writers, or transitions have distinct alteration permissions.
- Trade-off: shared enforcement reduces bypasses but needs explicit allowed
  corrections and actual resource/state context rather than blanket immutability.
- Verify: attempt protected-field changes through normal and alternate writers;
  inspect final state and retain authorized corrections as positive controls.

## Independent provenance expectation

- Use when imported content or behavior must match a trusted origin.
- Trade-off: a trustworthy comparison requires an independently established source;
  equality with an attacker-supplied reference gives no additional origin authority.
- Verify: alter content and its untrusted reference together, inspect the real
  trust anchor, and separate equality, origin, and freshness claims.

## Version and replay boundary

- Use when previously valid input can overwrite newer approved state.
- Trade-off: rejecting stale input can interrupt a legitimate workflow; conflict
  handling and authorized rollback must follow the stakeholder's transition policy.
- Verify: change approved state before an old edit commits, and replay an older
  import; inspect the actual version decision at the mutation/use boundary.

## Mismatch and repair behavior

- Use when a failed validation must preserve or reconcile protected state.
- Trade-off: refusing suspect input can block needed repair; accepting it can
  replace known-good state. The approved alternative must be explicit.
- Verify: exercise rejected, partially processed, and corrected input; inspect
  actual protected contents rather than accepting an error response as prevention.
