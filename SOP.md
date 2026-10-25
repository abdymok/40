# 40 / Kyiv infrastructure chronology — publishing SOP

## House style
## Names, monikers, and recurring motifs

- `ukraine@war` and `abdymok` (with the `y` rendered red where the design calls for it) are interchangeable monikers for the same body of work, not separate brands or projects.
- `ultra-competitive survival`, `ultra-competitive ukraine-style politics`, and `spontaeneous mass combustion` are interchangeable recurring phrases or motifs. Preserve the exact wording used in a particular context.
- Choose the moniker or motif to suit the site, page, and piece. The wording may vary across GitHub, Substack, the Google site, and individual pages. Do not impose one universal label or “standardize” these variations unless explicitly asked.

## Headlines

- Headlines must be short enough to fit on one line in the intended layout. If a headline wraps onto a second line, shorten it; never accept a two-line headline.


- For Ukrainian place names, use the project's preferred transliteration: write `-y`, not `-yi`. Examples: `Solomiansky`, `Darnytsky`, `Sviatoshynsky`, `Holosiivsky`. Do not “correct” these to forms ending in `-yi`.
- Always write `Zaporizhia`, never `Zaporizhzhia`, in all English-language project text, including headlines, chronology entries, captions, dashboard text, and update history. This is a fixed project spelling and must not be changed to match a source's transliteration.

## Images, figures, and captions

- Before publishing an image swap or caption edit, inspect the specific figure and its shared CSS; prefer a targeted fix over broad stylesheet changes.
- Check the actual line breaks, not merely the caption's width or CSS declarations. Keep short, meaningful phrases together with non-breaking spaces where appropriate when a word is stranded at a line end.
- When a caption wraps badly, inspect inherited rules in the shared stylesheet before changing its width. In particular, `text-wrap: balance` and `figure`/`figcaption` table layout can override the expected line flow. For a caption that should align with the 720px chronology column, explicitly use `display: block; width: 100%; max-width: 720px; box-sizing: border-box; text-wrap: wrap;` on that caption. Keep the fix scoped to the affected caption; use a non-breaking space only when a specific short phrase must stay together.
- After committing, fetch the file again to verify the exact change landed. Then inspect the rendered live page on desktop and mobile where possible. If live rendering cannot be checked, say so plainly; do not claim visual verification.

## Chronology

- Add the newest item at the top of the chronology. Preserve older entries and anchors; do not delete or silently regress earlier material.
- Give every chronology entry a unique, stable anchor ID. Every headline-bearing entry must link to its own anchor, and all existing links to entry anchors must continue to work when entries are reordered or moved to the archive.
- Attribute reported claims to the named source. Distinguish official statements, local-channel reports, eyewitness observations and independently corroborated facts.
- Do not infer a weapon, impact, exact location, damage or casualty figure from footage or sounds unless the evidence supports it.
- Link sources directly. Keep uncertainty explicit and concise.

## Video evidence and cutlines

- Every photo or video evidence window must carry an explicit visible date, including the year where appropriate. Spell out the month in full (for example, `KYIV · OCTOBER 22, 2026`); never abbreviate it in the visible caption.
- Verify the actual rendered-caption source for every evidence window before publishing. Do not rely on surrounding chronology text, file metadata, or a commit message to establish the date; check that the date is visibly present in the caption itself.

- Let the video lead. Keep the caption close to the video, with tight spacing.
- Use small, muted caption type (normally 12px) and restrained line spacing.
- Write one concise cutline: identify the place or subject, state only the necessary context, and include a direct source link where available.
- Do not repeat the cutline in a second paragraph below the video. No duplicate prose.
- Retain a usable poster/cover image and a direct link to the original video when appropriate. Do not change surrounding page structure merely to rotate or replace media.

## Media sizing and page margins

- Keep every chronology image, video, poster frame and caption within the same content-column margins as the surrounding text. On the infrastructure chronology, the maximum width is the 720px main column; do not let media expand to a wider archive or figure maximum.
- Set video and poster display to scale responsively within the column (`width: 100%; max-width: 100%; height: auto`). Keep the caption inside the same figure and aligned to the same margins.
- For lead videos where a poster image is available, use the poster as the immediate display and set `preload="none"` so the video file does not slow the initial page load; let playback trigger the video fetch.
- After changing media sizing, check the live page on desktop and mobile when possible. Confirm both the pre-play poster and the playing video stay within the text margins; do not claim visual verification unless actually checked.

## Dashboard and page restraint

