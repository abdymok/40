#!/usr/bin/env python3
"""Validate the chronology pages before the GitHub Pages build."""

from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
import json
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
        self.meta = {}
        self.title_parts = []
        self.jsonld_parts = []
        self.in_title = False
        self.in_jsonld = False

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
        if tag == "meta":
            key = attrs.get("property") or attrs.get("name")
            if key and attrs.get("content") is not None:
                self.meta[key.lower()] = attrs["content"]
        if tag == "title":
            self.in_title = True
        if tag == "script" and attrs.get("type", "").lower() == "application/ld+json":
            self.in_jsonld = True
            self.jsonld_parts.append([])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.in_jsonld:
            self.in_jsonld = False

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)
        if self.in_jsonld and self.jsonld_parts:
            self.jsonld_parts[-1].append(data)


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

latest = max(parser.entry_dates)
cutoffs = CUTOFF_PATTERN.findall(main_html)
if len(cutoffs) != 1 or cutoffs[0] != latest:
    print(
        "WARNING: source cutoff label is stale or missing; "
        f"expected one label for {latest}, found {cutoffs}. "
        "The Pages workflow will regenerate it before Jekyll."
    )

# Keep visible, social and structured-data titles in sync with the latest entry.
day = datetime.strptime(latest, "%Y-%m-%d")
expected_date = f"{day.strftime('%b')}. {day.day}, {day.year}"
required_titles = {
    "<title>": " ".join(parser.title_parts).strip(),
    "og:title": parser.meta.get("og:title", ""),
    "twitter:title": parser.meta.get("twitter:title", ""),
}
for label, value in required_titles.items():
    if not value or f"through {expected_date}" not in value:
        fail(f"{label} must include 'through {expected_date}'")

jsonld_objects = []
for parts in parser.jsonld_parts:
    try:
        value = json.loads("".join(parts))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON-LD in main chronology: {exc}")
    if isinstance(value, dict):
        jsonld_objects.append(value)
headlines = [obj.get("headline", "") for obj in jsonld_objects if "headline" in obj]
if not any(f"through {expected_date}" in headline for headline in headlines):
    fail(f"JSON-LD headline must include 'through {expected_date}'")
modified_dates = [obj.get("dateModified") for obj in jsonld_objects if "dateModified" in obj]
entry_date = datetime.strptime(latest, "%Y-%m-%d").date()
valid_modified_dates = []
for value in modified_dates:
    try:
        modified_date = datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        continue
    if modified_date >= entry_date:
        valid_modified_dates.append(value)
if not valid_modified_dates:
    fail(f"JSON-LD dateModified must be on or after latest entry date {latest}")

print(
    "Chronology validation passed: "
    f"{sum(len(parser.ids) for parser in parsers.values())} unique page IDs, "
    f"{sum(len(parser.links) for parser in parsers.values())} links inspected, "
    f"{len(parser.entry_dates)} main-page entries, latest {latest}."
)
