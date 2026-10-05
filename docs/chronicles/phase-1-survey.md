# Chronicle — Phase 1: Source Survey & Project Setup

## Entry 1: Surveyed the corpus, set up tracking (2026-10-05)

**What**: Inventoried and read all 9 PDFs (121 pages, ~166 KB text), extracted text layers, wrote the source survey, a draft state-of-knowledge family overview, and the roadmap; established this tracking system.

**Why**: First step of the project — understand what source material exists and how to get from it to a solid Borenstein/Mostkoff genealogy (Wendy's research; she is Philip Borenstein's partner).

**How**:
- `pdftotext -layout` on all 9 PDFs → `extracted-text/` (one .txt each; all had usable text layers)
- Read 8 sources in full; sampled the 71-page Narrative (intro, family section, headings) — full read deferred to Phase 2
- Synthesized the three ancestral lines and their convergence (Joseph Borenstein m. Ana Mostkoff Linares, Philip's parents' generation) in docs/FAMILY-OVERVIEW.md with [C]/[L]/[?] confidence marks
- Compiled the 10-item open-mysteries list; ordered research priorities in docs/ROADMAP.md
- Set up docs/ tracking per the project-tracking skill

**Decisions**: DEC-001 (tracking structure), DEC-002 (PDFs archival; Narrative = master doc), DEC-003 (confidence marks + citations), DEC-004 opened (Phase 2 data format).

**Files**: docs/{SOURCE-SURVEY,FAMILY-OVERVIEW,ROADMAP,IMPLEMENTATION,DECISIONS,CONTEXT}.md; docs/chronicles/phase-1-survey.md; extracted-text/*.txt

## Entry 2: Project infrastructure — git repo, base-documents/, GitHub (2026-10-05)

**What**: PDFs moved from the project root into `base-documents/`; repository initialized and pushed to `github.com:pborenstein/geneaology` (initial commit ca30b03). Docs updated to match the new layout.

**Why**: Give the archival PDFs a permanent home, put the project under version control, and make it shareable/backup-safe before Phase 2 starts generating data files.

**How**:
- 9 PDFs relocated to `base-documents/` (untouched content-wise)
- `git init` + remote + push by Philip; working tree clean at ca30b03
- CONTEXT.md / SOURCE-SURVEY.md path references updated; IMPLEMENTATION.md Phase 1 extended

**Decisions**: DEC-005 (base-documents/ as archival home; repo layout).

**Files**: docs/{CONTEXT,SOURCE-SURVEY,IMPLEMENTATION,DECISIONS}.md; this file

## Entry 3: Repo docs, AI provenance, and The Tania Project (2026-10-05)

**What**: Added README.md (front door: intro, layout rules, docs guide, conventions) and CLAUDE.md (agent rules: pickup protocol, hard rules, tooling); recorded AI provenance in the README; created docs/RESOURCES.md and registered **The Tania Project** — the full text of Tania Mostkoff's memoir (Russian transcription, English + Spanish translations, places gazetteer) at tania-project.com / github.com/pborenstein/tania-project.

**Why**: Make the repo self-explanatory and agent-safe; make AI assistance traceable; and stop treating Tania's memoir as missing material — it is a primary source now in hand for the Mostkoff line and Slutsk life.

**How**:
- Provenance verified from the session DB via acnehuatl (`~/projects/nahuatl-PROJECTS/acnehuatl`), not self-reported: GLM-5.3, ZCode harness
- "Memoir missing" mentions corrected in CONTEXT/SOURCE-SURVEY/ROADMAP/FAMILY-OVERVIEW; Phase 2 pass 3 now points at the site's English translation
- RESOURCES.md established as the registry for standalone external resources

**Decisions**: DEC-006 (RESOURCES.md registry), DEC-007 (AI provenance practice).

**Files**: README.md, CLAUDE.md, docs/{RESOURCES,CONTEXT,SOURCE-SURVEY,ROADMAP,FAMILY-OVERVIEW,IMPLEMENTATION,DECISIONS}.md, this file; commits 54e9dd6, b35c848, 73cffa5 + this wrap-up commit
