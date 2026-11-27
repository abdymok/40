# Stage 127 checkpoint — Oct. 19–21 casualty subtotal bridge

Date: Nov. 27, 2026

## Scope

Reconstruct the intermediate Oct. 19–21 changes between the Oct. 16 ≈98 subtotal and the Oct. 21 ≈105 subtotal. This reopens the bridge detail in Stage 124; it does not change any incident toll, effective date or public minimum.

## Dated dashboard sequence

| Transition | Commit / date | Change | Evidence |
|---|---|---:|---|
| 98→99 | `ac5b47d`, Oct. 19 | +1 Kyiv death | The commit changes the dashboard from ≈98 to ≈99 and revises the method paragraph to include the 21-year-old woman killed in the Oct. 19 Kyiv ballistic attack. |
| 99→102 | `a2ebd83`, Oct. 20 | +3 Chabany deaths | The commit changes the dashboard from ≈99 to ≈102 and explicitly includes three Chabany deaths in the method paragraph. At this point the deaths were attributed to local reporting. |
| 102→103 | `f40e650`, Oct. 20 | +1 Holosiivsky death | The commit changes the dashboard from ≈102 to ≈103 after adding the death reported following a UAV fall in Holosiivsky district. The method paragraph remains stale at ≈102 in this commit. |
| 103→100 | `25abf34`, Oct. 20 | −3 Chabany deaths | The dashboard changes from ≈103 to ≈100. Its detail labels the three Chabany deaths as attributed to one unverified local Telegram channel and excluded from the official/media subtotal. The method paragraph remains stale at ≈103 and still says Chabany is included. |
| 100→105 | `84c0c69`, Oct. 21 | +5 deaths | The dashboard changes from ≈100 to ≈105. The revised method paragraph names two Sviatoshynsky deaths and three Kramatorsk heating-supply workers, while retaining the Kyiv and Holosiivsky deaths already in the 100 subtotal. It explicitly says the Chabany deaths are excluded. |

The net increase from 98 to 105 is seven: one Kyiv death, one Holosiivsky death, two Sviatoshynsky deaths and three Kramatorsk heating-supply workers. The intermediate arithmetic is +1, +3, +1, −3 and +5. The +3 Chabany inclusion was temporary and was reversed before the 105 snapshot.

## Later Chabany inclusion

This Oct. 19–21 sequence is not the final public treatment of Chabany. On Oct. 22, after corroboration by the Kyiv Regional Military Administration, regional police, the prosecutor's office and independent reporting, the dashboard moved from ≈118 to ≈121 and explicitly included the three Chabany deaths. Stage 63 documents that later inclusion. The 121→123 transition was a separate scope/method change with no incident-level allocation.

The three Chabany deaths are not represented in the current structured incident ledger. Their inclusion in the historical public subtotal is therefore a documented scope difference between the public running count and the current incident ledger, not an unresolved addition to the 427 figure.

## Adjudication

- The 98→105 net arithmetic is confirmed by the dated snapshots and commit diffs.
- The Oct. 20 method paragraph briefly lagged behind the dashboard value in both directions: after 102→103 it still displayed ≈102; after 103→100 it still displayed ≈103 and continued to mention Chabany as included.
- The Oct. 21 105 method paragraph resolves the Chabany status for that snapshot: the three deaths are excluded.
- The later Oct. 22 118→121 update re-includes the three Chabany deaths after corroboration.
- No incident toll, revision value, `ledger_effective_at`, or public total changed in this stage.
- The public minimum remains 427 through Nov. 26, 2026.

## Integrity

Current incident ledger: 186 incidents, 477 source records, 465 final documented deaths and 245 revision entries (204 dated, 41 null). The historical-inclusion queue remains 17 revision entries, net arithmetic +27. No ledger validation issue was introduced.