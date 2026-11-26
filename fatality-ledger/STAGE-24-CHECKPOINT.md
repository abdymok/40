# Fatality ledger — Stage 24 checkpoint

**Status:** October pre-baseline arithmetic rechecked; prior +13 figure corrected to +14  
**Date:** 2026-11-26  
**Public pages and incident data unchanged.**

## Recalculation

A fresh programmatic sum of the current `fatality-ledger/incidents.json` by `incident_date` gives:

- Records dated on or before Oct. 28: **47**
- Sum of their current `documented_deaths`: **162**
- Legacy Oct. 28 subtotal: **148**
- Difference: **+14**, not +13 as stated in the Stage 20/22 working decomposition.

The current full dataset remains 165 incident records and 436 deaths. No record was changed to produce this result. The Stage 22 statement that the pre-Oct. 29 inventory sums to 161 is therefore stale or arithmetically incorrect and must not be carried forward.

## Why the initial revision values do not solve the baseline

The first `new_value` in each revision history sums to only 113 across the 47 records dated through Oct. 28. That is not a valid reconstruction of the 148 snapshot: many records were already revised before Oct. 28, and some later revisions occurred after the snapshot. The recorded source/update timestamp is not itself proof of the project's inclusion timestamp.

Large revision sequences that materially affect this comparison include:

- Kramatorsk bus strike, Oct. 8: 12 → 30 → 33.
- Pryluky residential strike, Oct. 7: 14 → 16 → 20 → 22.
- Sloviansk residential airstrikes, Oct. 17: 1 → 6 → 9.
- Lutsk, Oct. 14: 3 → 4 → 6.
- Nova Vodolaha, Oct. 19: 3 → 6.
- Zaporizhia, Oct. 10: 20 → 23.
- Lozova, Oct. 22: 2 → 3.
- Kyiv, Oct. 13: 1 → 2.
- Kyiv Darnytsky district, Oct. 12: 1 → 2.
- Kyiv Solomiansky shop strike, Oct. 8: 2 → 3.
- Kharkiv, Oct. 16: 3 → 2 (a downward correction).

These source-backed revisions demonstrate why a baseline membership table must use contemporaneous dashboard snapshots or dated project edits, not just incident dates or first reported values.

## Reconciliation impact

The earlier working decomposition ( +13 pre-Oct. 29, +2 on Oct. 29, +3 post-192 ) must be treated as provisional and superseded on its first component. With the corrected pre-Oct. 29 sum, the components no longer add neatly to the +18 overall difference. That is a sign that the categories overlap or that the post-baseline allocation has not yet been properly defined. Do not force the arithmetic by inventing a balancing death or reducing an incident.

## Next work

1. Reconstruct the 148 snapshot from contemporaneous commits and change-log entries.
2. Determine which of the 47 pre-Oct. 29 records and revisions were already included by Oct. 28.
3. Resolve the two Oct. 29 excess deaths separately.
4. Rebuild the post-192 bridge using incident-level increments, including Komyshuvakha's 18 baseline deaths and all subsequent revisions.
5. Update the reconciliation memo only when the record-by-record allocation is complete.

No public figure or incident record was changed.
