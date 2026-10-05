---
phase: 2 (not started)
updated: 2026-10-05
last_commit: ca30b03
last_entry: chronicles/phase-1-survey.md #2
---

# Context — Borenstein/Mostkoff Genealogy

**Project**: Build a solid, well-sourced genealogy of the Borenstein/Mostkoff family from Wendy's (Philip Borenstein's partner's) research. Sources: 9 PDFs in `base-documents/` (121 pp); git repo, remote `github.com:pborenstein/geneaology`.

**Current focus**: Phase 1 (survey & setup) complete. Phase 2 (master extraction) is next: build `data/` person index from all sources.

**Active tasks** (Phase 2, see IMPLEMENTATION.md):
- [ ] Decide people-index format (DEC-004: leaning markdown-first, GEDCOM at Phase 3)
- [ ] Create data/people, data/conflicts, data/evidence-log
- [ ] Extraction passes: Narrative → Notes → Tanya material → record collections → timeline

**Blockers**: None technical. Worth asking Wendy/Philip early (feeds Phase 4): Pola's information; the rest of Wendy's "hundreds of pages of notes and photographs"; Philip's old rough genealogy; any Ancestry/MyHeritage/Geni tree exports. (Tania's full memoir is no longer missing — it's online, see docs/RESOURCES.md.)

**Key facts for orientation**:
- Three lines converge in Mexico City: Borenstein (Kurow, Poland), Mostkoff (Slutsk/Ostrov, Belarus), Polak/Borukovich (Minsk/Slutsk). Philip & Edna/Jaye are children of Joseph Borenstein (b. 1936) and Ana Mostkoff Linares (dau. of Luis Mostkoff & Chelo Linares Lopez).
- Master source = "Mostkoff Family Narrative.pdf" (71 pp); everything else is satellite notes.
- Confidence marks everywhere: [C] record-confirmed, [L] likely, [?] open.

**Next session**: Read this file + IMPLEMENTATION.md Phase 2 section; start with the DEC-004 format decision, then extraction pass 1 (Narrative) using `extracted-text/` for grepping and `base-documents/` PDFs for page-accurate citations.

**Map**: docs/SOURCE-SURVEY.md (what the PDFs are) · docs/FAMILY-OVERVIEW.md (what we know + mysteries) · docs/ROADMAP.md (how we get there) · docs/DECISIONS.md · docs/IMPLEMENTATION.md · docs/chronicles/
