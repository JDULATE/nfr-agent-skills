# Import-recovery teaching example

Use this synthetic contract for the example only. Ask the user for real recovery semantics.

## Contract and practice assets

In the fictional sandbox, an import with rejected records does not automatically
retry. A learner must inspect a rejection reason, correct the source, and create
a new attempt without claiming the original attempt was successful.
Practice `import-slate` rejects `record-amber` for a missing required category.
Assessment `import-mint` rejects another record for a different known invalid category.
Both demand interpreting the reason and correcting category input; neither adds a new skill.
The fictional allowed categories are `operations` and `sales`. Practice starts
with category absent; its key corrects it to `operations`. Assessment starts with
unsupported `archived`; its key corrects it to `sales`. Keep those keys with the
instructor, not in the learner assessment prompt. Successful output is a new
accepted attempt with the corrected record; the original rejection remains in history.

| Stage | Input/state | Learner output | Carried evidence |
| --- | --- | --- | --- |
| Explanation | Contract and rejection meanings | Identify original failed/partial result | Material/product revision |
| Guided exercise | import-slate plus correction hints | Corrected source and new accepted attempt | Hints recorded |
| Reset | Modified sandbox fixture | Original rejection state restored | No accepted attempt left for next learner |
| Assessment | import-mint; answer-bearing steps withheld | Independently corrected source and new result | Output, reasoning, help retained |

## Specification example

Illustrative assessment scope; confirm with the user/stakeholder:
Use 2 changed-instance assessment cases with contrasting category corrections.
For the agreed prerequisites, require the confirmed task output and explanation
under the permitted assistance rule. No timing promise or credential is implied.

## Concrete negative case

If reset leaves an already accepted assessment result, a learner could point to
it without doing the recovery work. Reject that fixture and restore the declared
starting state before scoring. If the instructor names the category correction,
classify the result as assisted rather than independently demonstrated.

These are proposed assets and checks, not a training outcome. Passing this sandbox
would establish neither live-system permission nor retention after an untested delay.
