# Ressurs- og kildekart for arkivsystemanalyse

**Status:** Foreslått plassering og kildeoversikt, 2026-11-07. Dette er ikke i seg selv en vedtatt modell eller lisensvurdering.

## Hensikt og prinsipper

`digital-archive-workflow` er den åpne faglige inngangen. `depot-data-model` beskriver katalog-/integrasjonsidentitet. `data-workflow-manager` og `SIARD-Workflow-Manager` implementerer hver sin rolle og skal vise til de samme fagdefinisjonene. Private produsentspesifikke hjelpemidler holdes utenfor de åpne programrepoene.

Tre **private ressursklasser som appen skal kunne lese lokalt**:

1. `templates/decom/` – originale Decom-maler.
2. `templates/kdrs-sok-og-vis/` – originale KDRS Søk & Vis-maler.
3. `adapters/<system>/` – system-til-fagmodell-mappinger, reverse-engineered leverandørmateriale, leverandørspesifikk SQL og kundespesifikke varianter (inkludert ePhorte/Noark 4).

Det er kun disse tre **applikasjonsressurstypene** som planlegges som privat fagressursbibliotek. Operative depotdata, faktiske uttrekk og personopplysninger hører heller ikke hjemme i offentlige GitHub-repoer, men er en separat kategori *driftsdata*, ikke en fjerde appressurstype.

### Privat fagressursrot (konfigureres i SIARD Workflow Manager)

```text
<valgfri-lokal-rot>/
  templates/
    decom/
    kdrs-sok-og-vis/
  adapters/
    ephorte/
      noark4/
        queries/
    familia/
      barnevern/
```

Programmet leser den konfigurerte lokale rotmappen. Rotmappen kan være en **synkronisert utsjekk av et tilgangsstyrt privat GitHub-repo** dersom brukeren har tilgang. Ikke hardkod diskbokstaver og ikke legg private filer i et offentlig repo selv om de står i `.gitignore`.

## Åpne fagressurser og plassering

