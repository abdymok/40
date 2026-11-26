# Stage 34 checkpoint — Korotych omission and baseline scope differences

Date: 26 November 2026

## Ledger change

Added the missing Oct. 21 Korotych mass-drone-attack incident:
`UA-KHA-KOROTYCH-2026-10-21-MASS-DRONE-STRIKE`

Two civilians were killed: an 81-year-old woman and an 83-year-old man. The regional police report, Interfax-Ukraine, Ukrinform and Suspilne independently corroborate the two deaths. Eleven people who suffered acute stress reactions are not included in the death count.

Sources:
- Kharkiv Regional Police, Oct. 21, 10:08: https://npu.gov.ua/news/dvoie-liudei-zahynuly-shche-24-postrazhdaly-sered-yakykh-dity-politseiski-zadokumentuvaly-naslidky-voiennykh-zlochyniv-voroha-na-kharkivshchyni
- Interfax-Ukraine, Oct. 21, 07:21: https://interfax.com.ua/news/general/1223556-amp.html
- Ukrinform, Oct. 21, 06:23: https://www.ukrinform.net/rubric-ato/4176518-russian-drones-attack-settlement-in-kharkiv-region-killing-two.html
- Suspilne Kharkiv: https://suspilne.media/kharkiv/1432687-korotic-unoci-buv-pid-masovanim-udarom-zaginuli-dvoe-ludej-ponad-10-postrazdali/

The Oct. 22 historical method note explicitly included the two Korotych deaths. The current structured ledger had omitted them. The incident is now represented; no public subtotal was changed.

## Current ledger validation

- 168 incident records
- 390 source records
- 441 documented deaths
- No duplicate incident IDs
- No duplicate source IDs
- No broken revision-to-source references
- Every final revision value matches its incident's final documented-death count

## Historical baseline comparison

Current pre-Oct. 29 incident-date inventory: 164 deaths across 48 records.
Historical Oct. 28 published subtotal: 148.
Raw difference: +16.

Three scope differences now need to be retained alongside the arithmetic:
- Korotych (two deaths) was in the historical Oct. 22 method note and is now added to the current ledger.
- Chabany (three deaths) was explicitly included in the Oct. 28 historical dashboard subtotal but remains excluded from the current ledger under the later working exclusion.
- The Oct. 22 method note listed three deaths in Kharkiv on Oct. 16. The current ledger retains the later official final count of two. No corresponding downward adjustment was found in the Oct. 28 change log, so the historical subtotal is provisionally treated as carrying three.

For a like-for-like comparison only, add the three Chabany deaths and one Kharkiv market death to the current pre-Oct. 29 inventory: 164 + 3 + 1 = 168 versus 148, a +20 difference. These comparison adjustments do not authorize adding Chabany to the ledger or reverting the Kharkiv final count.

## Overall comparison

- Raw current ledger: 441
- Published method-page minimum: 418
- Raw difference: +23
- Like-for-like comparison after the two scope adjustments: 445 versus 418, or +27

The +27 decomposes arithmetically into:
- Pre-Oct. 29 like-for-like difference: +20
- Oct. 29 incident-date difference: +2
- Post-192 additions difference: +5

The post-192 +5 is accounted for by Chornomorsk (+3), Dnipro on Nov. 3 (+1) and Saltivsky district (+1, because one of its two deaths was already in the preceding subtotal).

This remains an arithmetic comparison, not a final allocation of every death to the date it entered the public subtotal. The pre-Oct. 29 +20 still requires record-by-record reconstruction of historical inclusion and later revisions.

## Change control

Updated `fatality-ledger/METHOD-TO-LEDGER-RECONCILIATION.md`.

No public chronology, methodology page or dashboard figure was changed.
