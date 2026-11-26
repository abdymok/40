# Stage 81 checkpoint — Oct. 21 Sloviansk and Korotych inclusions

Date: 2026-11-26

## Finding

The Oct. 21 dashboard update at commit `46a3feb1b3430a7e58185dbca864de617f72aa28` raised the selected-incident subtotal from approximately 107 to approximately 116 after the Oct. 17 Sloviansk rescue operation reached a final local toll of nine. The corresponding Oct. 22 method snapshot explicitly lists nine Sloviansk deaths and two deaths in Korotych. Stage 65 reconstructs the surrounding 105→107→116 sequence: the intermediate +2 duplicated Sviatoshynsky deaths already present in the 105 snapshot, while the later method reconciliation includes the nine Sloviansk deaths and two Korotych deaths.

## Changes made

- Sloviansk REV-003 (6→9): `ledger_effective_at` set to `2026-10-21`, supported by the explicit 107→116 update and method text naming nine deaths.
- Sloviansk REV-001 (—→1) and REV-002 (1→6) remain null because the historical evidence does not establish that either preliminary toll entered the running subtotal separately before the final nine-death count.
- Korotych REV-001 (—→2): `ledger_effective_at` corrected from `2026-10-22` to `2026-10-21`, the date of the 116 subtotal update and method inclusion.
- No incident death count or source record changed.

## Updated ledger status

- Incidents: 175
- Source records: 428
- Final documented deaths: 451
- Revision entries: 230
- Revisions with confirmed effective dates: 192
- Revisions still null: 38
- Remaining pre-Oct. 29 null revisions: 31, net +92
- Later null revisions: 7, net +8
- Total net change across null revisions: +100
- Public method-page minimum: 421 (unchanged)