| Innhold | Åpen kilde/foreslått plassering | Merknad |
|---|---|---|
| Noark 3 normative PDF-er/vedlegg | `digital-archive-workflow/docs/kilder/noark/noark3/spesifikasjoner/` | Kopier eksakte originaler når filene er tilgjengelige, registrer kilde og versjon |
| Noark 4.1 PDF-er, rettelser og kravtabeller | `digital-archive-workflow/docs/kilder/noark/noark4/spesifikasjoner/` | De seks opplastede filene er kildegrunnlag; avklar viderepubliseringsrett før offentlig commit |
| Noark 4 DTD-filer | [IKAMR/schemas/N4](https://github.com/IKAMR/schemas/tree/master/N4) | Bruk fork som kilde, ingen unødvendig duplikat. `/N4/latest` og `/N4/v1.0` har 101 identiske Git-objekter ved denne kontrollen |
| Andre Noark-/METS-/PREMIS-skjemaer | [IKAMR/schemas](https://github.com/IKAMR/schemas) | Referer versjon/ref og eventuell commit for reproduksjon |
| Normative begreper, fagområde-/modulmodeller | `digital-archive-workflow/docs/fagmodeller/` | Maskinlesbare, versjonerte modeller inngår i SIARD WM `siard_workflow/models/` |
| ASTA/KAISA 9 kategorier og kommunale 20 systemkategorier | `digital-archive-workflow/docs/kilder/kommunal-systemkartlegging/` | Bruk tidligere leverte 11 dokumenter/JSON/CSV, ikke operative FFKK-data |
| To eksisterende Noark-regneark | `data-workflow-manager/docs/reference-material/noark/` | Se særskilt vurdering av leverandørfaner under |
| Historisk kildekartlegging og prosess | `digital-archive-workflow/docs/kilder/` og `docs/prosess/` | Behold fagkilden uavhengig av app |
| Sammenlignings- og integrasjonskontrakter | `depot-data-model/docs/` + appenes egne kontrakter | Ingen operative katalogdata |
| Offentlig programkode, generiske QA-motorer og tester | `SIARD-Workflow-Manager` / `data-workflow-manager` | Ingen private adapterfiler |

## Eksisterende offentlig materiale som må gjennomgås

Følgende er **allerede i åpne repoer**, men blander muligens generiske referanser og produsentspesifikke detaljer:

- `data-workflow-manager/docs/reference-material/noark/noark4-fields-working-reference.xlsx` har ePhorte-, ESA- og DocuLive-spesifikke kolonner/faner. Del eventuelt generiske Noark 4-definisjoner (åpent) fra konfidensielle leverandørmappinger (privat), etter vurdering. IKKE slett eller endre kilden i stillhet.
- `digitalt-depot-prosesser/arkiv-work_default-folders/.../repository_operations/queries/noark4db/sql-queries_noark4_S1041_ephorte_2022-10-01.txt` og tilsvarende ESA-spørringer er også allerede offentlig tilgjengelige. Vurder om de er åpne egenutviklede analyser eller inneholder beskyttet leverandørmateriale.

**De to nyere opplastede** `S1041_ephorte_query-mysql.sql` og `S1041_ephorte_query-mysql_2021-11-25.sql` foreslås som referanser i privat `adapters/ephorte/noark4/queries/` inntil innhold og publiseringsrett er avklart; dette er under den *tredje* private ressursklassen, ikke en fjerde.

## Excel-original og person-/depotdata

`0000-kommune-elarkiv.xlsx` inneholder både kategori-/systemreferanser og et `FFKK`-ark med konkrete system-/bevaringsopplysninger og ansvarsfelt. Offentliggjør de **uttrukne generiske delene** under `docs/kilder/kommunal-systemkartlegging/`. Bevar uendret original på egnet intern kildeplassering inntil FFKK-innholdet er gjennomgått; offentlig, renset kildeutgave kan lages separat. Dette er ikke begrunnet i leverandørhemmeligheter, men i skillet mellom fagreferanser og operativ depotinformasjon.

## SHA-256 for de seks tilgjengelige Noark 4.1-kildene

| Originalt filnavn | SHA-256 |
|---|---|
| `Noark-4_del1.pdf` | `a7781175ce3ac21a0149ee08e8e38d79cd0925d2b829175d99a5df537ceef988` |
| `Noark-4_del2.pdf` | `35617381c98ab4d38ad8c8c9ea844a708c77cf4b03738eca5da074b00dc07956` |
| `N4_1 Kravtabellene.pdf` | `21a158a66382942e088452819d1ac06024962b622d570c9199b88d5471ab7f10` |
| `N4 Feilrettingslogg for Noark-4 Del 1 og 2.pdf` | `8434cbb7705f43d749f2132eebbd50b3816c160e6d71f06c5183fda5a49612f0` |
| `N4_endringer_del1.pdf` | `0b0109c6dfc30250ad556b5cbe5b4e8f2ae671be1d1f62f4dd09acdb2bf64366` |
| `N4_endringer_del2.pdf` | `11a78d9d75a1299cb288b8727aa320cce9d682ab401d8a5c200b1ff82d3eaae4` |

Hashene verifiserer nøyaktig den opplastede filutgaven; de fastslår ikke lisens eller normativ status.

## Hvordan finne igjen dette i nye AI-utviklingstråder

1. Start med den **levende** offentlige kunnskapsindeksen: `IKAMR/digital-archive-workflow/docs/RESSURS-OG-KILDEKART.md` og repoets `README.md`.
2. Bruk GitHub-tilkobling med autorisasjon til privat repo, dersom innholdet skal leses. Indeksen over private ressurser bør ligge privat som `README.md` og `catalog.json` med logisk ID, faktisk filsti, versjon, SHA-256, kilde og tilgangsklasse.
3. Oppgi konkret branch/commit for modell, adapter og kilde. Ikke gjør programmet avhengig av AI-minne. Skriv alle avgjørelser i repo.
4. Oppgi **godkjent LABEL eksplisitt** på uttrekk og rapporter. Et teknisk filnavn, eksempelvis et SQL-/databasebackup-navn, er ikke LABEL. `1547_003 ephorte (2012-2019)` og `1547_003 ephore SIARD (2012-2019)` er to ulike representasjoner og må ikke identifiseres med et vilkårlig tidligere QA-kildenavn.

Ved ny utvikling skal assistenten hente siste revisjon av kilderegister og relevante private manifest (hvis gitt tilgang) før noen mapping eller implementasjon endres.
