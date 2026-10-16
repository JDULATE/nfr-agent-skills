# Requirement-led removal decisions

Judge necessity against the accepted purpose, not personal style preferences.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| A fixed export always resolves the same formatter through a registry | Replace lookup/factory dispatch with a direct formatter call | New variants would require an explicit future design change | Compare fixed output and unsupported-format refusal before/after |
| A lifecycle wrapper has no effects in the supported path | Remove the wrapper after inspecting all registered hooks | Unadvertised consumers may be exposed by investigation | Search registrations and compare lifecycle event traces |
| Multiple internal paths implement the same fixed contract with no distinct role | Keep a justified path and remove the redundant route | Less internal substitution flexibility | Run retained contract cases and check external callers of the removed path |
| A new facade still invokes all unused framework layers | Remove the unjustified downstream machinery rather than rename it | Larger internal diff than a cosmetic wrapper | Inspect the executed path and remaining consumer graph |

## Direct fixed-path sketch

Illustrative pseudocode for the supplied export contract.

```text
export(rows, format):
    if format != "csv":
        return UnsupportedFormat
    payload = format_fixed_csv(rows)
    writer.write(payload)
    return Exported(payload)
```

This is appropriate only when format selection is not an accepted extension
surface and the fixed CSV behavior is fully specified elsewhere.
Preserve any real writer lifecycle requirements; this sketch does not justify
dropping them.

## Removal ledger

For each candidate, record actual consumers, required effects, retained substitute,
and any accepted loss of variation.
If the stakeholder confirms a plugin obligation, the registry may be justified.
Do not generalize a fixed-path example into a ban on registries or factories.
