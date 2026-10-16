# Separating billing from invoice rendering

This synthetic extraction uses illustrative task and preservation criteria;
confirm with the user/stakeholder before adopting them.
Amounts are fixture minor-unit integers, not a financial policy.

## Filled whole-path record

| Input | Value |
| --- | --- |
| Original object | InvoiceSession with private lines and initialized flag |
| Lines | [{amount_minor: 700}, {amount_minor: 300}] |
| Initial billing state | initialized=false, calculated_total absent |
| Billing responsibility | sum supplied line amounts and produce invoice view |
| Rendering responsibility | format a supplied label and total as text |
| Required whole output | invoice:1000 |
| Proposed boundary value | {label: invoice, total_minor: 1000} |
| State ownership | billing owns calculation state; renderer owns no persistent state |
| Necessary coordination | caller passes completed view to renderer |
| Owner | invoice feature maintainer role |

All numbers are illustrative fixture values; confirm with the user/stakeholder
before using them as acceptance examples.

## Before: file-only extraction fails independence

A new renderer module receives InvoiceSession and reads
session._calculated_total after checking session._initialized.
The original whole path calculates then renders invoice:1000.
The extracted renderer called with no initialized billing object returns
BillingNotInitialized.

That failure demonstrates the supplied private-state coupling.
The mere presence of a renderer file has not established separability.

## Remediation and after carried state

Make calculation return the inert view and make rendering consume only that view.

```text
billing-only input:
  lines = [{amount_minor:700}, {amount_minor:300}]
billing-only result:
  {label:invoice, total_minor:1000}
billing state:
  calculation complete; no renderer initialized

render-only input:
  {label:invoice, total_minor:1000}
render-only result:
  "invoice:1000"
renderer state:
  none; no InvoiceSession constructed
```

The caller joins these operations and obtains invoice:1000, preserving the
filled whole-path result.

## Boundary negative

Give render-only input {label:invoice} with no total_minor.
The declared boundary validator returns MissingTotal and emits no invoice text.
The renderer must not load or calculate the missing total from billing internals.
A separate view {label:invoice, total_minor:400} renders invoice:400 without
constructing billing; this shows the field is actually consumed.

## Coupling mutant

Replace the inert view with a wrapper that calls session._calculated_total
when total_minor is read. Without billing initialization, render-only execution
again returns BillingNotInitialized.
The independent exercise detects this hidden dependency.

## Limits

The example has no cross-part mutable invariant, transaction, or remote boundary.
It does not establish that production billing can become a separate service,
or that all domain responsibilities should be split this way.
