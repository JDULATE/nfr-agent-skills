# Batching under a supplied cost model

This synthetic workload, rate table, cap, and acceptance criteria are illustrative;
confirm with the user/stakeholder before adopting them.
Cost units below are fixture units, not market prices or a currency conversion.

## Filled workload and ledger

| Input | Value |
| --- | --- |
| Budget period | launch window amber |
| Required jobs | job-cedar:[a,b]; job-maple:[c,d]; job-oak:[e,f] |
| Provider behavior | render each supplied id as rendered-id |
| Supported batch | each job's pair can be submitted together with identical per-id output |
| Initial artifacts | [] |
| Required final artifacts | [rendered-a,rendered-b,rendered-c,rendered-d,rendered-e,rendered-f] |
| Setup cost | 20 cost units |
| Fixed period cost | 10 cost units |
| Charging rule | 4 cost units per provider request, independent of this supported batch size |
| Other priced items | none in this model |
| Illustrative cap | 50 cost units; confirm with the user/stakeholder |
| Owner | export-budget maintainer role |

## Before: full workload exceeds the model cap

The implementation sends each id in a separate request.
Request trace=[a,b,c,d,e,f].
Artifacts are the required six rendered outputs.

Modeled total = 20 + 10 + (6 * 4) = 54 cost units.
The full workload fails the illustrative 50-unit cap.
Successful rendering alone does not settle budget fit.

## Remediation and after carried state

Use the fixture provider's supported batch operation for each job.
Reset artifacts=[].

```text
requests = [[a,b], [c,d], [e,f]]
artifacts = [rendered-a,rendered-b,rendered-c,rendered-d,rendered-e,rendered-f]
priced_request_count = 3
modeled_total = 20 + 10 + (3 * 4) = 42 cost units
decision = fits-model
```

All numeric values and decisions are illustrative;
confirm with the user/stakeholder.
The named outputs remain unchanged; setup and fixed charges remain in the total.

## Failing scope reduction

A mutant sends only [a,b,c] individually and drops the other required ids.
Its modeled total is also 42, but artifacts=[rendered-a,rendered-b,rendered-c].
It fails the original workload even though the total fits.
It cannot be reported as an affordable implementation of all required jobs.

## Charging-model control

Under an alternative supplied model charging 4 per record instead of per request,
both implementations cost 20 + 10 + (6 * 4) = 54.
Batching still reduces calls but does not establish a monetary saving in that model.

## Limits

These calculations establish only the filled model comparison.
Actual prices, provider availability, batch failure handling, billing periods,
and additional charges are not verified by this fixture.
