> **Superseded in part by Stage 115 (Nov. 27, 2026):** The Oct. 14 consolidated report described three deaths in total across Desniansky and Holosiivsky: two Desniansky deaths already counted in 80→81→82, plus one Holosiivsky death. Therefore the 82→85 (+3) transition cannot be treated as three additional distinct deaths. The Oct. 13 Desniansky incident's final toll is now three, and the separate Holosiivsky incident's final toll is two. The combined final toll is five, not seven. The 82→85 dashboard arithmetic remains under review; no guessed correction has been applied to the public 427. Retain the checkpoint below as the Nov. 26 reconstruction snapshot.

# Stage 70 checkpoint — Oct. 11–14 selected-incident subtotal sequence

Date: 2026-11-26

## Scope
Reconstruct the contemporaneous selected-incident death subtotal from the Oct. 11 approximately-80 snapshot through the Oct. 14 approximately-90 snapshot. This is a historical method-page audit, not a revision of the current incident ledger or the public minimum.

## Verified snapshots and changes

1. **Oct. 11 baseline — approximately 80.** Commit `733a9b45892d232c5e0e2f2ac120f659ef58002b` explicitly itemizes six deaths in the Oct. 7–8 Kyiv reports: Darnytsky 2, Desniansky 2 and Solomiansky shop 2. It warns that broader citywide totals may overlap and are not added separately. The two initial shop deaths are therefore positively confirmed as included in this baseline. The later third shop victim must not be backdated.

2. **Oct. 13 Kyiv ballistic strike — approximately 80→81.** Commit `b630f05c50a0aa7459815a4e63b16e662f63b791` raises the dashboard from ≈80 to ≈81 and says the increase follows Kyiv mayor Vitali Klitschko's report of one death after the Oct. 13 ballistic strike. This is an explicitly attributed +1.

3. **Further body after the Oct. 13 strike — approximately 81→82.** Commit `e394809eb026530afc1933ccf9514483a740fb1f` raises ≈81 to ≈82. The method text says a further body was recovered after the strike, as reported by the compiler, and expressly notes that a linked published source for the revised toll was pending. This is a contemporaneous compiler report, not independently source-linked in that snapshot.

4. **Oct. 13–14 Kyiv overnight attack — approximately 82→85.** Commit `6096fa1309044424382b309e2545033c8b017eec` changes the dashboard to ≈85. Its update note says three deaths and at least 23 injured were reported across Desniansky, Holosiivsky and Darnytsky districts. The chronology entry preserves successive reports: the prosecutor initially reported four deaths for the wider overnight/morning attack, the police count later differed, and subsequent State Emergency Service/media reporting raised the toll. The consolidated update reported three deaths in total, including the two Desniansky deaths already counted in 80→81→82 and one Holosiivsky death. Stage 115 shows that the +3 cannot be treated as three additional distinct deaths; the dashboard increment is under review for duplicate inclusion. The 82→85 arithmetic is explicit in the sequence of snapshots and update note.

5. **Lutsk — approximately 85→89.** Commit `10a74ad99f3fb3911689965e6449fe41ded0c772` adds a Lutsk attack entry after Suspilne Lutsk reported the Volyn National Police confirmation of four deaths. The method paragraph says ≈89 includes four deaths reported in Kyiv and four in Lutsk on Oct. 14. This is an explicitly documented +4.

6. **Revised Kyiv toll — approximately 89→90.** Commit `fdbf9759933d6119841de42baf50ab0c03f19a2b` updates the existing Oct. 14 Kyiv attack entry to reflect Censor.NET's later report of five deaths and more than 30 injured, and raises the subtotal ≈89→≈90. The method wording changes from “four deaths reported in Kyiv” to “at least five deaths reported in Kyiv.” This is a revision of the same attack, not a separate incident. The chronology explicitly preserves the successive prosecutor, police, SES and later media reports rather than adding their tolls together.

## Reconciliation limits
- The visible sequence of displayed values is ≈80→81→82→85→89→90, but Stage 115 establishes that the 82→85 step is not a clean incident-level +3. The exact historical subtotal correction is not imposed.
- The Oct. 11 six-death Kyiv group is explicitly present in the baseline. Later wording “four deaths reported in Kyiv” and then “at least five deaths reported in Kyiv” refers to the new Oct. 13–14 attack toll, not a restatement or subtraction of the earlier six.
- The Oct. 14 attack's three-, four- and five-death reports are successive toll updates for the combined Kyiv attack. The final incident split is three deaths in Desniansky plus two in Holosiivsky. The initial three-death update repeats two deaths already counted at 80→81→82, so the +3 transition may double count those people in the historical subtotal.
- The extra Oct. 13 strike death at ≈82 was based on the compiler's report, with the contemporaneous method explicitly flagging the absence of a linked published source.
- This reconstruction does not prove the complete incident composition of every approximate subtotal. It does not resolve all earlier possible overlap or omission questions, nor establish the exact membership of the Solomiansky shop deaths in every later snapshot.
- The approximate selected-incident totals are historical editorial snapshots, not the current structured ledger sum and not the public nationwide documented minimum.

## Changes made
No changes to `fatality-ledger/incidents.json`, incident records, effective dates, chronology entries, the public dashboard or public method-page minimum. The public method-page minimum remains 421.

## Source commits
- Oct. 11 baseline: `733a9b45892d232c5e0e2f2ac120f659ef58002b`
- Oct. 13 +1: `b630f05c50a0aa7459815a4e63b16e662f63b791`
- Oct. 13 further body +1: `e394809eb026530afc1933ccf9514483a740fb1f`
- Oct. 14 consolidated Kyiv attack +3: `6096fa1309044424382b309e2545033c8b017eec`
- Oct. 14 Lutsk +4: `10a74ad99f3fb3911689965e6449fe41ded0c772`
- Oct. 14 Kyiv toll revision +1: `fdbf9759933d6119841de42baf50ab0c03f19a2b`
