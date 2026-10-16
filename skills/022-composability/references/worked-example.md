# Chaining stages through a borrowed stream

This synchronous model is synthetic.
Its ownership and result defaults are illustrative; confirm with the
user/stakeholder before adopting them.

## Filled join record

| Input | Value |
| --- | --- |
| Stages | header, report body, footer |
| Stream owner | caller running the chain |
| Initial stream | open, content="", close_events=[] |
| Header behavior | write "H|" without closing |
| Body output | write "B|" |
| Footer behavior | write "F" without closing |
| Whole success | content="H|B|F", stream closed by caller |
| Primary failure case | body reports BodyFailed before its write |
| Failure output policy | keep partial "H|"; report BodyFailed |
| Secondary failure case | caller close records CloseFailed and stream remains open |
| Boundary error policy | primary stage error preserved; cleanup error reported separately |
| Owner role | report-pipeline maintainer |

## Before: local success breaks the join

The standalone body stage assumes it owns the stream.
It writes B| and closes it.
Composed execution yields:

```text
header: content="H|", stream=open
body: content="H|B|", stream=closed, close_events=[body]
footer: WriteOnClosed
whole result: failure
```

The body produced its local output, but its lifetime guarantee conflicts with
the footer's precondition.

## Remediation and after state

Give the body an explicit borrowed-stream contract.
Keep finalization at the caller boundary.

```text
header: content="H|", stream=open
body: content="H|B|", stream=open
footer: content="H|B|F", stream=open
caller finalization: stream=closed, close_events=[caller]
whole result: success
```

Each trace starts from the same empty open stream.
The accepted chain has the filled result and ownership outcome.

## Stage failure and cleanup controls

Reset stream to open/empty with close_events=[].
Configure body to report BodyFailed before writing.
Header writes H|; body fails; footer is not run.
Caller closes the stream: content="H|", stream=closed, close_events=[caller].
Boundary result is BodyFailed with no cleanup finding.

Reset again and also configure caller close to fail.
After body failure: content="H|", stream=open,
close_events=[caller:CloseFailed].
Boundary result remains BodyFailed with cleanup finding CloseFailed.
The open resource is reported unresolved, not falsely finalized.

## Failing mutant

Restore body-owned close while keeping the new composition wrapper.
The footer still receives a closed stream and fails.
The actual join trace detects the violation even if all standalone stage tests pass.

## Limits

The fixture demonstrates lifetime composition and failure preservation only.
It does not validate concurrency, retrying writes, streaming cancellation,
or arbitrary stage reordering.
