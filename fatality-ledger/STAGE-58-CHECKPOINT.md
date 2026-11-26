# Stage 58 checkpoint — Oct. 15–21 subtotal sequence

Date: 26 November 2026

## Verified sequence

The historical dashboard chain from 92 through 105 is now reconstructed:

| Historical transition | Increment | Incident mapping | Evidence |
|---|---:|---|---|
| 92→95, Oct. 15 | +3 | Three people killed in the large Russian attack on Kirovohrad region | Commit `12ec18d5f902d58a59de878b5b8c0ddeff86d3ef` explicitly says the subtotal rose from approximately 92 to 95 |
| 95→98, Oct. 16 | +3 | Three people killed in Kharkiv | Commit `c1f0bb19c1f3aaea9ec4c793c569b72c18ed7a74` explicitly says the three Kharkiv deaths raised the subtotal from approximately 95 to 98 |
| 98→99, Oct. 19 | +1 | 21-year-old woman killed in the overnight Kyiv ballistic attack | Oct. 19–20 update history records the rise from 98 to 99; the Oct. 19 snapshot shows 99 |
| 99→102, Oct. 20 | +3 | Three reported Chabany deaths, temporarily included as attributed deaths | Parent snapshot `06588203ec27769eabbb6208422fa3a42109c62e` shows 102 and its method paragraph includes the three Chabany deaths |
| 102→103, Oct. 20 | +1 | One death after a UAV fell in Holosiivsky district | Commit `f40e650e341dfab9de4c3616a64d1d6a3132e4c6` raises the dashboard from 102 to 103; the method paragraph remains stale at 102 |
| 103→100, Oct. 20 | −3 | Removal of the three Chabany deaths from the official/media subtotal | Commit `25abf34f90ab2c0842aa162a143c0b19ce9d0ea7` changes 103 to 100 and labels Chabany as three additional deaths attributed to one unverified local Telegram channel |
| 100→103, Oct. 20 | +3 | Three Kramatorskteploenergo heating-supply workers killed in a Russian guided-aerial-bomb attack | Commit `43be9fb8bd3ebdab20092917f13d1a50fd1fe028` adds the three worker deaths and raises 100 to 103 |
| 103→105, Oct. 21 | +2 | Two people killed in Sviatoshynsky district | Commit `84c0c691e7114fc1295fa2b339976cfb276c487b` adds the deaths and raises 103 to 105 |

## Oct. 20 scope correction and method-note lag

The 102 snapshot explicitly includes the three Chabany deaths. The Holosiivsky update raises the dashboard to 103, but the method paragraph remains at 102, so it is stale by one at that snapshot.

The next correction changes the dashboard from 103 to 100. Its explanatory method paragraph still describes the broader 103 figure, including the three Chabany deaths, while the dashboard label clarifies that those three are attributed separately and excluded from the official/media subtotal. This is a scope correction, not a newly discovered three-death downward revision to an incident record.

The following Kramatorsk commit raises the official/media subtotal from 100 to 103 by adding three workers. Its method note now treats Chabany as excluded and includes the Holosiivsky death and Kramatorsk workers. The Sviatoshynsky update then raises 103 to 105.

## Commit ancestry

The relevant Oct. 20–21 commits form one chain:
- `f40e650e341dfab9de4c3616a64d1d6a3132e4c6`: 102→103, Holosiivsky.
- `25abf34f90ab2c0842aa162a143c0b19ce9d0ea7`: 103→100, Chabany scope correction.
- `43be9fb8bd3ebdab20092917f13d1a50fd1fe028`: 100→103, Kramatorsk workers.
- `84c0c691e7114fc1295fa2b339976cfb276c487b`: 103→105, Sviatoshynsky.
- `679cd4c4e1541842a3794c72b7d583e5deea1f1a`: preserves 105 in the 09:16 snapshot.

GitHub compare results confirm the ancestry order above.

## Link to Stage 57

The next two commits still show the intermediate anomaly:
- `3c205e7cb516ca3a9843c1234b23ff05408bf6dc`: 105→107, dashboard-only +2, duplicating Sviatoshynsky deaths already included in 105.
- `46a3feb1b3430a7e58185dbca864de617f72aa28`: 107→116, +9, while the revised method paragraph adds Sloviansk 9 and Korotych 2 (+11).

The offsetting two-death discrepancy means 105→116 overall is +11, matching the eleven Sloviansk and Korotych deaths. See `STAGE-57-CHECKPOINT.md`.

## Data handling

- No incident records or revision histories changed.
- No `ledger_effective_at` values changed.
- Chabany remains excluded from the current structured ledger and the official/media dashboard scope.
- The public subtotal remains untouched.
- The current ledger remains 175 incidents, 423 source records, 449 final documented deaths, 228 revisions, 175 confirmed effective dates and 53 unresolved dates.

## Next work

1. Continue backward from the 92 subtotal to identify the full incident membership of the opening October baseline.
2. Reconstruct the 121→123 (+2) transition, which remains unidentified.
3. Keep the public 421 unchanged until legacy membership and later scope differences are fully reconciled.
