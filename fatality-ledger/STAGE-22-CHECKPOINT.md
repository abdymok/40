# Fatality ledger — Stage 22 checkpoint

**Status:** Historical-inclusion audit and revision-timestamp gap identified  
**Date:** 2026-11-26  
**Public pages unchanged.**

## Current pilot dataset

A fresh read of `fatality-ledger/incidents.json` confirms:

- 165 incident records.
- 436 documented deaths in the incident-level sum.
- 374 source records.
- 210 revision events.
- All 210 revision events currently have `ledger_effective_at: null`.

The structural checks recorded in Stage 21 remain the latest validation result. This stage did not alter the incident data or any public page.

## Material finding

The current ledger captures incident dates, source publication times where known, record-entry dates and count-revision sequences. It does not yet capture when each death actually entered the project's running subtotal. The `ledger_effective_at` field exists, but none of the 210 revision events has been populated.

That distinction is essential. A death may have occurred on one date, been reported on another date, and entered the project subtotal only after a later source update or reconciliation. Therefore the 436 incident sum cannot be compared reliably with the historical 148, 192 or 418 cumulative snapshots by grouping on incident date alone.

## Reconciliation status carried forward

The working decomposition of the +18 difference remains:

- +13 in the pre-192 incident inventory against the legacy 148 baseline.
- +2 in the Oct. 29 incident records against the 173 snapshot (the 25-death increment).
- +3 in post-192 additions against the method's 226 additions.

This decomposition is not a final attribution of individual records. It remains subject to record-by-record reconstruction from the contemporaneous chronology, change log, method text and repository history.

## Required next work

1. Reconstruct the exact membership of the 148 and 192 snapshots from contemporaneous dated entries and repository history.
2. Assign `ledger_effective_at` only where the historical inclusion date is evidenced. Leave uncertain events null and list them explicitly.
3. Reconcile every later cumulative increment through Nov. 26 against incident IDs and revision events, preserving source timestamps and old/new counts.
4. Resolve the identified Chornomorsk, Dnipro, Saltivsky and other count differences without forcing the incident sum to 418.
5. Re-run structural and arithmetic validation before any public integration.

No public dashboard number, chronology entry, method-page total or change-log total has been changed. The 436 figure remains an internal pilot sum and must not be presented as the project's verified total.
