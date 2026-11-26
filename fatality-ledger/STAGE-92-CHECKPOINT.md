# Stage 92 checkpoint — Oct. 10 Zaporizhia 20→23 revision

Date: 2026-11-26

## Evidence and timing

- The Oct. 11 ≈80 snapshot at commit `733a9b45892d232c5e0e2f2ac120f659ef58002b` explicitly records 20 deaths in the Oct. 10 Zaporizhia residential strike. REV-001 (—→20) is already dated Oct. 11.
- Ukrainska Pravda, citing the State Emergency Service and President Volodymyr Zelenskyy, reported the revised toll of 23 at 15:23 Kyiv time on Oct. 11.
- The subsequent page update at commit `b9ce46536bc5ecb7af0d9ec28b9f386f769df0fb`, timestamped 17:01 Kyiv time, still displayed ≈80 and did not say that the additional three deaths had entered the selected subtotal.
- The archived 80→92 increments do not name this +3 revision.
- The 148→173 historical breakdown does not itemize the additional three deaths. The 148 figure is a carried-forward aggregate rather than a complete incident-by-incident list.

## Adjudication

- REV-002 (20→23) remains `ledger_effective_at: null`.
- The first 20 deaths are confirmed in the Oct. 11 ≈80 baseline; the later three have no confirmed inclusion date.
- Later inclusion in the 148 baseline cannot be confirmed or ruled out.
- No incident count, source record or public total changed.

Public method-page minimum remains 421.