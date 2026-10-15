---
phase: 2 (complete); Phase 3 next
updated: 2026-10-14
last_commit: 5464b82
last_entry: chronicles/phase-2-extraction.md #15
---

# Context — Borenstein/Mostkoff Genealogy

**Project**: Well-sourced genealogy of the Borenstein/Mostkoff family — Wendy Cadieux (research) & Philip Borenstein (tech). Sources: 10 PDFs in `base-documents/` (2,265 pp, fully extracted) + tania-project.com memoir + UFDC Prensa Israelita (EV-59–80). Repo: github.com/pborenstein/geneaology.

**Current focus**: **EV-35 mined (2026-10-14)** — 22 Prensa Israelita notices → `data/prensa-hits.md` + EV-59–80. Headlines: CF-16 record-confirmed (Menahem Mendl Glatt d. 1965 at 68 = Mendel Borensztejn b. 1897 Kurow); **A06 corrected** ("Tía Mania" = Felipe's *widow*, d. 15 Jun 1969 → new CF-30 vs. Chana Mindel Bauman); Shifra's own obit ("Sofía Mostkoff", d. 24 Sep 1962 at 85 — CF-21/31); CF-23 resolved (Pesele=Pola, Hinde=Aida, Anita=Ana, Sara=Chelo); CF-15 leaning resolved (Lucy m. Harry Pepper, Memphis); Toibe's obit d. 1973 at 79 (= Kurow 1894 ✓) with Sheindl Glatt alive 1973 in Israel; new people A19–A29, X19–X21. **Writing series at 3 posts** (01 orientation · 02 Pinkas · 03 Sapotnitsky — EN+ES pairs each; bylines per DEC-009). Corpus: 90 people / EV-01–80 / CF-01–31.

**Active tasks** (Phase 3, see IMPLEMENTATION.md):
- [ ] Decide GEDCOM tooling (Gramps?) → load reconciled people from `data/people.md` (now incl. the Glatt/Jarovinsky/Mitelhaus lines)
- [ ] Resolve/annotate every CF-## in `data/conflicts.md` (9 now resolved/leaning; CF-30 Mania's identity is the big new one — Bauman-side records or family memory)
- (Phase 4 next): family outreach (Pola's information — now also the key to CF-20/CF-30), JRI Kurow/Warsaw, NHAB archive pulls, USA records. Residue: Felipe Borenstein's own death notice (~1959/60 Prensa issue unidentified).

**Blockers**: None technical. Family-input items (feed Phase 4): Pola's information (CF-20 + CF-30); Wendy's remaining notes/photos; Philip's old rough genealogy; any Ancestry/MyHeritage/Geni GEDCOM exports.

**Key facts for orientation**:
- `data/people.md` is the deliverable: every entry has citations + [C]/[L]/[?] marks; conventions & citation keys in its header. Read it before anything else. `data/prensa-hits.md` (§-organized) + `data/pinkas-hits.md` hold the two big extraction passes.
- UFDC citable pattern: `ufdcimages.uflib.ufl.edu/AA/00/06/55/27/{vol}/{img}.jpg` and same-path `.txt` OCR; the Notes' `NN/NNx` citations do NOT map to image numbers — relocate notices by searching full-issue OCR.
- Prensa prints Hebrew names (Anita=Ana, Pesele=Pola, Hinde=Aida, Sara=Chelo, Fishl=Felipe, Sheindl=Sheine Miriam) — the CF-23 frame, now proven.
- Big corrections: Israel b. 1880; Nakhman alive ≥1932; Lyubka/Etl = Israel's sisters; Rachmeil=Mendel=Manuel Glatt (CF-16 confirmed); Mania = Felipe's widow (not sibling).
- The three grandparent-corner mysteries remain open: Sapotnitsky (`docs/investigations/sapotnitsky.md`, program §8–9 incl. Nesvizh), CF-20 (Abram's children), CF-30 (Mania/Chana Mindel).

**Next session**: Read this + `data/people.md` header; candidates: Phase 3 (GEDCOM tooling decision — the tree is now much richer), the Sapotnitsky program §8–9 (Nesvizh records for Chaya; new Minkov lead EV-79), more `writing/` posts (the Prensa-mining story itself is post-04 material: "what the community paper remembered"), or CF-30 follow-up. Ask Philip which. Chase: Pola's information. Wrap-up runs the session-wrapup skill (chronicle next entry = 16).

**Map**: data/prensa-hits.md (Prensa extraction — new) · writing/ (family-facing posts, 3 pairs) · data/pinkas-hits.md · data/people.md · data/conflicts.md (CF-30/31 new) · docs/investigations/sapotnitsky.md · docs/FAMILY-OVERVIEW.md · docs/SOURCE-SURVEY.md · docs/ROADMAP.md · docs/RESOURCES.md · docs/DECISIONS.md · docs/IMPLEMENTATION.md · docs/chronicles/.
