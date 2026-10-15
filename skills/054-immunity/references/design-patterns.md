# Exclusion-argument practices

The claim must name an exact class, enabling mechanism, assumptions and boundary.

## Enabling-path removal

- Use when a class depends on an interpretation, state transition or invocation
  that can be removed from the declared reachable path.
- Trade-off: removing a mechanism can limit required behavior; a replacement may
  retain an equivalent enabling path even if its name changes.
- Verify: inspect the actual reachable operation and preserved required use;
  record an argument for exclusion rather than treating rejected examples as proof.

## Alternative route and dependency closure

- Use when wrappers, plugins, loaders, background jobs or dependencies can invoke the same effect.
- Trade-off: broader closure costs review effort; an unexamined dependency leaves
  the local claim conditional rather than supporting all-environment exclusion.
- Verify: trace each declared route to its actual operation and challenge bypasses;
  disclose routes/dependencies whose enabling behavior is unknown.

## Assumption enforcement and invalidation

- Use when exclusion depends on configuration, environment or a restricted capability.
- Trade-off: a conditional mechanism can be useful, but the condition must remain
  inspectable and changing it must invalidate the old argument.
- Verify: change the relevant condition in an isolated fixture; inspect whether
  the property still holds and whether the claim is reopened when it does not.

## Counterexample versus proof boundary

- Use when test passes are being summarized as immunity.
- Trade-off: synthetic challenges can defeat a claim but cannot enumerate every
  unmodeled input or state. Structural reasoning must expose its own premises.
- Verify: retain mechanism reasoning, scoped paths, failed challenges and unknowns;
  do not call the case a formal proof without an actually checkable argument.
