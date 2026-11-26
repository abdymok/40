# Stage 87 checkpoint — correct unresolved inventory arithmetic

Date: 2026-11-26

## Verification

A fresh programmatic pass over `fatality-ledger/incidents.json` confirms:
- Incidents: 175
- Source records: 428
- Final documented deaths: 451
- Revision entries: 230
- Confirmed `ledger_effective_at`: 198
- Null `ledger_effective_at`: 32
- Pre-Oct. 29 null revisions: 26, net +82
- Later null revisions: 6, net +7
- Combined net arithmetic change among null revisions: +89

The six later null revisions are:
1. Two additional Oct. 29 Izium revisions (+2)
2. Oct. 31 Sloviansk death (+1)
3. Second Nov. 3 Dnipro death (+1)
4. Two later Chornomorsk revisions (+3)

## Chornomorsk finding

The historical Nov. 11 dashboard sequence explicitly records:
- ≈282 before the Chornomorsk addition
- 282→283 for the initial Chornomorsk market death
- 283→284 for the second Saltivsky death, with the chronology saying the first Saltivsky death had already been reported

The current incident ledger records four Chornomorsk deaths: one at the scene and three later hospital deaths. The first death is dated Nov. 11 in the public subtotal. The two subsequent revisions (1→3 and 3→4) remain null because the public 421 change history establishes the initial death but does not establish when, or whether, the three later hospital deaths entered the subtotal.

## Corrections made

- Corrected unresolved-inventory net from +100 to +89.
- Removed the first Saltivsky death from the null-revision category summary.
- Corrected the later unresolved category from seven entries / eight deaths to six entries / seven deaths.
- Updated the master reconciliation's current null-revision classification and the Saltivsky comparison row.
- No incident records, effective dates, source records or public totals changed.

The public method-page minimum remains 421.
