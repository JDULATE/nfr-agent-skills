# Keeping a device useful by bounding temporary state

This is a fictional device-profile simulation, not a prediction of hardware life.
All numeric fixture values and targets are illustrative examples;
confirm with the user/stakeholder before adopting a service-life requirement.

## Filled useful-service and review record

The stakeholder's example objective is continued report service on device-slate
until review-slate after 20 simulated shifts, with one report per shift.
The example policy permits the unchanged software/device profile through that
review event; it grants no indefinite support or security assurance.
Hardware faults and future software changes are outside this simulation.

Device memory allowance is 128 MiB, with 32 MiB base state.
Each report needs a 24 MiB temporary preview buffer. Its completed required output
is a 1 MiB file in the same device's output spool, which has 64 MiB free.
Inputs J01 through J20 use payload amber; file Jnn must contain exactly Jnn:amber.
Each task finishes before the next shift in this model; no other work, network
dependency, retry or concurrency occurs. Preview buffers are disposable under
the supplied policy; completed output files must remain readable at the review.
The evidence source is the simulated allocator plus exact file/content ledger.

## Before: retain every completed preview

The application retains each temporary buffer after writing its required file.
After J04, modeled memory is 32 + 4 * 24 = 128 MiB.
J05 requests a further buffer, requiring 152 MiB, so the allocator refuses it.
Its required file is absent; later jobs are not attempted after that failure.
No device-life extension is accepted from the fact that the device still powers on.

## After: release the disposable buffer on completion

Publish the required local file, then release that task's temporary pages/preview.
No file is deleted or moved to an unmeasured device.
Memory returns to 32 MiB between jobs and peaks at 56 MiB during each task.
At review-slate, J01 through J20 have all completed with exact readable contents;
the spool uses 20 MiB. No replacement device or extra memory was introduced.

| Check | Before | After |
| --- | --- | --- |
| Completed files | J01-J04 | J01-J20 |
| First failed job | J05, allocation refused | None in simulated horizon |
| Peak allocated memory | 128 MiB; next requested peak 152 MiB | 56 MiB |
| Memory between completed jobs | Grows by retained previews | Returns to 32 MiB |
| Physical device / spool | device-slate / same local spool | Unchanged |

## Decision and limits

The remedy supports this selected useful-service extension through review-slate.
It does not prove lower energy, net environmental benefit, longer physical hardware
life or safe operation after the approved review. Acquisition, retirement and
physical-failure evidence are explicitly unavailable. If previews were required
records rather than disposable working state, this remedy would not be authorized.
No actual device, memory allocator, retention decision or maintenance approval was tested.
