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

## Entry 6 — README rebuilt as the repo's entry portal (2026-10-10)

**What**: README.md restructured from a conventional readme into a navigation index: intent-based "start here" table (person → people.md, disagreement → conflicts.md, record → evidence-log.md, …), full repository map with rules, citation-key quick reference, and a dated Snapshot section carrying the volatile facts (phase, counts, corpus, queued research) that used to rot in prose.

**Why**: README is the entry portal to the whole project; it had drifted stale ("Phase 2 is next", "data/ — not yet created") exactly because nothing owned its freshness.

**How**: Volatile state now lives in one clearly-marked Snapshot table; everything else is stable structure pointing at CONTEXT.md/IMPLEMENTATION.md for live state. Freshness enforced by a new CLAUDE.md session-end rule (step 4): refresh Snapshot + map at every wrap-up.

**Files**: README.md · CLAUDE.md.

## Entry 7 — Investigation: the Sapotnitsky name (2026-10-10)

**What**: `docs/investigations/sapotnitsky.md` — full corpus inventory of the name (13 appearances + negative evidence), six ranked origin hypotheses, and an 8-step research program feeding Phase 4.

**Why**: Wendy finds the name mysterious; it is the sole surname anchor for Chaya (B02), resting on one document (Israel's 1957 Mexican death cert, EV-13).

**Key findings**: (1) the memoir's Russian original says **Несвиж/Nesvizh** outright — "Neswalok" was a misreading, and the interwar border resolves the "near Poland" tension; (2) the 1889 Minsk "Khaia Zaturinskii" marriage **cannot be Chaya's** (bride 20 vs Chaya ~1855–60 b.; Israel b. 1880 predates it) — new CF-29, with a younger-namesake-cousin reading that keeps the Nesvizh Zelik/Zaturensky natal-family hypothesis (H1) alive; (3) the Priluki 1877 Min'kov/Supanitskij pairing (EV-48) is the closest phonetic match and echoes the Mostkov+Sapotnitsky pair; (4) the name is attested as a real Slutsk/Minsk-region surname (Narrative p. 8) — the simplest hypothesis needs no exotic origin.

**Files**: docs/investigations/sapotnitsky.md · data/{people,evidence-log,conflicts}.md (B02, EV-10, CF-29) · README · CONTEXT.

## Entry 8 — Mermaid family tree (2026-10-10)

**What**: `data/family-tree.md` — the tree as 5 GitHub-renderable Mermaid diagrams: (1) the three-line convergence to Philip/Edna; (2) Line A incl. the Glatt branch; (3) Line B elder generation; (4) Israel & Shifra's descendants; (5) Line C Polak/Borukovich.

**Why**: Visual navigation of the 77-person index; Mermaid chosen over SVG for native GitHub rendering + text versioning + regenerability.

**How**: Derived by hand from data/people.md with confidence encoding (dashed nodes/edges = open [?]; marriage hubs `(("m. year"))`). All 5 diagrams validated parse+render against Mermaid 10 (CDN test page in-browser; npm registry blocked). X-line candidates deliberately omitted (documented in the file).

**Files**: data/family-tree.md · README · CONTEXT.

## Entry 9 — Shifra Borenstein added (2026-10-13)

**What**: Third child of Joseph Borenstein (A18) & Ana Mostkoff Linares (B17) — **Shifra** — added wherever the children were listed: people.md (A18, B17, index), family-tree diagrams 1 & 4, FAMILY-OVERVIEW, CLAUDE.md facts. Living person: name only, no dates.

**Why**: Family correction — the first direct family-input fact since the corpus was assembled. Source: Philip (session, 2026-10-13) [C].

**Note**: A daughter Shifra in this generation may explain the memoir's "Shifra" among Luis's children (CF-23 annotated — the memoir's letter-source may have mixed generations).

**Files**: data/{people,family-tree,conflicts}.md · docs/FAMILY-OVERVIEW.md · CLAUDE.md.

## Entry 10 — Corrections on Luis's children & the Shifra names (2026-10-13)

**What**: Philip corrected three things: (1) Luis & Chelo's children are Lucy, Ana, Moises, Pola, **Isidoro** (spelling), Aida; (2) the Prensa Israelita reports their **Hebrew names** — hence the memoir's differing list — and **Luis never had a daughter named Shifra** (entry 9's explanation for the memoir's "Shifra" is withdrawn; the memoir's list is simply wrong there); (3) Shifra Borenstein (Joseph & Ana's third child) was **named after Ana's grandmother Shifra Boruchovich** (C06). CF-23 → partially resolved; Hebrew↔civil mapping pending EV-35 mining.

**Files**: data/{people,family-tree,conflicts}.md. Commit 02f1fc4.

## Entry 11 — The full Pinkas of Slutsk arrives & is incorporated (2026-10-13)

**What**: Philip added *Pinkas-of-Slutsk.pdf* (2,178 pp; full English translation of the Slutsk Chevra Kadisha register, 16,266 entries, 1736–1924; provenance TBD — Wendy's collection, likely via Ancestry). Machine-parsed with page mapping (16,266 entries; #1 = Apr 1924, numbers run backward); family extraction in **data/pinkas-hits.md**; EV-50–58.

**Findings**: (1) **CF-17 resolved-leaning negative** — grandmother Chaya is *not in the register* (58 Khaya/Chaya deaths 1914–24 enumerated; 3 Khaya-wives-of-Leib across 1736–1924, none ours; 0 Mostkov) → she died near **Nesvizh**, not Slutsk; #870 weakened further (her husband Zev Volf Itskovits d. 1914, age 90). (2) **CF-13 resolved at full scale** — ≥4 distinct Berkovits/Borukhovich families in Slutsk; #1120's Avraham clusters with the Chaim-Zimil tailor clan (row 28). (3) **CF-10 restructured** — Tsiptsin is a cohesive Hacohen clan (10 entries, incl. the Chevra Kadisha's own beadle), Sapotnitsky has zero Slutsk burials; Bunin cousin-couple fixed: Y' Leib Boonin → Mendil (d. 11 Jan 1915; EV-52) m. Sheina Dvora Tsiptsin → sons Natan (d. 1909) & Yitskhak (killed 1922). (4) **4th child of Y' Mikhal Polak found** — Y' Leib Polak (d. by 1895, row 5; EV-51), making C16 Yosef his grandson. (5) Zaturensky family real in Slutsk (4 entries, no Zelik — EV-56); only Kharakh = Razoveh family (EV-57); Mrs. Zlateh (Pesheh's row-mate) = Zlateh Novik Krienes, no relation.

**Files**: base-documents/Pinkas-of-Slutsk.pdf · extracted-text/ · data/{pinkas-hits,people,conflicts,evidence-log}.md · docs/{SOURCE-SURVEY,investigations/sapotnitsky}.md · README · CONTEXT.
