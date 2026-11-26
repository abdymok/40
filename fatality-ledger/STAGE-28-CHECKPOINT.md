# Stage 28 checkpoint — missing Chernihiv incident records and Oct. 29 subtotal

Date: 26 November 2026

## New finding: the current ledger is missing fatality records documented in the chronology archive

The current `incidents.json` has four records dated Oct. 29, summing to 24 deaths:

- Dnipro railway-station strike: 15 (13 initially reported, 14 later on Oct. 29, and one additional death in hospital on Oct. 30)
- Kremenchuk apartment-building strike: 3
- Izium public-health institution strike: 5
- Separate Izium attack killing a 59-year-old woman: 1

However, the archived Oct. 29 chronology contains a separate Chernihiv entry reporting two people killed in a UAV strike on shops, citing Chernihiv City Military Administration head Dmytro Bryzhynsky's Oct. 29, 12:02 post and Suspilne. No Chernihiv incident record is present in the current ledger. This is a confirmed inventory omission from the structured dataset, although the incident's relationship to another same-day Chernihiv casualty report still needs deduplication review.

The same archived Oct. 29 roundup separately says that two 15-year-old girls had earlier been reported killed in an attack in central Chernihiv, while 27 people were injured. It is not yet clear from the chronology text whether these are the same two deaths as the 12:02 shop-strike report or a distinct attack. Do not create two separate two-death records without checking the original source posts and times.

## Historical arithmetic

The historical running subtotal progressed as follows:

- 148 on Oct. 28
- 161 after the initial 13 deaths at Dnipro railway station
- 163 after two deaths in Chernihiv
- 165 after two preliminary deaths in Kremenchuk
- 167 after the later Kremenchuk and Dnipro revisions
- 173 after the subsequent Kyiv, Dnipro hospital, and Izium updates described in the historical change log

The exact allocation of the last increments still needs source-by-source reconstruction. The historical Oct. 29–30 progression is more informative than treating all records by incident date as if they were counted simultaneously.

## Reconciliation against the existing Stage 20 note

The earlier `METHOD-TO-LEDGER-RECONCILIATION.md` states that the current Oct. 29 incident records summed to 27, two above the 25 deaths in the 173 snapshot. The current ledger now sums to 24 for Oct. 29. This indicates that the Stage 20 arithmetic note and the present structured file are not describing the same record set or calculation. The discrepancy must be resolved before relying on the old +13 +2 +3 decomposition as a final explanation.

The present calculation is explicit: 24 in four Oct. 29 incident records. The chronology provides at least two additional Chernihiv deaths requiring record-level adjudication. A further difference of one remains between the current 24 and the earlier 27 figure even before deciding whether the two Chernihiv reports are one event or two.

## Immediate next checks

1. Retrieve the original Bryzhynsky post 4420 and Suspilne post 78408, plus the original Suspilne report on the two 15-year-old girls.
2. Establish whether the two Chernihiv references describe one incident or two distinct incidents.
3. Confirm whether the 59-year-old Izium victim was included in the 173 snapshot or added later.
4. Trace the 27 figure in the Stage 20 reconciliation to the exact version of `incidents.json` used for that calculation.
5. Add a Chernihiv incident record only after the identity/date/deduplication question is settled, preserving the source chronology and historical inclusion time separately.

## Change control

No incident records, dashboard totals, methodology text, or chronology entries were changed. This checkpoint records a verified omission in the current ledger and a priority source-reconciliation task.
