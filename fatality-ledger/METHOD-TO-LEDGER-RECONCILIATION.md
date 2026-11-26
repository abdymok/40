# Method-page to incident-ledger reconciliation

**Working status:** Stage 20 analysis, amended through Stage 31 on Nov. 26  
**Current ledger sum:** 439  
**Published method-page minimum:** 418  
**Current difference:** +21 in the pilot incident dataset  

> **Stage 31 amendment:** The current dataset contains 167 incidents, 386 source records and 439 deaths. The missing Kyiv fatality from the late-evening Oct. 29 ballistic attack has been added. The current incident-date inventory through Oct. 28 sums to 162 (14 above the legacy 148); the Oct. 29 incident-date group sums to 27 (two above the historical 25-death transition to 173); and current post-192 additions sum to 231, five above the method's 226. The resulting arithmetic difference is +14 +2 +5 = +21. This is an incident-inventory comparison, not proof of when each death entered the public subtotal. Exact inclusion dates remain unresolved.

## What is established

The method page's cumulative sequence starts from an opening subtotal of approximately 192. It explicitly says this subtotal already included 18 deaths from the Nov. 2 Komyshuvakha strike. Subsequent increases in that incident were therefore increments from 18, not a fresh addition of the full 72.

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

Those eight now have incident records and are already included in the method-page total of 418.

## Known method/record differences

| Incident | Incident ledger | Method-page increment | Difference to explain |
|---|---:|---:|---:|
| Chornomorsk, Nov. 11 | 4 | 1 | +3 |
| Dnipro, Nov. 3 | 2 | 1 | +1 |
| Komyshuvakha, Nov. 2 onward | 72 final | 18 in opening subtotal, then staged increments | Must allocate the 18 baseline deaths once, not add them twice |
| Dymer, Nov. 22 onward | 12 final | 2 already in the 379 subtotal, then +5, +4, +1 | Must allocate the initial two deaths to the earlier subtotal |
| Saltivsky district, Nov. 11 | 2 final | +1 in the cited increment | One death may already have been included in the preceding subtotal |
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
- The Stage 20 snapshot of the current incident inventory through Oct. 28 was 161, 13 above the legacy 148. The refreshed Stage 24–29 dataset now sums to 162, 14 above the legacy 148. The exact membership of those 14 deaths in the old subtotal is still being reconstructed; incident date alone is insufficient because several deaths were reported or revised later.
- The Stage 20 snapshot stated that Oct. 29 incident records summed to 27, two above the 25 in the 173 snapshot. That figure is not reproduced by the current dataset. After adding the omitted Chernihiv incident, the current Oct. 29 incident-date sum is 26: Dnipro railway station (15), Kremenchuk (3), Chernihiv (2), the Izium public-health institution (5) and a separate Izium attack (1). The known historical count difference is the public-health institution's 4 → 5 revision; the separate Izium death must remain a distinct incident. The current one-death excess over the historical 25 is consistent with the institution's fifth death being added after the 173 snapshot, but the exact inclusion time still requires confirmation. The older 27 figure remains unexplained and is not reproduced by the current dataset.
- The current post-192 additions sum to 231, five above the method's 226. The five-death difference is now accounted for by three known incident-level differences: Chornomorsk (four final deaths against the method's one-death increment, +3); Dnipro on Nov. 3 (two final deaths against the method's one-death increment, +1); and Saltivsky district on Nov. 11 (two final deaths, but the first death was already in the preceding subtotal, so the method correctly adds only one; counting both as new produces +1). These explain the +5 arithmetic, subject to explicit effective-date fields still being completed.

The earlier working decompositions (+13 +2 +3 = +18, then +14 +1 +3 = +18 and the Stage 29 +20 estimate) are superseded by the Stage 31 comparison. The current arithmetic is **+14 +2 +5 = +21**: 162 versus 148 through Oct. 28; 27 versus 25 for Oct. 29; and 231 versus 226 in post-192 additions. The +14 pre-Oct. 29 difference still requires source-by-source allocation of revisions and historical inclusion dates. The +2 Oct. 29 difference is the fifth death in the public-health institution strike plus the separately reported 59-year-old woman killed in Izium; the historical 173 snapshot listed four Izium airstrike deaths. The Kyiv fatality is now included and is part of the historical 25. Do not infer `ledger_effective_at` from incident date or report date.

## Required next work

1. Reconstruct membership of the legacy 148 and 192 snapshots from the original commits and change-log entries, including source publication date and the date the project actually counted each death.
2. Add an explicit `ledger_effective_at` to every revision once the historical inclusion date is established. Do not infer it from incident date.
3. Compare every method-page increment from Nov. 2 through Nov. 26 against the matching incident record and revision history; identify the one-death offset in the post-baseline comparison.
4. Keep the DTEK driver and Kramatorsk Oct. 9 OHCHR lead unresolved until source/duplicate questions are settled.
5. Do not force the ledger to 418. The current total is a calculated pilot sum and may change if source-level deduplication or additional incident verification changes any record.

No public totals are to be changed until the incident dataset and method arithmetic reconcile or the discrepancy is explicitly explained and approved.
