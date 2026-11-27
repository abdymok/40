# Stage 130 checkpoint — resolve Oct. 22 +2 and close five new inclusion questions

Date: Nov. 27, 2026

## Scope

Use the original Oct. 22 project update record and the exact official source to allocate the 121→123 increase, then carry the final Zaporizhia toll through the later 123→148, 148→421 and 421→427 bridges. Reclassify the five new Oct. 21–22 incident records added in Stage 129 where the historical bridge now establishes inclusion or exclusion.

## 121→123 +2: exact attribution

The Oct. 22 Zaporizhia Regional Military Administration post at https://t.me/zoda_gov_ua/68556 reported two people killed in a Russian strike on a private house: a 37-year-old man and his 38-year-old wife.

The archived dashboard commit `93499a33c356c6766545f03e12dabf513025cc56` is timestamped 2026-10-22 16:52:18 UTC. The contemporaneous project update at 16:53:38 UTC explicitly records these two Zaporizhia deaths as the +2 that raised the nationwide documented minimum from ≈121 to ≈123. This is direct attribution, not a numerical inference.

The two-death revision in `incidents.json` now has `ledger_effective_at: 2026-10-22`.

## Third death: established exclusion

Suspilne Zaporizhia reported the initial two deaths at 15:30 UTC on Oct. 22, then reported at 18:22 UTC that the toll had risen to three after a 69-year-old woman also died. The latter report came 90 minutes after the 121→123 commit.

The 123→132 increase of nine is fully allocated to four deaths in Synelnykove, one death in Kharkiv's Novobavarsky district, and four Oct. 23 incident-date deaths: one each in Chernihiv, Dnipro, Kramatorsk and Sloviansk. The itemized 123→148 additions do not add the third Zaporizhia victim. The mapped 148→421 bridge does not add her, and the six additions after the 421 minimum are separate Nov. 25–26 incidents.

The incident's revision history is now split: the initial two deaths are included effective Oct. 22; the third death remains null as an established exclusion from the public 427 minimum. No public total changes.

## Four other Oct. 21–22 incidents: established exclusions

Stage 129 added four further incident records: one death in Druzhkivka, one in Kramatorsk, one in Kushuhum, and two in a civilian-car strike between Komyshuvakha and Shchaslyve. Their incident identities and tolls remain in the structured ledger.

The 121→123 +2 is now allocated to the two Zaporizhia city victims. The 123→132 +4 is allocated to the four Oct. 23 incidents listed above. The itemized 123→148 increments contain no addition for these four Oct. 21–22 incidents; neither the mapped 148→421 bridge nor the six later 421→427 additions adds them. Their null effective dates are retained as established exclusions, not unresolved inclusions.

## Queue effect

Five Stage 129 queue entries are closed: the initial two Zaporizhia deaths are dated inclusions; the third Zaporizhia death and the four other new incident records are established exclusions. The historical-inclusion queue returns to 17 unresolved revision entries, net arithmetic +27. The remaining 17 questions are unchanged.

## Integrity

Current incident ledger: 191 incidents, 488 source records, 473 final documented deaths and 251 revision entries (205 dated, 46 null). The 46 null revisions have a net arithmetic value of +90; they are not 46 additional deaths to add to the public count. The raw incident-ledger sum exceeds the public minimum by 46, a reconciliation difference rather than a balancing instruction.

Public minimum remains 427 through Nov. 26, 2026. No public subtotal or chronology entry changes.

## Sources and records

- Zaporizhia Regional Military Administration, initial two-death report: https://t.me/zoda_gov_ua/68556
- Suspilne Zaporizhia, initial two-death report, 15:30 UTC: https://t.me/s/suspilnezaporizhzhya/63838
- Suspilne Zaporizhia, final three-death update, 18:22 UTC: https://t.me/s/suspilnezaporizhzhya/63846
- Dashboard commit changing ≈121→≈123: https://github.com/abdymok/40/commit/93499a33c356c6766545f03e12dabf513025cc56
- 123→132 bridge: `STAGE-129-CHECKPOINT.md` and the four Oct. 23 incident records in `incidents.json`
- 148→421 carry-forward: Stages 44–52 and 105–106