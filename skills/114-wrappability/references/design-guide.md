# Retained-implementation wrapper decisions

Use the native contract as the preservation baseline.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Structured endpoint reports success for native missing-item output | Map native result variants explicitly | More boundary outcome states | Compare success, missing, and engine-failure cases |
| Wrapper duplicates reservation logic instead of calling the engine | Translate inputs into the retained public operation | Wrapper remains dependent on the native contract | Trace native invocation and compare its source identity |
| An automatic retry reserves stock again | Remove replay unless native semantics establish it as safe | Ambiguous completion may need visible unresolved handling | Inspect call count and stock change for one boundary request |
| New interface accepts an unsupported asynchronous option | Refuse that request before calling the native operation | The boundary advertises less capability | Send the option and verify refusal with no native call |

## Mapping sketch

Illustrative pseudocode for a local synchronous reservation engine.

```text
reserve_api(request):
    if request.mode != "sync":
        return UnsupportedMode
    if not valid_native_quantity(request.units):
        return InvalidUnits
    result = legacy.reserve(request.sku, request.units)
    if result.kind == "reserved":
        return {state: "reserved", sku: result.sku, units: result.units}
    if result.kind == "missing":
        return {state: "rejected", reason: "missing-item"}
    if result.kind == "insufficient":
        return {state: "rejected", reason: "insufficient-stock"}
    if result.kind == "engine-fault":
        return {state: "failed", reason: result.reason}
    return {state: "unresolved", reason: "unknown-native-outcome"}
```

The sketch makes no automatic second call.
Validate the complete boundary input before invoking the native operation.
Any unknown native outcome needs an explicit unresolved/failure mapping, not success.

## Boundary limits

The engine remains the implementation of reservation.
A remote transport around it would introduce additional delivery and ambiguous
completion questions; this local fixture does not resolve them.
