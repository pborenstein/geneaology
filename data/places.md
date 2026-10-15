# Place Gazetteer — Borenstein/Mostkoff Genealogy

One entry per **distinct place** mentioned in the corpus (people.md, evidence-log.md, pinkas-hits.md, conflicts.md, tania-project memoir incl. its locations table). Built 2026-10-14 (mapping session) per **docs/MAPPING-PLAN.md**. `data/places.geojson` / `data/places.kml` are **generated from this file** (`python3 scripts/places-to-geojson.py`) — edit here, never there.

## Conventions

- **IDs** (stable): `P##`, assigned in corpus order (Belarus cluster → Poland → USSR → USA → Mexico → Spain).
- **Tiers**: Tier 1 = family-connected places (full entries; geocoded where identification is sound). Tier 2 = background/lead toponyms (one-liners at the tail) — pinkas "from X" descriptors of unrelated townsfolk, record leads, transit stops, glancing mentions.
- **Confidence** (DEC-003): `[C]` confirmed/verified · `[L]` likely · `[?]` open question. Never merge two same-named places without corroboration (same rule as people).
- **Citations**: same keys as people.md (`tania-project (§N)`, `Tanya-summary, p. N`, `Narrative, p. N`, `Notes, p. N`, `Pinkas, p. N (entry #M)`, `timeline, p. N`, `EV-##`). `tania-project (locations)` = the memoir site's own places table (`/posts/locations/`, part of EV-40).
- **Coordinate provenance rule**: no coordinate without a source — Wikidata QID (+ GeoNames ID where present), or `tania-project (locations)` for places Wikidata lacks. Unidentified places ship **un-geocoded** (absent from the map, present here).

## Index

| ID | Place | Today | Region | Coords (lat, lon) | Conf. |
|----|-------|-------|--------|-------------------|-------|
| P01 | Slutsk | Slutsk, Belarus | Belarus | 53.0275, 27.5528 | [C] |
| P02 | Ostrov (near Slutsk) | village near Slutsk, Belarus | Belarus | ~53.0, ~27.5 (approx) | [?] |
| P03 | Nesvizh | Niasviž, Belarus | Belarus | 53.2189, 26.6819 | [C] |
| P04 | Urechye | Urecha, Belarus | Belarus | 52.9453, 27.8983 | [L] |
| P05 | Lida | Lida, Belarus | Belarus | 53.8956, 25.2958 | [C] |
| P06 | Dvoretz | Dvarets, Belarus | Belarus | 53.4069, 25.5697 | [L] |
| P07 | Radun | Raduń, Belarus | Belarus | 54.0531, 24.9978 | [C] |
| P08 | Minsk | Minsk, Belarus | Belarus | 53.9022, 27.5618 | [C] |
| P09 | Bobruisk | Babruysk, Belarus | Belarus | 53.15, 29.2333 | [C] |
| P10 | Vitebsk | Vitebsk, Belarus | Belarus | 55.1833, 30.1667 | [C] |
| P11 | Vilnius | Vilnius, Lithuania | Lithuania | 54.6872, 25.28 | [C] |
| P12 | Novogrudok | Navahrudak, Belarus | Belarus | 53.5992, 25.8256 | [C] |
| P13 | Dalhinoveh | Daŭhinava, Belarus | Belarus | 54.6453, 27.4772 | [L] |
| P14 | Braslaw | Braslaw, Belarus | Belarus | 55.6417, 27.0333 | [L] |
| P15 | Oreitsa | unidentified | Belarus | — | [?] |
| P16 | Laseh | unidentified | Belarus | — | [?] |
| P17 | Ozdeh | unidentified | Belarus | — | [?] |
| P18 | Kurow | Kurów, Poland | Poland | 51.3894, 22.185 | [C] |
| P19 | Warsaw | Warsaw, Poland | Poland | 52.23, 21.0111 | [C] |
| P20 | Bialystok | Białystok, Poland | Poland | 53.1324, 23.1687 | [C] |
| P21 | Moscow | Moscow, Russia | Russia | 55.7506, 37.6175 | [C] |
| P22 | Leningrad | Saint Petersburg, Russia | Russia | 59.95, 30.3167 | [C] |
| P23 | Saratov | Saratov, Russia | Russia | 51.53, 46.035 | [C] |
| P24 | Penza | Penza, Russia | Russia | 53.2, 45.0 | [C] |
| P25 | Velikiye Luki | Velikiye Luki, Russia | Russia | 56.35, 30.5167 | [C] |
| P26 | Pronsk district | Pronsky District, Russia | Russia | 54.1172, 39.6133 | [C] |
| P27 | Khabarovsk | Khabarovsk, Russia | Russia | 48.4833, 135.0667 | [C] |
| P28 | Pokrovka | Pokrovka, Russia | Russia | ~48.3, ~135.2 (approx) | [L] |
| P29 | Birobidzhan | Birobidzhan, Russia | Russia | 48.7833, 132.9333 | [C] |
| P30 | Valdheim kolkhoz | Valdgeym, Russia | Russia | ~48.7, ~132.7 (approx) | [L] |
| P31 | Odessa | Odesa, Ukraine | Ukraine | 46.4775, 30.7326 | [C] |
| P32 | Mississippi (peddler circuit) | Mississippi, USA | USA | ~32.7, ~-89.7 (approx) | [L] |
| P33 | Rosedale MS | Rosedale, Mississippi, USA | USA | 33.8536, -91.0269 | [C] |
| P34 | Clarksdale MS | Clarksdale, Mississippi, USA | USA | 34.2006, -90.5702 | [C] |
| P35 | Memphis TN | Memphis, Tennessee, USA | USA | 35.1461, -90.0519 | [C] |
| P36 | St. Louis MO | St. Louis, Missouri, USA | USA | 38.6264, -90.1994 | [C] |
| P37 | Baton Rouge LA | Baton Rouge, Louisiana, USA | USA | 30.4475, -91.1786 | [C] |
| P38 | Las Vegas NV | Las Vegas, Nevada, USA | USA | 36.1672, -115.1486 | [C] |
| P39 | New York | New York City, USA | USA | 40.7128, -74.0061 | [C] |
| P40 | Mexico City | Mexico City, Mexico | Mexico | 19.3538, -99.1359 | [C] |
| P41 | Guadalajara | Guadalajara, Jalisco, Mexico | Mexico | 20.677, -103.347 | [L] |
| P42 | Marbella | Marbella, Spain | Spain | 36.5114, -4.8834 | [C] |

