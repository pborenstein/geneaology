---
phase: 2 (complete); Phase 3 next (place authority done)
updated: 2026-10-14
last_commit: 46559af
last_entry: chronicles/phase-2-extraction.md #16
---

# Context — Borenstein/Mostkoff Genealogy

**Project**: Well-sourced genealogy of the Borenstein/Mostkoff family — Wendy Cadieux (research) & Philip Borenstein (tech). Sources: 10 PDFs in `base-documents/` (2,265 pp, fully extracted) + tania-project.com memoir + UFDC Prensa Israelita (EV-59–80). Repo: github.com/pborenstein/geneaology.

**Current focus**: **Two rounds on 2026-10-14.** (1) *Prensa round* (parallel "hello" session, entry 15): EV-35 mined → 22 notices, EV-59–80 + `data/prensa-hits.md`; CF-16 record-confirmed, **A06 corrected** ("Tía Mania" = Felipe's widow → new CF-30), CF-23 resolved (Hebrew↔civil names), CF-15 leaning, Shifra's obit (CF-21/31); post 03 Sapotnitsky EN+ES. (2) *Mapping round* (this session, entry 16, **DEC-010**): `docs/MAPPING-PLAN.md` + **`data/places.md` gazetteer** (42 Tier-1 places + Tier-2 tail) + generated `data/places.geojson` (39 pts) / `.kml` via `scripts/places-to-geojson.py`; README gained a **What's New** section + full refresh. People **91** (A01–A29, B01–B26, C01–C16, X01–X21; X10 unused — prior "90" was a miscount) / EV-01–80 / CF-01–31.

**Active tasks** (Phase 3, see IMPLEMENTATION.md):
- [ ] Decide GEDCOM tooling (Gramps?) → load reconciled people from `data/people.md` **+ places from `data/places.md`** (place authority ready — DEC-010)
- [ ] Resolve/annotate every CF-## in `data/conflicts.md` (9 resolved/leaning; CF-30 Mania's identity is the big new one)
- (Phase 4 next): family outreach (Pola's information — key to CF-20/CF-30), JRI Kurow/Warsaw, NHAB archive pulls, USA records. Residue: Felipe Borenstein's own death notice (~1959/60 issue unidentified).

**Blockers**: None technical. Family-input items (feed Phase 4): Pola's information (CF-20 + CF-30); Wendy's remaining notes/photos; Philip's old rough genealogy; any Ancestry/MyHeritage/Geni GEDCOM exports.

**Key facts for orientation**:
- `data/people.md` is the deliverable: every entry has citations + [C]/[L]/[?] marks; conventions & citation keys in its header. Read it before anything else. `data/prensa-hits.md` + `data/pinkas-hits.md` hold the two big extraction passes; `data/places.md` the gazetteer.
- **Places** (DEC-010): `places.md` is the only hand-edited place file; regenerate `places.geojson`/`.kml` with `python3 scripts/places-to-geojson.py`. No coordinate without provenance. Settled: Ostrov = near Slutsk; Kurow = Kurów (Lublin). Open: Urechye has a Wikidata-vs-memoir-site discrepancy; Oreitsa/Laseh/Ozdeh un-geocoded `[?]`.
- UFDC citable pattern: `ufdcimages.uflib.ufl.edu/AA/00/06/55/27/{vol}/{img}.jpg` + same-path `.txt` OCR; the Notes' `NN/NNx` citations do NOT map to image numbers.
- Prensa prints Hebrew names (Anita=Ana, Pesele=Pola, Hinde=Aida, Sara=Chelo) — the CF-23 frame, now proven.
- Big corrections: Israel b. 1880; Nakhman alive ≥1932; Lyubka/Etl = Israel's sisters; Rachmeil=Mendel=Manuel Glatt (CF-16 confirmed); Mania = Felipe's widow (not sibling).
- The three grandparent-corner mysteries remain open: Sapotnitsky (`docs/investigations/sapotnitsky.md`, program §8–9 incl. Nesvizh + Minkov lead EV-79), CF-20 (Abram's children), CF-30 (Mania/Chana Mindel).

**Next session**: Read this + `data/people.md` header + `data/places.md` header; candidates: Phase 3 (GEDCOM tooling decision — people *and* place authorities now ready), the migration-route map layer (MAPPING-PLAN "Deferred v2+"), the Sapotnitsky program §8–9, post 04 (the Prensa-mining story), or CF-30 follow-up. Ask Philip which. Chase: Pola's information. Wrap-up runs the session-wrapup skill (chronicle next entry = 17).

**Map**: data/places.md + places.geojson/.kml + scripts/ (mapping — new) · docs/MAPPING-PLAN.md · README "What's New" section · data/prensa-hits.md · writing/ (3 EN+ES posts) · data/pinkas-hits.md · data/people.md · data/conflicts.md · docs/investigations/sapotnitsky.md · docs/FAMILY-OVERVIEW.md · docs/SOURCE-SURVEY.md · docs/ROADMAP.md · docs/RESOURCES.md · docs/DECISIONS.md (DEC-010 new) · docs/IMPLEMENTATION.md · docs/chronicles/.
