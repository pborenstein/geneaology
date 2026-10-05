# Implementation Tracker — Borenstein/Mostkoff Genealogy

*Phase progress. Current state lives in CONTEXT.md; full history in chronicles/.*

## Phase overview

| # | Phase | Status | Chronicle |
|---|---|---|---|
| 1 | Source survey & project setup | ✅ Complete (2026-10-05) | chronicles/phase-1-survey.md |
| 2 | Master extraction (person/fact index) | Not started | — |
| 3 | Tree assembly (GEDCOM + charts) | Not started | — |
| 4 | Targeted research (mysteries & records) | Not started (can overlap 2–3) | — |
| 5 | Publication | Not started | — |

## Phase 1: Source survey & project setup ✅

- [x] Inventory 9 PDFs (121 pages); extract text layers → `extracted-text/`
- [x] Read/skim all sources; characterize each (docs/SOURCE-SURVEY.md)
- [x] Draft state-of-knowledge synthesis with confidence markers (docs/FAMILY-OVERVIEW.md)
- [x] Write roadmap with phases, principles, definition of done (docs/ROADMAP.md)
- [x] Set up tracking: docs/, CONTEXT.md, DECISIONS.md, chronicles/
- [x] Repo created and pushed to GitHub; PDFs archived in `base-documents/` (by Philip, post-survey)
- Not done (deliberately): full page-by-page extraction of the 71-page Narrative (Phase 2 work); image extraction; contacting anyone.

## Phase 2: Master extraction — next up

Plan of attack (details in ROADMAP.md):

- [ ] Decide data format for `data/people.*` (markdown index vs. CSV) — DEC-004
- [ ] Create `data/` with people index, conflicts log, evidence log
- [ ] Extraction pass 1: Mostkoff Family Narrative.pdf (master)
- [ ] Extraction pass 2: Borenstein Mostkoff Notes.pdf
- [ ] Extraction pass 3: Tanya material — Wendy's summary + memoir excerpts (MOSTKOFF.pdf) + **full memoir** (tania-project.com English translation, see RESOURCES.md)
- [ ] Extraction pass 4: record collections (chronicle, Slutsk Links, SUPONITZKY, Genealogy draft's Polak/Borukovich tree)
- [ ] Extraction pass 5: Borenstein family timeline (dates)
- [ ] Cross-check: every person in FAMILY-OVERVIEW appears in the index; every index entry cites sources
- [ ] Update FAMILY-OVERVIEW.md to sourced version; refresh CONTEXT.md

## Phase 3: Tree assembly (high level)

Decide GEDCOM tooling (Gramps?) → load reconciled people → resolve conflicts → charts + regenerated GEDCOM → updated overview.

## Phase 4: Targeted research (high level)

Priority order: UFDC Prensa Israelita links → family outreach (Pola, memoir, old trees) → JRI-Poland Kurow/Warsaw → Minsk archive pull (1889 marriage) → USA records (Arizona crossing, Mississippi/Memphis) → Shoah databases. Mystery list maintained in FAMILY-OVERVIEW.md.

## Phase 5: Publication (high level)

Format decision with Wendy/Philip (PDF book / website / GEDCOM) → assemble from Phase 2/3 data → photos from Narrative → source appendix + open questions.
