# Stage 33 checkpoint — Chabany scope mismatch identified

Date: 26 November 2026

## Finding

The Oct. 28 historical dashboard snapshot (commit `fb0d8ae4`) explicitly stated that the three deaths in the Oct. 20 Chabany drone attack were included in the dashboard's selected-incident subtotal. The archive entry says the deaths were reported by Kyiv Regional Military Administration and Kyiv regional police and corroborated by Ukrainska Pravda and Reuters.

Historical page at the 148 snapshot:
https://github.com/abdymok/40/blob/fb0d8ae4/articles/critical-infrastructure-damage.html

Current archive entry:
https://github.com/abdymok/40/blob/main/articles/critical-infrastructure-archive.html#2026-10-20-chabany-drone-attack

The current structured fatality ledger has no Chabany incident. This is consistent with the later working exclusion of those three deaths. They have not been reintroduced.

## Effect on reconciliation arithmetic

The raw pre-Oct. 29 comparison is 162 current ledger deaths versus 148 historically published, a net difference of +14. But the historical 148 includes three Chabany deaths that the current ledger excludes. On a like-for-like comparison only, adding those three to the current inventory would give 165 versus 148, a +17 difference. This is a comparison adjustment, not a proposed ledger addition.

The same scope mismatch carries forward into the 418 published minimum. The raw current-ledger difference remains +21 (439 versus 418). If the three Chabany deaths still embedded in the historical running subtotal are added only for comparison, the adjusted difference is +24 (442 versus 418). Do not interpret 442 as an approved count. The ledger remains 439 and the Chabany exclusion remains in force unless the user changes that instruction.

## Updated reconciliation model

- Pre-Oct. 29 current ledger: 162
- Historical Oct. 28 subtotal: 148
- Raw difference: +14
- Chabany scope difference: -3 in current ledger relative to historical subtotal
- Like-for-like pre-Oct. 29 difference: +17
- Oct. 29 current ledger: 27 versus historical 25 (+2)
- Post-192 additions: 231 versus method additions 226 (+5)
- Raw overall difference: +14 +2 +5 = +21
- Like-for-like overall difference after accounting for the three Chabany deaths: +17 +2 +5 = +24

The +17 pre-Oct. 29 like-for-like difference remains to be allocated record by record. It is not safe to treat it as a simple revision total without reconstructing which incident values were actually included in each historical subtotal.

## Change control

Updated `fatality-ledger/METHOD-TO-LEDGER-RECONCILIATION.md` to document this scope mismatch.

No incident was added. No public chronology, dashboard or method-page figure was changed.
