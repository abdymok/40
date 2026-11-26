# Fatality ledger — Stage 5 checkpoint

**Status:** Incident schema created and first incident entered  
**Date:** 2026-11-26  
**Publication status:** Internal working data only. The public dashboard, chronology, method page and change log remain unchanged.

## Files created

- `fatality-ledger/incident.schema.json` — JSON Schema for one incident record.
- `fatality-ledger/incidents.json` — initial incident array containing the Dymer pilot record.

## Required incident fields

Every record requires:
- permanent unique incident ID;
- incident date and structured location;
- concise incident description;
- current fixed documented death count;
- scope classification;
- evidence classification;
- source records with publisher, source type, URL and what each source supports;
- last-verified date;
- append-only revision history.

Each revision records a unique revision ID, timestamp, old value, new value, reason and source IDs. The schema disallows unrecognized fields so the data structure cannot silently drift.

## Dymer pilot record

- Incident ID: `UA-KYI-DYMER-2026-11-22-RESIDENTIAL`
- Incident date: Nov. 22, 2026
- Current documented deaths: 12
- Last verified: Nov. 26, 2026
- Sources: 13 official and independent source records
- Revisions: 9 dated count states, from the initial two confirmed deaths through the twelfth death on Nov. 24

The revision history explicitly distinguishes the 11 bodies recovered by the end of the Nov. 23 rescue operation from the subsequent hospital death of the woman rescued alive. Her rescue update is retained as a victim-status source but does not itself increment the death count.

## Validation performed

The committed JSON files were fetched back from GitHub and parsed. Checks confirmed:
- schema and data are valid JSON;
- one incident record is present;
- the revision sequence is continuous (each old value equals the previous new value);
- the final revision value equals the incident's current death count (12);
- every revision source ID resolves to a source in the record;
- all source URLs use HTTP or HTTPS.

This is a structural/data consistency check, not a formal JSON Schema validator run. A dedicated schema-validation step should be added to the repository's test workflow before the ledger is used as the public source of truth.

## Important boundary

The ledger currently contains only the Dymer pilot incident. It is not a complete fatality inventory, and its current record count must not be summed or displayed as a project total. Do not connect it to the live dashboard yet.

## Next stage

Continue the historical reconciliation incident by incident. The first task is to reconcile the Nov. 23 subtotal and subsequent Nov. 24–26 increments against unique incident IDs, identify overlaps and duplicates, and add records with source-backed revisions. Only after the full inventory reconciles should the dashboard and chronology be generated from the dataset.
