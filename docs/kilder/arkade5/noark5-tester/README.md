# Arkade 5 – Noark 5-tester

## Formål

Denne dokumentasjonsserien beskriver hva Arkade 5 sine Noark 5-tester faktisk gjør, basert på den åpne kildekoden.

Målet er at en arkivfaglig person skal kunne forstå testene uten å måtte lese C#, samtidig som hver beskrivelse skal være sporbar tilbake til implementasjonen.

Se [KILDESTATUS.md](KILDESTATUS.md) for dokumentert kode-snapshot.

## Dokumentasjonsmodell

For hver test dokumenteres så langt kildekoden gir grunnlag for det:

- test-ID og implementasjonsklasse
- type: analyse/telling, kontroll/validering eller annen funksjon
- hva testen leser
- hva testen faktisk gjør
- hva den rapporterer
- viktige særregler/forutsetninger
- kjent endringshistorikk som påvirker forståelsen
- direkte kildekodelenke
- senere kobling til historisk N5, KDRS Query/XPath og U1/U2

## Verifisert første kartlegging

Følgende forhold er eksplisitt bekreftet i Arkade-koden eller commit-historikken i første runde:

| Test | Implementasjon / verifisert funksjon | Foreløpig type |
|---|---|---|
| N5.01 | `N5_01_ValidateStructureFileExists` | kontroll |
| N5.02 | `N5_02_ValidateAddmlDataobjectsChecksums` | kontroll |
| N5.03 | `N5_03_ValidateXmlWithSchema` | kontroll |
| N5.04 | `N5_04_NumberOfArchives` | analyse/telling |
| N5.05 | `N5_05_NumberOfArchiveParts` | analyse/telling |
| N5.06 | `N5_06_StatusOfArchiveParts` | analyse/telling |
| N5.10 | teller mappetyper; senere endret til også å rapportere mapper uten type-attributt | analyse |
| N5.16 | teller registreringstyper og inkluderer også ukjente registreringstyper | analyse |
| N5.24 | antall dokumentbeskrivelser uten dokumentobjekt; `utgår` håndteres særskilt | kontroll/analyse |
| N5.25 | `N5_25_NumberOfEachDocumentStatus` | analyse |
| N5.26 | `N5_26_NumberOfDocumentObjects` | analyse/telling |
| N5.28 | dokumentfilavhengig test | kontroll |
| N5.30 | dokumentfilavhengig test | kontroll |
| N5.32 | dokumentfilavhengig test | kontroll |
| N5.33 | dokumentfilavhengig test | kontroll |
| N5.34 | valideringsresultat skiller feil fra warnings/information | kontroll |
| N5.35 | har versjonsspesifikk støtte for Noark 5-varianter | kontroll/analyse |
| N5.63 | rapporterer XML-elementer uten innhold | kontroll/analyse |
| N5.64 | teller/rapporterer dokumentfiler med faktisk filstørrelse 0 | kontroll/analyse |

Dette er **ikke den ferdige dokumentasjonen av hele testsettet**. Bare forhold som er eksplisitt verifisert er fylt inn. Resten skal dokumenteres test for test fra kildekoden, ikke utledes fra testnummer eller historisk testnavn alene.

## Viktige implementasjonsobservasjoner

Arkade 5 har en egen `Noark5TestFactory` som kobler N5-ID til konkrete testklasser. De individuelle testene ligger i `Core/Testing/Noark5/`.

Arkade har også egne enhetstester under `Core.Tests/Testing/Noark5/`. Disse er viktige fordi de kan dokumentere grenseverdier og forventet oppførsel som ikke er tydelig fra testnavnet alene.

Arkade skiller dessuten ut tester som er avhengige av dokumentfiler. Kodegrunnlaget identifiserer blant annet N5.28, N5.30, N5.32 og N5.33 som dokumentfilavhengige.
