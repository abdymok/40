# Stage 40 checkpoint — source conflicts and CI validation

Date: 26 November 2026

## Current ledger

- 172 incident records
- 411 source records
- 445 documented deaths
- 52 records through Oct. 28, summing to 168
- 29 revision entries with non-null `ledger_effective_at`
- 190 revision entries remain null

The actual Python validator ran in GitHub Actions and passed. Run:
https://github.com/abdymok/40/actions/runs/45796020791

The successful job includes the step `Validate ledger and revision history`. The schema-equivalent check in this session also returned zero errors.

## Nova Vodolaha source conflict

The final toll remains six. The contemporaneous regional updates record the sequence 3 → preliminary 6 → corrected 5 → final 6 after a 12-year-old boy died in hospital on Oct. 26. The October OHCHR monitoring report independently lists six civilians killed.

Ukraine Evidence Hub case-file v3 carries a conflicting seven-death headline and narrative. It is now retained in the incident's source list as a conflicting case-file figure, not adopted over the contemporaneous regional updates and OHCHR count. The final count and historical subtotal mapping remain unchanged.

## Kharkiv Oct. 28 age discrepancy

The 38-year-old man in the Oct. 29 24-hour Kharkiv report is the same person killed in the Oct. 28, 12:55 Osnoviansky district postal-branch strike already recorded in the ledger. Earlier city/regional reporting gives age 60; the prosecutor's office and later 24-hour report give 38. The existing incident record already contains the source conflict. The unresolved Kharkiv weekly note now explicitly excludes this Oct. 28 death from the Oct. 19–25 weekly window. No duplicate record was added.

## Historical reconciliation status

The Oct. 23 four-death batch is mapped to Dnipro, Kramatorsk, Chernihiv and Sloviansk. The Chernihiv and Sloviansk records were added in Stage 39. The Oct. 25 update from 123 to 132 is now mapped to four Synelnykove deaths, one Kharkiv Novobavarsky death and the four Oct. 23 locality deaths.

The Oct. 26 132→137 five-death update remains less precisely allocated. The working mapping is Marhanets, Lozova, Konotop and Yarova. The third Lozova death remains without a confirmed public inclusion date.

## Remaining unresolved leads

- Two deaths in the Oct. 19–25 Kharkiv citywide weekly total remain unallocated. The Oct. 28 Osnoviansky death is outside this window.
- DTEK driver Vitalii Shcherbyna's Oct. 25 death is confirmed, but the mine location is not precise enough to resolve overlap with the regional casualty total.
- The Oct. 9 Kramatorsk OHCHR one-death lead remains without sufficiently specific local corroboration.
- The precise inclusion date of the third Lozova death remains unresolved.
- The pre-Oct. 29 like-for-like difference of 24 is provisional pending that allocation and other remaining incident-by-incident checks.

## CI and deployment

- Fatality-ledger Python validation: successful.
- GitLab backup for the same head: successful.
- GitHub Pages deployment for the same head: pending at checkpoint time.

No public chronology, method page or dashboard figure was changed.
