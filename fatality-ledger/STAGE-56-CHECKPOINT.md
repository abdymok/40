# Stage 56 checkpoint — Oct. 21 dashboard/method mismatch

Date: 26 November 2026

## Correction from Stage 57

The direct HTML snapshot comparison has refined the finding. At the Oct. 21 09:16 snapshot, commit `679cd4c4e1541842a3794c72b7d583e5deea1f1a`, both the dashboard and the method paragraph say approximately 105, and the method paragraph explicitly includes the two Sviatoshynsky deaths.

The later `3c205e7cb516ca3a9843c1234b23ff05408bf6dc` commit changes the dashboard alone from approximately 105 to approximately 107. It leaves the method paragraph at 105 and leaves its Sviatoshynsky attribution untouched. Thus the prior Stage 56 statement that the 107-snapshot method paragraph could not prove baseline membership was incomplete: the 105 snapshot itself proves those deaths were already included before the +2 dashboard-only change.

The likely interpretation is that the intermediate 105→107 step duplicated the two Sviatoshynsky deaths. The following 107→116 step is +9 even though the updated method paragraph adds nine Sloviansk deaths and two Korotych deaths (+11). The two anomalies offset, making the overall 105→116 endpoint increase +11, equal to the Sloviansk and Korotych deaths together.

## What remains unresolved

The evidence strongly suggests an erroneous intermediate dashboard transition rather than an incorrect 116 endpoint. It does not yet establish why the +9 step was recorded as nine rather than eleven, or whether the original update arithmetic was deliberately netted against the prior duplicate. Do not change the public 421 or ledger effective dates on this basis alone.

See `STAGE-57-CHECKPOINT.md` for the complete snapshot comparison.
