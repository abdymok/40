# Stage 71 checkpoint — Oct. 10–11 methodology reset and the ≈80 baseline

Date: 2026-11-26

## Finding
The approximately-80 figure established on Oct. 11 was not a simple continuation of the earlier approximately-100 dashboard estimate. It was a deliberate methodological reset from a broad editorial estimate to a selected-incident subtotal.

## Historical sequence

1. **Oct. 10 initial dashboard.** Commit `27776283f345cdeb7d6803af49b8267fa022c68b` published the first infrastructure dashboard with a rounded `~100` civilian-death estimate and approximately 600 injuries. Its method text explicitly called both order-of-magnitude estimates, not a reconciled incident-by-incident sum, and warned that regional and citywide totals might overlap.

2. **Oct. 11 interim 90+ editorial estimate.** Commit `1b09f0d430a820ecfa5057569dae8a8f3e4d7ea9` described 90+ as a provisional editorial estimate, not a count of 90 individually documented deaths. It stated that the chronology then identified about 80 deaths in selected incidents and that the additional margin reflected editorial judgement about incomplete reporting, not ten separately verified deaths. This explicitly distinguishes the broad estimate from the incident-linked count.

3. **Oct. 11 formal reset to approximately 80.** Commit `b915a945a1d932a41cb7291a051de8b8be863bca` changed the dashboard label to “Estimated civilian deaths” and value to 90+ in one intermediate diff, but its correction text documents the casualty/site-count review replacing the earlier broad estimate of approximately 100 killed and 600 injured with a provisional incident-level subtotal of approximately 80 killed and at least 100 injured across selected incidents. The final snapshot at commit `733a9b45892d232c5e0e2f2ac120f659ef58002b` presents ≈80 and method text defining it as a selected-incident subtotal, not a comprehensive national count.

4. **Oct. 11 baseline composition.** The ≈80 method paragraph explicitly names six Kyiv deaths in the Oct. 7–8 reports: Darnytsky 2, Desniansky 2 and Solomiansky shop 2. It cautions that broader citywide totals may overlap and are not added separately. The later third Solomiansky shop death is not part of this contemporaneous two-death snapshot.

## Interpretation
- The change from ≈100 / 90+ to ≈80 is a scope-and-method correction, not evidence that 20 people were later determined not to have died.
- The approximately-80 selected subtotal is not a complete itemized ledger: the method names some incidents and gives a rule for avoiding overlap, but does not enumerate every component.
- The 90+ editorial margin was explicitly not ten individually verified deaths. It should not be carried into the selected-incident subtotal or converted into incident records.
- The Oct. 11 ≈80 baseline is the appropriate starting point for the subsequent historical sequence reconstructed in Stage 70.
- The Oct. 10 Zaporizhia toll was still changing during this period. By the Oct. 11 review it was reported as 20 killed and 32 injured; do not substitute earlier casualty snapshots into later totals without date-specific evidence.

## Changes made
No changes to `fatality-ledger/incidents.json`, incident records, effective dates, chronology entries, public dashboard or public method-page minimum. The public method-page minimum remains 421.

## Source commits
- Initial Oct. 10 dashboard: `27776283f345cdeb7d6803af49b8267fa022c68b`
- Oct. 11 interim method wording: `1b09f0d430a820ecfa5057569dae8a8f3e4d7ea9`
- Oct. 11 casualty/site-count review: `b915a945a1d932a41cb7291a051de8b8be863bca`
- Oct. 11 ≈80 baseline snapshot: `733a9b45892d232c5e0e2f2ac120f659ef58002b`
