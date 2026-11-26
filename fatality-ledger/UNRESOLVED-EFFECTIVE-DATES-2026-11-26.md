# Unresolved ledger-effective dates — Nov. 26, 2026

This inventory lists every revision whose `ledger_effective_at` remains null after Stage 85. A null date does not mean the death is unverified or excluded from the incident-level ledger. It means the date on which the project included that revision in the historical public subtotal has not been established, or the revision may overlap with an earlier subtotal.

## Summary

- Null revision entries: 33
- Net sum of count changes across these entries: 100
- Legacy pre-Oct. 29 entries: 26 entries, 82 net count changes
- Oct. 29 additional Izium revisions: 2 entries, 2 deaths
- Oct. 31 Sloviansk: 1 entry, 1 death
- Nov. 3 Dnipro second death: 1 entry, 1 death
- Nov. 11 Saltivsky first death: 1 entry, 1 death
- Nov. 11 Chornomorsk later hospital revisions: 2 entries, 3 deaths

The 26 remaining pre-Oct. 29 entries carry 82 net count changes, including one -1 correction in the Kharkiv market incident. Seven final-count revisions in the Oct. 11 ≈80 selected-incident baseline are now dated Oct. 11; see Stage 76. The other legacy revisions remain unresolved. The remaining seven entries account for eight further deaths with specific inclusion/overlap questions. These are not 147 additional deaths and must not be added to the public total as a block.

## Stage 76 adjudication

The Oct. 11 snapshot explicitly supports the final counts for seven selected incidents. The following revisions now have `ledger_effective_at: 2026-10-11`: Pryluky REV-004 (22), Kramatorsk bus strike REV-003 (33), Zaporizhia residential strike REV-001 (20), Pokrovske REV-001 (1), Darnytsky REV-001 (2), Desniansky REV-001 (2), and Solomiansky shop REV-001 (2). These seven values sum to 82. Earlier interim revisions for Pryluky and Kramatorsk, the later Zaporizhia 23 revision and later Solomiansky shop 3 revision remain null because their separate inclusion dates are not established. See `STAGE-76-CHECKPOINT.md`.

## Stage 77 adjudication

The Oct. 14 Kyiv overnight-attack record now reflects the successive official tolls of three, four and five. Its three revisions have `ledger_effective_at: 2026-10-14`, supported by the Oct. 14 dashboard sequence and method text. The initial three-death revision was previously in the null inventory and is now removed; the two later revisions were created with confirmed effective dates. See `STAGE-77-CHECKPOINT.md`.

## Stage 78 adjudication

The Oct. 14–15 method-page sequence explicitly establishes inclusion of the Lutsk revisions and the Kirovohrad incident: Lutsk's three- and four-death revisions entered the selected subtotal on Oct. 14 (85→89 adds four); the later four-to-six revision entered on Oct. 15 (90→92 adds two); and the Kirovohrad three-death incident entered on Oct. 15 (92→95 adds three). These four revisions now have `ledger_effective_at` dates of Oct. 14 or Oct. 15. See `STAGE-78-CHECKPOINT.md`.

## Stage 79 adjudication

For the Oct. 16 Kharkiv market incident, REV-001 (—→3) is now dated Oct. 16 because the archived dashboard update explicitly raised the selected subtotal 95→98 and named three deaths in Kharkiv. REV-002 (3→2) remains null: the regional administration later confirmed two, but the Oct. 16 dashboard snapshot continued to show ≈98 and the historical public sequence contains no documented -1 subtraction. The ledger keeps the final incident toll at two. See `STAGE-79-CHECKPOINT.md`.

## Stage 80 adjudication

The two revisions to the Oct. 13 Kyiv ballistic residential-building strike are now dated Oct. 14. The archived dashboard commits explicitly move the selected subtotal 80→81 for the first reported death and 81→82 for the second body recovered. The commits are timestamped just after midnight Kyiv time on Oct. 14, although GitHub records them on Oct. 13 UTC. See `STAGE-80-CHECKPOINT.md`.

