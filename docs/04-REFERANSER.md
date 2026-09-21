# Referanser og eksterne kilder

Denne listen er et kuratert kilderegister for `digital-archive-workflow`. Kildene har ulike roller: standarder og skjema, prosessgrunnlag, dokumentasjon, programvare, analyseverktøy og praktiske implementasjoner.

Kilderegisteret fungerer også som varig oversikt over sentrale repo-relasjoner. Ved oppstart av ny utviklingskontekst skal dokumenterte lenker brukes før kjente repo-adresser etterspørres på nytt.

## Nasjonalarkivet / Arkivverket

### Arkade 5

- Arkade: https://arkade.arkivverket.no/
- Arkade 5 kildekode: https://github.com/nasjonalarkivet/arkade5
- Arkade 5 dokumentasjon: https://github.com/nasjonalarkivet/arkade5-dokumentasjon
- Systemdokumentasjon / aktuell Noark 5-testliste: https://docs.arkade.nasjonalarkivet.no/no/latest/Systemdokumentasjon.html#noark-5
- Noark 5-testimplementasjoner i kildekoden: https://github.com/nasjonalarkivet/arkade5/tree/master/src/Arkivverket.Arkade.Core/Testing/Noark5
- Noark 5 test factory: https://github.com/nasjonalarkivet/arkade5/blob/master/src/Arkivverket.Arkade.Core/Base/Noark5/Noark5TestFactory.cs

**Relevans:** sentral offentlig implementasjon av validering, analyse og rapportering for Noark 5 og andre arkivuttrekk. Kildekoden brukes som grunnlag når vi dokumenterer hva de enkelte N5-testene faktisk gjør.

### Noark 5 og skjema

- Noark 5-standard: https://github.com/nasjonalarkivet/noark5-standard
- Skjema: https://github.com/nasjonalarkivet/schemas

**Relevans:** faglig og teknisk grunnlag for Noark 5-struktur, metadata og XML-validering.

## KDRS

### KDRS Prosesser og rutiner

- https://www.kdrs.no/kdrs-prosesser
- https://prosjekt.kdrs.no/ProsessDigitaltDepot/V1.0/ProsessDigitaltDepot.htm
- https://prosjekt.kdrs.no/ProsessDigitaltDepot/V2.02/ProsessDigitaltDepot.htm

**Relevans:** viktig prosessgrunnlag for mottak, kontroll, test, AIP, lagring, tilbakemelding og andre deler av digitalt depot.

`digital-archive-workflow` skal bygge videre på og operasjonalisere relevant arbeid herfra, ikke konkurrere med initiativet.

### KDRS-SA GitHub

- https://github.com/kdrs-sa
- https://github.com/orgs/KDRS-SA/repositories?type=all

**Relevans:** samling av åpne verktøy og prosjekter knyttet til blant annet validering, uttrekk, innsyn, metadata og digitalt depot. Relevante repositories skal kartlegges nærmere.

## IKAMR

### Noark 5 Workflow Manager

- https://github.com/IKAMR/noark5-workflow-manager

**Relevans:** aktiv implementasjon av arbeidsflyt, jobbmodell, validering, rapportering og depotrelaterte operasjoner. `digital-archive-workflow` er faglig kunnskapsgrunnlag for denne og andre implementasjoner, mens implementasjonsdetaljer skal ligge i applikasjonsrepoet.

### Incremental AI-Assisted Development Method

- https://github.com/IKAMR/incremental-ai-development-method

**Relevans:** felles metodikk for inkrementell AI-assistert programvareutvikling, repository som source of truth, kumulative ZIP-delta, testing, dokumentasjon og menneskestyrt Git. Prosjektspesifikke metodikkobservasjoner samles lokalt i de enkelte utviklingsrepoene før eventuell overføring til denne felles metodikken.

### KDRS Query

- https://github.com/IKAMR/KDRS_Query
- https://github.com/IKAMR/KDRS_Query/tree/master/doc

**Relevans:** historisk og praktisk analyse- og kontrollgrunnlag, inkludert XPath/XQuery-baserte Noark 5-analyser, arbeidsbeskrivelser og U1/U2.

### KDRS Metadata

- https://github.com/IKAMR/KDRS_Metadata

**Relevans:** metadatarelatert kilde og historikk knyttet til digitale arkivuttrekk og depotarbeid.

### digitalt-depot-prosesser

- https://github.com/IKAMR/digitalt-depot-prosesser

**Relevans:** IKAMRs implementering av KDRS Prosesser og rutiner, med tilhørende operativ dokumentasjon, test- og valideringsopplegg, uttrekksveiledning, depotlogger og standardiserte arbeids- og mappestrukturer.

### IKAMR GitHub

- https://github.com/IKAMR
- https://github.com/orgs/IKAMR/repositories

**Relevans:** flere åpne repositories kan inneholde relevant historikk, verktøy og dokumentasjon. Disse skal gjennomgås systematisk.

## SIARD og arbeidsflyt

### SIARD Workflow Manager

- https://github.com/smult/SIARD-Workflow-Manager

**Relevans:** praktisk arbeidsflyt for SIARD og viktig referanse for generiske prinsipper om profiler, logging, pakking og arbeidssteg.

## Videre arbeid

Kilderegisteret skal utvides etter hvert som relevante åpne repositories og normative kilder blir gjennomgått. Detaljert dokumentasjon skal ligge under `docs/kilder/`, mens denne filen fungerer som samlet inngang til eksterne kilder.
