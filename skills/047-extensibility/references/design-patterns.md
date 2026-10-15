# Existing extension-contract patterns

Use the documented contract as the boundary. An extension label does not establish
independent implementation, safe authority, or automatic support for every lifecycle.

## Data-driven registration

- **Use when:** The host already admits implementations through a manifest, registry,
  or configuration contract. Keep extension identity and dispatch at that seam.
- **Trade-off:** Registration validation and ownership still matter; configuration
  that executes new host logic is not automatically outside the core change surface.
- **How to verify:** Add a synthetic implementation through the documented route
  and inspect for added concrete-type branches or undocumented loader changes.

## Independent contract fixture

- **Use when:** Built-ins might rely on private state unavailable to an extension
  author. Build a fixture using only the declared inputs and lifecycle calls.
- **Trade-off:** A minimal fixture may miss real resource use; expand cases around
  the actual requested behavior rather than claiming universal extension support.
- **How to verify:** Exercise outputs, rejected inputs, failures, and cleanup with
  no private host access; compare the behavior with the documented obligations.

## Explicit lifecycle boundary

- **Use when:** Registration, activation, replacement, or removal changes resources
  or persistent extension-owned state. Declare which transitions the host supports.
- **Trade-off:** Hot removal may require work the current contract never promised;
  do not infer it from independent registration or invent it as a universal requirement.
- **How to verify:** Exercise only the supported transitions, inspect pending work
  and retained state, and record any restart or manual cleanup that remains necessary.

## Contract revision and authority record

- **Use when:** Extensions depend on a particular host meaning or can access host
  data and resources. Record the supported contract and allowed capabilities explicitly.
- **Trade-off:** A more capable hook exposes more obligations; old implementations
  may not understand a new meaning even when field names look unchanged.
- **How to verify:** Compare the intended host/extension combinations and inspect
  attempted access outside the declared boundary without equating this with a complete security review.

Illustrative source-edit target only: 0 core edits for a conforming added fixture;
confirm with the user/stakeholder. Measure the complete host diff and disclose
registration changes and contract revisions separately.

- Reject private built-in success as the only evidence of an independently usable hook.
- Mark old-contract admission unverified if the host contract changed first.
- Keep removal support and restart requirements as explicit lifecycle choices.
