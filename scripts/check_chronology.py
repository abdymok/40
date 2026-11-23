#!/usr/bin/env python3
"""Validate the chronology pages before the GitHub Pages build."""

from html.parser import HTMLParser
from pathlib import Path
import posixpath
import re
from urllib.parse import unquote, urlsplit

PAGES = (
    "articles/critical-infrastructure-damage.html",
    "articles/critical-infrastructure-archive.html",
    "method/index.html",
    "articles/changes.html",
)
ENTRY_PATTERN = re.compile(
    r'<article id="(\d{4}-\d{2}-\d{2})-[^"]+" class="chronology-entry"'
)
CUTOFF_PATTERN = re.compile(
    r'Chronology through <time datetime="(\d{4}-\d{2}-\d{2})"'
)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.entry_dates = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "article":
            classes = attrs.get("class", "").split()
            match = re.match(r"(\d{4}-\d{2}-\d{2})-", attrs.get("id", ""))
            if "chronology-entry" in classes and match:
                self.entry_dates.append(match.group(1))


def fail(message):
    raise SystemExit(f"Chronology validation failed: {message}")


parsers = {}
for filename in PAGES:
    path = Path(filename)
    if not path.is_file():
        fail(f"required page is missing: {filename}")
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        fail(f"duplicate IDs in {filename}: {', '.join(duplicates[:10])}")
    parsers[filename] = parser

# Resolve local fragment links when their destination is one of the pages above.
known_ids = {name: set(parser.ids) for name, parser in parsers.items()}
for source, parser in parsers.items():
    for href in parser.links:
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc or not parsed.fragment:
            continue
        raw_path = unquote(parsed.path)
        if raw_path.startswith("/"):
            target = raw_path.lstrip("/")
        elif raw_path:
            target = posixpath.normpath(
                posixpath.join(posixpath.dirname(source), raw_path)
            )
        else:
            target = source
        if target.endswith("/"):
            target += "index.html"
        if target in known_ids and unquote(parsed.fragment) not in known_ids[target]:
            fail(f"broken fragment in {source}: {href}")

main_path = Path(PAGES[0])
main_html = main_path.read_text(encoding="utf-8")
parser = parsers[PAGES[0]]
matched_entries = ENTRY_PATTERN.findall(main_html)
if len(matched_entries) != len(parser.entry_dates):
    fail(
        "pages.yml cutoff matcher sees "
        f"{len(matched_entries)} entries but HTML contains "
        f"{len(parser.entry_dates)} chronology entries; update the workflow matcher"
    )
if not parser.entry_dates:
    fail("no dated chronology entries found")
cutoffs = CUTOFF_PATTERN.findall(main_html)
latest = max(parser.entry_dates)
if len(cutoffs) != 1 or cutoffs[0] != latest:
    fail(
        f"source cutoff label must occur once and match latest entry {latest}; "
        f"found {cutoffs}"
    )

print(
    "Chronology validation passed: "
    f"{sum(len(parser.ids) for parser in parsers.values())} unique page IDs, "
    f"{sum(len(parser.links) for parser in parsers.values())} links inspected, "
    f"{len(parser.entry_dates)} main-page entries, latest {latest}."
)
