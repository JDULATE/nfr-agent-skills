# Interaction-burden decisions

Assess an explicit scenario before choosing a simplification.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| A refresh callback can reenter the save path | Separate refresh from persistence and define the phase boundary | More explicit operation roles | Trace flag-enabled and disabled cases and inspect whether refresh can reenter save |
| Flags are evaluated independently although their combinations change effects | Replace scattered checks with an explicit supported-combination decision record | The record must change with supported modes | Compare each supported combination with its actual effects |
| Multiple modules decide the same ordering constraint | Give that decision an explicit coordinating boundary | A coordinator becomes a dependency | Inspect which participants still need to know the ordering rule |
| A facade hides callbacks without changing them | Document actual downstream edges or remove a justified dependency | Documentation alone does not reduce runtime interaction | Compare reachable traces, not facade method count |

## Phase sketch

Illustrative pseudocode for the callback fixture.

```text
save(value, refresh_enabled, notify_enabled):
    persist(value)
    if refresh_enabled:
        refresh_cache_from_value(value)
    if notify_enabled:
        publish_saved(value)

refresh_cache_from_value(value):
    cache = value
    // no callback into save
```

This breaks the modeled feedback only if registration code does not add another
path back to save. Inspect actual subscriptions before accepting that conclusion.

## Reachability record

For each supported choice combination, record activated edges, shared state,
termination condition, and required effects.
A bounded trace that stops on a repeated state identifies reachable feedback;
it does not establish how a real unbounded execution terminates.
Do not remove required notifications merely to shorten the trace.
