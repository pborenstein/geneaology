# Decisions

### DEC-001: Adopt project-tracking structure in docs/ (2026-10-05)
**Status**: Active
**Context**: Not a code repo; genealogy research project with PDF sources and growing notes.
**Decision**: Use the project-tracking system — CONTEXT.md (session hot state), IMPLEMENTATION.md (phases), DECISIONS.md (this file), chronicles/ (session history). Project notes live in `docs/`; derived text extractions live in `extracted-text/`; structured data will live in `data/`.
**Alternatives**: Notes scattered in more PDFs (status quo — how the current material arrived); a wiki.
**Consequences**: Session pickup = read docs/CONTEXT.md only. PDFs stay untouched as archival sources.

### DEC-002: PDFs are archival; extraction happens into new files (2026-10-05)
**Status**: Active
**Context**: The 9 PDFs mix record extracts, memoir text, links, and narrative; some content overlaps between files.
**Decision**: Never edit the PDFs. All consolidation happens in `extracted-text/*.txt` (search layer, generated 2026-10-05) and Phase 2's person index. The Narrative (71 pp) is the master narrative document; other PDFs are satellites around it.
**Consequences**: Regenerating `extracted-text/` with pdftotext is always safe; the person index becomes the single working tree of record.

### DEC-003: Confidence markers on every fact (2026-10-05)
**Status**: Active
**Context**: Sources disagree frequently (dates, places, even parents); Wendy already distinguishes "confirmed" vs. "possible" in her timeline.
**Decision**: Standard marks everywhere: **[C]** confirmed by a record, **[L]** likely (record-adjacent or strong inference), **[?]** open question. Every fact carries a source citation (PDF+page, URL, or archive fond). Persons carry alias lists.
**Alternatives**: Plain prose without marks (loses the discipline); numeric certainty scores (overkill).
**Consequences**: FAMILY-OVERVIEW and later the person index can be trusted at a glance; publication can inherit the marks.

### DEC-004: Phase 2 data format — decided (2026-10-10)
**Status**: Decided (Philip, Phase 2 kickoff)
**Context**: Need one home for person/fact data that supports aliases, citations, confidence, and eventual GEDCOM export.
**Options**: Markdown index (human-readable, greppable, no tooling) vs. CSV per entity (structured, import-friendly) vs. jump straight to GEDCOM (interoperable but clumsy for narrative notes and citations as free text).
**Decision**: Single markdown index `data/people.md` — one entry per person with stable IDs (A/B/C/X), aliases, facts, inline citations, confidence marks; GEDCOM deferred to Phase 3. Inclusion rule: full entries for family-connected people (blood/marriage relatives and record-witnessed kin); background mentions stay in source notes.

### DEC-005: Repo layout — base-documents/ for archival PDFs, GitHub remote (2026-10-05)
**Status**: Active
**Context**: Philip initialized a git repo and pushed to `github.com:pborenstein/geneaology`; the 9 source PDFs moved from the project root into `base-documents/`.
**Decision**: Canonical layout: `base-documents/` = archival source PDFs (never modified, committed as-is), `extracted-text/` = regenerable text layer (safe to delete/rebuild), `docs/` = tracking + planning notes, `data/` = future Phase 2 structured output.
**Alternatives**: PDFs at root (clutters repo and mixes archival with derived); gitignoring large PDFs (loses history of the actual sources; repo is private).
**Consequences**: Citations reference `base-documents/<file>.pdf` + page; `extracted-text/` can always be regenerated with `pdftotext -layout` if it drifts from the PDFs.

### DEC-006: docs/RESOURCES.md is the registry for standalone external resources (2026-10-05)
**Status**: Active
**Context**: External material arrives in two kinds — link collections inside Wendy's notes PDFs, and standalone projects/sites (first arrival: The Tania Project, the full text of Tania Mostkoff's memoir).
**Decision**: Standalone resources get a docs/RESOURCES.md entry (what it is, URLs, why it matters, how the project uses it). Link collections living inside the source PDFs stay put and are covered by SOURCE-SURVEY.md.
**Alternatives**: Folding everything into SOURCE-SURVEY.md (whole projects would be buried among note links); copying Wendy's link lists into RESOURCES.md (duplication and drift).
**Consequences**: One place to check before hunting for external material; linked from README's docs guide.

