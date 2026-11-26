# Incident ledger

This directory contains the working incident-level dataset for the provisional non-combatant fatality count.

## Source of truth

- `incidents.json` is the authoritative incident dataset.
- `incidents.json` is authoritative for the incident-level documented-death inventory. Its current raw sum is 458 across 182 incident records.
- The current public method-page subtotal is 427 as of Nov. 26, 2026. It is a historical running subtotal, not yet identical to the raw incident-ledger sum because 31 deaths remain subject to scope, overlap or historical-inclusion reconciliation.
- `ledger_effective_at` records when a revision entered the historical running subtotal. A null value means the inclusion date is not established or the revision is not counted separately pending overlap/scope review.
- Do not derive a public dashboard number by summing all `documented_deaths` until the remaining eligibility and overlap differences are resolved.
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

Historical totals such as 123, 148, 192 and 418 are retained as legacy snapshots in audit notes. The current public method-page snapshot is 421 through Nov. 26, 2026. They are not authoritative data and must not be used as current totals. Historical membership and ledger-effective dates are being reconstructed separately. The raw incident-ledger sum and the public running subtotal must be displayed as separate measures until their difference is fully reconciled.

## Validation

`incident.schema.json` defines the machine-readable record contract. Keep its field definitions and enumerations aligned with `scripts/validate_fatality_ledger.py` whenever the ledger structure changes.

Run:

```bash
python scripts/validate_fatality_ledger.py fatality-ledger/incidents.json
```

The validator checks unique incident and source IDs, required fields, location structure, evidence and scope classifications, source types and support labels, URL and date formats, revision continuity, ledger-effective dates, final count consistency and source references. It prints the calculated total.
