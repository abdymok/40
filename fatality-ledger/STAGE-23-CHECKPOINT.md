# Fatality ledger — Stage 23 checkpoint

**Status:** Historical method sequence inspected; Nov. 3 and Nov. 11 count differences isolated  
**Date:** 2026-11-26  
**Public pages and incident data unchanged.**

## Source inspected

Read the live method page's fatality reconciliation section (current repository file: `method/index.html`, lines 84–135) and compared its dated cumulative increments with the pilot incident records.

## Confirmed method-to-record differences

### Chornomorsk, Nov. 11

The method page adds one death for the market strike, moving the running minimum from approximately 282 to 283. The incident record has a final toll of four: one initial death, then two hospital deaths (toll 1 → 3), then a further hospital death (3 → 4).

**Difference:** the incident record contains three more deaths than the method page's stated increment. The method page has not been updated to include the later deaths in its running total.

### Saltivsky district, Nov. 11

The method page says two people were killed, but moves the running minimum from approximately 283 to 284, a net increment of one. It notes that the mayor had earlier reported one death. The incident record preserves the sequence 1 → 2.

**Interpretation:** one Saltivsky death was already present in the subtotal before the paragraph; the later update contributes only the second death. The final incident total is two, not two new additions at this point. This is a timing/membership question, not evidence of a duplicate incident.

### Dnipro, Nov. 3

The method page adds one death in the morning Dnipro attack, moving approximately 207 to 208. The incident record preserves the regional administration's initial one-death report and its later update to two after the rescue operation (1 → 2).

**Difference:** the incident record contains one more death than the explicit method increment. The method page paragraph does not describe the later second death.

## Why the +18 remains unresolved

The Stage 20 decomposition remains a useful high-level comparison, but it is not yet a fully allocated record-level bridge. In particular:

- The pre-Oct. 29 incident inventory is 13 above the legacy 148 snapshot.
- Oct. 29 incident records are two above the 25-death increment to 173.
- The post-192 incident inventory is three above the method's stated 226 additions.

The newly confirmed Chornomorsk (+3) and Dnipro Nov. 3 (+1) differences alone account for four deaths. Saltivsky's final total of two must be handled as one death already in an earlier subtotal and one later increment. Other method paragraphs may contain additional count revisions, citywide aggregate overlap, or omissions that offset these differences. No balancing adjustment is justified without identifying the exact incident and source.

## Important guardrail

Do not set every `ledger_effective_at` equal to `recorded_at`. The latter is the source/report time preserved in the incident history; it is not proof that the project incorporated the death into its running subtotal at that moment. The historical cumulative paragraphs and repository revisions must establish that separately.

## Next audit sequence

1. Continue a paragraph-by-paragraph comparison of the method's running subtotal from 192 through 418 against each incident and revision.
2. Trace the Nov. 3 Dnipro second death and Nov. 11 Chornomorsk hospital deaths through subsequent method edits and change-log updates.
3. Resolve Saltivsky's first death's earlier inclusion point from the dated source and repository history.
4. Complete the same comparison for every Oct. 30–Nov. 26 incident before assigning effective dates.
5. Reconstruct the 148 baseline separately from the October source inventory.

No incident count, public figure, or historical snapshot was altered in this stage.
