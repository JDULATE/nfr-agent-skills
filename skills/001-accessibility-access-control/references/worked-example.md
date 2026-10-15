# Paired branch examples

These are separate fictional contracts, not findings about an installed application.

## Accessibility: correction inside a dialog

The user opens a report dialog with a keyboard, submits an empty required subject,
receives an error, corrects it, and closes the dialog. The intended task is creating
the report; merely reaching the opening button is insufficient.

| Input/event | Required interaction output | Carried state |
| --- | --- | --- |
| Open report dialog | Task-relevant focus and meaningful controls | Invoking control retained for return |
| Submit empty subject | Error meaning exposed in agreed interaction mode | Existing valid input preserved |
| Correct subject | Submit remains operable | Corrected value and report task result |
| Close dialog | Usable continuation/return | No lost focus on removed content |

## Access Control: valid role in the wrong team

Actor `editor-slate` may edit `report-mint` only within `team-amber` under the
example policy. `report-coral` belongs to another team. A direct update to it
must not change its contents even if the interface hides that action.
After the editor's grant is revoked, apply the stakeholder-confirmed validity
rule to a pending update rather than inventing a universal revocation delay.

| Action input | Expected permission effect | Control evidence |
| --- | --- | --- |
| editor-slate updates report-mint within grant | Approved update | Allowed action remains functional |
| editor-slate directly updates report-coral | No forbidden mutation | Scope policy enforced outside UI |
| Update after changed grant | Confirmed changed-authority decision | Actual final contents inspected |

## Proposed branch gates

Illustrative examples; confirm with the user/stakeholder:
Use 0 task-blocking barriers for the agreed dialog scenarios and 0 forbidden
mutation effects for the agreed permission cases. These independent gates do
not establish universal accessibility, standards compliance, or all authorization policy.
No keyboard/assistive session or real permission effect was executed here.
