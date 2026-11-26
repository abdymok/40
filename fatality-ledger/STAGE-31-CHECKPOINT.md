# Stage 31 checkpoint — missing Kyiv Oct. 29 fatality entered

Date: 26 November 2026

## Finding

The method page's historical 148 → 173 transition explicitly includes one person killed in Kyiv during the late-evening Oct. 29 ballistic attack. The current incident ledger had no Kyiv record for that death.

The attack began shortly before 23:00 on Oct. 29. The Kyiv City Military Administration confirmed one death at 23:48. The Kyiv City Prosecutor's Office reported the following morning that a man had been killed, with effects in Dniprovskyi and Darnytsky districts. Ukrinform, citing the Kyiv City Military Administration and Kyiv Police, identifies the fatality as a man killed in Dniprovskyi district. Reuters independently reported the one death.

Sources:
- Kyiv City Military Administration Telegram channel: https://t.me/s/VA_Kyiv/20353
- Kyiv City Prosecutor's Office Telegram archive, post visible at 07:14: https://t.me/s/kyiv_pro_office?before=11450
- Ukrinform, Oct. 30, 08:42: https://www.ukrinform.net/rubric-ato/4179604-russian-strikes-on-kyiv-kill-one-injure-another-damage-homes-and-businesses.html
- Reuters, Oct. 29: https://www.reuters.com/world/ukrainian-capital-kyiv-under-attack-russian-ballistic-missiles-mayor-says-2026-10-29/

## Ledger change

Added one incident:
`UA-KYI-KYIV-2026-10-29-BALLISTIC-ATTACK-DNIPROVSKYI-FATALITY`

The incident is dated Oct. 29, with one documented civilian death. Its initial revision is recorded at the time of the prosecutor's official report on Oct. 30, but `ledger_effective_at` remains null until the exact public subtotal inclusion point is established.

Commit: `98eba101bd939f4577dbfdee10abd8d6c8f85e2c`

## Current structural validation

- 167 incident records
- 386 source records
- 439 documented deaths
- No duplicate incident IDs
- No duplicate source IDs
- No broken revision-to-source references
- Every final revision value matches its incident's final documented-death count

## Oct. 29 incident-date comparison

The current ledger now contains 27 deaths attached to Oct. 29 incidents:
- Dnipro railway station: 15 (14 reported on Oct. 29, plus the later hospital death)
- Chernihiv: 2
- Kremenchuk: 3
- Kyiv ballistic attack: 1
- Izium public-health institution strike: 5
- Separate Izium attack killing a 59-year-old woman: 1

The method page's historical 148 → 173 transition adds 25. Its stated components are 14 initially reported killed at Dnipro railway station, two in Chernihiv, three in Kremenchuk, one in Kyiv, the subsequent hospital death of a Dnipro victim, and four in the Izium airstrike. That historical composition totals 25.

The current 27 therefore exceeds the historical 25 by two. The candidate differences are the fifth employee death in the Izium public-health institution strike and the separately reported 59-year-old woman killed in Izium. Both must be checked against the exact historical publication/inclusion sequence before assigning either to the 173 snapshot or later increments. The Kyiv death is now represented, so it is no longer a missing incident-level record.

## Change control

The incident ledger alone was changed. No public chronology, methodology page, dashboard figure or change-log total was edited. The current pilot sum of 439 is not approved as a replacement for the published 418.
