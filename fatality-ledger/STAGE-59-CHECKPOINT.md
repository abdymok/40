# Stage 59 checkpoint — Oct. 14–15 Kyiv and Lutsk casualty sequence

Date: 26 November 2026

## Reconstructed subtotal transitions

| Historical transition | Increment | Incident mapping | Evidence |
|---|---:|---|---|
| 82→85, Oct. 14 | +3 | First three deaths reported in Kyiv's overnight Oct. 13–14 attack: two in Desniansky district and one in Holosiivsky district | Commit `6096fa1309044424382b309e2545033c8b017eec` adds the consolidated attack report and changes 82 to 85 |
| 85→89, Oct. 14 | +4 | Initial Lutsk attack toll confirmed by Volyn National Police | Commit `10a74ad99f3fb3911689965e6449fe41ded0c772` adds four Lutsk deaths and changes 85 to 89 |
| 89→90, Oct. 14 | +1 | Fourth death in the Oct. 14 Kyiv attack, reconciling the later official toll | Commit `fdbf9759933d6119841de42baf50ab0c03f19a2b` changes 89 to 90 and updates the methodology note to at least five Kyiv deaths overall |
| 90→92, Oct. 15 | +2 | Lutsk toll revised from four to six | The Oct. 15 update history preserved in commit `1535e91b64e569338ad26b9283b9ed436cb6f8fb` explicitly says the later Volyn regional-administration report raised Lutsk from four to six, increasing the subtotal from 90 to 92 |
| 92→95, Oct. 15 | +3 | Three people killed in the large Russian attack on Kirovohrad region | Commit `12ec18d5f902d58a59de878b5b8c0ddeff86d3ef` explicitly raises 92 to 95 |

## Method/dashboard lag identified

At the 89 snapshot after the Lutsk addition, the method paragraph already lists four deaths in Kyiv and four in Lutsk, but the dashboard is still 89. The next commit raises the dashboard to 90 and the method paragraph now says at least five deaths in Kyiv and four in Lutsk. This is consistent with the dashboard catching up by one death to the four-death Oct. 14 Kyiv toll. The contemporaneous chronology update had first reported three deaths in the consolidated Kyiv overnight attack, then the Kyiv Prosecutor's Office later reported four.

The Oct. 15 snapshot at 92 still has a method paragraph showing 90, despite the update history explicitly saying Lutsk was revised from four to six and the dashboard rose to 92. The Kirovohrad update then brings both the dashboard and method paragraph to 95.

These are method-text lag points, not changes to the current incident ledger. The dashboard increments are supported by the archived update history and displayed values.

## Scope and data handling

- Lutsk's incident toll is six in the later regional-administration report, not four plus six.
- The Kyiv Oct. 14 incident's four-death toll replaces the earlier three-death report; it is not a separate additional incident.
- The Oct. 13 Kyiv ballistic-attack deaths remain a separate incident.
- No incident records or revision histories changed.
- No `ledger_effective_at` values changed.
- The public subtotal remains untouched.

## Next work

1. Continue backward from the 82 subtotal into the Oct. 13 and Oct. 12 casualty updates.
2. Establish the exact incident membership of the 82 baseline, including the Kyiv Oct. 13 strike revisions and Kharkiv's Oct. 12 fourth body.
3. Continue toward the earliest October baseline only where contemporaneous records can support inclusion dates.