## Tier 1 — family-connected places

### P01 · Slutsk
- **Variants:** Слуцк · Słuck · "Minsk" on Israel's Mexican immigration card (= gubernia) `EV-03`
- **Today:** Slutsk, Minsk Region, Belarus
- **Region:** Belarus
- **Coords:** 53.0275, 27.5528 — Wikidata Q201243 · GeoNames 621741; corroborated `tania-project (locations)`
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Minsk gubernia) → Byelorussian SSR → Belarus (1991)
- **People:** B02 lived with Israel's family (Sadovaya St., corner of the bedroom) `tania-project (§4)`; B04 residence 1905–24, haberdashery shop, left Dec 1924/25 `tania-project (§§4, 28)`; C06 b. 1880, seamstress, res. to Nov 1928 `tania-project (§35)`; `EV-04`; B10 b. 1909, school `tania-project (§35)`; B11 b. Jun 1911, school + Bund `tania-project (§35)`; Narrative, p. 14; B12/B13/B14 b. 1914/17/21 `tania-project (§35)`; B26 d. ~1921 `tania-project (§7)`; C02 d. 1922 `EV-05`; C03 res. (outskirts, at Ostrov) `Tanya-summary, p. 3`; C04 d. 1895 `EV-25`; C05 d. 1912 `EV-26`; C07 2nd-grade teacher `tania-project (§16)`; C08 head sexton of the Kalter shul `Slutsk Links, pp. 3–4`; C09 d. 1919 `EV-33`; C14 grain shop `tania-project (§32)`; C15 pharmacist (Gipchin's), 1941 family suicide `tania-project (§33)`; C16 d. 1915 `EV-44`; X01 buried 5 Feb 1922, martyrs' row `EV-06`; X02 d. 1915 `EV-52`; X03 d. 1916 `EV-07`; X04/X05 grew up in the Mostkoff home `tania-project (§3)`; X18 Bolotnaya St. hides workshop `tania-project (§34)`
- **Notes:** The corpus's center of gravity; the whole pinkas (EV-50) is the Slutsk Chevra Kadisha register. Micro-locations (kept here, not separate points): **Sadovaya Street** (Wolfson's courtyard, near the new synagogue, ~20–40 m from the Sluch river) `tania-project (§§2–3)`; **Proletarskaya Street** (the 1924 departure cart) `tania-project (§28)`; the **Sluch river**; the Kalter shul; Gipchin's pharmacy.

### P02 · Ostrov (near Slutsk)
- **Variants:** Остров · "the shtetl of Ostrov" `tania-project (§§4, 35)` · "Ostrever" epithet in the pinkas `Pinkas, p. 430 (entry #2989)`
- **Today:** village/outskirts near Slutsk, Minsk Region, Belarus — exact settlement unidentified
- **Region:** Belarus
- **Coords:** 53.0, 27.5 — `tania-project (locations)`, approximate
- **Confidence:** [?]
- **Jurisdictions:** as Slutsk
- **People:** B04 b. 1880 "in the shtetl of Ostrov" `tania-project (§§4, 35)`; `MOSTKOFF, p. 1`; C03 + C02 lived on the outskirts of Ostrov near Slutsk `Tanya-summary, p. 3`
- **Notes:** **Disambiguation:** this is *not* Ostrów Mazowiecka or any Polish Ostrov — the corpus itself fixes it next to Slutsk ("Lived on the outskirts of Ostrov near Slutsk"; a Slutsk-pinkas Borukhovich is "Ostrever"). Wikidata has no Ostrov in Slutsk raion; the memoir site marks it approximate. Pin down via JewishGen Gazetteer / 19th-c. lists when possible.

