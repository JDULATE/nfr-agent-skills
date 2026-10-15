# Worked example: the night-dispatch recipe

Assume a fictional product already supports `workflow=reviewed|direct` and
`layout=compact|wide`. A night-dispatch team needs explicit review before release
and a saved manifest after release; compact layout is a preference. These are
stakeholder-supplied scenario constraints, not universal dispatch obligations.

Propose: "For `{night_dispatch_context}`, `{supported_recipe}` shall satisfy
`{review_before_release_and_saved_manifest}` under `{team_actor_tasks}`, preserving
`{day_dispatch_baseline}`, verified by `{need_choice_and_state_fixture_matrix}`."
Illustrative fit bound only: 0 unmet agreed must-haves in these selected fixtures;
confirm with the user/stakeholder before adopting needs, recipe, or scope.

| Context need | Supported choice / test | Concrete state or result |
| --- | --- | --- |
| Night review before release | `workflow=reviewed`, actor `night-agent` | `parcel-umber`: awaiting-review stays unreleased when previewed |
| Manifest on release | Existing reviewed-route commit | After approval/release: released, manifest `manifest-umber` saved |
| Compact layout preference | `layout=compact` at night scope | Night task uses compact presentation without bypassing review |
| Day context retains its accepted direct route | No global default change; day recipe remains direct/wide | Fresh day task still follows direct release and writes its manifest |
| Request for a new handwritten dispatch rule | No existing choice in this fictional product | Explicit unsupported need; priority/authorship decision remains open |

Initial night state is `parcel-umber: awaiting-review, manifest=absent`. Apply the
night recipe from that declared start, preview without release, then exercise its
accepted approval/release action. Inspect both state changes and persisted manifest,
not just the selected mode displayed on a settings page.

Carry the scope selector and recipe values through the task. A global reviewed
default that unexpectedly changes the day context fails the declared preservation
check even if night tasks pass. A private source patch implementing the handwritten
rule is new behavior, not evidence that supported choices already fit that need.
The fit claim covers the confirmed must-haves above; the additional unsupported
request remains unresolved rather than being relabeled a preference. No production
workflow or live arrangement transition was exercised by this example.
