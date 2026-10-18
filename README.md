# Borenstein/Mostkoff Family Genealogy — Entry Portal

Building a solid, well-sourced genealogy of the **Borenstein/Mostkoff family** — **Wendy Cadieux (research)** & **Philip Borenstein (tech)**, begun 2020. Three lines converge in Mexico City, where Joseph Borenstein (b. 1936) married Ana Mostkoff Linares:

- **Line A — Borenstein** (Kurow, Lublin gubernia, Poland → Warsaw → Mexico City)
- **Line B — Mostkoff** (Ostrov/Slutsk region, Belarus → Mississippi interlude → Mexico City)
- **Line C — Polak/Borukovich** (Minsk/Slutsk, Belarus — Shifra Boruchovich m. Israel Mostkoff)

> **This file is the navigation index for the whole repo.** It is refreshed at every session wrap-up (rule in [CLAUDE.md](CLAUDE.md)); if it's out of date, that's a bug.

## Start here — by what you want

| I want to… | Go to |
|---|---|
| See where the project stands & what's next | [docs/CONTEXT.md](docs/CONTEXT.md) (hot state, read first) · [docs/IMPLEMENTATION.md](docs/IMPLEMENTATION.md) (phase checklists) |
| Look up a person (any line, any spelling) | **[data/people.md](data/people.md)** — the deliverable: 91 entries, each with aliases, facts, citations, confidence |
| **See the family tree visually** | [data/family-tree.md](data/family-tree.md) — 5 Mermaid diagrams (GitHub renders them natively): convergence overview + Lines A/B/C detail |
| Check a known disagreement between sources | [data/conflicts.md](data/conflicts.md) — every open/resolved conflict (CF-##) |
| Verify a record (birth, marriage, pinkas, obit, ship…) | [data/evidence-log.md](data/evidence-log.md) — 80 records with archive fonds/URLs (EV-##) |
| Understand the family shape + open mysteries | [docs/FAMILY-OVERVIEW.md](docs/FAMILY-OVERVIEW.md) — sourced synthesis over `data/` |
| Work with the source PDFs | [docs/SOURCE-SURVEY.md](docs/SOURCE-SURVEY.md) (what each PDF is) → `base-documents/` (archival) / `extracted-text/` (greppable) |
| Read Tania Mostkoff's memoir (primary source, Line B) | [tania-project.com](https://www.tania-project.com/) — registry entry in [docs/RESOURCES.md](docs/RESOURCES.md) |
| See the plan / phases | [docs/ROADMAP.md](docs/ROADMAP.md) |
| Find out *why* something is the way it is | [docs/DECISIONS.md](docs/DECISIONS.md) — DEC-001… · [docs/chronicles/](docs/chronicles/) — session-by-session history |
| Dig into a research theme (e.g. the Sapotnitsky name) | [docs/investigations/](docs/investigations/) — deep dives: corpus inventory + hypotheses + research programs |
| **Read the family-facing posts** | [writing/](writing/) — blog-style, for cousins, **in English & Spanish (MX)**: 01 project orientation · 02 what the Pinkas revealed · 03 the Sapotnitsky name · 04 what *Prensa Israelita* revealed (EN+ES pairs each). **Written by Z.ai GLM-5.3** (AI-drafted; DEC-009) |
| **Put the places on a map** | [data/places.md](data/places.md) — the place gazetteer (42 places, every fact cited) → generated [data/places.geojson](data/places.geojson) / [data/places.kml](data/places.kml): drop into [uMap](https://umap.openstreetmap.fr), geojson.io, QGIS, or Google Earth; each pin lists its people & events. Plan: [docs/MAPPING-PLAN.md](docs/MAPPING-PLAN.md) |

## What's New

*Newest first. The full session-by-session history lives in [docs/chronicles/](docs/chronicles/); decisions in [docs/DECISIONS.md](docs/DECISIONS.md).*

- **2026-10-18 — Fourth family post** 📰 — *The Paper That Knew Everyone* (EN+ES) tells the story of the *Prensa Israelita* mining round: the Hebrew-names key, the 1959 wedding portrait with Moscow's greetings, the Mania correction, Shifra as "Sofía," Toibe's plot — and the family asks (Felipe's missing death notice, Mania's other name, the Glatt surname, little Ydele, family clippings). Post 03 (EN+ES) now cross-links forward.
- **2026-10-14 — The family map** 🗺️ — Every place in the corpus is now a gazetteer entry ([data/places.md](data/places.md), 42 places from Slutsk to Mexico City) and a real map layer (`data/places.geojson` / `.kml`) viewable in uMap, QGIS or Google Earth, pins labeled with people & events and their citations. Two old questions settled by the sources themselves: the family's **Ostrov is the shtetl next to Slutsk**, and **Kurow is Kurów in Lublin**. Decisions in [docs/MAPPING-PLAN.md](docs/MAPPING-PLAN.md) (DEC-010).
- **2026-10-14 — The community paper, mined** 📰 — All 22 queued *Prensa Israelita* notices extracted → EV-59–80 ([data/prensa-hits.md](data/prensa-hits.md)). Headlines: **"Tía Mania" was Felipe's widow, not his sister** (new CF-30); Mendel = Manuel Glatt record-confirmed (CF-16); the Hebrew-vs-civil-names puzzle solved — Pesele=Pola, Hinde=Aida, Anita=Ana, Sara=Chelo (CF-23); Shifra's own obit found ("Sofía Mostkoff," 1962); 11 new people. Third family post live: *Three Names for One Grandmother* (EN+ES).
- **2026-10-13 — The Pinkas at full scale** 📖 — The entire 2,178-page Slutsk burial register extracted ([data/pinkas-hits.md](data/pinkas-hits.md)): grandmother Chaya is **not** in it — her trail moves to Nesvizh; the Bunin cousin-clan fixed; a fourth Polak child found. The writing series went **bilingual** (EN + ES-MX).

## Repository map

| Path | Contents | Rule |
|---|---|---|
| `base-documents/` | The 10 source PDFs (2,265 pp): master narrative, research notes, memoir summaries, record extracts, the full Slutsk Pinkas | **Archival — never modified** (sole exception to date: DEC-008 verified trim) |
| `extracted-text/` | One `.txt` per PDF (`pdftotext -layout`) | Derived — regenerate, never hand-edit |
| `data/` | **The deliverable**: `people.md` (person index) · `places.md` (place gazetteer) + generated `places.geojson`/`places.kml` (map layer) · `conflicts.md` (CF-##) · `evidence-log.md` (EV-##) · `family-tree.md` (Mermaid tree) · `pinkas-hits.md` · `prensa-hits.md` | Actively maintained; every fact cited + confidence-marked |
| `scripts/` | `places-to-geojson.py` — regenerates the map layer from `data/places.md` | Run after editing the gazetteer (`python3 scripts/places-to-geojson.py`) |
| `docs/` | Tracking & planning (see table above); `docs/investigations/` = themed deep dives | Actively maintained |
| `CLAUDE.md` | Agent instructions: pickup routine, hard rules, tooling | Read before any automated session |

**Source key for citations** (full conventions in [data/people.md](data/people.md)): `Narrative, p. N` · `Notes, p. N` · `Tanya-summary, p. N` · `Genealogy draft, p. N` · `chronicle` / `Slutsk Links` / `MOSTKOFF` / `SUPONITZKY` / `timeline, p. N` — all referring to the same-named PDFs · `tania-project (§N)` = the memoir's English translation · `EV-##` / `CF-##` = the two `data/` logs.

## Snapshot (2026-10-14 — refreshed at each wrap-up)

| | |
|---|---|
| **Phase** | 2 (master extraction) **complete** → Phase 3 (tree assembly) next; **place authority done** (gazetteer + map layer, 2026-10-14) |
| **People index** | 91 people — A01–A29 · B01–B26 · C01–C16 · X01–X21 (X10 unused) |
| **Places** | 42-entry gazetteer (`data/places.md`), 39 geocoded → `places.geojson`/`.kml` — new 2026-10-14 |
| **Evidence / conflicts** | EV-01…80 (Prensa Israelita queue **mined** 2026-10-14) · CF-01…31 (9 resolved/leaning/partial) |
| **Corpus** | 10 PDFs, 2,265 pp — incl. the **full Slutsk Pinkas** + memoir at tania-project.com + UFDC *Prensa Israelita* images |
| **Queued research** | Felipe Borenstein's own death notice (~1959/60 issue unidentified) · Phase 4: family outreach (Pola — key to CF-20/CF-30), JRI Kurow/Warsaw, NHAB archive pulls, USA records |
| **Family input** | Open stream (2026-10-13): Philip — more welcome; ask Pola |
| **Writing** | 4 family posts in `writing/` (EN+ES pairs each) — bylined Z.ai GLM-5.3 (DEC-009) |

## Conventions (quick reference)

- **Confidence**: `[C]` record-confirmed · `[L]` likely · `[?]` open question (DEC-003).
- **Citations** on every fact: source + page / URL / archive fond. Never merge same-named people without corroboration — this family recycles names across branches (two Taybas, two Gindas, two Dorises).
- Rebuild the text layer with:
  ```sh
  for f in base-documents/*.pdf; do pdftotext -layout "$f" "extracted-text/$(basename "${f%.pdf}").txt"; done
  ```

## Provenance

Project documentation and data extraction are AI-assisted (**GLM-5.3**, provider `account:zai-individual-coding-plan`, **ZCode** harness), verified via [acnehuatl](https://github.com/pborenstein/acnehuatl) — a cwd-keyed session-provenance tool, not self-reported. The genealogical substance is Wendy's research; the errors, where they remain, are the machines'.
