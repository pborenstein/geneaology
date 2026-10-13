---
phase: 2 (complete); Phase 3 next
updated: 2026-10-13
last_commit: 47cdb35
last_entry: chronicles/phase-2-extraction.md #10
---

# Context — Borenstein/Mostkoff Genealogy

**Project**: Well-sourced genealogy of the Borenstein/Mostkoff family — Wendy Cadieux (research) & Philip Borenstein (tech). Sources: 9 PDFs in `base-documents/` (121 pp, fully extracted) + tania-project.com memoir. Repo: github.com/pborenstein/geneaology.

**Current focus**: Phase 2 stable + **Pinkas pass done (2026-10-13)**: the full Slutsk register (EV-50; extraction `data/pinkas-hits.md`) fixed the Bunin clan (X02: d. 11 Jan 1915, son Natan), found a 4th Polak child (Y' Leib), resolved CF-13 at full scale, and gave CF-17 a strong negative (Chaya is NOT in Slutsk — search Nesvizh). Corpus now 10 PDFs / 2,265 pp (77 people / EV-01–58 / CF-01–29 in `data/`). A **family-input stream has opened** (2026-10-13, Philip): Shifra Borenstein added as third child of Joseph & Ana; Isidoro spelling; Hebrew-names-in-Prensa frame → CF-23 partially resolved. Family facts are recorded like any source (`[C — Philip, date]`). Phase 3 or Phase 4 next.

**Active tasks** (Phase 3, see IMPLEMENTATION.md):
- [ ] Decide GEDCOM tooling (Gramps?) → load reconciled people from `data/people.md`
- [ ] Resolve/annotate every CF-## in `data/conflicts.md` (6 already resolved/leaning)
- (Phase 4, parallel): mine the ~30 UFDC Prensa Israelita links (EV-35) — cheapest wins

**Blockers**: None technical. Family-input items (feed Phase 4): Pola's information; Wendy's remaining hundreds of pages of notes/photos; Philip's old rough genealogy; any Ancestry/MyHeritage/Geni GEDCOM exports.

**Key facts for orientation**:
- `data/people.md` is the deliverable: every entry has citations + [C]/[L]/[?] marks; conventions & citation keys in its header. Read it before anything else.
- Narrative PDF trimmed 71→37 pp 2026-10-10 (DEC-008): the duplicated second copy removed after text+image parity proof; citations to pp. 1–37 unchanged; 71-pp original in git history. Tania's memoir cited as `tania-project (§N)`; cloned to /tmp only (never commit it).
- Big corrections this phase: Israel b. 1880; Nakhman alive ≥1932 (pinkas 1918 death re-attributed); Lyubka/Etl = Israel's sisters; Pesya-not-Chaya kidney-death memory; Rachmeil=Mendel=Manuel Glatt.
- 62 people ≈ every family-connected person in the corpus; background-only names live as lead notes in people.md's tail + EV-35.

**Next session**: Read this + `data/people.md` header; candidates: Phase 3 (GEDCOM tooling decision), the EV-35 UFDC mining pass, or the Sapotnitsky research program (docs/investigations/sapotnitsky.md §8 — archive pulls + JewishGen searches). Ask Philip which. Wrap-up runs the session-wrapup skill (chronicle next entry = 11). Family-input facts to chase: Pola's information; more names/dates from Philip's recollection.

**Map**: writing/ (family-facing posts — new) · data/pinkas-hits.md (Pinkas extraction) · data/family-tree.md (Mermaid family tree) · docs/investigations/sapotnitsky.md (name investigation, updated 2026-10-13) · docs/FAMILY-OVERVIEW.md (sourced synthesis) · docs/SOURCE-SURVEY.md · docs/ROADMAP.md · docs/RESOURCES.md · docs/DECISIONS.md (DEC-004 decided) · docs/IMPLEMENTATION.md · docs/chronicles/.
