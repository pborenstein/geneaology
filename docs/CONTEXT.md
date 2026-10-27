---
phase: 2 (complete); 3 in progress (place authority + tree refresh done; GEDCOM deferred); 4 live
updated: 2026-10-27
last_commit: 55f1e41
last_entry: chronicles/phase-2-extraction.md #19
---

# Context — Borenstein/Mostkoff Genealogy

**Project**: Well-sourced genealogy of the Borenstein/Mostkoff family — Wendy Cadieux (research) & Philip Borenstein (tech). Sources: 10 PDFs in `base-documents/` (2,265 pp, fully extracted) + tania-project.com memoir + UFDC Prensa Israelita (EV-59–80) + **family input** (Philip live since 2026-10-19; **Ana Caddess round 2026-10-27**). Repo: github.com/pborenstein/geneaology.

**Current focus**: **2026-10-27 — Ana's papelitos batch, tree regeneration, post updates (entry 19).** By email via Philip: **Felipe d. Sunday 23 Aug 1959** (A05; unveiling 14 Aug 1960 = ~11.7 months ✓; notice hunt narrowed to the late-Aug/early-Sep 1959 Prensa issues); **Mania's parents = Zvi & Shoshanah Bauman, Chlodna 38, Warsaw** (new A30/A31; Ana's information via Avram Bromberg, 2004; the Notes' "Herz Bauman" gravestone lead ≈ Zvi — Herz is the Yiddish form of Tzvi); **CF-02 resolved** (Israel d. 1 Oct 1957; Ana recalls Sept 1957); **CF-21 resolved** (Shifra d. 24 Sep 1962; Ana's hospital memory); new lead: Consuelo survived Luis by ~10 years — neither death date known. **Tree regenerated against the index** (Bauman + Jarovinsky branches drawn; all flagged lags cleared; mermaid compile-checked). Post 04 EN/ES gained a second dated postscript; post 01's method example updated. **GEDCOM tooling deferred until further notice** (Philip). People **92 distinct** / CF-01–31 (**12 resolved/leaning**).

**Active tasks** (see IMPLEMENTATION.md):
- [ ] **CF-20 (Abram's children)** — the big open conflict; Pola's information is the key
- [ ] Phase 4 family chases: Pola (CF-20) · Sara Jarovinsky's death year (d. 1964–69?) · **Luis & Consuelo death dates** · **who was Avram Bromberg?** · Felipe's printed death notice (UFDC issues ~29 Aug / 5 Sep 1959) · JOWBR re-checks (Israel's engraved date, J_MEXICO_0002150; the Herz/Zvi Bauman stone)
- [ ] GEDCOM tooling (Gramps?) — **deferred until further notice** (Philip, 2026-10-27)
- (Phase 4 records queue): JRI Kurow/Warsaw (incl. Warsaw Bauman gravestones), NHAB pulls, USA records

**Blockers**: None technical. Family input keeps arriving — record per batch (`[C — <name> (email via Philip), date]`; approximate years `[L]`), commit per batch, no full wrap-up until asked.

**Key facts for orientation**:
- `data/people.md` is the deliverable: every entry has citations + [C]/[L]/[?] marks; conventions in its header (family-input citation form added 2026-10-27). Read it before anything else. `data/prensa-hits.md` + `data/pinkas-hits.md` hold the two big extraction passes; `data/places.md` the gazetteer; `data/family-tree.md` **regenerated 2026-10-27** — re-verify against the index whenever it changes.
- **Rules**: no pictograph emoji anywhere (DEC-011; check marks fine); merged person IDs become redirects, never reused (DEC-012); living people get names only (no publication outside the repo); corrections are shown, not hidden.
- **Posts** (writing/, 4 EN+ES pairs, byline per DEC-009): 01 orientation · 02 Pinkas · 03 Sapotnitsky · 04 the Prensa story — now with **two** dated postscripts (19 Oct, 27 Oct). Facts in posts trace only to `data/`.
- **Places** (DEC-010): `places.md` is the only hand-edited place file; regenerate `places.geojson`/`.kml` with `python3 scripts/places-to-geojson.py`. Warsaw = P19 (A30/A31 at Chlodna 38 noted). Open: Urechye discrepancy; Oreitsa/Laseh/Ozdeh un-geocoded.
- UFDC citable pattern: `ufdcimages.uflib.ufl.edu/AA/00/06/55/27/{vol}/{img}.jpg` + same-path `.txt` OCR. Prensa prints Hebrew names (Anita=Ana, Pesele=Pola, Hinde=Aida, Sara/Sarita=Consuelo "Chelo") — CF-23.
- Big corrections to date: Israel b. 1880; Nakhman alive ≥1932; Lyubka/Etl = Israel's sisters; Rachmeil=Mendel=Manuel Glatt (CF-16); Mania = Chana Mindel Bauman (CF-30); Sara Jarovinsky = Mania's sister; Chelo = Consuelo; **Felipe d. 23 Aug 1959; Mania's parents Zvi & Shoshanah Bauman of Warsaw**.
- Grandparent-corner mysteries still open: **Sapotnitsky** (`docs/investigations/sapotnitsky.md`, program §8–9 incl. Nesvizh + Minkov lead EV-79) and **CF-20** (Abram's children). CF-30/02/21 closed.

**Next session**: Read this + `data/people.md` header; candidates: **Felipe's death-notice hunt** (the UFDC window is now tight — issues of ~29 Aug / 5 Sep 1959), CF-20 via Pola, Sapotnitsky §8–9, the migration-route map layer (MAPPING-PLAN "Deferred v2+"), or Warsaw pulls (Bauman gravestones / Chlodna 38 context). Ask Philip which — and expect more family input mid-session (record + commit per batch, no full wrap-up until asked). Wrap-up runs the session-wrapup skill (chronicle next entry = 20).

**Map**: data/people.md · data/conflicts.md · data/evidence-log.md · data/prensa-hits.md · data/pinkas-hits.md · data/places.md + places.geojson/.kml + scripts/ · data/family-tree.md (fresh 2026-10-27) · writing/ (4 EN+ES posts) · README "What's New" + posts table · CLAUDE.md (hard rules: conventional commits + push) · docs/MAPPING-PLAN.md · docs/investigations/sapotnitsky.md · docs/FAMILY-OVERVIEW.md · docs/SOURCE-SURVEY.md · docs/ROADMAP.md · docs/RESOURCES.md · docs/DECISIONS.md (thru DEC-012) · docs/IMPLEMENTATION.md · docs/chronicles/.
