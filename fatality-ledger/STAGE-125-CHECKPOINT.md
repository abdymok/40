# Stage 125 checkpoint — Oct. 12 Kharkiv and Darnytsky historical membership

Date: Nov. 27, 2026

## Scope

Complete the follow-up audit promised after Stage 124: test the four-death Kharkiv Kholodnohirsky residential strike and the two-death Kyiv Darnytsky residential strike against the original ≈80 snapshot, the Oct. 12–14 80→92 updates, and the Oct. 28 ≈148 baseline description.

This is a historical-subtotal membership check. It does not revisit the established incident tolls.

## Source chronology and snapshot findings

### Oct. 11 ≈80 baseline

The archived Oct. 11 snapshot, commit `733a9b45892d232c5e0e2f2ac120f659ef58002b`, predates both incidents. It cannot include either the Oct. 12 Kharkiv strike or the Oct. 12 Darnytsky strike.

The page continued to display ≈80 on Oct. 12 and through most of Oct. 13. The existence of the incident entries in the chronology did not itself trigger a dashboard subtotal update.

### Oct. 12–14 transition

The only named death-bearing changes from ≈80 through ≈92 are:

- 80→81→82: the Oct. 13 Desniansky attack in Kyiv.
- 82→85: the Oct. 13–14 Kyiv overnight attack; the two Desniansky deaths were already counted, leaving one new Holosiivsky death.
- 85→89: the third Desniansky death and four Lutsk deaths, with the already-counted Desniansky victims repeated in the descriptive update.
- 89→90: the second Holosiivsky death.
- 90→92: two additional Lutsk deaths.

Neither the four Kharkiv Kholodnohirsky deaths nor either Darnytsky death is named in these transition updates. The dashboard remained ≈80 on Oct. 12 and during the Oct. 13 daytime chronology additions, so no contemporaneous subtotal update proves inclusion there.

### Oct. 28 ≈148 baseline

The Oct. 28 page describes the nationwide documented minimum as including:
- the previously recorded Kyiv death;
- the Oct. 19 Nova Vodolaha death;
- three deaths reported by Donetsk regional administration on Oct. 27;
- one death in Novodonetske;
- one death in Kharkiv on Oct. 28;
- and, in the methodology paragraph, three deaths in Kharkiv on Oct. 16, six in Lutsk on Oct. 14, three in Kirovohrad region on Oct. 15, and at least five earlier deaths reported in Kyiv.

It does not identify the Oct. 12 Kholodnohirsky incident or the Oct. 12 Darnytsky incident. The phrase “at least five earlier deaths reported in Kyiv” is not a sufficiently specific incident roster to match either Darnytsky death. Nor does the omission prove exclusion: the ≈148 baseline is a carried-forward aggregate, and the page itself says other reports remain under reconciliation.

The later 148→173 breakdown also does not name either incident. That breakdown is a list of additions after the 148 baseline, not a full membership roster.

## Incident-level adjudication

### Kharkiv, Kholodnohirsky district — four deaths

The final toll of four is supported by the Kharkiv Regional Military Administration and Suspilne Kharkiv. The incident occurred after the ≈80 baseline and is not named in the 80→92 additions or the Oct. 28 ≈148 description. Inclusion in the carried-forward 148 remains unproven; exclusion is also unproven.

Keep REV-001 `ledger_effective_at: null`. This remains a potential four-death membership gap, not a confirmed omission.

### Kyiv, Darnytsky district — two deaths

The final toll of two is supported by the Kyiv City Prosecutor's Office and Ukrinform. The incident occurred after the ≈80 baseline and neither death is named in the 80→92 additions or the Oct. 28 ≈148 description. The generic “at least five earlier deaths reported in Kyiv” wording does not identify the Darnytsky victims. Inclusion in the carried-forward 148 remains unproven; exclusion is also unproven.

Keep both REV-001 and REV-002 `ledger_effective_at: null`. They are two deaths in one incident, not separate incidents.

## Decision

No direct evidence of historical inclusion or exclusion was found for either incident. The existing null effective dates remain correct. Do not add six deaths to 427 and do not subtract any number from 427.

The public provisional minimum remains 427 through Nov. 26. The 17-entry historical-inclusion queue remains open, with net arithmetic +27. No incident toll, source record, revision value, public chronology or dashboard figure changed in this stage.

## Integrity

- Incident ledger remains 186 incidents.
- Source records remain 477.
- Final documented deaths remain 465.
- Revision entries remain 245 (204 dated, 41 null).
- Public provisional minimum remains 427.