- Keep dashboard tiles equal-sized and symmetrical, with large, legible numerals.
- Update dashboard figures and the latest chronology item as part of the same publishing workflow when relevant. Label estimates and provisional counts as such.
- The `Dead civilians` figure is a nationwide, provisional documented minimum of officially reported civilian deaths attributed to Russian attacks; exclude military deaths and check existing entries to avoid double-counting. It is not a complete national total, and the actual toll is likely higher.
- We are not running a national casualty-monitoring service. Record deaths when they come to our attention and can be attributed to reliable official reporting; make a good-faith effort, but do not imply exhaustive coverage or treat gaps in our tally as evidence that deaths did not occur. Correct the count when better information arrives.
- Keep the visual treatment restrained: white background, editorial typography, minimal decoration, no unnecessary cards, gradients or animation.
- Use concise labels and avoid redundant explanatory copy.


## Kyiv air-alert count and time under alert

- Keep the Kyiv alert count and cumulative time under alert as current as reasonably practical, using the alerts.in.ua Kyiv history and the user's firsthand observations where relevant. This is a good-faith running record, not a live monitoring service. We have other reporting, writing and site work to do, so updates may lag. Do not imply continuous monitoring or treat a delay as a failure.
- Reconcile the tracker against the existing dashboard baseline before adding intervals. Count each distinct Kyiv alert once. Check start and end times, account for alerts that cross midnight, and avoid double-counting intervals already included in the baseline. Keep Kyiv-only alerts separate from Ukraine-wide alerts.
- Use the durations reported by alerts.in.ua consistently for cumulative time where available. The tracker rounds durations, so its reported length may differ by a minute from subtracting the displayed start and end times. Do not mix methods silently.
- Count an ongoing alert as a provisional alert event. For a snapshot that includes its elapsed time, calculate from the reported start time or tracker-reported elapsed duration, state the snapshot/cutoff and make clear that the total will continue to grow while the alert remains active. Do not treat an active interval as completed.
- Exclude unresolved older intervals or intervals with uncertain duration from the cumulative total until they can be reconciled. Do not invent missing durations or silently estimate them. Where practical, retain the uncertainty in the methodology note.
- After a reconciliation, update the alert count, cumulative duration, page date, methodology and change history together. Record the cutoff, newly included completed intervals, any active interval, and the resulting totals. Keep dashboard copy concise and provisional where appropriate; put calculation details and rounding caveats in the methodology note.
- Work from the best available evidence at the time. Correct the figures when better information arrives, but do not delay other substantive work merely to keep the dashboard minute-perfect.

## Landing-page parity — hard requirement

- `https://abdymok.github.io/index.html` must always be byte-for-byte identical to the canonical landing-page HTML at `abdymok/landing_page/index.html` (published as `https://abdymok.github.io/`). The root page is not a separate design and must not be replaced with a redirect.
- Whenever either copy is changed, check both files and restore exact parity in the same work session. Compare the actual file contents; do not assume parity from appearance or from a prior check.
- Before editing, locate and fetch the real canonical file path and confirm the current contents. If the path cannot be found or fetched, stop and report that obstacle rather than guessing, recreating the file, or editing one copy alone.
- Preserve the approved landing-page design and existing desktop/iPhone layout and display behavior unless the user explicitly requests a change. When investigating a missing video or other media, diagnose the cause before changing layout or playback behavior.

## Page structure and maintenance

- Keep the dashboard as the first substantive block after navigation. Keep dashboard tiles symmetrical and their explanatory lines short; place detailed reconciliation in the linked methodology note.
- Treat dashboard counts as the single source of truth. Methodology notes should reference the dashboard values rather than repeat independent hard-coded counts.
- Keep the current chronology on the main page for roughly the latest week. Move older full entries to `articles/critical-infrastructure-archive.html`, preserving their IDs in the archive and anchor pointers on the main page.
- Group entries by date. Keep the latest three days expanded and collapse older day groups with native `details` elements. Add a jump link for each day in the navigation. No animation.
- Use a consistent entry structure: date, place, normalized evidence label, headline, paragraphs, then compact source links. Normalize evidence labels to official, operator or company, media, eyewitness, attributed, unverified or editorial; retain source-specific detail after the category.
- For developing stories, begin with a concise two-sentence summary, then present timestamped updates in a two-column layout with tabular numerals in the time column. Preserve the original sourcing and distinguish attributed claims from established facts.
- Keep status labels at least 12px, captions at least 13px and entry body text at 16px. Source links should be compact and one per line.
- Keep CSS declarations consolidated. Avoid duplicate base and dashboard rules that can silently override the approved layout.