### P03 · Nesvizh
- **Variants:** Нясвіж / Несвиж · Nieśwież · Niasviž · "Neswalok" (older mistranslation)
- **Today:** Niasviž, Minsk Region, Belarus
- **Region:** Belarus
- **Coords:** 53.2189, 26.6819 — Wikidata Q201230 · GeoNames 624700; corroborated `tania-project (locations)` 53.22/26.69
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Minsk gubernia) → Poland 1921–39 (Riga border ran just west of town — why the memoir says "near the Polish border") → Byelorussian SSR → Belarus
- **People:** B02 Chaya — natal village region ("lived her whole life in a distant village near the Polish border, near Nesvizh"); presumably died/buried there (CF-17 strong negative: not in the Slutsk register) `tania-project (§4)`; Zaturensky revision-list lead (EV-36, EV-10)
- **Notes:** The natal *village* itself is unidentified — a place to search (Nesvizh-area revision lists). See `docs/investigations/sapotnitsky.md`.

### P04 · Urechye
- **Variants:** Уречье · Urecha · Urechcha · "Urechye station"
- **Today:** Urecha, Lyuban district, Minsk Region, Belarus
- **Region:** Belarus
- **Coords:** 52.9453, 27.8983 — Wikidata Q1169315 · GeoNames 620558
- **Confidence:** [L]
- **Jurisdictions:** Russian Empire (Minsk gubernia) → Byelorussian SSR → Belarus
- **People:** B24 Etl (Israel's sister) + Samuil Reznik — summer home at Urechye station (Samuil in charge of fuel supplies; big official wooden house); children Masha/Musya & Anya `tania-project (§§34, 36)`; `MOSTKOFF, p. 1`
- **Notes:** "20–30 km from us" `tania-project (§36)` — Q1169315 is ~25 km SSE of Slutsk, fits. **Discrepancy:** `tania-project (locations)` places Urechye ~53.13/27.85 and calls it Slutsk district; Wikidata has it in Lyuban district at 52.945/27.898. Wikidata coordinates used; reconcile against a period map.

### P05 · Lida
- **Variants:** Ліда · Lida
- **Today:** Lida, Grodno Region, Belarus
- **Region:** Belarus
- **Coords:** 53.8956, 25.2958 — Wikidata Q241475 · GeoNames 626081
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Vilna gubernia, Lida uyezd) → Poland 1920–39 → Byelorussian SSR → Belarus
- **People:** B03 m. Dvora Portnoy 30 May 1906 `EV-01`; children Ginda b. 1907, Khaim Leyb b. 1909, Avraam b. 1913 `EV-19–21`
- **Notes:** The marriage/birth records say "of Dvoretz" (see P06) — Lida is the registry town.

### P06 · Dvoretz
- **Variants:** Дворец · Dvorets · Dvarec
- **Today:** Dvarets, Dziatlava district, Grodno Region, Belarus
- **Region:** Belarus
- **Coords:** 53.4069, 25.5697 — Wikidata Q3918885 · GeoNames 628692
- **Confidence:** [L]
- **Jurisdictions:** Russian Empire → Poland 1920–39 (Nowogródek voivodeship) → Byelorussian SSR → Belarus
- **People:** B03 "of Dvoretz" (petty bourgeois) `EV-01`; B05 b. Dvoretz per naturalization petition `Narrative, p. 11`
- **Notes:** Several Belarusian Dvoretzes exist; the Lida-uyezd marriage points to the Dziatlava-district Dvorets (former shtetl), but the uyezd attribution deserves a JewishGen check. Variant spellings kept.

