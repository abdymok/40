# Fatality ledger — Stage 11 checkpoint

**Status:** Nov. 12–14 incident batch entered  
**Date:** 2026-11-26  
**Public pages unchanged.**

## Records added

Twelve additional records were entered, covering 18 documented deaths:

- Kyiv, Solomiansky district, Nov. 12: one woman killed in a residential-building drone strike.
- Kramatorsk, Nov. 12: four people killed in attacks across the city.
- Odesa, Nov. 13: two people killed in a residential-area attack.
- Zaporizhia, Nov. 13: a 17-year-old boy killed in the morning private-sector attack.
- Zaporizhia district, Nov. 12: one woman critically injured in a drone strike on a passenger bus died in hospital on Nov. 13.
- Zaporizhia, Kosmichny district, Nov. 13: one man found dead under rubble at an industrial facility.
- Zolota Balka, Kherson region, Nov. 13: two residents killed in a drone attack. The next-day Berislav district report is retained as corroboration of the same victims, not an additional pair of deaths.
- Yasna Polyana, Donetsk region, Nov. 13: one resident killed.
- Zaporizhia, Kosmichny district, Nov. 13: one Cobra rescue-service worker killed when a concrete slab fell during rubble-clearing at a damaged five-storey residential building. This is distinct from the man found dead at the industrial facility.
- Pavlohrad, Nov. 14: one person killed in a missile strike.
- Mena, Chernihiv region, Nov. 14: two men killed in a drone strike on critical infrastructure.
- Borova, Kharkiv region, Nov. 14: one 67-year-old man killed in a Russian strike.

## Data status and validation

The pilot dataset now contains:
- 64 incident records;
- 174 documented deaths across those records;
- 171 source records.

The 174 is a partial dataset sum, not the national/project total. The pilot is still missing the rest of the October and November incidents.

Structural checks confirmed:
- unique incident IDs and source IDs;
- continuous revision histories;
- each record's final revision equals its documented death count;
- no dangling source references.

## Open arithmetic issues carried forward

1. Dnipro, Nov. 3: the final source count is two, while the method's running addition records one. The incident record preserves the 1 → 2 revision.
2. Chornomorsk, Nov. 11: the final source count is four, while the method adds only the initial one. The incident record preserves 1 → 3 → 4. The later three deaths may be missing from the cumulative subtotal unless found elsewhere.
3. The Nov. 16–17 sequence in the method contains stale or contradictory subtotal baselines around the third Chernihiv death, the 72-death Komyshuvakha revision, and the subsequent Zaporizhia updates. This is the next priority for reconciliation.

No public pages or figures have been changed.
