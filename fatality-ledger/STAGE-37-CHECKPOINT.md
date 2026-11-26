# Stage 37 checkpoint — missing historical deaths added and inclusion dates started

Date: 26 November 2026

## Two missing records added

The Oct. 26 historical change entry raised the running subtotal from 138 to 141 with one death each in Pavlohrad, Kherson and Yasnohirka. The ledger already contained the Pavlohrad DTEK miner, but omitted the Kherson and Yasnohirka deaths. Both are now added:

1. `UA-KHE-KHERSON-2026-10-25-MINIBUS-DRONE-STRIKE` — one 67-year-old man died in hospital after a Russian drone struck a passenger minibus in Tsentralnyi district on Oct. 25. Official Kherson city/regional administration posts, Ukrinform, Ukrainska Pravda and Ukraine Evidence Hub corroborate the death.
2. `UA-DON-YASNOHIRKA-2026-10-26-STRIKES` — one person killed and 10 injured in four strikes on Yasnohirka on Oct. 26. Ukrinform, Hromadske and Euromaidan Press corroborate the death and cite the Kramatorsk City Military Administration / Donetsk Regional Military Administration.

Both records have `ledger_effective_at: 2026-10-26`, matching the historical 138→141 subtotal update. These are not new deaths relative to the historical 148; they were missing from the structured ledger.

## Inclusion dates assigned

Twenty-three revision entries now have confirmed `ledger_effective_at` dates, based on explicit historical subtotal or method-page entries:

- Oct. 22: Korotych two deaths; the preliminary three-death Kharkiv market count.
- Oct. 25: four Synelnykove deaths and one Kharkiv Novobavarsky death.
- Oct. 26: Marhanets, the first two Lozova deaths, Konotop, Yarova, Kramatorsk, Pavlohrad, Kherson and Yasnohirka.
- Oct. 27: one Kyiv death and one death each in Iverske, Kramatorsk and Sukhanivka.
- Oct. 28: one Novodonetske death and one Kharkiv Osnoviansky death.
- Oct. 30: one Kyiv ballistic-attack death in the 173 transition.
- Nov. 3: the first Dnipro death in the method increment.
- Nov. 11: the first Chornomorsk death and both Saltivsky deaths, with the first already present in the preceding subtotal.

Later revisions remain null where the method page did not add them: the Kharkiv market correction from three to two, the third Lozova death, the later Chornomorsk toll increases and the later Dnipro death. The Nova Vodolaha revision is also left null because the current incident source sequence conflicts with the method page's separate report of a 12-year-old boy dying in hospital and raising the subtotal by one.

## Current ledger and validation

- 170 incident records
- 398 source records
- 443 documented deaths
- 50 incident records through Oct. 28, summing to 166
- 23 revisions with non-null `ledger_effective_at`
- 192 revision entries remain null
- Full structural/schema-equivalent validation: zero errors

## Reconciliation arithmetic

- Raw pre-Oct. 29 inventory: 166 versus historical 148 (+18).
- Like-for-like pre-Oct. 29 comparison, adding three Chabany deaths and the one Kharkiv market death retained in the historical subtotal but excluded/corrected in the current ledger: 170 versus 148 (+22).
- Oct. 29: 27 versus historical 25 (+2).
- Post-192 additions: 231 versus method 226 (+5).
- Raw overall difference: 443 versus 418 (+25).
- Like-for-like overall comparison: 447 versus 418 (+29).

These figures are reconciliation arithmetic, not an approved replacement for the public method-page total.

## Still unresolved

- Nova Vodolaha: current source record shows a six-death toll on Oct. 19, while the method page later records a 12-year-old boy's death as a one-death increase to six. Resolve the victim identity and incident mapping before assigning effective dates.
- Two additional deaths in the Oct. 19–25 Kherson citywide weekly total remain unallocated.
- DTEK driver Vitalii Shcherbyna's Oct. 25 death is confirmed, but the mine location is not precise enough to resolve overlap with the regional casualty total.
- The Oct. 9 Kramatorsk OHCHR one-death lead remains without sufficiently specific local corroboration.
- The four-death Oct. 23 cross-region update still needs mapping to exact incident records.

No public chronology, method page or dashboard figure was changed.
