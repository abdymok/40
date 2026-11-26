# Stage 63 checkpoint — Oct. 22 transition from selected-incident subtotal to nationwide minimum

Date: 26 November 2026

## Finding

The apparent 121→123 transition on Oct. 22 is not documented as two newly identified incident deaths. It is a change in the stated scope and method of the dashboard figure.

The preceding Oct. 22 commit `0f4dda082aba94f4f6c4a5b9279953cb4a0d17ac` revised the Chabany entry after corroboration and changed the selected-incident subtotal from approximately 118 to approximately 121. Its update-history text explicitly says the three Chabany deaths were included. The dashboard label remained a provisional selected-incident subtotal.

The next relevant commit, `93499a33c356c6766545f03e12dabf513025cc56` (Oct. 22, 16:52:18 UTC), changed the dashboard display from approximately 121 to approximately 123. The same diff changed the detail from “Official/media subtotal for selected incidents; provisional” to “Nationwide documented minimum from officially reported civilian deaths; incomplete.” It also rewrote the method paragraph from a selected-incident subtotal to a nationwide count of officially reported deaths. The commit did not add incident entries, cite two additional deaths, or itemize a +2 in the update history.

The subsequent commit `c3ce7dddf9d32e218fa13d77c4a0d44320e92bf4` clarified the update history to say the nationwide documented civilian-death count had been reconciled. The SOP change in `8814891624d013a92f5ad9439c0947ab55b173b2` describes the intended figure as a provisional nationwide documented minimum of officially reported civilian deaths, not a complete national total.

## Interpretation

The numerical difference of two is real in the displayed dashboard, but the repository evidence does not establish two particular deaths or incidents that explain it. The strongest supported interpretation is a scope expansion/reclassification: approximately 121 selected-incident deaths became an approximately 123 nationwide documented minimum. It is not safe to treat +2 as an incident-level addition or to assign it to any current ledger record.

This also explains why the 121→123 transition was not found as a pair of new incident rows in the current structured ledger. The historical dashboard was not consistently representing one fixed population: it moved from a selected-incident subtotal to a broader nationwide documented minimum.

The Oct. 22 selected-incident figure of 121 itself included the three Chabany deaths, which were later excluded from the current structured ledger because the source basis was judged insufficiently verified. This later scope correction is separate from the unexplained +2 transition and must not be conflated with it.

## Integrity and limits

- The historical commits above are the direct evidence for the change in label, method and displayed number.
- No source or incident is identified for the two-death numerical difference.
- Do not assign an effective date to +2.
- Do not backfill two placeholder deaths or invent incident records.
- Do not change the current public method-page minimum of 421.
- No current incident data, public counter or chronology entry was changed in this stage.

## Next follow-up

Continue backwards through the pre-Oct. 22 selected-incident subtotal. Keep the Oct. 22 scope switch distinct from later corrections and from the current structured-ledger scope.
