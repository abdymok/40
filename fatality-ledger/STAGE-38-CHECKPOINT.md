# Stage 38 checkpoint — Nova Vodolaha revision chain resolved

Date: 26 November 2026

## Nova Vodolaha, Oct. 19

The earlier incident record had a misleading revision history: it went from three deaths directly to six, omitting the official correction to five on Oct. 19 and the later death of a 12-year-old boy on Oct. 26.

The source sequence is now represented:

1. Three deaths initially reported: two women and an infant.
2. Preliminary regional-administration update raised the toll to six.
3. Interfax-Ukraine reported the updated regional-administration figure of five, correcting the preliminary six.
4. On Oct. 26, 12-year-old Artem Koval died in a Kyiv hospital. The Nova Vodolaha community head reported the death through Ukrinform, bringing the final toll to six.

The incident description now records five deaths before Oct. 26 and the final sixth death on Oct. 26. It no longer describes an adult male victim in the five-death group. Conflicting reporting on the age of one of the girls is not repeated.

The revision history now records:
- null → 3, initial report;
- 3 → 6, preliminary figure;
- 6 → 5, official correction;
- 5 → 6, final death on Oct. 26.

The five-death figure was in the 141 subtotal; the sixth death entered the public subtotal on Oct. 27. Accordingly, `ledger_effective_at` is set to Oct. 26 for the five-death revision and Oct. 27 for the final six-death revision. The two preliminary revisions remain null because their temporary inclusion in the public subtotal is not established.

The source timestamps for Oct. 19 were corrected to Ukraine's then-current UTC+3 offset.

Sources:
- Hromadske, Oct. 19, 18:16: https://hromadske.ua/en/war/272811-russian-drone-strike-kills-baby-in-stroller-and-two-women-at-park-in-kharkiv-region
- Ukrinform, Oct. 19: https://www.ukrinform.ua/rubric-regions/4176027-udar-po-parku-na-harkivsini-kilkist-zagiblih-zrosla-do-sesti-troe-z-nih-diti.html
- Interfax-Ukraine, Oct. 19, 20:34: https://en.interfax.com.ua/news/general/1222801.html
- Ukrinform, Oct. 26, 17:22: https://www.ukrinform.net/rubric-ato/4178335-death-toll-from-russian-strike-on-park-in-kharkiv-region-rises-as-third-child-dies-in-hospital.html

## Current ledger and validation

- 170 incident records
- 401 source records
- 443 documented deaths
- 50 records through Oct. 28, summing to 166
- 25 revisions with non-null `ledger_effective_at`
- 192 revision entries remain null
- Structural/schema-equivalent validation: zero errors

The Nova Vodolaha correction changes no incident's final death count, so the total remains 443.

## Reconciliation

- Raw ledger: 443 versus published 418 (+25).
- Like-for-like comparison after Chabany (3) and Kharkiv market (1) scope adjustments: 447 versus 418 (+29).
- Pre-Oct. 29 raw inventory: 166 versus historical 148 (+18); like-for-like: 170 versus 148 (+22).
- Oct. 29: 27 versus historical 25 (+2).
- Post-192 additions: 231 versus method 226 (+5).

The post-192 +5 remains accounted for by Chornomorsk (+3), Dnipro on Nov. 3 (+1) and Saltivsky district (+1).

## Still unresolved

- The four-death Oct. 23 cross-region update still needs mapping to exact incident records.
- Two deaths in the Oct. 19–25 Kherson citywide weekly total remain unallocated.
- DTEK driver Vitalii Shcherbyna's Oct. 25 death is confirmed, but the mine location is not precise enough to resolve overlap with the regional casualty total.
- The Oct. 9 Kramatorsk OHCHR one-death lead remains without sufficiently specific local corroboration.
- The pre-Oct. 29 like-for-like difference of 22 still requires record-by-record allocation.

No public chronology, method page or dashboard figure was changed.
