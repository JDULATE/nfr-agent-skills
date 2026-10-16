# Reservation invariant example

Treat this as an illustrative mathematical model and constructed trace.
All fixture amounts are illustrative examples; confirm with the user/stakeholder
before treating this model or its domain as a project's requirement.

## Filled proof record

| Field | Model value |
| --- | --- |
| Proposition | every reachable balance is nonnegative |
| Balance domain | mathematical integers |
| Amount domain | mathematical integers |
| Permitted initial states | any balance at least zero |
| Transition scope | one sequential reserve action at a time |
| Other state changes | none |
| Successful action | subtract amount when the guard accepts |
| Refused action | preserve balance |
| Implementation correspondence | not established; no production code is claimed |
| Excluded claims | concurrency, fixed-width overflow, crash persistence, external ledger agreement |
| Counterexample start / input | balance 4; reserve amount 7 |
| Carried next state before fix | balance -3 |

Zero defines the invariant's boundary, not an operational service target.

## Failing transition

The original guard accepts any strictly positive amount:
```text
if amount > 0: balance = balance - amount
else: balance = balance
```

From balance 4 with amount 7, it produces -3.
This constructed trace disproves preservation in the stated model.
It does not establish that an actual application has this guard.

## Remediation

Require the requested amount to fit the available balance:
```text
if amount > 0 and amount <= balance:
  balance = balance - amount
else:
  balance = balance
```

The same counterexample input now refuses and preserves balance 4.
From balance 4 with amount 2, it accepts and carries balance 2 forward.
From balance 0 with amount 1, it refuses and preserves balance 0.
From balance 4 with amount -1, it refuses and preserves balance 4.
These are illustrative trace values; confirm with the user/stakeholder before
using any fixture amount as a project acceptance value.

## Checkable argument

Establishment: permitted initial states satisfy balance >= 0 by definition.
Accepted branch: the guard makes amount at most balance, so subtracting amount
leaves a nonnegative next balance.
Refused branch: next balance equals the already nonnegative current balance.
Therefore every finite sequence of these modeled actions preserves nonnegativity
by induction over action count.

The rejected branch is part of the argument, not merely an error test.
The initial-state premise is necessary: starting at balance -1 would violate the
invariant before any action occurs.

## Requirement example

Under sequential mathematical-integer reservation transitions and a nonnegative
initial balance, every reachable balance shall remain nonnegative, established
by initial-state and branch-preservation arguments.

## Remaining obligations

A fixed-width implementation may have arithmetic behavior outside this model.
Concurrent callers may read the same prior balance before either update.
No statement here discharges those mapping obligations or establishes persistence.
Report the theorem as conditional until the actual representation and transition
boundaries are inspected and justified.
