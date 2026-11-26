# Unresolved ledger-effective dates — Nov. 26, 2026

This inventory lists every revision whose `ledger_effective_at` remains null after Stage 103. A null date does not mean the death is unverified or excluded from the incident-level ledger. It means the date on which the project included that revision in the historical public subtotal has not been established, or the revision may overlap with an earlier subtotal.

## Summary

- Null revision entries: 33
- Net sum of count changes across these entries: 90
- Legacy pre-Oct. 29 entries: 26 entries, 82 net count changes
- Nov. 11 Saltivsky first death: 1 entry, 1 death (not included in 421)
- Oct. 29 additional Izium revisions: 2 entries, 2 deaths (later inclusion in 421 unproven)
- Oct. 31 Sloviansk: 1 entry, 1 death (174-baseline membership unverified)
- Nov. 3 Dnipro second death: 1 entry, 1 death (not in mapped Nov. 3 increment)
- Nov. 11 Chornomorsk later hospital revisions: 2 entries, 3 deaths

The 26 remaining pre-Oct. 29 entries carry 82 net count changes, including one -1 correction in the Kharkiv market incident. Seven final-count revisions in the Oct. 11 ≈80 selected-incident baseline are now dated Oct. 11; see Stage 76. The other legacy revisions remain unresolved. The seven remaining post-Oct. 29 entries account for eight further deaths with specific inclusion/overlap questions: two additional Oct. 29 Izium revisions, the Oct. 31 Sloviansk death, the second Nov. 3 Dnipro death, the first Nov. 11 Saltivsky death and two later Chornomorsk revisions. Together with the seven post-Oct. 29 entries, the 26 legacy entries bring the unresolved revisions to a net arithmetic change of 90. This is not 89 additional deaths to be added to the public total as a block.

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

## Stage 86 adjudication

The first Saltivsky death is now dated Nov. 11. The ≈282 snapshot precedes the separate Chornomorsk 282→283 increment; the subsequent 283→284 Saltivsky update explicitly says the first death was already in the preceding subtotal. The first death was therefore present by the Nov. 11 ≈282 snapshot; the second death is the later Nov. 11 increment. See `STAGE-86-CHECKPOINT.md`.

## Stage 97 adjudication

The ≈283 snapshot commit `9a8a5b44430108fdb04e4744a1ff2dc8a88db799` predates Terekhov's first death report (13:37 UTC) and second-death update (13:43 UTC). The 283→284 commit `26a44c4287b2429832fc9f2fc26087cfe45c7e12` adds only one and is titled “Add second Kharkiv strike death and update dashboard.” REV-002 remains dated Nov. 11; REV-001 is returned to null and is not included in the 421 subtotal. See `STAGE-97-CHECKPOINT.md`.

## Stage 88 adjudication

The Nov. 3 dashboard sequence maps 203→207 to four deaths in Donetsk region from Nov. 2, including a Nov. 2 Sloviansk incident distinct from the Oct. 31 death. The first Dnipro death is the 207→208 increment; the subsequent 208→211 changes are Komyshuvakha 29→31 (+2) and Hotiv (+1). The second Dnipro death is not part of the mapped sequence. The Oct. 31 Sloviansk death is not named in the 174 baseline's incident-level list, and its carry-forward membership cannot be established. Both revisions remain null. See `STAGE-88-CHECKPOINT.md`.

## Stage 89 adjudication

The Nov. 2 174 baseline itemizes four deaths in the Oct. 29 Izium airstrike and one death in a separate Nov. 2 morning attack. It does not itemize the fifth death in the Oct. 29 airstrike, reported later on Oct. 30, or the separate 59-year-old victim killed in another Oct. 29 attack, first identified Oct. 31. The later 421 reconciliation names no separate additions for either revision. Their inclusion in a later, non-itemized subtotal is unproven, so both remain null. See `STAGE-89-CHECKPOINT.md`.

## Stage 90 adjudication

The Oct. 12 Kharkiv strike killed four people, with the fourth body recovered on Oct. 13. The archived 80→82 increments are explicitly attributed to the separate Kyiv ballistic strike, and 82→85 adds three deaths in the Oct. 13–14 Kyiv overnight attack. The 148→173 breakdown does not itemize this Kharkiv incident, but the 148 baseline is a carried-forward aggregate, not a complete incident list. Its inclusion in 148 or a later subtotal remains unproven. REV-001 remains null; this is a potential four-death inclusion gap, not a confirmed omission. See `STAGE-90-CHECKPOINT.md`.

