# Stage 107 checkpoint — final ledger integrity and public-subtotal audit

Date: 27 November 2026

## Scope

Final read-only audit of the current incident ledger, the historical running-subtotal reconciliation, and the public chronology/dashboard/method figures. The audit preserves the incident dataset and public count.

## Current inventory

The current `fatality-ledger/incidents.json` contains:

- 182 incident records.
- 442 source records.
- 458 final documented deaths when all incident-level records are summed.
- 237 revision entries: 204 with a confirmed `ledger_effective_at` date and 33 null.
- The dated revision changes have a net arithmetic sum of +368.
- The null revision changes have a net arithmetic sum of +90.

The raw incident-ledger sum of 458 is not the public running subtotal. The public subtotal remains **at least 427 through Nov. 26**. The 31-death difference is disclosed and remains a reconciliation difference; it is not a discrete incident batch and must not be added to or subtracted from the public subtotal by balancing arithmetic.

## Structural and reference checks

A programmatic read-only check of the current JSON found:

- No duplicate incident IDs.
- No duplicate source IDs across the ledger.
- No duplicate revision IDs.
- No broken revision chains.
- Every final revision value matches its incident's `documented_deaths`.
- Every revision source reference resolves within its incident.
- All source URLs use HTTPS.

No structural defect was found in the current dataset. The repository's Python validator remains the authoritative repeatable check and is run by `.github/workflows/validate-fatality-ledger.yml` on changes to the ledger directory or validator.

## Historical reconciliation

The public 421 subtotal is reconstructed in the stage checkpoints as:

`148 + 19 + 25 + 229 = 421`

The Nov. 26 public updates add six separately documented deaths, taking the subtotal from 421 to 427. The Nov. 26 chronology and method-page text also retain two reports outside the subtotal pending clarification: a later Kharkiv regional description of a woman killed at a private house, which may refer to the university-strike victim, and a Kherson regional roundup that does not identify the fatal incident.

The 33 null effective-date entries are not 33 unresolved deaths and their +90 arithmetic must not be added to 427:

- Fourteen pre-Oct. 29 entries remain unresolved historical-inclusion questions, net +19. The surviving snapshots and change records do not establish whether later carried-forward aggregates included these deaths.
- The other 19 entries have been categorized as interim or superseded tolls, a downward correction not reflected in the historical subtotal, or established exclusions. Stage 106 closes all seven post-Oct. 29 null revisions as established exclusions from the 421 subtotal.
- A null effective date is therefore not synonymous with an unverified incident or an open inclusion question. The revision reason and relevant checkpoint record the disposition.

The Nov. 21–26 public additions are itemized in Stages 51–52 and the Nov. 26 update record. In particular, the formerly flagged 372→374 Kryvyi Rih step is explicitly mapped in Stage 51, and the 390→391 Zaporizhia enterprise death is included in the five-death 379→391 allocation. The 391→421 sequence is itemized in Stage 52. No unexplained arithmetic jump was identified in the reviewed 372→427 sequence.

## Public-facing synchronization

The current files agree on the principal public figures and cutoff:

- Chronology title and reporting update: through Nov. 27.
- Dashboard deaths: at least 427, through Nov. 26.
- Method-page reconciliation: at least 427 through Nov. 26.
- Changes page: 421→426 for five separately documented deaths, then 426→427 for the Zaporizhia Dnipro-district death.
- Kyiv air-alert dashboard: 404 completed alerts and 316 hours, 10 minutes, 46 seconds through the Nov. 27 03:46 all-clear.
- The Nov. 27 metro restriction entry is present at the top of the chronology.

The two casualty reports held pending overlap/incident identification are not added to the public fatality subtotal.

## Change control

- `incidents.json`: **not changed**.
- Incident count, source count, revision values, final incident tolls and effective dates: **not changed**.
- Public fatality minimum: **remains 427**.
- Dashboard, chronology incident entries and method-page arithmetic: **not changed**.
- `fatality-ledger/README.md`: clarified the current inventory, the 31-death raw-ledger/public-subtotal difference, the 14 unresolved historical-inclusion questions, and the dispositions of the other null revisions. Removed duplicated and stale explanatory text.

## Closeout

The current structural checks found no ledger integrity defect. Historical public-subtotal membership remains unresolved for the 14 pre-Oct. 29 entries described above; those questions are disclosed and no balancing adjustment is made. The incident-level ledger and public subtotal remain separate measures until the remaining scope, overlap and historical-membership questions are resolved with evidence.
