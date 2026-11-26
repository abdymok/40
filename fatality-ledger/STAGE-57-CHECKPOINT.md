# Stage 57 checkpoint — Oct. 21 duplicate transition and offsetting subtotal

Date: 26 November 2026

## Direct snapshot comparison

The Oct. 21 commit `84c0c691e7114fc1295fa2b339976cfb276c487b` explicitly changes the dashboard from 103 to 105 while adding the two Sviatoshynsky deaths to the chronology and method paragraph. The subsequent 09:16 snapshot, commit `679cd4c4e1541842a3794c72b7d583e5deea1f1a`, retains 105. Fetching the HTML at that exact 09:16 snapshot gives:

- Dashboard subtotal: approximately 105.
- Method paragraph: approximately 105.
- The method paragraph explicitly says the subtotal includes two people killed in Sviatoshynsky district on Oct. 21.
- The update-history entry says Klitschko reported the two Sviatoshynsky deaths at 09:16.

The next relevant count commit, `3c205e7cb516ca3a9843c1234b23ff05408bf6dc`, changes the dashboard from approximately 105 to approximately 107. Its diff changes only the dashboard value and does not change the method paragraph. Fetching the HTML at this commit confirms the mismatch: dashboard 107, method 105, with the same two Sviatoshynsky deaths still explicitly included in the method text.

This is strong evidence that the 105→107 intermediate step counted the same two Sviatoshynsky deaths a second time.

## Parent-chain verification

The commits are sequential, not sibling snapshots: `84c0c691e7114fc1295fa2b339976cfb276c487b` (103→105) is the parent of `679cd4c4e1541842a3794c72b7d583e5deea1f1a` (09:16 snapshot); `679cd4` is the parent of `5fa8898b9b948d012f685aecfef552889d587361`; `5fa8898` is the parent of `3c205e7cb516ca3a9843c1234b23ff05408bf6dc` (105→107); and `3c205e7` is the parent of `deed5ac0c64b453223ea33b24457322d80532bf1`, followed by `1cdeb119645e32bde16e6cbf3907eea47c8a90ba` and `46a3feb1b3430a7e58185dbca864de617f72aa28` (107→116). This confirms the 105, 107 and 116 snapshots belong to one commit chain.

## The 107→116 transition

Commit `46a3feb1b3430a7e58185dbca864de617f72aa28` changes the dashboard from approximately 107 to approximately 116, an increase of nine. Its update history says the subtotal was updated after the Oct. 17 Sloviansk toll reached nine and says the method was reconciled to include the two Korotych deaths reported on Oct. 21.

The revised method paragraph at the 116 snapshot lists:
- Sloviansk: nine deaths;
- Korotych: two deaths;
- Sviatoshynsky: two deaths;
- Kramatorsk heating-supply workers: three deaths;
- Holosiivsky district: one death;
- Kyiv Oct. 19 ballistic attack: one death;
- Kharkiv Oct. 16: three deaths;
- earlier Kyiv deaths: at least five;
- Lutsk: six deaths;
- Kirovohrad region: three deaths.

The Sviatoshynsky two are already in the 105 snapshot. The new Sloviansk and Korotych tolls together total eleven. Yet the recorded 107→116 increment is nine.

## Offset arithmetic

The two intermediate discrepancies are exact opposites:

| Transition | Displayed change | Evidence-based incident change |
|---|---:|---:|
| 105→107 | +2 | 0; Sviatoshynsky deaths already included in 105 |
| 107→116 | +9 | +11; Sloviansk 9 + Korotych 2 |
| **105→116 overall** | **+11** | **+11** |

This suggests the intermediate 107 display double-counted the Sviatoshynsky deaths, while the next +9 update effectively absorbed the two-death discrepancy when it incorporated Sloviansk and Korotych. The 116 endpoint is therefore arithmetically consistent with the 105 baseline plus the eleven new Sloviansk and Korotych deaths.

This is a strong reconciliation hypothesis supported by the exact archived snapshots and diffs. It is not yet a license to revise the ledger's effective dates or the public 421 total. The historical update process may have had additional undocumented bookkeeping, and the earlier 105 baseline itself still requires full incident-membership reconstruction.

## Related baseline: Oct. 20

Commit `43be9fb8bd3ebdab20092917f13d1a50fd1fe028` changes the selected-incident dashboard from approximately 100 to 103 after adding three Kramatorskteploenergo worker deaths. Its method paragraph identifies the three workers, the Holosiivsky death, the Oct. 19 Kyiv death, three Kharkiv deaths, at least five earlier Kyiv deaths, six Lutsk deaths and three Kirovohrad deaths. Three Chabany deaths are separately attributed and explicitly excluded.

The 103→105 commit itself explicitly adds the two Sviatoshynsky deaths and raises the subtotal to 105. The 09:16 snapshot retains that count.

## Data handling

- No incident records or revision histories changed.
- No `ledger_effective_at` values changed.
- Chabany remains excluded from the structured ledger.
- The public subtotal remains untouched.
- The current ledger remains 175 incidents, 423 source records, 449 final documented deaths, 228 revisions, 175 confirmed effective dates and 53 unresolved dates.

## Next work

1. Find the commit that first raised the dashboard from 103 to 105 and inspect its evidence.
2. Continue reconstructing the 105 baseline membership.
3. Treat 105→107 and 107→116 as an offsetting intermediate arithmetic anomaly unless further source evidence disproves this.
4. Keep 121→123 (+2) unresolved pending an incident-level source.
5. Do not revise the public subtotal or assign effective dates solely from the displayed intermediate arithmetic.
