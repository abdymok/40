# Stage 78 checkpoint — Oct. 14–15 Lutsk and Kirovohrad effective dates

Date: 2026-11-26

## Finding

The archived method-page sequence explicitly documents the inclusion dates of four current ledger revisions:

| Incident / revision | Count change | Effective date | Historical dashboard evidence |
|---|---:|---|---|
| Lutsk REV-001 | —→3 | 2026-10-14 | The 85→89 update added the Lutsk attack as a four-death incident after the regional administration confirmed the final initial toll. |
| Lutsk REV-002 | 3→4 | 2026-10-14 | The ≈89 snapshot method paragraph explicitly includes four deaths in Lutsk. |
| Lutsk REV-003 | 4→6 | 2026-10-15 | The Oct. 15 update history explicitly records the Lutsk toll revision and subtotal increase 90→92. |
| Kirovohrad REV-001 | —→3 | 2026-10-15 | The Oct. 15 update explicitly adds the Kirovohrad attack with three deaths and raises the subtotal 92→95. |

The Oct. 14 Lutsk update is supported by the dashboard snapshot at commit `10a74ad99f3fb3911689965e6449fe41ded0c772`. The Oct. 15 Lutsk revision is preserved in the update history visible in commit `1535e91b64e569338ad26b9283b9ed436cb6f8fb`. The Kirovohrad update is explicit in commit `12ec18d5f902d58a59de878b5b8c0ddeff86d3ef`.

## Changes made

- Set Lutsk REV-001 and REV-002 `ledger_effective_at` to `2026-10-14`.
- Set Lutsk REV-003 `ledger_effective_at` to `2026-10-15`.
- Set Kirovohrad REV-001 `ledger_effective_at` to `2026-10-15`.
- Updated reason text to identify the archived dashboard evidence.
- No `documented_deaths` values, source records or incident identities changed.
- No chronology or public dashboard figures changed.

## Updated ledger status

- Incidents: 175
- Source records: 427
- Final documented deaths: 451
- Revision entries: 230
- Revisions with confirmed effective dates: 189
- Revisions still null: 41
- Remaining pre-Oct. 29 null revisions: 34, net +95
- Later null revisions: 7, net +8
- Total net change across null revisions: +103
- Public method-page minimum: 421 (unchanged)

The unresolved inventory now contains 41 rows. The four revisions dated in this stage were removed from it.

## Data handling

No public total was changed. The current incident ledger remains at 451 final documented deaths, and the public method-page minimum remains 421.
