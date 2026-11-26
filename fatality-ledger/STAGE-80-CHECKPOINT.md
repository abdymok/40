# Stage 80 checkpoint — date the Oct. 13 Kyiv ballistic-strike revisions

Date: 2026-11-26

## Finding

The current incident record `UA-KYI-KYIV-2026-10-13-EVENING-BALLISTIC` contains two revisions:
- REV-001: initial mayoral report of one person killed.
- REV-002: second body recovered, raising the toll to two.

Both revisions are explicitly reflected in the Oct. 14 selected-subtotal sequence:
- Commit `b630f05c50a0aa7459815a4e63b16e662f63b791` raises the dashboard from ≈80 to ≈81 following the initial death report.
- Commit `e394809eb026530afc1933ccf9514483a740fb1f` raises it from ≈81 to ≈82 after a further body is recovered.

The commits are timestamped 23:03 and 23:04 UTC on Oct. 13. In Kyiv, both occurred on **Oct. 14**, at approximately 02:03 and 02:04 local time. The revisions' `ledger_effective_at` dates are therefore set to 2026-10-14.

## Changes made

- REV-001 `ledger_effective_at`: null → `2026-10-14`.
- REV-002 `ledger_effective_at`: null → `2026-10-14`.
- Updated reason text to cite the exact dashboard transitions and distinguish UTC commit dates from Kyiv local dates.
- No incident count, source record, incident identity or public figure changed.

## Updated ledger status

- Incidents: 175
- Source records: 428
- Final documented deaths: 451
- Revision entries: 230
- Revisions with confirmed effective dates: 191
- Revisions still null: 39
- Remaining pre-Oct. 29 null revisions: 32, net +93
- Later null revisions: 7, net +8
- Total net change across null revisions: +101
- Public method-page minimum: 421 (unchanged)