## Stage 91 adjudication

The Oct. 12 Darnytsky residential-building strike killed two people. Neither death is named in the 80→92 dashboard increments: those changes concern the Oct. 13 ballistic strike, the separate Oct. 13–14 Kyiv overnight attack and Lutsk. The 148→173 breakdown also does not itemize this incident, but the 148 baseline is not a complete incident list. Both revisions remain null; this is a potential two-death inclusion gap, not a confirmed omission. See `STAGE-91-CHECKPOINT.md`.

## Stage 92 adjudication

The Oct. 11 ≈80 snapshot explicitly records 20 deaths in the Oct. 10 Zaporizhia strike. The final 23-death toll was reported at 15:23 Kyiv time on Oct. 11. A subsequent 17:01 Kyiv-time page update still displayed ≈80 and did not say that the additional three deaths had entered the subtotal. The archived 80→92 increments and the 148→173 breakdown do not itemize the +3 revision. Later inclusion in the 148 carried-forward aggregate cannot be confirmed or ruled out. REV-002 remains null. See `STAGE-92-CHECKPOINT.md`.

## Stage 93 adjudication

The Oct. 9 Synelnykove-district death is not itemized in the Oct. 11 ≈80 snapshot. Its one Dnipropetrovsk-region row is matched in Stage 62 to the separate Pokrovske child death. The Oct. 25 123→132 update's four Synelnykove deaths concern a distinct Oct. 24 attack. The Oct. 22 ≈123 baseline does not enumerate every incident, so the Oct. 9 death's inclusion in 123 or 148 cannot be established. REV-001 remains null. See `STAGE-93-CHECKPOINT.md`.

## Stage 94 adjudication

The Oct. 9 Zaporizhia guided-bomb death is distinct from the Oct. 10 residential strike whose 20-death toll appears in the ≈80 baseline. It is not itemized in that snapshot or the 80→92 changes. The Oct. 11 Sloviansk death was reported on Oct. 12, after the ≈80 cutoff, and is also absent from the 80→92 changes. Neither is individually identified in the carried-forward 148 baseline. Later inclusion remains unverified; both revisions remain null. See `STAGE-94-CHECKPOINT.md`.

## Stage 96 adjudication

The Oct. 20 ≈100/103 and Oct. 21 ≈105 method snapshots do not identify the Oct. 17 Sloviansk incident or its interim tolls of one and six. The Oct. 21 105→116 update explicitly adds the final nine-death toll; the net +11 from 105 to 116 matches nine Sloviansk deaths and two Korotych deaths. No separate inclusion of the one- or six-death interim toll is established. REV-001 and REV-002 remain null; REV-003 (6→9) remains dated Oct. 21. See `STAGE-96-CHECKPOINT.md`.

## Stage 98 adjudication

The Oct. 19 Nova Vodolaha toll progressed 3→preliminary 6→corrected 5. The Oct. 20 ≈100/103 and Oct. 21 ≈105/116 snapshots do not name the incident. The corrected five-death toll is carried by the Oct. 26 ≈138 baseline; the Oct. 27 142→143 increment explicitly adds the sixth death after a 12-year-old boy died in hospital. The initial three and preliminary six revisions were not separately added to the subtotal. REV-001 and REV-002 remain null; REV-003 (6→5) remains dated Oct. 26 and REV-004 (5→6) Oct. 27. See `STAGE-98-CHECKPOINT.md`.

## Stage 99 adjudication

The Oct. 25 death of DTEK driver Vitaliy Shcherbyna is a distinct incident: DTEK and Interfax-Ukraine identify a drone strike on a lorry at a coal-mining enterprise in Dnipropetrovsk region. The regional administration's Oct. 25 casualty update identifies the three deaths in Synelnykove, later revised to four after a wounded man died in hospital. The earlier working note's reference to a one-death Dnipro enterprise incident was incorrect; the ledger's one-death Dnipro incident occurred on Oct. 23.

The Oct. 22 ≈123 baseline predates Shcherbyna's death. The mapped Oct. 25–28 increments identify other incidents and do not include him. A separate incident record has therefore been added to `incidents.json` with one documented death, regional-level location and two sources. Its `ledger_effective_at` remains null because the death is not evidenced in the historical 148 baseline or published 421 minimum. The incident ledger now contains 176 records, 430 source records and 452 final documented deaths; 34 revision entries remain null. The public subtotal remains 421. See `STAGE-99-CHECKPOINT.md` and `UNRESOLVED-DTEK-SHCHERBYNA-OCT25.md`.

