# Source Survey — Borenstein/Mostkoff Genealogy

*Surveyed 2026-10-05. PDFs live in `base-documents/`; text layer of each extracted to `extracted-text/` (one `.txt` per PDF, via `pdftotext -layout`). PDFs remain the source of truth; the text files are for searchability.*

## Corpus at a glance

| PDF | Pages | Type | Role |
|---|---|---|---|
| Mostkoff Family Narrative | 37 | Wendy's master narrative + photos | **Master document** |
| Borenstein Mostkoff Notes | 19 | Research notes, links, records, obits | Research workhorse |
| Summarized Belarus memories of Tanya Mostkoff | 8 | Wendy's annotated summary of Tania's memoir | Bridge source |
| Borenstein-Mostkoff Family Genealogy | 8 | Earlier draft of the master narrative | Earlier draft — mostly superseded |
| chronicle | 5 | Raw research notes, Pinkas translations | Raw notes |
| Slutsk Links | 4 | Links + Slutsk Yizkor book excerpts | Raw notes |
| MOSTKOFF | 2 | Memoir excerpt + LitvakSIG record | Raw notes |
| SUPONITZKY | 2 | Link + 1877 Priluki marriage record | Lead file |
| Borenstein family timeline | 2 | Borenstein-line chronology | Working timeline |
| Pinkas-of-Slutsk | 2,178 | **Full Slutsk Chevra Kadisha burial register, English translation** (16,266 entries, 1736–1924; provenance TBD — Wendy's collection) | Reference database — search, don't read; extraction in `data/pinkas-hits.md` |
| bobespassport/ (folder) | 11 images | **"Bobe's passport"** — Shifra's 1928 BSSR foreign passport + the Luis × Chelo ketuba copy (email: Ana Caddess → Wendy Cadieux, 2020-02-04) | **First image-only source** — no text layer; inventory & read-status in §11 (EV-81/EV-82) |

Total: 2,265 pages (10 PDFs), ~5.9 MB of text. Everything has a usable text layer (the ~38 MB narrative is text + many embedded photographs — mostly one shared set of photo objects). Plus, from 2026-10-29: the 11 JPEG scans of `bobespassport/` (§11) — the corpus's only non-PDF source.

## File-by-file

### 1. Mostkoff Family Narrative.pdf — the master document
*(37 pp; originally 71 — the export embedded a second, repaginated copy of the same text as pp. 38–71, removed 2026-10-10 after line-level text and image-hash parity checks — DEC-008; original in git history.)*
Wendy's full write-up of the Mostkoff line (started 2020, COVID project, researching "Philip's family"). Contains: the naming-conventions essay; Mostkoff surname-origin discussion (incl. Yad Vashem searches); **The Mostkoff Family** section — Leibe "Leon" Mostkoff & Chaya Sapotnitsky and their six known children (incl. Keili m. Reuben Iscovitch); the Mississippi interlude (~1895–1905, Rosedale fur trade); Israel Mostkoff & Shifra Boruchovich and their five children with Mexican spouses; extensive excerpts from Tania's memoir; Slutsk context and photographs (1925 family photo, Russian stove, Slutsk synagogue). This is where the other documents' threads converge.

### 2. Borenstein Mostkoff Notes.pdf — research workhorse
The active research file: name-variant list (Chifra/Shifra/Sofia; Anna/Ana/Hannah/Chana Mindel/Jane; Luis/Leibe; Felipe/Philip/Fishel); obituaries clipped (Doris Padawer 2006 St. Louis, Harold "Skeeter" Mostkoff 2006, Ignacio Mostkoff Nudelman 2013 Mexico City, Rebeca Rubinstein de Bornstein 2014, Myrna Bilak 2001, Pierre Secher 2008); the Rosedale MS blog post about Isadore Mostkoff, fur trader; ~30 links into the UFDC **Prensa Israelita** archive (Mexican Jewish newspaper) — weddings, obits, bris announcements, incl. **"Ana/Joseph marriage announcement"**, **"Philip's Bris Announcement"**, "Rebecca Finkler (wife to Sidney Borenstein)"; record extractions (Kurow JRI-Poland marriages/births; Lida Mostkov births 1907–13; Minsk marriage candidates incl. the 1889 Minkovich/Zaturniskii record Wendy believes is Leibe & Chaya; Borukhovich Bobruysk births 1884–88; Polak Minsk births 1847/1852; 1894 Minsk town dwellers); correspondence fragments (Memphis Iskiwitz family; "Leon from Lithuania" theory; the marriage-record hypothesis to be pulled from Minsk archives); Kurow archive fond info; Boruchovich genealogy site link.

### 3. Summarized Belarus memories of Tanya Mostkoff.pdf — bridge source
Wendy's section-by-section summary of Tania Mostkoff's memoir **with correlations to archival records**: identifies Tanya = Tatyana (Taiba) Izrailevna Mostkova, b. ~1911/12 Slutsk, stayed in the USSR; maps names (Mikhail = Miguel, Lev = Luis); quotes the Pinkas burial records that match the people in the memoir; Bobruysk Borukhovich birth records (Movsha family — possible brother of Nakhman); notes the "Chaya-Henya Itskovits d. 1919" candidate for grandmother Khaya (with the surname problem it creates); the Isaac Bunin 1922 bandit-massacre story tied to Pinkas entry 229.

### 4. Borenstein-Mostkoff Family Genealogy.pdf — earlier draft
An earlier, condensed version of the master narrative (same intro essay, "as of April 2020, barely begun"). Valuable for the clean **Polak/Borukovich tree from the Slutsk Chevra Kadisha Pinkas**: Y' Mikhal Polak → Ary Leib (d. 1895), Tsieta m. Basin (d. 1912), Pesheh m. Avraham Nakhman Borukovich (d. 1922); Nakhman d. 1918 (s. of Yosef Halevy Berkovits); their children incl. Chifra (b. ~1878, m. Israel Mostkoff), Etle, Malka, Mikhail, Beila (m. Shlomo Yonas, d. 1919). Also the Belarus history primer. Text ends mid-section — superseded by the Narrative for Mostkoff content.

### 5. Borenstein family timeline.pdf — working timeline
Two-page chronology of the Borenstein line, 1870–1942, marking each item **confirmed vs. possible** and flagging open questions inline (Fishel's solo Arizona crossing May 1934; the 1934/35 Warsaw trip; the "parents died 1942" memory vs. Sara d. 1925). The model for how Wendy tracks confidence.

### 6. chronicle.pdf — raw notes
Link collection (FamilySearch Russia records, Belarus archives, JewishGen, BH databases, toldot.ru) + the block of translated **Pinkas of Slutsk Chevra Kadisha** records for the Polak family + Tania's quote describing grandfather Nakhman (Ostrov, furs, "noble but impoverished" Pesya, 11 children) + the "Polaks in Chevra Kadisha of Slutsk" collection + UPenn Boonin/Bunin family letters archive link.

### 7. Slutsk Links.pdf — raw notes
Slutsk Yizkor book links; gravestone 17 translation (Yechiel Michel s. Aryeh, d. 1867); the Yizkor chapter on **Fayvl the Town Sexton (Kharakh/Charach)** — husband of Malka Borukhovich; Sapotskin (Polish-Belarusian border) photo-essay link — the border region grandmother Chaya lived near.

### 8. MOSTKOFF.pdf — raw notes
Memoir excerpt (Isrol Mostkov b. 1880 Ostrov, d. 1956 Mexico; return from Mississippi ~1905–08; sisters Lyubka and Etl; grandmother Khaya near Nesvizh; the "bridge" surname legend; grandfather Leiba; the Dveyra-Dora dysentery story) + **LitvakSIG record: Samuel Mostkow, b. 1883 Novogrudok, mother Khaya Sara Grodzienska** (unplaced candidate relative).

### 9. SUPONITZKY.pdf — lead file
Warsaw Jewish cemetery link (**Sura Borenstein gravestone** — Sara Ayzenszmit Borenstein, d. 1925 Warsaw) + garbled 1877 Priluki marriage record (Min'kov/Supanitskij) — a lead on the Sapotnitsky family name.

### 11. bobespassport/ — Shifra's 1928 Soviet exit passport + the Luis × Chelo ketuba copy
*(11 JPEG scans + README — the corpus's first image-only source, no text layer. Email from Ana Caddess to Wendy Cadieux, 2020-02-04, subject "Bobe's passport"; added to the repo 2026-10-29. The passport photos are reproduced, smaller, inside the Narrative (caption "Shifra Mostkoff's Passport," p. 15; reads at pp. 10, 15, 18–20) — the folder gives the full set at resolution, plus the ketuba copy. Records: **EV-81** (passport) and **EV-82** (ketuba). Citation key: `Bobe's passport, IMG_NNNN`.)*

Contents machine-read 2026-10-29 (purple-ink Cyrillic handwriting is hard; every `[?]` needs eyes on the scan):

| IMG | Best read | Flags |
|-----|-----------|-------|
| 1922 | Title page (Belarusian): ЗАМЕЖНЫ ПАШПАРТ, bearer **Мосткава Шыфра Нахманаўна**, citizen BSSR; children Leiba 14 · Mikhel 11 · Dvoyra 7 | First pass misread the name as "Маслюкова Мара"; focused re-read confirms Мосткава Шыфра |
| 1923 | Info page: b. **1878**, **Bobruisk district**; married; issued **Minsk, 27 Nov 1928**; 50-ruble fee; NKVD BSSR seal | One pass read the birthplace as "Mozyr okrug" — verify (CF-11) |
| 1924 | *(unread — the vision service rejects this file; it is a valid JPEG)* | Needs eyes on |
| 1925 | Russian info page: physical description (medium height, brown eyes, light-brown hair, no special marks); the same page also read "issued Apr 1928" / "exit by 27 Sep 1928" | Conflicts with 27 Nov 1928 on two other pages — reissue or misread; the children's ages (14/11/7) fit November only |
| 1928 | **French summary page** — the identity anchor: "Mostkoff Chifra," b. 1878, Distr. de Bobrouisk, married, citizen BSSR, issued Minsk 27 Nov 1928; children Leiba 14, Michel 11, Abeira [read for Dvoyra] 7 | |
| 1929 | Handwritten internal page, mostly illegible; a border-point word | Read as "Sebezh"-like [?] — cf. IMG_1923 |
| 1930 | Internal page; seals dated 1928/1929 | |
| 1931 | Photo page: young man in dark suit (Luis, 14?) and others; round purple seals over the photo corners | |
| 1932 | Photo page: woman ~50 in headscarf (Shifra) + a child | |
| 1933 | Photo page: four photos; one read as "young woman ~16–20" | Does not match the manifest (Dvoyra was 7); likely an age misjudgment — check the scan |
| 1934 | **Ketuba copy** — Luis × Chelo wedding certificate, Confederación de Centros Israelitas de México; attests the bride's orthodox conversion (per Ana's email) | Date/number/rabbi unread — the CF-06 key |

*Notes: the IMG numbering skips 1926–1927 (two photos not included in the email); the passport's series/number has not been read. Ana, on reading it herself: "I couldn't read any of the Russian pages but it was easy to decipher the ones written in French and the stamps or seals written in Spanish" — the **Spanish seals** (Mexican entry stamps, presumably on IMG_1929/1930) still need a careful read.*

**Verification to-dos (eyes on the scans):** IMG_1924 (entirely unread); the birthplace word on IMG_1923/1925 (Bobruisk vs Mozyr — CF-11); the April/September 1928 dates on IMG_1925; the **Kislev year on IMG_1934** (CF-06); the Spanish entry stamps.

## Observations

- **One master narrative, many satellite notes.** The satellites are working files; the Narrative is the deliverable-in-progress. Phase 2 should extract from all of them into one person-based index rather than editing the PDFs.
- **Overlap/duplication**: the Narrative's intro duplicates the Genealogy PDF's intro (longer version wins); the Pinkas Polak records appear in four files. Extraction should deduplicate against one canonical list.
- **Citation gap**: notes rarely record *where/when* a fact was found beyond a URL. Newspaper links (UFDC) are already keyed to specific pages — good — but record extracts lack full source strings (fond/folio given for some, e.g. NHAB Minsk/1226/2/27). Phase 2 should normalize citations.
- **Images not extracted**: `pdftotext` gets text only; the Narrative's photographs (and cemetery scans etc.) stay in the PDFs. If publication needs them, extract with `pdfimages` or by page rendering later.
- **Confidence discipline already exists** (timeline's confirmed/possible markers, bracketed doubts) — preserve and extend it.
- **What exists outside this folder**: the Narrative intro mentions "hundreds of pages of notes, links and photographs" — more material likely exists elsewhere (Wendy's computer, Ancestry/MyHeritage/Geni trees, the family's photos). Still unaccounted for: Philip's original rough genealogy from "many years ago," and any GEDCOM exports. **Tania's full memoir, however, is located** — published as [The Tania Project](https://www.tania-project.com/) (see RESOURCES.md).
