# Stage 124 checkpoint — trace the Oct. 14 subtotal through the Oct. 28 baseline

Date: Nov. 27, 2026

## Scope

Trace the historical dashboard from ≈92 on Oct. 14 through ≈148 on Oct. 28. The question is whether the Oct. 14 one-death discrepancy disappears in a later correction, and what other scope differences enter the 148 baseline. This is a historical bridge audit; it does not authorize a correction to the current 427 public minimum.

## Reconstructed sequence

| Transition | Dated addition or scope change | Adjudication |
|---|---|---|
| 92→95, Oct. 15 | Three deaths in Kirovohrad region | Three-death incident; supported and dated Oct. 15. |
| 95→98, Oct. 16 | Three deaths reported in the Kharkiv market strike | The final incident toll is two. The later official correction did not produce a -1 dashboard subtraction. This leaves a second known one-death overstatement in the historical subtotal. |
| 98→99, Oct. 19 | One death in Kyiv from the overnight ballistic attack | Commit `ac5b47d` raises the dashboard from ≈98 to ≈99 and updates the method paragraph to include the 21-year-old woman killed in Kyiv. |
| 99→102, Oct. 20 | Three deaths in Chabany | Commit `a2ebd83` raises the dashboard from ≈99 to ≈102 and explicitly includes the three Chabany deaths in the method paragraph. |
| 102→103, Oct. 20 | One death in Holosiivsky district | Commit `f40e650` raises the dashboard from ≈102 to ≈103 after adding the Holosiivsky death. The method paragraph at this commit remains stale at ≈102. |
| 103→100, Oct. 20 | Three Chabany deaths removed from the subtotal | Commit `25abf34` changes the dashboard from ≈103 to ≈100 and labels the Chabany deaths as attributed to an unverified local Telegram channel and excluded. The method paragraph in that commit remains stale at ≈103 and still says Chabany is included; the Oct. 21 method paragraph resolves the inconsistency by explicitly excluding them. |
| 100→105, Oct. 21 | Five deaths: two in Sviatoshynsky district and three Kramatorsk heating-supply workers | Commit `84c0c69` raises the dashboard from ≈100 to ≈105. The revised method paragraph names these five and retains the Kyiv and Holosiivsky deaths already in the 100 baseline. |
| 98→105 net | Seven deaths retained above the Oct. 16 baseline: one Kyiv death from Oct. 19, one Holosiivsky death from Oct. 20, two in Sviatoshynsky district and three Kramatorsk heating-supply workers | Net increase is +7: +1 Kyiv, +3 Chabany, +1 Holosiivsky, −3 Chabany, then +5. The final ≈105 method paragraph explicitly excludes Chabany and names the seven deaths retained above 98. |
| 105→116, Oct. 21 | Nine deaths in Sloviansk and two in Korotych | The ≈116 method paragraph explicitly itemizes the 9+2. |
| 116→117, Oct. 22 | One death in Lymanivka, Lozova community | Explicitly added in the Oct. 22 update. |
| 117→118, Oct. 22 | One death in Kyiv from the overnight attack | Explicitly added in the Oct. 22 update. |
| 118→121, Oct. 22 | Three deaths in Chabany | Explicitly included after corroboration, but later excluded from the current structured ledger because the source basis was judged insufficiently verified. |
| 121→123, Oct. 22 | +2 while the dashboard changed from selected-incident subtotal to nationwide documented minimum | Scope/method change. No two incidents or new deaths were identified in the commit. Do not allocate +2 to incident records. |
| 123→132, Oct. 25 | Nine deaths: four in Synelnykove, one in Kharkiv and four reported across other regions on Oct. 23 | The update history itemizes the nine-death addition. |
| 132→137, Oct. 26 | Five deaths in Nikopol district, Lozova, Sumy region and Yarova | The update history itemizes the five-death addition; the Lozova component is limited to the first two market deaths. |
| 137→138, Oct. 26 | One death in Kramatorsk | Separate one-death addition. |
| 138→141, Oct. 26 | One each in Pavlohrad, Kherson and Yasnohirka | Three-death addition. |
| 141→142, Oct. 27 | One death in Kyiv | Explicit one-death addition. |
| 142→143, Oct. 27 | Sixth death in Nova Vodolaha after a child died in hospital | Explicit one-death revision. |
| 143→146, Oct. 27 | Three deaths reported by Donetsk regional administration | Explicit three-death addition. |
| 146→147, Oct. 28 | One death in Novodonetske | Explicit one-death addition. |
| 147→148, Oct. 28 | One death in Kharkiv | Explicit one-death addition. |