## Stage 101 adjudication

The Kyiv ballistic attack that began late on Oct. 21 killed one person. The State Emergency Service confirmed the death in its Oct. 22 morning report. The Oct. 22 dashboard snapshot explicitly lists one person killed in the overnight attack on Kyiv and raises the selected-incident subtotal to approximately 118. Revision `UA-KYI-KYIV-DNIPROVSKY-2026-10-21-BALLISTIC-REV-001` is therefore dated `ledger_effective_at: 2026-10-22`, the first confirmed public inclusion date. This is the same attack recorded in the Oct. 21 incident record, not a second incident. See `STAGE-101-CHECKPOINT.md` and dashboard commit `4ada778321c66b570c73f8d5353617a076db8ee`.

The overall null inventory falls from 34 to 33. The pre-Oct. 29 null inventory falls from 27 (+83 net) to 26 (+82 net). Fourteen pre-Oct. 29 revisions remain unresolved, carrying a net +19. The public 421 minimum is unchanged.

## Stage 100 adjudication

Stage 100 classified 12 of the 27 pre-Oct. 29 null revisions without assigning invented effective dates. Nine are interim or superseded tolls for Pryluky, the Kramatorsk two-bus strike, Sloviansk (Oct. 17) and Nova Vodolaha; their final tolls are represented by separately dated revisions and the interim values are not independent death batches. Two deaths (Uman and DTEK driver Vitaliy Shcherbyna) are not evidenced in the Oct. 28 148 baseline; Uman's later inclusion in 421 remains unproven, while Shcherbyna is not evidenced in the mapped public sequence. One Kharkiv market correction (3→2) was not subtracted from the public count: the Oct. 16 dashboard added three and the subsequent public sequence contains no -1 correction. These 12 entries carry a net arithmetic change of +63, but this is not an amount to add to the public subtotal.

The remaining 15 pre-Oct. 29 null revisions carry a net +20 and still require incident-level membership checks against the Oct. 22–28 snapshots and updates. See `STAGE-100-CHECKPOINT.md`. The total pre-Oct. 29 null inventory remains 27 entries / +83; the overall null count remains 34 / +91.

## Adjudication rules

1. Do not assign Oct. 28 to every pre-Oct. 29 incident merely because the 148 snapshot exists. The 148 baseline's incident membership must be reconstructed from archived change logs and sources.
2. The two additional Oct. 29 Izium deaths remain separate from the historical 25-death cohort. Do not add them to a later subtotal without a dated source-to-dashboard link.
3. The Oct. 31 Sloviansk death must be checked against the 174 pre-Komуshuvakha baseline and 192 opening snapshot.
4. The second Nov. 3 Dnipro death is documented in the incident record, but the mapped Nov. 3 sequence includes only one Dnipro death. The first death is the 207→208 increment; subsequent 208→211 changes are Komyshuvakha (+2) and Hotiv (+1).
5. The initial Saltivsky death is not assigned as a new increment because the method's 283→284 step adds only one and says the first was already in the preceding subtotal.
6. The two later Chornomorsk revisions add three deaths to the incident's final count of four, but the public 421 change history only establishes the initial death.

## Complete null-revision inventory

