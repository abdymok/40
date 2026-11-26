# Incident ledger

This directory contains the working incident-level dataset for the provisional non-combatant fatality count.

## Source of truth

- `incidents.json` is the authoritative incident dataset.
- The current cumulative total is the sum of `documented_deaths` across eligible incident records. No page or dashboard should maintain its own total.
- A regional or citywide month-to-date subtotal is not a separate incident and must not be added alongside the incidents it summarizes.
- Injuries and people merely listed as missing are excluded.
- Military personnel are excluded. Police, rescuers and other non-combatant emergency personnel are included.
- Unresolved possible duplicates and unsupported leads are kept in separate audit notes, not silently added to the total.

## Incident record fields

| Field | Meaning |
|---|---|
| `incident_id` | Permanent, unique incident identifier. Never recycle an ID. |
| `incident_date` | Date the attack/incident occurred, not the date the report was published. |
| `location` | Settlement, district, region and country. Use null where the source does not establish a more precise location. |
| `incident_description` | Concise description distinguishing the incident from nearby or same-day attacks. |
| `documented_deaths` | Current final number of deaths supported by the record's sources. |
| `scope_classification` | Civilian/non-combatant scope. |
| `evidence_classification` | Summary classification derived from the source types. |
| `sources` | Source records with unique IDs, publisher, type, publication time, URL, claims supported and notes. |
| `last_verified_date` | Date the incident record was last checked against its sources. |
| `revision_history` | Append-only history of every count change. |

## Evidence classification

- `official_and_media`: at least one official source and at least one media report.
- `official_only`: one or more official sources, without a media report.
- `media_reported`: media reports only.
- `monitoring_or_case_file`: monitoring report or case file, without official or media source types.
- `project_record_only`: project record only.
- `unverified`: no qualifying source type.

This is a source/evidence summary, not a guarantee that every claim has been independently verified. The source-level `source_type`, `supports` and `notes` fields retain the actual evidentiary basis.

## Revision history

Each revision must preserve:
- `old_value`
- `new_value`
- `recorded_at`: the report/update time associated with the revised information, where known
- `ledger_effective_at`: the date the project incorporated the change into its running total; null until reconstructed from the historical change log
- `reason`
- `source_ids`

Never overwrite a prior count silently. A later death in hospital is a new increment to the same incident, not a new incident. A corrected preliminary estimate is a revision, not an additional death.

## Historical snapshots

Historical totals such as 123, 148, 192 and 418 are retained as legacy snapshots in audit notes. They are not authoritative data and must not be used as current totals. Historical membership and ledger-effective dates are being reconstructed separately. The final current total must always be calculated from the incident records.

## Validation

Run:

```bash
python scripts/validate_fatality_ledger.py fatality-ledger/incidents.json
```

The validator checks IDs, required fields, date formats, revision continuity, final count consistency and source references. It prints the calculated total.
