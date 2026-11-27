# Incident ledger

This directory contains the working incident-level dataset for the provisional non-combatant fatality count.

## Source of truth and current inventory

- `incidents.json` is the authoritative incident-level dataset.
- Current inventory: **182 incident records**, **442 source records**, **458 final documented deaths** and **237 revision entries**.
- Of the revision entries, **204 have a confirmed `ledger_effective_at` date** and **33 remain null**.
- The current public method-page and chronology subtotal is **427 through Nov. 26, 2026**.
- The raw incident-ledger sum exceeds the public subtotal by **31**. This is a disclosed reconciliation difference, not an additional batch to add to the public count and not a reason to alter either figure by balancing arithmetic.

The public subtotal is a historical running minimum built from dated project updates. It is not obtained by summing every final incident toll in `incidents.json`. The ledger includes documented final tolls and superseded interim revisions, later incident revisions, corrections and cases whose membership in the historical subtotal is not established.

### Historical reconciliation status

The public 421 subtotal was reconstructed as:

`148 + 19 + 25 + 229 = 421`

The Nov. 26 updates then raised the public minimum from 421 to 427. The detailed dated mappings are retained in the stage checkpoints, including Stages 44–52 and 103–106.

The 33 null `ledger_effective_at` values do **not** represent 33 unresolved incidents or 90 additional deaths:

- **12 entries** remain unresolved historical-inclusion questions, with a net arithmetic change of **+17**. Two later Lozova revisions (the third market death and the separate Oct. 24 warehouse death) are now classified as established exclusions from the 148 baseline and the 421 carry-forward. Their null effective dates are retained to distinguish exclusion from a dated addition. These are pre-Oct. 29 cases for which the surviving snapshots and change records do not establish whether a later carried-forward aggregate included the deaths.
- The other **21 entries** have been categorized as interim or superseded tolls, a downward correction not reflected in the historical subtotal, or established exclusions from that subtotal. In particular, Stage 106 closes all seven post-Oct. 29 null revisions as established exclusions from the 421 subtotal.
- Null is retained where no public-subtotal inclusion date is established. The revision's reason field and the relevant checkpoint state whether the case is unresolved, superseded, corrected or excluded.

Do not add the net arithmetic of null revisions to the public subtotal. Do not infer inclusion from incident date, source-publication date, chronology appearance or a later aggregate whose incident membership is incomplete. Do not impose a balancing adjustment.

## Scope rules

- The ledger records the documented final death toll for each incident, not injuries or people merely listed as missing.
- Military personnel are excluded.
- Police, rescuers and other non-combatant emergency personnel are included.
- A later death in hospital is a revision to the original incident, not a new incident.
- A corrected preliminary estimate is a revision, not an additional death batch.
- Regional or citywide month-to-date subtotals are not separate incidents and must not be added alongside the incidents they summarize.
- Potential overlaps and unsupported leads remain documented for review and are not silently added.

## Incident record fields

| Field | Meaning |
|---|---|
| `incident_id` | Permanent, unique incident identifier. Never recycle an ID. |
| `incident_date` | Date the attack or incident occurred, not the date the report was published. |
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
- `ledger_effective_at`: the date the project incorporated the change into its historical running subtotal; null when that inclusion date is not established or the revision was not counted separately
- `reason`
- `source_ids`

Never overwrite a prior count silently. Preserve the distinction between the incident's final documented toll and the date, if known, on which a revision entered the public subtotal.

## Validation

`incident.schema.json` defines the machine-readable record contract. Keep its field definitions and enumerations aligned with `scripts/validate_fatality_ledger.py` whenever the ledger structure changes.

Run:

```bash
python scripts/validate_fatality_ledger.py fatality-ledger/incidents.json
```

The validator checks unique incident and source IDs, required fields, location structure, evidence and scope classifications, source types and support labels, URL and date formats, revision continuity, effective-date formats, final count consistency and source references. It prints the calculated incident-level total.
