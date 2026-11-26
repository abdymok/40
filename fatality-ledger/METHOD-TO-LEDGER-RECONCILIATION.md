# Method-page to incident-ledger reconciliation

**Working status:** Stage 20  
**Current ledger sum:** 436  
**Published method-page minimum:** 418  
**Difference:** +18 in the pilot incident dataset

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
- The current incident inventory through Oct. 28 sums to 161, 13 above the legacy 148. The exact membership of those 13 deaths in the old subtotal is still being reconstructed; incident date alone is insufficient because several deaths were reported or revised later.
- The current Oct. 29 incident records sum to 27, two above the 25 in the 173 snapshot: four rather than five at the public-health institution at the first snapshot, later corrected to five, plus a separate 59-year-old woman killed in another Izium attack.
- The current post-192 additions sum to 229, three above the method's 226. The clearly identified upward revisions are Chornomorsk (+3 beyond the method's one) and Dnipro on Nov. 3 (+1 beyond the method's one). One death elsewhere in the post-baseline comparison remains to be reconciled downward or identified as a missing method increment.

These components produce the current difference: +13 +2 +3 = **+18**. This is a working decomposition, not yet a final sign-off.

## Required next work

1. Reconstruct membership of the legacy 148 and 192 snapshots from the original commits and change-log entries, including source publication date and the date the project actually counted each death.
2. Add an explicit `ledger_effective_at` to every revision once the historical inclusion date is established. Do not infer it from incident date.
3. Compare every method-page increment from Nov. 2 through Nov. 26 against the matching incident record and revision history; identify the one-death offset in the post-baseline comparison.
4. Keep the DTEK driver and Kramatorsk Oct. 9 OHCHR lead unresolved until source/duplicate questions are settled.
5. Do not force the ledger to 418. The current total is a calculated pilot sum and may change if source-level deduplication or additional incident verification changes any record.

No public totals are to be changed until the incident dataset and method arithmetic reconcile or the discrepancy is explicitly explained and approved.
