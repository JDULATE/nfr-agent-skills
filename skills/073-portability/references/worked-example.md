# Report-root portability example

Use these illustrative synthetic profiles, not real operating-system assumptions.
All fixture values and the proposed adaptation surface are illustrative examples;
confirm with the user/stakeholder before applying them.

## Filled migration record

| Field | Fixture value |
| --- | --- |
| Software / input | report-renderer fern / key alpha, value 7 |
| Domain output | header key,value followed by row alpha,7 |
| Artifact name | report-elm.csv |
| Source profile | working directory artifact-store; required root artifact-store |
| Target profile | working directory scratch-store; required root artifact-store |
| Shared capabilities | both profiles support declared named-artifact writes |
| Initial artifact state | artifact-store and scratch-store empty |
| Allowed adaptation | platform root resolver and target profile configuration |
| Preserved surface | renderer input, row content, artifact name, required root |
| Generated/native artifacts | none in this fixture |
| External dependencies | none |
| Carried state | created artifact remains in its recorded store |

## Before migration

The source implementation writes report-elm.csv relative to its working directory.
On the source profile the artifact appears in artifact-store and satisfies the contract.
The exact file text is:
```text
key,value
alpha,7
```

On the target profile the same writer puts it in scratch-store.
Rendering succeeds and bytes match, but the required artifact-store result is absent.
The fixture isolates an implicit directory assumption, not a real host failure.

## Remediation

Resolve the required artifact root from the explicit profile.
Keep the domain renderer unchanged.

| Profile | Current directory | Explicit root | Artifact location | Result |
| --- | --- | --- | --- | --- |
| source | artifact-store | artifact-store | artifact-store/report-elm.csv | preserved |
| target | scratch-store | artifact-store | artifact-store/report-elm.csv | preserved |

Both runs start from empty stores and produce the exact content above.
No domain source changes are needed for this constructed adaptation.

## Failing capability case

Use target-without-store, identical to the target profile except it cannot write
artifact-store. The capability check must report unsupported required output.
It must not silently write scratch-store and call the migration complete.

## Adaptation ledger

Assumption: current directory equals required output root.
Source: that assumption happens to hold.
Target: it does not hold.
Intervention: explicit platform artifact-root resolution.
Preservation evidence: same content and required location after the adapter change.
Unchanged boundary: domain renderer and input format.

## Requirement example and limits

Across the declared source and target profiles, report-renderer fern shall produce
the specified report in artifact-store using only the permitted adapter/configuration
change, or report the missing required capability.

This fixture does not establish a real runtime port, filesystem permissions,
native-artifact support, elapsed effort, or compatibility with every host.
