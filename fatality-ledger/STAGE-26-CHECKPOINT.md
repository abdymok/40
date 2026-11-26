# Stage 26 checkpoint — pre-Oct. 29 revision arithmetic

Date: 26 November 2026

## Scope

A record-level review of all 47 current incident records dated on or before Oct. 28. This stage isolates how the current ledger's first recorded values differ from its current final values. It does not claim that the first recorded values were the values used in the public dashboard.

## Recalculation

- Incident records dated on or before Oct. 28: **47**
- Sum of each record's first revision value: **113**
- Net effect of subsequent revisions within those records: **+49**
- Current final sum: **162**
- Historical dashboard subtotal published through Oct. 28: **148**
- Unexplained difference between current final sum and historical subtotal: **14**

The +49 net revision effect breaks down as follows:

| Incident | First value | Current value | Net change |
|---|---:|---:|---:|
| Kramatorsk, two buses, Oct. 8 | 12 | 33 | +21 |
| Pryluky, Oct. 7 | 14 | 22 | +8 |
| Sloviansk, Oct. 17 | 1 | 9 | +8 |
| Lutsk, Oct. 14 | 3 | 6 | +3 |
| Zaporizhia, Oct. 10 | 20 | 23 | +3 |
| Nova Vodolaha, Oct. 19 | 3 | 6 | +3 |
| Solomiansky district, Kyiv, Oct. 8 | 2 | 3 | +1 |
| Darnytsky district, Kyiv, Oct. 12 | 1 | 2 | +1 |
| Kyiv ballistic attack, Oct. 13 | 1 | 2 | +1 |
| Lozova, Oct. 22 | 2 | 3 | +1 |
| Kharkiv market, Oct. 16 | 3 | 2 | -1 |
| **Net revision effect** | | | **+49** |

All other records in this date range have a single recorded value and therefore no revision delta in the current file.

## What this does and does not establish

The 113 figure is a mechanical sum of the first values now present in revision histories. It is **not** a reconstructed Oct. 28 baseline. The current ledger was assembled and backfilled after the events, and the recorded timestamps in these records are not proof of when each item first entered the public running subtotal.

The public update history establishes that selected large revisions were incorporated during Oct. 7–23. However, the current record schema does not yet distinguish:
- first reported incident count;
- count after each source update;
- date the revision was incorporated into the running public subtotal;
- whether the incident was included in the 148 subtotal at the Oct. 28 cutoff.

The arithmetic therefore remains: 162 current final deaths versus 148 historically published, a 14-death gap. No allocation of that gap is justified yet.

## Next reconstruction step

Use the historical Git versions of the public chronology and dated update log to identify which incident records were already represented in the 148 subtotal, then compare those inclusions with the current 47-record set. Do not assume that every current pre-Oct. 29 record was included in the historical baseline.

## Change control

No incident record, method text, dashboard number, or public chronology was changed. This checkpoint records arithmetic and the unresolved historical-inclusion question only.