### P07 · Radun
- **Variants:** Радунь · Raduń · Radun
- **Today:** Raduń, Voronava district, Grodno Region, Belarus
- **Region:** Belarus
- **Coords:** 54.0531, 24.9978 — Wikidata Q2995176 · GeoNames 622869
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Vilna gubernia, Lida uyezd) → Poland 1920–39 → Byelorussian SSR → Belarus
- **People:** Dvora (Dveyra) Portnoy (B03's bride) "of Radun, dau. of Pinkhus" `EV-01`
- **Notes:** Well-known yeshiva town (the Chofetz Chaim's).

### P08 · Minsk
- **Variants:** Мінск · Minsk
- **Today:** Minsk, Belarus (capital)
- **Region:** Belarus
- **Coords:** 53.9022, 27.5618 — Wikidata Q2280 · GeoNames 625143; corroborated `tania-project (locations)`
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Minsk gubernia seat) → Byelorussian SSR → Belarus
- **People:** B01/B02 candidate civil marriage 1889 `EV-10` (CF-29: cannot be Chaya's own); C01 candidate birth "Mikhel b. 1847" `EV-28` + brother X14 b. 1852 `EV-29`; C03 candidate Nokhim b. 1838 `EV-30`; 1894 town-dwellers list `EV-37`; C12 school inspector (Belorussian Commissariat of Education) `tania-project (§30)`; X01 convoy origin — "ten men from the town of Minsk" `Pinkas, p. 31 (entry #229)`; memoir: the first love's pedagogical college; train transfer `tania-project (locations)`
- **Notes:** C01's rich Polyaks "fled to Moscow, Leningrad, or abroad" `tania-project (§3)`.

### P09 · Bobruisk
- **Variants:** Бабруйск · Bobruysk · Babruysk · "Baborisk" (pinkas #219)
- **Today:** Babruysk, Mogilev Region, Belarus
- **Region:** Belarus
- **Coords:** 53.15, 29.2333 — Wikidata Q207294 · GeoNames 630468
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Minsk gubernia) → Byelorussian SSR → Belarus
- **People:** X16 Movsha Borukhovich family — births of Yenta 1888, Iakha 1884, Girsha 1885 `EV-42`; X16 Enta born & raised `tania-project (§33)`; C06 Shifra's passport birthplace — **CF-11** (leaning Slutsk) `Narrative`; C07 Malka education inspector `tania-project (§30)`
- **Notes:** Pinkas #219 "Israel Itskovitch from Baborisk" d. 1922 `EV-53` — a Bobruisk Itskovits, cf. CF-17/CF-12 threads.

### P10 · Vitebsk
- **Variants:** Віцебск · Vitebsk
- **Today:** Vitebsk, Belarus
- **Region:** Belarus
- **Coords:** 55.1833, 30.1667 — Wikidata Q102217 · GeoNames 620127
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Vitebsk gubernia seat) → Byelorussian SSR → Belarus
- **People:** C07 Malka's family home from ~1930; Tania's visits 1932 & 1934/35 `tania-project (§§30–32)`; C03 Nakhman moved in with Malka by 1932, alive that year, death place unknown (Vitebsk?) `tania-project (§32)`; B11's dau. Nyusenka b. ~1934/35 at Malka's `tania-project (§§16, 31)`

### P11 · Vilnius
- **Variants:** Вильна · Wilno · Vilna · Vilnius
- **Today:** Vilnius, Lithuania (capital)
- **Region:** Lithuania
- **Coords:** 54.6872, 25.28 — Wikidata Q216 · GeoNames 593116
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Vilna gubernia seat) → Poland 1920–39 (Wilno) → Lithuania
- **People:** X08 Chaim Owzer Mostow d. 2 Mar 1935 `EV-08`; X09 Movshe Mostkov d. 12 Jun 1911 `EV-09` (both candidate siblings of Israel, patronymic Leyb/Lejb); X15 Samuel Mostkow passports 1916/1923, Piwna St. 2-33 `EV-41`

### P12 · Novogrudok
- **Variants:** Навагрудак · Nowogródek · Navahrudak
- **Today:** Navahrudak, Grodno Region, Belarus
- **Region:** Belarus
- **Coords:** 53.5992, 25.8256 — Wikidata Q278743 · GeoNames 624785
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Minsk gubernia, Novogrudok uyezd) → Poland 1920–39 → Byelorussian SSR → Belarus
- **People:** X15 Samuel Mostkow b. 1883 (mother Khaya Sara Grodzienska) `EV-41`

### P13 · Dalhinoveh
- **Variants:** Далгінава / Долгиново · Dalhinov · Dalhinove
- **Today:** Daŭhinava (agrotown), Vileika district, Minsk Region, Belarus
- **Region:** Belarus
- **Coords:** 54.6453, 27.4772 — Wikidata Q2029657 · GeoNames 628990 (corroborated by Q30007302 "Dolginovo ghetto", same site)
- **Confidence:** [L]
- **Jurisdictions:** Russian Empire (Vilna gubernia, Vileika uyezd) → Poland 1920–39 → Byelorussian SSR → Belarus
- **People:** X01 Yitskhak Bunin killed there 31 Jan 1922 in the massacre of the Minsk merchants `Pinkas, p. 31 (entry #229)`; `EV-06`; `tania-project (§3)`
- **Notes:** Name is a transliteration off the pinkas translation ("by the village Dalhinoveh not far from the town Laseh"). The Vileika-district Daŭhinava is the known former shtetl on the Minsk–Vileika road — identification likely, not confirmed. See P16 Laseh.

### P14 · Braslaw
- **Variants:** Браслаў · Braslav · Braslaw
- **Today:** Braslaw, Vitebsk Region, Belarus
- **Region:** Belarus
- **Coords:** 55.6417, 27.0333 — Wikidata Q628623 · GeoNames 629640
- **Confidence:** [L]
- **Jurisdictions:** Russian Empire (Vilna gubernia, Braslaw uyezd) → Poland 1920–39 → Byelorussian SSR → Belarus
- **People:** "The author's relatives" killed in the Braslav ghetto, 1942 — memoir foreword, via `tania-project (locations)` — which relatives is not established `[?]`
- **Notes:** Only the foreword names it; not in the memoir body. Kept [L] for the place, [?] for the kinship.