The Oct. 22 118→121 and 121→123 distinctions are documented in Stage 63. The Oct. 25–28 sequence is documented in Stage 100. The 92→118 incident inclusions are documented in Stages 78–85 and 101.

## Findings

1. **The Oct. 14 discrepancy survives to the 118 snapshot.** Stage 122 reconstructs the 82→92 sequence as ten published additions but nine distinct deaths, conditional on accepting the ≈82 baseline. No later subtotal update subtracts the excess.
2. **A second one-death overstatement enters at 95→98.** The Oct. 16 update adds three Kharkiv market deaths; the final incident toll is two, and the historical dashboard shows no -1 correction. This is documented in Stage 79.
3. **The Oct. 20–21 bridge contains a temporary Chabany inclusion and correction.** The 98→105 net increase is seven, but the intermediate snapshots show 98→99 (+1 Kyiv), 99→102 (+3 Chabany), 102→103 (+1 Holosiivsky), 103→100 (−3 Chabany correction), and 100→105 (+5, two Sviatoshynsky deaths and three Kramatorsk heating workers). The Oct. 21 method paragraph confirms Chabany is excluded from 105. This correction is separate from the later 118→121 Chabany inclusion on Oct. 22, which Stage 63 documents as a renewed inclusion after corroboration.
4. **The 121→123 step is a scope change of +2 with no incident-level allocation.** It must not be treated as two new deaths in the ledger.
5. **The 123→148 bridge adds 25 through itemized Oct. 25–28 updates.** The Oct. 28 ≈148 baseline therefore carries forward the two known one-death overstatements unless a separate subtraction can be found. The surviving 148→421 bridge is additive and records no such subtraction.

## Why 427 remains unchanged

The historical bridge is now clearer, but ≈148 is not a complete incident roster. It contains the three Chabany deaths later excluded from the structured ledger, the unexplained 121→123 scope change, and the two one-death historical subtotal overstatements. Other current-ledger incidents still have unresolved membership in the 148 baseline or later 421 carry-forward. These positive and negative differences cannot be collapsed into a single correction without a complete incident-level roster.

The 148→421 bridge and later 421→427 update do not record a subtraction for either one-death overstatement. They therefore appear to carry the historical differences forward. This is evidence about the published subtotal's lineage, not a sufficient basis to revise 427 while other membership questions and the +2 scope change remain unresolved.

## Integrity

- No incident death toll or effective date changed in this stage.
- No `incidents.json` change was made.
- Public minimum remains 427 through Nov. 26.
- The Oct. 14 one-death discrepancy and Oct. 16 Kharkiv-market one-death correction remain separately documented.
- The 17-entry historical-inclusion queue, net +27, remains open.

## References

- Stage 122: `STAGE-122-CHECKPOINT.md` — Oct. 14 82→92 transition.
- Stage 123: `STAGE-123-CHECKPOINT.md` — correction of Lutsk REV-003 inclusion date.
- Stage 63: `STAGE-63-CHECKPOINT.md` — Chabany inclusion and 121→123 scope change.
- Stage 78: `STAGE-78-CHECKPOINT.md` — Lutsk and Kirovohrad dates.
- Stage 79: `STAGE-79-CHECKPOINT.md` — Kharkiv market 3→2 correction.
- Stages 81–85 and 101: dated Oct. 21–22 inclusions.
- Stage 100: `STAGE-100-CHECKPOINT.md` — 123→148 bridge.
- Stage 106: `STAGE-106-CHECKPOINT.md` — 148→421 carry-forward.

No public chronology, dashboard figure or public subtotal was changed.
