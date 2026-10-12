# Evenimente în Satu Mare, ca date deschise

**[ilovesm.ro](https://ilovesm.ro)** („Satu Mare, te iubesc”) este agenda evenimentelor din Satu Mare și din tot județul: teatru, Filarmonica „Dinu Lipatti”, concerte, expoziții, festivaluri, cinema, stand-up și activități pentru copii, în Satu Mare, Carei și în localitățile din jur. Agenda e gratuită și există în română, maghiară și engleză.

Am vrut ca aceste informații să nu stea doar pe site. Oricine are un site, o aplicație, un ecran într-un hol de hotel sau un proiect la facultate poate lua evenimentele direct, fără cont și fără să ne ceară voie. Aici e tot ce trebuie pentru asta.

> Pagina oficială a datelor: **[ilovesm.ro/date-deschise](https://ilovesm.ro/date-deschise)**

## Ce găsești pe ilovesm.ro

Dacă ai ajuns aici căutând ce faci în Satu Mare, începe cu paginile astea:

- [Toate evenimentele din Satu Mare](https://ilovesm.ro/evenimente)
- [Ce faci azi](https://ilovesm.ro/evenimente/azi) și [ce faci în weekend în Satu Mare](https://ilovesm.ro/evenimente/weekend)
- [Teatru în Satu Mare](https://ilovesm.ro/evenimente/teatru): Teatrul de Nord, trupa Harag György, spectacole în română și maghiară
- [Filarmonica și muzică clasică](https://ilovesm.ro/evenimente/filarmonica)
- [Concerte și muzică live](https://ilovesm.ro/evenimente/concerte)
- [Evenimente cu intrare liberă](https://ilovesm.ro/evenimente/gratuit)
- [Pentru copii](https://ilovesm.ro/evenimente/copii)
- [Evenimente în Carei](https://ilovesm.ro/evenimente/in-carei)
- [Programul cinematografelor](https://ilovesm.ro/cinema) (Cinema One și Cineplexx)
- [Harta locurilor](https://ilovesm.ro/harta) și [calendarul pe zile](https://ilovesm.ro/calendar)

Pe maghiară: [Szatmárnémeti programok](https://ilovesm.ro/hu/). Pe engleză: [Events in Satu Mare](https://ilovesm.ro/en/).

## Cum iei datele

Totul e public și merge direct din browser, de pe orice domeniu (CORS deschis). Răspunsurile sunt în JSON și au mereu aceeași formă:

```json
{ "ok": true, "data": { ... } }
```

iar la eroare `{ "ok": false, "error": "..." }`. Rezultatele stau câteva minute în cache, deci nu are rost să întrebi mai des de atât.

### Lista evenimentelor: `GET /api/events`

```
https://ilovesm.ro/api/events?date=weekend&lang=ro
```

| Parametru | Ce face |
|---|---|
| `page` | pagina, implicit 1 |
| `per_page` | câte pe pagină, maximum 50 (implicit 20) |
| `date` | `today`, `tomorrow`, `weekend`, `week`, `month`, `past` sau `all` |
| `cat` | categoria, de exemplu `teatru`, `filarmonica`, `concerte`, `copii` |
| `audience` | `copii`, `familie`, `adulti`, `seniori`, `general` |
| `free` | `1` pentru evenimentele cu intrare liberă |
| `neighbourhood` | cartierul |
| `q` | text de căutat |
| `lang` | `ro`, `hu` sau `en` (titlurile și adresele vin traduse, unde avem traducere) |

Un eveniment arată cam așa:

```json
{
  "id": 2667,
  "title": "Concert cameral: Vlad Răceu, Gabriel Cupșa și Cadmiel Boțac",
  "url": "https://ilovesm.ro/e/concert-cameral-kamaraest-filarmonica-de-stat-dinu-lipatti/2667",
  "date_label": "Mar, 13 oct · 19:00",
  "start_datetime": "2026-10-13 19:00:00",
  "cover_image": "https://cdn.ottoweb.ro/...webp",
  "category_name": "Filarmonică & Muzică Clasică",
  "category_slug": "filarmonica",
  "venue_name": "Filarmonica „Dinu Lipatti” - Sala de Concerte",
  "is_free": false,
  "price_info": null,
  "audience_type": null
}
```

Folosește `id` ca identificator. E stabil, pe când titlul se mai corectează.

Categoriile existente: `teatru`, `filarmonica`, `concerte`, `evenimente-publice`, `copii`, `familie`, `cultura`, `expozitii`, `educatie`, `sport`, `wellness`, `food`, `comunitate`, `business`, `outdoor`, `traditii`, `cinema`, `standup`.

### Calendar pentru telefon: `GET /api/calendar`

Un flux iCalendar la care te abonezi o dată, iar evenimentele noi apar singure în Google Calendar, Apple Calendar sau Outlook. Se actualizează la câteva ore, iar anulările ajung și ele.

```
https://ilovesm.ro/api/calendar?cat=teatru
https://ilovesm.ro/api/calendar?org=2&lang=hu
```

Filtre: `org` (organizatorul), `cat` (categoria), `venue` (locul), `lang`. Calendarul general, cu tot orașul, e la [ilovesm.ro/calendar.ics](https://ilovesm.ro/calendar.ics).

### RSS

[ilovesm.ro/rss](https://ilovesm.ro/rss), cu `?lang=hu` sau `?lang=en` pentru celelalte limbi. Conține doar evenimente la care mai poți merge.

### Widget pentru site-ul tău

Dacă organizezi evenimente în Satu Mare și vrei programul tău pe site-ul tău, fără să-l actualizezi de mână:

```html
<div class="smev-widget" data-org="2" data-limit="5" data-theme="light" data-lang="ro"><a href="https://ilovesm.ro/o/teatrul-de-nord/2">Programul complet pe ilovesm.ro</a></div>
<script src="https://ilovesm.ro/assets/js/smev-widget.js" async></script>
```

`data-org` e numărul organizatorului din adresa paginii lui de pe ilovesm.ro (de exemplu `/o/teatrul-de-nord/2`). Cu `data-org="all"` primești toate evenimentele din oraș. Mai poți pune `data-cat` (o categorie), `data-theme="dark"` și `data-lang="hu"` sau `"en"`. Datele vin din `GET /api/widget`. Legătura din interiorul blocului rămâne vizibilă dacă cineva are JavaScript oprit sau dacă lista nu se poate încărca.

## Exemple

În folderul [`examples`](examples) sunt trei exemple scurte, fără biblioteci:

- [`weekend.html`](examples/weekend.html): o pagină care arată ce e în weekend în Satu Mare;
- [`evenimente.py`](examples/evenimente.py): același lucru din linia de comandă, cu Python;
- [`widget.html`](examples/widget.html): widgetul pus într-o pagină.

## Licență

Datele despre evenimente sunt oferite sub [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ro). Le poți folosi, schimba și publica mai departe, și în scop comercial, cu o singură condiție: să scrii de unde le ai, adică **ilovesm.ro**, de preferat cu link. Codul exemplelor din acest repository e sub licența MIT.

Imaginile evenimentelor (afișele) aparțin organizatorilor. Pentru ele, întreabă organizatorul.

## Ai găsit ceva greșit?

Dacă vezi un eveniment cu ora greșită, un loc care lipsește sau vrei un câmp nou în API, scrie-ne pe [ilovesm.ro/contact](https://ilovesm.ro/contact) sau deschide un issue aici. Iar dacă organizezi ceva în Satu Mare, îl poți [propune direct pe site](https://ilovesm.ro/propune-eveniment).

---

## Magyarul

Az **[ilovesm.ro](https://ilovesm.ro/hu/)** Szatmárnémeti és Szatmár megye programnaptára: színház (Északi Színház, Harag György Társulat), filharmónia, koncertek, kiállítások, mozi és gyerekprogramok, Szatmárnémetiben, Nagykárolyban és a környéken. Az események nyílt adatként is elérhetők: JSON API, naptár-feliratkozás (iCalendar), RSS és beágyazható widget. Minden végpont magyarul is válaszol a `lang=hu` paraméterrel. Licenc: CC BY 4.0, forrásmegjelöléssel (ilovesm.ro).

## In English

**[ilovesm.ro](https://ilovesm.ro/en/)** is the events agenda for Satu Mare, Romania, and the surrounding county: theatre, the Dinu Lipatti Philharmonic, concerts, exhibitions, cinema and family events. All events are available as open data: a JSON API, iCalendar feeds, RSS and an embeddable widget, in Romanian, Hungarian and English (`lang=en`). Data license: CC BY 4.0, please credit ilovesm.ro.
