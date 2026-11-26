# Stage 25 checkpoint — historical dashboard sequence and baseline bridge

Date: 26 November 2026

## Purpose

Continue reconstructing the fatality subtotal sequence from the contemporaneous dashboard and method-page history. This stage records what the historical text establishes, without changing incident records or public figures.

## Confirmed historical sequence

The contemporaneous dashboard update history and the current method-page reconciliation establish this sequence:

- **Oct. 27:** the working minimum moved from approximately 141 to 142 after one Kyiv death, then to 143 after a child died in hospital from injuries sustained in Nova Vodolaha, then to 146 after three Donetsk-region deaths (Sukhanivka, Kramatorsk and Iverske).
- **Oct. 28:** one Novodonetske death moved the subtotal to approximately 147; Kharkiv Mayor Ihor Terekhov's report of one death moved it to approximately **148**. The Iverske report was explicitly not counted again because that location had already appeared in the Oct. 27 update.
- **Oct. 29:** the Dnipro railway-station strike initially added 13 deaths, moving 148 to 161. Two Chernihiv deaths moved 161 to 163. Two preliminary Kremenchuk deaths moved 163 to 165.
- **Later Oct. 29–30 reporting:** revisions raised Kremenchuk to three and Dnipro railway station to 14, moving 165 to 167; one Kyiv death moved it to 168; the subsequent hospital death of a Dnipro railway-station victim moved it to 169; four Izium deaths moved it to 173.
- **Nov. 2:** one further Izium death moved 173 to 174. The Komyshuvakha subtotal was then added as 18, moving 174 to approximately **192**.
- **Nov. 3:** the Komyshuvakha figure was revised from 18 to 26, a net +8, while one Izium death had also been added. The contemporaneous dashboard therefore reported approximately **200**. Later that day, the Komyshuvakha count rose from 26 to 29 (+3), and the dashboard/method sequence reached approximately **203**.
- Subsequent method entries document the later increments through 418, but this stage does not attempt to recalculate those later dates.

## Important arithmetic correction and unresolved bridge

The current structured incident ledger contains 47 incident records dated on or before Oct. 28, with a sum of 162 deaths. The contemporaneous Oct. 28 dashboard baseline was 148. The difference is therefore **14**, not 13.

This is a comparison between two different things:
- 148 is the historical working subtotal actually published on Oct. 28.
- 162 is the sum of the current final incident-level values for records dated on or before Oct. 28.

The 14-death difference cannot be allocated safely by taking each incident's first revision value. Many records were revised before Oct. 28, others after it, and the ledger's revision history does not currently encode when each change entered the running public subtotal. The historical update prose confirms selected daily increments, but does not by itself reconstruct every component of the 148 baseline.

## Methodological findings retained

- The nine-death Dnipro citywide month-to-date statement was explicitly treated as a subtotal, not nine additional deaths on Oct. 29.
- The Oct. 27 Iverske death was not counted again on Oct. 28.
- Later revisions to Dnipro railway station and Kremenchuk were net changes to existing incident counts, not new incidents.
- The Nov. 2 Komyshuvakha change from 18 to 26 was a replacement (+8), not an additional 26. The subsequent 26→29 change was +3.
- The current incident ledger and historical public subtotal must not be forced to match by inventing a balancing adjustment.

## Work still required

1. Reconstruct which pre-Oct. 29 incident values were actually included in the Oct. 28 subtotal of 148.
2. Identify all pre-Oct. 29 incident revisions incorporated before and after that cutoff, using dated Git history and the chronology's own dated update text.
3. Reconstruct the exact transition from 148 to 173, including later revisions to Dnipro and Kremenchuk.
4. Reconcile the 174→192 Komyshuvakha replacement and the 192→203 sequence.
5. Only then compare the historical 203 subtotal with the subsequent source-audited additions and current incident ledger.

## Change control

No incident records, running totals, chronology text, dashboard values, or live pages were changed in this stage. This checkpoint is an audit note only.