## Stage 81 adjudication

The Oct. 21 dashboard/method update establishes inclusion of the final nine-death Sloviansk toll and the two Korotych deaths in the approximately-116 subtotal. Sloviansk REV-003 is dated Oct. 21; its earlier 1- and 6-death interim revisions remain null because their separate entry into the running subtotal is not established. Korotych REV-001's date is corrected from Oct. 22 to Oct. 21. See `STAGE-81-CHECKPOINT.md`.

## Stage 82 adjudication

Lymanivka REV-001 (—→1) is now dated Oct. 22. Commit `3513193d093e5166b216f9112bd25da39f8dbb41` adds the fatal incident and explicitly raises the selected subtotal 116→117; the Oct. 22 method snapshot includes the death. See `STAGE-82-CHECKPOINT.md`.

## Stage 83 adjudication

The Oct. 26 Uman death is not included in the Oct. 28 ≈148 baseline: the 138→141 update names three other deaths, and subsequent increments to 148 are separately itemized without Uman. The 174→192 transition on Nov. 2 is explicitly the Komyshuvakha revision; the 174 baseline's itemized additions also do not identify Uman. The current dashboard update history contains no Uman reference. Later inclusion in the 421 minimum is not proven, so Uman REV-001 remains null. See `STAGE-83-CHECKPOINT.md`.

## Stage 84 adjudication

The Oct. 21 ≈105 method snapshot explicitly includes two Sviatoshynsky deaths and three Kramatorsk heating-supply workers. Both revisions are now dated Oct. 21, the first documented inclusion date. The Oct. 22 ≈118 method snapshot independently repeats both items. See `STAGE-84-CHECKPOINT.md`.

## Stage 85 adjudication

The Oct. 21 ≈116 method snapshot explicitly includes one death in Holosiivsky district on Oct. 20 and the 21-year-old woman killed in Kyiv on Oct. 19. Both revisions are now dated Oct. 21, the first documented inclusion date in the selected subtotal. See `STAGE-85-CHECKPOINT.md`.

## Adjudication rules

1. Do not assign Oct. 28 to every pre-Oct. 29 incident merely because the 148 snapshot exists. The 148 baseline's incident membership must be reconstructed from archived change logs and sources.
2. The two additional Oct. 29 Izium deaths remain separate from the historical 25-death cohort. Do not add them to a later subtotal without a dated source-to-dashboard link.
3. The Oct. 31 Sloviansk death must be checked against the 174 pre-Komуshuvakha baseline and 192 opening snapshot.
4. The second Nov. 3 Dnipro death is documented in the incident record, but the method's Nov. 3 update adds only one.
5. The initial Saltivsky death is not assigned as a new increment because the method's 283→284 step adds only one and says the first was already in the preceding subtotal.
6. The two later Chornomorsk revisions add three deaths to the incident's final count of four, but the public 421 change history only establishes the initial death.

## Complete null-revision inventory

