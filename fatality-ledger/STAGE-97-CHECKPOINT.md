# Stage 97 checkpoint — correct the Saltivsky two-death allocation

Date: 2026-11-26

## Timestamped sequence

- Commit `9a8a5b44430108fdb04e4744a1ff2dc8a88db799` records the ≈283 subtotal at 11:17:07 UTC (13:17 Kyiv). Its +1 is explicitly the Chornomorsk market death.
- Terekhov's Telegram channel archive records the first Saltivsky death at 13:37 UTC on Nov. 11 and the second-death update at 13:43 UTC. Both reports postdate the ≈283 baseline.
- Commit `26a44c4287b2429832fc9f2fc26087cfe45c7e12` at 13:58:46 UTC (15:58 Kyiv) is titled “Add second Kharkiv strike death and update dashboard.” It raises the displayed subtotal only 283→284 (+1).
- The chronology entry says two people were killed, but the public subtotal increases by only one. The commit title and revision sequence allocate that +1 to the second-death revision (REV-002). The first-death revision (REV-001) has no separate dashboard increment.

## Corrected adjudication

- Saltivsky REV-001 (—→1): `ledger_effective_at` changes from `2026-11-11` back to `null`. The first death was reported after the ≈283 baseline and is not separately included in the 421 subtotal.
- Saltivsky REV-002 (1→2): remains `ledger_effective_at: 2026-11-11`, assigned to the 283→284 increment.
- The public 421 therefore includes one of the two Saltivsky deaths; the first reported death is not included. No public total is changed in this audit.

## Updated ledger status

- Incidents: 175
- Source records: 428
- Final documented deaths: 451
- Revision entries: 230
- Revisions with confirmed effective dates: 197
- Revisions still null: 33
- Pre-Oct. 29 null revisions: 26, net +82
- Later null revisions: 7, net +8
- Total net change across null revisions: +90
- Public method-page minimum: 421 (unchanged)