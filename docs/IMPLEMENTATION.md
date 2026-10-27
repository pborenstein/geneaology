# Implementation Tracker — Borenstein/Mostkoff Genealogy

*Phase progress. Current state lives in CONTEXT.md; full history in chronicles/.*

## Phase overview

| # | Phase | Status | Chronicle |
|---|---|---|---|
| 1 | Source survey & project setup | ✅ Complete (2026-10-05) | chronicles/phase-1-survey.md |
| 2 | Master extraction (person/fact index) | ✅ Complete (2026-10-10); Pinkas + Prensa passes added 2026-10-13/14 | chronicles/phase-2-extraction.md |
| 3 | Tree assembly (GEDCOM + charts) | In progress — place authority (2026-10-14) + tree refresh (2026-10-27) done; **GEDCOM deferred** (2026-10-27) | chronicles/phase-2-extraction.md #16, #19 |
| 4 | Targeted research (mysteries & records) | In progress — Prensa mined (2026-10-14); family-input stream live (Philip 2026-10-19; **Ana's round 2026-10-27**) | chronicles/phase-2-extraction.md #15, #18, #19 |
| 5 | Publication | Not started | — |

## Phase 1: Source survey & project setup ✅

- [x] Inventory 9 PDFs (121 pages); extract text layers → `extracted-text/`
- [x] Read/skim all sources; characterize each (docs/SOURCE-SURVEY.md)
- [x] Draft state-of-knowledge synthesis with confidence markers (docs/FAMILY-OVERVIEW.md)
- [x] Write roadmap with phases, principles, definition of done (docs/ROADMAP.md)
- [x] Set up tracking: docs/, CONTEXT.md, DECISIONS.md, chronicles/
- [x] Repo created and pushed to GitHub; PDFs archived in `base-documents/` (by Philip, post-survey)
- Not done (deliberately): full page-by-page extraction of the 71-page Narrative (Phase 2 work); image extraction; contacting anyone.

## Phase 2: Master extraction — COMPLETE (2026-10-10)

Plan of attack (details in ROADMAP.md):

- [x] Decide data format — single markdown index `data/people.md` (DEC-004, decided 2026-10-10)
- [x] Create `data/` with people index, conflicts log, evidence log
- [x] Extraction pass 1: Mostkoff Family Narrative.pdf (master) — NB pp. 38–71 duplicate pp. 1–37
- [x] Extraction pass 2: Borenstein Mostkoff Notes.pdf
- [x] Extraction pass 3: Tanya material — summary + MOSTKOFF.pdf + full memoir (§-cited)
- [x] Extraction pass 4: record collections (chronicle, Slutsk Links, SUPONITZKY, Genealogy draft)
- [x] Extraction pass 5: Borenstein family timeline (dates)
- [x] Cross-check: every person in FAMILY-OVERVIEW appears in the index; every index entry cites sources (2026-10-10)
- [x] Update FAMILY-OVERVIEW.md to sourced version; refresh CONTEXT.md (2026-10-10)

## Phase 3: Tree assembly (high level)

Decide GEDCOM tooling (Gramps?) → load reconciled people → resolve conflicts → charts + regenerated GEDCOM → updated overview. **Place authority: done 2026-10-14** (`data/places.md` gazetteer + generated `places.geojson`/`.kml`, DEC-010 — see docs/MAPPING-PLAN.md for the deferred migration-route layer, Leaflet family map, and GEDCOM place strings). **Tree: regenerated against the index 2026-10-27** (Bauman grandparents A30/A31 + the Jarovinsky branch drawn; all flagged lags cleared; mermaid compile-checked — see entry #19). **GEDCOM load: deferred until further notice** (Philip, 2026-10-27 — "not crucial right now"). **Conflicts**: CF-30 resolved 2026-10-19 (A15 merged into A06 — DEC-012); CF-02 & CF-21 resolved 2026-10-27 (Ana's round); CF-20 (Abram's children) is the big open one.

## Phase 4: Targeted research (high level)

Priority order: ~~UFDC Prensa Israelita links~~ **✅ mined 2026-10-14** (EV-59–80, `data/prensa-hits.md`) → family outreach — **stream live** (Philip 2026-10-19, CF-30 closed; **Ana Caddess 2026-10-27**: Felipe d. 23 Aug 1959, Bauman grandparents found, CF-02/21 closed — entry #19; still to chase: **Pola for CF-20**, Sara Jarovinsky's death year, **Luis & Consuelo death dates**, **who was Avram Bromberg**, Felipe's printed death notice — now narrowed to the late-Aug/early-Sep 1959 issues) → JRI-Poland Kurow/Warsaw (incl. Bauman/Warsaw-cemetery gravestones) → Minsk archive pull (1889 marriage) → USA records (Arizona crossing, Mississippi/Memphis) → Shoah databases. Mystery list maintained in FAMILY-OVERVIEW.md.

## Phase 5: Publication (high level)

Format decision with Wendy/Philip (PDF book / website / GEDCOM) → assemble from Phase 2/3 data → photos from Narrative → source appendix + open questions.
