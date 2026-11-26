# Baseline gap and change-log reconciliation — Nov. 21–23

**Status:** Stage 4 — reconciliation finding, no public data changed  
**Repository state:** The three earlier audit files remain saved. This checkpoint adds the next set of discrepancies.

## 1. The 374 → 377 → 379 progression is now explained

The methodology history resolves the apparent gap. The sequence is:

- **374 through Nov. 21:** after adding two deaths in Kryvyi Rih to the 372 subtotal through Nov. 20.
- **377 through Nov. 21:** add one death in Nikopol district and two deaths in Zaporizhia/Zaporizhia district, as reported by the two regional administrations.
- **378 through Nov. 22:** the first confirmed Dymer death, a woman whose body was recovered from the rubble.
- **379 through Nov. 22:** the second confirmed Dymer death, an 18-year-old man whose body DSNS reported recovered at 14:52 on Nov. 22.

This is preserved in the historical methodology commits:
- `53ad3461608b` contains the 374 → 377 update.
- `5152843e599f` contains the first Dymer death, 377 → 378.
- `ec4d6af92df0` contains the second Dymer death, 378 → 379.

**Finding:** the 379 baseline is supported. It already includes exactly two Dymer deaths, as the later reconciliation assumes. The prior apparent +2 gap was caused by reading the Nov. 21 subtotal without the two subsequent Dymer updates.

## 2. Nov. 22 +12 reconciliation: what is actually listed

The methodology paragraph's six incident groups do add to 12 if all listed figures are accepted:

| Incident | Addition |
|---|---:|
| Dymer: two already counted → seven | +5 |
| Vyshneve supermarket | +3 |
| Bila Tserkva district | +1 |
| Dnipro | +1 |
| Novoslobidska community | +1 |
| Zaporizhia enterprise | +1 |
| **Total** | **+12** |

The Zaporizhia enterprise death is separately present in the Nov. 22 chronology: a guided aerial bomb killed a 40-year-old man. It is absent from the corresponding Nov. 23 change-log paragraph that enumerates the other five groups.

This explains one missing death in the change log's first subtotal:
- Its Nov. 23 reconciliation paragraph lists Dymer +4 (two already counted to six), Vyshneve +3, Bila Tserkva +1, Dnipro +1 and Novoslobidska +1. These add to **+10**, giving 379 → 389.
- A separate update raises Dymer from six to seven: **+1**, giving 389 → 390.
- The separately recorded Zaporizhia enterprise fatality contributes the remaining **+1**, giving 390 → 391.

The methodology paragraph instead groups Dymer's full rise from two to seven (+5) and the enterprise death with the other incidents, presenting the consolidated 379 → 391 total. The historical edit that established this corrected total is commit `1a24eec76281`. Its patch explicitly adds the Zaporizhia enterprise fatality and revises the Nov. 22 subtotal from 390 to 391, then revises the subsequent Dymer progression from 390 → 394 to 391 → 395.

This identifies the source of the stale one-death difference in the change log: the 40-year-old worker killed in the Zaporizhia enterprise strike was missing from the earlier Nov. 22 change-log enumeration. The methodology later incorporated him, but the change log's intermediate arithmetic was not fully updated.

## 3. Dymer intermediate arithmetic in the change log

The change log has:
- 379 → 389 for the Nov. 22 incident additions as itemized above, excluding the final Dymer update and Zaporizhia enterprise fatality;
- 389 → 390 for the 22:52 Dymer update from six to seven;
- 392 → 394 for the Nov. 23 Dymer update from nine to 11.

The final line is inconsistent with the earlier arithmetic. If the project subtotal after Nov. 22 was 391, then the Nov. 23 interim progression should be:
- 391 → 393 when Dymer rises from seven to nine;
- 393 → 395 when Dymer rises from nine to 11.

The change log's 392 → 394 line is one below the methodology/chronology baseline at both ends. This is not a separate incident count. It is a cumulative-baseline error or a missing one-death reconciliation immediately before that update. No evidence located so far explains it.

## 4. Other source corrections captured

- Vyshneve: Ukrainska Pravda's Nov. 22 20:44 report explicitly records the final toll of three, after earlier updates of one and two. Count the incident once at three.
- Novoslobidska: the current chronology says the boy was 15, while an earlier syndicated report said 14. The regional administration's Nov. 23 update is cited in the chronology as correcting the age to 15. Age does not affect the death count.
- Dymer: the Nov. 23 recovery operation ended at 11 deaths; the woman rescued alive died in hospital on Nov. 24, making 12 for the incident. Do not count her on Nov. 23.

## 5. What remains to be done

1. Retain the 379 baseline as supported: it includes the two initial Dymer deaths.
2. Retain the Zaporizhia enterprise worker as a separate +1 incident addition on Nov. 22. The method history incorporates him in commit `1a24eec76281`, while the earlier change-log breakdown omits him.
3. Correct the change-log's stale Dymer intermediate arithmetic in the eventual synchronized display update. Given the 391 subtotal through Nov. 22, the 7 → 9 update should be 391 → 393 and the 9 → 11 update should be 393 → 395, not 392 → 394.
4. Continue the incident-by-incident reconciliation forward from the Nov. 23 subtotal of 405, before calculating any project-wide sum.

**No live totals, chronology entries, method text or published change-log text have been edited.** This checkpoint records audit findings only. The historical repository commits were inspected to resolve the previously open 377 → 379 question.
