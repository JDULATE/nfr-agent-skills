# Exchange decisions

Inspect both endpoints; an adapter needs an agreed interpretation to preserve.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Sender sends packs while receiver expects individual items | Introduce a unit-aware boundary adapter using supplied pack content | Conversion context must be maintained with the item | Compare requested and applied item counts; refuse absent conversion context |
| Caller displays completed after a queued acknowledgement | Expose accepted and applied states through the response mapping | Caller must handle an intermediate state | Pause application and inspect caller status before and after the effect |
| Unknown unit reaches a default numeric handler | Add an explicit supported-unit gate | Some previously accepted messages now refuse | Send unsupported units and inspect refusal plus unchanged domain state |
| Empty and absent fields have distinct documented meanings | Preserve presence information through serialization | More explicit payload construction and mapping | Exercise omit, empty, and clear cases against the agreed effects |

## Unit adapter sketch

Illustrative pseudocode for the synthetic item contract.

```text
to_items(message, catalog):
    if message.unit == "item":
        return message.amount
    if message.unit == "pack" and catalog.has(message.sku):
        return message.amount * catalog[message.sku].items_per_pack
    return Refused("unsupported-or-unresolved-unit")
```

Do not infer catalog content from a product name.
The sketch assumes amount validity has already been checked against the contract.
If participants disagree about rounding or fractional quantities, then resolve
that contract before implementing a conversion.

## Response contract

Map receiver accepted to caller pending.
Map receiver applied to caller completed only after the promised effect exists.
Map semantic refusal to a visible rejected outcome without replaying it as success.
Determine retry obligations separately; no generic success code establishes them.
