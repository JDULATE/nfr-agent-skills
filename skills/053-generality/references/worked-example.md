# One numeric interval model across related fields

This synthetic family and its values are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled family record

| Input | Value |
| --- | --- |
| Family | finite numeric interval predicates on fields whose values and bounds share a declared unit |
| Common operation | contains(rule, record), returning true/false |
| Variation dimensions | field, lower, upper, include_lower, include_upper |
| Invariants | lower is below upper; inclusion flags always determine equality semantics |
| Supported fields in fixture | quantity in items; duration in seconds |
| Exclusions | categorical values, dates, unit conversion, missing fields |
| Initial state | no persistent state; each evaluation is independent |
| Owner | validation-model maintainer role |

All bounds and acceptance cases below are illustrative;
confirm with the user/stakeholder.

## Before: named special cases

The old evaluator accepts field=quantity and checks an inclusive interval.
It returns UnsupportedField for duration even when the same operation applies.
Adding duration previously meant editing the evaluator's field-name switch.

For rule quantity/[2,5] inclusive and record {quantity:3}, it returns true.
For rule duration/(10,20] and record {duration:15}, it returns UnsupportedField.
The latter is inside the declared family and fails the coverage proposal.

## Remediation

Represent the varying field and endpoint modes in a common rule object.
Validate the family assumptions, then call the same evaluator.

| Rule object | Record | Result after change |
| --- | --- | --- |
| field=quantity, lower=2, upper=5, include_lower=true, include_upper=true | {quantity:3} | true |
| same quantity rule | {quantity:2} | true |
| same quantity rule | {quantity:6} | false |
| field=duration, lower=10, upper=20, include_lower=false, include_upper=true | {duration:15} | true |
| same duration rule | {duration:10} | false |
| same duration rule | {duration:20} | true |

The duration case adds rule data, not a duration branch.
No persistent state changes in any run.

## Caller branch negative

A mutant generic core handles both fields, but its caller chooses an entirely
separate duration evaluator by field name.
Its values can pass the table while its construction still requires per-member
redesign. Source inspection fails that part of the acceptance record.

## Outside-family control

Supply rule field=state with bounds draft and published, record {state:review}.
These unordered categories have no supplied numeric order.
Model validation returns UnsupportedFamily before comparison.
It does not invent an ordering or silently use textual sorting.

## Requirement example and limits

For the declared numeric interval family, supported fields shall use the same
contains operation with explicit endpoint semantics and no field-name dispatch.
This is an illustrative proposal; confirm with the user/stakeholder.

The fixture shows contrasting fields and equality behavior only.
It does not prove coverage of every finite numeric representation or future
predicate family, and it does not establish distinct task roles for a product.
