# 40 / Kyiv infrastructure chronology — publishing SOP

## House style

- For Ukrainian place names, use the project's preferred transliteration: write `-y`, not `-yi`. Examples: `Solomiansky`, `Darnytsky`, `Sviatoshynsky`, `Holosiivsky`. Do not “correct” these to forms ending in `-yi`.

## Chronology

- Add the newest item at the top of the chronology. Preserve older entries and anchors; do not delete or silently regress earlier material.
- Attribute reported claims to the named source. Distinguish official statements, local-channel reports, eyewitness observations and independently corroborated facts.
- Do not infer a weapon, impact, exact location, damage or casualty figure from footage or sounds unless the evidence supports it.
- Link sources directly. Keep uncertainty explicit and concise.

## Video evidence and cutlines

- Let the video lead. Keep the caption close to the video, with tight spacing.
- Use small, muted caption type (normally 12px) and restrained line spacing.
- Write one concise cutline: identify the place or subject, state only the necessary context, and include a direct source link where available.
- Do not repeat the cutline in a second paragraph below the video. No duplicate prose.
- Retain a usable poster/cover image and a direct link to the original video when appropriate. Do not change surrounding page structure merely to rotate or replace media.

## Dashboard and page restraint

- Keep dashboard tiles equal-sized and symmetrical, with large, legible numerals.
- Update dashboard figures and the latest chronology item as part of the same publishing workflow when relevant. Label estimates and provisional counts as such.
- Keep the visual treatment restrained: white background, editorial typography, minimal decoration, no unnecessary cards, gradients or animation.
- Use concise labels and avoid redundant explanatory copy.


## Page structure and maintenance

- Keep the dashboard as the first substantive block after navigation. Keep dashboard tiles symmetrical and their explanatory lines short; place detailed reconciliation in the linked methodology note.
- Treat dashboard counts as the single source of truth. Methodology notes should reference the dashboard values rather than repeat independent hard-coded counts.
- Keep the current chronology on the main page for roughly the latest week. Move older full entries to `articles/critical-infrastructure-archive.html`, preserving their IDs in the archive and anchor pointers on the main page.
- Group entries by date. Keep the latest three days expanded and collapse older day groups with native `details` elements. Add a jump link for each day in the navigation. No animation.
- Use a consistent entry structure: date, place, normalized evidence label, headline, paragraphs, then compact source links. Normalize evidence labels to official, operator or company, media, eyewitness, attributed, unverified or editorial; retain source-specific detail after the category.
- For developing stories, begin with a concise two-sentence summary, then present timestamped updates in a two-column layout with tabular numerals in the time column. Preserve the original sourcing and distinguish attributed claims from established facts.
- Keep status labels at least 12px, captions at least 13px and entry body text at 16px. Source links should be compact and one per line.
- Keep CSS declarations consolidated. Avoid duplicate base and dashboard rules that can silently override the approved layout.
