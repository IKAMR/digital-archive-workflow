# Noark - historiske standardspesifikasjoner

Dette er kildebiblioteket for Noark-spesifikasjoner i **digital-archive-workflow**.
Denne leveransen inneholder **Noark 3 (1994)** og **Noark 4/4.1**.

| Standard | Mappe | Status i denne leveransen |
| --- | --- | --- |
| Noark 3 | [`noark3/`](noark3/) | Original PDF, 1994 |
| Noark 4 / 4.1 | [`noark4/`](noark4/) | Seks originalfiler, inkludert rettelser og endringer |

## Skjemaer og tilknyttede kilder

Noark 4-DTD-filer kopieres ikke inn her, fordi de allerede er tilgjengelige i
[IKAMR/schemas - N4](https://github.com/IKAMR/schemas/tree/master/N4).
De to versjonsmappene i skjemarepoet er separate referanser og skal behandles
som versjonerte kilder.

Noark 5-dokumentasjon fra den innsendte `noark.zip` er bevisst **ikke tatt med**
i denne deltaen. Ingen produktgodkjenninger, egne arbeidsdokumenter,
Noark 4-testing, DTD-er eller Noark 5-skjemaer er flyttet hit.

## Sporbarhet og versjonering

- Originale filnavn og PDF-innhold er beholdt uendret.
- [`SOURCE-MANIFEST.json`](SOURCE-MANIFEST.json) registrerer kildeplassering,
  sidetall, filstørrelse og SHA-256 per dokument.
- [`SHA256SUMS.txt`](SHA256SUMS.txt) muliggjør bitvis kontroll av PDF-ene.
- Opphav for denne samlingen: innsendt brukerarkiv `noark.zip`, 2026-11-07.
- Dokumentene er **historiske kilder** og skal ikke tolkes som gjeldende
  standardkrav uten særskilt kilde- og versjonsvurdering.

## Rettigheter

**Rett til offentlig viderepublisering av PDF-kopiene er ikke bekreftet i
arbeidet med denne deltaen.** Avklar dette før PDF-ene committes til et
offentlig repository. Ved tvil kan README, kildehenvisninger og kontrollsummer
publiseres først, mens PDF-ene beholdes lokalt frem til avklaring.
