# Invoice rerun example

Use this illustrative fixture to separate hidden carry from inherent variation.
All quantities, identifiers, and rerun counts are illustrative examples;
confirm with the user/stakeholder before using the procedure as an acceptance gate.

## Filled run contract

| Field | Fixture value |
| --- | --- |
| Executor / environment | same local invoice fixture runner / isolated in-memory store |
| Code / fixture revision | invoice-routine pine / invoice-fixture ash |
| Run boundary | fixture restoration through returned invoice and final state capture |
| Line input | quantity 3; unit price 10 credits; tax 0 credits |
| Initial rows | empty invoice table |
| Initial counter | last issued invoice number 40 |
| External inputs | none; no clock or random field in the result |
| Intended carry | run artifacts only; application rows and counter reset per run |
| Required result | invoice id inv-41; total 30 credits |
| Required final state | invoice row inv-41, total 30; last issued number 41 |
| Comparison | exact id, total, and required final state |
| Planned sequence | run-amber, run-birch, run-cedar |
| Artifact | each run's initial rows/counter, input, result, final rows/counter |

## Failing procedure before remediation

The loader restores only the empty invoice table.
The routine increments the last-issued counter before assigning the invoice id.

| Run | Initial counter | Result | Final counter |
| --- | ---: | --- | ---: |
| run-amber | 40 | inv-41, total 30 | 41 |
| run-birch | 41 | inv-42, total 30 | 42 |
| run-cedar | 42 | inv-43, total 30 | 43 |

Rows are emptied before each run, but the counter is not.
The captured starting-state difference demonstrates a condition mismatch.
It does not demonstrate that the routine is intrinsically random.

## Remediation

Restore the counter together with the rows at each run boundary.
Inspect the restored state before invoking the routine.

| Run | Initial rows / counter | Result | Final rows / counter |
| --- | --- | --- | --- |
| run-amber | empty / 40 | inv-41, total 30 | inv-41, total 30 / 41 |
| run-birch | empty / 40 | inv-41, total 30 | inv-41, total 30 / 41 |
| run-cedar | empty / 40 | inv-41, total 30 | inv-41, total 30 / 41 |

The changed loader removes the observed starting-state mismatch in this
constructed fixture. Retain the original differing sequence with the after record.

## Failing comparison case

If run-cedar returns inv-41 with total 20, exact comparison must fail even though
the identifier matches. Do not normalize away total merely to obtain consistency.
If invoice ids were intentionally global across runs, resetting this counter would
be the wrong procedure; choose a carry-aware requirement instead.

## Requirement example

The synthetic invoice procedure shall, after restoring its empty rows and
last-issued number 40, produce inv-41 totaling 30 credits in each planned rerun,
with the stated final row and counter.

These are illustrative fixture acceptance values, not universal billing rules;
confirm with the user/stakeholder before adopting them.

## Limits

The sequence supports consistency only for this executor, fixture, and reset policy.
It establishes neither independent reproducibility elsewhere nor a production
latency-variation bound. It does not justify resetting a live identifier counter.
