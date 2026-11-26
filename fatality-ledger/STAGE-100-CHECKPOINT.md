# Stage 100 checkpoint — classify the 27 pre-Oct. 29 null revisions

Date: 26 November 2026

## Objective

Reconstruct the incident-level composition of the Oct. 28 nationwide documented minimum of approximately 148, starting from the Oct. 22 scope change and the explicitly itemized Oct. 25–28 increments. The public 421 minimum remains frozen until a complete bridge is supported.

## Historical sequence established from repository commits

- Oct. 22, 10:17: dashboard moved to ≈118 after the Kyiv overnight attack toll was revised to one death.
- Oct. 22, 11:38: the Chabany entry was revised after corroboration; selected-incident subtotal moved ≈118→≈121.
- Oct. 22, 19:52: dashboard changed ≈121→≈123 while its label and method changed from a selected-incident subtotal to a nationwide documented minimum. The commit identifies no two additional deaths or incident-level increment. Stage 63 correctly treats this as a scope change, not a two-death incident addition.
- Oct. 25: the 123→132 update explicitly adds four deaths in Synelnykove, one in Kharkiv and four deaths reported across other regions on Oct. 23.
- Oct. 26: the 132→137 update adds five deaths reported in Nikopol district, Lozova, Sumy region and Yarova; the separate 137→138 update adds one death in Kramatorsk.
- Oct. 26: the 138→141 update adds three deaths in Pavlohrad, Kherson and Yasnohirka.
- Oct. 27: 141→142 adds one death in Kyiv; 142→143 adds the sixth Nova Vodolaha victim after the boy died in hospital; 143→146 adds three deaths reported by Donetsk regional administration.
- Oct. 28: 146→147 adds one death in Novodonetske; 147→148 adds one death in Kharkiv.

Sources for the sequence are the archived repository commits:
`4ada778321c66b570c73f8d5353617a076db8ee6`,
`0f4dda082aba94f4f6c4a5b9279953cb4a0d17ac`,
`93499a33c356c6766545f03e12dabf513025cc56`,
`d6cae076a8a9f6e5ef01f796d32a483723e18d08`,
`4817f634493b98f6d4f07ce0bd7b78ad386d8120`,
`738de54872c914d9d0fbde107923e479597dc62b`,
`36c741a248835baf9fadc6d087c3c29066f43d37`,
`e9adbbe64131938e45ec72dbc4ac4c4fe61fec27`,
`a927b2897d051e1a595f362289228823902c27fb`, and
`fb0d8ae4d5c0c27af974ce7a20e1672b28454c05`.

## Stage 100 adjudication: 12 of 27 classified

Twelve pre-Oct. 29 null revisions now have clearer explanations in `incidents.json`. Their `ledger_effective_at` fields remain null deliberately; none is assigned an invented public inclusion date.

### Nine interim toll revisions, not independent batches

- Pryluky: interim 14, 16 and 20 tolls. The final 22 is represented in the Oct. 11 ≈80 selected-incident snapshot.
- Kramatorsk two-bus strike: interim 12 and 30 tolls. The final 33 is represented in the Oct. 11 snapshot.
- Sloviansk Oct. 17 airstrikes: interim one- and six-death tolls. The Oct. 21 105→116 step explicitly adds the final nine deaths together with two Korotych deaths.
- Nova Vodolaha: initial three and superseded preliminary six. The corrected five-death toll is carried by the Oct. 26 ≈138 baseline; the sixth death is the explicit Oct. 27 142→143 addition.

These are successive descriptions of the same incidents, not additional groups of deaths. The interim values must not be summed on top of the final tolls.

### Two deaths known to be outside the 148 baseline

- Uman: the 86-year-old woman died on Oct. 26 after injuries sustained Oct. 21. The Oct. 26 and Oct. 27 itemized increments and the Oct. 28 148 sequence do not identify her. Her inclusion in the later 421 remains unproven.
- DTEK driver Vitaliy Shcherbyna: distinct Oct. 25 mine lorry strike. The Oct. 22 baseline predates the death, and the mapped Oct. 25–28 increments do not include him. The incident is in the ledger, not in the evidenced 148 baseline or 421 minimum.

### One public correction not applied

- Kharkiv market, Oct. 16: the public 95→98 increment added three. The later official clarification reduced the incident's final local toll to two, but the contemporaneous dashboard sequence contains no -1 subtraction. The public 148 baseline therefore appears to retain the initial three; the structured incident ledger correctly retains two. This is a known one-death difference between the two records, not a missing death to add.

## Remaining 15 revisions

The 15 remaining pre-Oct. 29 null revisions carry a net arithmetic change of +20. Their incident-level inclusion in the 148 baseline or later carry-forward is still unproven. They are:

1. Kramatorsk Oct. 5 residential-building death (+1).
2. Ivano-Frankivsk Oct. 8 drone-debris death (+1).
3. Unallocated Kyiv Oct. 8 morning death (+1).
4. Solomiansky shop strike third death (+1).
5. Synelnykove district Oct. 9 death (+1).
6. Zaporizhia Oct. 9 guided-bomb death (+1).
7. Zaporizhia Oct. 10 final toll revision 20→23 (+3).
8. Sloviansk Oct. 11 death (+1).
9. Kharkiv Kholodnohirsky Oct. 12 residential strike (+4).
10. Kyiv Darnytsky Oct. 12 residential strike, two revisions (+2).
11. Kherson Korabelny district Oct. 17 ambulance-driver death (+1).
12. Kyiv Oct. 21 ballistic death (+1).
13. Lozova Oct. 22 central-market third death (+1).
14. Lozova Oct. 24 warehouse-strike death (+1).

This list has 14 incident lines because the Darnytsky record has two separate null revisions; there are 15 revision entries in total. Their net arithmetic change is +20.

The next pass must test each remaining incident against the contemporaneous Oct. 22 118/121/123 snapshots, the Oct. 25 123→132 allocation, and the Oct. 26–28 itemized increments. Do not assign the Oct. 28 date simply because an incident predates the 148 snapshot.

## Integrity

- Current incident records: 176
- Current source records: 430
- Current final documented deaths in incident ledger: 452
- Revision entries: 231
- Null revisions overall: 34
- Pre-Oct. 29 null revisions: 27, net +83
- Pre-Oct. 29 revisions classified in this stage: 12, net +63
- Pre-Oct. 29 revisions still needing membership determination: 15, net +20
- Published Oct. 28 baseline: ≈148
- Current published minimum: 421, unchanged

No public chronology, dashboard, methodology figure or change-log entry was changed.
