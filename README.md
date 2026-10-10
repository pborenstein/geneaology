# Borenstein/Mostkoff Family Genealogy — Entry Portal

Building a solid, well-sourced genealogy of the **Borenstein/Mostkoff family**, from the research of Wendy (partner of Philip Borenstein), begun 2020. Three lines converge in Mexico City, where Joseph Borenstein (b. 1936) married Ana Mostkoff Linares:

- **Line A — Borenstein** (Kurow, Lublin gubernia, Poland → Warsaw → Mexico City)
- **Line B — Mostkoff** (Ostrov/Slutsk region, Belarus → Mississippi interlude → Mexico City)
- **Line C — Polak/Borukovich** (Minsk/Slutsk, Belarus — Shifra Boruchovich m. Israel Mostkoff)

> **This file is the navigation index for the whole repo.** It is refreshed at every session wrap-up (rule in [CLAUDE.md](CLAUDE.md)); if it's out of date, that's a bug.

## Start here — by what you want

| I want to… | Go to |
|---|---|
| See where the project stands & what's next | [docs/CONTEXT.md](docs/CONTEXT.md) (hot state, read first) · [docs/IMPLEMENTATION.md](docs/IMPLEMENTATION.md) (phase checklists) |
| Look up a person (any line, any spelling) | **[data/people.md](data/people.md)** — the deliverable: 77 entries, each with aliases, facts, citations, confidence |
| Check a known disagreement between sources | [data/conflicts.md](data/conflicts.md) — every open/resolved conflict (CF-##) |
| Verify a record (birth, marriage, pinkas, obit, ship…) | [data/evidence-log.md](data/evidence-log.md) — 49 records with archive fonds/URLs (EV-##) |
| Understand the family shape + open mysteries | [docs/FAMILY-OVERVIEW.md](docs/FAMILY-OVERVIEW.md) — sourced synthesis over `data/` |
| Work with the source PDFs | [docs/SOURCE-SURVEY.md](docs/SOURCE-SURVEY.md) (what each PDF is) → `base-documents/` (archival) / `extracted-text/` (greppable) |
| Read Tania Mostkoff's memoir (primary source, Line B) | [tania-project.com](https://www.tania-project.com/) — registry entry in [docs/RESOURCES.md](docs/RESOURCES.md) |
| See the plan / phases | [docs/ROADMAP.md](docs/ROADMAP.md) |
| Find out *why* something is the way it is | [docs/DECISIONS.md](docs/DECISIONS.md) — DEC-001… · [docs/chronicles/](docs/chronicles/) — session-by-session history |
| Dig into a research theme (e.g. the Sapotnitsky name) | [docs/investigations/](docs/investigations/) — deep dives: corpus inventory + hypotheses + research programs |

## Repository map

| Path | Contents | Rule |
|---|---|---|
| `base-documents/` | The 9 source PDFs (87 pp): master narrative, research notes, memoir summaries, record extracts | **Archival — never modified** (sole exception to date: DEC-008 verified trim) |
| `extracted-text/` | One `.txt` per PDF (`pdftotext -layout`) | Derived — regenerate, never hand-edit |
| `data/` | **The deliverable**: `people.md` (person index), `conflicts.md` (CF-##), `evidence-log.md` (EV-##) | Actively maintained; every fact cited + confidence-marked |
| `docs/` | Tracking & planning (see table above); `docs/investigations/` = themed deep dives | Actively maintained |
| `CLAUDE.md` | Agent instructions: pickup routine, hard rules, tooling | Read before any automated session |

**Source key for citations** (full conventions in [data/people.md](data/people.md)): `Narrative, p. N` · `Notes, p. N` · `Tanya-summary, p. N` · `Genealogy draft, p. N` · `chronicle` / `Slutsk Links` / `MOSTKOFF` / `SUPONITZKY` / `timeline, p. N` — all referring to the same-named PDFs · `tania-project (§N)` = the memoir's English translation · `EV-##` / `CF-##` = the two `data/` logs.

## Snapshot (2026-10-10 — refreshed at each wrap-up)

| | |
|---|---|
| **Phase** | 2 (master extraction) **complete** → Phase 3 (tree assembly) next |
| **People index** | 77 people — A01–A18 · B01–B26 · C01–C16 · X01–X18 |
| **Evidence / conflicts** | EV-01…49 · CF-01…29 (27 entries, CF-18/19 unused; 6 resolved/leaning) |
| **Corpus** | 9 PDFs, 87 pp (Narrative trimmed 71→37 pp, DEC-008) + full memoir at tania-project.com |
| **Queued research** | ~30 UFDC Prensa Israelita links (EV-35) — Phase 4 priority 1 |

## Conventions (quick reference)

- **Confidence**: `[C]` record-confirmed · `[L]` likely · `[?]` open question (DEC-003).
- **Citations** on every fact: source + page / URL / archive fond. Never merge same-named people without corroboration — this family recycles names across branches (two Taybas, two Gindas, two Dorises).
- Rebuild the text layer with:
  ```sh
  for f in base-documents/*.pdf; do pdftotext -layout "$f" "extracted-text/$(basename "${f%.pdf}").txt"; done
  ```

## Provenance

Project documentation and data extraction are AI-assisted (**GLM-5.3**, provider `account:zai-individual-coding-plan`, **ZCode** harness), verified via [acnehuatl](https://github.com/pborenstein/acnehuatl) — a cwd-keyed session-provenance tool, not self-reported. The genealogical substance is Wendy's research; the errors, where they remain, are the machines'.
