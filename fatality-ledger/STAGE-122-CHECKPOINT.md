# Stage 122 checkpoint — Oct. 14 subtotal transition bridge

Date: Nov. 27, 2026

## Scope

Reconstruct the Oct. 14 selected-incident subtotal sequence from approximately 82 to 85, 89, 90 and 92. This is a transition-level audit of the published snapshots, not a new incident review. It does not change incident tolls, effective dates, or the current public minimum.

## Incident facts already established

- The Oct. 13 Desniansky residential-building strike killed three women. The first two deaths were reported overnight; the third was confirmed by the Kyiv City Prosecutor's Office at 08:50 on Oct. 14 and by Kyiv Police at 11:50.
- A separate strike in Holosiivsky district killed two people. Klitschko reported the first at 06:46; Kyiv Police confirmed the second in its 11:50 update.
- The Lutsk YevroHurt strike killed six people. The regional toll rose from three to four, then six.

The final Kyiv toll is five: three Desniansky plus two Holosiivsky. The final Lutsk toll is six. These are separate incidents.

## Reconstructed public snapshots

All times below are Kyiv time. Commit timestamps are UTC, converted to Kyiv time (UTC+3).

| Snapshot | Commit and time | Displayed subtotal | What the page said |
|---|---|---:|---|
| Baseline | `e394809`, Oct. 14 02:04 | ≈82 | The second Desniansky body had been found; the first two deaths were already included through 80→81→82. |
| First combined Kyiv update | `6096fa1`, Oct. 14 08:18 | ≈85 | Three Kyiv deaths: two in Desniansky and one in Holosiivsky. The two Desniansky deaths were already in the 82 baseline. Only one death was new. |
| Lutsk and revised Kyiv toll | `10a74ad`, Oct. 14 14:26 | ≈89 | Four deaths in Kyiv (three Desniansky, one Holosiivsky) and four in Lutsk. Relative to the 08:18 state, this represents one new Desniansky death plus four Lutsk deaths: five distinct additions, while the displayed subtotal rises by four. |
| Later Kyiv update | `fdbf975`, Oct. 14 14:37 | ≈90 | Five deaths in Kyiv (three Desniansky, two Holosiivsky) and four in Lutsk. The second Holosiivsky death is new; the displayed subtotal rises by one. |
| Final Lutsk update | `203f67d`, Oct. 14 16:48 | ≈92 | Five deaths in Kyiv and six in Lutsk. The two additional Lutsk deaths are new; the displayed subtotal rises by two. |

## Arithmetic finding

From the ≈82 baseline, the distinct additions described by the successive reports are:

1. One Holosiivsky death in the first three-death Kyiv report.
2. One further Desniansky death and four Lutsk deaths by the ≈89 snapshot.
3. One further Holosiivsky death by the ≈90 snapshot.
4. Two further Lutsk deaths by the ≈92 snapshot.

That is **nine distinct additions**. The published subtotal rises by ten, from ≈82 to ≈92. On the reconstructed transition sequence, the final Oct. 14 snapshot is therefore one death higher than the distinct-incident arithmetic: approximately 91 rather than 92.

The discrepancy is not simply a two-death duplicate. The 82→85 transition counted two Desniansky deaths a second time (+2), while the 85→89 transition's displayed +4 did not fully reflect the five distinct additions described in its updated Kyiv and Lutsk entries (−1). The remaining net difference is +1.

## Adjudication

This resolves the intermediate transition arithmetic, conditional on accepting the ≈82 baseline and the incident membership described in each dated snapshot. It does **not** by itself establish that the one-death excess flowed unchanged into the Oct. 28 ≈148 baseline or the later 421 carry-forward. Those later aggregates are not complete incident rosters, and the surviving transition records do not establish their exact membership.

- Do not change the current public minimum of 427.
- Do not change any incident toll or `ledger_effective_at` value.
- Do not change `incidents.json`.
- Carry this one-death Oct. 14 subtotal discrepancy into the remaining historical bridge audit. A correction to 427 requires direct evidence that the excess survived the later carry-forward, not arithmetic balancing against the raw ledger.

## Source and commit trail

- `b630f05` and `e394809`: the Oct. 13 Desniansky death updates, 80→81→82.
- `6096fa1`: 82→85, with two Desniansky deaths already in the baseline and one Holosiivsky death.
- `10a74ad`: 85→89, four Lutsk deaths and the revised four-death Kyiv description.
- `fdbf975`: 89→90, five deaths in Kyiv.
- `203f67d`: 90→92, six deaths in Lutsk.
- Kyiv Police, Oct. 14, 11:50: https://kyiv.npu.gov.ua/news/kilkist-zahyblykh-vnaslidok-vorozhoho-udaru-po-stolytsi-zbilshylasia-do-piaty-osib-politsiia-kyieva
- Volyn Regional Military Administration, Lutsk toll 3→4: https://t.me/volynskaODA/11356 and https://t.me/volynskaODA/11357
- Six-death Lutsk update: https://glavnoe.in.ua/en/news-en/death-toll-in-lutsk-rises-to-six-as-another-body-is-found-under-wholesale-store-rubble

## Integrity

No public page, dashboard figure, incident record, or fatality total was changed in this stage. The current public provisional minimum remains 427 through Nov. 26.
