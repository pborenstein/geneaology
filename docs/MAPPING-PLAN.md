# Mapping Plan — Gazetteer & Map Layer

*Written 2026-10-14 (the "mapping" session). Status: executing this plan — deliverables are `data/places.md` (gazetteer, source of truth) and the generated `data/places.geojson` / `data/places.kml`.*

## Goal

A **place gazetteer** of every place the corpus mentions, and from it a labeled map of the family's Eastern Europe (and the migration arc beyond: USA, Mexico). Two consumers:

1. **Human / family** — a map viewable in standard tools with places *and* people labeled: uMap (OpenStreetMap-based, zero install), QGIS, Google Earth, geojson.io, GitHub's inline map.
2. **Phase 3 (GEDCOM/Gramps)** — a **place authority**: one canonical record per town so GEDCOM export writes consistent place strings and Gramps doesn't sprout duplicates for every name variant. Doing this before the GEDCOM load is the right sequencing (it was Phase 3 groundwork all along).

## Architecture: gazetteer first, the map is generated

- **`data/places.md`** — the deliverable and the only hand-edited file. Same conventions as `data/people.md`: stable IDs, confidence marks, citation keys.
- **`scripts/places-to-geojson.py`** — stdlib-only converter; parses `places.md` and writes `data/places.geojson` (primary interchange) + `data/places.kml` (Google Earth). Regenerate after any edit: `python3 scripts/places-to-geojson.py`.
- **`data/places.geojson` / `data/places.kml`** — generated artifacts; never hand-edit them (same rule as `extracted-text/`).

## Data model

One entry per **distinct place**, with the same discipline as people: *never merge same-named places without corroboration* (there are several Ostrovs, several Dvoretzes, dozens of Kurow-like names in Poland).

- **IDs**: `P##`, assigned in rough corpus order (Belarus cluster first, then Poland, USSR, USA, Mexico, beyond).
- **Tiers**: Tier 1 = family-connected places (full entries, geocoded where unambiguous). Tier 2 = background/lead toponyms (one-liners at the tail: pinkas "from X" descriptors for unrelated townsfolk, record leads, glancing mentions) — mirroring people.md's background-notes tail.
- **Fields per entry**: Variants (as sourced) · Today (modern name + country) · Region · Coords (lat, lon **+ provenance**) · Jurisdictions (empire → today chain) · People & events (`ID — event — citation`) · Notes.
- **Confidence & citations** exactly as people.md: `[C]` / `[L]` / `[?]`; citation keys (`tania-project (§N)`, `Tanya-summary, p. N`, `Pinkas, p. N (entry #M)`, EV-##, URLs).
- **Coordinate provenance rule**: no coordinate without a source (Wikidata QID, GeoNames ID, JewishGen Gazetteer, the memoir-site gazetteer, or a record). A place that can't be pinned (unidentified pinkas toponyms like Laseh/Ozdeh) ships **un-geocoded** — present in `places.md`, absent from the map — rather than guessed.

## Disambiguation decisions (the genealogically load-bearing part)

- **Ostrov ≠ Ostrów Mazowiecka (or any other Ostrov)**: the corpus places Ostrov *next to Slutsk* — Nakhman lived "on the outskirts of Ostrov near Slutsk" (`Tanya-summary, p. 3`), and a Slutsk-pinkas Borukhovich is "Ostrever" (`Pinkas, p. 430 (entry #2989)`). Israel's birth shtetl is the Slutsk-area Ostrov, Minsk gubernia `[C text / L identification]`. Pinning the exact village among same-named ones needs the JewishGen Gazetteer — coords marked `[L]`/pending until then.
- **Kurow = Kurów (Lublin region)**: the JRI-Poland Kurow holdings sit in Fond 1751, **Lublin Archive** (`Notes, p. 17`) → the Kurów of Puławy county, Lublin voivodeship `[C archive fond]`.
- **Dvoretz** (B03/B05's town): the 1906 Lida marriage (`EV-01`) points to the Dvorets of the former **Lida uyezd** (today Dziatlovo district, Grodno region). Other Dvoretzes exist — keep `[L]` and the variants.
- **Dalhinoveh / Laseh / Ozdeh** (pinkas #229 massacre geography, EV-06) and **Oreitsa/Oretesheh** (Itskovits of CF-17): transliterations off the register's translation; identifications tentative `[?]` until cross-checked (Dalhinoveh ≈ Dalhinov, Vileika district `[L]`).
- **Chaya's natal village** near Nesvizh is *unidentified as a settlement* — record it inside the Nesvizh entry as a note, not as its own guess.

## Historical jurisdictions (recorded per entry — this is the genealogical value-add)

The chain that matters for sourcing and for reading period documents, e.g.:

- **Nesvizh**: Russian Empire (Minsk gubernia) → Poland 1921–39 (the Riga border ran just west of town — why the memoir says "near the Polish border"; see people.md B02) → Byelorussian SSR → Belarus.
- **Vilnius**: Russian Empire (Vilna gubernia) → Poland (Wilno) 1920–39 → Lithuania.
- **Kurow**: Congress Poland / Russian Empire (Lublin gubernia) → Poland 1918.

## Scope (v1, 2026-10-14)

- **Tier 1 (~36)**: Belarus cluster — Slutsk, Ostrov, Nesvizh, Urechye, Lida, Dvoretz, Radun, Minsk, Bobruisk, Vitebsk, Vilnius, Novogrudok, Dalhinoveh (+ un-geocoded `[?]` Laseh, Ozdeh, Oreitsa) · Poland — Kurow, Warsaw, Bialystok · Russia/USSR — Moscow, Leningrad/St Petersburg, Saratov, Birobidzhan, Khabarovsk, Velikiye Luki, Penza · USA — Rosedale MS, Clarksdale MS, Memphis TN, St. Louis MO, Baton Rouge LA, Las Vegas NV · Mexico — Mexico City, Guadalajara · Spain — Marbella.
- **Tier 2 (one-liners)**: pinkas background toponyms (Kletsk, Brisk, Lakhovits, Lekhevits, Ivenits, Luban, Radkevits/Ratskevits, Resk, Razoveh, …), record leads (Koidanov, Smorgon, Bogunov, Gomel, Rechitsa, Priluki, Berezino), glancing mentions (Arizona 1934 crossing, New York).

## Viewing the map

- **uMap (recommended; the "OpenMap" answer)**: <https://umap.openstreetmap.fr> → Create a map → Import data → upload `data/places.geojson`. The map link is shareable; import can be refreshed.
- **QGIS**: Layer ▸ Add Layer ▸ Add Vector Layer → `places.geojson`.
- **Google Earth**: File ▸ Open → `places.kml`.
- **Quick look**: drop `places.geojson` onto <https://geojson.io>, or open it on GitHub (renders an inline map).

## Deferred (v2+)

- **Migration-route layer** — a second GeoJSON of LineStrings: Slutsk→Moscow→Birobidzhan (Tania); Slutsk→Veracruz→Mexico City (Israel 1924, Abram 1926, Shifra + children 1928–29); Kurow→Warsaw→Mexico City (Borenstein); the Mississippi/Arkansas fur circuit (Eiser). Needs an event ordering pass first.
- **Leaflet family map** — self-contained HTML, bilingual EN/ES per DEC-009, for the writing series once the point layer is stable.
- **GEDCOM place strings** from the gazetteer at Phase 3.
