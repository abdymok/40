# Stage 55 checkpoint — October 21–22 legacy subtotal chain

Date: 26 November 2026

## Reconstructed changes

The archived dashboard commits establish this sequence before the 123 baseline:

| Historical transition | Increment | Incident mapping | Status |
|---|---:|---|---|
| 105 → 107 (Oct. 21) | +2 | Two people killed in the Oct. 21 drone strike on a residential high-rise in Kyiv's Sviatoshynsky district | Identified in the contemporaneous commit and incident record; ledger effective date remains null pending 148-baseline membership proof |
| 107 → 116 (Oct. 21) | +9 | Sloviansk Oct. 17 strike final toll and two Korotych deaths | Public change-log identifies both elements, but their precise arithmetic allocation is not yet proven from the 107 baseline |
| 116 → 117 (Oct. 22) | +1 | Lymanivka, Kharkiv region: one woman killed | Identified in the Oct. 22 commit and incident record; effective date remains null |
| 117 → 118 (Oct. 22) | +1 | Kyiv Dniprovsky district: one person killed in the overnight Oct. 21–22 attack | Identified in the Oct. 22 update text and incident record; effective date remains null |
| 118 → 121 (Oct. 22) | +3 | Chabany drone attack: three deaths, newly corroborated by Kyiv Regional Military Administration, regional police and independent reporting | Explicitly documented in the commit; the three deaths remain excluded from the current structured ledger under the later scope decision |
| 121 → 123 (Oct. 22) | +2 | No incident-level allocation in the commit or update-history diff | Unresolved; do not infer |

## Important arithmetic caution: 107 → 116

The Oct. 21 update-history text says the subtotal rose from 107 to 116 after the Sloviansk toll reached nine, and that the two Korotych deaths were included. The earlier 107→116 dashboard change is +9. The current Sloviansk incident record has a revision history of 1→6→9, but that alone does not reveal how much of its toll was already carried in the 107 subtotal. The original 107 baseline's membership is not individually itemized. Do not assume +7 Sloviansk plus +2 Korotych until the earlier 105→107 allocation and initial Sloviansk subtotal are reconciled from the archived Oct. 17–21 changes.

The 105→107 commit is explicitly titled as a Kyiv casualty update and the following Oct. 21 history says two people were killed in Sviatoshynsky district. This identifies the +2 as that incident. It does not, by itself, establish all the other incident membership in 107.

## 123 baseline implication

By the 123 snapshot, the historical public tally explicitly includes:
- two deaths in Kyiv's Sviatoshynsky district (added 105→107);
- two deaths in Korotych (identified in the 107→116 update);
- one death in Lymanivka (116→117);
- one death in Kyiv's Dniprovsky district (117→118);
- three deaths in Chabany (118→121).

The 123 snapshot still has two unexplained additions from 121. The 123→132 and later transitions are documented separately in STAGE-54-CHECKPOINT.md.

## Data handling

No ledger_effective_at fields were changed. The Sviatoshynsky, Sloviansk, Lymanivka and Kyiv Dniprovsky records remain null because their inclusion in the 148 baseline must still be proven from the full original subtotal sequence. Chabany remains excluded from the current ledger. No public totals or final incident counts were changed.

## Next priority

Reconstruct the Oct. 17–21 sequence to determine what the 105 baseline contained and how much of the Sloviansk toll was already counted before Oct. 21. Then resolve the unidentified +2 between 121 and 123. Do not change the public 421 subtotal.