# Fatality ledger — Stage 7 checkpoint

**Status:** 17 incident records entered; source and revision checks passed  
**Date:** 2026-11-26  
**Public pages unchanged.**

## Current data files

- `fatality-ledger/incident.schema.json`
- `fatality-ledger/incidents.json`
- `fatality-ledger/NOV23-26-RECONCILIATION.md`
- `fatality-ledger/UNRESOLVED-NIKOPOL-2026-11-23.md` (now resolved; retained as a dated investigation record)

## Records entered

The current pilot dataset contains:
- Dymer residential strike: 12 documented deaths, with nine dated revisions and 13 source records.
- Two separate deaths in Sloviansk and Stepaniivka, reported in one National Police roundup.
- Zaporizhia non-operating private clinic: 3 deaths.
- Two separate deaths in Nikopol city on Nov. 23, now identified through local reporting: a 45-year-old woman killed in a heavy-artillery attack and a 62-year-old woman killed in a separate reported attack.
- Kramatorsk civilian evacuation vehicle: 2 deaths.
- Zaporizhia residential strike on Nov. 24: 2 deaths.
- Korosten railway station: 1 death.
- Bila Tserkva overnight attack: 1 death.
- Two separate Odesa-region deaths on Nov. 24: one in Odesa district and one in Podilsk.
- Fedorivka passenger bus: 1 death.
- Two separate Sumy-region incidents: the Nov. 24 Sumy car strike and the delayed Nov. 25 hospital death from the Nov. 23 Seredyno-Budska attack.
- Malyn vehicle parking area: 1 death.
- Kharkiv Novobavarsky residential strike: 2 deaths.

The 17 records currently contain 34 documented deaths. **This is only a partial dataset sum. It is not the project-wide total and must not be displayed as one.** It includes Dymer's full 12-death incident record, including two deaths already present in the historical 379 baseline, while most earlier incidents from October and November have not yet been entered.

## Source-boundary decisions

- The National Police's Nov. 23 report was split into distinct Sloviansk and Stepaniivka records because the deaths occurred in different settlements and on different incident dates.
- The Nov. 24 Odesa report was split into two records because local reporting identifies separate deaths in Odesa district and Podilsk.
- The two Nov. 23 Nikopol deaths were initially held in an unresolved queue. Local reports citing the Nikopol mayor identify two women and distinguish the heavy-artillery fatality from the other fatal attack. They are now separate records. The cumulative addition remains two, 401 → 403.
- The two deaths in Seredyno-Budska and Sumy city are separate incidents, with incident dates Nov. 23 and Nov. 24 respectively, despite being reported together on Nov. 25.

## Validation performed

The schema and incident data were fetched back from GitHub and parsed. Structural checks confirmed:
- 17 unique incident IDs;
- 54 globally unique source IDs;
- no duplicate incident identifiers;
- no missing source references in revision histories;
- each record's final revision value equals its current documented death count;
- every revision sequence is continuous;
- all source references resolve within their own incident record.

This remains a structural consistency check, not a full JSON Schema validator run. A repository-level automated validator is still required before public integration.

## Next stage

Continue the source-by-source reconciliation for the rest of the project inventory, beginning with the earlier October and November records. The current public minimum of 418 is supported by the dated method arithmetic through Nov. 26, but it is not yet independently regenerated from the incident dataset. Do not connect the partial pilot to the live dashboard, chronology or change log.
