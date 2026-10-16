# Responsibility-split decisions

Choose a cut that can be exercised through an explicit contract.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Extracted renderer reads billing's private fields | Supply a billing result value containing only required rendering data | Boundary value must evolve when rendering needs change | Render from the value without constructing billing |
| Both extracted parts mutate the same private object | Assign state ownership and expose explicit operations or immutable results | Some operations remain coordinated | Inspect writes and run each task with only declared dependencies |
| Constructors initialize unrelated services to perform a local task | Move construction to the caller and accept the task's actual dependency | More explicit assembly code | Exercise the task without the unrelated service |
| A proposed process split divides an invariant with no coordination mechanism | Keep that state under a common owner until a valid boundary exists | Less independent deployment than requested | Check the invariant at each allowed state transition |

## Boundary-value sketch

Illustrative pseudocode for billing and presentation separation.

```text
calculate_invoice(lines):
    total = sum(line.amount_minor for line in lines)
    return InvoiceView(label="invoice", total_minor=total)

render_invoice(view):
    if not view.contains("total_minor"):
        return MissingTotal
    return view.label + ":" + decimal_text(view.total_minor)
```

InvoiceView is inert data in this fixture, not a wrapper around a live billing
object. The caller assembles the tasks; rendering does not invoke calculation.

## Boundary challenge

Remove access to the billing object when testing rendering.
If a field needed by rendering is absent, add or reject it through the explicit
contract rather than letting the renderer rediscover it in private state.
A split may retain a common state owner without becoming an independent service.