| Incident date | Incident ID | Revision | Count change | Delta | Unresolved category |
|---|---|---|---:|---:|---|
| 2026-10-05 | `UA-DON-KRAMATORSK-2026-10-05-AMBULANCE-AND-HIGHRISE` | `UA-DON-KRAMATORSK-2026-10-05-AMBULANCE-AND-HIGHRISE-REV-001` | — → 1 | +1 | Public subtotal retained three; -1 correction not reflected |
| 2026-10-07 | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE` | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE-REV-001` | — → 14 | +14 | Not in 148; later 421 inclusion unproven |
| 2026-10-07 | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE` | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE-REV-002` | 14 → 16 | +2 | Legacy 148 membership unresolved |
| 2026-10-07 | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE` | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE-REV-003` | 16 → 20 | +4 | Legacy 148 membership unresolved |
| 2026-10-08 | `UA-DON-KRAMATORSK-2026-10-08-TWO-BUSES-STRIKE` | `UA-DON-KRAMATORSK-2026-10-08-TWO-BUSES-STRIKE-REV-001` | — → 12 | +12 | Legacy 148 membership unresolved |
| 2026-10-08 | `UA-DON-KRAMATORSK-2026-10-08-TWO-BUSES-STRIKE` | `UA-DON-KRAMATORSK-2026-10-08-TWO-BUSES-STRIKE-REV-002` | 12 → 30 | +18 | Legacy 148 membership unresolved |
| 2026-10-08 | `UA-IFR-IVANO-FRANKIVSK-2026-10-08-DRONE-DEBRIS` | `UA-IFR-IVANO-FRANKIVSK-2026-10-08-DRONE-DEBRIS-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-08 | `UA-KYI-KYIV-2026-10-08-MORNING-ATTACK-UNALLOCATED` | `UA-KYI-KYIV-2026-10-08-MORNING-ATTACK-UNALLOCATED-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-08 | `UA-KYI-KYIV-SOLOMIANSKY-2026-10-08-SHOP-STRIKE` | `UA-KYI-KYIV-SOLOMIANSKY-2026-10-08-SHOP-STRIKE-REV-002` | 2 → 3 | +1 | Legacy 148 membership unresolved |
| 2026-10-09 | `UA-DNE-SYNELNYKOVE-DISTRICT-2026-10-09-ATTACKS` | `UA-DNE-SYNELNYKOVE-DISTRICT-2026-10-09-ATTACKS-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-09 | `UA-ZAP-ZAPORIZHIA-2026-10-09-GUIDED-BOMB-STRIKE` | `UA-ZAP-ZAPORIZHIA-2026-10-09-GUIDED-BOMB-STRIKE-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-10 | `UA-ZAP-ZAPORIZHIA-2026-10-10-RESIDENTIAL-GLIDE-BOMBS` | `UA-ZAP-ZAPORIZHIA-2026-10-10-RESIDENTIAL-GLIDE-BOMBS-REV-002` | 20 → 23 | +3 | Legacy 148 membership unresolved |
| 2026-10-11 | `UA-DON-SLOVIANSK-2026-10-11-ATTACK` | `UA-DON-SLOVIANSK-2026-10-11-ATTACK-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-12 | `UA-KHA-KHARKIV-2026-10-12-KHOLODNOGIRSKY-RESIDENTIAL-STRIKE` | `UA-KHA-KHARKIV-2026-10-12-KHOLODNOGIRSKY-RESIDENTIAL-STRIKE-REV-001` | — → 4 | +4 | Legacy 148 membership unresolved |
| 2026-10-12 | `UA-KYI-KYIV-DARNYTSKY-2026-10-12-RESIDENTIAL-DRONE` | `UA-KYI-KYIV-DARNYTSKY-2026-10-12-RESIDENTIAL-DRONE-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-12 | `UA-KYI-KYIV-DARNYTSKY-2026-10-12-RESIDENTIAL-DRONE` | `UA-KYI-KYIV-DARNYTSKY-2026-10-12-RESIDENTIAL-DRONE-REV-002` | 1 → 2 | +1 | Legacy 148 membership unresolved |
| 2026-10-16 | `UA-KHA-KHARKIV-2026-10-16-MARKET-STRIKE` | `UA-KHA-KHARKIV-2026-10-16-MARKET-STRIKE-REV-002` | 3 → 2 | -1 | Legacy 148 membership unresolved |
| 2026-10-17 | `UA-DON-SLOVIANSK-2026-10-17-RESIDENTIAL-AIRSTRIKES` | `UA-DON-SLOVIANSK-2026-10-17-RESIDENTIAL-AIRSTRIKES-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-17 | `UA-DON-SLOVIANSK-2026-10-17-RESIDENTIAL-AIRSTRIKES` | `UA-DON-SLOVIANSK-2026-10-17-RESIDENTIAL-AIRSTRIKES-REV-002` | 1 → 6 | +5 | Legacy 148 membership unresolved |
| 2026-10-17 | `UA-KHE-KHERSON-2026-10-17-KORABELNY-DOUBLE-TAP` | `UA-KHE-KHERSON-2026-10-17-KORABELNY-DOUBLE-TAP-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-19 | `UA-KHA-NOVA-VODOLAHA-2026-10-19-CENTRAL-PARK-DRONE` | `UA-KHA-NOVA-VODOLAHA-2026-10-19-CENTRAL-PARK-DRONE-REV-001` | — → 3 | +3 | Legacy 148 membership unresolved |
| 2026-10-19 | `UA-KHA-NOVA-VODOLAHA-2026-10-19-CENTRAL-PARK-DRONE` | `UA-KHA-NOVA-VODOLAHA-2026-10-19-CENTRAL-PARK-DRONE-REV-002` | 3 → 6 | +3 | Legacy 148 membership unresolved |
| 2026-10-21 | `UA-CHE-UMAN-2026-10-21-PRIVATE-HOUSE-DRONE-STRIKE` | `UA-CHE-UMAN-2026-10-21-PRIVATE-HOUSE-DRONE-STRIKE-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-21 | `UA-KYI-KYIV-DNIPROVSKY-2026-10-21-BALLISTIC` | `UA-KYI-KYIV-DNIPROVSKY-2026-10-21-BALLISTIC-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-22 | `UA-KHA-LOZOVA-2026-10-22-CENTRAL-MARKET` | `UA-KHA-LOZOVA-2026-10-22-CENTRAL-MARKET-REV-002` | 2 → 3 | +1 | Legacy 148 membership unresolved |
| 2026-10-24 | `UA-KHA-LOZOVA-2026-10-24-WAREHOUSE-MISSILE` | `UA-KHA-LOZOVA-2026-10-24-WAREHOUSE-MISSILE-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-29 | `UA-KHA-IZIUM-2026-10-29-OTHER-ATTACK-59YO` | `UA-KHA-IZIUM-2026-10-29-OTHER-ATTACK-59YO-REV-001` | — → 1 | +1 | Oct. 29 extra death; inclusion after 173 unverified |
| 2026-10-29 | `UA-KHA-IZIUM-2026-10-29-PUBLIC-HEALTH-INSTITUTION` | `UA-KHA-IZIUM-2026-10-29-PUBLIC-HEALTH-INSTITUTION-REV-002` | 4 → 5 | +1 | Oct. 29 extra death; inclusion after 173 unverified |
| 2026-10-31 | `UA-DON-SLOVIANSK-2026-10-31-ATTACK` | `UA-DON-SLOVIANSK-2026-10-31-ATTACK-REV-001` | — → 1 | +1 | Nov. 2 baseline inclusion unverified |
| 2026-11-03 | `UA-DNE-DNIPRO-2026-11-03-MORNING-STRIKE` | `UA-DNE-DNIPRO-2026-11-03-MORNING-STRIKE-REV-002` | 1 → 2 | +1 | Second death not established in 421 subtotal |
| 2026-11-11 | `UA-KHA-KHARKIV-SALTIVSKY-2026-11-11-DRONE-STRIKE` | `UA-KHA-KHARKIV-SALTIVSKY-2026-11-11-DRONE-STRIKE-REV-001` | — → 1 | +1 | First death may be included in preceding subtotal; overlap unresolved |
| 2026-11-11 | `UA-ODE-CHORNOMORSK-2026-11-11-MARKET` | `UA-ODE-CHORNOMORSK-2026-11-11-MARKET-REV-002` | 1 → 3 | +2 | Later hospital deaths not established in 421 subtotal |
| 2026-11-11 | `UA-ODE-CHORNOMORSK-2026-11-11-MARKET` | `UA-ODE-CHORNOMORSK-2026-11-11-MARKET-REV-003` | 3 → 4 | +1 | Later hospital deaths not established in 421 subtotal |

## Next audit

Reconstruct the legacy 148 membership from the archived chronology and change log, beginning with the 123 baseline and the Oct. 25–28 increments. Resolve the Oct. 31 Sloviansk inclusion separately. Do not change public totals until the incident-level membership and overlap questions are closed.
