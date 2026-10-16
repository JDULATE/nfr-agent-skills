# Defined-family decisions

Choose a common operation before introducing parameters.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Range checks branch on each field name despite identical ordered-bound behavior | Represent field, bounds, and endpoint modes as data | Invalid model combinations need validation | Run quantity and duration through the same evaluator and inspect callers |
| Equality semantics differ accidentally between family members | Make endpoint inclusion an explicit dimension with invariant meaning | More explicit rule data | Use values equal to each bound across different fields |
| A proposed member has no ordering relation required by intervals | Reject that member or choose a different abstraction | The family remains intentionally limited | Supply an unordered category and inspect unsupported-family refusal |
| A generic core still requires custom construction for every new member | Move legitimate variation into the shared model boundary | Existing callers may need migration | Add a declared field without adding member-name branches |

## Interval sketch

Illustrative pseudocode for finite numeric values in matching units.

```text
contains(rule, record):
    value = record[rule.field]
    if not finite_numeric(value):
        return UnsupportedFamily
    lower_ok = value >= rule.lower if rule.include_lower else value > rule.lower
    upper_ok = value <= rule.upper if rule.include_upper else value < rule.upper
    return lower_ok and upper_ok
```

Validate numeric bounds, ordering, and the field's unit before evaluation.
The sketch does not define date ordering, unit conversion, or categorical ranges.

## Family boundary

A configurable field name does not justify arbitrary predicates.
If different cases need unrelated operations, revisit the family rather than
adding opaque callbacks that conceal a member-specific algorithm.
Keep model construction and evaluation within the same coverage inspection.
