# Stage 86 checkpoint — date the first Saltivsky death

Date: 2026-11-26

## Finding

The current Saltivsky incident record has two revisions:
- REV-001: first death reported by Kharkiv Mayor Ihor Terekhov.
- REV-002: second death, later confirmed by Interfax-Ukraine and Ukrainska Pravda.

The Nov. 11 sequence establishes that REV-001 was already in the subtotal before the second death:
1. Commit `1e4714bd2c3b7490bdf0da1d7488b967ad52cd96` records the ≈282 subtotal through Nov. 11.
2. Commit `9a8a5b44430108fdb04e4744a1ff2dc8a88db799` separately adds the Chornomorsk market death, raising the subtotal 282→283.
3. Commit `26a44c4287b2429832fc9f2fc26087cfe45c7e12` adds the second Saltivsky death, raising 283→284. Its chronology entry explicitly says the mayor had earlier reported one death.

Therefore the first Saltivsky death was already present in the ≈282 subtotal, while the second death is the 283→284 increment. REV-001's first confirmed inclusion date is Nov. 11.

## Changes made

- Saltivsky REV-001 `ledger_effective_at`: null → `2026-11-11`.
- Revision reason updated to identify the 282 baseline and the two later increments.
- No incident death count, source record or public figure changed.

## Updated ledger status

- Incidents: 175
- Source records: 428
- Final documented deaths: 451
- Revision entries: 230
- Revisions with confirmed effective dates: 198
- Revisions still null: 32
- Remaining pre-Oct. 29 null revisions: 26, net +82
- Later null revisions: 6, net +7
- Total net change across null revisions: +89
- Public method-page minimum: 421 (unchanged)


## Superseded finding — Stage 97 correction

The original Stage 86 inference that the first Saltivsky death was already present in the ≈282 baseline was incorrect. The ≈283 snapshot was committed at 11:17:07 UTC (13:17 Kyiv), before Terekhov's first death report at 13:37 UTC and second-death update at 13:43 UTC. The 283→284 update at 13:58:46 UTC adds only one and is titled “Add second Kharkiv strike death and update dashboard.” REV-001 is therefore returned to null; REV-002 remains dated Nov. 11. See `STAGE-97-CHECKPOINT.md`.
