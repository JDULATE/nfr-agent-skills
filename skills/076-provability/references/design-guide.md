# Proof construction decisions

Use this guide only after the proposition and modeled domains are explicit.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| The invariant fails for an allowed initial state. | Repair initialization or narrow the permitted initial states with an enforced precondition. A narrower precondition excludes callers. | Exhibit establishment for each initialization branch and reject an out-of-domain caller explicitly. |
| A successful update breaks the invariant. | Strengthen the transition guard or change the state update. Some formerly accepted actions may now refuse. | Replay the counterexample, then check preservation for allowed and refused actions. |
| The proof uses a premise absent from the implementation. | Add and verify the enforcement boundary, or retain a conditional theorem only. Enforcement can change behavior. | Trace each premise to an actual guard, type contract, or stated external assumption. |
| Interleaving invalidates a sequential argument. | Model the relevant shared-state steps and coordination, or narrow the claim to sequential use. A richer model costs proof effort. | Check conflicting operations in the chosen model rather than citing the sequential theorem. |
| A tool reports no counterexample within a limit. | State the explored bounds and unresolved obligations. Stronger claims need an argument beyond that exploration. | Inspect the search domain and ensure the report does not quantify over unexamined states. |

## Invariant sketch

```text
Invariant: balance >= 0
Initial: balance >= 0
Action reserve(amount):
  if amount > 0 and amount <= balance:
    next_balance = balance - amount
  else:
    next_balance = balance
Obligations:
  Initial implies Invariant
  Invariant and allowed_action imply next_balance >= 0
  Invariant and refused_action imply next_balance >= 0
```

Here zero is the mathematical boundary defining the proposition, not a universal
operational target. The model uses mathematical integers and one sequential action.
An actual implementation needs its own arithmetic and concurrency correspondence.

## Premise ledger

For each premise, record whether it is a definition, an enforced condition,
or an environmental assumption. A domain restriction in the model is not
evidence that production inputs obey that restriction.

Keep theorem revision, transition revision, and counterexample revision together.
If a guard changes, revisit the affected preservation obligation rather than
reusing a prior proof label.
