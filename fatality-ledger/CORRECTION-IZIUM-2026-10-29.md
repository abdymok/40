# Correction: two separate Izium incidents on Oct. 29

**Saved:** 2026-11-26  
**Commit:** 8c5d7f857e1fd248ac7aacd83a425df540ed07ef

A source-level review showed that two separate Russian attacks in Izium on Oct. 29 had been conflated in the first ledger pass.

## Incident A: public-health institution strike — five deaths

Russian guided bombs struck the local branch of the Center for Disease Control and Prevention, killing five employees and injuring 14.

- The project dashboard displayed four deaths on Oct. 30.
- Interfax-Ukraine reported five employees killed at 20:16 on Oct. 30.
- The incident record now preserves **4 → 5**.
- Sources: [Interfax-Ukraine](https://en.interfax.com.ua/news/general/1229008.html), [Ukrinform](https://www.ukrinform.net/rubric-regions/4179271-russian-airstrike-on-izium-kills-five-employees-of-public-health-center.html), and [the Oct. 30 project dashboard commit](https://github.com/abdymok/40/commit/2056133993).

## Incident B: separate attack on Izium — one death

Ukrainska Pravda reported on Oct. 31 that a 59-year-old woman had been killed in a separate Russian attack on Izium on Oct. 29, while a 57-year-old woman was injured.

- This is not the public-health institution strike.
- A separate one-death incident record has been restored.
- The earlier one-death regional roundup is attached as corroboration, with its location limitation retained.

Source: [Ukrainska Pravda, Oct. 31](https://www.pravda.com.ua/eng/news/2026/10/31/8060604/index.amp).

## Effect on the pilot dataset

The previous pilot count of 421 included five deaths at the public-health institution but had absorbed the separate 59-year-old woman's death into the same record as an initial one-death report. Separating the incidents correctly raises the pilot sum to **422** (153 incident records).

No public page or displayed total has been changed. The correction is saved as a distinct commit so the prior audit checkpoint remains recoverable.
