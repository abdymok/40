# Method-page to incident-ledger reconciliation

**Working status:** Stage 53, updated Nov. 26, 2026  
**Current ledger sum:** 449  
**Published method-page minimum:** 421  
**Raw difference:** +28 in the pilot incident dataset

> **Stage 53 amendment:** The current dataset contains 175 incidents, 423 source records and 449 final documented deaths. The current public chronology and method page both stand at 421 through Nov. 26. The pre-Oct. 29 incident-date inventory sums to 169 (21 above the legacy 148); the Oct. 29 cohort sums to 27 (two above the historical 25); and post-192 incident-date additions sum to 234 (five above the method's 229). Raw arithmetic: +21 +2 +5 = +28. The historical 148 includes three Chabany deaths excluded from the current ledger and appears to retain three deaths in the Oct. 16 Kharkiv market incident, while the current ledger keeps the later official final count of two. Adjusting only for those two known scope differences gives a provisional like-for-like pre-Oct. 29 comparison of 173 versus 148 (+25), and a provisional like-for-like overall comparison of 453 versus 421 (+32). The Uman death's inclusion in 148 remains unestablished and could shift the comparison by one. These are comparison adjustments, not proposed public totals. The ledger has 175 revision entries with confirmed ledger_effective_at dates and 53 still null. The dated historical sequence now reconciles the public 421 as 148 + 19 (Oct. 29) + 25 (Oct. 30–Nov. 2) + 229 (Nov. 3–26).

> **Null-revision classification:** The 53 null `ledger_effective_at` revisions are now inventoried and classified. Forty-six pre-Oct. 29 legacy revisions carry a net +139 count change, including one −1 correction. Seven later revisions carry a net +8 and concern two additional Oct. 29 Izium deaths, the Oct. 31 Sloviansk death, the second Nov. 3 Dnipro death, the first Saltivsky death and three later Chornomorsk hospital deaths. Their inclusion or overlap remains unresolved. The 53 entries are not 147 additional deaths and do not change the public 421 subtotal. See `UNRESOLVED-EFFECTIVE-DATES-2026-11-26.md` and `STAGE-53-CHECKPOINT.md`.

> **Stage 54 amendment:** The Oct. 25–27 transitions are now mapped to existing incident records: 123→132 (+9), 132→137 (+5), 137→138 (+1), 138→141 (+3), and 141→146 (+5 across two updates). The Oct. 22 transition from 121→123 (+2) remains unidentified: the contemporaneous commit changes the displayed number but supplies no incident-level allocation. No ledger effective dates or public figures were changed. See `STAGE-54-CHECKPOINT.md`.

> **Stage 58 expanded finding:** The Oct. 20 commit chain now reconciles the apparent 100/102/103 conflict. The sequence is 99→102 (+3 Chabany, temporarily included as attributed deaths); 102→103 (+1 Holosiivsky); 103→100 (−3 Chabany, explicitly excluded from the official/media dashboard subtotal); 100→103 (+3 Kramatorsk heating workers); and 103→105 (+2 Sviatoshynsky). The relevant commits are `f40e650`, `25abf34`, `43be9fb` and `84c0c69`, in that parent chain. The Oct. 20 102 snapshot's method note includes Chabany but not Holosiivsky; the 103 snapshot after Holosiivsky still has a stale 102 method paragraph. The 25ab snapshot displays 100 while its explanatory note still describes 103 including Chabany, then explicitly labels Chabany as outside the subtotal. The 43be and 84c0 updates then raise the official/media subtotal to 103 and 105 respectively. This resolves the intermediate count sequence without changing any public figure now. See STAGE-58-CHECKPOINT.md.

> **Stage 58 amendment:** The earlier subtotal chain is now verified through the Oct. 19 Kyiv death: 92→95 (+3) on Oct. 15 for the three Kirovohrad-region deaths (commit `12ec18d5f902d58a59de878b5b8c0ddeff86d3ef`); 95→98 (+3) on Oct. 16 for the three Kharkiv deaths (commit `c1f0bb19c1f3aaea9ec4c793c569b72c18ed7a74`); and 98→99 (+1) for the 21-year-old woman killed in the Oct. 19 Kyiv ballistic attack, reflected in the Oct. 19–20 update history and the 99 snapshot. The 95→98 and 98→99 changes are explicitly described in the archived update history. The subsequent Oct. 20 snapshots show inconsistent intermediate baselines (including 100, 102 and 103) while the Kramatorsk and Holosiivsky deaths are added; those transitions require a separate commit-parent sequence audit and are not yet allocated here. No incident dates, effective dates or public figures changed. See STAGE-58-CHECKPOINT.md.

> **Stage 57 correction to Stage 56:** Directly fetching the HTML at the Oct. 21 09:16 snapshot commit `679cd4c4e1541842a3794c72b7d583e5deea1f1a` confirms that both the dashboard (≈105) and its method paragraph already included the two Sviatoshynsky deaths. The later `3c205e7` commit changed only the dashboard from ≈105 to ≈107; it left that method paragraph unchanged. The intermediate +2 is therefore a likely duplicate step, not a new incident addition. The subsequent 107→116 update is +9 even though its revised method paragraph adds both the nine Sloviansk deaths and two Korotych deaths (+11). These two anomalies offset arithmetically: 105→116 is +11, exactly the combined Sloviansk and Korotych toll, while the intermediate 107 appears to double-count the two Sviatoshynsky deaths. This strongly suggests the 116 endpoint is consistent with the 105 baseline, but the intermediate transition labels are not. Do not subtract from the public total or alter ledger effective dates without a full membership check. See STAGE-57-CHECKPOINT.md.

> **Stage 56 amendment:** The Oct. 21 105→107 (+2) transition is attributed by the dashboard commit to the Sviatoshynsky deaths, but the contemporaneous method paragraph is not independent proof of baseline membership: it continued to display “approximately 105” while already naming those two deaths. The following commit changed only the dashboard value from 105 to 107, leaving that method paragraph untouched. Treat the paragraph as stale/internally inconsistent at that point, not as proof that the two deaths were already in 105. The Oct. 21 107→116 (+9) change history names both the nine-death Sloviansk final toll and two Korotych deaths, but does not allocate the nine increment between them. The precise amount of Sloviansk already present in 107 remains unresolved. See `STAGE-56-CHECKPOINT.md`. No ledger dates, incident counts or public totals changed.

> **Stage 55 amendment:** The archived Oct. 21–22 commits establish the displayed sequence 105→107 (+2, attributed by the contemporaneous dashboard update to the Sviatoshynsky deaths), 107→116 (+9, with the change history naming Sloviansk and Korotych but not allocating the increment). The method paragraph at the 107 snapshot still displayed 105 while already naming the Sviatoshynsky deaths, so it is stale/internally inconsistent and cannot independently prove baseline membership. See Stage 56. The 121→123 increment remains unidentified. No effective dates or public figures were changed. See STAGE-55-CHECKPOINT.md.

## What is established

The method page's cumulative sequence starts from an opening subtotal of approximately 192. It explicitly says this subtotal already included 18 deaths from the Nov. 2 Komyshuvakha strike. Subsequent increases in that incident were therefore increments from 18, not a fresh addition of the full 72.

The Nova Vodolaha park strike's revision sequence is now reconciled: the initial three deaths rose to a preliminary six, the regional administration corrected the toll to five on Oct. 19, and a 12-year-old boy died in hospital on Oct. 26, returning the final toll to six. The 141 subtotal carried five; the Oct. 27 update added the sixth. The structured revision chain now records all four steps. The October OHCHR monitoring report independently confirms six civilian deaths. Ukraine Evidence Hub case-file v3 carries a conflicting seven-death figure in its headline and narrative; it is retained as a source conflict but not adopted over the contemporaneous regional updates and OHCHR count.

The method page also identifies six late-reported deaths from Oct. 30 attacks that were added on Nov. 5, raising the running minimum from approximately 230 to 236:
- two in Sloviansk;
- one in Shostka;
- one in Nikopol district;
- one in Dnipro district;
- one in Orikhiv.

Those six now have incident records.

The method's Nov. 4–6 source audit identified eight further deaths:
- two in Yasnohirka;
- two in Serhiivka;
- one in Putyvl community;
- one in Antonivka;
- one in Kramatorsk;
- one in Sarny district.

Those eight now have incident records and are already included in the current method-page total of 421.

## Scope mismatches in the pre-Oct. 29 baseline

Five historical records that were absent from the structured ledger have now been added:

1. **Korotych, Oct. 21 — two deaths.** The Oct. 22 methodology note included both victims.
2. **Kherson minibus, Oct. 25 — one death.** The Oct. 26 historical update included one death in Kherson. The 67-year-old passenger who died in hospital is now represented.
3. **Yasnohirka, Oct. 26 — one death.** The Oct. 26 historical update included one death in Yasnohirka.
4. **Chernihiv enterprise, Oct. 23 — one death.** The Oct. 25 update's four-death Oct. 23 batch included the Chernihiv fatality.
5. **Sloviansk, Oct. 23 — one death.** The same Oct. 23 batch included the 62-year-old woman who died in hospital on Oct. 24.

**Uman, Oct. 21 — one death, historical inclusion unknown.** The ledger now records 86-year-old Tamara Yasynska, who died on Oct. 26 from injuries sustained in the Oct. 21 attack. The historical Oct. 22–28 change log does not identify whether this death entered the 148 subtotal. Its `ledger_effective_at` remains null. Do not assume it was either included or omitted.

Two count-scope differences are confirmed:
- **Chabany, Oct. 20 — three deaths.** The Oct. 28 historical chronology snapshot explicitly says these three deaths were included in the dashboard subtotal. The current structured ledger has no Chabany record, consistent with the later working exclusion. They remain excluded and have not been reintroduced.
- **Kharkiv market, Oct. 16 — three versus two.** The Oct. 22 method note listed three deaths in Kharkiv on Oct. 16. The current ledger retains the later official final count of two. No corresponding downward adjustment was found in the Oct. 28 change log, so the historical subtotal is provisionally treated as still carrying three.

After adding Korotych, Kherson, Yasnohirka, Chernihiv and Sloviansk, plus the Uman incident whose inclusion date is unresolved, the raw pre-Oct. 29 comparison is 169 current ledger deaths versus 148 historically published, a net +21. For a like-for-like comparison only, add the three Chabany deaths that remain in the historical subtotal and the one Kharkiv market death that the current ledger has corrected downward: 169 + 3 + 1 = 173 versus 148, or +25. This is provisional because the Uman death may or may not already be in 148. These comparison adjustments are not proposed ledger additions. The ledger stands at 449 overall and the Chabany exclusion remains in force unless the user changes that instruction.

The same scope adjustments carry forward into the published 421 total. The raw current-ledger difference is +28 (449 versus 421). A provisional like-for-like comparison is 453 versus 421, or +32. Do not interpret 453 as an approved count. The current ledger remains 449.


## Historical subtotal sequence now mapped

The old update history can now be mapped more completely to individual records:

| Historical update | Increment | Current incident mapping |
|---|---:|---|
| Oct. 25, 123→132 | +9 | Synelnykove 4, Kharkiv Novobavarsky 1, Dnipro 1, Kramatorsk 1, Chernihiv 1, Sloviansk 1 |
| Oct. 26, 132→137 | +5 | Marhanets 1, Lozova, Konotop 1, Yarova 1. The precise split within the Lozova revision chain remains under review; the third Lozova death has no confirmed public inclusion date. |
| Oct. 26, 137→138 | +1 | Kramatorsk 1 |
| Oct. 26, 138→141 | +3 | Pavlohrad 1, Kherson 1, Yasnohirka 1 |
| Oct. 27, 141→146 | +5 | Kyiv 1, Nova Vodolaha 1, Donetsk region 3 |
| Oct. 28, 146→148 | +2 | Kharkiv 1, Novodonetske 1 |

The Oct. 23 batch is now mapped to four localities. The Dnipro and Kramatorsk records were already present. Chernihiv and Sloviansk were added in Stage 39. The Nova Vodolaha revision chain now shows five deaths in the 141 subtotal and the sixth death entering on Oct. 27.

## Known method/record differences

| Incident | Incident ledger | Method-page increment | Difference to explain |
|---|---:|---:|---:|
| Chornomorsk, Nov. 11 | 4 | 1 | +3 |
| Dnipro, Nov. 3 | 2 | 1 | +1 |
| Komyshuvakha, Nov. 2 onward | 72 final | 18 in opening subtotal, then staged increments | Must allocate the 18 baseline deaths once, not add them twice |
| Dymer, Nov. 22 onward | 12 final | 2 already in the 379 subtotal, then +5, +4, +1 | Must allocate the initial two deaths to the earlier subtotal |
| Saltivsky district, Nov. 11 | 2 final | +1 in the cited increment | One death may already have been included in the preceding subtotal |
| Nova Vodolaha, Oct. 19 | 6 final | 5 in the 141 subtotal, then +1 on Oct. 27 | Revision history now records 3 → preliminary 6 → corrected 5 → final 6; no remaining count difference after the Oct. 27 update |
| Izium, Oct. 29 | 5 at public-health institution, plus a separate one-death attack | Dashboard first showed 4 for the institution strike; a separate woman was also killed | Keep the two incidents separate and preserve 4 → 5 |
| Zaporizhia, Oct. 10 | 23 final local toll | Early project snapshot showed 20 | Confirm which figure was included in the 192 baseline |
| Kyiv, Oct. 13 | 2 final local toll | Early project snapshot showed 1 | Confirm whether the second death was included in the 192 baseline |
| Solomiansky district, Oct. 8 | 3 in shop strike plus 1 earlier citywide death | Early project snapshot reported 2 at the shop and 1 elsewhere | Confirm whether the later third shop death was included in the 192 baseline |
| Kharkiv, Oct. 16 | 2 final local deaths | Early report said 3 | Ensure the superseded preliminary third death was not retained |

These entries are not yet a complete reconciliation. The table distinguishes known count differences from unresolved baseline membership; it does not assume that every difference is an error in the method.

## Reconciliation arithmetic and open allocation

The historical sequence is now explicit:
- Oct. 28 legacy subtotal: 148.
- Oct. 29 additions: 25, producing the Oct. 30 snapshot of 173.
- Nov. 2 Komyshuvakha opening count: 18, plus the Nov. 2 Izium death, producing the 192 opening subtotal used by the method page.
- The Stage 20 snapshot of the current incident inventory through Oct. 28 was 161. The Stage 24–29 refresh raised this to 162, Stage 34 to 164, Stage 37 to 166, Stage 39 to 168 and Stage 41 to 169 after adding the missing Korotych, Kherson, Yasnohirka, Chernihiv, Sloviansk and Uman incidents. The current raw difference is 21 above the legacy 148; after the two known scope adjustments, the provisional like-for-like difference is 25, subject to the unresolved Uman inclusion date. The exact membership of the remaining difference is still being reconstructed; incident date alone is insufficient because several deaths were reported or revised later.
- The Stage 20 snapshot's Oct. 29 total of 27 is now reproduced by the current dataset, but its composition is corrected. The current incident-date sum is 27: Dnipro railway station (15), Kremenchuk (3), Chernihiv (2), Kyiv's late-evening ballistic attack (1), the Izium public-health institution (5) and a separate Izium attack (1). The historical 173 transition totals 25: 14 initially reported at Dnipro, the subsequent Dnipro hospital death (+1), Kremenchuk (3), Chernihiv (2), Kyiv (1) and four in the Izium airstrike. The two-death difference is the institution's fifth employee death plus the separate 59-year-old woman killed in Izium, neither of which appears in the 173 snapshot breakdown. The Kyiv death was missing from the structured ledger and has now been added.
- The current post-192 additions sum to 234, five above the method's 229. The five-death difference is now accounted for by three known incident-level differences: Chornomorsk (four final deaths against the method's one-death increment, +3); Dnipro on Nov. 3 (two final deaths against the method's one-death increment, +1); and Saltivsky district on Nov. 11 (two final deaths, but the first death was already in the preceding subtotal, so the method correctly adds only one; counting both as new produces +1). These explain the +5 arithmetic, subject to explicit effective-date fields still being completed.

The earlier working decompositions (+13 +2 +3 = +18, then +14 +1 +3 = +18, Stage 29 +20, Stage 31 +21, Stage 34 +23) are superseded by Stage 37. The current raw arithmetic is **+21 +2 +5 = +28**: 169 versus 148 through Oct. 28; 27 versus 25 for Oct. 29; and 234 versus 229 in post-192 additions. On a provisional like-for-like basis after the Chabany and Kharkiv market adjustments, the arithmetic is **+25 +2 +5 = +32**. The Uman death's inclusion in 148 remains unknown and may shift the pre-Oct. 29 comparison by one. The pre-Oct. 29 difference still requires source-by-source allocation of revisions and historical inclusion dates. The +2 Oct. 29 difference is the fifth death in the public-health institution strike plus the separately reported 59-year-old woman killed in Izium; the historical 173 snapshot listed four Izium airstrike deaths. The Kyiv fatality is now included and is part of the historical 25. Do not infer `ledger_effective_at` from incident date or report date.

## Required next work

1. Reconstruct membership of the legacy 148 and 192 snapshots from the original commits and change-log entries, including source publication date and the date the project actually counted each death.
2. Continue populating `ledger_effective_at` only where the old dashboard history confirms inclusion. One hundred seventy-five revision entries now have confirmed ledger_effective_at dates; 53 remain null. Stage 53 classified all 53 null revisions into a 46-entry pre-Oct. 29 legacy group (net +139) and seven later revisions (net +8). These are not additive public-total changes. Do not infer dates from incident date alone.
3. Continue mapping historical subtotal increments to individual records. The post-192 +5 is now accounted for by Chornomorsk (+3), Dnipro Nov. 3 (+1) and Saltivsky (+1).
4. Keep the DTEK driver and Kramatorsk Oct. 9 OHCHR lead unresolved until source/duplicate questions are settled.
5. Do not force the ledger to 421. The current total is a calculated pilot sum and may change if source-level deduplication or additional incident verification changes any record.

No public totals are to be changed until the incident dataset and method arithmetic reconcile or the discrepancy is explicitly explained and approved.


## Stage 43 — Oct. 29 cohort and the 192 opening baseline

The original repository snapshots now establish the historical sequence more precisely:

| Snapshot / update | Historical minimum | Evidence |
|---|---:|---|
| Oct. 28 | 148 | Dashboard snapshot in commit fb0d8ae4d5c0c27af974ce7a20e1672b28454c05 |
| Oct. 29, 22:10 | 167 | Dashboard snapshot in commit e42ba88524f1ca9a23dffd13ae26e8875d1d257d |
| Oct. 30 | 173 | The change history records the late Kyiv death, the delayed Dnipro railway-station death and four deaths in Izium |
| Nov. 2, before Komyshuvakha | 174 | The method history records one further death in the Nov. 2 Izium attack |
| Nov. 2, after Komyshuvakha update | 192 | The regional administration's initial Komyshuvakha count of 18 is added to 174 |

### Oct. 29 incident cohort: 25 historical deaths

The historical 148→173 transition is now mapped as follows:

| Incident | Deaths included in historical 173 | Effective date(s) |
|---|---:|---|
| Dnipro railway station | 15 | 13 and 14 on Oct. 29; 15th death on Oct. 30 |
| Chernihiv central drone strike | 2 | Oct. 29 |
| Kremenchuk apartment-building strike | 3 | Two initially, then three on Oct. 29 |
| Kyiv late-evening ballistic attack | 1 | Oct. 30 |
| Izium public-health institution strike | 4 | Oct. 30 |
| **Total** | **25** | |

This matches the historical 148→167 movement by Oct. 29 (+19), followed by six deaths in the Oct. 30 167→173 update (+1 Kyiv, +1 delayed Dnipro hospital death and +4 Izium). The chronology's Oct. 30 entry explicitly records the four-death Izium increment. The later official report of five employees killed is preserved as a source-supported final count, but the fifth employee is not in the historical 173 snapshot.

The current incident-date inventory for Oct. 29 is 27, not 25. The two additional deaths are:
- the fifth employee in the Izium public-health institution strike, reported after the dashboard's four-death update;
- a 59-year-old woman killed in a separate Izium attack, first specifically identified in the Oct. 31 reporting.

The separate Izium death is not to be merged into the public-health institution incident. Neither of these two additional deaths is included in the historical 173 breakdown. Their inclusion in a later public subtotal is not yet established, so their ledger_effective_at fields remain null.

### Revision-history changes made

The incident dataset now records the historical progression rather than only the final toll:
- Dnipro railway station: 13 → 14 on Oct. 29 → 15 on Oct. 30.
- Kremenchuk: 2 → 3 on Oct. 29.
- Chernihiv: two deaths entered on Oct. 29.
- Kyiv ballistic attack: one death entered on Oct. 30.
- Izium public-health institution: four deaths entered on Oct. 30; the fifth death remains a later final-count revision with no proven dashboard inclusion date.

The dataset now has 157 revision entries with non-null ledger_effective_at and 69 entries still null. The total remains 173 incident records, 419 source records and 446 final documented deaths. No final incident count was changed by this stage.

### 192 baseline interpretation

The original Nov. 2 dashboard snapshot shows 192 after an increase from approximately 174 to 192 for the initial 18 deaths reported in Komyshuvakha. The 174 baseline therefore precedes that +18. The method page also identifies one further Nov. 2 death in Izium before the Komyshuvakha increment. The 192 snapshot arithmetic is consequently 173 + 1 + 18 = 192.

The additional Nov. 2 Izium death is matched to UA-KHA-IZIUM-2026-11-02-GUIDED-BOMBS and its ledger_effective_at is set to Nov. 2. The Komyshuvakha revision from one preliminary death to 18 is also assigned to Nov. 2; the preliminary one is not counted as a separate increment. The 18 Komyshuvakha deaths are a baseline allocation, not an additional incident-date subtotal to be added again later.

No public chronology, methodology page, dashboard figure or live running total was changed.


## Stage 44 — Nov. 2–4 running subtotal mapped

The 192→221 progression is now assigned to incident records and dated revisions:

| Historical snapshot | Running minimum | Increment | Mapped changes |
|---|---:|---:|---|
| Nov. 2 | 192 | — | 174 baseline + 18 Komyshuvakha deaths |
| Nov. 3, 02:56 | 200 | +8 | Komyshuvakha revised from 18 to 26 |
| Nov. 3, 06:19 | 207 | +7 | Komyshuvakha 26→29 (+3); four deaths in Donetsk Oblast from Nov. 2 (+4) |
| Nov. 3, 13:14 | 211 | +4 | Komyshuvakha 29→31 (+2); one death in Dnipro (+1); Hotiv child (+1) |
| Nov. 3, 13:57 | 212 | +1 | One woman killed in Yasnohirka |
| Nov. 4, 11:38 | 218 | +6 | Komyshuvakha 31→37 |
| Nov. 4, 13:50 | 221 | +3 | Komyshuvakha 37→40 |

The four Nov. 2 Donetsk-region deaths are separately represented in Bilenke, Druzhkivka, Kramatorsk and Sloviansk. They are assigned to the Nov. 3 update, not to the Nov. 2 192 baseline. The Nov. 3 Dnipro incident has two final deaths, but the historical dashboard description identifies only one; the second death remains without a confirmed inclusion date and is not included in the 192→221 mapping.

The Komyshuvakha source and revision history now includes the official 26-death update (ZOVA post 68774). Its sequence is recorded as 1→18, 18→24, 24→26, 26→29, 29→31, 31→33, 33→37, 37→40 and later updates. The 24-death report is retained as an interim source update; the Nov. 3 dashboard changed from the 18-death baseline to the 26-death figure, a net increase of eight. The Nov. 3 and Nov. 4 dashboard snapshots support the subsequent 29, 31, 37 and 40 counts.

The Nov. 4 page briefly displayed a stale card value of 212 while its text and update history stated 218. The next repository correction commit restored the card to 218. The later 221 snapshot is consistent.

The current incident ledger remains at 173 records, 420 source records and 446 final deaths. It now has 57 revisions with confirmed effective dates and 167 still null. The validator passed after a revision-chain continuity correction. No public totals were changed in this audit.


## Stage 45 — Nov. 4–6 additions mapped to the 254 baseline

The next historical sequence is now reconstructed:

| Historical subtotal | Increment | Incident mapping |
|---|---:|---|
| 221→222, Nov. 4 | +1 | Kramatorsk FPV-drone death from the Nov. 3 attack |
| 222→225, Nov. 5 | +3 | Bilenke (1) and Vilniansk (2), attacks on Nov. 4 |
| 225→229, Nov. 5 | +4 | Komyshuvakha 40→42 (+2); two police officers wounded in the separate Nov. 1 vehicle attack died in hospital (+2) |
| 229→230, Nov. 5 | +1 | Komyshuvakha 42→43 |
| 230→236, Nov. 5 | +6 | Late-reported Oct. 30 deaths: Sloviansk (2), Shostka (1), Nikopol district (1), Dnipro district (1), Orikhiv (1) |
| 236→246, Nov. 6 | +10 | Komyshuvakha 43→50→53; use the higher 53 count, not 50+53 |
| 246→254, by Nov. 7 | +8 | Nov. 4–6 source audit: Serhiivka (2), Yasnohirka (2), Putyvl community (1), Antonivka (1), Kramatorsk (1), Sarny district (1) |

The 246→254 allocation is based on the existing Nov. 4–6 source audit, which identifies the eight incidents and states they were included in the 254 subtotal used for the Nov. 7 additions. The records are assigned an effective date of Nov. 6, the end of that audit window; no intraday timestamp is asserted.

The six late-reported Oct. 30 deaths were not previously in the running minimum. The Nikopol-district and Dnipro-district deaths are distinct from the nine-death Dnipro month-to-date subtotal and are not added twice. The two police officers are a separate Nov. 1 incident, not part of the 72 deaths from the Nov. 2 Komyshuvakha humanitarian-hub strike.

The relevant incident revisions now carry effective dates through Nov. 6. The ledger has 173 incidents, 420 source records and 446 final deaths. Of 224 revision entries, 72 have non-null effective dates and 152 remain null. No final incident counts changed.


## Stage 46 — Nov. 7–11 additions mapped to the 282 baseline

The running subtotal from 254 to 282 is now allocated:

| Historical subtotal | Increment | Incident mapping |
|---|---:|---|
| 254→256, Nov. 7 | +2 | Brovary district delayed hospital death (1); Lypova Dolyna (1) |
| 256→261, Nov. 8 | +5 | Kramatorsk (3), Druzhkivka (1), Bilenke (1) |
| 261→262, Nov. 8 | +1 | Odesa infrastructure attack (1) |
| 262→263, Nov. 8 | +1 | Bezruky, Derhachi community (1) |
| 263→265, Nov. 8 | +2 | Komyshuvakha 53→55 |
| 265→267, Nov. 8 | +2 | Dnipro suburb (1), Nikopol district (1) |
| 267→270, Nov. 9 | +3 | Odesa food warehouse (3) |
| 270→273, Nov. 10 | +3 | Kramatorsk (2), Sloviansk (1), Nov. 9 attacks |
| 273→274, Nov. 10 | +1 | Vyshhorod district (1) |
| 274→276, Nov. 10 | +2 | Ladyzhyn civilian enterprise (2) |
| 276→278, Nov. 11 | +2 | Kramatorsk (1), Sloviansk (1), Nov. 10 attacks |
| 278→282, Nov. 11 | +4 | Dnipro (3), Marhanets community (1), Nov. 10 attacks |

The Nov. 8 Donetsk-region group is separated from the four deaths reported on Nov. 3 for Nov. 2 attacks. The Brovary death is dated to the Nov. 6 incident but enters the subtotal after the victim dies in hospital on Nov. 7. The Lypova Dolyna death is assigned to the Nov. 7 update. The Komyshuvakha 53→55 revision is effective Nov. 8, when the regional administration's confirmation is reflected in the 263→265 subtotal.

The current ledger remains 173 incidents, 420 source records and 446 final deaths. It now has 90 revision entries with confirmed effective dates and 134 still null. No final incident counts changed.


## Stage 47 — Nov. 11–16 additions mapped to the 333 baseline

The running subtotal from 282 to 333 is now mapped:

| Historical subtotal | Increment | Incident mapping |
|---|---:|---|
| 282→283, Nov. 11 | +1 | Chornomorsk market strike, initial death |
| 283→284, Nov. 11 | +1 | Second Saltivsky-district death; the first was already in the preceding subtotal |
| 284→287, Nov. 11 | +3 | Yahotyn initial strike (1) and repeat strike on rescuers (2) |
| 287→288, Nov. 12 | +1 | Kyiv, Solomiansky district |
| 288→292, Nov. 12 | +4 | Kramatorsk citywide attacks |
| 292→297, Nov. 13 | +5 | Odesa (2), Zaporizhia private-sector strike (1), passenger-bus victim who died in hospital (1), Kosmichny industrial facility (1) |
| 297→301, Nov. 14 | +4 | Zolota Balka (2), Yasna Polyana (1), Cobra rescue-service worker (1) |
| 301→302, Nov. 14 | +1 | Pavlohrad missile strike |
| 302→305, Nov. 15 | +3 | Mena (2), Borova (1), added in the subsequent source review |
| 305→316, Nov. 16 | +11 | Bilenke (1), Dnipro morning road strike (1), Khortytsky district (1), Sadove (1), Druzhkivka (3), Lvivka (1), Chernihiv (2), Balakliia (1) |
| 316→333, Nov. 16 | +17 | Komyshuvakha 55→72 |

The Chornomorsk incident's initial death is in the historical subtotal. Three later hospital deaths remain in the final four-death incident record but have no proven inclusion in the 418 method total, so those later revisions remain null. The Saltivsky incident has two final deaths; the first is already represented in the subtotal preceding the second-death update, so the 283→284 increment is one, not two.

The Chernihiv incident record now separates the two deaths at the scene, included on Nov. 16, from the third man who died in hospital on Nov. 17. The third death is assigned to Nov. 17, not the 316 subtotal. The Nov. 16 Donetsk deaths later identified in Kramatorsk, Sloviansk, Yasnohirka and Shabelkivka are not added to the 316 baseline here; their later source updates will be mapped separately.

The ledger remains 173 incidents, 420 source records and 446 final deaths. It now has 113 revision entries with confirmed effective dates and 112 still null. No final incident counts changed.


## Stage 48 — Nov. 17–18 reconciliation mapped to 350

The post-333 sequence is now allocated:

| Historical subtotal | Increment | Incident mapping |
|---|---:|---|
| 333→334, Nov. 17 | +1 | First death in the Nov. 17 combined Zaporizhia industrial-facility attack |
| 334→336, Nov. 17 | +2 | Nov. 16 FPV deaths in Kushuhum (1) and Zaporizhia's Kosmichny district (1) |
| 336→337, Nov. 17 | +1 | Third Chernihiv victim died in hospital after the Nov. 16 attack |
| 337→338, Nov. 17 | +1 | Second death in the separate Nov. 17 Zaporizhia industrial-facility attack; the first was already included |
| 338→340, Nov. 17 | +2 | Kyiv, Obolonsky district, non-residential-building strike |
| 340→341, Nov. 17 | +1 | Vinnytsia vehicle-parking-area strike |
| 341→345, Nov. 17 | +4 | Mykolaiv port/industrial strike (2), Kramatorsk (1), Svitlovodsk community (1) |
| 345→350, Nov. 18 | +5 | Dnipro citywide update's additional death (1), Kherson water-utility operator (1), doctor Yuriy Zimin's delayed hospital death (1), Chervona Khvylia (2) |

The 333→334 step is the first death reported in the Nov. 17 Zaporizhia industrial-facility attack. Its second death is a separate 337→338 revision. The two Nov. 16 Zaporizhia FPV deaths then account for 334→336. This resolves the otherwise unexplained one-death gap between the 333 and 336 snapshots.

The Chernihiv incident is now split into two deaths at the scene on Nov. 16 and a third death in hospital on Nov. 17. The Nov. 18 Dnipro addition is separate from the morning road-strike death already included on Nov. 16. Doctor Zimin's incident date remains Oct. 6, but the fatal outcome was reported and entered in the running subtotal on Nov. 18; it was not part of the Oct. 28 baseline.

The four Nov. 16 Donetsk deaths later identified in Sloviansk (2), Yasnohirka (1) and Shabelkivka (1) are assigned to Nov. 18 and will be reconciled against the next subtotal. They are not part of the 345→350 five-death group.

The ledger remains 173 incidents, 420 source records and 446 final deaths. It now has 129 revision entries with confirmed effective dates and 96 still null. No final incident counts changed.


## Stage 49 — Nov. 18–19 additions mapped to 363

The next running-subtotal sequence is now allocated:

| Historical subtotal | Increment | Incident mapping |
|---|---:|---|
| 350→353, Nov. 18 | +3 | Initial reported deaths in the central Odesa strikes |
| 353→357, Nov. 18 | +4 | Donetsk region: Sloviansk (2), Yasnohirka (1), Shabelkivka (1) |
| 357→358, Nov. 18 | +1 | Fourth death in the central Odesa strikes |
| 358→359, Nov. 18 | +1 | Ploske, Kharkiv region |
| 359→360, Nov. 18 | +1 | Woman killed in a separate FPV-drone attack in Kushuhum |
| 360→361, Nov. 19 | +1 | Horenychi, Bucha district |
| 361→362, Nov. 19 | +1 | Kyiv, Podilsky district |
| 362→363, Nov. 19 | +1 | Unallocated Chernihiv-region fatality in the overnight energy-attack roundup |

The Odesa incident now records three deaths in the initial update and the fourth in a later revision. The four Donetsk deaths are distinct from the earlier Sloviansk and Yasnohirka incidents. The Nov. 18 Kushuhum woman is distinct from the 70-year-old man killed there on Nov. 16.

A Nov. 19 National Police daily summary separately reported a 59-year-old woman killed by an FPV drone in Zaporizhia district. The available report did not identify the settlement. Because the Nov. 18 Kushuhum entry already records a woman killed by an FPV drone in Zaporizhia district, the later summary is not added as another death pending location-level identification.

The ledger remains 173 incidents, 420 source records and 446 final deaths. It now has 136 revision entries with confirmed effective dates and 90 still null. No final incident counts changed.


## Stage 50 — Nov. 20 Kyiv and Lviv subtotal mapped

The 363→372 transition is now fully allocated:

| Historical subtotal | Increment | Incident mapping |
|---|---:|---|
| 363→366 | +3 | Initial Kyiv ballistic-attack death toll |
| 366→368 | +2 | Lviv, Sknyliv railway station |
| 368→371 | +3 | Kyiv toll revised from three to six in the prime minister's nationwide update; Lviv's two deaths and the first three Kyiv deaths were already counted |
| 371→372 | +1 | Kyiv toll revised from six to seven in the mayor's update |

The Kyiv incident's revision chain is 3→6→7, not 3+6+7. The two Lviv deaths are separate. Other Nov. 20 incident records, including the Nikopol-district death and the later Zaporizhia regional daily aggregate, remain outside this 363→372 mapping until their later inclusion dates are established.

The ledger remains 173 incidents, 420 source records and 446 final deaths. It now has 140 revision entries with confirmed effective dates and 86 still null. No final incident counts changed.


## Stage 51 — Nov. 21–22 subtotal and Dymer sequence mapped

The 372→391 progression is now allocated:

| Historical subtotal | Increment | Incident mapping |
|---|---:|---|
| 372→374, Nov. 21 | +2 | Kryvyi Rih ballistic strike: a seven-year-old boy and a 20-year-old woman paramedic |
| 374→379, by Nov. 22 | +5 | Dymer's first two recovered bodies (2), Nikopol district (1), Zaporizhia city/district aggregate (2) |
| 379→391, Nov. 22 | +12 | Dymer 2→7 (+5), Vyshneve supermarket (3), Bila Tserkva district (1), Dnipro (1), Novoslobidska community (1), Zaporizhia enterprise (1) |

The Dymer incident's revision chain is now dated and reconciled:
- two initial recovered bodies entered the 379 baseline;
- three further recoveries raised the toll from two to five;
- the sixth and seventh bodies brought the Nov. 22 incident toll to seven;
- the eighth through eleventh bodies were recovered on Nov. 23;
- the 79-year-old woman rescued alive on Nov. 23 died in hospital on Nov. 24, bringing the final incident count to 12.

The initial two Dymer deaths are not added again to the 379→391 transition. The Nov. 22 update adds only five more Dymer deaths to the baseline, then the other seven incident groups in the table complete the +12. The Nov. 23 and Nov. 24 Dymer revisions are mapped to later subtotals, not the Nov. 22 update.

The ledger remains 173 incidents, 420 source records and 446 final deaths. It now has 157 revision entries with confirmed effective dates and 69 still null. No final incident counts changed.


## Stage 52 — Nov. 23–26 additions mapped to the current 421 total

The final public sequence is now reconstructed:

| Historical subtotal | Increment | Incident mapping |
|---|---:|---|
| 391→395, Nov. 23 | +4 | Dymer: eighth through eleventh bodies recovered |
| 395→398, Nov. 23 | +3 | Sloviansk (2), Stepaniivka (1) |
| 398→401, Nov. 23 | +3 | Zaporizhia non-operating private clinic (3) |
| 401→403, Nov. 23 | +2 | Nikopol (two separate deaths in separate attacks) |
| 403→407, Nov. 24 | +4 | Zaporizhia overnight residential strike (2), Kramatorsk civilian evacuation vehicle (2) |
| 407→408, Nov. 24 | +1 | Dymer survivor rescued alive on Nov. 23 died in hospital |
| 408→409, Nov. 24 | +1 | Korosten railway station |
| 409→410, Nov. 25 | +1 | Bila Tserkva overnight drone attack |
| 410→412, Nov. 25 | +2 | Odesa district (1), Podilsk (1) |
| 412→413, Nov. 25 | +1 | Fedorivka passenger minibus |
| 413→415, Nov. 25 | +2 | Sumy civilian car (1), delayed hospital death in Seredyno-Budska (1) |
| 415→416, Nov. 25 | +1 | Malyn vehicle-parking-area strike |
| 416→418, Nov. 26 | +2 | Kharkiv, Novobavarsky district |
| 418→419, Nov. 26 | +1 | Separate Nov. 25 FAB-500 strike in Sloviansk |
| 419→421, Nov. 26 | +2 | Two people killed on a road near Dovzhyk on Nov. 25 |

The Dovzhyk and Sloviansk deaths were absent from the prior structured ledger and have now been added as separate incident records with official or corroborating sources. The 418→421 increment is therefore fully represented in the current 175-incident dataset.

The public 421 total now reconciles as 148 + 19 + 25 + 229. The current incident ledger remains 28 higher in raw final-count arithmetic. The remaining raw difference is not to be erased by changing the public total: it reflects the identified scope differences and unresolved later-count inclusions, including the three later Chornomorsk deaths, the second death in the Nov. 3 Dnipro incident, the Saltivsky overlap, and the two additional Oct. 29 Izium deaths.

Current ledger status: 175 incidents, 423 source records, 449 final documented deaths, 228 revision entries, 175 with confirmed effective dates and 53 still null. No public chronology or method-page figure was changed by this audit.


## Stage 53 — all 53 null effective dates classified

The remaining null revisions have been inventoried in `UNRESOLVED-EFFECTIVE-DATES-2026-11-26.md`. They fall into six categories:

| Category | Null revision entries | Net count change |
|---|---:|---:|
| Pre-Oct. 29 legacy baseline membership not individually mapped | 46 | +139 |
| Two additional Oct. 29 Izium deaths, later inclusion unverified | 2 | +2 |
| Oct. 31 Sloviansk death, Nov. 2 baseline inclusion unverified | 1 | +1 |
| Second death in Nov. 3 Dnipro incident, not established in the 421 subtotal | 1 | +1 |
| First Saltivsky death, possible overlap with preceding subtotal | 1 | +1 |
| Three later Chornomorsk hospital deaths, not established in the 421 subtotal | 2 | +3 |
| **Total** | **53** | **+147 net** |

The pre-Oct. 29 group includes a -1 correction in the Kharkiv market incident, hence 139 net rather than 140. These 53 null revisions are not 147 additional deaths to be added to the public total. They combine legacy-baseline candidates, known uncounted revisions and possible overlaps.

The immediate remaining historical task is to reconstruct the 148 baseline's incident membership from the archived 123 baseline and Oct. 25–28 change log. The 46 legacy entries remain null until that membership is proven. No public figure or incident final count changed in this stage.
