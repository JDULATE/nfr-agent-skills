# Recipient handoff decisions

Start with what changes hands and what acceptance means for the recipient.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| The export contains handles the recipient cannot resolve. | Include the required assets or a confirmed recipient resolution path. Packages may become larger. | Open every required linked asset in the recipient context. |
| Source identities have no recipient equivalent. | Use an approved mapping or stop as incomplete. Some handoffs may need human decisions. | Import an unmapped assignee and inspect the explicit failure rather than a silent default. |
| Package creation is mistaken for recipient acceptance. | Stage the unit and validate recipient usability before acceptance. More lifecycle states are needed. | Produce a well-formed package with a missing asset and verify it cannot complete the handoff. |
| Source responsibility ends while acceptance is pending. | Keep source disposition as a separate confirmed step. Duplicate staged copies may temporarily exist. | Withhold acceptance and inspect that source responsibility remains unchanged. |
| A schema/unit conversion changes meaning. | Declare the semantic mapping and compare the interpreted result. A superficially successful import may be rejected. | Compare the source and recipient value under the approved units and mapping. |

## Staged handoff sketch

```text
package = build_unit_and_required_assets(source_unit)
mapped = apply_confirmed_recipient_mapping(package)
staged = recipient_stage(mapped)
if not validate_recipient_use(staged):
  return handoff_incomplete(source_responsibility_unchanged)
receipt = recipient_accept(staged)
apply_confirmed_disposition(receipt)
```

This sketch orders responsibilities; it does not supply a distributed transaction.
A lost receipt or failed disposition remains pending/uncertain until reconciled.

## Boundary decisions

Copying content and transferring responsibility are different outcomes.
Ask the user which outcome is requested and which source data must remain.

Recipient acceptance does not by itself grant permissions beyond the existing policy.
Use that policy when applying any assignment or source-release step.
