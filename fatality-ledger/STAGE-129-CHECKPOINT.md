# Stage 129 checkpoint — Oct. 21–22 casualty reports and the unallocated +2

Date: Nov. 27, 2026

## Scope

Investigate the Oct. 22 121→123 scope change and the Oct. 25 123→132 update using contemporaneous official regional and police reports. Add source-backed incident records where the reports identify distinct incidents, but do not assign historical inclusion dates without a direct project record.

## Five new incident records

Five incident records have been added to `incidents.json`, covering eight documented deaths:

1. Druzhkivka, Oct. 21 — one resident killed by an FPV drone. The National Police reports the death.
2. Kramatorsk, overnight into Oct. 22 — one person killed in the private sector, according to the National Police.
3. Kushuhum, Oct. 21 — a 68-year-old man killed by a guided aerial bomb. Zaporizhia regional administration and police identify the incident.
4. Road between Komyshuvakha and Shchaslyve, Oct. 21 — a couple killed when an FPV drone struck their civilian car. Zaporizhia regional administration and police identify the incident.
5. Zaporizhia, Oct. 22 — three people killed by a missile strike near a private residential area. The initial report gave two deaths; the regional police and administration confirmed the final toll of three on Oct. 23.

These are distinct incidents, not duplicate descriptions of the same regional daily totals. Each new revision has `ledger_effective_at: null` pending historical-subtotal adjudication.

## The 121→123 +2 is not uniquely attributable

The National Police reported one person killed in Druzhkivka by an FPV drone and one person killed overnight in the private sector of Kramatorsk. Separately, Filashkin's Oct. 21 daily toll, published on Oct. 22, reports two people killed in Kostiantynivka. That Kostiantynivka pair is an exact +2 and was reported before the 121→123 commit. The same reporting window also includes three deaths in Zaporizhia region and two initial deaths in the Oct. 22 Zaporizhia city strike.

But other official reports were also available before the 121→123 commit:

- Filashkin's Oct. 22 morning operational report recorded two people killed in Kostiantynivka. This is a regional daily aggregate and does not identify the precise incidents, so it is not added as a separate incident record here.
- Zaporizhia regional authorities and police reported three deaths from Oct. 21 attacks: one in Kushuhum and two in the civilian-car strike between Komyshuvakha and Shchaslyve.
- On the afternoon/evening of Oct. 22, Zaporizhia authorities initially reported two deaths in a strike near private homes. The final toll rose to three, confirmed on Oct. 23.

The 121→123 commit does not cite or allocate its +2 to any of these reports. The Kostiantynivka pair is the clearest exact-two candidate, but the Donetsk and Zaporizhia reports are competing contemporaneous cases. None is uniquely attributable. Do not set an effective date for any of these incidents on the strength of the +2 alone.

## The 123→132 +4 across other regions

The Oct. 25 update describes four deaths across other regions reported on Oct. 23, without naming incidents. The three deaths in the Oct. 22 Zaporizhia city strike were confirmed by police on Oct. 23 and are a possible fit. The update does not identify them, so no inclusion date is assigned. The other three Zaporizhia-region deaths from Oct. 21 are not explicitly identified in the 123→132 allocation either.

## Adjudication

- Add the five distinct, officially sourced incident records and preserve their final tolls: 1, 1, 1, 2 and 3.
- Keep all five new revision entries null for historical inclusion.
- Treat the two Kostiantynivka deaths as a plausible but unproven match to 121→123 +2; the Donetsk pair and Zaporizhia incidents remain competing contemporaneous reports.
- Do not assign the 121→123 +2 to the Kostiantynivka daily aggregate or any Zaporizhia incident without direct evidence.
- Treat the three Zaporizhia city deaths as a possible, unproven match to the four deaths reported across other regions on Oct. 23 in the 123→132 update.
- Public minimum remains 427 through Nov. 26, 2026. No public subtotal changes.

## Integrity

Current incident ledger: 191 incidents, 485 source records, 473 final documented deaths and 250 revision entries (204 dated, 46 null). The historical-inclusion queue now has 22 unresolved revision entries, net arithmetic +35. The raw incident-ledger sum exceeds the public minimum by 46; this is a reconciliation difference, not a batch to add or subtract.

## Sources

- Vadym Filashkin, Donetsk Regional Military Administration, Oct. 22, reporting two deaths in Kostiantynivka for Oct. 21: https://t.me/VadymFilashkin/18815
- Filashkin's Oct. 22 morning operational report, also recording two deaths in Kostiantynivka: https://t.me/s/VadymFilashkin?before=11919
- National Police of Ukraine, Donetsk region, Oct. 22: https://npu.gov.ua/news/dvi-liudyny-zahynuly-sered-9-poranenykh-dity-politsiia-donechchyny-dokumentuie-naslidky-rosiiskykh-atak
- Ivan Fedorov, Zaporizhia Regional Military Administration, Oct. 22: https://t.me/ivan_fedorov_zp/49091
- Zaporizhia regional police, Oct. 22 report: https://t.me/s/police_zp_news/27348
- Ivan Fedorov, Zaporizhia Regional Military Administration, Oct. 23: https://t.me/ivan_fedorov_zp/49097
- Zaporizhia regional police, Oct. 23: https://npu.gov.ua/news/na-zaporizhzhi-cherez-rosiiski-ataky-zahynulo-troie-liudei-shche-odna-otrymala-poranennia-politsiia-dokumentuie-naslidky-voiennykh-zlochyniv