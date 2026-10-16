# Join-contract decisions

A component's standalone default may not satisfy the assembled chain.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| A stage closes a stream that a later stage must use | Make ownership explicit and use a borrowed-resource mode | Caller must reliably finalize the resource | Trace writes and close events across the entire chain |
| A downstream precondition is not guaranteed by its producer | Introduce a checked adapter or change the join contract | Adapter may refuse inputs previously passed through | Exercise supported and unsupported upstream outputs at the actual join |
| Reordering stages changes side effects or output meaning | Fix the required order in the composition boundary | Fewer freely reorderable assemblies | Compare both orders with a case where the difference is visible |
| Cleanup failure masks the stage's original error | Return the primary error with a separate cleanup finding | Richer error handling at the boundary | Inject both failures and inspect which claim reaches the caller |

## Borrowed stream sketch

Illustrative pseudocode for a synchronous owner-managed stream.

```text
write_report(stream):
    // stream is borrowed; this function never closes it
    stream.write("body")

run_chain(stream):
    try:
        write_header(stream)
        write_report(stream)
        write_footer(stream)
    finally:
        owner_close(stream)
```

The sketch establishes a lifetime arrangement, not a complete error envelope.
When primary and cleanup failures can coexist, preserve both under the agreed
boundary policy instead of relying on an unspecified language exception default.

## Whole-path acceptance

Test the footer after the report stage; checking report output alone misses an
early close. Keep the open/closed state and primary error in the same trace.
If a stage owns an internal resource, its own cleanup can remain local;
borrowed mode is not a universal ban on stage cleanup.
