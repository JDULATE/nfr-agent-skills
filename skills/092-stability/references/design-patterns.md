# Drift-and-oscillation practices

Use the actual operating envelope and response obligations, not a universal control recipe.

## Aligned input/action/output trace

- Use when reversals may reflect stale measurements or different observation windows.
- Trade-off: detailed traces add collection work, but smoothing independent series
  can make feedback timing or real input changes impossible to inspect.
- Verify: retain time, input condition, measured signal/freshness, chosen action,
  output, and controller state with a consistent window and version.

## Transition band and dwell decision

- Use when noise near a decision boundary repeatedly changes mode.
- Trade-off: separate enter/exit conditions or a hold interval can reduce reversals
  while delaying a necessary response; permitted delay belongs in the contract.
- Verify: exercise boundary noise and a genuine sustained input change; inspect
  both reversals and required response before accepting the candidate rule.

## Settling and directional drift

- Use when initial transients differ from longer held-condition behavior.
- Trade-off: an explicit settling interval avoids misclassifying expected startup,
  but excessive exclusions can hide the behavior the user needs bounded.
- Verify: predeclare settling and trend criteria, retain the full trace, and
  inspect post-settling behavior without selecting a favorable window afterward.

## Coupled feedback inspection

- Use when multiple loops, schedulers, or periodic actions affect the same state.
- Trade-off: changing a single loop may shift rather than remove the oscillation;
  coordinating them can alter responsiveness and ownership of the control decision.
- Verify: trace each controller's measured input, action, and effect on the other's
  next observation; test the declared combined envelope rather than isolated success only.
