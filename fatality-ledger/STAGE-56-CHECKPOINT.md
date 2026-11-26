# Stage 56 checkpoint — Oct. 21 dashboard/method mismatch

Date: 26 November 2026

## New finding

The Oct. 21 dashboard transition from 105 to 107 is attributable to the two deaths in Kyiv's Sviatoshynsky district, based on the commit titled “Update civilian death count after Kyiv drone attack report” and the contemporaneous chronology.

However, the method paragraph fetched at that same 107 snapshot still says “approximately 105” while already naming the two Sviatoshynsky deaths. The commit that changes the dashboard from 105 to 107 modifies only the dashboard value and does not update the method paragraph.

This is a clear contemporaneous dashboard/method inconsistency. The method paragraph is stale at that snapshot and cannot independently prove whether the two deaths were already included in the 105 baseline. The +2 attribution is supported by the commit and chronology, but the exact membership of the 105 baseline remains unproven.

## 107 → 116 remains unresolved

The Oct. 21 update history says the subtotal rose from 107 to 116 after the Sloviansk toll reached nine and says the two Korotych deaths were included. The arithmetic increase is +9. The later method paragraph lists nine Sloviansk deaths and two Korotych deaths, but that list does not establish how many Sloviansk deaths were already included in 107.

The current Sloviansk incident record has a revision history of 1→6→9. That revision chain is not enough to infer the public baseline's membership. Do not assume +7 Sloviansk plus +2 Korotych without a dated historical snapshot proving the earlier Sloviansk allocation.

## Historical evidence checked

- Commit `3c205e7cb516ca3a9843c1234b23ff05408bf6dc`: dashboard changes from approximately 105 to approximately 107; the diff contains no method-paragraph change.
- Commit `46a3feb1b3430a7e58185dbca864de617f72aa28`: dashboard changes from approximately 107 to approximately 116; update history explicitly names Sloviansk and Korotych but does not provide an arithmetic split.
- The HTML fetched at commit `3c205e7cb516ca3a9843c1234b23ff05408bf6dc` displays approximately 107 in the dashboard while its method paragraph says approximately 105 and names the Sviatoshynsky deaths.
- The HTML fetched at commit `46a3feb1b3430a7e58185dbca864de617f72aa28` displays approximately 116 and lists nine Sloviansk deaths and two Korotych deaths.

## Data handling

No `ledger_effective_at` fields changed. No incident final counts changed. Chabany remains excluded from the current ledger. The public 421 subtotal remains untouched.

## Next work

1. Continue reconstructing the pre-Oct. 21 subtotal and its exact incident membership from earlier dashboard commits.
2. Establish whether the two Sviatoshynsky deaths were genuinely new to the 105→107 transition or whether the earlier method paragraph was prematurely updated.
3. Find an earlier Sloviansk toll snapshot and determine how much, if any, was included in 107.
4. Only then allocate the 107→116 increment between Sloviansk and Korotych, if the evidence supports it.
5. Keep the 121→123 +2 unidentified unless an archived source provides an incident allocation.
