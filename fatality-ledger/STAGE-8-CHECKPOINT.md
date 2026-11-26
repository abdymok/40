# Fatality ledger — Stage 8 checkpoint

**Status:** Komyshuvakha and separate Nov. 1 police-vehicle incident added  
**Date:** 2026-11-26  
**Public pages unchanged.**

## Komyshuvakha incident record

Added `UA-ZAP-KOMYSHUVAKHA-2026-11-02-HUMANITARIAN-HUB` to `incidents.json`.

- Incident date: Nov. 2, 2026.
- Final documented deaths: **72**.
- Evidence classification: official and independent.
- Scope: mixed non-combatant, including civilians, police officers, rescuers, school and administrative-services-centre staff, municipal workers and medical personnel.
- Four people remained missing when the rescue operation concluded. They are not counted.
- Source records preserve official and independent reporting from Nov. 2 through Nov. 16.

### Preserved count progression

The revision history now preserves 14 sequential states:

`1 → 18 → 24 → 29 → 31 → 33 → 37 → 40 → 42 → 43 → 50 → 53 → 55 → 72`

Important distinctions:
- The first official Nov. 2 report said one person had been killed.
- Interfax reported 18 deaths at 19:55.
- DSNS reported 24 at 22:54.
- On Nov. 3, the toll rose through 29, 31 and 33 in successive reports.
- On Nov. 4, it rose to 37 and then 40.
- On Nov. 5, police reported 42 bodies recovered; the president then confirmed 43 deaths.
- On Nov. 6, DSNS reported 50 at 10:49. Semikin reported 53 at 10:51. These are successive updates, not two counts to add together.
- On Nov. 7, the toll rose to 55.
- On Nov. 16, the search-and-rescue operation concluded with 72 confirmed deaths.

The Nov. 5 source trail also mentions two police officers who died in hospital after being wounded in a **separate Nov. 1 drone strike on a police vehicle**. Those officers are not part of the 72 Komyshuvakha victims.

## Separate Nov. 1 police-vehicle incident

Added `UA-ZAP-KOMYSHUVAKHA-2026-11-01-POLICE-VEHICLE`:
- Incident date: Nov. 1, 2026.
- Two police officers, Oleh Dubetskyi and Serhii Berezhko, died in hospital on Nov. 4.
- The record is classified as non-combatant emergency personnel.
- It is explicitly separate from the Nov. 2 humanitarian-hub strike.

This distinction matters to the Nov. 5 cumulative reconciliation: two bodies recovered at Komyshuvakha and the two delayed police deaths are four separate additions. The later increase from 42 to 43 belongs only to the Nov. 2 Komyshuvakha incident.

## Data and validation

The pilot dataset now contains:
- 19 incident records;
- 108 documented deaths across those records;
- 79 source records.

The 108 is a partial data sum, not the national/project total. Earlier October and November incidents are still missing from the pilot.

Validation after the additions confirmed:
- all incident IDs unique;
- all source IDs unique across the dataset;
- no dangling source references;
- each revision sequence continuous;
- each record's final revision equals its current death count;
- all source URLs use HTTP or HTTPS.

The schema now permits date-only revision timestamps where the original report gives a date but no reliable publication time. Exact times are retained where established.

## Next stage

Continue reconstructing the October and early-November incidents, starting with the large early-November corrections and any duplicated deaths in the Oct. 30–Nov. 5 source-to-page audit. The Komyshuvakha incident is now a single 72-death record; its interim tolls are not additional incidents. The separate Nov. 1 police-vehicle incident is a two-death record.

No public figures or pages have been changed.
