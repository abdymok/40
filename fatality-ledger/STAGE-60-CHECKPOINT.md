# Stage 60 checkpoint — Oct. 12–14 Kyiv and Kharkiv sequence

Date: 26 November 2026

## Reconstructed subtotal transitions

| Historical transition | Increment | Incident mapping | Evidence |
|---|---:|---|---|
| 80→81, Oct. 13 | +1 | One person killed in the Oct. 13 Kyiv ballistic strike on a residential building and CHP-4 | Commit `b630f05c50a0aa7459815a4e63b16e662f63b791` changes the dashboard from 80 to 81 and explicitly attributes the addition to Klitschko's report of one death |
| 81→82, Oct. 13–14 | +1 | A further body recovered after the Oct. 13 Kyiv ballistic strike | Commit `e394809eb026530afc1933ccf9514483a740fb1f` changes 81 to 82; its method paragraph identifies the further body, based on the compiler's report, and flags the lack of a linked published source |
| 82→85, Oct. 14 | +3 | Two people killed in Desniansky district and one in Holosiivsky district in the Oct. 13–14 Kyiv overnight attack | Commit `6096fa1309044424382b309e2545033c8b017eec` changes 82 to 85 and records three deaths in the consolidated district-level update |

## Kharkiv Oct. 12 evening strike: fourth death and baseline uncertainty

The Oct. 12 Kharkiv evening strike initially had three bodies recovered. On Oct. 13 at 11:41, Mayor Ihor Terekhov reported recovery of a fourth body. Commit `fe3278d0874258aa5e073ce1ca77dd348dcdbca3` updates the chronology entry from three to four deaths but leaves the dashboard at approximately 80.

The later 80, 81 and 82 snapshots retain the four-death Kharkiv chronology entry. However, the method paragraph at the 80 baseline does not itemize this incident. The evidence therefore confirms that the chronology toll was corrected before the 80→81 and 81→82 updates, but does not independently prove whether the fourth Kharkiv death was already included in the 80 subtotal or whether the counter failed to move when it should have. Do not assign a separate effective date from the chronology update alone.

## Oct. 14 Kyiv casualty revision

The 82→85 update initially described three deaths in the consolidated overnight Kyiv attack. A later commit `98d925d4950664529ea0002835076ae7e06fabeb` updates the method paragraph to four deaths in Kyiv on Oct. 14, while leaving the dashboard at 85. Stage 59 shows that the fourth death was eventually reflected in the 89→90 transition, after the four-death Lutsk addition. This is a one-death method/dashboard lag, not an additional incident.

## Data handling

- No incident records or revision histories changed.
- No `ledger_effective_at` values changed.
- The compiler-reported further death after the Oct. 13 Kyiv strike remains a source/evidence caveat in the historical method record; no new source was added here.
- The public subtotal remains untouched.

## Next work

1. Reconstruct the 80 baseline's incident membership from the Oct. 11 snapshot and earlier change history.
2. Resolve whether the fourth Kharkiv Oct. 12 death entered the 80 baseline or was omitted from the dashboard arithmetic.
3. Continue backward through the 80 subtotal only where the historical dashboard and source records establish inclusion.
