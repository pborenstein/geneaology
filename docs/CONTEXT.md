---
phase: 2 (complete); Phase 3 next (place authority done)
updated: 2026-10-18
last_commit: b7354ce
last_entry: chronicles/phase-2-extraction.md #17
---

# Context — Borenstein/Mostkoff Genealogy

**Project**: Well-sourced genealogy of the Borenstein/Mostkoff family — Wendy Cadieux (research) & Philip Borenstein (tech). Sources: 10 PDFs in `base-documents/` (2,265 pp, fully extracted) + tania-project.com memoir + UFDC Prensa Israelita (EV-59–80). Repo: github.com/pborenstein/geneaology.

**Current focus**: **2026-10-18 writing round (entry 17): post 04** — the Prensa-mining story for the family, EN+ES (*The Paper That Knew Everyone* / *El periódico que conocía a todos*): the Hebrew-names key (CF-23), the 1959 wedding portrait with Moscow's printed greetings, the Mania correction (CF-30), Mendel=Manuel (CF-16), Shifra as "Sofía Mostkoff" (CF-21/31), Toibe's chosen plot, the Minkov lead — closing with five family asks (Felipe's death notice, Mania=Bauman?, Glatt surname, "Ydele," clippings) + a direct invitation to Pola. Post 03 EN+ES forward-linked; README What's New + counts updated; stray duplicate `data/places 2.kml` deleted. Prior rounds: 2026-10-14 ×2 — Prensa EV-35 mined (entry 15: EV-59–80, CF-16/23 resolved, A06→CF-30, post 03) + place layer (entry 16: gazetteer + map files, DEC-010).

**Active tasks** (Phase 3, see IMPLEMENTATION.md):
- [ ] Decide GEDCOM tooling (Gramps?) → load reconciled people from `data/people.md` **+ places from `data/places.md`** (place authority ready — DEC-010)
- [ ] Resolve/annotate every CF-## in `data/conflicts.md` (9 resolved/leaning; CF-30 Mania's identity is the big new one — post 04 now asks the family directly)
- (Phase 4 next): family outreach (Pola's information — key to CF-20/CF-30; post 04 invites her), JRI Kurow/Warsaw, NHAB archive pulls, USA records. Residue: Felipe Borenstein's own death notice (~1959/60 issue unidentified) — now also a family ask in post 04.

**Blockers**: None technical. Family-input items (feed Phase 4): Pola's information (CF-20 + CF-30); Wendy's remaining notes/photos; Philip's old rough genealogy; any Ancestry/MyHeritage/Geni GEDCOM exports.

**Key facts for orientation**:
- `data/people.md` is the deliverable: every entry has citations + [C]/[L]/[?] marks; conventions & citation keys in its header. Read it before anything else. `data/prensa-hits.md` + `data/pinkas-hits.md` hold the two big extraction passes; `data/places.md` the gazetteer.
- **Posts** (writing/, 4 EN+ES pairs, byline per DEC-009): 01 orientation · 02 Pinkas · 03 Sapotnitsky · 04 the Prensa story. Facts in posts trace only to `data/`; post 04's fact-check pass is documented in chronicle #17.
- **Places** (DEC-010): `places.md` is the only hand-edited place file; regenerate `places.geojson`/`.kml` with `python3 scripts/places-to-geojson.py`. No coordinate without provenance. Settled: Ostrov = near Slutsk; Kurow = Kurów (Lublin). Open: Urechye has a Wikidata-vs-memoir-site discrepancy; Oreitsa/Laseh/Ozdeh un-geocoded `[?]`.
- UFDC citable pattern: `ufdcimages.uflib.ufl.edu/AA/00/06/55/27/{vol}/{img}.jpg` + same-path `.txt` OCR; the Notes' `NN/NNx` citations do NOT map to image numbers.
- Prensa prints Hebrew names (Anita=Ana, Pesele=Pola, Hinde=Aida, Sara=Consuelo "Chelo") — the CF-23 frame, now proven and explained publicly in post 04. NB: "Chelo" is an apodo; her name is Consuelo (B15, Philip 2026-10-18).
- Big corrections: Israel b. 1880; Nakhman alive ≥1932; Lyubka/Etl = Israel's sisters; Rachmeil=Mendel=Manuel Glatt (CF-16 confirmed); Mania = Felipe's widow (not sibling).
- The three grandparent-corner mysteries remain open: Sapotnitsky (`docs/investigations/sapotnitsky.md`, program §8–9 incl. Nesvizh + Minkov lead EV-79), CF-20 (Abram's children), CF-30 (Mania/Chana Mindel).

**Next session**: Read this + `data/people.md` header + `data/places.md` header; candidates: Phase 3 (GEDCOM tooling decision — people *and* place authorities now ready), the migration-route map layer (MAPPING-PLAN "Deferred v2+"), the Sapotnitsky program §8–9, or CF-30 follow-up. Ask Philip which. Chase: Pola's information (post 04 invites her directly). Wrap-up runs the session-wrapup skill (chronicle next entry = 18).

**Map**: data/places.md + places.geojson/.kml + scripts/ (mapping) · docs/MAPPING-PLAN.md · README "What's New" + posts table · data/prensa-hits.md · writing/ (4 EN+ES posts) · data/pinkas-hits.md · data/people.md · data/conflicts.md · docs/investigations/sapotnitsky.md · docs/FAMILY-OVERVIEW.md · docs/SOURCE-SURVEY.md · docs/ROADMAP.md · docs/RESOURCES.md · docs/DECISIONS.md (DEC-010) · docs/IMPLEMENTATION.md · docs/chronicles/.
