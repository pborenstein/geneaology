# Roadmap — From Wendy's Notes to a Solid Genealogy

*Written 2026-10-05 after the Phase 1 survey. The end state: a well-sourced, confidently-marked genealogy of the Borenstein/Mostkoff family (both lines, all generations down to the present), in a form Wendy and Philip can read, extend, and share.*

## Guiding principles (carried over from Wendy's own practice)

1. **Every fact carries a source** — record, document, or "family memory (who)". No silent merges.
2. **Confidence is explicit**: confirmed / likely / uncertain — the timeline PDF already works this way.
3. **Name variants are first-class data**: each person keeps an aliases list (Hebrew/Yiddish/secular/Mexican/nickname + transcription misspellings). Cross-genealogy collisions (same names across branches) are checked before anyone joins the tree.
4. **Distinguish** reconstructed facts (from Pinkas, memoir) vs. civil records vs. newspaper announcements vs. memory.

## Phases

### Phase 1 — Survey & project setup ✅ (2026-10-05)
Inventory the 9 PDFs; extract text layers to `extracted-text/`; write SOURCE-SURVEY, FAMILY-OVERVIEW (draft), ROADMAP; set up tracking (docs/, CONTEXT.md, IMPLEMENTATION.md, DECISIONS.md, chronicles/).

### Phase 2 — Master extraction (the big one)
Goal: one consolidated, person-based fact index built from *all* current material, replacing the scattered PDF notes.

- Create `data/people.md` (or CSV — decide at phase start, see DECISIONS): one entry per person — ID, canonical name, aliases, birth/death/marriage facts with place, spouse(s), parents, children, and **source citations** (PDF + page, or URL, or archive fond).
- Work source by source: Narrative (master pass), Notes, Tanya summary + memoir excerpts, chronicle/Slutsk Links/MOSTKOFF/SUPONITZKY (record collections), timeline (Borenstein dates), Genealogy draft (Polak/Borukovich tree).
- Start a `data/conflicts.md`: every place sources disagree (Israel's birth year; Ana Mitelhaus birthplace; Rachmeil vs. Mendel; Khaya's identity...).
- Start a `data/evidence-log.md` of external records already found (JRI-Poland Kurow, Lida births, Pinkas entries, Bobruysk Borukovich, Minsk 1894 dwellers, UFDC links) with full citations — this becomes the bibliography.
- Deliverable: complete person index with no facts left behind in the PDFs; the PDFs can then be treated as archival.

### Phase 3 — Tree assembly
Goal: a single reconciled tree, computer-usable and human-readable.

- Resolve/annotate every conflict in `conflicts.md` (resolve, or record why it stays open).
- Build the tree: likely a **GEDCOM file** (interoperable with Ancestry/MyHeritage/Geni, all of which Wendy already touches) + a rendered chart/report (e.g. via Gramps — free, GEDCOM-native; decision at phase start).
- Extend confidence markers to every edge of the tree.
- Deliverable: `data/borenstein-mostkoff.ged` + generated tree charts + an updated FAMILY-OVERVIEW that is now fully sourced.

### Phase 4 — Targeted research (starts whenever; runs in parallel with 2–3)
Ordered by expected payoff; each lead closes an item in FAMILY-OVERVIEW's mystery list.

1. **Mine the queued UFDC Prensa Israelita links** (~30 in Notes) — dates, spouses, and parents for the Mexico City generation. Cheapest wins; material already collected.
2. **Ask the family**: Pola (Philip says she has information); other Mostkoff/Borenstein cousins in Mexico; the rest of Wendy's "hundreds of pages of notes and photographs"; Tania's full memoir text; Philip's old rough genealogy; any Ancestry/MyHeritage/Geni tree exports (GEDCOMs).
3. **Poland**: JRI-Poland Kurow records (confirm Chaim/Cyrla/Necha; push Borensztejn/Ajzenszmit lines past 1890); Warsaw records for Sara's death (1925) and the 1934–35 visit; cemetery.jewish.org.pl for the gravestone text.
4. **Belarus**: pull the 1889 Minsk marriage record (Wendy's contact at the genealogy society was already on this); JewishGen/LitvakSIG for Mostkov/Saponitsky/Polak/Borukovich; the "Leon from Lithuania" thread.
5. **USA**: Fishel's May 1934 Arizona crossing (border crossing records, Ancestry/CBP indexes, Ancestry collection 1528 already noted); Mississippi/Memphis cousins (Isadore Mostkoff, Iskiwitz family, Baron Hirsch Cemetery); Rosedale/Bolivar County records.
6. **Shoah**: USHMM/Yad Vashem for the 1942 deaths and any family who remained in Warsaw/Slutsk.

### Phase 5 — Publication
Goal: the deliverable Wendy can hand to the family.

- Structure (proposed): introduction & method → the world they lived in (Pale of Settlement, Slutsk, Kurow, Mexico's Jewish community) → line narratives (Borenstein; Mostkoff; Polak/Borukovich) → descendant charts → full source appendix → open questions (kept visible, with status).
- Format decision with Wendy/Philip at phase start: print-ready PDF book (pdf skill available), simple website, and/or GEDCOM for the cousins — not mutually exclusive; the content pipeline (Phase 2/3 data) feeds all of them.
- Include photographs from the Narrative (extract with `pdfimages` when needed).

## Definition of "solid genealogy" (agreed target)

Every person in the tree has: birth/death/marriage data with places where known, alias list, source citations, and a confidence mark; every parent-child link either record-backed or explicitly marked as inferred; the three lines traced as far back as records allow; open questions documented rather than papered over.

## Tools noted along the way

`pdftotext`/`pdfinfo` (installed) for sources; `pdfimages` for photos later; Gramps (candidate, needs install) or plain GEDCOM for the tree; UFDC/JRI-Poland/JewishGen/LitvakSIG/Ancestry as the research sites; this docs/ system for tracking.
