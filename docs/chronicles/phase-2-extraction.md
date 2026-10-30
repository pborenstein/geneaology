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

## Entry 12 — Family-facing writing series opened (2026-10-13)

**What**: `writing/` — two blog-style posts for family members at the leaves: (1) *The Book That Remembers Everyone* — what the Pinkas is, why it matters, the three mysteries it moved (Chaya not in Slutsk; the 1918 Berkovits re-attribution; the Bunin cousins given dates); (2) *How Do You Rebuild a Family…* — project intro: method ([C]/[L]/[?], sources, conflicts kept visible), 10,000-ft history (three lines → Mexico City convergence), and an invitation to cousins. Jargon-free; no CF/EV keys; privacy footer (family-only).

**Care taken**: two invented dates removed before commit (Joseph–Ana wedding year, Shifra Borenstein's implied birth) — the archive doesn't hold them; posts only claim what's sourced.

**Files**: writing/{01,02}*.md · README · CONTEXT.

## Entry 13 — Attribution & ordering corrected in writing/ (2026-10-13)

**What**: Posts reordered (01 = orientation, 02 = the Pinkas) and reattributed: bylines now "Written by Z.ai GLM-5.3, the project's AI research agent"; the first-person "I'm Philip" framing removed (AI narrates as itself, third person for family). Project credit unchanged: Wendy Cadieux (research) & Philip Borenstein (tech).

**Why**: Philip: "If my name is on it, I wrote it." AI-drafted prose must carry the AI's name; LLM use may be openly celebrated. Recorded as **DEC-009**.

**Files**: writing/{01,02}*.md · README · CONTEXT · DECISIONS.md.

## Entry 14 — Writing series goes bilingual (2026-10-13)

**What**: Mexican-Spanish versions of both posts: `01-como-se-reconstruye-una-familia.es.md` · `02-el-libro-que-recuerda-a-todos.es.md`, cross-linked with the English originals (`.es.md` suffix pairs files). Bylines per DEC-009 (Z.ai GLM-5.3). Rationale: half the family's leaves — Pola's, Isidoro's, Lucy's, Aida's, Moisés' branches — live in Spanish; prose reports will run bilingually going forward.

**How**: Written as native Mexican Spanish (idioms: "a sus órdenes", "pan de cada día", "a vuelo de pájaro"), not calques; family names and all facts identical to the sourced English versions; one stray-CJK corruption caught and fixed before commit.

**Files**: writing/ (4 files) · README.

## Entry 15 — Sapotnitsky post (03, EN+ES) + EV-35 Prensa Israelita fully mined (2026-10-14)

**What**: (1) Third family-facing post, the promised Sapotnitsky-name story — "Three Names for One Grandmother" EN + ES-MX pair, cross-linked from post 02 in both languages. (2) The ~30 queued UFDC Prensa Israelita links (EV-35) mined end-to-end: 22 notices → **EV-59–80** + `data/prensa-hits.md`.

**How**: UFDC's viewer is a JS app, but the static layer is citable — `ufdcimages.uflib.ufl.edu/AA/00/06/55/27/{vol}/{img}.jpg` + same-path `.txt` OCR (Notes' `NN/NNx` citations don't map to image numbers; notices relocated by searching full-issue OCR; 2 pivotal obits verified against page images).

**Headline findings**: **CF-16 record-confirmed** (Menahem Mendl Glatt d. 1965 at 68 = Mendel Borensztejn b. 1897 Kurow — five notices converge); **A06 corrected** ("Tía Mania" = Felipe's *widow*, d. 15 Jun 1969, not his sister → new CF-30 vs. Chana Mindel Bauman); Shifra's own obit found ("Sofía Mostkoff," 24 Sep 1962, 85 — CF-21/31); CF-23 resolved (Pesele=Pola, Hinde=Aida, Anita=Ana, Sara=Chelo); CF-15 leaning resolved (Lucy m. Harry Pepper, Memphis); Toibe's obit (d. 1973 at 79 = Kurow 1894 ✓) with Sheindl alive 1973 in Israel; new people A19–A29, X19–X21; Moscow Baskins greet Ana's 1959 wedding; Alberto Jarovinsky & son Salomón died together 2 Jan 1970; stray "Leib Minkov" in the community (Sapotnitsky lead).

**Files**: data/prensa-hits.md (new) · data/evidence-log.md · data/people.md · data/conflicts.md · writing/03-* (new, EN+ES) · writing/01-02 (links) · docs/investigations/sapotnitsky.md · CONTEXT.

## Entry 16 — Place gazetteer + map layer (2026-10-14, the "mapping" session)

**What**: Same day as the Prensa round (entry 15, the parallel session), this session built the **place layer**: `docs/MAPPING-PLAN.md` (the plan), `data/places.md` (gazetteer — 42 Tier-1 places + ~30 Tier-2 background toponyms), and the generated `data/places.geojson` (39 points; primary interchange for uMap/QGIS/geojson.io) + `data/places.kml` (Google Earth) via `scripts/places-to-geojson.py`. The README gained a **What's New** section covering both 2026-10-14 rounds.

**Why**: A labeled map of the family's Eastern Europe and migration arc — and Phase 3 groundwork: a place authority for the GEDCOM/Gramps load. Recorded as **DEC-010**.

**How**: Extraction pass over people.md / evidence-log / pinkas-hits / memoir; every coordinate carries provenance (Wikidata QID + GeoNames ID, cross-checked against the memoir site's own locations table — a dozen independent corroborations). Disambiguation wins: **Ostrov = the shtetl near Slutsk** (the memoir's own words, not Ostrów Mazowiecka); **Kurow = Kurów, Lublin** (archive fond); Dvoretz → Dziatlava-district Dvarets `[L]`. Flagged: a Wikidata-vs-memoir-site discrepancy on Urechye (district + coordinates); Oreitsa/Laseh/Ozdeh deliberately un-geocoded `[?]`. QA note: a from-memory "Saratov" QID turned out to be the South Pole — every QID was verified against returned labels before use.

**Files**: docs/MAPPING-PLAN.md (new) · data/places.md (new) · data/places.geojson · data/places.kml · scripts/places-to-geojson.py (new) · README · DECISIONS.md (DEC-010) · IMPLEMENTATION.md · CONTEXT.

## Entry 17 — Post 04: the Prensa-mining story, EN+ES (2026-10-18)

**What**: Fourth family-facing post — *The Paper That Knew Everyone* / *El periódico que conocía a todos* — telling the EV-35 Prensa Israelita round to the family: the Hebrew-names key (CF-23), the 1959 wedding portrait (incl. the Moscow Baskins' printed greetings), the Mania correction (A06/CF-30), Mendel = Manuel Glatt (CF-16) with the Thursday-gabaim bar mitzvah, Shifra's "Sofía Mostkoff" obit (CF-21/31 dates dance), Toibe's chosen plot (EV-73), and the Leib Minkov sighting (EV-79) as the forward hook from post 03's Sapotnitsky story. Family asks: Felipe's missing death notice, Mania's other name (Bauman?), the Glatt surname residue, "Ydele," family clippings — plus a direct invitation to Pola.

**Why**: Philip picked post 04 from the CONTEXT "next session" candidates; the Prensa round (entry 15) was the series' untold story, and posts 01–03 already promised the newspaper dossier.

**How**: All facts from `data/prensa-hits.md` + `conflicts.md` + `people.md`; four pre-ship inaccuracies caught in fact-check (Linares guests include grandfather Leobardo, not only uncles; Rebeca's balance notice = six weeks post-obit; Chanowskys = named kin, not brothers; bris→obit interval phrasing). Post 03 EN+ES gained forward links in the "wild card" paragraph; README posts table, What's New (2026-10-18), Snapshot count → 4. Housekeeping: stray byte-identical `data/places 2.kml` (Finder duplicate from the mapping session) deleted.

**Files**: writing/04-* (new, EN+ES) · writing/03-* (links) · README · CONTEXT. Commit b7354ce.

## Entry 18 — Family-input round: CF-30 resolved, A15 merged, Jarovinskys re-anchored (2026-10-18/19)

**What**: Philip's first sustained family-input stream, taken straight into `data/` (all `[C — Philip, 2026-10-19]` unless marked): (1) **"Chelo" is an apodo** — B15's name is Consuelo; the Prensa used Sara / Chelo / Consuelo / Sarita across four notices. (2) **Ana's names** Mostkoff Linares → Borenstein Mostkoff → Borenstein → **Caddess** (m. 2) Hugh N. Caddess, 2 Jan 1982); Ana & José **divorced 1978**. (3) **José's names** Borenstein Bauman / Borenstein / Joseph (Joe); m. 2) Carol Ackerman ~1986 `[L]`; **d. March 2026**. (4) **CF-30 resolved**: Mania / Mañe / Manye = Chana Mindel Bauman = civil María Borenstein — José's legal apellido "Bauman" supplied the surname anchor, Philip's testimony the identity; **A15 merged into A06** (DEC-012). (5) **A27 corrected**: Sara Jarovinsky was **Mania's sister, a Bauman** — not a Borenstein sister of Felipe (the 2026-10-14 structural reading withdrawn; every notice fits the Bauman reading at least as well); the timeline's "Sura Ita" = *Sarita*; Alberto Jarovinsky (A29) is Mania's nephew by blood. Also: pictographs stripped from the README + CLAUDE.md hard rule (DEC-011); What's New entries now link their posts and files.

**Why**: Post 04 asked the family for exactly these things (Mania's other name, the Baumans); Philip answered within a day. Three of the Prensa round's inferences were wrong or incomplete — the record had kept them `[L]`, which is what made them cheap to correct.

**How**: Every change cited to Philip + date; withdrawn readings left visible ("corrected 2026-10-19") in people.md, prensa-hits, evidence-log EV-59/61/62/76, CF-23/CF-30. Tree: the stale "Tía Mania — likely sibling" node (wrong since entry 15) removed; Chana Mindel's A15 node → A06 as Felipe's wife; José d.2026 in all three diagrams; convergence hub "m. 1959 · div. 1978" with both second marriages drawn names-only. Post 04 EN/ES corrected in place (Chelo/Consuelo; Alberto's parentage; the "no natal kin" argument) + a dated **Postscript (19 Oct)** telling the family what they settled.

**Decisions**: DEC-011 (no pictograph emoji), DEC-012 (merged IDs become redirects).

**Open**: Sara Jarovinsky's death year — not visible among Mania's 1969 obit mourners (d. 1964–69, or an OCR miss) `[?]`; Carol Ackerman marriage year `[L]`; Felipe's own death notice (unchanged). Tree still lags the index elsewhere (A07 "alive 1966" → 1973 Israel; A27–A29 not drawn) — a full tree-vs-index refresh is due.

**Files**: data/{people,conflicts,evidence-log,prensa-hits,family-tree}.md · writing/04-* (EN+ES) · README · CLAUDE.md · DECISIONS.md · CONTEXT. Commits 83e6159…f634a04.

## Entry 19 — Ana's papelitos: Felipe's date, Bauman grandparents, CF-02/21 closed; tree regenerated (2026-10-27)

**What**: Second family-input round, from **Ana Caddess** (email via Philip; cited `[C — Ana Caddess (email via Philip), 2026-10-27]`): (1) **Felipe d. Sunday 23 Aug 1959** (A05) — alive at the 15 Mar 1959 wedding ✓, unveiling 14 Aug 1960 at ~11.7 months ✓; his printed-notice hunt narrows to the late-Aug/early-Sep 1959 Prensa issues. (2) **Mania's parents: Zvi & Shoshanah Bauman, Chlodna 38, Warsaw** (Ana's information via Avram Bromberg, 2004) — new people **A30/A31**, indexed in Line A by attachment like the Jarovinskys; the Notes' old "Herz Bauman" Warsaw-cemetery lead is plausibly Zvi himself (Herz = Yiddish form of Tzvi) `[L]`; the 1934/35 "Chana's jewels" trip gains a likely destination `[?]`. (3) **CF-02 resolved**: Israel d. **1 Oct 1957** — Ana recalls "September 1957" (gravestone worn); 1957 now double-attested vs the memoir's 1956. (4) **CF-21 resolved**: Shifra d. **Monday 24 Sep 1962** — Ana's own memory ("after we came back from Israel in August"; she visited her in the hospital; the family asked José "Pepe" to go) anchors it; the memoir's August retires. (5) New lead: her mother **Consuelo survived Luis by ten years** — neither death date otherwise known (B12/B15 `[?]`). Same session: **GEDCOM tooling deferred until further notice** (Philip). Counts: **92 people; 12 of 31 CFs resolved/leaning**.

**Why**: Post 04's asks keep producing. Ana's own hedge ("all of this may or may not be accurate, but these papelitos will soon disappear") made every checkable date worth corroborating — and all of them checked (weekday arithmetic, wedding, unveiling interval, obit dates).

**How**: Family-input convention extended to name the relaying family member (people.md conventions header). Then the **tree regenerated against the index** — its whole flagged lag list cleared: A05 d.1959; A07 → "alive May 1973 · Israel"; B02 "d.Slutsk ?" → "d.? near Nesvizh?" (per CF-17); **A30/A31 + the entire Jarovinsky branch (A27–A29 + daughter Sara) drawn** in diagrams 1–2; Glatt children A19–A24 + Freddie (A26) + Emma added; Mitelhaus set completed (José d.1969); Lucy m. Harry Pepper; Pola m. Bierzwinski 1965; Alberto Mostkoff "d. at 13" → ~1945–1959 (14); CF-23 footnote → resolved. All five mermaid blocks compile via mermaid-cli (tooling note: headless-shell cache missing — point puppeteer at local Chrome with `-p` config or `PUPPETEER_CACHE_DIR=~/Library/Caches/puppeteer`); visual spot-checks of diagrams 1–2 (NB: the vision pass hallucinated label details on the dense diagram — compile + grep of the source is the trustworthy gate, not its readings). **Posts**: 04 EN/ES — Felipe's ask updated in place (date known; notice still missing), Shifra's "working reading" marked sealed by family memory, second dated **postscript (27 Oct)** (Bauman grandparents, the Herz=Zvi hook, two new asks: Luis/Consuelo's dates; who was Avram Bromberg); 01 EN/ES method example updated (1956-vs-1957 now family-settled). Places: P19 Warsaw carries Chlodna 38 (geojson/kml regenerated, no coordinate change).

**Open**: Luis & Consuelo death dates; Avram Bromberg's identity/relation; Felipe's printed notice (window now tight); Sara Jarovinsky's death year; CF-20 (Pola); CF-31 (Shifra's 1877-vs-1880); JOWBR re-check for Israel's engraved date (J_MEXICO_0002150).

**Files**: data/{people,conflicts,places,places.geojson,places.kml,family-tree}.md · writing/01-* (EN+ES) · writing/04-* (EN+ES) · README · IMPLEMENTATION.md · CONTEXT. Commits 703c218…12375f2.

## Entry 20 — Bobe's passport: Shifra's 1928 Soviet exit document + the ketuba copy (2026-10-29)

**What**: Philip dropped `base-documents/bobespassport/` — 11 JPEG scans from **Ana Caddess's 2020-02-04 email to Wendy** ("Bobe's passport"; cited `[C — Ana (email to Wendy, 2020-02-04)]`), the corpus's **first image-only source**. Machine-reading gave: (1) **EV-81 — Shifra's (C06) BSSR foreign passport**: bearer **Мосткава Шыфра Нахманаўна** ("Mostkoff Chifra" on the French page); b. **1878, Bobruisk district**; issued **Minsk, 27 Nov 1928**; designated exit **Sebezh**; manifest = Shifra with **Leiba 14, Michel 11, Dvoyra 7** — the three youngest (B12/B13/B14), whose memoir birth years are thereby record-corroborated; her photo (~50, headscarf) and the children's photos pasted in. This is the Soviet-exit half of the Jan 1929 Mexico arrival (EV-03). (2) **EV-82 — the Luis × Chelo ketuba copy** (Confederación de Centros Israelitas de México): Ana's gloss attests **Chelo's orthodox conversion** — a new [C] fact, unrecorded elsewhere in the corpus; explains her Prensa name Sara/Sarita. (3) **CF-31** now three-way (memoir 1880 / passport 1878 / obit ~1877); **CF-11** annotated (passport says *district* — a Bobruisk-uyezd village birth + Slutsk residence would satisfy all sources); **CF-06** reframed on the ketuba's unread Kislev year (5699 → religious marriage before Lucy's b. 10 Mar 1939; 5700 → after, matching the license). C03 "father of Shifra" [L]→[C] (patronymic corroborates EV-04).

**Why**: The passport photos were already inside the Narrative (pp. 10, 15–20; Wendy had read "b. ~1878, Bobruisk" at p. 10) but too small to cite — the scans turn impressions into records. Identity locked three ways: children's names + ages (14/11/7 at Nov 1928 = Luis/Mikhail/Dvoira exactly), the French-page name, and the Nakhimanovna patronymic.

**How**: Vision-model transcription with every uncertain read flagged `[?]` and collected in **SOURCE-SURVEY §11** (per-image inventory) per DEC-013; a first pass misread the bearer as "Маслюкова Мара" — a focused re-read corrected it to Мосткава Шыфра (the flag system working as designed). Places: +**P43 Sebezh** (Wikidata Q193641, OSM cross-check; the exit word itself is a `[?]` read), P08 Minsk annotated; geojson/kml regenerated (40 geocoded). Tree: Shifra "b.1878/80" in both C06 diagrams — no structural change. Not yet read: the passport number, the Spanish entry stamps, the ketuba's date.

**Decisions**: DEC-013 (image-only sources get a folder citation key + SOURCE-SURVEY inventory; machine reads keep `[?]` until eyes verify; email citations name the actual correspondent pair).

**Open**: The §11 eyes-on list — **IMG_1924 unread** (the vision service rejects the file); the ketuba's Kislev **year** (the CF-06 key); Bobruisk-vs-Mozyr (IMG_1923/1925); Apr/Sep-1928 vs 27-Nov-1928 (IMG_1925); the Spanish stamps; the "young woman ~16–20" photo (IMG_1933) that matches no one on the manifest. Standing queue unchanged (Felipe's notice in the late-Aug/early-Sep 1959 issues; Pola/CF-20; Luis & Consuelo dates; Avram Bromberg; Sara Jarovinsky; Sapotnitsky §8–9). The batch has obvious post material — the first source whose strongest content is images — unwritten.

**Files**: base-documents/bobespassport/ (new) · data/{people,conflicts,evidence-log,places,places.geojson,places.kml,family-tree}.md · docs/SOURCE-SURVEY.md · README · IMPLEMENTATION.md · CONTEXT. Commit 50bc4fa.
