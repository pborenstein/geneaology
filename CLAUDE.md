# CLAUDE.md — agent instructions

Genealogy research project (not a code project): assembling the Borenstein/Mostkoff family history from Wendy's PDF research notes. See README.md for layout and docs/ROADMAP.md for the plan.

## Session pickup

1. Read **docs/CONTEXT.md** first (hot state, <50 lines) — current focus, active tasks, blockers.
2. Read the current-phase section of **docs/IMPLEMENTATION.md**.
3. Session end: run the session-wrapup skill — update CONTEXT.md, check off IMPLEMENTATION.md tasks, add a chronicle entry if meaningful work was done (next entry number = max across `docs/chronicles/*.md` + 1), add DEC-XXX for real decisions, commit.
4. **README.md is the repo's entry portal and must never go stale** — at session end, refresh its "Snapshot" section (phase, people/evidence/conflict counts, corpus notes, queued research) and update the repository map / start-here table if paths, docs, or conventions changed.

## Hard rules

- **Never modify anything in `base-documents/`** — the PDFs are archival sources (DEC-002).
- `extracted-text/` is derived and regenerable (`pdftotext -layout`); never hand-edit it — regenerate instead.
- Every new fact gets a **citation** (source PDF + page, URL, or archive fond) and a **confidence mark**: `[C]` confirmed by record, `[L]` likely, `[?]` open question (DEC-003).
- Every person keeps an **alias list** (Hebrew/Yiddish/secular/Mexican/nicknames + transcription variants). Never merge two same-named people without corroborating — cross-branch name collisions are common in this family.
- Disagreements between sources go in `data/conflicts.md` once it exists; don't silently resolve them.
- `data/family-tree.md`: Mermaid closing fences must sit at column 0 (4+ leading spaces makes CommonMark treat them as block content, silently breaking GitHub's rendering).
- This is family history: living people are in the tree. Keep research in this repo; don't publish details about living relatives anywhere external without explicit instruction.

## Tooling

- `pdftotext` / `pdfinfo` are installed; `qpdf` and Python PDF libs are not. Grep `extracted-text/` for content; open the PDF in `base-documents/` only when page-accurate citation or images matter.
- Shell cwd resets to the ZCode workspace between commands — `cd /Users/philip/projects/geneaology` (or use absolute paths) in each command.
- Repo: `git@github.com:pborenstein/geneaology.git`, branch `main`. Commit doc/data changes with conventional-commit messages and push.

## Project facts worth knowing

- Three lines converge in Mexico City: Borenstein (Kurow, Poland), Mostkoff (Slutsk, Belarus), Polak/Borukovich (Minsk/Slutsk). Philip and Edna/Jaye are children of Joseph Borenstein and Ana Mostkoff Linares.
- The master source is `base-documents/Mostkoff Family Narrative.pdf` (71 pp); the other 8 PDFs are satellite notes. Survey: docs/SOURCE-SURVEY.md; current picture + mysteries: docs/FAMILY-OVERVIEW.md.
- Next phase (2): master extraction into `data/` — format decision pending (DEC-004, leaning markdown people index, GEDCOM at Phase 3).
