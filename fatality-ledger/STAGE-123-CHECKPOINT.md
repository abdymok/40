# Stage 123 checkpoint — correct Lutsk final-death inclusion date

Date: Nov. 27, 2026

## Finding

The Lutsk REV-003 (4→6) effective date was incorrectly recorded as Oct. 15 in Stage 78. The contemporaneous evidence establishes Oct. 14:

- Commit `203f67dd701b0a0f34d152fcf0bb4b664d8d9c52` was created at 13:48:50 UTC on Oct. 14 (16:48:50 Kyiv). Its diff changes the displayed subtotal from ≈90 to ≈92 and changes the dashboard detail from four to six deaths in Lutsk. Its update history says the later regional-administration report of six deaths and 12 injured was incorporated.
- Volyn.com.ua published at 15:30 Kyiv time on Oct. 14 that six people had been killed and 12 injured, quoting Lutsk City Council secretary Andriy Razumovskyi. This precedes the 16:48 dashboard commit.
- The Oct. 15 commit `1535e91b64e569338ad26b9283b9ed436cb6f8fb` replaces dashboard media and carries forward the update history. It is not the original 90→92 transition.
- The Oct. 15 92→95 update is a separate addition: three deaths in Kirovohrad.

The source is available at https://www.volyn.com.ua/news/314396-u-lutsku-vzhe-shestero-ubytykh-pislia-rosiiskoi-ataky.

## Changes made

- Corrected Lutsk REV-003 `ledger_effective_at` from `2026-10-15` to `2026-10-14`.
- Added source `LUTSK-VOLYN-COM-2026-10-14-1530`, a Volyn.com.ua report quoting the city council secretary.
- Updated the REV-003 reason to cite the Oct. 14 90→92 commit and the earlier 15:30 report.
- Rewrote Stage 78 to distinguish the Oct. 14 Lutsk 90→92 update from the Oct. 15 Kirovohrad 92→95 update.
- Updated the Stage 78 reconciliation paragraph accordingly.

The incident's final death toll remains six. No incident total, public dashboard figure or public minimum changed.

## Updated ledger status

- Incidents: 186
- Source records: 477
- Final documented deaths: 465
- Revision entries: 245
- Revisions with confirmed effective dates: 204
- Revisions still null: 41
- Historical-inclusion questions: 17, net +27
- Public provisional minimum: 427

## Integrity

This is a correction to the historical inclusion date and source evidence only. The public minimum remains 427 through Nov. 26.
