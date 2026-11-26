# Stage 58 checkpoint — Oct. 15–19 subtotal increments

Date: 26 November 2026

## Verified historical transitions

| Historical transition | Increment | Incident mapping | Evidence |
|---|---:|---|---|
| 92→95, Oct. 15 | +3 | Three people killed in the large Russian attack on Kirovohrad region | Commit `12ec18d5f902d58a59de878b5b8c0ddeff86d3ef` explicitly says the subtotal rose from approximately 92 to 95 after the regional administration reported three deaths |
| 95→98, Oct. 16 | +3 | Three people killed in Kharkiv | Commit `c1f0bb19c1f3aaea9ec4c793c569b72c18ed7a74` says the three Kharkiv deaths raised the selected-incident subtotal from approximately 95 to 98 |
| 98→99, Oct. 19 | +1 | 21-year-old woman killed in the overnight Kyiv ballistic attack | The Oct. 19–20 update history says the selected-incident subtotal rose from approximately 98 to 99 after the Kyiv fatality; the Oct. 19 snapshot shows 99 and identifies the woman |

These three transitions are supported by contemporaneous change-history language and are not inferred from incident dates alone.

## Oct. 20 baseline remains a separate reconciliation problem

The later Oct. 20 commits show inconsistent intermediate subtotal states. Commit `43be9fb8bd3ebdab20092917f13d1a50fd1fe028` changes the displayed subtotal from approximately 100 to 103 after adding three Kramatorskteploenergo worker deaths. Its revised method paragraph also lists one Holosiivsky death and other previously reported incidents.

A separate Oct. 20 commit, `f40e650e341dfab9de4c3616a64d1d6a3132e4c6`, changes a displayed subtotal from approximately 102 to 103 after adding the Holosiivsky death. These snapshots cannot yet be placed in a single clean sequence from the 99 baseline without reconstructing their commit parents and intervening casualty updates. Do not assume 99→100 is the only missing step, or treat 100 and 102 as equivalent snapshots.

The three Chabany deaths remain separately attributed and excluded from the dashboard subtotal under the later scope decision.

## Data handling

- No incident records or revision histories changed.
- No `ledger_effective_at` values changed.
- The public subtotal remains untouched.
- The current ledger remains 175 incidents, 423 source records, 449 final documented deaths, 228 revisions, 175 confirmed effective dates and 53 unresolved dates.

## Next work

1. Reconstruct the commit-parent chain between the 99 Oct. 19 snapshot and the Oct. 20 snapshots showing 100, 102 and 103.
2. Establish precisely when the Holosiivsky death and three Kramatorsk worker deaths entered the displayed subtotal.
3. Continue backward from the 92 baseline once the Oct. 20 branch/parent sequence is clear.
4. Keep the public 421 unchanged until the legacy membership and scope reconciliation is complete.
