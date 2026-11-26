# Stage 72 checkpoint — dashboard introduction and first casualty-method reset

Date: 2026-11-26

## Finding

The infrastructure dashboard was first published on **Oct. 10, 2026, at 16:05 Kyiv time**, in commit `27776283f345cdeb7d6803af49b8267fa022c68b` (“Publish infrastructure dashboard and provisional October 10 update”).

The first dashboard contained five measures:
- Sites hit: 20+
- Civilians killed: approximately 100
- Injured: approximately 600
- Bridge strikes: 7+
- Kyiv air alerts: 73, with approximately 2 days 12 hours under alert

The first death figure was explicitly a broad working estimate. It was not a sum of individually reconciled incident records.

## Oct. 11 methodology transition

The Oct. 11 review documents the move from the broad estimate to a selected-incident subtotal:

1. Commit `1b09f0d430a820ecfa5057569dae8a8f3e4d7ea9` introduced an interim 90+ editorial estimate and clarified that the chronology then identified approximately 80 deaths in selected incidents. The extra margin was editorial judgement about incomplete reporting, not ten individually verified deaths.
2. Commit `b915a945a1d932a41cb7291a051de8b8be863bca` records the casualty and site-count review. Its correction note says the earlier broad estimate of approximately 100 killed and 600 injured was replaced with a provisional incident-level subtotal of approximately 80 killed and at least 100 injured across selected incidents documented in the chronology.
3. The later Oct. 11 snapshot, commit `733a9b45892d232c5e0e2f2ac120f659ef58002b`, presents approximately 80 and defines it as a selected-incident subtotal, not a comprehensive national count.

The change from approximately 100 / 90+ to approximately 80 is therefore a scope-and-method change. It is not evidence that approximately 20 deaths were disproven or removed.

## Relationship to later reconstruction

Stage 70 reconstructs the subsequent selected-subtotal sequence from the Oct. 11 ≈80 baseline through Oct. 14 ≈90. Stage 72 establishes the dashboard's origin and explains why the first broad estimate must not be treated as a prior ledger total.

The Oct. 11 ≈80 baseline explicitly names six Kyiv deaths: Darnytsky 2, Desniansky 2 and Solomiansky shop 2. Broader Kyiv totals are cautioned against as potential overlaps. The later third Solomiansky shop death must not be backdated into this snapshot.

## Correction to the Stage 59 summary

The Oct. 14 transition from ≈89 to ≈90 is the update from **four to at least five deaths** in the Oct. 14 Kyiv attack, not the transition from three to four. The ≈85 snapshot had first added three deaths; the ≈89 snapshot then had a method paragraph already listing four Kyiv deaths plus four in Lutsk while the dashboard remained at 89. The next update raised the Kyiv toll to five and the dashboard to 90. Stage 59's 89→90 row and explanatory paragraph are corrected in this checkpoint.

## Changes made

No changes to `fatality-ledger/incidents.json`, incident records, revision histories, `ledger_effective_at` values, chronology entries, public dashboard figures or the public method-page minimum. The public minimum remains 421.

## Source commits

- First dashboard, Oct. 10 16:05: `27776283f345cdeb7d6803af49b8267fa022c68b`
- Oct. 11 interim 90+ wording: `1b09f0d430a820ecfa5057569dae8a8f3e4d7ea9`
- Oct. 11 casualty-method review: `b915a945a1d932a41cb7291a051de8b8be863bca`
- Oct. 11 ≈80 baseline: `733a9b45892d232c5e0e2f2ac120f659ef58002b`
- Oct. 14 ≈85→≈89 Lutsk update: `10a74ad99f3fb3911689965e6449fe41ded0c772`
- Oct. 14 ≈89→≈90 Kyiv toll revision: `fdbf9759933d6119841de42baf50ab0c03f19a2b`
