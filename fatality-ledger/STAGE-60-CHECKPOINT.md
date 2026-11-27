> **Superseded in part by Stage 115 (Nov. 27, 2026):** Stage 60's 82→85 mapping treated the Oct. 14 three-death citywide report as a fresh +3 after the 80→81→82 increments had already counted the first two deaths in the Desniansky building. The Oct. 13 Desniansky and Oct. 14 Holosiivsky records are now separated: three deaths in Desniansky and two in Holosiivsky. The 82→85 dashboard transition is under review for duplicate inclusion; no guessed correction has been applied to the public 427. Retain the original checkpoint below as the historical state of the audit.

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

The Oct. 11 ≈80 baseline predates the Oct. 12 Kharkiv attack, so the four Kharkiv deaths cannot have been part of that baseline. The later Oct. 13 snapshots still display ≈80 after the Kharkiv incident was added to the chronology and its toll was updated to four. The 80→81 and 81→82 dashboard commits then explicitly attribute their +1 increments to the Oct. 13 Kyiv ballistic strike and the further body recovered after that strike; neither mentions Kharkiv. This establishes that no separate Kharkiv increment is visible in the dashboard change history. Because the displayed total is approximate and the method does not enumerate all incident membership, we cannot prove whether a rounded recalculation absorbed some or all of the four deaths, or whether they were omitted. Treat this as a potential four-death inclusion gap, not a confirmed +4 adjustment. Do not assign a separate effective date from the chronology update alone.

## Oct. 14 Kyiv casualty revision

The 82→85 update initially described three deaths in the consolidated overnight Kyiv attack. A later commit `98d925d4950664529ea0002835076ae7e06fabeb` updates the method paragraph to four deaths in Kyiv on Oct. 14, while leaving the dashboard at 85. Stage 59 shows that the fourth death was eventually reflected in the 89→90 transition, after the four-death Lutsk addition. This is a one-death method/dashboard lag, not an additional incident.

## Data handling

- No incident records or revision histories changed.
- No `ledger_effective_at` values changed.
- The compiler-reported further death after the Oct. 13 Kyiv strike remains a source/evidence caveat in the historical method record; no new source was added here.
- The public subtotal remains untouched.

## Next work

1. Reconstruct the 80 baseline's incident membership from the Oct. 11 snapshot and earlier change history.
2. Resolve whether the four Kharkiv Oct. 12 deaths were incorporated into the later ≈80 display after the incident was added, or remained outside the running subtotal.
3. Continue backward through the 80 subtotal only where the historical dashboard and source records establish inclusion.
