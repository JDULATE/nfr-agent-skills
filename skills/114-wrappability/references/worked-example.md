# Structured entrypoint around a retained reservation engine

This synthetic engine and its preservation criteria are illustrative;
confirm with the user/stakeholder before adopting them.

## Filled native and boundary contracts

| Input | Value |
| --- | --- |
| Retained engine | legacy.reserve revision amber; source unchanged |
| Native operation | reserve(sku, units) |
| Native initial stock | {pen:5} |
| Native success input | sku=pen, units=2 |
| Native success | reserved(pen,2); stock pen becomes 3 |
| Missing item input | sku=lamp, units=2; result missing; no mutation |
| Engine-failure fixture | result engine-fault:offline before mutation |
| New input envelope | {sku:pen, units:2, mode:sync} |
| Allowed unit input | positive integer; native engine checks availability and returns insufficient on excess |
| Unsupported mode | async |
| Initial call trace | [] |
| Owner | reservation-boundary maintainer role |

All quantities and cases are illustrative; confirm with the user/stakeholder.

## Before: envelope hides native rejection

The old wrapper calls reserve(lamp,2), receives missing, and always returns
{state:reserved, sku:lamp, units:2}.
Stock remains {pen:5}; trace=[reserve(lamp,2)].
The wrapper reports an effect that the retained engine did not perform.

## Remediation and comparison

Map native outcomes explicitly and validate unsupported requests before calling.
Each comparison starts with stock={pen:5}, trace=[].

| Path and input | Boundary/native output | Final stock | Call trace |
| --- | --- | --- | --- |
| native reserve(pen,2) | reserved(pen,2) | {pen:3} | [reserve(pen,2)] |
| wrapped pen/2/sync | {state:reserved, sku:pen, units:2} | {pen:3} | [reserve(pen,2)] |
| wrapped lamp/2/sync | {state:rejected, reason:missing-item} | {pen:5} | [reserve(lamp,2)] |
| wrapped pen/2/sync with offline fault | {state:failed, reason:offline} | {pen:5} | [reserve(pen,2)] |
| wrapped pen/0/sync | InvalidUnits | {pen:5} | [] |
| wrapped pen/2/async | UnsupportedMode | {pen:5} | [] |

The local wrapper and native success preserve the same stock effect.
The old native entrypoint still calls revision amber.
No native source edit or replacement implementation is involved.

## Replay failing control

A mutant wrapper calls reserve(pen,2) twice for the same request.
Starting from pen=5, the calls leave pen=1 and trace contains both invocations.
A single reserved response would conceal the extra mutation.
The effect and call-count checks reject that wrapper.

## Insufficient-stock mapping

With initial pen=1, request pen/2/sync produces native insufficient without mutation.
The declared mapping returns {state:rejected, reason:insufficient-stock};
stock stays {pen:1}, trace=[reserve(pen,2)].
An implementation must add this native variant to the mapping rather than let
a generic fallback imply success.

## Limits

The fixture covers local synchronous calls with deterministic outcomes.
It does not establish retry safety, remote delivery semantics, cancellation,
or recovery after an unknown completion state.
