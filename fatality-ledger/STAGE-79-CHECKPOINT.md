# Stage 79 checkpoint — correct Oct. 16 Kharkiv market effective date

Date: 2026-11-26

## Finding

The Kharkiv market incident `UA-KHA-KHARKIV-2026-10-16-MARKET-STRIKE` has two revisions:
- REV-001: preliminary three deaths.
- REV-002: revised official count of two deaths after a man initially reported dead was resuscitated.

The Oct. 16 dashboard snapshot at commit `c1f0bb19c1f3aaea9ec4c793c569b72c18ed7a74` explicitly says that three deaths reported in Kharkiv raised the selected-incident subtotal from approximately 95 to approximately 98. Therefore REV-001's `ledger_effective_at` is corrected from Oct. 22 to **Oct. 16**.

The later official regional update, reported by Ukrinform at 13:12 and Interfax-Ukraine at 11:09, confirmed two deaths, identifying a 71-year-old woman and a 58-year-old man. The Oct. 16 dashboard snapshot continued to show approximately 98 and still named three deaths in Kharkiv. No archived subtotal update documents a one-death subtraction. Therefore REV-002 remains null. This is not an unresolved incident death count: the current incident ledger correctly retains two final deaths. It is an unresolved historical subtotal correction.

## Changes made

- REV-001 `ledger_effective_at` corrected from `2026-10-22` to `2026-10-16`.
- REV-001 reason updated to cite the Oct. 16 95→98 dashboard update.
- REV-002 reason updated to explain why the -1 correction remains undated.
- Added Interfax-Ukraine's Oct. 16 report confirming two deaths, citing Kharkiv Regional Military Administration head Oleh Syniehubov.
- Added the Interfax source to REV-002's source list.
- No `documented_deaths` value changed; the incident remains at two.
- No public dashboard or method-page figure changed.

## Updated ledger status

- Incidents: 175
- Source records: 428
- Final documented deaths: 451
- Revision entries: 230
- Revisions with confirmed effective dates: 189
- Revisions still null: 41
- The Kharkiv market -1 revision remains in the unresolved inventory because the historical public subtotal did not visibly deduct it.
- Public method-page minimum: 421 (unchanged)
