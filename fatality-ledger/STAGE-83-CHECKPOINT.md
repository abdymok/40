# Stage 83 checkpoint — Uman death and the 148/192 baselines

Date: 2026-11-26

## Finding

The current ledger records the death of 86-year-old Tamara Yasynska from injuries sustained in the Oct. 21 Uman strike. Cherkasy Regional Military Administration head Ihor Taburets reported the death on Oct. 26.

The historical dashboard sequence shows:

1. **Oct. 26 ≈138 snapshot** — commit `4817f634493b98f6d4f07ce0bd7b78ad386d8120`, at 08:10 UTC, predates the Uman death report (10:05 UTC).
2. **Oct. 26 ≈138→≈141** — commit `738de54872c914d9d0fbde107923e479597dc62b` explicitly adds three deaths in Pavlohrad, Kherson and Yasnohirka. It does not add Uman.
3. **Oct. 26–28 ≈141→≈148** — subsequent updates itemize one Kyiv death, one Nova Vodolaha hospital death, three Donetsk deaths, one Novodonetske death and one Kharkiv death. None identifies Uman.
4. **Nov. 2 ≈148→≈174** — the expanded dashboard detail itemizes 25 additional deaths from the Oct. 29 Dnipro, Chernihiv, Kremenchuk, Kyiv and Izium incidents, followed by one further Izium death. It does not identify Uman.
5. **Nov. 2 ≈174→≈192** — commit `5d54c0fc36e2f8f8a22e3793122a2393b0402315` explicitly adds 18 deaths in Komyshuvakha. It does not identify Uman.
6. The current public dashboard update-history block contains no Uman, Tamara or Yasynska entry.

The evidence establishes that Uman was not in the 148 baseline and was not explicitly added in the 148→174 or 174→192 transitions. It does not prove whether Uman was folded into the later 421 minimum through a broader, non-itemized update.

## Changes made

- Uman REV-001 remains `ledger_effective_at: null`.
- Updated its reason text to record the negative baseline evidence and the unresolved later 421 inclusion.
- Updated the unresolved inventory category to “Not in 148; later 421 inclusion unproven”.
- No incident count, source record, effective date or public figure changed.

## Updated ledger status

- Incidents: 175
- Source records: 428
- Final documented deaths: 451
- Revision entries: 230
- Revisions with confirmed effective dates: 193
- Revisions still null: 37
- Remaining pre-Oct. 29 null revisions: 30, net +89
- Later null revisions: 7, net +8
- Public method-page minimum: 421 (unchanged)