### P15 · Oreitsa
- **Variants:** Oreitsa · Oretesheh · Oreitsa/Oretesheh (one pinkas family, two spellings)
- **Today:** unidentified — presumably near Slutsk
- **Region:** Belarus
- **Coords:** —
- **Confidence:** [?]
- **Jurisdictions:** —
- **People:** Zev Volf Itskovits "tailor from Oreitsa," d. 1914 aged 90 `EV-53`; his widow Chaya-Henya "from Oretesheh" (#870, the CF-17 candidate) `EV-43`
- **Notes:** CF-17 appendix. If identified, would anchor the #870/#1809 family; the Itskovits-Itskovitch spellings also brush B08 (Tsukovich) and B07 (Iskiwitz) — probably coincidence, keep separate.

### P16 · Laseh
- **Variants:** Laseh (as transliterated)
- **Today:** unidentified — "not far from" Dalhinoveh (P13)
- **Region:** Belarus
- **Coords:** —
- **Confidence:** [?]
- **Jurisdictions:** —
- **People:** Site of the 1922 massacre aftermath — two martyrs buried in Laseh `Pinkas, p. 31 (entry #229)`
- **Notes:** Possibly "Łaś"-type small settlement; needs a Russian-original reading of the pinkas.

### P17 · Ozdeh
- **Variants:** Ozdeh (as transliterated)
- **Today:** unidentified
- **Region:** Belarus
- **Coords:** —
- **Confidence:** [?]
- **Jurisdictions:** —
- **People:** The three wounded survivors of the 1922 massacre "escaped to the town Ozdeh" `Pinkas, p. 31 (entry #229)`
- **Notes:** Transliteration off the register; unidentified.

### P18 · Kurow
- **Variants:** Kurów · Kurow · Borensztejns' home town (JRI-Poland spelling "Kurow")
- **Today:** Kurów, Lublin Voivodeship, Poland
- **Region:** Poland
- **Coords:** 51.3894, 22.185 — Wikidata Q2316 · GeoNames 766980
- **Confidence:** [C]
- **Jurisdictions:** Congress Poland / Russian Empire (Lublin gubernia) → Poland (1918–)
- **People:** A01 Szol Kelman m. A02 Sura Brandla 1890, akta 4 `EV-31`; births of A03 Toibe 1894, A04 Mendel 1897, A05 Fiszel 1901 `EV-32`; possible A12–A14 (Chaim 1891, Cyrla 1892, Necha 1895) `timeline, p. 1`
- **Notes:** **Disambiguation:** many Kuróws exist; ours is fixed by the JRI-Poland Fond 1751, **Lublin Archive** holdings (`Notes, p. 17` — Kurow PSA births 1862–98, marriages 1868–1908, deaths 1871–76/82–98/1901–08).

### P19 · Warsaw
- **Variants:** Warszawa · Warsaw
- **Today:** Warsaw, Poland (capital)
- **Region:** Poland
- **Coords:** 52.23, 21.0111 — Wikidata Q270 · GeoNames 756135
- **Confidence:** [C]
- **Jurisdictions:** Congress Poland / Russian Empire (Warsaw gubernia) → Poland (1918–)
- **People:** A02 d. 1925 + gravestone, Warsaw Jewish cemetery `EV-47` (**CF-28**, one timeline line says 1935); A01 possibly d. 1942 Warsaw `[?] timeline, p. 2`; A05 family trip 1934/35 ("showing off Chana's jewels") `[?] timeline, pp. 1–2`; A03's dau. Ana Mitelhaus b. Warsaw per most records (**CF-27**); Herz Bauman gravestone leads `Notes, p. 11`

### P20 · Bialystok
- **Variants:** Białystok · Bialystok
- **Today:** Białystok, Podlaskie Voivodeship, Poland
- **Region:** Poland
- **Coords:** 53.1324, 23.1687 — Wikidata Q761 · GeoNames 776069
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Grodno gubernia) → Poland (1918–)
- **People:** A08 Angela Glatt b. 1923 `timeline, p. 1`

