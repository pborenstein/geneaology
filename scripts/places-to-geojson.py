#!/usr/bin/env python3
"""Generate data/places.geojson + data/places.kml from data/places.md.

Parses the Tier-1 entries of the place gazetteer (### P## · Name headers with
- **Field:** value bullets) and writes the two generated map files. Generated
artifacts are never hand-edited (docs/MAPPING-PLAN.md).

Usage: python3 scripts/places-to-geojson.py   (from the repo root)
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "data" / "places.md"
GEOJSON = REPO / "data" / "places.geojson"
KML = REPO / "data" / "places.kml"

ENTRY_RE = re.compile(r"^### (P\d+) · (.+?)\s*$")
FIELD_RE = re.compile(r"^- \*\*(.+?):\*\* (.+)$")
COORD_RE = re.compile(r"(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)")


def parse_entries(text):
    entries, current = [], None
    for line in text.splitlines():
        m = ENTRY_RE.match(line)
        if m:
            if current:
                entries.append(current)
            current = {"id": m.group(1), "name": m.group(2), "fields": {}}
            continue
        if current:
            f = FIELD_RE.match(line)
            if f:
                current["fields"][f.group(1)] = f.group(2).strip()
            elif line.startswith("## "):  # next major section ends the block
                entries.append(current)
                current = None
    if current:
        entries.append(current)
    return entries


def build_place(e):
    f = e["fields"]
    cm = COORD_RE.search(f.get("Coords", ""))
    coords = (float(cm.group(1)), float(cm.group(2))) if cm else None
    return {
        "id": e["id"],
        "name": e["name"],
        "today": f.get("Today", ""),
        "region": f.get("Region", ""),
        "confidence": f.get("Confidence", "").strip("[]") or "?",
        "precision": "approximate" if "approx" in f.get("Coords", "") else "town",
        "coords_source": f.get("Coords", ""),
        "jurisdictions": f.get("Jurisdictions", ""),
        "variants": [v.strip() for v in f.get("Variants", "").split("·")],
        "people": [p.strip() for p in f.get("People", "").split(";") if p.strip()],
        "notes": f.get("Notes", ""),
        "coords": coords,
    }


def to_geojson(places):
    feats = []
    for p in places:
        if not p["coords"]:
            continue
        feats.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [p["coords"][1], p["coords"][0]]},
            "properties": {
                "id": p["id"],
                "name": p["name"],
                "today": p["today"],
                "region": p["region"],
                "confidence": p["confidence"],
                "precision": p["precision"],
                "variants": p["variants"],
                "people": p["people"],
                "jurisdictions": p["jurisdictions"],
                "coords_source": p["coords_source"],
                "notes": p["notes"],
            },
        })
    return {"type": "FeatureCollection", "features": feats}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def kml_desc(p):
    lines = [
        f"<b>{esc(p['id'])} · {esc(p['name'])}</b>",
        f"Today: {esc(p['today'])}",
        f"Confidence: [{esc(p['confidence'])}] · precision: {esc(p['precision'])}",
    ]
    if p["jurisdictions"]:
        lines.append(f"Jurisdictions: {esc(p['jurisdictions'])}")
    if p["people"]:
        lines.append("<br/><b>People &amp; events</b><br/>" + "<br/>".join(esc(x) for x in p["people"]))
    if p["notes"]:
        lines.append(f"<br/><i>{esc(p['notes'])}</i>")
    lines.append(f"<br/><i>coords: {esc(p['coords_source'])}</i>")
    return "<br/>".join(lines)


def to_kml(places):
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<kml xmlns="http://www.opengis.net/kml/2.2"><Document>',
           "<name>Borenstein/Mostkoff place gazetteer</name>",
           "<description>Generated from data/places.md — do not edit by hand.</description>"]
    for p in places:
        if not p["coords"]:
            continue
        out.append("<Placemark>")
        out.append(f"<name>{esc(p['id'])} · {esc(p['name'])}</name>")
        out.append(f"<description>{kml_desc(p)}</description>")
        out.append(f"<Point><coordinates>{p['coords'][1]},{p['coords'][0]},0</coordinates></Point>")
        out.append("</Placemark>")
    out.append("</Document></kml>")
    return "\n".join(out) + "\n"


def main():
    text = SRC.read_text(encoding="utf-8")
    places = [build_place(e) for e in parse_entries(text)]
    if not places:
        sys.exit("no entries parsed — parser/format mismatch")
    GEOJSON.write_text(json.dumps(to_geojson(places), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    KML.write_text(to_kml(places), encoding="utf-8")
    geocoded = [p for p in places if p["coords"]]
    missing = [f"{p['id']} {p['name']}" for p in places if not p["coords"]]
    print(f"{len(places)} Tier-1 entries parsed; {len(geocoded)} geocoded -> {GEOJSON.name}, {KML.name}")
    if missing:
        print("un-geocoded (by design):", ", ".join(missing))
    bad = [p["id"] for p in places if not p["region"] or not p["people"]]
    if bad:
        sys.exit(f"entries missing Region/People fields: {bad}")


if __name__ == "__main__":
    main()
