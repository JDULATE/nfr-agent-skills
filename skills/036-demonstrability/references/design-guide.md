# Demonstration design decisions

Use this guide when a reviewer cannot inspect the consequence being claimed.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| A decline banner is visible but the payment ledger is hidden. | Add a scene-bound, read-only receipt of charge state. Expose synthetic identifiers only; the extra inspection is less theatrical. | Match scene id, attempt id, banner, and ledger entry status. |
| Only the author's account can reach the scenario. | Ship a synthetic fixture loader and a reset action scoped to that fixture. Reset support adds upkeep and must not target live accounts. | Replay from a new fixture instance using the written actions. |
| A provider is unavailable in the demo environment. | Substitute the response boundary and visibly label simulation. This shows local handling, not provider behavior. | Inspect mode on both screen and receipt; verify the local handler actually ran. |
| A recording splices unrelated steps together. | Capture one scene's ordered actions and final receipt together. A longer recording may be needed. | Compare the scene identity throughout and reproduce the same actions. |
| Reviewers need to see a refusal, but only success is scripted. | Add the contrasting rejected action and forbidden-state check. The scene set grows without becoming exhaustive coverage. | Show refusal output and inspect that the prohibited effect is absent. |

## Tool-agnostic scene sketch

```text
fixture = load_synthetic_scene("declined-payment")
show_label(scene=fixture.scene, provider_mode="simulated")
submit_payment(scene=fixture.scene, response="declined")
receipt = inspect_scene_read_only(fixture.scene)
show(receipt.message, receipt.attempt, receipt.charge_state)
assert receipt.charge_state == "absent"
```

Keep the assertion visible or export its result with the scene identity.
Do not implement the demo by returning the expected receipt without executing
the local payment handling being claimed.

## Scene handoff

Publish the initial fixture, action sequence, expected visible result, inspection
location, simulated boundary, reset behavior, and replay command category.
Include the failure path in that handoff if refusal is part of the shown claim.
Keep publication or live-provider use outside the fixture unless authorized.

If the audience cannot access the inspection artifact, narrow the demonstration
claim or provide an authorized synthetic view. Do not silently replace
inspectability with the author's assurance.
