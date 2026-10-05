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

### DEC-004: Phase 2 data format — pending (opened 2026-10-05)
**Status**: Open — decide at Phase 2 start
**Context**: Need one home for person/fact data that supports aliases, citations, confidence, and eventual GEDCOM export.
**Options**: Markdown index (human-readable, greppable, no tooling) vs. CSV per entity (structured, import-friendly) vs. jump straight to GEDCOM (interoperable but clumsy for narrative notes and citations as free text).
**Leaning**: Markdown people index first (extraction-friendly), convert to GEDCOM at Phase 3.

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
