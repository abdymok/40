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

The history is more nuanced than a simple 100→80 correction:

1. At 12:00 Kyiv time, commit `733a9b45892d232c5e0e2f2ac120f659ef58002b` displayed ≈80 as the provisional selected-incident subtotal.
2. At 12:18 Kyiv time, commit `b915a945a1d932a41cb7291a051de8b8be863bca` changed the tile to 90+, a provisional editorial estimate.
3. At 12:50 Kyiv time, commits `1b09f0d430a820ecfa5057569dae8a8f3e4d7ea9` and `11f63c34ecc63cb1253ea7d12d00d10fad4e25c8` clarified that the 90+ headline was not a count of 90 individually documented deaths: the chronology identified about 80 deaths in selected incidents, and the additional margin was editorial judgement, not ten separately verified deaths.
4. At 15:18 Kyiv time, commit `bed64256d24c70e0f2c71835fb3dd4c1133842bb` returned the dashboard tile to ≈80 and the label “Deaths documented in selected incidents.”

The Oct. 11 selected subtotal is therefore distinct from both the Oct. 10 ≈100 broad estimate and the temporary Oct. 11 90+ editorial estimate. The movement among these figures is a scope-and-presentation change, not evidence that deaths were disproven or removed.

## Relationship to later reconstruction

Stage 70 reconstructs the subsequent selected-subtotal sequence from the Oct. 11 ≈80 baseline through Oct. 14 ≈90. Stage 73 reconstructs the ≈80 baseline as seven selected incident/region rows summing to 82, while retaining the page's approximate label.

The Oct. 11 ≈80 baseline explicitly names six Kyiv deaths: Darnytsky 2, Desniansky 2 and Solomiansky shop 2. Broader Kyiv totals are cautioned against as potential overlaps. The third Solomiansky shop death is not named in the Oct. 11 method or chronology snapshot, and its inclusion in that subtotal remains unresolved.

## Correction to the Stage 59 summary

The Oct. 14 transition from ≈89 to ≈90 is the update from **four to at least five deaths** in the Oct. 14 Kyiv attack, not the transition from three to four. The ≈85 snapshot had first added three deaths; the ≈89 snapshot then had a method paragraph already listing four Kyiv deaths plus four in Lutsk while the dashboard remained at 89. The next update raised the Kyiv toll to five and the dashboard to 90. Stage 59's 89→90 row and explanatory paragraph are corrected in this checkpoint.

## Changes made

No changes to `fatality-ledger/incidents.json`, incident records, revision histories, `ledger_effective_at` values, chronology entries, public dashboard figures or the public method-page minimum. The public minimum remains 421.

## Source commits

- First dashboard, Oct. 10 16:05: `27776283f345cdeb7d6803af49b8267fa022c68b`
- Oct. 11 ≈80 baseline: `733a9b45892d232c5e0e2f2ac120f659ef58002b`
- Oct. 11 interim 90+ tile: `b915a945a1d932a41cb7291a051de8b8be863bca`
- Oct. 11 90+ explanation: `1b09f0d430a820ecfa5057569dae8a8f3e4d7ea9` and `11f63c34ecc63cb1253ea7d12d00d10fad4e25c8`
- Oct. 11 return to ≈80: `bed64256d24c70e0f2c71835fb3dd4c1133842bb`
- Oct. 14 ≈85→≈89 Lutsk update: `10a74ad99f3fb3911689965e6449fe41ded0c772`
- Oct. 14 ≈89→≈90 Kyiv toll revision: `fdbf9759933d6119841de42baf50ab0c03f19a2b`
