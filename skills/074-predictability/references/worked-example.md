# Consistent results that are too slow

This hypothetical task preserves its required result in both candidates.
The accepted absolute deadline and variation criterion are separate obligations.

## Illustrative observations

Illustrative fixtures and targets; confirm with the user/stakeholder:
Propose an observed range of at most 50 ms and an independent 300 ms deadline.

| Trace | Completion observations, ms | Observed range, ms | Result against proposed rules |
| --- | --- | ---: | --- |
| Baseline | 100, 100, 800 | 700 | Range fails; slow case exceeds deadline |
| Uniformly slow candidate | 900, 910, 905 | 10 | Range passes; absolute deadline fails |

The finite candidate observations do not establish that future outcomes cannot
vary more. Passing a spread rule cannot waive the independent timing obligation.

## Carried conditions and missing outcome

Retain input/data, load, device/config and warm-state group for each trace.
If the slow baseline case was a distinct cold condition, report that group and
its scope rather than blaming an unexplained within-group spread automatically.
If another task never finished, preserve it as pending/censored; the completed
observations' narrow range says nothing conclusive about that unknown outcome.

## Requirement and verification

Under confirmed condition groups, compare raw outcomes with the agreed range,
eligibility and absolute limits. Trace rare branches and retain inconvenient
extremes rather than dropping them. A stable average, frozen control or selected
quiet window is not the specified distribution evidence.
No actual timing trial, exceptional-path diagnosis or future guarantee is supplied here.
