# Measurement design decisions

Choose an intervention for a defective measurement procedure, not a performance target.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| Job creation includes time before admission to the queue. | Emit or locate an admission event and define the measured interval explicitly. Extra events cost collection work. | Compare creation-to-start and admission-to-start on the same fixture; name each separately. |
| Producers send durations in incompatible units. | Normalize through an explicit unit conversion while retaining source-unit metadata. Schema changes may affect existing queries. | Convert a known seconds value and compare it with its millisecond equivalent. |
| The instrument rounds away the needed distinction. | Use finer collection resolution where supported, or report a bound rather than a point value. Finer collection may add overhead. | Feed known inputs around the decision difference and inspect whether distinct values survive. |
| Duplicate or missing end events create fabricated durations. | Pair events by entity and phase, with an explicit duplicate policy and an unresolved ledger. This reduces the completed-value population. | Inject a duplicate end and an absent end; verify neither silently supplies another entity's duration. |
| One dashboard conflates completed and still-queued work. | Publish completed-pair summaries and unresolved counts as different outputs. Readers must interpret both. | Reconcile every fixture entity to a paired duration or unresolved entry. |

## Unit-aware sketch

```text
normalize(value, unit):
  if unit == "seconds": return value * 1000
  if unit == "milliseconds": return value
  return invalid_unit

pair(admission, start):
  require same_entity(admission, start)
  require same_clock_domain(admission, start)
  return normalize(start.value, start.unit)
         - normalize(admission.value, admission.unit)
```

The conversion constant is a unit definition, not a system target.
Reject a negative interval for review instead of silently clipping it to zero.
A clock-domain mismatch needs a supported mapping, not a guessed offset.

## Choosing the result type

Use a direct value when the observations support it.
Use an interval or a resolution-qualified value when the instrument supports only
that information. Use "unresolved" for missing observations, not an invented value.

If the stakeholder needs a distinction the collection source cannot represent,
say so before selecting an acceptance threshold. More decimal places in a chart
do not create additional observation precision.
