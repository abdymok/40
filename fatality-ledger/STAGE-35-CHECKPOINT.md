# Stage 35 checkpoint — schema and validator alignment

Date: 26 November 2026

## Problem found

The existing `incident.schema.json` did not describe the live dataset or the validator:
- Its evidence-classification enum used different labels from the README, validator and ledger.
- It omitted the live `ledger_effective_at` revision property.
- It omitted the live `non_combatant_security_personnel` scope value.
- It omitted source types already used in the ledger: `case_file`, `official_company_statement` and `international_monitoring_report`.
- It omitted two source-support labels already used by an OHCHR source: `evidence_classification` and `verification_status`.
- It required neither `notes` nor the ledger-effective field even though the validator/README expect them.
- Its `published_at` field did not allow the date-only values present in the source records.

## Corrections saved

Updated `fatality-ledger/incident.schema.json` to match the live record shape, allowed values and date representations. The schema now requires source notes and `ledger_effective_at` on every revision.

Updated `scripts/validate_fatality_ledger.py` to check:
- allowed scope classifications;
- allowed source types;
- allowed source-support labels;
- location object and required region/settlement fields;
- full ISO date or date-time validation for `published_at`;
- existing unique IDs, required fields, evidence classifications, URL format, revision continuity, ledger-effective dates, final count consistency and source references.

Updated `fatality-ledger/README.md` to identify the JSON Schema as the machine-readable contract and explain the expanded validator checks.

## Validation

A complete structural check mirroring the strengthened validator and the updated schema enums was run against the current JSON dataset. Result:

- Status: OK
- 168 incident records
- 390 source records
- 441 documented deaths
- 0 validation errors

All 390 source records have required notes and allowed source types/support labels. Every revision has a `ledger_effective_at` property (currently null where historical inclusion is not yet reconstructed). No duplicate IDs, broken revision chains or dangling source references were found.

The Python validator file was inspected after editing; its code now implements the same checks. The data/schema-equivalent check passed in this session.

## Relevant commits

- `77dd191e05f449ca784dc9f1e872b2c38dc955d7` — align schema enums and revision fields
- `05add3d57d5a025a00936afd67055833dd4fc9e8` — require source notes
- `989b2c75f60b00bac51f652a45d8255b98132bfe` — strengthen validator
- `db339a67da71e967ab282443ad41a448c9cf89fb` — document schema/validator contract
- `0fdeea0886882430c3e029fbc826b03a8c813673` — allow verification-status support labels
- `4466cf0e0a419f4f50d495f73c5cdf9307f43e6b` — align schema support enum

## Change control

No public chronology, methodology page or dashboard total was changed.
