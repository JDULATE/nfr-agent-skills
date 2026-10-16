# Shard ownership move

Use this synthetic centralized fixture to inspect assignment authority.
Its ownership policy and fixture values are illustrative examples; confirm
with the user/stakeholder before adopting them.

## Filled inputs

| Field | Value |
| --- | --- |
| Allocation unit | shard cedar |
| Eligible nodes | node east and node west; both allowed to process cedar |
| Initial authority | owner east, revision amber, stage active |
| Source state | last accepted job Juno; completed set {Juno} |
| Target state | replica containing completed set {Juno}; no effect authority |
| New assignment | owner west, revision birch |
| Protected effect | append an accepted job identifier to the authoritative completed set |
| Handoff boundary | source quiesced with completed set {Juno} |
| Authority-loss policy | refuse effects |
| Allowed paused behavior | return paused without changing the completed set |
| Owner of policy | processing-service maintainer role |

## Failing implementation

The router is updated to west, but workers can append without checking authority.

```text
router: cedar -> west, birch
east receives delayed job Kestrel with revision amber
east result: applied
completed: {Juno, Kestrel}
```

East performed an effect after its assignment was retired.
This fixture demonstrates missing effect-boundary enforcement; it does not
simulate all possible message failures.

## Remediation trace

Add the serialized authority-and-effect gate shown in the design guide.
Begin again from completed set {Juno}.

| Stage | Authority / state | Attempt | Output and carried state |
| --- | --- | --- | --- |
| Quiesce | cedar paused; east retired | east/amber applies Kestrel | paused; completed remains {Juno} |
| Copy | target checkpoint {Juno}, matches source | west/birch applies Lark before activation | paused; completed remains {Juno} |
| Activate | west/birch active | east/amber retries Kestrel | stale-owner; completed remains {Juno} |
| Process | west/birch active | west/birch applies Lark | applied; completed becomes {Juno, Lark} |

The replica already possessed the checkpoint before activation.
That possession did not authorize the premature Lark attempt.

## Failing handoff branch

Reset to the quiesced source checkpoint {Juno}.
Deliberately provide target checkpoint {}.
The comparison fails, activation is withheld, and west's Lark attempt returns
paused with completed still {Juno}.
No automatic recovery or timeout is claimed by this fixture.

## Eligibility control

A proposed destination north is not in the eligible-node set.
Placement rejects north before copying; owner remains absent in paused state.
Adding north to a resource inventory would not alone authorize cedar placement.

## Requirement example and limits

For cedar, only the active authoritative owner at its current revision may
append jobs; a failed checkpoint comparison shall prevent target activation.
Treat this as an illustrative proposal; confirm with the user/stakeholder.

The trace supports the declared sequential authority model.
A real repository still needs evidence for atomic authority/effect enforcement,
authority service loss, and any network-partition behavior it promises.
