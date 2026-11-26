# Stage 75 checkpoint — seven other pre-Oct. 12 ledger records

Date: 2026-11-26

## Scope

This stage checks the seven current-ledger records dated on or before Oct. 11 that are not among the seven selected incident/region rows reconstructed in Stage 73. The question is whether they were part of the Oct. 11 ≈80 selected subtotal.

## Record-by-record findings

| Record | Current deaths | Source timing | Oct. 11 snapshot finding |
|---|---:|---|---|
| Kramatorsk, Oct. 5 ambulance/high-rise attack | 1 | Ukrainska Pravda, Censor.NET and Ukrinform reports on Oct. 6 | Not present as a chronology entry in the Oct. 10 first-dashboard snapshot or Oct. 11 ≈80 snapshot. No evidence of inclusion in the selected subtotal. |
| Kherson, Oct. 6 attack on doctor Yuriy Zimin | 1 | Doctor died in hospital Nov. 16; Suspilne reported the death Nov. 17; ledger says it entered the running minimum Nov. 18 | Definitely not part of the Oct. 11 subtotal. This is a delayed death first reported more than a month later. |
| Ivano-Frankivsk, Oct. 8 drone debris | 1 | Ukrainska Pravda reported at 00:18 Oct. 9; Ukrinform at 06:58 Oct. 9 | Not present as a chronology entry in the Oct. 10 or Oct. 11 snapshot. No evidence of inclusion in the selected subtotal. |
| Synelnykove district, Oct. 9 attacks | 1 | Ukrinform at 09:30 Oct. 9; Ukrainska Pravda at 19:08 Oct. 9 | Not present as a chronology entry in the Oct. 10 or Oct. 11 snapshot. No evidence of inclusion in the selected subtotal. |
| Zaporizhia, Oct. 9 guided-bomb attack | 1 | RBC-Ukraine at 08:34 Oct. 9; Ukrinform at 11:27 Oct. 9 | Not present as a chronology entry in the Oct. 10 or Oct. 11 snapshot. No evidence of inclusion in the selected subtotal. |
| Sloviansk, Oct. 11 attack | 1 | Donetsk regional administration report was published/recorded Oct. 12 | The death was reported after the Oct. 11 ≈80 snapshot. It cannot be included in that baseline. |
| Kyiv, Oct. 8 citywide casualty report | 1 | Kyiv mayor's Oct. 8 10:52 report; chronology entry present in the Oct. 11 snapshot | Present as a row, but the Oct. 11 method explicitly says broad citywide totals may overlap with incident-level reports and are not added separately. It is not an additional selected incident. |

## Reconciliation

The seven records explain seven deaths in the current raw ledger sum of 93, but they do not add seven to the Oct. 11 selected subtotal:
- One is a delayed death first reported and incorporated in November (Kherson).
- One was reported after the Oct. 11 snapshot (Sloviansk).
- Three other incident records were reported before Oct. 11 but do not appear in either the Oct. 10 or Oct. 11 chronology snapshot (Kramatorsk Oct. 5, Ivano-Frankivsk, Synelnykove and Zaporizhia Oct. 9 are four records, not three).
- The separate Kyiv citywide one-death report is visible but explicitly excluded from additive use because of overlap risk.

The four pre-snapshot incident reports (Kramatorsk Oct. 5, Ivano-Frankivsk, Synelnykove and Zaporizhia Oct. 9) are source-backed current-ledger records, but their absence from the contemporaneous chronology snapshots means there is no positive evidence that they entered the selected subtotal. Do not treat them as included or assign effective dates by inference.

## Data handling

- No incident records or revision histories changed.
- No `ledger_effective_at` values changed.
- No chronology entries or public figures changed.
- The Oct. 11 historical subtotal remains ≈80, with the 82 row-sum reconstruction in Stage 73.
- The current raw ledger remains 449 overall; public method-page minimum remains 421.

## Next work

1. Continue checking the Oct. 11–14 commit chain for any first appearance of the four pre-snapshot incident records.
2. If they were added to the chronology after Oct. 11, record their addition date separately from the incident date and from any confirmed dashboard inclusion date.
3. Preserve the distinction between a record's existence in the current ledger and its inclusion in a historical running subtotal.
