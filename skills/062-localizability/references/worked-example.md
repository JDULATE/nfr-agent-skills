# Synthetic locale resource example

These profiles are deliberately synthetic, not real languages or regional standards.
All numeric values and proposed formats are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled canonical record

| Field | Fixture value |
| --- | --- |
| Operation / key | export / export_summary |
| Canonical amount | integer 1250 minor units; 100 minor units per fixture unit |
| Canonical date | calendar date 2026-04-05, not a time-zone instant |
| Resource inputs | amount display string; date display string |
| Profile plain amount / date | 12.50 / 2026-04-05 |
| Profile alternate amount / date | 12,50 / 05/04/2026 |
| Plain template | Amount {amount}; date {date} |
| Alternate template | Date {date}; amount {amount} |
| Plain / alternate operation label | Export / Prepare files |
| Machine representation | operation export; amount_minor integer 1250; date 2026-04-05 |
| Missing-resource policy | return unsupported-resource, not a successful locale claim |
| Language approval | none; both strings are synthetic mechanism fixtures |
| Carry | canonical record unchanged after either rendering |

The fixture-unit relationship above is a supplied model convention.
It does not describe any actual currency.

## Failing design before remediation

The business branch checks display_label == Export.
After a resource changes that label, the branch no longer selects export.
The same code also serializes the display amount into amount_minor and the
alternate display date into the machine date field.

The alternate output becomes:
```text
operation = not selected
amount_minor = "12,50"
date = "05/04/2026"
```

That changes a stable operation key, an integer amount type, and a canonical date.

## Remediation and after outputs

Select the operation through the stable key.
Render the whole supplied template using its named placeholders.
Keep machine serialization separate from display:
| Profile | Human summary |
| --- | --- |
| plain | Amount 12.50; date 2026-04-05 |
| alternate | Date 05/04/2026; amount 12,50 |

Both produce the same machine record:
```text
operation = export
amount_minor = 1250
date = 2026-04-05
```

The alternate resource reorders complete placeholders without changing canonical meaning.
Render plain, alternate, then plain with the same canonical record. The final
plain summary must equal the first; alternate selection must not leak into it.
Interpret 05/04/2026 only under the explicitly supplied alternate day/month/year rule;
do not infer its meaning for an arbitrary real audience.

## Missing-resource and date failure cases

Remove export_summary from alternate.
Return unsupported-resource according to the filled policy.
Do not report alternate supported because a plain fallback happened to render.

Treating the canonical date as an instant and shifting its day would violate this
fixture's calendar-date contract. No time-zone conversion is part of this example.

## Requirement example and limits

The resource boundary shall change the displayed order and supplied date/amount
formats while preserving operation export and the canonical machine record.

The fixture verifies mechanism and data boundaries only.
It does not validate linguistic correctness, a real locale's conventions,
bidirectional rendering, glyph support, screen layout, or legal requirements.
