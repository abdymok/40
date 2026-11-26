# Stage 76 checkpoint — date seven Oct. 11 baseline revisions

Date: 2026-11-26

## Finding

The Oct. 11 historical snapshot at commit `733a9b45892d232c5e0e2f2ac120f659ef58002b` explicitly supports a selected-incident subtotal of approximately 80. Stage 73 reconstructs the seven selected incident/region rows as 82, excluding the separate one-death Kyiv citywide aggregate. The current ledger contains the same seven incident records, and their snapshot counts are established.

The first documented inclusion date for the seven snapshot-count revisions below is therefore set to **2026-10-11** in `ledger_effective_at`:

| Incident | Revision dated | Count at the Oct. 11 snapshot |
|---|---|---:|
| Pryluky residential strike | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE-REV-004` | 22 |
| Kramatorsk bus/residential strike | `UA-DON-KRAMATORSK-2026-10-08-TWO-BUSES-STRIKE-REV-003` | 33 |
| Zaporizhia residential strike | `UA-ZAP-ZAPORIZHIA-2026-10-10-RESIDENTIAL-GLIDE-BOMBS-REV-001` | 20 |
| Pokrovske community death | `UA-DNE-NIKOPOL-POKROVSKE-2026-10-10-DRONE-BOY-REV-001` | 1 |
| Kyiv, Darnytsky district | `UA-KYI-KYIV-DARNYTSKY-2026-10-07-ATTACK-REV-001` | 2 |
| Kyiv, Desniansky residential strike | `UA-KYI-KYIV-DESNIANSKY-2026-10-07-RESIDENTIAL-STRIKE-REV-001` | 2 |
| Kyiv, Solomiansky shop strike | `UA-KYI-KYIV-SOLOMIANSKY-2026-10-08-SHOP-STRIKE-REV-001` | 2 |

The seven snapshot values sum to 82. The field records the first confirmed inclusion in the selected-incident subtotal. It does not assert that the same incidents were absent from, or not considered in, the earlier broad Oct. 10 estimate.

## Revisions deliberately left undated

- Earlier interim Pryluky revisions (14, 16 and 20) remain null because the Oct. 11 snapshot proves the final 22-death count, not the date each interim count entered a running subtotal.
- Earlier interim Kramatorsk revisions (12 and 30) remain null for the same reason.
- The later Zaporizhia revision from 20 to 23 remains null. The Oct. 11 snapshot shows 20; no later selected-subtotal snapshot in this stage establishes when 23 entered the running total.
- The later Solomiansky shop revision from two to three remains null. The Oct. 11 method and chronology still say two, despite the later same-day police report confirming three. Its subsequent inclusion in a running subtotal is not established.
- The unallocated Oct. 8 Kyiv citywide death remains excluded from additive use because the method explicitly warns of overlap with incident-level reports.
- The other pre-Oct. 12 ledger records remain unresolved as described in Stage 75.

## Updated null-revision inventory

After dating these seven revisions:
- Null revision entries: 46
- Remaining pre-Oct. 29 null entries: 39, net +107
- Later null entries: 7, net +8
- Total net change across remaining null revisions: +115

These are unresolved historical inclusion changes, not additional deaths to add to the public total.

## Changes made

- Set `ledger_effective_at: "2026-10-11"` for the seven final-count revisions listed above.
- Updated the reason text for those seven revisions to record the evidence basis.
- No `documented_deaths` values, source records, incident identities or incident dates changed.
- No chronology or public dashboard values changed.
- Current raw ledger sum remains 449.
- Public method-page minimum remains 421.

## Verification

The ledger JSON was reparsed after the edit. Unique incident IDs and revision IDs, revision continuity, count totals, and effective-date formats were checked. The remaining null-revision inventory was recalculated from the edited dataset and saved separately.
