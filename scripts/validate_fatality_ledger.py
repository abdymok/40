#!/usr/bin/env python3
"""Validate the incident-level fatality ledger and print its calculated total."""
import json
import re
import sys
from pathlib import Path
from datetime import datetime

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ALLOWED_EVIDENCE = {
    "official_and_media", "official_only", "media_reported",
    "monitoring_or_case_file", "project_record_only", "unverified",
}
ALLOWED_SCOPE = {
    "civilian", "non_combatant_emergency_personnel",
    "non_combatant_security_personnel", "mixed_non_combatant", "unresolved",
}
ALLOWED_SOURCE_TYPES = {
    "official_statement", "official_social_post", "news_report",
    "eyewitness", "project_record", "case_file",
    "official_company_statement", "international_monitoring_report",
}
ALLOWED_SUPPORTS = {
    "incident_identity", "death_count", "count_revision",
    "incident_date", "victim_status", "corroboration",
    "evidence_classification", "verification_status",
}

def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    return False

def valid_date(value, allow_datetime=False):
    if not isinstance(value, str):
        return False
    if DATE.match(value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    if allow_datetime:
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
            return True
        except ValueError:
            return False
    return False

def validate(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("top-level JSON value must be an array")

    incident_ids = set()
    global_source_ids = set()
    total = 0
    errors = []

    for index, record in enumerate(data):
        label = record.get("incident_id", f"record[{index}]")
        if not isinstance(label, str) or not label:
            errors.append(f"{label}: missing incident_id")
        elif label in incident_ids:
            errors.append(f"{label}: duplicate incident_id")
        incident_ids.add(label)

        required = (
            "incident_date", "location", "incident_description",
            "documented_deaths", "scope_classification",
            "evidence_classification", "sources",
            "last_verified_date", "revision_history",
        )
        for field in required:
            if field not in record:
                errors.append(f"{label}: missing {field}")

        if not valid_date(record.get("incident_date")):
            errors.append(f"{label}: invalid incident_date")
        if not valid_date(record.get("last_verified_date")):
            errors.append(f"{label}: invalid last_verified_date")

        location = record.get("location")
        if not isinstance(location, dict):
            errors.append(f"{label}: location must be an object")
        else:
            if "settlement" not in location or not (
                location.get("settlement") is None or isinstance(location.get("settlement"), str)
            ):
                errors.append(f"{label}: location.settlement must be a string or null")
            if not isinstance(location.get("region"), str) or not location.get("region"):
                errors.append(f"{label}: location.region must be a non-empty string")
            if location.get("country", "Ukraine") != "Ukraine":
                errors.append(f"{label}: location.country must be Ukraine")

        deaths = record.get("documented_deaths")
        if not isinstance(deaths, int) or isinstance(deaths, bool) or deaths < 0:
            errors.append(f"{label}: documented_deaths must be a non-negative integer")
        else:
            total += deaths

        if record.get("evidence_classification") not in ALLOWED_EVIDENCE:
            errors.append(f"{label}: invalid evidence_classification")
        if record.get("scope_classification") not in ALLOWED_SCOPE:
            errors.append(f"{label}: invalid scope_classification")

        sources = record.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{label}: sources must be a non-empty array")
            sources = []

        local_source_ids = set()
        for source in sources:
            sid = source.get("source_id")
            if not isinstance(sid, str) or not sid:
                errors.append(f"{label}: source missing source_id")
                continue
            if sid in local_source_ids:
                errors.append(f"{label}: duplicate source_id within record: {sid}")
            if sid in global_source_ids:
                errors.append(f"{label}: duplicate source_id across ledger: {sid}")
            local_source_ids.add(sid)
            global_source_ids.add(sid)
            for field in ("publisher", "source_type", "url", "supports", "notes"):
                if field not in source:
                    errors.append(f"{label}/{sid}: missing {field}")
            if source.get("source_type") not in ALLOWED_SOURCE_TYPES:
                errors.append(f"{label}/{sid}: invalid source_type")
            supports = source.get("supports")
            if not isinstance(supports, list) or not supports:
                errors.append(f"{label}/{sid}: supports must be a non-empty array")
            else:
                for claim in supports:
                    if claim not in ALLOWED_SUPPORTS:
                        errors.append(f"{label}/{sid}: invalid supports value: {claim}")
            url = source.get("url", "")
            if not isinstance(url, str) or not url.startswith("https://"):
                errors.append(f"{label}/{sid}: URL must use https://")
            published = source.get("published_at")
            if published is not None and not valid_date(published, allow_datetime=True):
                errors.append(f"{label}/{sid}: invalid published_at date/time")

        history = record.get("revision_history")
        if not isinstance(history, list) or not history:
            errors.append(f"{label}: revision_history must be a non-empty array")
            continue

        previous = None
        for rev_index, revision in enumerate(history):
            rid = revision.get("revision_id", f"{label}/revision[{rev_index}]")
            old = revision.get("old_value")
            new = revision.get("new_value")
            if rev_index == 0:
                if old is not None and (not isinstance(old, int) or old < 0):
                    errors.append(f"{rid}: first old_value must be null or a non-negative integer")
            elif old != previous:
                errors.append(f"{rid}: old_value does not match previous new_value")
            if not isinstance(new, int) or isinstance(new, bool) or new < 0:
                errors.append(f"{rid}: new_value must be a non-negative integer")
            previous = new
            if not revision.get("reason"):
                errors.append(f"{rid}: missing reason")
            if not valid_date(revision.get("recorded_at"), allow_datetime=True):
                errors.append(f"{rid}: invalid recorded_at")
            effective = revision.get("ledger_effective_at")
            if effective is not None and not valid_date(effective, allow_datetime=True):
                errors.append(f"{rid}: invalid ledger_effective_at")
            refs = revision.get("source_ids")
            if not isinstance(refs, list) or not refs:
                errors.append(f"{rid}: source_ids must be a non-empty array")
            else:
                for sid in refs:
                    if sid not in local_source_ids:
                        errors.append(f"{rid}: source reference not found: {sid}")

        if history and history[-1].get("new_value") != deaths:
            errors.append(f"{label}: final revision does not match documented_deaths")

    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        print(f"FAILED: {len(errors)} error(s)", file=sys.stderr)
        return 1

    print(json.dumps({
        "status": "ok",
        "incident_records": len(data),
        "source_records": len(global_source_ids),
        "documented_deaths": total,
    }, indent=2))
    return 0

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "fatality-ledger/incidents.json"
    raise SystemExit(validate(target))
