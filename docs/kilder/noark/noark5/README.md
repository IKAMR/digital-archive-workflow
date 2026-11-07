# Noark 5 – historiske versjoner og kildemateriale

Denne mappen samler versjonsdelte standarddokumenter, vedlegg, eksempler og XML-skjemaer for **Noark 5**. Den er et kildebibliotek for `digital-archive-workflow`, ikke en komplett katalog over alle publiserte eller gjeldende kilder.

## Innhold i repositoryet (2026-11-07)

| Versjon | XML-skjemaer | Standarder, vedlegg og eksempler |
| --- | ---: | ---: |
| [v1.0](v1.0/) | 4 | 0 |
| [v2.0](v2.0/) | 5 | 0 |
| [v3.0](v3.0/) | 5 | 0 |
| [v3.1](v3.1/) | 5 | 7 |
| [v4.0](v4.0/) | 5 | 13 |
| [v5.0](v5.0/) | 5 | 9 |
| [v6.0](v6.0/) | 0 | 6 |

Versjon 6.0 har per denne gjennomgangen ingen XSD-filer i repoet. For 1.0, 2.0 og 3.0 er det bare XSD-filer i de respektive versjonsmappene. Dette er **mangler i samlingen**, ikke dokumentasjon på hva som finnes hos opprinnelig utgiver.

## Prinsipper

- Velg standardversjon ut fra det aktuelle uttrekkets dokumentasjon og kravgrunnlag.
- Hold originalfilene uendret og bevar filnavnene.
- Ikke bruk senere skjemaer som automatisk erstatning for eldre versjoners XSD.
- Oppgi eksakt versjon og fil ved faglige vurderinger.
- Skill kildemateriale fra egne tester, analyser og beslutninger.

## Sporbarhet og publisering

Det eksisterende [`SOURCE-MANIFEST.json`](../SOURCE-MANIFEST.json) og [`SHA256SUMS.txt`](../SHA256SUMS.txt) omfatter i dag bare Noark 3/4. Før Noark 5-samlingen omtales som fullt sporbar bør opphav, kilde-URL, hentedato, filstørrelse, SHA-256 og rettighetsstatus registreres for hver fil. Kontrollsummer skal beregnes fra faktiske filbytes, ikke antas. Avklar publiseringsrett for kopierte standarddokumenter.

Se [overordnet Noark-oversikt](../README.md).
