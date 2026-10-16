# Assembly decisions

Use the integration ledger to distinguish supplied pieces from new component work.

| Observed evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| A component requires a setting the host names differently | Map host names to constructor inputs at the composition root | Explicit mapping needs maintenance when interfaces change | Assemble with the host setting and inspect the component's actual binding |
| Startup reaches a component before a required binding exists | Validate prerequisites before constructing dependent pieces | Some formerly tolerated partial setups now refuse early | Remove a required input and inspect the named refusal and absence of downstream effects |
| Every connection requires editing private modules | Add a supplied interface or adapter seam and record that component work separately | Initial component work exceeds a glue-only scope | Inspect edited paths and connect through the published seam afterward |
| Authors manually register an endpoint outside the repo | Encode the registration as a declared prerequisite or reproducible setup step | Additional setup responsibility and ownership | Reconstruct from a clean declared state without the author intervening |

## Composition sketch

Illustrative pseudocode; names belong to this local fixture.

```text
compose(host_config):
    if not host_config.contains("jobs_address"):
        return MissingPrerequisite("jobs_address")
    transport = make_transport(host_config["jobs_address"])
    worker = make_worker(inbox=transport)
    return worker
```

This mapping establishes a binding, not message semantics.
Keep credentials and real endpoints outside fixture examples.
If the repository requires registration before transport creation, then include
that prerequisite rather than assuming construction creates it.

## Ledger fields

Record task, supplied artifact, actual edited path, responsible role, and outcome.
Distinguish glue edits from component implementation and environment preparation.
Use elapsed effort only under a confirmed counting procedure; file counts alone
do not establish that integration will be inexpensive for another team.
