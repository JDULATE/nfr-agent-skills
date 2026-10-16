# Specified-behavior repair decisions

Obtain the rule before choosing a code change.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Equality takes the wrong branch under an inclusive rule | Align the comparison operator with that rule | May change an externally visible boundary result | Check below, equal, and above inputs against independent expectations |
| An already-used token is accepted again | Add the contract's state precondition before applying the normal operation | Callers need a distinct refused outcome | Repeat the operation and inspect both response and protected state |
| Response is correct but state transitions incorrectly | Place the required mutation on the accepted path and preserve refusal state | More explicit state/effect handling | Compare initial and final state for accepted and rejected cases |
| Regression expectations repeat the current branching logic | Replace the circular oracle with a rule-derived decision table | Expected cases require separate maintenance and review | Introduce the known wrong predicate and confirm the case detects it |

## Fixture behavior sketch

Illustrative pseudocode for the supplied discount rule, not a pricing standard.

```text
apply_discount(total_minor, coupon_state):
    if coupon_state != "unused":
        return {result: "refused-used", coupon_state: coupon_state}
    if total_minor < threshold_minor:
        return {result: "ineligible", payable: total_minor, coupon_state: "unused"}
    return {
        result: "applied",
        payable: total_minor - discount_minor,
        coupon_state: "used"
    }
```

The threshold and discount come from the approved contract.
This pure fixture returns the proposed next state; real persistence and concurrent
redemption require additional implementation evidence.

## Oracle boundary

A table can be independent of code while still reflecting a wrong specification.
If the contract is disputed, show the disagreement instead of proving compliance
with whichever source is easiest to satisfy.