| Incident date | Incident ID | Revision | Count change | Delta | Unresolved category |
|---|---|---|---:|---:|---|
| 2026-10-05 | `UA-DON-KRAMATORSK-2026-10-05-AMBULANCE-AND-HIGHRISE` | `UA-DON-KRAMATORSK-2026-10-05-AMBULANCE-AND-HIGHRISE-REV-001` | — → 1 | +1 | Public subtotal retained three; -1 correction not reflected |
| 2026-10-07 | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE` | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE-REV-001` | — → 14 | +14 | Not in 148; later 421 inclusion unproven |
| 2026-10-07 | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE` | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE-REV-002` | 14 → 16 | +2 | Potential four-death gap; 148 membership unverified |
| 2026-10-07 | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE` | `UA-CHN-PRYLUKY-2026-10-07-RESIDENTIAL-MISSILE-STRIKE-REV-003` | 16 → 20 | +4 | Legacy 148 membership unresolved |
| 2026-10-08 | `UA-DON-KRAMATORSK-2026-10-08-TWO-BUSES-STRIKE` | `UA-DON-KRAMATORSK-2026-10-08-TWO-BUSES-STRIKE-REV-001` | — → 12 | +12 | Legacy 148 membership unresolved |
| 2026-10-08 | `UA-DON-KRAMATORSK-2026-10-08-TWO-BUSES-STRIKE` | `UA-DON-KRAMATORSK-2026-10-08-TWO-BUSES-STRIKE-REV-002` | 12 → 30 | +18 | Legacy 148 membership unresolved |
| 2026-10-08 | `UA-IFR-IVANO-FRANKIVSK-2026-10-08-DRONE-DEBRIS` | `UA-IFR-IVANO-FRANKIVSK-2026-10-08-DRONE-DEBRIS-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-08 | `UA-KYI-KYIV-2026-10-08-MORNING-ATTACK-UNALLOCATED` | `UA-KYI-KYIV-2026-10-08-MORNING-ATTACK-UNALLOCATED-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-08 | `UA-KYI-KYIV-SOLOMIANSKY-2026-10-08-SHOP-STRIKE` | `UA-KYI-KYIV-SOLOMIANSKY-2026-10-08-SHOP-STRIKE-REV-002` | 2 → 3 | +1 | Legacy 148 membership unresolved |
| 2026-10-09 | `UA-DNE-SYNELNYKOVE-DISTRICT-2026-10-09-ATTACKS` | `UA-DNE-SYNELNYKOVE-DISTRICT-2026-10-09-ATTACKS-REV-001` | — → 1 | +1 | Not in visible ≈80 rows; 123/148 inclusion unverified |
| 2026-10-09 | `UA-ZAP-ZAPORIZHIA-2026-10-09-GUIDED-BOMB-STRIKE` | `UA-ZAP-ZAPORIZHIA-2026-10-09-GUIDED-BOMB-STRIKE-REV-001` | — → 1 | +1 | Not in visible ≈80 rows; later inclusion unverified |
| 2026-10-10 | `UA-ZAP-ZAPORIZHIA-2026-10-10-RESIDENTIAL-GLIDE-BOMBS` | `UA-ZAP-ZAPORIZHIA-2026-10-10-RESIDENTIAL-GLIDE-BOMBS-REV-002` | 20 → 23 | +3 | 20 in Oct. 11 baseline; later +3 inclusion unverified |
| 2026-10-11 | `UA-DON-SLOVIANSK-2026-10-11-ATTACK` | `UA-DON-SLOVIANSK-2026-10-11-ATTACK-REV-001` | — → 1 | +1 | After ≈80 cutoff; later inclusion unverified |
| 2026-10-12 | `UA-KHA-KHARKIV-2026-10-12-KHOLODNOGIRSKY-RESIDENTIAL-STRIKE` | `UA-KHA-KHARKIV-2026-10-12-KHOLODNOGIRSKY-RESIDENTIAL-STRIKE-REV-001` | — → 4 | +4 | Potential four-death gap; 148 membership unverified |
| 2026-10-12 | `UA-KYI-KYIV-DARNYTSKY-2026-10-12-RESIDENTIAL-DRONE` | `UA-KYI-KYIV-DARNYTSKY-2026-10-12-RESIDENTIAL-DRONE-REV-001` | — → 1 | +1 | Potential two-death gap; 148 membership unverified |
| 2026-10-12 | `UA-KYI-KYIV-DARNYTSKY-2026-10-12-RESIDENTIAL-DRONE` | `UA-KYI-KYIV-DARNYTSKY-2026-10-12-RESIDENTIAL-DRONE-REV-002` | 1 → 2 | +1 | Potential two-death gap; 148 membership unverified |
| 2026-10-16 | `UA-KHA-KHARKIV-2026-10-16-MARKET-STRIKE` | `UA-KHA-KHARKIV-2026-10-16-MARKET-STRIKE-REV-002` | 3 → 2 | -1 | Legacy 148 membership unresolved |
| 2026-10-17 | `UA-DON-SLOVIANSK-2026-10-17-RESIDENTIAL-AIRSTRIKES` | `UA-DON-SLOVIANSK-2026-10-17-RESIDENTIAL-AIRSTRIKES-REV-001` | — → 1 | +1 | Interim toll not independently included |
| 2026-10-17 | `UA-DON-SLOVIANSK-2026-10-17-RESIDENTIAL-AIRSTRIKES` | `UA-DON-SLOVIANSK-2026-10-17-RESIDENTIAL-AIRSTRIKES-REV-002` | 1 → 6 | +5 | Interim toll not independently included |
| 2026-10-17 | `UA-KHE-KHERSON-2026-10-17-KORABELNY-DOUBLE-TAP` | `UA-KHE-KHERSON-2026-10-17-KORABELNY-DOUBLE-TAP-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-19 | `UA-KHA-NOVA-VODOLAHA-2026-10-19-CENTRAL-PARK-DRONE` | `UA-KHA-NOVA-VODOLAHA-2026-10-19-CENTRAL-PARK-DRONE-REV-001` | — → 3 | +3 | Initial toll not separately included |
| 2026-10-19 | `UA-KHA-NOVA-VODOLAHA-2026-10-19-CENTRAL-PARK-DRONE` | `UA-KHA-NOVA-VODOLAHA-2026-10-19-CENTRAL-PARK-DRONE-REV-002` | 3 → 6 | +3 | Preliminary six superseded; no separate increment |
| 2026-10-21 | `UA-CHE-UMAN-2026-10-21-PRIVATE-HOUSE-DRONE-STRIKE` | `UA-CHE-UMAN-2026-10-21-PRIVATE-HOUSE-DRONE-STRIKE-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-22 | `UA-KHA-LOZOVA-2026-10-22-CENTRAL-MARKET` | `UA-KHA-LOZOVA-2026-10-22-CENTRAL-MARKET-REV-002` | 2 → 3 | +1 | Legacy 148 membership unresolved |
| 2026-10-24 | `UA-KHA-LOZOVA-2026-10-24-WAREHOUSE-MISSILE` | `UA-KHA-LOZOVA-2026-10-24-WAREHOUSE-MISSILE-REV-001` | — → 1 | +1 | Legacy 148 membership unresolved |
| 2026-10-25 | `UA-DNE-DNIPROPETROVSK-2026-10-25-DTEK-DRIVER` | `UA-DNE-DNIPROPETROVSK-2026-10-25-DTEK-DRIVER-REV-001` | — → 1 | +1 | Distinct DTEK mine lorry strike; not evidenced in 148 or 421 |
| 2026-10-29 | `UA-KHA-IZIUM-2026-10-29-OTHER-ATTACK-59YO` | `UA-KHA-IZIUM-2026-10-29-OTHER-ATTACK-59YO-REV-001` | — → 1 | +1 | Oct. 29 extra death; inclusion after 173 unverified |
| 2026-10-29 | `UA-KHA-IZIUM-2026-10-29-PUBLIC-HEALTH-INSTITUTION` | `UA-KHA-IZIUM-2026-10-29-PUBLIC-HEALTH-INSTITUTION-REV-002` | 4 → 5 | +1 | Oct. 29 extra death; inclusion after 173 unverified |
| 2026-10-31 | `UA-DON-SLOVIANSK-2026-10-31-ATTACK` | `UA-DON-SLOVIANSK-2026-10-31-ATTACK-REV-001` | — → 1 | +1 | Nov. 2 baseline inclusion unverified |
| 2026-11-03 | `UA-DNE-DNIPRO-2026-11-03-MORNING-STRIKE` | `UA-DNE-DNIPRO-2026-11-03-MORNING-STRIKE-REV-002` | 1 → 2 | +1 | Second death not established in 421 subtotal |
| 2026-11-11 | `UA-KHA-KHARKIV-SALTIVSKY-2026-11-11-DRONE-STRIKE` | `UA-KHA-KHARKIV-SALTIVSKY-2026-11-11-DRONE-STRIKE-REV-001` | — → 1 | +1 | First death not included in 421; no separate increment |
| 2026-11-11 | `UA-ODE-CHORNOMORSK-2026-11-11-MARKET` | `UA-ODE-CHORNOMORSK-2026-11-11-MARKET-REV-002` | 1 → 3 | +2 | Later hospital deaths not established in 421 subtotal |
| 2026-11-11 | `UA-ODE-CHORNOMORSK-2026-11-11-MARKET` | `UA-ODE-CHORNOMORSK-2026-11-11-MARKET-REV-003` | 3 → 4 | +1 | Later hospital deaths not established in 421 subtotal |

## Next audit

Reconstruct the legacy 148 membership from the archived chronology and change log, beginning with the 123 baseline and the Oct. 25–28 increments. Resolve the Oct. 31 Sloviansk inclusion separately. Do not change public totals until the incident-level membership and overlap questions are closed.


## Stage 102 adjudication

Stage 102 reviewed six pre-Oct. 29 revisions: the Oct. 5 Kramatorsk death, Oct. 8 Ivano-Frankivsk drone-debris death, unallocated Oct. 8 Kyiv morning death, third death in the Oct. 8 Solomiansky shop strike, Oct. 9 Synelnykove-district death and Oct. 9 Zaporizhia guided-bomb death. None receives a new effective date. The Oct. 11 ≈80 snapshot explicitly includes only the first two Solomiansky shop deaths; the third death's later inclusion remains unverified. The Oct. 11 broad Kyiv citywide row may overlap incident-level reports and is not treated as an independent additional death. The Dnipropetrovsk row is matched to the separate Pokrovske child death, not Oct. 9 Synelnykove. The Oct. 9 Zaporizhia death is distinct from the Oct. 10 strike whose 20 deaths are in the snapshot. The other cases are not individually itemized, and later carried-forward aggregates do not establish membership. Six incident-revision reasons were clarified; counts and null effective dates remain unchanged. See `STAGE-102-CHECKPOINT.md`.


## Stage 103 adjudication and legacy closeout

Stage 103 completed the review of the final eight pre-Oct. 29 revision entries: Zaporizhia Oct. 10 (20→23, +3), Sloviansk Oct. 11 (+1), Kharkiv Kholodnohirsky Oct. 12 (+4), Kyiv Darnytsky Oct. 12 (two revisions, one incident, +2), Kherson Korabelny Oct. 17 (+1), Lozova central market Oct. 22 (+1) and the separate Lozova warehouse strike Oct. 24 (+1). All eight remain null because no surviving dashboard update or method snapshot establishes their inclusion date. The Oct. 11 Zaporizhia baseline includes the first 20, not a dated addition of the later three. The Oct. 26 +5 includes the first two Lozova market deaths, not the third; the warehouse is separate. The Kharkiv and Darnytsky cases remain potential inclusion gaps, not confirmed omissions. See `STAGE-103-CHECKPOINT.md`.

Stages 100, 102 and 103 now account for all 26 pre-Oct. 29 null revisions: 12 classified in Stage 100, six audited in Stage 102 and eight audited in Stage 103. The review is closed to the limit of the surviving evidence. Fourteen legacy revisions, net +19, still have no confirmed inclusion date; the other 12 are interim/superseded tolls, the unreflected Kharkiv market correction or separately classified cases. No date was inferred and no public subtotal was changed.

## Final inventory integrity after Stage 103

- Total null revisions: 33, net +90.
- Pre-Oct. 29 null revisions: 26, net +82.
- Post-Oct. 29 null revisions: 7, net +8.
- Incident ledger: 176 incidents, 430 sources, 452 final documented deaths, 231 revisions.
- Public provisional minimum: 421, unchanged.

The seven post-Oct. 29 revisions were reviewed and closed in Stage 104. Two are explicitly not included in the 421 subtotal (the first Saltivsky death and the second Dnipro death); five have no confirmed inclusion date in the carried-forward subtotal (the two additional Oct. 29 Izium deaths, Oct. 31 Sloviansk and two later Chornomorsk deaths). No further historical audit work is pending unless new contemporaneous evidence is recovered.


## Stage 104 — post-Oct. 29 and 421-baseline closeout

Stage 104 reviewed all seven post-Oct. 29 null revisions, net +8. The first Saltivsky death is not included in the 421 subtotal: the timestamped 283→284 update adds only the second death. The second Nov. 3 Dnipro death is also not included: the mapped sequence adds one Dnipro death, with the following +3 fully allocated to Komyshuvakha and Hotiv. The two additional Oct. 29 Izium deaths, Oct. 31 Sloviansk death and two later Chornomorsk hospital deaths have no confirmed inclusion date in the carried-forward subtotal. All seven remain null. See `STAGE-104-CHECKPOINT.md`.

## Final audit closeout

The historical reconciliation audit is complete to the limit of surviving evidence. All 33 null revisions have been reviewed: 26 pre-Oct. 29 entries, net +82, and seven later entries, net +8. Of the legacy entries, 12 are classified as interim/superseded tolls, a public-count correction not reflected in the subtotal, or separately categorized cases; 14 remain without a confirmed inclusion date, net +19. Of the seven later entries, two are established exclusions from 421 and five have unverified inclusion in a carried-forward aggregate. Null dates are retained where evidence does not establish a first public inclusion date. The arithmetic net +90 is not a correction to the public total.

The ledger remains 176 incidents, 430 sources, 452 final documented deaths and 231 revisions (198 dated, 33 null). The public provisional minimum remains 421. No public-facing files or figures were changed.
