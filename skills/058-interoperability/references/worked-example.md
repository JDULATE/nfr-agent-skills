# Stock request meaning

This fixture is synthetic. Its quantities and acceptance criteria are illustrative
examples; confirm with the user/stakeholder before adopting them.

## Filled contract

| Input | Value |
| --- | --- |
| Sender | purchase client revision cedar |
| Receiver | stock allocator revision maple |
| Item | SKU pen |
| Catalog context | pen has 6 items per pack |
| Request | request=order-elm, sku=pen, amount=2, unit=pack |
| Receiver native unit | item |
| Initial allocated state | pen=0 items |
| Caller initial state | order-elm=new |
| Acceptance promise | accepted means queued with no allocation yet |
| Completion promise | applied means the requested item allocation exists |
| Unsupported unit behavior | refused, no allocation, caller rejected |
| Contract owner | ordering integration maintainer role |

## Before: parse success with wrong meaning

The old mapper drops unit and forwards amount=2 as individual items.
Receiver state becomes pen=2 items and responds applied.
Caller displays order-elm=completed.

Expected domain amount is 12 items from the supplied pack definition.
The fixture proves a semantic mismatch and shows the mapper dropping the unit;
it does not claim a real service has this defect.

## Remediation and carried state

Add the unit-aware conversion and preserve distinct response states.
Reset allocated pen=0 and caller order-elm=new.

```text
outbound mapped request: sku=pen, amount=12, unit=item
receiver response: accepted
receiver queue: [order-elm -> pen, 12 items]
allocated state: pen=0
caller state: order-elm=pending

after receiver applies the queued request:
receiver queue: []
allocated state: pen=12
receiver response: applied
caller state: order-elm=completed
```

Before application, claiming completion would still fail even though conversion
is correct. The pending state preserves the response's narrower promise.

## Unknown-unit failing case

Reset queue=[], allocated pen=0, caller order-elm=new.
Supply request order-elm, sku=pen, amount=2, unit=crate.
No crate conversion exists in the filled catalog.
The adapter returns refused:unsupported-or-unresolved-unit.

After refusal, queue remains [], allocated pen remains 0, and the caller state
is order-elm=rejected. Silently treating crate as item would fail this contract.

## Missing-context control

With catalog={} and unit=pack, the same request is refused with unchanged state.
The adapter cannot invent the contents of a pack.
The item-unit path does not need pack context: amount=2, unit=item maps to 2 items.

## Requirement and limits

For these participants, a supported quantity shall preserve its item meaning;
accepted shall display pending, and applied shall display completed only after
the promised allocation exists. Treat this as an illustrative requirement;
confirm with the user/stakeholder.

The fixture covers unit conversion, missing conversion context, and outcome meaning.
It does not cover duplicate delivery, partial allocation, field-clearing semantics,
or every participant revision; keep those claims open.