### P21 · Moscow
- **Variants:** Москва · Moskva
- **Today:** Moscow, Russia (capital)
- **Region:** Russia
- **Coords:** 55.7506, 37.6175 — Wikidata Q649 · GeoNames 524894; corroborated `tania-project (locations)`
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire → RSFSR/USSR → Russia
- **People:** B11 lived 1926–30/31 (first with Aunt Enta at Bolshaya Pirogovskaya 2a; Timiryazev college; expulsion & reinstatement; mother's 1930 visit) `tania-project (§§31, 36)`; C07 Malka at the Krupskaya Academy from 1925 `tania-project (§§13, 21)`; X16 Yenta (Enta) at the Krupskaya Academy `tania-project (§33)`; C13 Khaya Pastron + dau. Genya lived by Chistye Prudy `tania-project (§37)`; C12's widow & Genya in Moscow `tania-project (§30)`; B04's emigration train left Moscow 10 Dec 1924 `EV-02`; C01's Polyaks "probably fled to Moscow" `tania-project (§3)`
- **Notes:** Birobidzhan trips 1932+ pass through (see P29).

### P22 · Leningrad
- **Variants:** Ленинград · Saint Petersburg · Sankt-Peterburg (renamed 1991)
- **Today:** Saint Petersburg, Russia
- **Region:** Russia
- **Coords:** 59.95, 30.3167 — Wikidata Q656 · GeoNames 498817
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (imperial capital, Petrograd 1914–24) → RSFSR/USSR (Leningrad) → Russia (Saint Petersburg, 1991)
- **People:** X12 Bronya + Grisha (B09 Lyubka's children) `tania-project (§34)`; C12 Mikhail — medical institute, married Khaya Pastron ~1925 `tania-project (§16)`; a Klara studied there (likely B11's dau.) `[L] tania-project (§33)`; "second cousins Manya and Nina in Leningrad" `tania-project (§21)`; C01's Polyaks "fled to… Leningrad" `tania-project (§3)`

### P23 · Saratov
- **Variants:** Саратов · Saratov
- **Today:** Saratov, Saratov Oblast, Russia
- **Region:** Russia
- **Coords:** 51.53, 46.035 — Wikidata Q5332 · GeoNames 498677
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Saratov gubernia) → RSFSR/USSR → Russia
- **People:** X01's wife (mother of Masha & Nina Bunin) died of TB in Saratov `tania-project (§3)`

### P24 · Penza
- **Variants:** Пенза · Penza
- **Today:** Penza, Penza Oblast, Russia
- **Region:** Russia
- **Coords:** 53.2, 45.0 — Wikidata Q5540 · GeoNames 511565; corroborated `tania-project (locations)`
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Penza gubernia) → RSFSR/USSR → Russia
- **People:** C07 Malka's wartime evacuation; met Yakhna's Russian-married daughter there `tania-project (§33)`; that daughter had earlier settled in Penza `tania-project (§33)`

### P25 · Velikiye Luki
- **Variants:** Великие Луки · Velikiye Luki
- **Today:** Velikiye Luki, Pskov Oblast, Russia
- **Region:** Russia
- **Coords:** 56.35, 30.5167 — Wikidata Q101825 · GeoNames 476077
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Pskov gubernia) → RSFSR/USSR → Russia
- **People:** B11's later home `tania-project (§33)`; X16 Enta's friends there `tania-project (§§33, 36)`

### P26 · Pronsk district
- **Variants:** Пронский район · Pronsky District, Ryazan Oblast
- **Today:** Pronsky District, Ryazan Oblast, Russia
- **Region:** Russia
- **Coords:** 54.1172, 39.6133 — Wikidata Q1644769 · GeoNames 504714
- **Confidence:** [C]
- **Jurisdictions:** RSFSR/USSR → Russia
- **People:** B11 sent for collectivization fieldwork, spring 1929 `tania-project` (via locations table)
- **Notes:** District centroid; `tania-project (locations)` gives ~53.85/39.58 (approximate) — either way, district-level.

### P27 · Khabarovsk
- **Variants:** Хабаровск · Khabarovsk
- **Today:** Khabarovsk, Khabarovsk Krai, Russia
- **Region:** Russia
- **Coords:** 48.4833, 135.0667 — Wikidata Q4454 · GeoNames 2022890
- **Confidence:** [C]
- **Jurisdictions:** RSFSR/USSR → Russia
- **People:** B11 arrived Feb 1931 (first assignment); typhoid in Khabarovsk hospital 1933 `tania-project (§§31, 16)`; `tania-project (locations)`

### P28 · Pokrovka
- **Variants:** Покровка · Pokrovka
- **Today:** Pokrovka, Khabarovsk Krai, Russia (near Khabarovsk)
- **Region:** Russia
- **Coords:** 48.3, 135.2 — `tania-project (locations)`, approximate
- **Confidence:** [L]
- **Jurisdictions:** RSFSR/USSR → Russia
- **People:** B11's first posting — state-farm training stop before Birobidzhan `tania-project (locations)`

### P29 · Birobidzhan
- **Variants:** Биробиджан · станция Тихонькая (Tikhonkaya station, renamed 1931)
- **Today:** Birobidzhan, Jewish Autonomous Oblast, Russia
- **Region:** Russia
- **Coords:** 48.7833, 132.9333 — Wikidata Q7769 · GeoNames 2026643; corroborated `tania-project (locations)`
- **Confidence:** [C]
- **Jurisdictions:** RSFSR/USSR — Jewish Autonomous Oblast from 1934 (station renamed Birobidzhan 1931) → Russia
- **People:** B11 & Iosif Baskin by 1935 `tania-project (§32)`; B11 arrived at Tikhonkaya station to join the Valdheim kolkhoz `tania-project (locations)`
- **Notes:** B11 visited grandfather Nakhman in Vitebsk in 1932 "from Birobidzhan" `tania-project (§32)`.

### P30 · Valdheim kolkhoz
- **Variants:** колхоз «Валдгейм» · Valdheim · Valdgeym
- **Today:** Valdgeym, Jewish Autonomous Oblast, Russia
- **Region:** Russia
- **Coords:** 48.7, 132.7 — `tania-project (locations)`, approximate
- **Confidence:** [L]
- **Jurisdictions:** RSFSR/USSR → Russia
- **People:** B11 working there as an agronomist where the memoir's surviving pages end `tania-project (locations)`

