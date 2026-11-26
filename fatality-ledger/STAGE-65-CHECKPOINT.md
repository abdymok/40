# Stage 65 checkpoint — final additions to the Oct. 22 selected-incident subtotal

Date: 26 November 2026

## Verified transitions

The historical diffs establish the following sequence of displayed selected-incident subtotals:

- **107 → 116 (+9), Oct. 21:** commit `46a3feb1b3430a7e58185dbca864de617f72aa28` explicitly says the selected-incident subtotal rose from approximately 107 to 116 after the Oct. 17 Sloviansk strike toll reached nine. The same update reconciled the methodology note to include the two people killed in Korotych reported on Oct. 21. As established in Stage 57, the preceding 105→107 dashboard-only update duplicated the two Sviatoshynsky deaths already present in the 105 snapshot; the later +9 and the two Korotych deaths together account for the net +11 from 105 to 116. This is a documented offset, not a reason to preserve the duplicated intermediate number.
- **116 → 117 (+1), Oct. 22:** commit `3513193d093e5166b216f9112bd25da39f8dbb41` added the fatal attack on Lymanivka in Kharkiv region and changed the dashboard from approximately 116 to approximately 117. The update text identifies the Lymanivka death as the newly added fatal incident.
- **117 → 118 (+1), Oct. 22:** commit `4ada778321c66b570c73f8d5353617a076db8ee6` updated the Kyiv overnight attack entry after the later report of one person killed and changed the dashboard from approximately 117 to approximately 118. Its update text identifies the Kyiv death.
- **118 → 121 (+3), Oct. 22:** commit `0f4dda082aba94f4f6c4a5b9279953cb4a0d17ac` revised Chabany after corroboration by regional authorities and independent media and changed the selected-incident subtotal from approximately 118 to approximately 121. The Chabany entry's evidence classification and the dashboard diff support the three-death addition.

These commits are not asserted to form one uninterrupted parent chain; the findings rely on their individual diffs and the historical snapshot at `9a4749285ace80c3c9931aeb25869b4532457655`.

## Relationship to the 118 snapshot

The Oct. 22 118 snapshot explicitly includes the Lymanivka death and the Kyiv death in its method paragraph. Its listed named items sum mechanically to 37 (Stage 64). It separately excludes Chabany's three deaths at that point. The Chabany revision then raises the selected-incident subtotal to 121.

The 121→123 change is not another incident addition. Stage 63 establishes that it changes the count's scope from selected incidents to a nationwide documented minimum.

## Limits

- The 107→116 arithmetic is understood only by reading the sequence together with Stage 57: +2 was a duplicate dashboard-only increase, while the later +9 dashboard increase accompanied +9 Sloviansk plus +2 Korotych in the method paragraph. Net change from the 105 snapshot is +11, matching those 11 deaths.
- The approximately 118 snapshot's 37 explicitly named deaths are not a complete breakdown of 118.
- Chabany's temporary inclusion in the historical 121 is not evidence that the current ledger should reinstate it.
- No effective dates were changed or assigned in this stage.
- No current incident data, public counter or chronology entry changed.

## Next follow-up

Continue backwards from the Oct. 21 107 subtotal and the Oct. 20 100/103/102 transitions, distinguishing actual additions, revisions, scope corrections and duplicated dashboard updates.