### DEC-007: Record AI-assistance provenance in the README (2026-10-05)
**Status**: Active
**Context**: Much of this project's doc/data output is AI-generated, and models/harnesses may change over the project's life. acnehuatl (`~/projects/nahuatl-PROJECTS/acnehuatl`) reads the session database and reports the true harness/provider/model per cwd — models cannot reliably self-attribute.
**Decision**: README carries a Provenance section naming harness/provider/model for AI-generated bulk work (session id and cwd excluded). Update it whenever a different model/harness produces a major deliverable (e.g. the Phase 2 extraction). Verify with acnehuatl, never by asking the model.
**Consequences**: Readers can tell which AI produced which pass of the work; no session-level identifiers are published.

### DEC-008: Content-preserving trim of the Narrative PDF's duplicated pages (2026-10-10)
**Status**: Active (amends DEC-002 for this one case, on Philip's explicit instruction)
**Context**: *Mostkoff Family Narrative.pdf* (71 pp) embedded two copies of the same text — a second, repaginated copy as pp. 38–71. The duplication misled extraction passes and bloats the corpus. DEC-002 forbids modifying `base-documents/`.
**Decision**: With Philip's explicit approval, keep pages 1–37 (the complete first copy) and delete pp. 38–71 — only after programmatic verification: (a) every substantive text line of pp. 38–71 exists in pp. 1–37 (the only diffs were table line-wrap artifacts, key fragments confirmed present); (b) all 31 embedded images on pp. 38–71 are MD5-identical to images on pp. 1–37; (c) post-trim text layer and all 33 first-half images verified identical via pypdf (lossless page-object copy, no re-encoding; gs deliberately avoided). The 71-page original remains recoverable from git history (≤ commit 073001e).
**Alternatives**: Keep the duplicate (confusing for future passes and citations); trim with Ghostscript (re-encodes content — not acceptable for archival); store a separate "trimmed" file (two sources of truth for one citation key).
**Consequences**: `Narrative, p. N` citations unchanged (they always used first-copy pages; pages 1–37 keep their numbering). `extracted-text/` regenerated. Corpus is 87 pp / ~125 KB text. DEC-002's blanket rule stands for everything else; any future `base-documents/` change needs its own recorded decision.

### DEC-009: Writing attribution — AI-drafted prose carries the AI's byline (2026-10-13)
**Status**: Active
**Context**: Philip writes for a living: "If my name is on it, I wrote it. If I didn't write it, someone else's name goes on it." The `writing/` posts are AI-drafted (Z.ai GLM-5.3) from Wendy Cadieux's research and family records; an earlier draft was mistakenly voiced/signed as Philip.
**Decision**: All AI-drafted prose is bylined **"Written by Z.ai GLM-5.3, the project's AI research agent"** (with research credit to Wendy Cadieux), never a family member's name. First-person "I" in prose = the AI speaking as itself. LLM use for data-processing and inference may be acknowledged and celebrated openly. Family members' names go only on words they actually wrote (e.g., family-input facts quoted as `[C — Philip, date]`). Project *credit* is separate: Wendy Cadieux (research) & Philip Borenstein (tech).
**Alternatives**: ghost-write in Philip's voice (rejected — misattribution); unattributed (rejected — same problem, silent).
**Consequences**: `writing/` bylines and the Provenance section stay consistent; any future human-authored text (e.g., Wendy's narrative excerpts, Tania's memoir) is credited to its human author. Applies repo-wide.

### DEC-010: Place gazetteer is the source of truth; map layers are generated (2026-10-14)
**Status**: Active
**Context**: The family's places needed to go on a labeled map of Eastern Europe in a standard format (uMap/OpenStreetMap, Google Earth, QGIS). Genealogical place data needs the same discipline as people.md — name variants as-sourced, historical jurisdictions, confidence marks, citations — and Phase 3 (GEDCOM/Gramps) needs a place authority first, or imports sprout duplicate places for every name variant.
**Decision**: `data/places.md` is the gazetteer and the only hand-edited file (IDs `P##`; Tier 1 = family-connected, Tier 2 = background/lead toponyms; `[C]/[L]/[?]` + people.md citation keys; people-and-events links per place). `scripts/places-to-geojson.py` (stdlib-only) generates `data/places.geojson` (primary interchange) + `data/places.kml` — regenerate after every edit, never hand-edit. **Coordinate provenance rule**: no coordinate without a source (Wikidata QID / GeoNames ID, or the tania-project locations table); unidentifiable places ship un-geocoded rather than guessed (Oreitsa, Laseh, Ozdeh). Load-bearing disambiguations recorded in docs/MAPPING-PLAN.md: **Ostrov = the shtetl near Slutsk** (not any Polish Ostrów — the memoir says so); **Kurow = Kurów, Lublin** (JRI Fond 1751 sits in the Lublin Archive); Dvoretz = likely the Dziatlava-district Dvarets `[L]`.
**Alternatives**: hand-maintained GeoJSON (two sources of truth); geocode-by-guess (breaks citation discipline); defer to Gramps' own place database (not portable, no authority for other consumers).
**Consequences**: v1 = 42 Tier-1 places, 39 geocoded. Adding a place = edit `places.md` + rerun the script. Deferred and teed up in MAPPING-PLAN.md: migration-route layer, Leaflet family map, GEDCOM place strings at Phase 3.

### DEC-011: No pictograph emoji anywhere in the repo (2026-10-18)
**Status**: Active
**Context**: The README "What's New" section had accumulated decorative pictographs (newspaper / map / book symbols) as entry markers, and a new entry copied the pattern while omitting the links the entry should have carried. Philip: never use the "cutesy" pictographs.
**Decision**: No pictograph emoji anywhere — README, docs, `writing/`, `data/`, commit messages. Check marks (✅ / ✓) used as status markers in IMPLEMENTATION.md, ROADMAP.md and `data/` are fine. Recorded as a CLAUDE.md hard rule. What's New entries link what they name (posts, data files).
**Alternatives**: ban all non-ASCII symbols including check marks (rejected — Philip explicitly kept them); a whitelist of pictographs (rejected — none wanted).
**Consequences**: README What's New rewritten without pictographs and with links to every referenced post and file; the CLAUDE.md rule prevents recurrence across sessions.

### DEC-012: Merging duplicate persons — the dropped ID becomes a redirect (2026-10-19)
**Status**: Active
**Context**: Family testimony (Philip) established that A06 ("Mania," the Prensa's name for Felipe's widow) and A15 ("Chana Mindel Bauman," the timeline's name for Felipe's wife) were one woman (CF-30). people.md IDs are stable (DEC-004) and are cited across the evidence log, conflicts, prensa-hits, the Mermaid tree and the posts; deleting an ID would break citations silently.
**Decision**: When two entries prove to be one person, the entry with the richer record trail (here A06) becomes canonical and absorbs all facts and aliases; the other ID is **retained as a redirect** ("→ merged into A06") in both the index table and the detail section, and is never reused for another person. Citations are updated where touched; a dangling reference still resolves via the redirect. The people count reports distinct persons (redirects excluded), noted alongside the existing "X10 unused" convention.
**Alternatives**: delete and renumber (breaks stable IDs); keep both entries cross-marked "same person" (two sources of truth that drift — this was the interim state earlier the same day, before testimony).
**Consequences**: People count 91 → 90 distinct (A15 is a redirect). Precedent for future merges (e.g., X-line candidates resolving into B-line siblings).
