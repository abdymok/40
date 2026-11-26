# Fatality ledger — Stage 20 checkpoint

**Status:** Nov. 4–6 source-audit incidents entered  
**Date:** 2026-11-26  
**Public pages unchanged.**

Six incident records have been added for eight deaths identified in the Nov. 4–6 source audit:
- Yasnohirka, Nov. 4: two people killed by two KAB-250 bombs.
- Serhiivka, Nov. 4: two people killed in an airstrike.
- Putyvl community, Nov. 4: one 69-year-old woman killed in a drone strike on a house.
- Antonivka, Nov. 4: one man killed by a Russian drone.
- Kramatorsk, Nov. 5: one man killed in an FPV drone attack on a civilian car.
- Sarny district, Nov. 6: one man killed in a Russian attack.

The two Yasnohirka deaths are separate from the woman killed in a Nov. 3 attack. The two Serhiivka deaths are a separate incident. The Kramatorsk Nov. 5 death is separate from the Nov. 3 Kramatorsk death already in the ledger.

## Current pilot dataset

- 159 incident records.
- 430 documented deaths.
- 362 source records.

Validation passed:
- all incident IDs unique;
- all source IDs unique;
- revision histories are continuous;
- final revision values match each incident's current death count;
- no revision points to a missing source.

## Reconciliation status

The current incident-level sum is **430**, compared with the published method-page minimum of **418**. The 12-death difference is unresolved. The eight Nov. 4–6 deaths above were already included in the method's 418 total, but had been missing from the pilot incident dataset. They have now been added.

Known differences that require line-by-line reconciliation include:
- Chornomorsk: final incident record has four deaths; the method's Nov. 11 increment added one.
- Dnipro, Nov. 3: final incident record has two deaths; the method's Nov. 3 increment added one.
- Several October incidents have final local counts that differ from early project snapshots, including Zaporizhia, Kyiv, Kharkiv and Izium.
- The 192 opening baseline includes 18 deaths from the Nov. 2 Komyshuvakha strike. The 72-death Komyshuvakha record must therefore preserve its baseline portion and subsequent increments, rather than being treated as 72 new deaths after the baseline.

No public page, dashboard number or change-log total has been changed. The 430 figure is a pilot dataset sum, not yet an approved replacement for the public minimum.
