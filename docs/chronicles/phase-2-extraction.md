# Phase 2 — Master Extraction

## Entry 4 — Phase 2 complete: data/ built from all 9 sources (2026-10-10)

**What**: Full person-based extraction of the corpus into `data/`: **77 people** (A01–A18 Borenstein, B01–B26 Mostkoff, C01–C16 Polak/Borukovich, X01–X18 unplaced), **49 evidence records** (EV-01–49), **26 conflicts** (CF-01–28 with CF-18/19 unused; 6 resolved/leaning-resolved).

**Why**: Replace the scattered PDF notes with one cited, confidence-marked index (ROADMAP Phase 2; "no facts left behind in the PDFs").

**How**: Five source passes — Narrative (master; NB its pp. 38–71 duplicate pp. 1–37), Notes (JRI Kurow, obits, pinkas set, UFDC queue), Tanya material (Wendy's summary + MOSTKOFF.pdf + full tania-project memoir, §-cited), record collections (chronicle/Slutsk Links/SUPONITZKY/Genealogy draft), and the Borenstein timeline. Page-accurate citation via /tmp page-marked copies; memoir cloned to /tmp (not committed — copyright).

**Key findings**: Israel b. 1880 (memoir ×2) d. 1957 cert/1956 memoir; exact birth dates for his five children (§35 recap); Lyubka & Etl are Israel's sisters (B09/B24); **Nakhman Borukovich alive ≥1932** → pinkas-1918 death re-attributed (CF-13); Pesya's kidney-death memory was mis-filed to grandmother Chaya (CF-22); Rachmeil=Mendel=Manuel Glatt identity resolved Line A's Glatt cluster (A04/A08); Mikhail Borukhovich's 1925/26 suicide; Movsha Bobruysk family = likely Nakhman's brother (X16).

**Decisions**: DEC-004 (single markdown people index; family-connected inclusion rule) — docs/DECISIONS.md.

**Files**: data/{people,conflicts,evidence-log}.md · docs/FAMILY-OVERVIEW.md (rewritten as sourced synthesis) · docs/IMPLEMENTATION.md (Phase 2 ✅). Commits 15f1a5e…9b71601.

## Entry 5 — Narrative PDF trimmed: duplicated pages removed (2026-10-10)

**What**: `base-documents/Mostkoff Family Narrative.pdf` cut from 71 → 37 pages — the export's second, repaginated copy of the same text (pp. 38–71) deleted. `extracted-text/` regenerated; corpus now 87 pp / ~125 KB text.

**Why**: The duplicate misled extraction (pass 1 had to disambiguate page citations) and contradicted a tidy source corpus. Philip requested the trim, overriding DEC-002's blanket rule.

**How**: Programmatic parity proof first — every substantive text line of pp. 38–71 present in pp. 1–37 (only table line-wrap artifacts differed; fond-number fragments confirmed) and all 31 second-half images MD5-identical to first-half images. Lossless trim via pypdf (page-object copy, no re-encoding; Ghostscript deliberately avoided). Post-trim verification: 37 pages, 33 images, text layer character-identical to the original pp. 1–37.

**Decisions**: DEC-008 (one-case amendment of DEC-002; original 71-page file recoverable from git history ≤ 073001e).

**Files**: base-documents/Mostkoff Family Narrative.pdf · extracted-text/ · docs/{SOURCE-SURVEY,DECISIONS}.md · README.md · data/people.md (citation NB). Commit 246248d.
