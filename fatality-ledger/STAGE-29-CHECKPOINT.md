# Stage 29 checkpoint — Chernihiv incident added and ledger revalidated

Date: 26 November 2026

## Source adjudication

The two Chernihiv references in the Oct. 29 archive are the same incident, not two separate fatality events. The City Military Administration's post 4420 reported two deaths in a UAV strike on shops. Ukrinform, Ukrainska Pravda, LB.ua and Interfax-Ukraine independently describe the same central-city strike and identify the two victims as 15-year-old girls. Later injury updates refer to the same event. The ledger must therefore contain one Chernihiv incident with two deaths, not two two-death records.

Sources reviewed:
- Bryzhynskyi, Chernihiv City Military Administration, Oct. 29, 12:02: https://t.me/bryzynskyi/4420
- Ukrinform, Oct. 29, 14:00: https://www.ukrinform.net/rubric-ato/4179356-russian-drone-attack-on-central-chernihiv-kills-two-teenage-girls-injures-11.html
- Ukrainska Pravda, Oct. 29: https://www.pravda.com.ua/eng/news/2026/10/29/8060232/
- Interfax-Ukraine, Oct. 29, 12:25: https://en.interfax.com.ua/news/general/1227940.html
- LB.ua, Oct. 29: https://en.lb.ua/news/2026/10/29/47154_enemy_drone_hits_central.html

## Ledger change

Added incident `UA-CHN-CHERNIHIV-2026-10-29-CENTRAL-DRONE-STRIKE` to `fatality-ledger/incidents.json` with two documented deaths, five source records and one initial revision. The record preserves `ledger_effective_at: null` because the date it entered the project's public running subtotal has not yet been established.

Commit: `29f200397b9955cbdf29b61b28877063bc50d2d8`

## Revalidated current dataset

A fresh structural pass over the updated JSON reports:
- 166 incident records
- 379 source records
- 438 documented deaths
- No duplicate incident IDs
- No duplicate source IDs
- No broken revision chains
- Every revision source reference resolves within its incident record
- Every final revision value matches the incident's `documented_deaths`

The repository validator's accepted evidence classification is `official_and_media`, which is used for the new record. The current ledger total is now 438, compared with the published method-page minimum of 418. The difference is **+20**, not +18 as stated in the earlier Stage 20 reconciliation note. That older decomposition is therefore not a current sign-off and must be recalculated against the latest dataset.

## Updated Oct. 29 comparison

The four previously present Oct. 29 records summed to 24. The confirmed Chernihiv incident adds two, bringing the current Oct. 29 incident-date sum to **26**. The historical 173 snapshot is 25 above the Oct. 28 subtotal of 148. This leaves a provisional +1 difference for the Oct. 29 incident-date group, subject to exact historical inclusion dates and the fact that the current Dnipro record includes a later hospital death.

The prior Stage 20 note's Oct. 29 sum of 27 is not reproduced by the current file and should not be carried forward without identifying the extra death it included.

## Change control

Only the incident ledger was changed. No public chronology, method-page text or dashboard figure was changed. The 438 figure is the calculated pilot-ledger sum, not an instruction to replace the published 418 before the full reconciliation is complete.
