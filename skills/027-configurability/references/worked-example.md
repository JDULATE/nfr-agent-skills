# Worked example: absence and source precedence

Assume a fictional routing configuration offers `route` and `review_required`.
Its complete proposed combinations are `guided,true` and `direct,false`; other
pairs are invalid. These meanings are scenario assumptions, not a real product schema.
Defaults are guided with review. Team choices override defaults; request choices
then override team choices. Only supplied keys participate in that precedence.

Propose: "The resolver shall expose `{accepted_route_review_pairs}` with
`{absence_and_precedence_rules}`, rejecting `{unsupported_combinations}`, verified
by `{resolved_document_source_and_consumer_fixtures}`."
Illustrative unknown-key target only: 0 silently accepted unknown keys;
confirm with the user/stakeholder before accepting the schema or that bound.

```json
{"defaults":{"route":"guided","review_required":true},
 "team":{"route":"direct","review_required":false}}
```

| Request overlay | Expected resolved result / response |
| --- | --- |
| No keys | `direct,false`, both values from team |
| `review_required=false` | `direct,false`; explicit false is not absence |
| `route=guided` only | Reject `guided,false`; no silent repair to review=true |
| `route=guided, review_required=true` | `guided,true`, both values from request |
| `route=null` | Reject invalid route domain, not default guided |
| Unknown `routee=direct` | Reject under the proposed unknown-key policy |

Feed resolved valid pairs through the route consumer. Check guided selects its
review path and direct does not request review under these invented meanings.
A UI showing the request value while a downstream reader still uses defaults is
an accepted-but-unused choice, not successful configurability.

Carry the supplied/absent distinction and winning-source record through resolution;
do not use a truthiness merge that replaces false with true. This fixture tests
choice meaning, not applying a running arrangement or transporting in-flight jobs.
No actual resolver or consumer was executed by this fictional example.
