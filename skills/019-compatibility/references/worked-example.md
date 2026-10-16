# Shared-settings coexistence example

This is a synthetic repository fixture, not a claim about an actual product.
Treat its preservation criteria as illustrative defaults; confirm with the
user/stakeholder before using them as requirements.

## Filled record

| Input | Value |
| --- | --- |
| Components | report-tool revision amber; preview-tool revision birch |
| Shared environment | one settings dictionary owned by the fixture host |
| Initial persistent state | empty dictionary |
| report-tool setup | saves theme dark; renders report header using its saved theme |
| preview-tool setup | saves theme light; renders preview header using its saved theme |
| Protected outputs | report header dark; preview header light |
| Neighbor lifecycle | setup, launch, update preferences, remove preview-tool |
| Allowed interference | none for either component's theme |
| Fixture owner | repository maintainer role |
| Observation | settings dictionary and rendered header values |
| Exclusions | no dependency-resolution or operating-system compatibility claim |

## Standalone controls

With empty state, report-tool writes `theme=dark` and produces
`report-header:dark`.
Reset the dictionary.
With empty state, preview-tool writes `theme=light` and produces
`preview-header:light`.
Both protected standalone operations pass.

## Failing combined run

Start from empty state.
Run report setup, then preview setup.

```text
state = {theme: light}
report output = report-header:light
preview output = preview-header:light
```

The report result differs from its standalone contract.
The fixture records both writes to the same key, establishing the collision
within this dictionary model; it says nothing about other host resources.

Reverse setup order after resetting state:
`state={theme:dark}`; report stays dark but preview incorrectly becomes dark.
Calling the pair compatible would hide an order-dependent failure.

## Remediation and after state

Change both settings accessors to component-scoped keys.
Give removal an explicit component-key ownership filter.

```text
after both setups:
  (component, report-tool, theme): dark
  (component, preview-tool, theme): light
outputs:
  report-header:dark
  preview-header:light
after preview preference changes to sepia:
  report-header:dark
  preview-header:sepia
after removing preview:
  state = {(component, report-tool, theme): dark}
  report output = report-header:dark
```

Reset and reverse setup order: the same protected pair remains dark/light.
The removal check also preserves the report-owned key.

## Negative and reporting boundary

A deliberately broken remover that clears the entire dictionary still fails:
report theme becomes missing after preview removal.
Keep that failure as a check against broad cleanup.

Report that the scoped-key revision passes the named theme operations and
lifecycle actions in the fixture.
Leave dependency conflicts, concurrent file writes, and untested revisions
unverified; a dictionary example cannot establish their compatibility.
