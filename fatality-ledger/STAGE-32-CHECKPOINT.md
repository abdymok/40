# Stage 32 checkpoint — revised +21 reconciliation arithmetic

Date: 26 November 2026

## Current ledger

- 167 incident records
- 386 source records
- 439 documented deaths
- Structural validation passed after the Oct. 29 Kyiv incident was added.
- No duplicate incident IDs or source IDs; no dangling revision-source references; all final revision values match final incident counts.

## Reconstructed historical sequence

The method page and original commits establish:
- Oct. 28 running subtotal: 148.
- Oct. 29–30 incident transition: +25, producing 173.
- The 173 transition comprised 14 initially reported deaths at Dnipro railway station, two in Chernihiv, three in Kremenchuk, one in Kyiv's late-evening ballistic attack, the later hospital death of a Dnipro railway-station victim, and four in the Oct. 29 Izium airstrike.
- Opening subtotal used for the Nov. 2 onward method sequence: 192. This included 18 deaths from the Komyshuvakha strike and the one Nov. 2 Izium death.
- Published method-page additions after 192: 226, producing 418.

## Current incident-inventory comparison

The current ledger groups by incident date as follows:
- Through Oct. 28: 162, versus the historical 148 (+14).
- Oct. 29: 27, versus the historical 25 (+2).
- Post-192 additions: 231, versus the method's 226 (+5).

Arithmetic: 162 + 27 + 231 = 420? No. The post-192 figure is calculated after allocating the 19 deaths already included in the 192 opening subtotal (18 Komyshuvakha and one Nov. 2 Izium death) from the 250 deaths attached to Oct. 30 onward. The 162 through Oct. 28 and 27 on Oct. 29 sum to 189; adding the 19 opening-subtotal deaths gives 208; adding 231 post-baseline deaths gives the current 439. The historical equivalent is 148 + 25 + 19 + 226 = 418. Difference: +14 +2 +5 = +21.

This is a final-inventory arithmetic comparison, not proof that every record in the first two incident-date groups had already entered the public subtotal on those dates. Historical inclusion timestamps remain to be assigned from commit and source chronology.

## Oct. 29 difference (+2) explained

The current Oct. 29 total of 27 comprises:
- Dnipro railway station: 15 (14 reported on Oct. 29 plus one later hospital death)
- Kremenchuk: 3
- Chernihiv: 2
- Kyiv ballistic attack: 1
- Izium public-health institution: 5
- Separate Izium attack killing a 59-year-old woman: 1

The historical 25 included the first five listed categories except that the Izium institution count was four. The +2 is therefore the fifth employee death in the institution strike and the separate 59-year-old woman. Neither appears in the 173 snapshot breakdown. The Kyiv fatality is now in the ledger and belongs to the historical 25.

## Post-192 difference (+5) explained

Three known incident-level differences account for the five:
- Chornomorsk, Nov. 11: four final deaths against a one-death method increment (+3).
- Dnipro, Nov. 3: two final deaths against a one-death method increment (+1).
- Saltivsky district, Nov. 11: two final deaths, but one had already been included in the preceding subtotal. The method adds only the second death; treating both as new creates +1.

The Komyshuvakha sequence is not a 72-death post-baseline addition: 18 were already in the 192 opening subtotal, and subsequent method revisions add the remaining 54.

## Remaining work

The main unresolved allocation is the +14 difference between the current final incident inventory through Oct. 28 (162) and the legacy subtotal (148). This includes final-count revisions to incidents that may have entered the public subtotal after their incident date. Reconstruct actual inclusion dates from original dashboard commits and source updates before populating `ledger_effective_at`.

The reconciliation note was updated in:
- `fatality-ledger/METHOD-TO-LEDGER-RECONCILIATION.md`

No public chronology, method page or dashboard number was changed.
