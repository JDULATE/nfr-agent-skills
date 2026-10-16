# Stewardship decisions

Start from an accepted operational-energy or useful-device-life objective.
Do not select a greener label or a newer device as the objective by default.

## Decision table

| Observed evidence | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Metered energy follows repeated identical computation | Coalesce that computation within the approved task scope | Retained state or setup can increase other costs | Compare complete metered energy and unchanged useful outputs over the chosen horizon |
| Unbounded historical working state makes an otherwise usable device fail its task | Bound live working state and release unneeded completed-task buffers | Reconstruction work may grow; needed historical content must remain available | Exercise the task horizon on the retained device profile and inspect service adequacy |
| Optional background work holds a device active between required tasks | Schedule it into approved activity windows or disable only unneeded work | Delayed background results may violate the service contract | Meter the complete period including idle time and test background deadlines |
| A proposed replacement saves operational energy but other lifecycle stages lack evidence | Keep a conditional operational comparison and defer the net-impact decision | A decision can remain open despite a favorable running measurement | Show acquisition/retirement evidence separately and inspect continued useful service |

## Bounded working-state sketch

Pseudocode for a device-life candidate whose completed-task buffers are disposable.
Do not evict required durable records or violate the approved retention policy.

~~~text
finish_report(report):
    publish_required_output(report)
    release_temporary_pages(report)
    discard_disposable_preview(report)
    keep_only_current_job_working_state()
~~~

If old outputs remain required, provide their approved retrieval route before
discarding a preview. Verify continued task delivery through the chosen review event;
a small working set alone is not evidence of longer useful device service.

## Evidence boundaries

Keep measured, allocated, modeled and unknown quantities explicit with their sources.
Use the same functional output, idle allocation and horizon for an energy comparison.
Include shifted devices and remote work or limit the conclusion to the local boundary.
A CPU ratio is not a metered energy result. A conversion to emissions needs
supported factors and source/context limits; Ask the user when those are unknown.
Keeping a device or buying a new one has no universal lifecycle preference.
