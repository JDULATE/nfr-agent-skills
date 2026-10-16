# Rising arrivals with a completion plateau

This fictional fixed-resource series keeps the operation, data mix and required
result unchanged. No rejected work is hidden outside the offered-work record.

## Illustrative growth observations

Illustrative inputs and measurements; confirm with the user/stakeholder:
The fixture has no rejections; excess admitted work accumulates as backlog.

| Offered work/s | Correct completions/s | Unserved rate/s | Completed p95, ms |
| ---: | ---: | ---: | ---: |
| 50 | 50 | 0 | 100 |
| 100 | 90 | 10 | 250 |
| 200 | 90 | 110 | 800 |

Illustrative acceptance proposal; confirm with the user/stakeholder:
For the agreed sustained points, match offered useful demand without growing
backlog and keep the required completion budget at 300 ms. The middle point's
completed timing looks acceptable, but its accumulating work still fails the
proposed service envelope. The largest point also exceeds the timing proposal.

## Carried resource and causal limits

Keep the resource amount fixed for this series. An added-worker experiment must
be a separate labeled resource series with useful results and cost retained.
The plateau does not prove whether a store, serial coordinator, hot partition
or generator is responsible; inspect that actual path before choosing a fix.

## Verification boundary

Offer the declared axis with the actual input/skew assumptions and check source
capacity. Preserve failed points and actual observation duration; a finite passing
point cannot establish unlimited or linear future growth. No real load or capacity
measurement was executed here.
