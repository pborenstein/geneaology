# People Index — Borenstein/Mostkoff Genealogy

One entry per **family-connected person** (blood/marriage relatives and record-witnessed kin; background mentions stay in the source notes). Built in Phase 2 extraction passes (DEC-004: single markdown index; GEDCOM conversion deferred to Phase 3).

**Pass status**: All five extraction passes complete (1 Narrative · 2 Notes · 3 Tanya material · 4 record collections · 5 timeline) · **Pinkas pass 2026-10-13** (full Slutsk Chevra Kadisha register → `data/pinkas-hits.md`) · **Prensa Israelita pass 2026-10-14** (EV-35 queue mined → EV-59–80, `data/prensa-hits.md`).

## Conventions

- **IDs** (stable): `A##` Borenstein line · `B##` Mostkoff line · `C##` Polak/Borukovich line · `X##` unplaced/other-affiliation. People are indexed in their **birth line** where known (Shifra Boruchovich → C); spouses without a line marry into their spouse's line.
- **Confidence** (DEC-003): `[C]` confirmed by record · `[L]` likely (source or strong inference) · `[?]` open question.
- **Citations** (short keys; page = PDF page of the file in `base-documents/`):
  - `Narrative, p. N` = *Mostkoff Family Narrative.pdf* (master; 37 pp). The original export embedded a second, repaginated copy of the text as pp. 38–71 — those pages were removed 2026-10-10 after verifying content parity (DEC-008); the 71-page original remains in git history (≤ commit 073001e). Citations were always to first-copy pages, so numbering is unchanged.
  - `Notes, p. N` = *Borenstein Mostkoff Notes.pdf*
  - `Tanya-summary, p. N` = *Summarized Belarus memories of Tanya Mostkoff.pdf*
  - `Genealogy draft, p. N` = *Borenstein-Mostkoff Family Genealogy.pdf*
  - `chronicle, p. N` · `Slutsk Links, p. N` · `MOSTKOFF, p. N` · `SUPONITZKY, p. N` · `timeline, p. N` = same-named PDFs
  - `Pinkas, p. N (entry #M)` = *Pinkas-of-Slutsk.pdf* (full Slutsk Chevra Kadisha register, 1736–1924); extraction in `data/pinkas-hits.md`
  - `tania-project (§N)` = full English translation of Tania's memoir (written 1976–80) at tania-project.com — `src/posts/provisional-translation-en.md`; sections are the memoir's own numbered `###` headers (EV-40).
  - `EV-##` = record in `data/evidence-log.md`; anything else cited by URL verbatim.
