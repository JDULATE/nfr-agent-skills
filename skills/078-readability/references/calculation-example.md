# Worked example: expose an order subtotal

Treat this as synthetic Python code, not a finding about the user's application.
Keep the business behavior fixed; do not add rounding, validation, or pricing rules.

## Inspect the context

Take the request: "Make this calculation easier to follow."
Read the caller, line-item schema, tests, and pricing explanation first. For this
example, assume those artifacts establish unit price times quantity, then discount
subtraction, then delivery-fee addition, with the existing function's public names.
In a real project, Ask the user if that interpretation or the intended audience
cannot be established from the artifacts.

## Before

```python
def order_total(line_items, discount_amount, delivery_fee):
    return sum(item["unit_price"] * item["quantity"] for item in line_items) - discount_amount + delivery_fee
```

## After

```python
def order_total(line_items, discount_amount, delivery_fee):
    subtotal = sum(item["unit_price"] * item["quantity"] for item in line_items)
    return subtotal - discount_amount + delivery_fee
```

Expose the intermediate result as `subtotal`; retain the function signature and
the input keys. Do not rename the keys to make them match a new local vocabulary.
Preserve subtraction before fee addition and the original input and exception
behavior. Explain the additional line by the meaning it exposes, not its length.

## Requirement proposal

Propose: "For the order-total helper, a reader familiar with the line-item schema
shall identify the fields used in the subtotal, the discount and fee order, and
the external names that must remain compatible, using the function and schema
as context, with answers matching the reviewed pricing interpretation."

If a time budget is needed, propose this illustrative example only: 2 minutes
for these questions with required answers correct; confirm with the user/stakeholder.
Do not require a fixed budget or claim an improvement until the user accepts the
task and representative readers attempt it.

## Answer key and preservation checks

| Question | Expected answer from the example contract |
| --- | --- |
| Which fields form subtotal? | Multiply unit_price by quantity per item and sum the products. |
| Where are discount and delivery fee applied? | Subtract discount from subtotal, then add the fee. |
| Which names stay compatible? | Keep order_total, its keyword parameter names, and the serialized item keys. |

Compare both implementations using illustrative synthetic inputs: no line items,
several line items, a nonempty discount, and a delivery fee. Compare exceptions
for a missing required item key. Check keyword callers as well as positional
callers. Record that passing these cases supports preservation for those cases,
not a proof for all possible Python objects or overloaded numeric operations.

## Review the reading claim

Give the reader the code and schema before supplying the answer key. Capture the
answers and any mistaken interpretation. Avoid showing the original and then
assuming a quicker second reading proves improvement; report order and familiarity
limitations or use equivalent independent tasks.

If the new name still fails to convey the intended subtotal, revisit the domain
term with the reader. If the actual problem is an unexplained pricing rule,
route the conceptual explanation to the comprehensibility sibling. Report any
executed preservation checks separately from reader evidence; this hypothetical
example alone supplies neither an observed audience result nor project acceptance.
