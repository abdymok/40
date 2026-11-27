# Stage 109 checkpoint — Lozova market final toll and historical exclusion

Date: 27 November 2026

## Scope

Reopen the Lozova Oct. 22 central-market incident after locating later local reporting that identifies two additional male victims. Distinguish those deaths from the separate Oct. 24 warehouse victim, update the incident-level record, and reassess historical inclusion in the 148 baseline and 421 carry-forward.

## New source findings

### Fourth market death — reported Oct. 24

Suspilne Kharkiv reported that the Oct. 22 market strike had killed four people after another injured man died. The article cites Lozova Mayor Serhii Zelensky's Oct. 24 statement. This is a death from the Oct. 22 market attack, not the separate warehouse strike.

The mayor's official Telegram post (https://t.me/Zelenskiy_Sergiy/12783) also distinguishes the warehouse victim from a man previously injured at the central market.

### Fifth market death — reported by Oct. 25

Ukrinform reported at 07:47 on Oct. 25 that another man injured in the Oct. 22 market strike had died in hospital. The mayor said the market attack had taken five lives. The same report separately describes the 45-year-old man killed in the Oct. 24 warehouse strike. These are distinct incidents and distinct victims.

The local final market toll is therefore five: three women and two men. The incident record now preserves 2→3→4→5. The evidence classification is updated to official_and_media, supported by the mayor's official Telegram post, Suspilne Kharkiv and Ukrinform.

## OHCHR cross-check

The OHCHR October update lists four deaths in the Oct. 22 market-area incident (two women and two men). Local reporting later establishes five (three women and two men). The four in the OHCHR report is not an unidentified extra casualty: the local sources identify the fourth and fifth victims as men. The remaining difference is one death in the reported totals and a difference in the sex breakdown. Preserve both source records and do not force a one-to-one victim match or import the OHCHR figure as an additional death.

## Historical public-subtotal membership

The Oct. 22 ≈123 baseline predates the third, fourth and fifth market deaths. The Oct. 26 132→137 transition explicitly includes only the two initial deaths at the market, alongside one death in Marhanets/Nikopol district, one in Konotop district and one in Yarova.

The later 137→148 transitions are itemized in Stages 54 and 100 and do not include the market's third, fourth or fifth deaths. All three later market revisions (2→3, 3→4 and 4→5) are therefore established exclusions from the Oct. 28 148 baseline and its 421 carry-forward. Their ledger_effective_at values remain null because they were not additions to the public subtotal.

The separate Oct. 24 warehouse death is also an established exclusion: it is not in the 123→132 or 132→137 itemized additions, and no later 137→148 update identifies it. It remains a separate one-death incident.

No market or warehouse death is added to the public 421 or 427 subtotal.

## Current ledger inventory

- 182 incident records.
- 445 source records.
- 460 final documented deaths when all incident-level records are summed.
- 239 revision entries: 204 with confirmed ledger_effective_at dates and 35 null.
- Null revisions have a net arithmetic sum of +92.
- Twelve historical-inclusion questions remain unresolved, net +17.
- The other 23 null revisions are categorized as interim/superseded tolls, a downward correction not reflected in the historical subtotal, or established exclusions.
- Public provisional minimum remains 427 through Nov. 26.

The two new market revisions add two to the raw incident-ledger sum and two null revision entries. The public subtotal is unchanged. The raw difference between the ledger sum and the public minimum is now 33; it is not a batch to add or subtract by balancing arithmetic.

## Change control

- The Lozova market incident's documented_deaths changes from 3 to 5, with two new sourced revisions (3→4 and 4→5).
- Its evidence classification changes from media_reported to official_and_media.
- Three new source records are added: Suspilne Kharkiv, the mayor's official Telegram post and Ukrinform.
- The existing third-death revision reason is clarified to record its exclusion from the public subtotal.
- The separate warehouse incident remains at one death and remains excluded from the public subtotal.
- No ledger_effective_at value is changed.
- No public chronology, dashboard or method-page fatality subtotal changes. Public minimum remains 427.

## Validation

The JSON structure, revision chain and source references must pass the repository's validate-fatality-ledger workflow after this commit. GitLab backup is also required. This checkpoint records the source adjudication; workflow status is reported separately after the runs complete.