- **Aliases**: every person keeps all known variants. Never merge same-named people without corroboration (CLAUDE.md rule). NB the two **Taybas**: the eldest daughter of Chaya & Leibe (B08) and her grandniece Tania herself (B11) — classic cross-branch name collision.
- Where sources disagree, entries cite both sides and reference `data/conflicts.md` (CF-##).

## Index

| ID | Canonical name | b.–d. | One line |
|----|----------------|-------|----------|
| A01 | Szol Kelman Borensztejn | m. 1890 [C] | Kurow patriarch; m. Sura Brandla Ajzenszmidt |
| A02 | Sura Brandla Ajzenszmidt (Borenstein) | d. 1925 Warsaw [L] | Kurow matriarch |
| A03 | Toibe "Touba" Borensztejn (Mitelhaus) | b. 1894 Kurow [C] · d. 23 May 1973 Mexico City [C] | Dau. A01/A02; m. Rachmeil Mitelhaus; children Ana, José, Enrique, Sara [C] |
| A04 | Mendel "Menahem Mendl/Manuel" Borensztejn (Glatt) | b. 1897 Kurow [C] · d. 5 Sep 1965 Mexico City [C] | S. A01/A02; the Glatt patriarch (CF-16 confirmed); six children |
| A05 | Fiszel "Fishel/Felipe" Borenstein | b. 1901 Kurow [C] · d. ~1959/60 Mexico City [C] | S. A01/A02; to Mexico; m. Chana Mindel "Mania" Bauman (A06) |
| A06 | Chana Mindel "Mania/Mañe/Manye/Mane/Malke" Bauman (Borenstein) · civil María | b. ~1902/03 [C/L] · d. 15 Jun 1969 Mexico City [C] | **Felipe's wife, widow & matriarch**; Joseph's mother; A15 merged here (CF-30 resolved 2026-10-19) |
| A07 | Sophia/Sheindel "Sheine Miriam" Chanovesky (Glatt) | b. ~1900s · alive May 1973, Israel [C] | M. Menahem Mendl Glatt (A04); née Chanovesky confirmed [C] |
| A08 | Angela Glatt (Ringel) | b. 1923 Bialystok [L] | Dau. of A04/A07; m. Isaac Ringel [C]; mother of Myrna, Freddie, Janette |
| A09 | Myrna (Ringel) Bilak | b. 4 Feb 1946 Mexico City · d. 4 Sep 2001 [C] | Dau. of Angela; obit EV-39 |
| A10 | Janette (Ringel) Epstein | — | Dau. of Angela [C obit] |
| A11 | Alfredo Ringel | — | S. of Angela [C obit] |
| A12 | Chaim Borensztejn? | b. 1891 Kurow? [?] | Possible child of A01/A02 (timeline) |
| A13 | Cyrla Borensztejn? | b. 1892 Kurow? [?] | Possible child of A01/A02 (timeline) |
| A14 | Necha Borensztejn? | b. 1895 Kurow? [?] | Possible child of A01/A02 (timeline) |
| A15 | → merged into A06 (2026-10-19) | — | Chana Mindel Bauman = Mania (CF-30 resolved); ID retained as redirect |
| A16 | Enrique Borenstein | b. 1926 Mexico City [C] | S. Fishel & Chana (Henry/Herszel/Hersh/Tvi); m. Emma [C]; 5 children [C] |
| A17 | Sidney Borenstein | b. 1927 Mexico City [C] | S. Fishel & Chana; m. Rebecca Finkler [C]; children Susana, Saúl, Ruth [C] |
| A18 | Joseph "Jose/Joe" Borenstein Bauman | b. 1936 Mexico City [C] · d. Mar 2026 [C] | S. Fishel & Chana Mindel "Mania" (A06); m. 1) Ana Mostkoff Linares (B17) 15 Mar 1959 [C] → Philip, Edna/Jaye, Shifra; div. 1978 [C]; m. 2) Carol Ackerman ~1986 [L] |
| A19 | Max Glatt | b. ~1920s | S. A04/A07; m. Elena; daughters Susy, Nelly, Nancy, Julie [C] |
| A20 | Lic. Jacobo Glatt | b. ~1920s | S. A04/A07; m. Irene Russek; sons Sigui (A21), Siggie, Eddie, Carlos [C] |
| A21 | Sigui "Shaul" Glatt Russek | b. ~1950 | S. A20; bar mitzvah 1963 [C]; grandfathers Manuel Glatt & Gabriel Russek |
| A22 | Benny Glatt | b. ~1920s | S. A04/A07; m. Eugenia; later Israel [C] |
| A23 | Sonia Glatt (Schwarz) | b. ~1920s | Dau. A04/A07; m. Marcus Schwarz; children Teddy, Vivian, Jacqueline [C] |
| A24 | Anita/Nejume Glatt (Epelstein) | b. ~1930s | Dau. A04/A07; m. Isaac Shajne Epelstein 1953 [C]; son Elías b. 1956 |
| A25 | Isaac Ringel | b. ~1920s | M. Angela Glatt (A08) [C]; s. of Bernardo Ringel |
| A26 | Freddie Ringel | b. ~1940s | S. Isaac & Angela [C]; brother of Myrna (A09), Janette (A10), Alfredo (A11) |
| A27 | Sara Borenstein (Jarovinsky) | b. ~1900 | **Sister of Felipe/Toibe/Mendel** [L — structural]; m. Víctor Jarovinsky (A28) |
| A28 | Víctor Jarovinsky (Yarowinsky) | b. ~1890s | M. Sara Borenstein (A27); the Jarovinsky in-law patriarch |
| A29 | Alberto Jarovinsky | b. ~1932 · d. 2 Jan 1970 [C] | S. A27/A28; m. Rosa/Reizl; died Acapulco–Iguala road with son Salomón (10) |
| B01 | Aryeh Leib "Leibe/Lev" Mostkoff | b. ~1855–60 [L] · d. young [C memoir] | Patriarch; poor; house by the bridge (surname legend) |
| B02 | Chaya (Sapotnitsky?) Mostkoff | b. ~1855–60 [L] · d. not in Slutsk register — likely near Nesvizh [?] | Matriarch; village near Nesvizh; lived with Israel's family |
| B03 | Morduckh "Motl/Motel/Max" Mostkov | b. ~1877 [L] | Eldest known son; m. Dvora Portnoy 1906 Lida [C]; Lida children 1907–13 [C] |
| B04 | Israel "Isrol Leibovich" Mostkoff | b. 1880 Ostrov [C memoir] · d. 1956/57 Mexico City [CF-02] | Mississippi ~1895–1905; m. Shifra ~1907; to Mexico 1924/25 |
| B05 | Eiser "Isodoro/Isadore" Mostkoff | b. 1888 [C] | Brother; Mississippi fur trade; buried Clarksdale MS |
| B06 | Hinde "Ginde/Ginda" Mostkoff | — | Dau. of B01/B02; m. ___ Charches [?] |
| B07 | Keili "Clara?" Mostkoff (Iskiwitz) | — | Dau. B01/B02; m. Iskiwitz (Israel vs. Reuben — CF-12); Memphis line |
| B08 | Taiba/Tayba Mostkoff (Tsukovich?) | — | "Eldest daughter" (memoir); son Israel Tsukovich |
| B09 | Lyubka Mostkoff | — | **Israel's sister** (memoir, explicit); mother of Bronya & Grisha (Leningrad) |
| B10 | Abram "Abraham/Avram" Mostkoff | b. Apr 1909 [C memoir] | S. Israel & Shifra; to Mexico 1926; m. Clara Nudelman, later Leonor [C]; grandchildren incl. Nachman, Rubén, Motele, Violeta [C] |
| B11 | Tania "Tayba/Tanya/Tatyana" Mostkoff (Baskin) | b. Jun 1911 Slutsk [C memoir] | Memoir author; Moscow 1926; USSR; m. Iosif Baskin; 3 children; "Yosef y Taia Baskin" greet Ana's 1959 wedding from Moscow [C] |
| B12 | Aryeh Leib "Leiba/Luis" Mostkoff | b. Aug 1914 [C memoir] | S. Israel & Shifra; "the potato-eater"; m. Chelo Linares 1939; six children |
| B13 | Mikhail "Mikhl/Miguel/Miquel" Mostkoff | b. Nov 1917 [C memoir] | S. Israel & Shifra; m. Berta Tolmatsky; children Alberto (d. 1959, 14), Silvia |
| B14 | Dvoira "Dveyra/Dora/Doris" Mostkoff (Glassman, Padawer) | b. Aug 1921 [C memoir] | Dau. Israel & Shifra; Memphis by 1959 [C], later St. Louis; m. David Glassman, later Lawrence Padawer |
| B15 | Maria Consuelo "Chelo" Linares Lopez | b. 7 Aug 1917 Mexico [C] | M. Luis Mostkoff 1939; six children |
| B16 | Lucy Mostkoff Linares | b. 10 Mar 1939 [C] | Eldest dau. Luis & Chelo; m. Harry Pepper, Memphis [C] — CF-15 leaning resolved |
| B17 | Ana "Anita" Mostkoff Linares (Borenstein; Caddess) | b. 29 Dec 1940 [C] | M. 1) Joseph Borenstein 15 Mar 1959 [C] → Philip, Edna/Jaye, Shifra; m. 2) Hugh N. Caddess 2 Jan 1982 [C] |
| B18 | Moises Mostkoff | b. 13 Jan 1942 [C] | S. Luis & Chelo |
| B19 | Pola "Pesele" Mostkoff (Bierzwinski) | b. 13 Apr 1946 [C] | Dau. Luis & Chelo; m. Jaime Bierzwinski 18 Dec 1965 [C]; may hold family information (Philip) |
| B20 | Isidoro "Lazaro?" Mostkoff | b. 26 Mar 1950 [C] | S. Luis & Chelo |
| B21 | Aida "Hinde" Mostkoff | b. 31 Mar 1957 [C] | Youngest dau. Luis & Chelo; Hebrew name Hinde [C] |
| B22 | Ignacio Mostkoff Nudelman | b. ~1938 [L] · d. 15 Mar 2013 [C] | S. Abram [L]; m. Bella; structure vs. memoir — CF-20 |
| B23 | Louise Mostkoff | — | Dau. of Isadore Mostkoff (B05) [L], Rosedale MS |
| B24 | Etl Mostkoff (Reznik) | — | Sister of Israel (memoir); Urechye; m. Samuil Reznik |
| B25 | Israel/Isrol Tsukovich | b. ~1902–04 [L] | S. of the eldest sister (B08); the stove-scene nephew |
| B26 | Dveira-Dora (Mostkova?) | d. ~1921 Slutsk [C memoir] | Israel's niece; died of dysentery; B14 named for her [L] |
| C01 | Y' Mikhal Polak | b. ~1840s [?] | Father of Pesheh/Ary Leib/Tsieta (pinkas); candidate = Mikhel b. 1847 Minsk |
| C02 | Pesheh "Pesya" Polak | d. 1 Apr 1922 Slutsk [C pinkas] | Rich Polak stock; m. Nakhman; 11 children, 4 grew up |
| C03 | Avraham Nakhman Borukovich | alive ≥1932 [C memoir] | Furs/customs specialist; pinkas-1918 death NOT his (CF-13) |
| C04 | Ary Leib Polak | d. 13 Jan 1895 Slutsk [C] | S. Y' Mikhal Polak; melamed of Talmud Torah |
| C05 | Tsieta Polak (Basin) | d. 31 Mar 1912 Slutsk [C] | Dau. Y' Mikhal Polak; m. Kalman Osher Basin |
| C06 | Shifra/Chifra/Sofia Boruchovich (Mostkoff) | b. 1880 Slutsk [C memoir] (obit age → ~1877, CF-31) · d. 24 Sep 1962 Mexico City [C obit] | Dau. C02/C03; seamstress; m. Israel Mostkoff; obit under "Sofía" [C] |
| C07 | Malka Boruchovich (Kharakh) | — | Dau. C02/C03; Krupskaya Academy; Bobruisk→Vitebsk; m. Faivel; children Misha, Polya |
| C08 | Faivel Kharakh (Harakh/Charach) | — | M. Malka; Slutsk "town sexton" of the Yizkor chapter (pass 4) |
| C09 | Beila Borukovich (Yonas) | d. 4 Feb 1919 Slutsk [C] | Dau. of Avraham Barukhovits [C]; m. Shlomo Yonas; probable 4th sibling [L] |
| C10 | Kalman Osher Basin | — | M. Tsieta Polak (C05) |
| C11 | Shlomo Yonas | — | M. Beila Borukovich (C09) |
| C16 | Yosef Polak | d. 27 Jan 1915 Slutsk [C] | S. of Y' Leib Polak; possibly C04's son [?] |
| C12 | Mikhail "Meishke" Borukhovich | d. ~1925/26 Minsk [C memoir] | S. Nakhman & Pesya; Leningrad medical institute; suicide; m. Khaya Pastron |
| C13 | Khaya Pastron (Borukovich) | — | M. Mikhail (C12); Moscow; daughter Genya |
| C14 | Yakhna Borukhovich | alive 1941 [C memoir] | Nakhman's sister; grain shop, Slutsk; died in 1941 family suicide |
| C15 | Khaim-Yudl Borukhovich | d. 1941 Slutsk [C memoir] | S. Yakhna; pharmacist (Gipchin's); poisoned household ahead of German action |
| X01 | Yitskhak "Isaac" Bunin | d. 31 Jan 1922 [C] | Killed in Dalhinoveh massacre (Pinkas 229); father of Masha & Nina |
| X02 | Mendil Bunin (Boonin) | d. 11 Jan 1915 [C] | S. Y' Leib Boonin; m. Sheina Dvora; sons Yitskhak & Natan |
| X03 | Sheina Dvora (Tsiptsin) Bunin | d. 15 Aug 1916 [C] | Dau. of Yitskhak Tsiptsin — Sapotnitsky variant? CF-10 |
| X04 | Masha Bunin/Guitiyk | — | Dau. of Isaac Bunin; grew up in the Mostkoff home |
| X05 | Nina Bunin/Guitiyk | — | Dau. of Isaac Bunin; grew up in the Mostkoff home |
| X06 | Leobardo Linares | — | Father of Chelo Linares Lopez |
| X07 | Petra Lopez Fuentes | — | Mother of Chelo Linares Lopez |
| X08 | Chaim Owzer Mostow | b. 1878 · d. 2 Mar 1935 Vilnius [C] | Candidate sibling of Israel (patronymic Lejb) [?] |
| X09 | Movshe "Moshe" Mostkov | b. ~1876 · d. 12 Jun 1911 Vilnius [C] | Candidate sibling of Israel (patronymic Leyb) [?] |
| X11 | Harold "Skeeter" Mostkoff | b. ~1918 Rosedale MS · d. 31 Jul 2006 Baton Rouge [C] | Candidate son of Isadore (B05) [?] |
| X12 | Bronya Leybovna Barshay | — | Burial record; dau. of Lyubka (B09) [L memoir] |
| X13 | Abraham Borenstein | b. 1906 · d. 1990 | Ancestry record — different family or mis-merge? [?] |
| X14 | Moshek Polak | b. 11 Oct 1852 Minsk [C] | Brother of the 1847 Mikhel candidate; relation to C01 unknown [?] |
| X15 | Samuel Mostkow (Mostk) | b. 1883 Novogrudok [C] | LitvakSIG record; mother Khaya Sara Grodzienska; unplaced [?] |
| X16 | Movsha Borukhovich | — | Bobruysk records; likely Nakhman's brother [L]; wife Feiga; children Yenta, Iakha, Girsha |
| X17 | "Navy brother" Borukovich | — | Youngest s. Pesya & Nakhman; ran away to the navy, never returned [C memoir] |
| X18 | David & Lipke (—?) | — | "Uncle David and Aunt Lipke," hide workers, Bolotnaya St. Slutsk; dau. Luba → Poland [?] |
| X19 | David Tolmatsky | d. after 1962 | Father of Berta (B13's wife) [C]; widower of Busi (X20); mejutan in Shifra's obit |
| X20 | Busi Tolmatsky | d. Dec 1958/Jan 1959 [C] | Mother of Berta [C]; obit names "Ydele y Silvita" as granddaughters |
| X21 | Java Finkler | b. ~1885 Ukraine [L] · d. 20 Nov 1959 [C] | Mother of Rebecca Finkler (A17's wife) [L]; "de Ucrania" |

*Spouses without separate entries (one-liners): Dvora Portnoy (B03) [C]; Annie Frank (B05); Iosef/Iosif Baskin (B11); Berta "Busi" Tolmatsky (B13 — parents X19/X20); David Glassman & Lawrence Padawer (B14); Clara Nudelman & Leonor Esquinazzi (B10); Bella (B22's widow); Samuil Reznik (B24); Genya Borukhovich (dau. of C12); Emma/Ema (A16); Rebecca Finkler (A17 — mother X21); Elena (A19); Irene née Russek (A20 — dau. of Gabriel Russek); Eugenia (A22); Marcus/Marcos Schwarz (A23 — mother Jane Rivke Schwarz); Isaac Shajne Epelstein (A24 — father Alter Yaacov); Rosa/Reizl (A29); Jaime Bierzwinski (B19); Harry Pepper (B16); Hugh N. Caddess (B17 — 2nd husband, m. 2 Jan 1982 [C — Philip, 2026-10-19]); Carol Ackerman (A18 — 2nd wife, m. ~1986 [L — Philip, 2026-10-19]).*

## Line A — Borenstein (Kurow, Lublin gubernia, Poland → Mexico City)

*(Passes 2 + 5: JRI-Poland Kurow extractions (Notes, pp. 17–18), the timeline chronology, the Genealogy draft's naming notes, and the Prensa Israelita queue. Kurow PSA holdings: births 1862–98, marriages 1868–1908, deaths 1871–76/82–98/1901–08; Fond 1751, Lublin Archive — Notes, p. 17.)*

### A01 · Szol Kelman "Saul Kalmon/Kalman" Borensztejn
- b. ~1870 `[L]` timeline, p. 1; m. **Sura Brandla Ajzenszmidt** 1890, Kurow, akta 4 `[C]` EV-31.
- Children (Kurow births): **Toibe 1894** `[C]` EV-32, **Rachmeil-Mendel 1897** `[C]` EV-32, **Efraim Fishel 1901** `[C]` EV-32; possible (timeline, p. 1): Chaim 1891, Cyrla 1892, Necha 1895 `[?]` (A12–A14).
- Death unknown — Joseph's 1942 "parents' deaths" memory (A05) might mean Saul d. 1942 Warsaw `[?]` timeline, p. 2 (mystery 2).

### A02 · Sura Brandla "Sara Friendel" Ajzenszmidt (Ayzenszmit; Borenstein)
- b. ~1879 `[L]` timeline, p. 1; m. 1890 Kurow `[C]` EV-31.
- d. **1925 Warsaw** `[L]` timeline, p. 1; gravestone in the Warsaw Jewish cemetery (cemetery.jewish.org.pl, list c_1) `[C link]` EV-47 — the timeline once writes "1935" for this death (p. 2) — **CF-28**.

### A03 · Toibe "Touba" Borensztejn (Mitelhaus)
- b. 1894, Kurow, akta 7 `[C]` EV-32; d. **23 May 1973, Mexico City, age 79** — obituary "Sra. Vda. Toibe Mitelhaus Borenstein" (exact match to the Kurow birth year) `[C]` EV-73.
- m. **Rachmeil Mitelhaus** ~1933 `[L]` timeline, p. 2.
- Children (full set, Prensa 1969/73) `[C]` EV-72/73: **Ana Mitelhaus** b. 1934 — Warsaw per most records, Mexico per one (**CF-27**); m. Fayerman, dau. **Lilia**; **Jose Mitelhaus** b. 1937, d. **10 Jun 1969** `[C]` EV-72; **Dr. Enrique Mitelhaus**; **Sara Mitelhaus**. (Timeline knew only Ana & José.)
- Buried beside son José, in the plot she chose the day he died `[C]` EV-73.
- Repeatedly the "Tía Toibe" of Prensa notices (EV-59/60/61) — the surviving sister of the Kurow generation.

### A04 · Mendel "Menahem Mendl/Manuel" Borensztejn (Glatt)
- b. 1897, Kurow, akta 63 — JRI record name **Mendel** `[C]` EV-32; d. **5 Sep 1965, Mexico City, age 68** — obituary "Menahem Mendl Glatt" `[C]` EV-63 (b. ~1897 ✓).
- **The Glatt patriarch — CF-16 confirmed by convergence (2026-10-14)**: one man with the Rachmeil-Mendel double name, later Glatt. Evidence: his 1965 obit gives b. ~1897 = the Kurow record; "Fishl y Mane Borenstein (Tíos de la novia)" at his daughter Anita's 1953 engagement (EV-64) — Felipe his brother; "Mendl Glatt" among the "Tíos" at Philip's 1961 bris alongside Toibe Mitelhaus and Víctor Jarovinsky (EV-60); his children appear as Felipe's "Sobrinos" (EV-61) and among Mania's "Sobrinos" (EV-62); Sheindl is Toibe's "Cuñada" (EV-73); grandson Sigui's bar mitzvah names grandfather "**Manuel** Glatt" (EV-66). Why the surname diverges (Borensztejn in Kurow records vs. Glatt from the Bialystok years on) remains open `[?]` — cf. Angela b. 1923 Bialystok as "Glatt."
- m. **Sophia/Sheindel Chanovesky** (A07) between 1915–22, place unknown `[L]` timeline, p. 1.
- Children `[C]` EV-63/66/67: **Max** (A19), **Lic. Jacobo** (A20), **Benny** (A22), **Angela** (A08, b. 1923 Bialystok), **Sonia** (A23), **Anita** (A24).
- Funeral rabbis: Rafalón, Avigdor, Hershberg, Rosenbaum, Goldberg `[C]` EV-63.

### A05 · Fiszel "Fishel/Felipe/Philip" Borenstein (Efraim Fishel; once indexed "Peroim Pizzel")
- b. 1901, Kurow, akta 42 `[C]` EV-32; **d. ~1959/60, Mexico City** — matzevah unveiling 14 Aug 1960 `[C]` EV-61 (death notice itself still unfound); rabbis Rafalón & Goldberg at the unveiling.
- m. **Chana Mindel "Mania" Bauman** (A06; the Prensa's "Malke"/"Mania" — CF-30 resolved) between 1919–25, place unknown `[L]` timeline, p. 1; emigrated to Mexico ~1919–25 (with Chana?) `[?]` timeline, p. 1.
- Children, b. Mexico City `[C timeline, p. 1–2]`: **Enrique** 1926 (Henry/Herszel/Hersh/Tvi — A16), **Sidney** 1927 (A17), **Joseph/Jose** 1936 (A18), an unnamed son d. at birth 1942.
- **May 1934: crossed into Arizona without family — destination/purpose unknown** (open mystery; border-crossing records queued — Ancestry collection 1528, Notes, p. 11) `[?]` timeline, p. 1.
- **1934/35: Warsaw trip** — Joseph remembers Fishel, Chana, Enrique and Sidney going; family story of "going back to Poland to show off Chana's jewels" `[?]` timeline, pp. 1–2.
- 1942: "Fishel told of parents' deaths" — but Sara d. 1925; perhaps Saul d. 1942, or Chana's parents, or siblings — check Shoah records `[?]` timeline, p. 2.
- Prensa trail: "Fishl y Malke Borenstein (Padres del novio)" at José's 1959 wedding; "Fishl y Mane Borenstein (Tíos de la novia)" 1953; his own unveiling 1960 (EV-59/61/64).

### A06 · Chana Mindel "Mania/Mañe/Manye/Mane/Malke" Bauman (Borenstein) — civil name María Borenstein — Felipe's wife, widow and matriarch (A15 merged here 2026-10-19)
- **One woman** `[C — Philip, 2026-10-19]`: Mania, Mañe, Manye, Chana Mindel, María Borenstein — Felipe Borenstein's wife and Joseph's mother — are all the same person (direct family testimony; **CF-30 resolved**). The record chain already pointed there: her son's Mexican legal name **José Borenstein Bauman** fixes her as née Bauman, and EV-62 makes her José's mother. Formerly split as A06 (the Prensa's "Mania") and A15 (the timeline's "Chana Mindel Bauman"); A15 now redirects here.
- **Not a sibling of Fishel** (the earlier inference from "Fishl and Mane as uncles of the bride" is corrected): the Prensa shows her consistently as **Felipe's wife** — "(Esposa)" at his 1960 unveiling; "(Abuelita)" at Philip's 1961 bris; her own obituary names Enrique, Dr. Sidney and Dr. José as her sons `[C]` EV-60/61/62.
- b. ~1902/03 — obit "67 at death" → ~1902 `[C]` EV-62; timeline ~1903 `[L]` timeline, p. 1. Sister **Sura Ita Bauman** b. ~1904 `[L]`; parents unknown — **Herz Bauman** gravestone links (Notes, p. 11) may be her father `[?]`.
- m. Fishel (A05) 1919–25 `[L]` timeline; the 1934/35 Warsaw "showing off Chana's jewels" story `[?]`.
- d. **Sunday 15 Jun 1969, Mexico City**, buried same day; rabbi Rafalón `[C]` EV-62.
- Names: Hebrew/Yiddish **Chana Mindel**; called **Mania / Mañe / Manye** in the family `[C — Philip]`; printed **Mania / Mane / Malke** in the Prensa 1953–69 `[C]` (the 1959 "Malke" = variant or OCR); Mexican civil name **María Borenstein** `[C — Philip]`. No natal relatives appear in her obit (consistent with the Baumans being outside Mexico).
- Grandchildren at her death: Gerardo, Fernando, Eduardo, Esther, Felipe (Enrique's); Susana, Saúl, Ruth (Sidney's); Edna, Felipe, Shifra (José's) `[C]` EV-62.
- Her obituary was ordered and administered by Rebeca (Sidney's wife), per the paper's 1969 collection notice `[C]` EV-62.

### A07 · Sophia/Sheindel Chanovesky (Chovesky; Glatt) — "Sheine Miriam"
- m. Menahem Mendl Glatt (A04) between 1915–22 `[L]` timeline, p. 1; the Prensa prints her as **"Sheindl"/"Sheine Miriam"** `[C]` EV-63/65/72.
- **Née Chanovesky confirmed**: her husband's 1965 obit lists **Zalmen & Dov Chanowsky** (her brothers) and US relatives Sara Cohen / Jack Cohen family `[C]` EV-63.
- **Alive May 1973, living in Israel** — "(Cuñada-Israel)" in Toibe's obituary `[C]` EV-73 (upgrades "alive 1966").
- Children: Max, Jacobo, Benny, Angela, Sonia, Anita (see A04).

### A08 · Angela Glatt (Ringel)
- b. 1923, Bialystok `[L]` timeline, p. 1; dau. of A04/A07 — confirmed as "(Hija y yerno)" with Isaac in her father's 1965 obit `[C]` EV-63.
- m. **Isaac Ringel** `[C]` EV-63/67 (A25; father Bernardo Ringel, the 1953 "consuegro," EV-64).
- Children `[C]` EV-39/66/67: Myrna (A09), Janette/Jeanette (A10), Alfredo (A11), **Freddie** (A26).

### A09 · Myrna Bilak (Ringel)
- b. 4 Feb 1946, Mexico City; d. 4 Sep 2001, Las Vegas `[C]` EV-39; sons Dorian, Olivier, Marcel Bilak; sister Janette Epstein (Marbella), brother Alfredo Ringel (Guadalajara).

### A10 · Janette (Ringel) Epstein — dau. of Angela `[C]` EV-39.
### A11 · Alfredo Ringel — s. of Angela `[C]` EV-39.

### A12 · Chaim Borensztejn? — possible s. of A01/A02, b. 1891 Kurow `[?]` timeline, p. 1. No further trace.
### A13 · Cyrla Borensztejn? — possible dau., b. 1892 Kurow `[?]` timeline, p. 1.
### A14 · Necha Borensztejn? — possible dau., b. 1895 Kurow `[?]` timeline, p. 1.

### A15 · Chana Mindel Bauman → merged into **A06** (CF-30 resolved 2026-10-19: the same woman as "Mania"; ID retained as a redirect, all facts now under A06).

### A16 · Enrique Borenstein — b. 1926, Mexico City `[C]` timeline, p. 1 (Henry/Herszel/Hersh/Tvi). m. **Emma/Ema** `[C]` EV-60/62. Children `[C]` EV-62: **Gerardo, Fernando, Eduardo, Esther, Felipe**.
### A17 · Sidney Borenstein — b. 1927, Mexico City `[C]` timeline, p. 1; m. **Rebecca Finkler** `[C]` EV-59/62 ("Dr. Sidney y Rebeca"); children `[C]` EV-62: **Susana, Saúl, Ruth**. Rebecca's mother **Java Finkler** d. 1959 (X21, EV-71); Rebecca administered Mania's 1969 obituary `[C]` EV-62. Almost certainly the "**Sydney Borenstein Bauman**" who was medical certifier on Shifra's 1962 death certificate `[C]` EV-14 (signed with both family surnames).
### A18 · Joseph "Jose/Joe" Borenstein Bauman — b. 1936, Mexico City `[C]` timeline, p. 2; d. **March 2026** `[C — Philip, 2026-10-19]`; m. **Ana Mostkoff Linares** (B17) **15 Mar 1959, Centro Deportivo Israelita** `[C]` EV-59; in the US June 1969 (José Mitelhaus's obit) `[C]` EV-72; children **Philip (Felipe; indexed Felipe Mostkoff / Felipe Mostkoff Borenstein / Felipe M. Borenstein)**, **Edna (Jaye; indexed Edna or Jaye, switched between indexes)**, and **Shifra** — Philip & Edna per Genealogy draft, p. 2; Shifra per Philip `[C — 2026-10-13]` (living; names only). Philip's bris (as **Fishl**) 9 Jan 1961, mohel David Klipp `[C]` EV-60; "Edna y Fishele" greet Shifra's 1962 obit `[C]` EV-68. Ana and José **divorced 1978** `[C — Philip, 2026-10-19]`; José m. 2) **Carol Ackerman**, **~1986** `[L — Philip, 2026-10-19; year uncertain]`. **Names** `[C — Philip, 2026-10-19]`: **José Borenstein Bauman** (Mexican legal form — the maternal apellido **Bauman** fixed his mother as née Bauman, the key that resolved **CF-30**) · **José Borenstein** · **Joseph (Joe) Borenstein** (US form; cf. "Dr. José Borenstein (Estados Unidos)" in June 1969, EV-72). Wedding date 15 Mar 1959 independently confirmed by family (= EV-59).

### A19 · Max Glatt — s. of A04/A07 `[C]` EV-63; m. **Elena**; padrino at Elías Epelstein's 1956 bris `[C]` EV-65; daughters **Susy, Nelly, Nancy, Julie** `[C]` EV-66/67. His father's "mejutan" circle (Braun, Ellstein, Rudoy, Port, Gershberg) = the in-law network.
### A20 · Lic. Jacobo Glatt — s. of A04/A07 `[C]` EV-63; m. **Irene Russek** (dau. of Gabriel Russek, the 1953 "consuegro" — EV-64) `[C — structural]` EV-66; sons **Sigui/Shaul (A21), Siggie, Eddie, Carlos** `[C]` EV-66/67.
### A21 · Sigui "Shaul" Glatt Russek — s. of A20; bar mitzvah 24 Oct 1963, Shul Agudas Ajim (Thursday — both grandfathers are gabaim and avoid Shabbat driving) `[C]` EV-66; the Notes' "cousin to Joseph/Enrique/Sidney Borenstein" ✓ (first cousin once removed via A04).
### A22 · Benny Glatt — s. of A04/A07 `[C]` EV-63; m. **Eugenia** ("Hegenia"/"Hee" in OCR) `[C]` EV-63/67; later Israel (sobrino "(Israel)" in Toibe's 1973 obit) `[C]` EV-73.
### A23 · Sonia Glatt (Schwarz) — dau. of A04/A07 `[C]` EV-63; m. **Marcus/Marcos Schwarz** `[C]` EV-63/67; children **Teddy** (bar mitzvah 12 Feb 1966, b. ~1952/53 — already named in EV-66, 1963), **Vivian, Jacqueline** `[C]` EV-66/67; grandmother Jane Rivke Schwarz; Marcos's family linked to Venezuela (mejutanim, EV-63).
### A24 · Anita/Nejume Glatt (Epelstein) — dau. of A04/A07 `[C]` EV-63; her 1953 engagement notice prints the bride as "**Nejume**" (Nechemá?) with the 1956 bris naming her **Anita** — same couple `[L]` EV-64/65; m. **Isaac Shajne Epelstein** (father Alter Yaacov) 1953 `[C]` EV-64; children **Becky, Alex, Silvia, Mónicque**; son **Elías** b. Aug 1956 (bris 5 Aug 1956, mohel David Klipp) `[C]` EV-65.
### A25 · Isaac Ringel — m. Angela Glatt (A08) `[C]` EV-63/67; s. of **Bernardo Ringel** (the Glatt family's "consuegro," 1953) `[C]` EV-64; "tío" at the 1953 engagement and 1956 bris; father of Myrna (A09), Janette (A10), Alfredo (A11), Freddie (A26).
### A26 · Freddie Ringel — s. of Isaac & Angela `[C]` EV-66/67 ("Fredy"/"Freddie," with Myrna and Janet, 1963/1966); no further records yet.
### A27 · Sara Borenstein (Jarovinsky) — sister of Felipe (A05), Toibe (A03) and Mendel (A04) `[L — structural]`: "Víctor Yarowinski y fam. (Cuñados)" at Felipe's unveiling (EV-61); "Víctor y Sara Yarowinsky" tíos at Philip's bris (EV-60); her daughter's 1964 wedding lists the Borenstein boys as "Primos" and Mania as "Tía" (EV-76). Appears as "Víctor y Sara Jarovinski (Padres de la novia)." Kurow birth record not yet located (A12–A14 candidates?) `[?]`.
### A28 · Víctor Jarovinsky (Yarowinsky/Jarovinski) — m. Sara Borenstein (A27) `[L]`; the family's pervasive in-law: "tío" at José's 1959 wedding, "cuñado" at Felipe's 1960 unveiling; his son Alberto (A29) m. Rosa/Reizl; daughter Sara m. Abraham 1964 `[C — events]` EV-59/61/76. A second Jarovinsky brother m. **Sheindl Mac** (d. Mar 1970, sister of Keren Hayesod's Aarón Mac) `[?]` EV-75; the Macs appear as "mejutanim" at Mostkoff-Borenstein events EV-59/60/62.
### A29 · Alberto Jarovinsky — s. of A27/A28; b. ~1932; m. **Rosa/Reizl** `[C]` EV-59/62/76; children **Salomón, Tzipora, Esther** (the 1964 "sobrinos") `[C]` EV-76. **Died with his son Salomón (10) in a road accident on the Acapulco–Iguala highway, Friday 2 Jan 1970**; buried 4 Jan `[C]` EV-74.

## Line B — Mostkoff (Ostrov/Slutsk, Belarus → Mexico City)

### B01 · Aryeh Leib "Leibe/Lev" Mostkoff (Leiba; Leon?)
- b. ~1855–60, "about the same time as Chaya" `[L]` Narrative, p. 5. "He was a poor man — that much I know for certain, and the growing young people left for America" `tania-project (§4)`.
- Married **Chaya** ~1875–76 `[L]` Narrative, p. 5. Candidate civil-marriage record 1889 Minsk (EV-10; son Israel b. 1880 predates it — religious marriage earlier, or wrong record) — under that hypothesis Leibe's father was Zisman `[?]` Notes, p. 12.
- Israel's patronymic **Leibovich** and headstone "Israel son of Aryeh Leib" `[C]` MOSTKOFF, p. 1; Narrative, p. 6; memoir: "his own father, Lev, died young, leaving a wife and children behind" `tania-project (§34)`.
- d. before 1914 (birth of grandson Aryeh Leib/Luis — Ashkenazi don't name for the living) `[L]` Narrative, p. 5.
- Surname legend: house near a bridge → "Mostkov" ("bridge") `tania-project (§4)`. "Leon from Lithuania" theory: name more prevalent in Litvak databases; family may have started in Lithuania `[?]` Notes, p. 12.

### B02 · Chaya (Sapotnitsky?) Mostkoff (Khaya; Sapotnisky/Saptonitsky)
- Surname is a **guesstimate** from Israel's Mexican death record "Israel Mostkoff Saptonitsky"; no other confirmation `[?]` Narrative, pp. 4–5.
- b. 1837–62 bounds; Wendy proposes ~1855–60 `[L]` Narrative, p. 4.
- "Lived her whole life in a distant village near the Polish border, near **Nesvizh**" `tania-project (§4)` — the older translation's "Neswalok" was a misreading: the memoir's Russian original says **Несвиж (Nesvizh)** outright, and the site's gazetteer places it (53.22°N 26.69°E) "near the Polish border of the time" (the interwar Riga border ran just west of Nesvizh). See **docs/investigations/sapotnitsky.md** for the full name investigation.
- Lived with Israel's family on Sadovaya St. in Tania's childhood (corner of the bedroom; knitting; "I don't even remember when she left us, or perhaps died") `tania-project (§4)`.
- "Many children": Tayba (eldest daughter), Motle, Ginde, Eizer, Israel + "others"; "all my father's brothers and sisters, along with their children and grandchildren, live in the USA" (as of 1976–80) `tania-project (§§4, 35)`.
- Death: **timing unknown** — the Narrative's "1917–18, kidney disease, Tania 6–7" is almost certainly a misattribution of the *Pesya* memory (CF-22).
- **Full-register verdict (2026-10-13)**: grandmother Chaya is **not in the Slutsk pinkas at all** — all 58 Khaya/Chaya deaths 1914–24 enumerated, every Khaya-wife-of-a-Leib across 1736–1924 checked, zero Mostkov burials (CF-17 resolved-leaning negative). She presumably died and was buried in her village region near **Nesvizh**. The #870 candidate (Chaya-Henya Itskovits) is further weakened: her husband Zev Volf Itskovits, tailor of Oreitsa, d. 7 Feb 1914 aged 90 `Pinkas, p. 258 (entry #1809)`.
- Surname & natal family: see **docs/investigations/sapotnitsky.md** (the 1889 Minsk "Khaia Zaturinskii" marriage cannot be hers on age — CF-29 — but may be a younger namesake cousin of the same Nesvizh clan; father candidate Zelik `[?]`).

### B03 · Morduckh "Motl/Motel/Max" Mostkov (Mordukh; Mordoch)
- b. ~1877 (age 29 at 1906 marriage) `[C]` EV-01; "about 1877" Narrative, p. 5; "= Motl Moskov, brother to Israel and son of Leibe (Leon) and Chaya" Notes, p. 14.
- Of **Dvoretz**; m. **Dvora (Dveyra) Portnoy** (23, of Radun; father Pinkhus) 30 May 1906, Lida `[C]` EV-01.
- Children (Lida births, father "petty bourgeois from Dvoretz") `[C]` EV-19–21: **Ginda** b. 29 Jun 1907, **Khaim Leyb** b. 3 Feb 1909, **Avraam** b. 10 Feb 1913.
- One of the "older brothers" (memoir: likely *uncles*) who went to America ~1895 with 15-yr-old Israel `tania-project (§5); Tanya-summary, p. 3`.

### B04 · Israel "Isrol Leibovich" Mostkoff (Israel Moskov/Moskov)
- b. **1880, shtetl of Ostrov** `tania-project (§§4, 35); MOSTKOFF, p. 1` — Narrative, p. 5 has "1878" — **CF-01** (memoir states 1880 twice; leaning 1880).
- To Mississippi ~1895, age 15, with "elder brothers"/uncles — peddlers, haberdashery `tania-project (§5)`; identities open `[?]` Narrative, p. 11.
- Hid in fire ruins (probably from conscription); stomach ulcer from hunger `tania-project (§4)`. Returned to Slutsk 1905–08 `tania-project (§34)`; m. **Shifra Boruchovich** (C06) ~1907–08 (he ~25, she ~27) `[L]` Narrative, p. 17; Tanya-summary, p. 3 ("family created about 1908/09").
- Description: "a handsome man arrived from America, with a mustache, curly-haired, red-headed… honest and respectable… stayed faithful to her all his life" `tania-project (§33)`.
- Family lived on **Sadovaya Street**, Slutsk (Wolfson's courtyard, near the new synagogue, ~20–40 m from the Sluch river) `tania-project (§§2–3); Tanya-summary, p. 1`; haberdashery shop (Shifra's dowry) burned in the revolution `tania-project (§4)`.
- Left Slutsk Dec 1924/1925 (the cart down Proletarskaya St., all six in the cart, Dorochka 4–5; several other men riding to Mexico) `tania-project (§28)`; Mexico entry 1924 per immigration card & ship record `[C]` EV-02/03 — **CF-03**.
- d. Mexico City — death cert: **1 Oct 1957** `[C]` EV-13; memoir: **1956** `tania-project (§35); MOSTKOFF, p. 1` — **CF-02**. Buried Panteon Israelita; headstone "Israel son of Aryeh Leib" `[C]` EV-15.

### B05 · Eiser "Isodoro/Isadore" Mostkoff (Eizer; Isidore)
- Son of B01/B02; the memoir's "youngest son Eizer" `tania-project (§4)` (but see CF-09).
- b. 1888 — 17 Sep (Narrative, p. 5) vs. **12 Oct** per Petition for Naturalization `[C]` (Narrative, p. 11) — **CF-04**; born **Dvoretz** per petition.
- Emigrated 1905 per petition; Mississippi fur trade: "Skeeter's step-grandfather, **Isadore Mostkoff**, bought and sold furs… traveled along the Mississippi and up the Arkansas River to buy pelts" (Rosedale, Bolivar County) `[C blog]` EV-22 — identification likely but timing loose (CF-14).
- m. **Annie Frank** Narrative, p. 5. Daughter **Louise Mostkoff** (B23) `[L]` EV-22.
- Buried **Beth Israel Cemetery, Clarksdale, Mississippi** `[C]` Narrative, p. 21.

### B06 · Hinde "Ginde/Ginda" Mostkoff
- Dau. of B01/B02 `tania-project (§4)` ("the daughter Ginde" — one translation "Hinde"; Ginda is also the name of B03's dau., a cross-branch collision).
- m. ______ Charches — "possibly Kharakh?" `[?]` Narrative, p. 5. If Kharakh: relation to Faivel Kharakh (C08) unestablished `[?]`.

### B07 · Keili "Clara?" Mostkoff (Iskiwitz/Iscovitch/Iskawitz)
- Dau. of B01/B02; the Memphis line: "descended from Leon's sister, Keili's marriage to Israel Iskiwitz… Their son Israel married a Dora Bernstein" (family correspondence) `[L]` Notes, p. 12; Narrative, p. 5 has "**Reuben** Iscovitch" — **CF-12**.
- Possibly the midwife "Keilya (Clara) or maybe Rosa" at Mikhail's 1917 birth `[?]` Tanya-summary, p. 1.
- Grandson **Israel Iskiwitz** m. **Dora Bernstein** `[L]` Notes, p. 12; burials at Baron Hirsch Cemetery, Memphis `[C]` EV-23.

### B08 · Taiba/Tayba Mostkoff (Tsukovich?)
- "Eldest daughter" of B01/B02 `tania-project (§4)`.
- Her son **Israel/Isrol Tsukovich** (B25) — "Papa's nephew… son of the eldest sister" `tania-project (§8)`; so m. a Mr. Tsukovich `[L]`.
- NB: shares her name with her grandniece Tania (B11) — do not conflate.

### B09 · Lyubka Mostkoff — Israel's sister (CF-07 resolved)
- "In Slutsk lived my father with his family…, **his sister Lyubka** — mother of Bronya and Grisha, from Leningrad" `tania-project (§34)`; MOSTKOFF, p. 1. (The Narrative's "elder sister of *Leibe*" was a misreading; the memoir is explicit.)
- Children: **Bronya** (X12) and **Grisha**, Leningrad `tania-project (§34)`.

### B10 · Abram "Abraham/Avram" Mostkoff
- S. Israel & Shifra; b. **April 1909** `tania-project (§35)`; Tanya-summary, p. 1 (~1908/09).
- Finished seven grades in Slutsk; never studied in Mexico — helped Papa `tania-project (§35)`.
- Sent for ~1926 ("about a year" after Israel's 1925 departure) `tania-project (§28)`; Mexico immigration card 1926 `[C]` EV-03; "the late **Avram**" in Dora's obit `[C]` EV-34.
- **Married twice**: first wife two children (**Nokhem and Pesya**), second wife three more children `tania-project (§35)` — vs. the obit-based structure (wives Clara Nudelman then Leonor Esquinazzi; son Ignacio) — **CF-20**.
- Known wives: **Clara Nudelman**, later **Leonor Esquinazzi** Narrative, p. 12 — **Leonor confirmed by Prensa** ("Abraham y Leonor Mostkoff" as tíos at the 1959 wedding; "(Hijo y nuera)" in Shifra's 1962 obit) `[C]` EV-59/68.
- Grandchildren named in Shifra's 1962 obit `[C]` EV-68: **Nachman** Mostkoff (listed separately) and **Rubén, Motele y Violeta Mostkoff**; great-granddaughter **Alicia Nudelman** (US, m. Richard) — feeds CF-20 (how do these map onto Ignacio (B22, d. 2013, children Moises/Luba/Clara, sister Alicia)? Note Alicia appears in both records — cf. EV-24).
- Appears with Leonor at José's 1959 wedding and Alberto Mostkoff's 1959 obit `[C]` EV-59/69.

### B11 · Tania "Tayba/Tanya/Tatyana (Татьяна)" Mostkova, later Baskin
- Dau. of Israel & Shifra; b. **June 1911**, Slutsk `tania-project (§35)`; fire memory "7 or 8 years" before/after the revolution → ~1911/12 `Tanya-summary, p. 1`; formally Tatyana (Taiba) **Izrailevna** Mostkova `Tanya-summary, p. 1`.
- Memoir written 1976–80; full text at tania-project.com (EV-40). "The late **Tanya** Mostkoff" in Dora's obit `[C]` EV-34.
- School in Slutsk (2nd grade under Aunt Malka; club; Bund milieu); joined the **Bund** ~1926 (~15) Narrative, p. 14.
- Left for **Moscow 1926** (photo caption; §31), lived first with Aunt Enta (Yenta Movshevna, X16) at Bolshaya Pirogovskaya 2a `tania-project (§§31, 36)`; Moscow 1926–30/31 `tania-project (§36 header)`.
- Stayed in the USSR when mother + siblings left Nov 1928 (~17) Narrative, p. 15.
- m. **Iosif/Iosef Baskin**; Birobidzhan by 1935 (typhoid in Khabarovsk hospital 1933); dau. **Nyusenka** b. ~1934/35 at Aunt Malka's in Vitebsk; **three children** in all (1943 famine note); a **Klara** who studied in Leningrad is likely a daughter `[L]` `tania-project (§§16, 31, 33)`.
- 1932: visited grandfather Nakhman in Vitebsk "with Papa (Iosif) from Birobidzhan" `tania-project (§32)`.
- Later Velikiye Luki `tania-project (§33)`.

### B12 · Aryeh Leib "Leiba/Luis" Mostkoff
- S. Israel & Shifra; b. **August 1914** `tania-project (§35)`; headstone "Areyh Leib, son of Israel" `[C]` Narrative, p. 6; "the late **Luis**" in Dora's obit `[C]` EV-34; nicknamed "the potato-eater" as a child `tania-project (§8)`.
- Arrived Mexico Jan 1929 with mother, Miguel, Dora Narrative, pp. 15, 18, 20; finished school in Mexico `tania-project (§35)`.
- m. **Maria Consuelo "Chelo" Linares Lopez** (B15); civil marriage license 23 Dec 1939; ketuba dated Kislev (year illegible) Narrative, p. 20.
- Six children `[C family data]` Narrative, pp. 20–21; the memoir knows them as "Lucy, Shifra, Pesya, Moises, Lazaro, Ida" `tania-project (§35)` — Jewish vs. civil names, mapping partly uncertain (**CF-23**).
- TM's "child Lyova born 1914" (Narrative, p. 6) is Luis himself `[L]` (CF-08).

### B13 · Mikhail "Mikhl/Miguel/Miquel" Mostkoff
- S. Israel & Shifra; b. **November 1917** `tania-project (§35)`; "the late **Miquel**" in Dora's obit `[C]` EV-34; to Mexico Jan 1929; m. **Berta "Busi" Tolmatsky** Narrative, p. 12 — confirmed "Miguel y Bertha Mostkoff" throughout the Prensa `[C]` EV-59/68/69.
- Berta's parents: **David Tolmatsky (X19)** & **Busi Tolmatsky (X20)** `[C]` EV-68/69/78.
- Children per memoir: son **Alberto** (d. at 13 of Botkin's disease) and dau. **Silvia** (b. 1956) `tania-project (§35)` — **Alberto's obituary (EV-69)**: d. Saturday **16 May 1959, age 14** (so b. ~1945, not "at 13"), 3rd-year student (Yavne school), buried 17 May; grandmother Shifre + grandfather David Tolmatsky named. Silvia: "Silvita"/"Silvia" in 1959–62 notices `[C]`; a granddaughter **"Ydele"** appears once beside Silvita (EV-78) — unattested elsewhere (d. young? misprint?) `[?]`. A **Furszyfer cousinhood** is implied by "José Furszyfer y fam. (Primos)" at Alberto's obit (EV-69) and the Mostkoff brothers greeting Silvia Furszyfer's 1966 wedding (EV-77) — link unresolved `[?]`.

### B14 · Dvoira "Dveyra/Dora/Doris" Mostkoff (Glassman; Padawer)
- Dau. Israel & Shifra; b. **August 1921**, "the year of famine" `tania-project (§35)` — **CF-05 resolved** (obit's "83" is off by ~1; Narrative's "1922" wrong).
- Named for her cousin Dveira-Dora (B26), who died of dysentery shortly before her birth `[L]` `tania-project (§7)`.
- To Mexico Jan 1929 with mother; later St. Louis. m. **David Glassman**, later **Lawrence Padawer**; children Jerry (Patty), Mel (Linda), Paul (Debbie) Padawer `[C]` EV-34.
- Obit names exactly the siblings "the late Avram, Luis, Miquel and Tanya Mostkoff" `[C]` EV-34.
- NB: distinct from **Doris Rhea Arst Mostkoff** (X11 Harold's wife, Baton Rouge).

### B15 · Maria Consuelo "Chelo" Linares Lopez
- b. 7 Aug 1917, Mexico, dau. of **Leobardo Linares** (X06) & **Petra Lopez Fuentes** (X07) `[C "Linares/Lopez data sheet"]` Narrative, p. 20; "a Mexican woman, Chelo" `tania-project (§35)`.
- m. Luis Mostkoff (B12) — license 23 Dec 1939 Narrative, p. 20.
- **"Chelo" is an apodo, not her name** — her name is **Consuelo** `[C — Philip, 2026-10-18]`. The Prensa used all three of her names across four notices: **Sara** (Hebrew) at Ana's 1959 wedding (EV-59), **Chelo** — the apodo itself, printed once — in Alberto Mostkoff's 1959 obit (EV-69), **Consuelo** (civil) at Philip's 1961 bris (EV-60), **Sarita** at Shifra's 1962 obit (EV-68).

### B16–B21 · Children of Luis & Chelo `[C family data]` Narrative, pp. 20–21
- The six children (civil names): **Lucy, Ana, Moises, Pola, Isidoro, Aida** — corrected spelling & frame per Philip `[C — 2026-10-13]`: the Prensa Israelita reports their **Hebrew names**, which differ from the civil names; **Luis never had a daughter named Shifra** (the memoir's list errs there — CF-23).
- **B16 Lucy** b. 10 Mar 1939 — born ~9 months *before* the civil marriage license (23 Dec 1939): religious marriage earlier? `[?]` (CF-06). **m. Harry Pepper, Memphis** — "Harry y Lucy Pepper (Nietos, Memphis)" in Shifra's 1962 obit `[C]` EV-68; this anchors the Memphis Lucy of the Notes' obit cluster (**CF-15 leaning resolved**: the "Lucy Secher" reading remains unexplained — possibly a first marriage or a garble — but Lucy Mostkoff of Memphis is now documented).
- **B17 Ana** (Prensa: "**Anita**") b. 29 Dec 1940 — m. **Joseph Borenstein** 15 Mar 1959 `[C]` EV-59 (the paper prints her as "Anita Mostkoff," a profesora); children **Philip (Felipe)**, **Edna/Jaye**, and **Shifra Borenstein** `[C — Philip, 2026-10-13]` (living; names only). Dau. **Shifra** was named after Ana's grandmother **Shifra Boruchovich** (C06) `[C — Philip, 2026-10-13]`. **Names in sequence** `[C — Philip, 2026-10-19]`: **Ana Mostkoff Linares** (birth) → **Ana Borenstein Mostkoff** / **Ana Borenstein** (married name, Mexican convention) → **Ana Caddess**: m. 2) **Hugh N. Caddess**, **2 Jan 1982**. The 1959 marriage ended in **divorce, 1978** `[C — Philip, 2026-10-19]`.
- **B18 Moises** b. 13 Jan 1942 (Prensa "Moishe/Moises" ✓ EV-59/60).
- **B19 Pola** (Prensa Hebrew name "**Pesele**" ✓ EV-59 — CF-23) b. 13 Apr 1946 — **m. Jaime Bierzwinski 18 Dec 1965**, Templo Rab Yehuda Halevi, Mexico City `[C]` EV-70; "connect with your sister Pola" (Philip, `[C]` Notes, p. 12).
- **B20 Isidoro** (earlier extracted as "Isodoro"; memoir: "Lazaro"?) b. 26 Mar 1950 (Prensa "Isidoro" ✓ EV-60).
- **B21 Aida** (Prensa Hebrew name "**Hinde**" ✓ EV-59 — CF-23; memoir: "Ida"?) b. 31 Mar 1957.
- Hebrew vs. civil names (**CF-23 resolved 2026-10-14**): the Prensa prints Hebrew names — **Pesele=Pola, Hinde=Aida, Anita=Ana, Sara/Sarita=Consuelo (apodo "Chelo" — see B15)** — and the memoir's list ("Lucy, Shifra, Pesya, Moises, Lazaro, Ida") maps as Lucy=Lucy, Pesya=Pola, Moises=Moises, Ida=Aida, Lazaro=Isidoro `[L]`; its "Shifra" remains an error (no such daughter).

### B22 · Ignacio Mostkoff Nudelman
- S. Abram (B10) & Clara Nudelman `[L — surname]`; b. ~1938 (75 at death) `[L]`; d. 15 Mar 2013, Mexico City; buried Panteón Anexo 1 `[C]` EV-24.
- Widow **Bella Mostkoff**; children Moises, Luba, Clara Mostkoff; sister Alicia Mostkoff `[C]` EV-24.
- Tension with the memoir's "Nokhem and Pesya + three more" structure for Abram's children — **CF-20** (now fed by the 1962 obit's grandchildren: Nachman, Rubén, Motele, Violeta — EV-68).

### B23 · Louise Mostkoff
- Dau. of Isadore Mostkoff (B05) `[L]`; ran the family clothing store in Rosedale, MS with her half-nephew Skeeter Michael `[C blog]` EV-22.

### B24 · Etl Mostkoff (Reznik) — sister of Israel
- "…and, at a summer place in Urechye near Slutsk, **another sister, Etl** — mother of Musya and Anya Reznik" `tania-project (§34)`; "my Aunt Etl (mother of Reznik's Masha and Anya) at Urechye station, 20–30 km from us" `tania-project (§36)` (Masha/Musya spelling varies).
- m. **Samuil Reznik** — worked at Urechye railway station in charge of fuel supplies; big official wooden house `tania-project (§34); MOSTKOFF, p. 1`. "We loved our Aunt Etl of Urechye very much."
- Children: **Masha/Musya** and **Anya** Reznik `tania-project (§34)`.

### B25 · Israel/Isrol Tsukovich
- "Papa's nephew — already a young man of 17 or 18, **Israel Tsukovich, son of the eldest sister**" — present at the stove scene (~1920/21, when the family had four children with a fifth coming) `tania-project (§8)`; identified elsewhere as "I think Isrol Tsukovich" `tania-project (§23)`.
- b. ~1902–04 `[L — scene arithmetic]`; son of Taiba (B08) `[L]`.

### B26 · Dveira-Dora (Mostkova?) — Israel's niece
- "A girl named Dveyra-Dora… **my father's niece**… perhaps she was left an orphan… She died of dysentery" when Tania was 10 (~1921) `tania-project (§7); MOSTKOFF, p. 2; Tanya-summary, p. 5`.
- Her death shortly before Aug 1921: the newborn Dora (B14) was presumably named for her `[L]`.
- Parent unknown — dau. of one of Israel's siblings `[?]`.
- Wendy floated pinkas #353 — **Dvora (dau. Avraham-Yitskhak Baienov Halevy), wife of Y' Leib Milkes, d. 16 Jun 1921** — as this niece `chronicle, p. 2` `[?]`; unlikely: a married woman vs. the orphaned girl of the memoir, but the date fits — kept as a long-shot candidate (EV-45).

## Line C — Polak / Borukovich (Minsk/Slutsk, Belarus)

*(Founded pass 1; completed pass 3 (memoir §§32–35) — the fullest account of this line. Pass 4 adds the Genealogy draft's Polak tree.)*

### C01 · Y' Mikhal Polak
- Father of Pesheh (C02), Ary Leib (C04), Tsieta (C05) per their pinkas burial records `[C]` EV-05/25/26; wife/mother unknown `[?]`. The draft puts his birth "about 1838 in Minsk" `[L]` Genealogy draft, p. 5 ("Y'" = honorific or a Hebrew name — Yisrael/Yehuda — unresolved).
- "There had been rich people named Polyak… who probably fled to Moscow, Leningrad, or even abroad" `tania-project (§3)`.
- **Fourth child confirmed (2026-10-13): Y' Leib Polak**, d. by Feb 1895 — "rests by rabbi mh"r r' Y' LEIB, the son of Y' MIKHAI. POLAK, in row five" `Pinkas, p. 620 (entry #4379)` — same row as his brother Ary Leib (C04). Children of C01 now: Pesheh, Ary Leib, Tsieta, Y' Leib `[C]`.
- Candidate: **Mikhel Polak b. 13 Jun 1847 Minsk** (father Dovid) `[C record / ? identification]` EV-28 — note the tension with "~1838" `[?]`; brother-candidate **Moshek Polak b. 11 Oct 1852** (X14) EV-29.
- Many *other* Slutsk pinkas Polaks exist (Tsvi-Hirsh s. Yacov-Moshe d. 1924; Avraham s. Zev-Volf, bachelor 15, d. 1922; Rakhel-Galdeh wife of Yakov Polak d. 1920; Yosef Polak d. 1912; Yosef Meir Polak d. 1898; Nenkeh dau. of Binyamin d. 1894; Leah Miryam wife of Tsvi Melamed Polak d. 1903; Feiga wife of Polak Melamed d. 1866) `[C pinkas / ? relation]` EV-45 — relations, if any, unknown. Same for the Slutsk **Berkovits "melamed" family** (Yehuda-Leib s. Chaim-Mosheh d. 1921; wife Khaya Bat-Sheva d. 1920) — EV-45 — possibly the family of the pinkas-#1120 "Yosef Halevy Berkovits" (see CF-13).

### C02 · Pesheh "Pesya" Polak (Pessia; Polyak)
- Dau. of Y' Mikhal Polak, of "a rich but impoverished Polyak family"; husband's household was "well-off… a young man from Ostrov" `tania-project (§33)`.
- m. **Avraham Nakhman Borukovich** (C03) `[C]` EV-05; "married a poor but very cultured and learned man… a good manager of affairs" `tania-project (§3)` — note the two characterizations (well-off vs poor) `[?]`.
- Left a fabric/textile shop as inheritance; ran it only briefly (poor health) `tania-project (§4); Tanya-summary, p. 4`.
- **11 children, only 4 grew to adulthood** (Shifra, Malka, Mikhail, + the navy brother X17); 7 died young of illnesses; "the rest were spoken of in whispers" `tania-project (§§4, 33)`.
- d. **1 Apr 1922** (3 Nisan), Slutsk, buried row 27 `[C]` EV-05 — vs. memoir "died of kidney disease when I was about 6 or 7… 'has the river broken up yet?… Then I'll die soon'" (spring; ~1918) — **CF-22** (pinkas likely right; April 1922 *is* river-breakup time, and Tania's age memory is off).
- NB: the Narrative's "Chaya d. ~1917–18 of kidney disease" is this same memory misattributed to the *other* grandmother — see B02/CF-22.

### C03 · Avraham Nakhman Borukovich (Nachman/Boruchovitch; "Nakhamani Korukhilmai" in one garbled translation)
- Husband of Pesya; father of Shifra (C06) `[L]` Narrative, p. 10; 1925 photo with Tania `[C]` Narrative, p. 9.
- Cheder and yeshiva educated (with his brother) `Tanya-summary, p. 3`. Cultured, refined, even-tempered, clever; "tall, slender, dark, with strong bones… He called me 'daughter'" `tania-project (§33)`; the chronicle's translation adds **hunchbacked** and: "respected by all in business circles and in the synagogue. They trusted grandfather, went for advice, went to borrow and borrowed themselves" `chronicle, p. 3`.
- **Furs and agricultural raw-materials specialist** — assessed skins, "never lying… his word was law"; from the 1920s hired by Soviet customs as a specialist at 25 rubles/month, trade-union member `Tanya-summary, p. 4`; mushrooms drying in his apartment `Tanya-summary, p. 4`. Lived on the outskirts of **Ostrov** near Slutsk `Tanya-summary, p. 3`.
- **Alive in 1932**: "Grandfather moved to live with her [Malka] in Vitebsk, and I saw him one more time, in 1932, when I first came with Papa (Iosif) from Birobidzhan" `tania-project (§32)` → the pinkas #1120 death (21 Jan 1918, Slutsk) attributed to him **cannot be his** — **CF-13** (that Avraham Berkovits is another man; drop the 1918 death).
- Death: after 1932, place unknown (Vitebsk?) `[?]`.
- Register note: an unrelated "AVRAHAM s. Yehuda **BORUKHOVITS OSTREVER**" d. 28 Dec 1904 shows Ostrov-linked Borukhoviches beyond Nakhman's family `[C / ? relation]` `Pinkas, p. 430 (entry #2989)`; on the multiplicity of Slutsk Berkovits families see CF-13 (EV-55).

### C04 · Ary Leib Polak
- S. Y' Mikhal Polak; d. 13 Jan 1895 (17 Tevet), Slutsk — pinkas: "the rabbi… r' ARY' LEIB… the 'melamed' of 'talmud tora'"; buried one grave from Aharon (d. 14 Feb 1894), row 5, town side `[C]` EV-25.

### C05 · Tsieta Polak (Basin)
- Dau. Y' Mikhal Polak; wife of **Kalman Osher Basin** (C10); d. 31 Mar 1912 (13 Nisan), Slutsk — "important venerable woman"; buried one grave from Mrs. Dvora (d. 25 Dec 1911), row 1 `[C]` EV-26.
- Probable children: **Mendel and Sora Basin** `[?]` Genealogy draft, p. 5 (basis unstated — likely burial adjacency).

### C06 · Shifra/Chifra/Sofia Boruchovich (Mostkoff)
- Dau. of Nachman & Pesheh; eldest and favorite daughter `tania-project (§4)`; confirmed by Vsia Rossiia 1911 ("Mastkov, Shifra **Nakhman**[ovna], textiles, Slutsk") `[C]` EV-04.
- b. **1880, Slutsk** `tania-project (§35)` — vs. passport "Bobruisk" (**CF-11**, leaning Slutsk); "27 when engaged" ~1907 Narrative, p. 17.
- As a bride, saved the family's skins from a night fire (jumped up in one nightgown, threw all the goods out the window) `tania-project (§6)`. Smart, businesslike; mutual-aid work; "close to the Bund" though not a member `tania-project (§6)`.
- First love, "some simple young man" (a shoemaker), not allowed ("did not permit marrying below one's class"); then matched with the red-haired returnee from America `tania-project (§§6, 33)`. Dowry: the haberdashery shop `tania-project (§7)`.
- Seamstress in Slutsk `[C]` EV-04.
- Left Slutsk end Nov 1928; entered Mexico Jan 1929 `[C]` EV-03.
- Namesake: her great-granddaughter **Shifra Borenstein** (dau. of Joseph Borenstein & Ana Mostkoff Linares), named after her `[C — Philip, 2026-10-13]`.
- d. 1962 Mexico City — death cert **26 Sep 1962** `[C]` EV-14 vs. obituary **"Sofía Mostkoff… Monday 24 Sep 1962, aged 85, buried 25 Sep"** `[C]` EV-68 vs. memoir "**August 1962**" `tania-project (§35)` — **CF-21** (leaning: died 24 Sep, registered 26; obit age → b. ~1877 vs memoir 1880, **CF-31**); buried beside Israel, Panteon Israelita; earlier obituary image "Sofia/Chifra Boruchovitz" (Narrative, p. 25).
- Her 1962 obituary (EV-68) names the full surviving family: all four children with spouses; grandchildren Jerry Melwyn & Paul Padawer, Nachman, Moisés/Pola/Isidoro/Aida, Silvia, Rubén/Motele/Violeta, Harry & Lucy Pepper; great-grandchildren Alicia & Richard Nudelman, Edna & Fishele Borenstein. The Baskins (USSR) do not appear.

### C07 · Malka Boruchovich (Kharakh; "Malke")
- Dau. of Pesya & Nakhman; Shifra's younger sister `tania-project (§§33, 35)`.
- b. ~1892 `[L]` Genealogy draft, p. 6. Teacher in Slutsk (Tania sat in her 2nd-grade class) `tania-project (§16)`; **Krupskaya Academy, Moscow** (1925; Lenin's-death news-bearer, 22 Jan 1924) `tania-project (§§13, 21)`; education inspector in Bobruisk `tania-project (§30)`.
- Fiancé betrayed her (married her friend); **m. Faivel Kharakh** (C08) — "who loved Malka very much, a good, calm man, but he could not put out the fire of Malka's suffering" `tania-project (§30)`.
- Later Vitebsk (Tania's visits 1932, 1934/35) `tania-project (§§31–32)`; wartime evacuation to Penza, where she met Yakhna's Russian-married daughter `tania-project (§33)`.
- Children: **Misha** and **Polya (Pesya)**; "now their whole family, children and grandchildren, live in the USA and Israel" (1976–80) `tania-project (§35)`.

### C08 · Faivel Kharakh (Harakh/Charach; Fayvl)
- m. Malka; "moved into Grandfather's apartment, to stay with him once I left to study in Moscow" `tania-project (§30)`; theater companion of Tania & Malka `tania-project (§32)`.
- **"Fayvl the Town Sexton"** (Slutsk Yizkor chapter, EV-46): born a sexton — father **Reb Aaron** (Jewish Court of Justice sexton) died young, leaving widow **Esther Frume** with four small children; Fayvl took the position at **14** to feed the family; later head sexton of the Kalter shul; knew Tanach and Ein Yankev; in the 1920s, with the synagogues requisitioned, bought a horse and wagon — hauling loads and selling kegs of water to Soviet restaurants `[C Yizkor excerpt]` Slutsk Links, pp. 3–4. (If Hinde's "Charches" husband (B06) was a Kharakh, he'd be of this family `[?]`.)
- Register note: the only Kharakh in the full pinkas is **Tsileh dau. of Yoseh Hacohen Kharakh of Razoveh** (m. Nadelson), d. 2 Oct 1918 `[C]` `Pinkas, p. 140 (entry #998)`; the sexton dynasty itself (Reb Aaron etc.) does not appear, and the word "sexton" never occurs in the register — relation of the Razoveh Kharakhs to Faivel's family unknown `[?]` (EV-57).

### C09 · Beila Borukovich (Yonas/Jonus)
- d. 4 Feb 1919, suddenly — pinkas: "Mrs. **BEILA** dau. of mh"r r' Avraham Barukhovits, wife of r' **Shlomo Yonus**… new row 3" `[C]` EV-33; Geni profile "Beila Jonas" linked Notes, p. 13.
- Father "Avraham" vs. Pesheh's husband "Nakhman" — same man, double name `[L]` — but note: with Nakhman alive past 1932 (C03), Beila's father may be *another* Avraham Borukovich; her placement as Pesya's daughter is affected by **CF-13** `[?]`.
- Not among the memoir's "four grew to adulthood" — died 1919 (young woman) `tania-project (§33)`.

### C10 · Kalman Osher Basin — husband of Tsieta Polak (C05) `[C]` EV-26; probable children Mendel & Sora `[?]` Genealogy draft, p. 5.
### C11 · Shlomo Yonas (Yonus/Jonas) — husband of Beila (C09) `[C]` EV-33; Geni profile "Beila Jonas" Notes, p. 13.

### C16 · Yosef Polak — grandson of Y' Mikhal (resolved 2026-10-13)
- "Young man" Yosef s. of **Y' Leib Polak**, d. suddenly 27 Jan 1915 (12 Shvat), Slutsk; buried two graves from M' Mendil (d. 24 Jan 1915), row 2, town side `[C]` EV-44; `Pinkas, p. 239 (entry #1676)`.
- His father Y' Leib Polak is **another son of Y' Mikhal** (d. by Feb 1895, buried row 5 beside brother Ary Leib — `Pinkas, p. 620 (entry #4379)`), so Yosef is Y' Mikhal's grandson `[C]`.

### C12 · Mikhail "Meishke/Moise?" Borukhovich
- S. Nakhman & Pesya; the youngest of the four who grew up `tania-project (§33)`; the draft calls him "a/k/a Moise (born about 1916)" `[?]` Genealogy draft, p. 6 — **CF-25** (a 1916 birth is impossible for a medical student marrying in 1925; b. ~1900s per the memoir's arithmetic, as Shifra's younger brother).
- **Medical institute, Leningrad**; end of August (c. 1925) suddenly married **Khaya Pastron** (C13) "without his parents' or anyone's consent… a lively girl who… wasn't right for him (Genya's mother)" `tania-project (§16)`.
- School inspector for the Belorussian Commissariat of Education in Minsk; **suicide (hanged himself with a towel) one winter morning** during Tania's last Slutsk months (~1925/26); "Grandfather's grief knew no bounds" `tania-project (§30)`.
- Brought Tania a drawing album with colored pencils `tania-project (§17)`. Wife and daughter Genya lived in Moscow `tania-project (§30)`.

### C13 · Khaya Pastron (Borukovich)
- m. Mikhail Borukhovich (C12) `tania-project (§16)`; "Genya's mother."
- Moscow — the Pastrons lived by Chistye Prudy; "lived with her newborn, **Esya**, and with **Genya** in one room" `tania-project (§37)` — Esya possibly a second child `[?]`.
- Daughter: **Genya Borukhovich**; Pastron cousins: Samuel and Khaya Pastron `tania-project (§33)`.

### C14 · Yakhna Borukhovich — Nakhman's sister
- "Grandfather's sister living in Slutsk — Aunt Yakhna… an energetic woman who ran a grain shop and managed it well" `tania-project (§32)`.
- **Alive in 1941**: died in the family's collective suicide (see C15) `tania-project (§33)`.
- Another daughter (whom Tania never knew) married a Russian, moved to Penza; Malka's family met her there during wartime evacuation `tania-project (§33)` — name unknown `[?]`.

### C15 · Khaim-Yudl Borukhovich ("Chaim Yudya/Yudl")
- S. of Yakhna (C14) — hence Shifra's first cousin ("my uncle… a cousin of my mother's") `tania-project (§7); Tanya-summary, p. 5`.
- **Pharmacist at Gipchin's pharmacy, Slutsk**; "big and burly — he looked like Malka" `tania-project (§32)`. Old bachelor; married late in life to a Pastron (no longer young; cousin of Samuel & Khaya Pastron — Genya's aunt); three children `tania-project (§33)`.
- **1941, German occupation of Slutsk**: kept working as a specialist; "when he sensed, or perhaps was warned, that an action was being prepared against him, he gave poison to all his household at a meal, and to himself… old Aunt Yakhna, his wife, their three children, and he himself" `tania-project (§33)`.

## X — Unplaced / uncertain affiliation

### X01 · Yitskhak "Isaac" Bunin (Boonin)
- Father of Masha & Nina; brought the girls to relatives in Slutsk after their mother died of TB in Saratov; went to Minsk for goods; bandits overtook the convoy, robbed it, **tied him to a tree and burned him** `tania-project (§3)`.
- Killed 31 Jan 1922 in the Dalhinoveh–Laseh massacre (Pinkas 229) `[C]` EV-07; Narrative, pp. 10, 27; s. of Mendil Bunin (X02) `[C]`.

### X02 · Mendil Bunin (Boonin) — s. of Y' Leib Boonin
- Father of Yitskhak (X01) `[C]` EV-07; m. **Sheina Dvora (Tsiptsin)** (X03) `[C]` EV-08.
- **Full record (2026-10-13)**: "an honest and G-D fearing man mh"r r' M' MENDIL the son of mh"r r' Y' LEIB BOONIN," d. **11 Jan 1915** (25 Tevet) `[C]` `Pinkas, p. 240 (entry #1684)` — confirms the Narrative's "probably died in 1915."
- Children: **Yitskhak** (X01, killed 1922) and **Natan** — "a dear and G-D fearing man… NATAN the son of mh"r r' M' MENDIL BOONIN," d. 22 Jun 1909 `[C]` `Pinkas, p. 340 (entry #2362)`.

### X03 · Sheina Dvora (Tsiptsin) Bunin
- d. 15 Aug 1916, Slutsk (Pinkas 1391) `[C]` EV-08; dau. of Yitskhak Hacohen **Tsiptsin** — "perhaps another idiosyncratic spelling of Sapotnisky??" `[?]` **CF-10**.

### X04 · Masha Bunin/Guitiyk — dau. of Isaac Bunin; several years older than Tania; slept in the girls' room; "stayed with us for good" `tania-project (§3); Tanya-summary, p. 1` `[?]`.
### X05 · Nina Bunin/Guitiyk — same `[?]`. (Tania later looked for "second cousins Manya and Nina (Nekhamka) in Leningrad" `tania-project (§21)` — possibly these girls `[?]`.)

### X06 · Leobardo Linares — father of Chelo (B15) `[C data sheet]` Narrative, p. 20.
### X07 · Petra Lopez Fuentes — mother of Chelo (B15) `[C data sheet]` Narrative, p. 20.

### X08 · Chaim Owzer Mostow — b. 1878; d. 2 Mar 1935 Vilnius `[C]` EV-09; **patronymic Lejb** → candidate sibling of Israel `[?]` Narrative, p. 11.
### X09 · Movshe "Moshe" Mostkov — b. ~1876; d. 12 Jun 1911 Vilnius `[C]` EV-10; **patronymic Leyb** → candidate sibling `[?]` Narrative, p. 11.

### X11 · Harold "Skeeter" Mostkoff
- b. ~1918 (88 at death), native of Rosedale, Miss.; d. 31 Jul 2006, Baton Rouge; founder, Baton Rouge Restaurant Supply; WWII US Army veteran `[C]` EV-38.
- Wife **Doris Rhea (Arst) Mostkoff** (d. 21 Dec 2006); children Anne, Dale `[C]` EV-38. Candidate son of Isadore (B05) `[?]` — no source states the link.

### X12 · Bronya Leybovna Barshay
- Dau. of Lyubka (B09) `[L — memoir]` `tania-project (§34)`; burial record (mitzvatemet #20686) `[C]` Notes, p. 18. Patronymic "Leybovna" (father Leyb) sits oddly with Lyubka-as-mother `[?]`.
- Brother **Grisha**, Leningrad `tania-project (§34)`.

### X13 · Abraham Borenstein (1906–1990) — Ancestry-derived: b. 1906 to Yehuda Leib & Mindla Gitla Borensztein; siblings Szmuel, Fishel + 4 others; m. Sara; d. 1990 `[C Ancestry / ? relevance]` Notes, pp. 10–11. Same family or mis-merge? `[?]`.

### X14 · Moshek Polak — b. 11 Oct 1852 Minsk (father Dovid) `[C]` EV-29; brother of the 1847 Mikhel candidate; relation to C01 unknown `[?]`.

### X15 · Samuel Mostkow (Mostk) — b. 1883 Novogrudok; mother **Khaya Sara Grodzienska**; internal-passport application 29 Jan 1923, Vilnius (Piwna St. 2-33); German passport #35539 issued Vilnius 19 Feb 1916 `[C LitvakSIG]` EV-41; MOSTKOFF, p. 1. Unplaced candidate relative `[?]`.

### X16 · Movsha Borukhovich — likely Nakhman's brother `[L]`
- Memoir: "Grandfather Nakhman and **his brother (Yenta Moiseyevna's father)** studied in a cheder and then in a yeshiva" `Tanya-summary, p. 3`; "Enta Moiseevna was **a cousin of my mother's and Malka's**. She was born and raised in Bobruisk" `tania-project (§33)` → matches **Yenta Movshevna Borukhovich, b. 3 Jan 1888 Bobruysk** (EV-42) `[L correlation]`.
- Wife **Feiga**; children (Bobruysk births, EV-42 `[C]`): **Yenta** (b. 3 Jan 1888), **Iakha** (b. 17 Aug 1884; father registered Slutsk, record taken 1907), **Girsha** (b. 11 Dec 1885; circumciser Galant Khaim).
- Yenta ("Aunt Enta"): Krupskaya Academy, Moscow; Tania lodged with her at Bolshaya Pirogovskaya 2a in 1926; later friends in Velikiye Luki `tania-project (§§31, 33, 36)`.

### X17 · "Navy brother" Borukovich
- Youngest brother of Shifra; "ran away from home without his parents' consent, served in the navy, and never came home" `tania-project (§33)` — likely the 4th of the four who grew to adulthood `[L]`; name unknown `[?]`.

### X18 · David & Lipke ("Uncle David and Aunt Lipke")
- Worked with animal hides; Bolotnaya Street, Slutsk; daughter **Luba** left for Poland — "a beauty (she is Khanele's mother, from New York)" `tania-project (§34)`. Which side of the family — unknown `[?]`.

### X19 · David Tolmatsky — father of Berta (B13's wife)
- "David Tolmatsky (Abuelito)" in Alberto Mostkoff's 1959 obit `[C]` EV-69; "David Tolmatsky (Esposo)" in Busi's obit `[C]` EV-78; mejután in Shifra's 1962 obit `[C]` EV-68; alive 1962, predeceased by Busi.

### X20 · Busi Tolmatsky — mother of Berta
- d. a Sunday in late Dec 1958/early Jan 1959 (day digit illegible in OCR) `[C]` EV-78; "Miguel y Bertha Mostkoff (Hija y yerno)"; granddaughters "Ydele y Silvita" — see B13 for the Ydele question `[?]`.

### X21 · Java Finkler — mother of Rebecca Finkler (A17's wife)
- d. Friday 20 Nov 1959, age 74 (b. ~1885), "de Ucrania" `[C]` EV-71; the mourning families "Finkler, Rubinstein, Lerner y Borenstein"; Dr. Sidney y Rebeca Borenstein chief mourners ⇒ mother of Rebecca `[L]`. A **Jaim Finkler** among Mania's 1969 mourners `[C]` EV-62 — Rebecca's father or brother `[?]`.

*Leads without entries: **Felipe Borenstein's own death notice** (~1959/60, Prensa issue unidentified — only his unveiling is in hand, EV-61); **Frida Borenstein m. Kurt Efter 1960** — a different, unrelated Borenstein family (Moishe y Sara Borenstein; brother Abraham — likely the 1964 groom of Sara Jarovinsky, EV-76) `prensa-hits §7.2`; **Israel Itskovits "from Baborisk"** d. 19 Feb 1922, buried Slutsk row 31 `Pinkas, p. 30 (entry #219)` — a Bobruisk Itskovits (cf. Movsha Borukhovich of Bobruysk, X16; Shifra's passport birthplace) `[?]`; **"Leib Minkov"** in the Mostkoffs' Mexico City community 1959 (EV-79 — Sapotnitsky/Min'kovich lead); **1877 Priluki marriage** Min'kov/Supanitskij (EV-48 — Sapotnitsky-name lead); **Gravestone 17** — Yechiel Michel s. Aryeh, d. 10 Nov 1867, Slutsk (EV-49 — unplaced); **Secher** — the one unexplained name in Lucy's Memphis record (CF-15); **Rebeca Rubinstein de Bornstein** obit 2014 (Notes, p. 15 `[?]`); **Zaturensky family, Nesvizh 1851 revision list** (EV-36); **Herz Bauman** Warsaw cemetery links (Notes, p. 11 — pass 5); **Boruchovich genealogy site** (maloratsky-vinitsky, Notes, p. 18); pinkas **#870 Chaya-Henya Itskovits** (EV-43 — grandmother-Khaya candidate, CF-17); **Dveira Ostrovskaya** (teacher near Minsk — the sweetheart's sister, NOT family `tania-project (§31)`).*
