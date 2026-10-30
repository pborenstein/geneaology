---
phase: 2 (complete); 3 in progress (place authority + tree refresh done; GEDCOM deferred); 4 live
updated: 2026-10-29
last_commit: 50bc4fa
last_entry: chronicles/phase-2-extraction.md #20
---

# Context — Borenstein/Mostkoff Genealogy

**Project**: Well-sourced genealogy of the Borenstein/Mostkoff family — Wendy Cadieux (research) & Philip Borenstein (tech). Sources: 10 PDFs in `base-documents/` (2,265 pp, fully extracted) + **`bobespassport/` (11 scans — first image-only source, 2026-10-29)** + tania-project.com memoir + UFDC Prensa Israelita (EV-59–80) + family input (Philip live since 2026-10-19; Ana Caddess rounds 2026-10-27 and — via her 2020 email-to-Wendy scans — 2026-10-29). Repo: github.com/pborenstein/geneaology.

**Current focus**: **2026-10-29 — Bobe's passport batch recorded (EV-81/82, entry 20).** **Shifra's 1928 Soviet exit passport** (bearer Мосткава Шыфра Нахманаўна / "Mostkoff Chifra"; b. 1878 Bobruisk dist.; issued Minsk 27 Nov 1928; exit Sebezh; manifest Leiba 14 / Michel 11 / Dvoyra 7 = B12/B13/B14, birth years now record-corroborated) — the Soviet half of the Jan 1929 Mexico arrival (EV-03). **Ketuba copy → Chelo's orthodox conversion** (new [C] fact; explains Prensa name Sara/Sarita). CF-31 now three-way (1880/1878/~1877); CF-06's key = the ketuba's unread Kislev year (5699 → religious marriage before Lucy's b. Mar 1939; 5700 → after). Machine reads keep `[?]` per DEC-013; inventory + eyes-on list in SOURCE-SURVEY §11.

**Active tasks** (see IMPLEMENTATION.md):
- [ ] Eyes-on scan verification (SOURCE-SURVEY §11): IMG_1924 (vision tool can't read it) · ketuba Kislev year (CF-06) · Bobruisk-vs-Mozyr word · Apr/Sep-1928 dates on IMG_1925 · Spanish entry stamps · the "young woman ~16–20" photo (IMG_1933)
- [ ] Phase 4 chases: Pola (CF-20) · Felipe's notice (late-Aug/early-Sep 1959 issues) · Luis & Consuelo death dates · who was Avram Bromberg · Sara Jarovinsky (d. 1964–69?) · Sapotnitsky §8–9
- [ ] GEDCOM tooling (Gramps?) — deferred until further notice (Philip, 2026-10-27)
- (Phase 4 records queue): JRI Kurow/Warsaw (incl. Bauman gravestones), NHAB pulls, USA records

**Blockers**: None technical. Family input keeps arriving — record per batch (`[C — <name>, date]`; DEC-013 forms), commit per batch, no full wrap-up until asked (last wrap-up: 2026-10-29, entry 20).

**Key facts for orientation**:
- `data/people.md` is the deliverable: citations + [C]/[L]/[?]; conventions in its header (family-input forms; `Bobe's passport, IMG_NNNN` key). `data/family-tree.md` regenerated 2026-10-27 (Shifra labels "b.1878/80" since 2026-10-29; no structural change since).
- **Rules**: no pictograph emoji (DEC-011); merged IDs = redirects (DEC-012); machine-read facts keep `[?]` until human verification (DEC-013); never modify `base-documents/`; living people names-only.
- **Posts** (writing/, 4 EN+ES pairs, byline DEC-009); facts in posts trace only to `data/`. The passport batch is obvious post material (first image-first source) — unwritten.
- **Places** (DEC-010): 43 entries, 40 geocoded (P43 Sebezh new). Regenerate geojson/kml with `python3 scripts/places-to-geojson.py` after edits.
- UFDC citable pattern: `ufdcimages.uflib.ufl.edu/AA/00/06/55/27/{vol}/{img}.jpg` + same-path `.txt` OCR. Prensa prints Hebrew names (Anita=Ana, Pesele=Pola, Hinde=Aida, Sara/Sarita=Consuelo) — CF-23.
- Big corrections to date: Israel b. 1880; Rachmeil=Mendel=Manuel Glatt (CF-16); Mania = Chana Mindel Bauman (CF-30); **Chelo = Consuelo, orthodox convert (EV-82)**; Felipe d. 23 Aug 1959; Mania's parents Zvi & Shoshanah Bauman, Chlodna 38 Warsaw; **Shifra b. 1878 per her own passport; the family's USSR exit Nov 1928–Jan 1929 via Sebezh**.

**Next session**: Read this + `data/people.md` header; candidates: **scan-verification sitting with Philip/Wendy** (the §11 [?] flags — esp. the ketuba year), Felipe's notice hunt, Sapotnitsky §8–9, the migration-route map layer (MAPPING-PLAN "Deferred v2+" — the passport just gave it its first documented route), or Warsaw pulls. Ask Philip which — and expect more family input mid-session. Wrap-up runs the session-wrapup skill (chronicle next entry = 21).

**Map**: data/people.md · data/conflicts.md · data/evidence-log.md (EV-01…82) · data/prensa-hits.md · data/pinkas-hits.md · data/places.md (P01–P43) + places.geojson/.kml + scripts/ · data/family-tree.md · writing/ (4 EN+ES posts) · README "What's New" + Snapshot (refreshed 2026-10-29) · CLAUDE.md (hard rules: conventional commits + push) · docs/MAPPING-PLAN.md · docs/SOURCE-SURVEY.md (§11 = passport inventory) · docs/investigations/sapotnitsky.md · docs/FAMILY-OVERVIEW.md · docs/ROADMAP.md · docs/RESOURCES.md · docs/DECISIONS.md (thru DEC-013) · docs/IMPLEMENTATION.md · docs/chronicles/.
