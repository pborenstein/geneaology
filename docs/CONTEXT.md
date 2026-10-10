---
phase: 2 (complete)
updated: 2026-10-10
last_commit: 9b71601
last_entry: chronicles/phase-2-extraction.md #4
---

# Context — Borenstein/Mostkoff Genealogy

**Project**: Well-sourced genealogy of the Borenstein/Mostkoff family from Wendy's research. Sources: 9 PDFs in `base-documents/` (121 pp, fully extracted) + tania-project.com memoir. Repo: github.com/pborenstein/geneaology.

**Current focus**: **Phase 2 (master extraction) is COMPLETE** — `data/` now holds the full person index (77 people, A/B/C/X lines), evidence log (EV-01–49), and conflicts log (26 entries, CF-01–28). Phase 3 (tree assembly) is next; Phase 4 research can start anytime.

**Active tasks** (Phase 3, see IMPLEMENTATION.md):
- [ ] Decide GEDCOM tooling (Gramps?) → load reconciled people from `data/people.md`
- [ ] Resolve/annotate every CF-## in `data/conflicts.md` (6 already resolved/leaning)
- (Phase 4, parallel): mine the ~30 UFDC Prensa Israelita links (EV-35) — cheapest wins

**Blockers**: None technical. Family-input items (feed Phase 4): Pola's information; Wendy's remaining hundreds of pages of notes/photos; Philip's old rough genealogy; any Ancestry/MyHeritage/Geni GEDCOM exports.

**Key facts for orientation**:
- `data/people.md` is the deliverable: every entry has citations + [C]/[L]/[?] marks; conventions & citation keys in its header. Read it before anything else.
- Narrative PDF pp. 38–71 duplicate pp. 1–37 (cite first-copy pages). Tania's memoir cited as `tania-project (§N)`; repo cloned to /tmp only (copyright — never commit it).
- Big corrections this phase: Israel b. 1880; Nakhman alive ≥1932 (pinkas 1918 death re-attributed); Lyubka/Etl = Israel's sisters; Pesya-not-Chaya kidney-death memory; Rachmeil=Mendel=Manuel Glatt.
- 62 people ≈ every family-connected person in the corpus; background-only names live as lead notes in people.md's tail + EV-35.

**Next session**: Read this + `data/people.md` header; then either start Phase 3 (GEDCOM tooling decision, DEC pending) or the EV-35 UFDC mining pass — ask Philip which. Wrap-up runs the session-wrapup skill (chronicle next entry = 5).

**Map**: docs/FAMILY-OVERVIEW.md (sourced synthesis) · docs/SOURCE-SURVEY.md · docs/ROADMAP.md · docs/RESOURCES.md · docs/DECISIONS.md (DEC-004 decided) · docs/IMPLEMENTATION.md · docs/chronicles/.