### P31 · Odessa
- **Variants:** Одесса · Odesa (official since 1995)
- **Today:** Odesa, Ukraine
- **Region:** Ukraine
- **Coords:** 46.4775, 30.7326 — Wikidata Q1874 · GeoNames 698740
- **Confidence:** [C]
- **Jurisdictions:** Russian Empire (Kherson gubernia) → Ukrainian SSR → Ukraine
- **People:** B11's first love went there to study theater; she saw him perform years later with a touring troupe `tania-project (§31)`; `tania-project (locations)`

### P32 · Mississippi (peddler circuit)
- **Variants:** Миссисипи · Mississippi (state)
- **Today:** Mississippi, USA
- **Region:** USA
- **Coords:** 32.7, -89.7 — `tania-project (locations)`, approximate (state)
- **Confidence:** [L]
- **Jurisdictions:** USA (state since 1817)
- **People:** B04 peddler/haberdashery years ~1895–1905, having arrived at 15 with elder brothers/uncles `tania-project (§5)`; B05 fur trade along the Mississippi and up the Arkansas River `EV-22`
- **Notes:** A region, not a point — the state-centroid pin is a visual anchor only; the known towns are P33 Rosedale and P34 Clarksdale.

### P33 · Rosedale
- **Variants:** Rosedale, Bolivar County, Mississippi
- **Today:** Rosedale, Mississippi, USA
- **Region:** USA
- **Coords:** 33.8536, -91.0269 — Wikidata Q2065882 · GeoNames 4828755
- **Confidence:** [C]
- **Jurisdictions:** USA (Mississippi)
- **People:** B05 Isadore's fur trade base (bought pelts along the Mississippi/Arkansas; companions Johnny Mott, Fred Couey) `EV-22`; B23 Louise ran the family clothing store `EV-22`; X11 Harold "Skeeter" b. ~1918 `EV-38`
- **Notes:** CF-14 (identification of the blog's Isadore with Eiser b. 1888 — likely, timing loose).

### P34 · Clarksdale
- **Variants:** Clarksdale, Coahoma County, Mississippi
- **Today:** Clarksdale, Mississippi, USA
- **Region:** USA
- **Coords:** 34.2006, -90.5702 — Wikidata Q990145 · GeoNames 4421935
- **Confidence:** [C]
- **Jurisdictions:** USA (Mississippi)
- **People:** B05 buried Beth Israel Cemetery, Clarksdale `Narrative, p. 21`

### P35 · Memphis
- **Variants:** Memphis, Tennessee
- **Today:** Memphis, Tennessee, USA
- **Region:** USA
- **Coords:** 35.1461, -90.0519 — Wikidata Q16563 · GeoNames 4641239
- **Confidence:** [C]
- **Jurisdictions:** USA (Tennessee)
- **People:** B07 Keili's line — grandson Israel Iskiwitz m. Dora Bernstein; Baron Hirsch Cemetery burials `EV-23`; `Notes, p. 12` (CF-12: Israel vs. Reuben Iscovitch)
- **Notes:** CF-15 — "Lucy Secher of Memphis" possibly B16 Lucy `[?]`.

### P36 · St. Louis
- **Variants:** St. Louis, Missouri
- **Today:** St. Louis, Missouri, USA
- **Region:** USA
- **Coords:** 38.6264, -90.1994 — Wikidata Q38022 · GeoNames 4407066
- **Confidence:** [C]
- **Jurisdictions:** USA (Missouri)
- **People:** B14 Dora's later life; m. David Glassman, later Lawrence Padawer; children Jerry, Mel, Paul `EV-34`

### P37 · Baton Rouge
- **Variants:** Baton Rouge, Louisiana
- **Today:** Baton Rouge, Louisiana, USA
- **Region:** USA
- **Coords:** 30.4475, -91.1786 — Wikidata Q28218 · GeoNames 4315588
- **Confidence:** [C]
- **Jurisdictions:** USA (Louisiana)
- **People:** X11 Harold "Skeeter" Mostkoff d. 31 Jul 2006; wife Doris Rhea d. 2006; founded Baton Rouge Restaurant Supply `EV-38`

### P38 · Las Vegas
- **Variants:** Las Vegas, Nevada
- **Today:** Las Vegas, Nevada, USA
- **Region:** USA
- **Coords:** 36.1672, -115.1486 — Wikidata Q23768 · GeoNames 5506956
- **Confidence:** [C]
- **Jurisdictions:** USA (Nevada)
- **People:** A09 Myrna Bilak d. 4 Sep 2001 `EV-39`

### P39 · New York
- **Variants:** Нью-Йорк · New York City
- **Today:** New York City, New York, USA
- **Region:** USA
- **Coords:** 40.7128, -74.0061 — Wikidata Q60 · GeoNames 5128581; corroborated `tania-project (locations)`
- **Confidence:** [C]
- **Jurisdictions:** USA
- **People:** "Khanele" — dau. of Luba (X18's dau.), "a beauty (she is Khanele's mother, from New York)" `tania-project (§34)`
- **Notes:** "All my father's brothers and sisters… live in the USA" (1976–80) `tania-project (§35)` — the US Mostkoff diaspora is mostly unplaced.

### P40 · Mexico City
- **Variants:** Мехико · Ciudad de México · Mexico, D.F.
- **Today:** Mexico City, Mexico (capital)
- **Region:** Mexico
- **Coords:** 19.3538, -99.1359 — Wikidata Q1489 · GeoNames 3527646
- **Confidence:** [C]
- **Jurisdictions:** Mexico
- **People:** B04 entered Mexico 1924 `EV-02/03` (**CF-03** date), d. 1957, buried Panteon Israelita `EV-13/15`; B10 sent for ~1926 `EV-03`; C06 + B12/B13/B14 entered Jan 1929 `EV-03`; C06 d. 1962 `EV-14`; B12 m. B15 1939 `EV-16`; B16–B21 b. 1939–57 `EV-17`; A05 to Mexico ~1919–25; A16–A18 b. 1926–36 `timeline, pp. 1–2`; A18 m. B17 — children Philip, Edna/Jaye, Shifra `[C — Philip, 2026-10-13]`; B22 d. 2013, buried Panteón Anexo 1 `EV-24`; A09 b. 1946 `EV-39`
- **Notes:** The three lines converge here (CLAUDE.md): Borenstein (Kurow), Mostkoff (Slutsk), Polak/Borukovich (Minsk/Slutsk).

### P41 · Guadalajara
- **Variants:** Guadalajara, Jalisco
- **Today:** Guadalajara, Jalisco, Mexico
- **Region:** Mexico
- **Coords:** 20.677, -103.347 — city-center coordinates (Wikidata Q9022, not re-verified by a second source this session)
- **Confidence:** [L]
- **Jurisdictions:** Mexico
- **People:** A11 Alfredo Ringel (Angela's son) — "brother Alfredo Ringel (Guadalajara)" `EV-39`

### P42 · Marbella
- **Variants:** Marbella, Málaga province
- **Today:** Marbella, Spain
- **Region:** Spain
- **Coords:** 36.5114, -4.8834 — Wikidata Q484799 · GeoNames 6359474
- **Confidence:** [C]
- **Jurisdictions:** Spain
- **People:** A10 Janette (Ringel) Epstein — "sister Janette Epstein (Marbella)" `EV-39`

## Tier 2 — background & lead toponyms (one-liners; un-geocoded)

*Pinkas "from X" descriptors for unrelated Slutsk townsfolk (EV-45/50 — may identify later if a family link surfaces):* **Kletsk** (#750) · **Brisk** (= Brest, #925) · **Lakhovits** (#1369) · **Lekhevits** (#687, #797) · **Ivenits** (#609) · **Luban** (#1792) · **Radkevits/Ratskevits** (Radkevitser Bunin clan — incl. "Yaakov ? of Yitskhak Bunin from Ratskevits," #5134, EV-45) · **Resk** (Zaturensky "from Resk," #2312, EV-56) · **Razoveh** (Kharakh of Razoveh, #998, EV-57 — C08 lead) · **Sareva** (#4380) · **Haresk** (#229, "Shulman from Haresk") · **Tsilevits** (#1036) · **Kudmits** (#435) · **Kaoutsh-Berodeh** (#335) · **Yamushk** (#117) · **Halusk** (#30) · **Kashmanits** (#17700) · **Shinavke/Shlinavkeh** (#1506, #1211) · **Malasevits** (Malasevitser Bunin clan) · **Tsaplits** (#848) · **Timkevits** (#2019) · **Ozdeh/Laseh** covered as P16/P17.

*Record leads:* **Koidanov** (now Dzyarzhynsk — EV-11, "probably not ours") · **Smorgon** + **Bogunov** (EV-30, the 1838 Nokhim candidate's grandparents) · **Gomel** + **Rechitsa** (EV-12 Bunin-adjacent marriage lead) · **Priluki** (Ukraine — EV-48, 1877 Sapotnitsky-surname marriage, investigation lead) · **Berezino** (EV-10 — Wendy's email gloss; a mis-parse, not clearly a person/place of ours).

*Memoir transit stops (tania-project locations table):* **Osipovichi** (Asipovichy — 1926 transfer) · **Smolensk** (same journey) · **Bitsa station** (now part of Moscow — seed-growing college) · **Crimea** (a state farm, Finkelstein's previous post — not family).

*Glancing mentions:* **Arizona** (A05 crossed into Arizona May 1934 alone, destination unknown `[?] timeline, p. 1`) · **Poland** (generic — X18's dau. Luba "left for Poland") · **Vera Cruz** (port of arrival, *Edam* 1924 — EV-02) · **"the USA"** (the unplaced post-war diaspora of B01/B02's children, `tania-project (§35)`).
