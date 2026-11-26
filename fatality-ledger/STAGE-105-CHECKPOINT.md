# Stage 105 checkpoint — Oct. 31 Sloviansk death excluded from 421

Date: 2026-11-26

## Incident

- Incident ID: `UA-DON-SLOVIANSK-2026-10-31-ATTACK`
- Revision: `UA-DON-SLOVIANSK-2026-10-31-ATTACK-REV-001`
- Incident date: Oct. 31, 2026
- Deaths: 1
- Source: Donetsk Regional Military Administration head Vadym Filashkin, Nov. 1, 10:05 Kyiv time, [Telegram post 19012](https://t.me/VadymFilashkin/19012). The post reports one person killed in Sloviansk over the preceding 24 hours.

## Reconstructed 174 baseline

The earlier Stage 88 review correctly distinguished this death from the four Nov. 2 deaths in the Nov. 3 203→207 increment, but left open whether it might have been embedded in the carried-forward 174 baseline.

The historical arithmetic now closes that possibility:

| Component of 174 | Deaths |
|---|---:|
| Oct. 28 carried-forward baseline | 148 |
| Oct. 29 cohort, included by Oct. 30 | 19 |
| Oct. 30 update: Kyiv (1), delayed Dnipro hospital death (1), Izium (4) | 6 |
| Separate Izium death reported Nov. 2 | 1 |
| **Reconstructed 174 baseline** | **174** |

The 148 baseline is dated Oct. 28. The Oct. 29 cohort and Oct. 30 update are separately mapped in the historical reconciliation. The Nov. 2 Izium death is the one further incident-level addition before the 174→192 Komyshuvakha update. There is no remaining arithmetic space in this reconstructed bridge for the Oct. 31 Sloviansk death.

## Later increments checked

- The 174→192 update is the 18-death Komyshuvakha addition.
- The Nov. 3 203→207 increment is four deaths from Nov. 2 in Sloviansk, Kramatorsk, Druzhkivka and Bilenke. The Sloviansk death is a separate incident and date.
- The Nov. 5 230→236 increment explicitly lists six late-reported deaths: two in Sloviansk from Oct. 30 attacks, one in Shostka, one in Nikopol district, one in Dnipro district and one in Orikhiv. It does not include the Oct. 31 Sloviansk death.
- The subsequent 192→421 sequence is reconstructed as incident-level additions in the method-to-ledger reconciliation. No separate increment for this death appears.

The two Sloviansk deaths in the 230→236 update are from Oct. 30 attacks and must not be conflated with this separate Oct. 31 incident.

## Disposition

**Finding: established exclusion from the historical 421 public subtotal.**

The incident remains in the structured ledger as one documented civilian death. Its `ledger_effective_at` remains null because it was not included in the historical public subtotal. The revision reason in `incidents.json` has been updated to record the exclusion and its evidence trail.

No death has been added to the public 427 minimum. No incident count, documented-death count or revision count has changed. The current 33 null effective-date entries remain 33; one is now explicitly classified as an established exclusion rather than an unresolved inclusion question.

## Change control

- `incidents.json`: revision reason only; no count or date changed.
- Public chronology, dashboard and method-page figures: unchanged.
- Current public minimum: 427.
- Current raw incident-ledger sum: 458.
- Current null revisions: 33.
