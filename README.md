# Borenstein/Mostkoff Family Genealogy

Building a solid, well-sourced genealogy of the **Borenstein/Mostkoff family**, from the research of Wendy (partner of Philip Borenstein), who began the project in 2020.

The family is three lines converging in Mexico City, where Joseph Borenstein (b. 1936) married Ana Mostkoff Linares:

- **Borenstein** — Kurow, Lublin gubernia, Poland (→ Warsaw → Mexico City)
- **Mostkoff** — Slutsk/Ostrov/Nesvizh region, Belarus (→ Mississippi interlude → Mexico City)
- **Polak/Borukovich** — Minsk/Slutsk, Belarus (Shifra Borukhovich m. Israel Mostkoff)

## Status

Phase 1 (source survey & project setup) is complete. Phase 2 (master extraction into a person/fact index) is next. See [docs/ROADMAP.md](docs/ROADMAP.md) for the full plan.

## Repository layout

| Path | Contents | Rule |
|---|---|---|
| `base-documents/` | The 9 source PDFs (121 pages): Wendy's master narrative, research notes, memoir summaries, record extracts | **Archival — never modified** |
| `extracted-text/` | One `.txt` per PDF (via `pdftotext -layout`) | Derived — safe to regenerate anytime |
| `docs/` | Tracking & planning docs (below) | Actively maintained |
| `data/` | Structured person/fact output (Phase 2) | Not yet created |

## Navigating the docs

- **[docs/CONTEXT.md](docs/CONTEXT.md)** — start here: current session state, what's next
- [docs/SOURCE-SURVEY.md](docs/SOURCE-SURVEY.md) — what each source PDF is and its role
- [docs/FAMILY-OVERVIEW.md](docs/FAMILY-OVERVIEW.md) — state of knowledge: the three lines, confidence-marked, plus the open-mysteries list
- [docs/ROADMAP.md](docs/ROADMAP.md) — the phased plan from sources to final genealogy
- [docs/RESOURCES.md](docs/RESOURCES.md) — external resources (incl. the full text of Tania Mostkoff's memoir at [tania-project.com](https://www.tania-project.com/))
- [docs/IMPLEMENTATION.md](docs/IMPLEMENTATION.md) — phase-by-phase progress tracker
- [docs/DECISIONS.md](docs/DECISIONS.md) — project decisions (DEC-001…)
- [docs/chronicles/](docs/chronicles/) — session history

## Conventions

- **Confidence marks** on every fact: `[C]` record-confirmed, `[L]` likely, `[?]` open question.
- **Citations** accompany facts: source PDF + page, URL, or archive fond/reference.
- **Alias lists** per person: Hebrew / Yiddish / secular / Mexican / nickname / transcription variants (naming conventions are this family's hardest problem — see the intro of the master narrative).
- `extracted-text/` can be rebuilt with:
  ```sh
  for f in base-documents/*.pdf; do pdftotext -layout "$f" "extracted-text/$(basename "${f%.pdf}").txt"; done
  ```

## Provenance

The Phase 1 survey and planning docs (2026-10-05) were generated with the assistance of **GLM-5.3** (provider `account:zai-individual-coding-plan`) in the **ZCode** harness — verified via [acnehuatl](https://github.com/pborenstein/acnehuatl), a cwd-keyed session-provenance tool, not self-reported.
