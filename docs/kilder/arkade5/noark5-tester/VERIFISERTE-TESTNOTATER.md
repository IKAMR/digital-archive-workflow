# Første verifiserte testnotater

Dette dokumentet inneholder bare forhold som er eksplisitt støttet av Arkade 5-kode eller commit-historikk i den første kartleggingen.

## N5.01 – strukturfil finnes

**Implementasjonsklasse:** `N5_01_ValidateStructureFileExists`

Factory-navnet viser at testen validerer at strukturfilen som Arkade forventer finnes.

**Type:** kontroll.

**Kilde:**  
https://github.com/nasjonalarkivet/arkade5/blob/40a32ee0ae84ddf44d1f3c35f1860567ca262733/src/Arkivverket.Arkade.Core/Base/Noark5/Noark5TestFactory.cs

## N5.02 – sjekksummer for ADDML-dataobjekter

**Implementasjonsklasse:** `N5_02_ValidateAddmlDataobjectsChecksums`

Factory-navnet viser at testen validerer sjekksummer for dataobjekter referert gjennom ADDML.

Commit-historikken viser senere feilrettinger slik at testen ikke skulle abortere ved bestemte problemer, og at riktig filnavn skulle brukes som location i testresultatet.

**Type:** kontroll.

## N5.03 – XML mot skjema

**Implementasjonsklasse:** `N5_03_ValidateXmlWithSchema`

Validerer XML med skjema.

**Type:** kontroll/validering.

## N5.04 – antall arkiv

**Implementasjonsklasse:** `N5_04_NumberOfArchives`

Teller arkiv. Arkades egne enhetstester inneholder blant annet et scenario der to arkiv forventes funnet.

**Type:** analyse/telling.

**Implementasjon:**  
https://github.com/nasjonalarkivet/arkade5/blob/40a32ee0ae84ddf44d1f3c35f1860567ca262733/src/Arkivverket.Arkade.Core/Testing/Noark5/N5_04_NumberOfArchives.cs

## N5.05 – antall arkivdeler

**Implementasjonsklasse:** `N5_05_NumberOfArchiveParts`

Teller arkivdeler.

**Type:** analyse/telling.

## N5.06 – status for arkivdeler

**Implementasjonsklasse:** `N5_06_StatusOfArchiveParts`

Rapporterer statusfordeling for arkivdeler.

**Type:** analyse.

## N5.10 – mappetyper

Commit-historikken viser at testen teller mappetyper, og at den senere ble endret til også å rapportere mapper uten type-attributt.

**Type:** analyse.

Dette er viktig i sammenligning med U1/U2 fordi testen ikke bare teller mapper totalt, men grupperer etter type og behandler manglende type eksplisitt.

## N5.16 – registreringstyper

Commit-historikken viser at N5.16 ble endret til å telle registreringstyper, og senere til å inkludere ukjente registreringstyper.

**Type:** analyse.

Dette ligger svært nær formålet med de generiske registreringstellingene i KDRS Query/U1.

## N5.24 – dokumentbeskrivelser uten dokumentobjekt

Factory-koden identifiserer klassen som `N5_24_NumberOfDocumentDescriptionsWithoutDocumentObject`.

Commit-historikken viser at `utgår`-status senere ble håndtert særskilt sammen med N5.21.

**Type:** kontroll/analyse.

## N5.25 – dokumentstatus

**Implementasjonsklasse:** `N5_25_NumberOfEachDocumentStatus`

Teller forekomster per dokumentstatus.

**Type:** analyse.

## N5.26 – dokumentobjekter

**Implementasjonsklasse:** `N5_26_NumberOfDocumentObjects`

Teller dokumentobjekter.

**Type:** analyse/telling.

## Dokumentfilavhengige tester

Arkades `TestSession` har en egen liste over dokumentfilavhengige Noark 5-tester. Første verifiserte utdrag omfatter:

- N5.28
- N5.30
- N5.32
- N5.33

Dette er arkitektonisk viktig: disse testene har andre I/O- og ytelsesegenskaper enn tester som bare analyserer metadata-XML.

## N5.34

Commit-historikken viser en feilretting der warnings/information fra underliggende validering ikke lenger skulle rapporteres som errors.

**Type:** kontroll/validering.

Detaljert valideringsmekanisme må dokumenteres fra selve testklassen før vi beskriver mer.

## N5.35

Commit-historikken viser eksplisitt versjonsavhengig håndtering, blant annet støtte for Noark 5 v5.5 og senere retting av testnavn for v5-uttrekk.

Dette betyr at dokumentasjonen må beskrive versjonslogikken, ikke bare én generell testbeskrivelse.

## N5.63 – XML-elementer uten innhold

Commit-historikken beskriver N5.63 som en test som rapporterer arkiv-XML-elementer uten innhold.

**Type:** kontroll/analyse.

## N5.64 – dokumentfiler med størrelse 0

N5.64 ble lagt til for å telle og rapportere dokumentfiler med størrelse 0.

Senere endring presiserte at:
- skråstrekretning i sti fra `arkivstruktur.xml` ikke skal ha betydning
- bare filer med faktisk filstørrelse 0 skal rapporteres

**Type:** kontroll/analyse.
