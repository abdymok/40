# Fatality ledger — Stage 18 checkpoint

**Status:** Oct. 30–31 late-reported deaths entered; Izium revisions merged; baseline reconciliation exposed  
**Date:** 2026-11-26  
**Public pages unchanged.**

## Records added

Five new records were added for six deaths reported on Oct. 31:
- Sloviansk, Oct. 30: two people killed in separate attacks, including a 16-year-old railway-college student and a 73-year-old man.
- Shostka, Oct. 30: one 43-year-old woman killed in a drone strike on a civilian enterprise.
- Nikopol district, Oct. 30: one person killed in regional attacks.
- Dnipro district, Oct. 31: one person killed in overnight attacks.
- Orikhiv, Oct. 30: one 53-year-old man killed by an FPV drone.

These six are the six additional fatalities that the methodology says were added on Nov. 5 after a source-to-page audit, raising the running minimum from approximately 230 to approximately 236.

One additional record was added for Pavlohrad, Oct. 26: DTEK miner Valentyn Kotelevskyi, whose death is already included in the 192 baseline. This does not add a new cumulative death beyond the baseline; it supplies the incident record and company corroboration.

## Izium incident reconciliation

The earlier one-death report about a 59-year-old woman killed in Izium on Oct. 29 is now merged into the five-death public-health institution strike record. The incident history is 1 → 5. The earlier one-death report is treated as a partial update of the same strike, not a separate incident. The generic one-death Kharkiv-region record has been removed to avoid double-counting this victim.

## Unresolved DTEK driver

DTEK driver Vitaliy Shcherbyna was killed in an attack on Oct. 25. The methodology says it is unclear whether he was already included in the Dnipropetrovsk Regional Military Administration's Oct. 25 casualty total. A separate unresolved file records the source trail and required deduplication. He is not added as a separate death until the overlap is resolved.

## Reconciliation arithmetic

The pilot dataset now contains:
- 147 incident records;
- 416 documented deaths;
- 338 source records.

Structural checks confirmed:
- unique incident IDs and source IDs;
- continuous revision histories;
- every final revision equals the record's current documented-death count;
- no dangling source references.

The partial dataset is now close to the published 418, but it does not reconcile:

| Measure | Deaths |
|---|---:|
| Current pilot dataset | 416 |
| Published project minimum | 418 |
| Difference | -2 |

A more important split reveals why the difference is misleading:

- The incident records currently recover **176 deaths** that were known in the opening 192 baseline.
- The opening baseline is **192**, leaving **16 deaths unallocated** to incident records.
- The dataset contains **240 deaths** from later additions and delayed confirmations.
- The method's cumulative additions after the 192 baseline total **226**.
- Therefore the post-baseline incident sum is **14 higher** than the method's additions, while the opening baseline inventory is 16 short. The net result is 416, two below 418.

This is not a reason to force the dataset to 418. It means some pre-baseline incidents are still missing and some later records or revisions may be duplicated or exceed the method's cumulative arithmetic. The next stage must compare every post-baseline incident record against the method's 192 → 418 change sequence, not merely search for two additional deaths.

## Next stage

1. Complete the Oct. 1–Nov. 1 incident inventory and allocate the 16-death baseline gap.
2. Compare Nov. 2–26 incident records against each method increment to identify the 14-death post-baseline overage.
3. Resolve the DTEK Shcherbyna overlap.
4. Revisit the OHCHR/local-source discrepancies without importing OHCHR totals automatically.

No public totals or pages have been changed.
