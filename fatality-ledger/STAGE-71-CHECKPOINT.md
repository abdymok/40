# Stage 71 checkpoint — Oct. 10–11 methodology transition and ≈80 baseline

Date: 2026-11-26

## Finding

The first dashboard's ≈100 was a broad order-of-magnitude estimate. The ≈80 selected-incident subtotal was established on Oct. 11, but the dashboard tile temporarily switched to 90+ before returning to ≈80 later that afternoon. The 90+ was a separate editorial estimate, not an exact incident subtotal and not ten additional verified deaths.

## Historical sequence

1. **Oct. 10 first dashboard.** Commit `27776283f345cdeb7d6803af49b8267fa022c68b` published the dashboard with approximately 100 civilians killed and approximately 600 injured. Its method text explicitly called both order-of-magnitude estimates, not a reconciled incident-by-incident sum.

2. **Oct. 11 ≈80 selected-incident snapshot, 12:00 Kyiv time.** Commit `733a9b45892d232c5e0e2f2ac120f659ef58002b` (09:00:05 UTC) displays ≈80 and defines it as a provisional incident-level subtotal for selected reports in the chronology. Its method excludes broad citywide/nationwide aggregates where they may overlap. Stage 73 reconstructs the seven selected rows as 82.

3. **Oct. 11 90+ editorial estimate, 12:18 Kyiv time.** Commit `b915a945a1d932a41cb7291a051de8b8be863bca` (09:18:49 UTC) changes the dashboard tile from ≈80 to 90+. Its method describes 90+ as a provisional editorial estimate based on available reporting, not a precise count of individually documented deaths. The update log also contains a casualty/site-count review describing the approximately-80 selected-incident subtotal, creating a distinction between the broad headline estimate and the incident-linked subtotal.

4. **Oct. 11 clarification, 12:50 Kyiv time.** Commit `1b09f0d430a820ecfa5057569dae8a8f3e4d7ea9` (09:51:40 UTC), followed by `11f63c34ecc63cb1253ea7d12d00d10fad4e25c8` (09:51:47 UTC), retains the 90+ tile but clarifies in the method that the chronology identifies about 80 deaths in selected incidents. The additional margin is editorial judgement about incomplete reporting, not ten separately verified deaths or deaths assigned to particular incidents.

5. **Return to ≈80, 15:18 Kyiv time.** Commit `bed64256d24c70e0f2c71835fb3dd4c1133842bb` (12:18:47 UTC) changes the tile back to “Deaths documented in selected incidents” at ≈80. Its parent snapshot, `2a234dc5c373ece2435b14a32f839fe8c48291ae`, still shows 90+. The following commits preserve the ≈80 tile.

## Interpretation

- The Oct. 10 ≈100 and Oct. 11 90+ were broad editorial estimates, not reconciled incident sums.
- The Oct. 11 ≈80 was the selected-incident subtotal. It was visible before the 90+ interim headline, remained identified in the 90+ method note, and returned as the dashboard headline at 15:18 Kyiv time.
- The changes among ≈100, 90+ and ≈80 are changes in scope and presentation. They do not establish that approximately 20 or 10 deaths were disproven, removed or newly verified.
- The Oct. 11 ≈80 baseline explicitly names six Kyiv deaths: Darnytsky 2, Desniansky 2 and Solomiansky shop 2. Stage 73 reconstructs the seven selected rows at 82 while excluding the separate citywide Kyiv death.
- The third Solomiansky shop death is not named in the Oct. 11 method or chronology snapshot; its historical inclusion remains unresolved.

## Changes made

No changes to `fatality-ledger/incidents.json`, incident records, effective dates, chronology entries, public dashboard or public method-page minimum. The public method-page minimum remains 421.

## Source commits

- First dashboard: `27776283f345cdeb7d6803af49b8267fa022c68b`
- Oct. 11 ≈80 snapshot: `733a9b45892d232c5e0e2f2ac120f659ef58002b`
- 90+ tile: `b915a945a1d932a41cb7291a051de8b8be863bca`
- 90+ clarification: `1b09f0d430a820ecfa5057569dae8a8f3e4d7ea9` and `11f63c34ecc63cb1253ea7d12d00d10fad4e25c8`
- Return to ≈80: `bed64256d24c70e0f2c71835fb3dd4c1133842bb`
