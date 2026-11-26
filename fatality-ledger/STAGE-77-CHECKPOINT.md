# Stage 77 checkpoint — Oct. 14 Kyiv overnight-attack ledger correction

Date: 2026-11-26

## Finding

The current incident record `UA-KYI-KYIV-2026-10-14-OVERNIGHT-STRIKES` previously carried three deaths. Contemporaneous public reporting and the Oct. 14 method-page snapshots establish a final toll of **five**, with successive official updates:

1. State Emergency Service / Red Cross: three deaths — two in Desniansky district and one in Holosiivsky.
2. Kyiv City Prosecutor's Office, update as of 08:50: four deaths — three in Desniansky and one in Holosiivsky. Ukrinform published this at 09:19 Kyiv time.
3. Kyiv Police, 11:50: five deaths — three in Desniansky and two in Holosiivsky. Interfax-Ukraine and Ukrinform independently reported the police update.

The official police source directly confirms the final five-death count and its district breakdown. This is one incident with successive casualty revisions, not three separate incidents.

## Ledger changes

- `documented_deaths`: 3 → 5.
- Incident description updated to reflect three women killed in Desniansky and two people killed in Holosiivsky.
- Evidence classification changed from `media_reported` to `official_and_media`.
- Four source records added: the prosecutor's four-death update, Kyiv Police's five-death statement, Interfax-Ukraine's police-cited report, and Ukrinform's police-cited report.
- Revision history now records:
  - REV-001: 0→3, effective 2026-10-14 (the 82→85 selected-subtotal update).
  - REV-002: 3→4, effective 2026-10-14 (the prosecutor's update).
  - REV-003: 4→5, effective 2026-10-14 (the police update; the public method page later says at least five and the dashboard moves 89→90).

## Why the correction is warranted

The Oct. 14 chronology entry already documented the four-death prosecutor update and later five-death police report. The Oct. 14 method snapshots report four and then at least five deaths in Kyiv. The structured ledger had retained only the initial SES/Red Cross toll of three. The two additional deaths are therefore not new, unreported incidents; they are missing revisions to this existing incident record.

## Updated ledger status

- Incidents: 175
- Source records: 427
- Final documented deaths: 451
- Revision entries: 230
- Revisions with confirmed effective dates: 185
- Revisions still null: 45
- Pre-Oct. 29 incident-date sum: 171
- Raw difference from the public method-page minimum: +30
- Public method-page minimum: 421 (unchanged)

The unresolved effective-date inventory now contains 45 entries: 38 pre-Oct. 29 legacy revisions with net +104 and seven later revisions with net +8.

## Data handling

- No new incident ID was created; the two additional deaths belong to the existing Oct. 14 Kyiv overnight-attack incident.
- No public chronology or dashboard figure changed because the public method page already recorded the five-death toll.
- Public method-page minimum remains 421.
