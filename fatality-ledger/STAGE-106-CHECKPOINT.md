# Stage 106 checkpoint — post-Oct. 29 null revisions closed

Date: 2026-11-26

## Scope and result

This stage rechecks all seven post-Oct. 29 revision entries that remained null after Stage 104. The full historical bridge is now available: 148 + 19 + 25 + 229 = 421. The 174 baseline and all later increments from 192 to 421 are mapped in the historical checkpoint series. The post-Oct. 29 null revisions are now classified as established exclusions from the 421 public subtotal.

This does not mean the underlying deaths are unverified. All seven revisions remain in the incident ledger as documented local toll changes. Their null `ledger_effective_at` values now mean that the changes were not included in the public 421 subtotal.

## Historical baseline bridge

The 174 baseline is 148 carried forward through Oct. 28, plus 19 deaths in the Oct. 29 cohort, six deaths in the Oct. 30 update (one Kyiv death, one delayed Dnipro railway-station death and four in the Oct. 29 Izium public-health-institution strike), and one separate Izium guided-bomb death reported Nov. 2.

The 174→192 transition is the initial 18-death Komyshuvakha toll. The historical 421 is then reached through the fully mapped 192→421 sequence in Stages 44–52. The six late-reported deaths added at 230→236 on Nov. 5 are a separate group: two Sloviansk deaths from Oct. 30 attacks, Shostka, Nikopol district, Dnipro district and Orikhiv. They do not include the two additional Oct. 29 Izium deaths or the separate Oct. 31 Sloviansk death.

## Revision-by-revision dispositions

| Incident | Revision | Change | Disposition |
|---|---|---:|---|
| Izium, separate Oct. 29 attack on a 59-year-old woman | `UA-KHA-IZIUM-2026-10-29-OTHER-ATTACK-59YO-REV-001` | +1 | Excluded: not in 148, 19-death Oct. 29 cohort, six-death Oct. 30 update, Nov. 2 Izium addition or any mapped 192→421 increment |
| Izium public-health institution, fifth employee death | `UA-KHA-IZIUM-2026-10-29-PUBLIC-HEALTH-INSTITUTION-REV-002` | +1 | Excluded: Oct. 30 public increment explicitly includes four, not five; no later mapped increment adds the fifth |
| Sloviansk, Oct. 31 attack | `UA-DON-SLOVIANSK-2026-10-31-ATTACK-REV-001` | +1 | Excluded: not in reconstructed 174 baseline, 230→236 late-report group or any other mapped increment |
| Dnipro, Nov. 3 morning strike, second death | `UA-DNE-DNIPRO-2026-11-03-MORNING-STRIKE-REV-002` | +1 | Excluded: 207→208 includes only the first death; 208→211 is fully allocated to Komyshuvakha (+2) and Hotiv (+1) |
| Kharkiv Saltivsky district, first death | `UA-KHA-KHARKIV-SALTIVSKY-2026-11-11-DRONE-STRIKE-REV-001` | +1 | Excluded: postdates the 283 baseline; 283→284 adds only the second death |
| Chornomorsk market, two later hospital deaths | `UA-ODE-CHORNOMORSK-2026-11-11-MARKET-REV-002` | +2 | Excluded: 282→283 counts the initial death; the later 283→421 increments contain no Chornomorsk addition |
| Chornomorsk market, fourth and final death | `UA-ODE-CHORNOMORSK-2026-11-11-MARKET-REV-003` | +1 | Excluded: same complete 283→421 mapping; no later Chornomorsk addition |

The 192→421 sequence is mapped in Stages 44–52. Its increments sum to 229: 192→221 (+29), 221→254 (+33), 254→282 (+28), 282→333 (+51), 333→350 (+17), 350→363 (+13), 363→372 (+9), 372→391 (+19), and 391→421 (+30).

For Chornomorsk, the independent method-to-ledger comparison also identifies the three later hospital deaths as part of the +5 difference between 234 raw incident-ledger additions after 192 and 229 public additions: Chornomorsk (+3), Dnipro (+1) and Saltivsky (+1). The Chornomorsk initial death remains included at 282→283.

## Resulting null inventory

- All seven post-Oct. 29 null revisions are now established exclusions from the 421 subtotal.
- The 26 pre-Oct. 29 null revisions remain as adjudicated in Stage 103: 14 still lack a confirmed inclusion date (net +19); the other 12 are classified as interim/superseded tolls, the unreflected Kharkiv market correction or other separately adjudicated cases.
- Total null revision fields remain 33 because exclusions are still represented by null effective dates.
- There are now 14 unresolved historical inclusion questions, all in the pre-Oct. 29 group. No later inclusion question remains open.

## Change control

- Updated explanatory reason strings for six revisions: four newly classified exclusions (the two Izium revisions and two Chornomorsk revisions) and two previously established exclusions (the second Dnipro death and first Saltivsky death). Stage 105 had already updated the Oct. 31 Sloviansk reason.
- No incident final death count, revision value, incident count or source count changed.
- No `ledger_effective_at` value was filled.
- Public minimum remains 427; raw incident-ledger sum remains 458.
- No public chronology, dashboard or methodology figure changed.
