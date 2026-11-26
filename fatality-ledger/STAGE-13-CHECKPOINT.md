# Fatality ledger — Stage 13 checkpoint

**Status:** Nov. 18–21 incident records entered  
**Date:** 2026-11-26  
**Public pages unchanged.**

## Records added

Nine incident records were added for Nov. 18–21:

- Nov. 18: one woman killed in a separate FPV strike in Kushuhum.
- Nov. 19: one woman killed in Horenychi, Kyiv region.
- Nov. 19: one person killed in a drone attack on Kyiv's Podilsky district.
- Nov. 19: one person killed in overnight attacks on energy and civilian facilities in Chernihiv region. The prime minister's report did not identify the settlement or specific facility.
- Nov. 20: seven people killed in the Kyiv ballistic-missile attack. The record preserves the successive tolls of 3 → 6 → 7; the figures are not added together.
- Nov. 20: two people killed in the strike on Sknyliv railway station in Lviv.
- Nov. 20: two people killed in the ballistic strike on Kryvyi Rih, a seven-year-old boy and a 20-year-old paramedic.
- Nov. 20: one person killed in attacks on Nikopol district. The regional summary did not identify the exact settlement or strike site.
- Nov. 20–21: two people killed in attacks across Zaporizhia city and district over the 24 hours before the Nov. 21 regional bulletin. The source did not allocate the deaths to individual locations or strikes, so the record is explicitly a source-defined attack cluster.

The Nov. 20 Nikopol death and the two Zaporizhia deaths account for the three additions that move the historical minimum from 374 through Nov. 20 to 377 through Nov. 21. The incident dates are Nov. 20, even though the regional reports were published on Nov. 21.

## Kyiv ballistic revision history

The Nov. 20 Kyiv incident record preserves:
- 07:27: initial report of three deaths;
- 10:32: Prime Minister's update raises the toll to six;
- 15:32: Kyiv Mayor Klitschko raises the toll to seven.

The cumulative arithmetic adds the first three once, then three more, then one more. It does not add 3 + 6 + 7.

## Data status and validation

The pilot dataset now contains:
- 98 incident records;
- 229 documented deaths across those records;
- 236 source records.

The 229 is a partial dataset sum, not the national/project total. Most of the remaining work is now the Oct. 1–Nov. 1 source inventory and the Nov. 22 incident batch, plus final cross-checks for duplicate or missing deaths.

Structural checks confirmed:
- unique incident IDs and source IDs;
- continuous revision histories;
- each record's final revision equals its documented death count;
- no dangling source references.

## Open arithmetic issues carried forward

- Dnipro, Nov. 3: the final source count is two, while the method's running addition records one.
- Chornomorsk, Nov. 11: the final source count is four, while the method adds only the initial one. The later three deaths need to be checked against the subsequent cumulative chain.
- Nov. 16–18 sequence reconciles through 358 when the first Zaporizhia industrial-attack death, the two Obolon deaths, the third Chernihiv death, and the Odesa fourth death are all placed at their actual update points.
- The Nov. 22 Zaporizhia enterprise death and the separate morning report of one death in Zavodskyi district need to be matched carefully to ensure they are one incident, not two.

No public figures or pages have been changed.
