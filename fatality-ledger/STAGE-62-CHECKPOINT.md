# Stage 62 checkpoint — Oct. 11 baseline versus current ledger

Date: 26 November 2026

## Scope

This stage compares the Oct. 11, 2026, 09:00 UTC chronology snapshot (commit `733a9b45892d232c5e0e2f2ac120f659ef58002b`) with the current incident ledger for incidents dated through Oct. 11. It is a comparison of two different artifacts, not a claim that the approximate historical subtotal can be reconstructed exactly.

No incident records, effective dates, public counters, method-page totals or chronology entries were changed.

## Current ledger slice

The current `fatality-ledger/incidents.json` contains 14 records dated on or before Oct. 11, with a raw final-death sum of 93.

Eight of those records correspond to death-bearing rows visible in the Oct. 11 snapshot. The Oct. 10 Dnipropetrovsk-region row is the same 11-year-old boy killed in Pokrovske who has a dedicated current Nikopol-district ledger record; it is not a missing incident:
- Pryluky, Oct. 7: 22.
- Kyiv, Darnytsky district, Oct. 7: 2.
- Kyiv, Desniansky district, Oct. 7: 2.
- Kramatorsk, Oct. 8: 33.
- Kyiv, citywide morning report, Oct. 8: 1.
- Kyiv, Solomiansky shop strike, Oct. 8: 3 in the current ledger.
- Zaporizhia residential strike, Oct. 10: 23 in the current ledger.

These seven current records sum to 86. The snapshot's corresponding figures are not all identical: it recorded two deaths at the Solomiansky shop and 20 in Zaporizhia, so the current ledger is four higher on those two incidents combined (Solomiansky 2→3; Zaporizhia 20→23).

The Oct. 11 snapshot also listed one death in Dnipropetrovsk region on Oct. 10. There is no matching incident record in the current 14-record ledger slice. This remains a specific ledger-coverage gap to investigate; it is not silently treated as part of another incident.

## Six records not itemized as death-bearing rows in the snapshot

The other six current records, totalling six deaths, are not itemized as death-bearing rows in the visible Oct. 11 snapshot:
1. Kramatorsk, Oct. 5: one woman killed in the ambulance/high-rise attack; contemporaneous reports published Oct. 6.
2. Kherson, Oct. 6: doctor Yuriy Zimin died on Nov. 16 from injuries sustained in the Oct. 6 drone attack; this is a delayed death reported Nov. 17.
3. Ivano-Frankivsk, Oct. 8: one civilian security guard killed by drone debris; reports published Oct. 9.
4. Synelnykove district, Oct. 9: one person killed in attacks on Zaitseve and Petropavlivka communities.
5. Zaporizhia, Oct. 9: one man killed in a guided-bomb strike.
6. Nikopol district, Oct. 10: an 11-year-old boy killed in a drone attack in the Pokrovske community.
7. Sloviansk, Oct. 11: one woman killed.

“Not itemized in the visible snapshot” is deliberate wording. It does not prove that none of these deaths was included in the approximate 80 figure, because the Oct. 11 subtotal is explicitly approximate and the historical method paragraph does not provide a complete incident-by-incident membership list. The Kramatorsk and Ivano-Frankivsk reports were available before the snapshot; the Zimin death was not known until November. The remaining cases need source-by-source historical inclusion checks before assigning any effective dates.

## Arithmetic and overlap warning

The visible death-bearing rows cited in Stage 61 sum to 83 when their displayed figures are added mechanically. That is not a defensible exact historical subtotal: the same snapshot's method paragraph explicitly warns that broad citywide Kyiv totals may overlap incident-level figures and should not be added separately. The snapshot itself labels the subtotal “approximately 80,” not 83.

The current ledger's 93 is likewise a raw incident-record sum, not a like-for-like restatement of the Oct. 11 public figure. It includes later-known and later-added records, the delayed Nov. 16 death, and two increased incident tolls. The 14-record slice sums to 93; the eight records corresponding to visible incident rows sum to 87; the other six records sum to six. This arithmetic describes the current ledger structure only. It does not reconcile the historical approximate-80 subtotal.

## Open follow-up

1. Identify the Oct. 10 Dnipropetrovsk-region death-bearing row in the historical chronology and determine whether a distinct current ledger record should exist. Do not create one until the incident can be identified and distinguished from the Synelnykove/Nikopol records.
2. Check the Oct. 11-era source trail for the Kramatorsk Oct. 5, Ivano-Frankivsk Oct. 8, Synelnykove Oct. 9, Zaporizhia Oct. 9, Nikopol Oct. 10 and Sloviansk Oct. 11 records to determine whether each was in scope at the time of the approximate-80 snapshot.
2. Preserve the Oct. 6 Kherson doctor death as a delayed-death case with its Nov. 17 publication date; do not backdate knowledge of the death to the Oct. 11 snapshot.
3. Keep the Solomiansky 2→3 and Zaporizhia 20→23 revisions separately documented. Their current incident records still have unresolved/null effective dates; this stage does not assign them.

## Integrity

- Current ledger file SHA at review: `5c4ef0bfc5cc50831dc11d28384c3ac3a25a5f35`.
- Current slice: 14 records, raw sum 93.
- Public method-page minimum: 421, unchanged.
- No ledger or public-facing data changed in this stage.
