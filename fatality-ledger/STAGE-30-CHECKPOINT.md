# Stage 30 checkpoint — Kharkiv Oct. 28 fatality source reconciliation

Date: 26 November 2026

## Finding

The Oct. 29 Kharkiv Regional Military Administration 24-hour report of one person killed in Kharkiv during the previous day refers to the existing Oct. 28 Osnoviansky district incident. It is not evidence of a second fatality.

The event is identified more specifically by the Kharkiv Regional Prosecutor's Office: at about 12:55 on Oct. 28, a Russian Geran-3 jet-powered drone struck a postal operator's branch in Osnoviansky district, killing one man and injuring four. ArmyInform reported the prosecutor's statement on Oct. 28. The regional administration's Oct. 29 report and Interfax-Ukraine's same-morning report identify one 38-year-old man killed during the previous day.

Sources:
- Kharkiv Regional Prosecutor's Office, reported by ArmyInform, Oct. 28, 17:04: https://armyinform.com.ua/2026/10/28/rosiya-vdaryla-po-harkovu-ye-zagyblyj-chetvero-poranenyh/
- Kharkiv Regional Military Administration, Oct. 29, 08:54: https://kharkivoda.gov.ua/news/137725
- Interfax-Ukraine, Oct. 29, 08:58: https://interfax.com.ua/news/general/1227728-amp.html
- Earlier Oct. 28 report, Ukrainska Pravda: https://www.pravda.com.ua/eng/news/2026/10/28/8060077/

## Age discrepancy

The early Oct. 28 regional update, repeated by Ukrainska Pravda and other outlets, identified the dead man as 60. The Prosecutor's Office report and the next-day regional 24-hour report identify him as 38. The ledger now preserves this discrepancy explicitly in the incident description and source notes. It does not silently select the earlier age, and the discrepancy does not create an additional death.

## Ledger change

Updated the existing incident `UA-KHA-KHARKIV-OSNOVIANSKY-2026-10-28-DRONE` with the postal-branch / Geran-3 details and three additional source records. No incident was added, no death count changed, and no revision was created.

Commits:
- `2e68632b4799e9b6a26be85f069d985bb01b1448` — source reconciliation update
- `4b4fc8a7774d882a616db4cc99ebf57c843a49fb` — corrected ArmyInform source URL

## Structural validation

Fresh validation after the update:
- 166 incident records
- 382 source records
- 438 documented deaths
- No duplicate incident IDs
- No duplicate source IDs
- No broken revision-to-source references
- Every final revision value matches its incident's final documented-death count

## Reconciliation impact

This closes the apparent Kharkiv Oct. 28/29 extra-fatality lead as a duplicate report of an already-recorded incident. The current pilot-ledger sum remains 438. The published method-page minimum remains 418. The +20 difference is unchanged and still requires historical inclusion-date reconstruction. No public chronology or dashboard total was changed.
