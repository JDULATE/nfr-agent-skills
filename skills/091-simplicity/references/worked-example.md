# Removing dispatch from a fixed export

This synthetic example uses illustrative purpose and preservation defaults;
confirm with the user/stakeholder before adopting them.

## Filled purpose record

| Input | Value |
| --- | --- |
| Supported request | export rows as the fixed CSV representation |
| Rows | [{name: cedar}] |
| Supported format | csv only |
| Required payload | "name\ncedar\n" |
| Unsupported input | format=json |
| Required refusal | UnsupportedFormat, no writer output |
| Writer initial state | output absent, events=[] |
| Writer effect | store payload and append written |
| Registry state | {csv: CsvFactory}; no external registration API |
| Hook state | init_hooks=[], cleanup_hooks=[] |
| Accepted future variants | none supplied in this fixture |
| Owner | export maintainer role |

## Before executed path

```text
request -> empty_hook_wrapper.enter -> registry.lookup(csv)
        -> CsvFactory.create() -> formatter.format(rows)
        -> writer.write(payload) -> empty_hook_wrapper.exit
payload = "name\ncedar\n"
writer = {output: "name\ncedar\n", events: [written]}
```

Registry lookup and factory creation perform no required selection or side effect
beyond choosing the fixed formatter in this filled model.
The hook wrapper also has no registered effects.
Those facts are supplied by the consumer/effect ledger, not inferred from size.

The original json request returns UnsupportedFormat with output absent and events=[].

## Remediation and after state

Replace lookup, factory, and empty lifecycle dispatch with the direct path.
Reset writer to output absent and events=[].

```text
request -> format_fixed_csv(rows) -> writer.write(payload)
result = Exported("name\ncedar\n")
writer = {output: "name\ncedar\n", events: [written]}
```

The fixed formatter and writer behavior remain.
For format=json, return UnsupportedFormat with output absent and events=[].
No unsupported format is silently coerced to csv.

## Failing reduction candidate

A shorter candidate returns the formatted payload but removes writer.write.
With the same rows it returns the expected text, yet output remains absent and
events=[].
That candidate fails the retained writer-effect requirement and is rejected.

A facade that still calls registry.lookup and CsvFactory.create also fails the
specific mechanism-removal objective even when behavior is preserved.

## Changed-purpose control

Introduce a separately confirmed requirement for runtime third-party format
registration. That is outside this filled purpose; the previous removal decision
cannot be reused without reevaluating the accepted variation.
No such registration capability is claimed after the direct-path change.

## Limits

The example supports removal of unjustified fixed-path dispatch in this model.
It does not measure faster execution, easier maintenance, or reader understanding.
Its local CSV fixture does not establish general CSV-format coverage.
