> **Superseded in part by Stages 116–117 (Nov. 27, 2026):** Later local reporting establishes 30 deaths in the 10:00 Kramatorsk bus strike, three in a separate 10:10 Bilenke strike and two in an 18:40 FPV attack on a civilian car. However, the Oct. 11 ≈80 snapshot explicitly labels 33 deaths as the bus strike. The surviving snapshot does not establish whether the three Bilenke deaths were folded into that 33 or whether the bus toll was overstated. The two car deaths are a separate incident. Do not reinterpret the historical 33 row as a confirmed 30+3 community total. See `STAGE-116-CHECKPOINT.md` and `STAGE-117-CHECKPOINT.md`.

# Stage 73 checkpoint — reconstructing the Oct. 11 ≈80 baseline

Date: 2026-11-26

## Finding

The Oct. 11 snapshot at commit `733a9b45892d232c5e0e2f2ac120f659ef58002b` displays approximately 80 deaths. Its method note explicitly excludes broad citywide totals where they may overlap with incident-level reports. The eight visible death-bearing chronology rows mechanically sum to 83, but one of those rows is a separate Kyiv citywide report of one death. The method says citywide totals are not added separately.

The seven incident/region rows remaining after excluding that citywide aggregate sum to **82**:

| Selected incident/report in the Oct. 11 snapshot | Deaths |
|---|---:|
| Pryluky residential strike | 22 |
| Kramatorsk bus strike (contemporaneous reported toll) | 33 |
| Zaporizhia residential strike | 20 |
| Pokrovske community, Dnipropetrovsk region | 1 |
| Darnytsky district, Kyiv | 2 |
| Desniansky residential strike, Kyiv | 2 |
| Solomiansky shop building, Kyiv | 2 |
| **Selected incident-row sum** | **82** |

This provides a coherent arithmetic reconstruction of the displayed rounded figure ≈80. It does not justify changing the historical label to an exact 82: the original page deliberately labels it approximate, and its methodology says it is a selected-report subtotal.

## Why the gross row sum was 83

The eighth row was the Oct. 8 Kyiv citywide casualty report (one death). The method paragraph specifically says broader citywide totals may overlap with the incident-level figures and are not added separately. The gross 83 therefore double-counts that citywide line if treated as an additional incident. The 82 sum above is the best-supported selected-incident reconstruction.

## Comparison with current ledger records

The seven matching current ledger records now carry 86 final deaths:
- Pryluky: 22
- Kramatorsk: 33
- Zaporizhia: 23, revised from 20
- Pokrovske: 1
- Darnytsky: 2
- Desniansky: 2
- Solomiansky shop: 3, revised from 2

The four-death difference from the reconstructed 82 consists of two documented later revisions: Zaporizhia +3 and Solomiansky shop +1. This is an arithmetic comparison of current final values with the Oct. 11 snapshot values, not evidence that the historical subtotal was revised by exactly four at a known later date.

The current ledger has 93 final deaths across 14 records dated on or before Oct. 11. Seven other records account for the remaining seven deaths: Kramatorsk Oct. 5 (1), Kherson Oct. 6 (1), Ivano-Frankivsk debris Oct. 8 (1), the separate Kyiv citywide Oct. 8 report (1), Synelnykove district Oct. 9 (1), Zaporizhia Oct. 9 (1), and Sloviansk Oct. 11 (1). Their inclusion in the Oct. 11 selected subtotal is not established by the ≈80 method paragraph. Do not add them retrospectively merely because they exist in the current ledger.

## Solomiansky shop discrepancy requiring caution

The Oct. 11 method paragraph and the contemporaneous chronology entry both say **two** deaths in the Solomiansky shop strike. The current ledger records an initial two-death report at 12:08 on Oct. 8 and a revision to three at 18:20 on Oct. 8, citing Ukrinform's later report that Kyiv police confirmed three killed. The Oct. 11 snapshot still names two. The historical baseline therefore explicitly supports inclusion of the first two deaths, but does not show the third in its stated incident count. The reason for that omission is not established. Do not assume the third was included merely because the report predates Oct. 11, and do not assign a historical inclusion date for it without further evidence.

The current incident description says the third victim later died in hospital, but the source inventory currently cited in the ledger establishes a later police confirmation of three and does not itself identify the hospital detail. Treat that detail as requiring a direct supporting source before relying on it in future edits.

## Data handling

- No incident records or revision histories changed.
- No `ledger_effective_at` values changed.
- No chronology entries or public dashboard figures changed.
- The public method-page minimum remains 421.
- The historical Oct. 11 label remains approximately 80.

## Next work

1. Trace the seven other pre-Oct. 12 ledger records against the contemporaneous Oct. 10–11 dashboard snapshots and method wording.
2. Establish whether any of them entered the broad Oct. 10 estimate or the Oct. 11 selected subtotal, without treating the broad estimate as a reconciled sum.
3. Locate a direct source for the hospital detail in the Solomiansky shop incident before changing that description.
