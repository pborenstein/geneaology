---
phase: 2 (complete); Phase 3 next (place authority done)
updated: 2026-10-19
last_commit: f634a04
last_entry: chronicles/phase-2-extraction.md #18
---

# Context — Borenstein/Mostkoff Genealogy

**Project**: Well-sourced genealogy of the Borenstein/Mostkoff family — Wendy Cadieux (research) & Philip Borenstein (tech). Sources: 10 PDFs in `base-documents/` (2,265 pp, fully extracted) + tania-project.com memoir + UFDC Prensa Israelita (EV-59–80) + **family input (Philip, live since 2026-10-19)**. Repo: github.com/pborenstein/geneaology.

**Current focus**: **2026-10-18/19 — post 04 + the first family-input round (entries 17–18).** Post 04 (*The Paper That Knew Everyone*, EN+ES) told the Prensa-mining story and asked the family five things; Philip answered within a day, and the record moved: **CF-30 resolved** (Mania = Chana Mindel Bauman = civil María; **A15 merged into A06**, DEC-012); **A27 corrected** — Sara Jarovinsky was *Mania's* sister (a Bauman), not Felipe's; "Sura Ita" = Sarita; **"Chelo" is an apodo** for Consuelo (B15); Ana → Caddess (m. 2) 1982), Ana & José **divorced 1978**, José **d. March 2026**, m. 2) Carol Ackerman ~1986 `[L]`. Tree fixed (the stale "Tía Mania — sibling" node removed; José d.2026; convergence hub m. 1959 · div. 1978 + second marriages). Post 04 corrected in place + dated postscript. README: pictographs out (DEC-011), What's New entries linked. People **90 distinct** (A01–A29, B01–B26, C01–C16, X01–X21; X10 unused, A15 → A06 redirect) / EV-01–80 / CF-01–31 (10 resolved/leaning).

**Active tasks** (Phase 3, see IMPLEMENTATION.md):
- [ ] GEDCOM tooling (Gramps?) → load people (now 92 distinct; honor the A15 redirect) **+ places** (`data/places.md`, DEC-010) — **deferred until further notice** (Philip, 2026-10-27: "not crucial right now")
- [ ] Resolve/annotate every CF-## (`data/conflicts.md`): CF-30 closed; **CF-20 (Abram's children) is now the big open one** — Pola's information is the key
- [ ] **Tree refresh against the index** — `data/family-tree.md` lags (A07 "alive 1966" → 1973 Israel; A27–A29 not drawn; only diagram 1 shows the second marriages)
- (Phase 4): family outreach — **stream live** (Philip); chase: Pola (CF-20), Sara Jarovinsky's death year (not in Mania's 1969 obit mourners — d. 1964–69?), Felipe's own death notice (~1959/60), Carol Ackerman's marriage year; then JRI Kurow/Warsaw, NHAB pulls, USA records.

**Blockers**: None technical. Family-input items keep arriving — take them as they come (cite `[C — Philip, date]`; approximate years `[L]`).

**Key facts for orientation**:
- `data/people.md` is the deliverable: every entry has citations + [C]/[L]/[?] marks; conventions in its header. Read it before anything else. `data/prensa-hits.md` + `data/pinkas-hits.md` hold the two big extraction passes; `data/places.md` the gazetteer.
- **Rules added this round**: no pictograph emoji anywhere (DEC-011; check marks fine); merged person IDs become redirects, never reused (DEC-012). Family input is cited `[C — Philip, YYYY-MM-DD]`; living people get names only (no publication outside the repo).
- **Posts** (writing/, 4 EN+ES pairs, byline per DEC-009): 01 orientation · 02 Pinkas · 03 Sapotnitsky · 04 the Prensa story (carries a dated postscript — corrections are shown, not hidden). Facts in posts trace only to `data/`.
- **Places** (DEC-010): `places.md` is the only hand-edited place file; regenerate `places.geojson`/`.kml` with `python3 scripts/places-to-geojson.py`. Ostrov = near Slutsk; Kurow = Kurów (Lublin). Open: Urechye discrepancy; Oreitsa/Laseh/Ozdeh un-geocoded.
- UFDC citable pattern: `ufdcimages.uflib.ufl.edu/AA/00/06/55/27/{vol}/{img}.jpg` + same-path `.txt` OCR; the Notes' `NN/NNx` citations do NOT map to image numbers. Prensa prints Hebrew names (Anita=Ana, Pesele=Pola, Hinde=Aida, Sara/Sarita=Consuelo "Chelo") — CF-23.
- Big corrections to date: Israel b. 1880; Nakhman alive ≥1932; Lyubka/Etl = Israel's sisters; Rachmeil=Mendel=Manuel Glatt (CF-16); Mania = Felipe's widow = Chana Mindel Bauman (CF-30); Sara Jarovinsky = Mania's sister, not Felipe's; Chelo = Consuelo.
- Grandparent-corner mysteries still open: **Sapotnitsky** (`docs/investigations/sapotnitsky.md`, program §8–9 incl. Nesvizh + Minkov lead EV-79) and **CF-20** (Abram's children). CF-30 is closed.

**Next session**: Read this + `data/people.md` header; candidates: Phase 3 GEDCOM tooling (people + places ready), the tree refresh, the migration-route map layer (MAPPING-PLAN "Deferred v2+"), Sapotnitsky §8–9, or CF-20 via Pola. Ask Philip which — and expect more family input mid-session (record + commit per batch, no full wrap-up until asked). Wrap-up runs the session-wrapup skill (chronicle next entry = 19).

**Map**: data/people.md · data/conflicts.md · data/evidence-log.md · data/prensa-hits.md · data/pinkas-hits.md · data/places.md + places.geojson/.kml + scripts/ · data/family-tree.md · writing/ (4 EN+ES posts) · README "What's New" + posts table · CLAUDE.md (hard rules) · docs/MAPPING-PLAN.md · docs/investigations/sapotnitsky.md · docs/FAMILY-OVERVIEW.md · docs/SOURCE-SURVEY.md · docs/ROADMAP.md · docs/RESOURCES.md · docs/DECISIONS.md (DEC-011/012 new) · docs/IMPLEMENTATION.md · docs/chronicles/.
