# Stage 78 checkpoint — correct Oct. 14–15 Lutsk and Kirovohrad effective dates

Date: 2026-11-27

## Finding

The archived dashboard sequence establishes the inclusion dates of four current ledger revisions:

| Incident / revision | Count change | Effective date | Historical dashboard evidence |
|---|---:|---|---|
| Lutsk REV-001 | —→3 | 2026-10-14 | The 85→89 update added the Lutsk attack after the regional administration confirmed the initial three-death toll. |
| Lutsk REV-002 | 3→4 | 2026-10-14 | The ≈89 snapshot explicitly includes four deaths in Lutsk. |
| Lutsk REV-003 | 4→6 | 2026-10-14 | The 90→92 dashboard change is in commit `203f67dd701b0a0f34d152fcf0bb4b664d8d9c52`, created at 13:48:50 UTC (16:48:50 Kyiv) on Oct. 14. Its update history explicitly says the Lutsk toll rose to six and the subtotal rose 90→92. Volyn.com.ua reported six deaths and 12 injured at 15:30 Kyiv time on Oct. 14, quoting Lutsk City Council secretary Andriy Razumovskyi. |
| Kirovohrad REV-001 | —→3 | 2026-10-15 | The Oct. 15 update explicitly adds the Kirovohrad attack with three deaths and raises the subtotal 92→95; commit `12ec18d5f902d58a59de878b5b8c0ddeff86d3ef`. |

The previous Stage 78 version incorrectly assigned Lutsk REV-003 to Oct. 15 because it relied on a later report timestamp. The contemporaneous 15:30 Volyn.com.ua report and the Oct. 14 90→92 commit establish Oct. 14 as the first documented inclusion date. The Oct. 15 commit `1535e91b64e569338ad26b9283b9ed436cb6f8fb` is a later media replacement that carries forward the update history; it is not the 90→92 transition.

## Changes made

- Lutsk REV-001 and REV-002 remain dated `2026-10-14`.
- Corrected Lutsk REV-003 `ledger_effective_at` from `2026-10-15` to `2026-10-14`.
- Added Volyn.com.ua's 15:30 Oct. 14 report as source `LUTSK-VOLYN-COM-2026-10-14-1530`.
- Updated the REV-003 reason to identify the 90→92 commit and the earlier corroborating report.
- Kirovohrad REV-001 remains dated `2026-10-15`.

## Updated ledger status

- Incidents: 186
- Source records: 477
- Final documented deaths: 465
- Revision entries: 245
- Revisions with confirmed effective dates: 204
- Revisions still null: 41
- Remaining historical-inclusion questions: 17, net +27
- Public provisional minimum: 427 (unchanged)

## Data handling

No incident death toll changed. Only the Lutsk REV-003 effective date and supporting source record were corrected. No public chronology, dashboard figure or public subtotal changed.
