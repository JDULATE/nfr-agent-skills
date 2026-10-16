# Queue-delay measurement example

Use this illustrative fixture to check a measurement definition.
Fixture times and proposed handling are illustrative examples;
confirm with the user/stakeholder before adopting the procedure.

## Filled measurement record

| Field | Fixture value |
| --- | --- |
| Property / entity | residence in queue / job id |
| Start boundary | queue admission, not job creation |
| End boundary | first execution start |
| Clock domain | synthetic queue-clock for every event below |
| Source units | milliseconds for job-ash; seconds for job-birch |
| Output unit | milliseconds |
| Eligible population | job-ash, job-birch, job-cedar admitted in this fixture |
| Aggregation | arithmetic mean over valid completed pairs |
| Duplicate policy | first execution-start event by queue-clock order |
| Missing policy | unresolved pair; no duration imputed |
| Resolution | fixture stores exact integer milliseconds after conversion |
| Owner / query | synthetic queue owner / queue-residence query revision moss |
| Decision | whether the procedure recovers the known intervals, not whether delay is acceptable |

## Input events and carried state

| Entity | Created | Admitted | Execution start | Source unit |
| --- | ---: | ---: | ---: | --- |
| job-ash | 500 | 1000 | 1800 | milliseconds |
| job-birch | 1.5 | 2.0 | 2.6 | seconds |
| job-cedar | 2500 | 3000 | absent | milliseconds |

Each entity is unique. No retries, restarts, or duplicate starts occur in this fixture.
After collection, job-ash and job-birch are started; job-cedar remains queued.
Retain the admitted-but-unstarted record for job-cedar.

## Failing procedure before remediation

The original expression subtracts creation from execution start without unit
normalization and labels the arithmetic mean "queue delay, ms".

It produces 1300 for job-ash and 1.1 for job-birch, then reports 650.55 ms.
That number mixes units and includes pre-admission time.
The fixture establishes those definition errors; it says nothing about the
production queue's actual delay.

## Remediation

Pair admission with execution start and normalize each event to milliseconds.
The resulting completed durations are:
- job-ash: 1800 - 1000 = 800 ms.
- job-birch: 2600 - 2000 = 600 ms.
- job-cedar: unresolved because the start event is absent.

The completed-pair mean is (800 + 600) / 2 = 700 ms.
Report coverage as two valid pairs out of three admitted jobs, with job-cedar
listed as unresolved. These are illustrative fixture results, not accepted targets;
confirm with the user/stakeholder before using any number as a project criterion.

## Requirement example

The queue-residence procedure shall recover admission-to-first-start intervals
in milliseconds from the synthetic queue-clock fixture, report the completed-pair
mean separately from unresolved jobs, and preserve entity and source-unit lineage.

## Failing case after conversion

Replace job-birch's clock domain with external-clock while retaining its times.
The defined procedure must mark that pair unresolved until a supported clock
mapping exists. Unit conversion alone cannot establish a cross-clock interval.

## Limits

This fixture demonstrates the measurement calculation and its invalid-pair handling.
It does not establish acceptable production queue delay, explain why jobs wait,
or validate accuracy of an actual clock source.
