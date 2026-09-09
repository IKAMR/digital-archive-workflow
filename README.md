# digital-archive-workflow

Kunnskapsbase for mottak, validering, godkjenning, bevaring og innsyn i digitale arkivuttrekk.

Prosjektet starter med **Noark 5 og norske kommunale arkivdepotprosesser**, men kunnskapsmodellen skal ikke unødvendig låses til Noark. SIARD og andre uttrekkstyper kan senere inngå i samme overordnede arbeidsmodell.

## Hvorfor repoet finnes

Dagens kunnskap ligger fordelt mellom standarder, prosessbeskrivelser, rutiner, sjekklister, rapportmaler, depotlogger, XPath/XQuery, verktøy som Arkade 5 og KDRS Query, praktisk erfaring og programkode.

Hvis denne sammenhengen bare finnes i hodet på enkeltpersoner eller i gamle samtaler, blir både arbeidsprosess og programvare personavhengig.

Repoet skal derfor gjøre fagkunnskapen **eksplisitt, etterprøvbar og lett å lese for både mennesker og AI**.

## Formål

Repoet skal:

- dokumentere eksisterende praksis og historisk utvikling
- bevare detaljkunnskap, ikke bare overordnede sammendrag
- skille kilder/fakta fra vurderinger og beslutninger
- redusere person-, verktøy- og leverandøravhengighet
- gjøre samme fagkunnskap gjenbrukbar i flere implementasjoner
- danne faglig grunnlag for automatisering, først i Noark 5 Workflow Manager
- bidra til en enklere, mer automatisert og etterprøvbar arbeidsmodell for digitalt depot
- bygge videre på, gjenbruke og operasjonalisere arbeid fra relevante fagmiljøer, standarder, prosjekter og verktøy

Repoet er ikke i seg selv en vedtatt nasjonal standard. Det er en åpen kunnskaps- og utviklingsbase som kan vurderes og gjenbrukes av andre.

## Forholdet til andre initiativ

`digital-archive-workflow` er ikke ment å konkurrere med KDRS Prosesser og rutiner eller andre nasjonale, regionale eller lokale initiativ for digitalt depot.

Repoet er praktisk orientert og skal samle, strukturere, vurdere og anvende kunnskap fra eksisterende standarder, prosjekter, verktøy og fagmiljøer. Når andre initiativ utvikler bedre eller nyere praksis, skal dette kunne tas inn som grunnlag for videre utvikling her.

KDRS Prosesser og rutiner, inkludert pågående videreutvikling som fase 3 i 2026, er derfor en viktig faglig referanse og kilde – ikke en konkurrent.

Målet er å gjøre eksisterende og ny kunnskap lettere å omsette til praktiske, dokumenterte og automatiserbare arbeidsprosesser.

## Grunnprinsipp

> **Fagkravet skal kunne overleve verktøyet som implementerer det.**

Vi skiller derfor så langt som mulig mellom:

1. hva som faglig skal gjøres
2. hvorfor det skal gjøres
3. hvilke data/resultater som kreves
4. hvordan kontrollen kan automatiseres
5. hvilken konkret programvare som implementerer den

## Dokumentstatus

Dokumentene skal når det er relevant skille tydelig mellom:

- **KILDE / FAKTA** – hva eksisterende kilder faktisk sier eller viser
- **VÅR VURDERING** – analyse av eksisterende praksis
- **NY STANDARD / BESLUTTET** – eksplisitt besluttet retning
- **ÅPENT SPØRSMÅL** – ikke avklart

Historiske feil, nummereringsavvik eller uventede data i kildene skal ikke rettes i stillhet. De dokumenteres som kildeobservasjoner.

## Detaljnivå

Kunnskapsbasen har tre nivåer:

1. **Oversikt og syntese**
2. **Kildekartlegging**
3. **Tverrgående kartlegging**

Et generelt sammendrag alene er ikke nok til å unngå at kunnskapen må rekonstrueres senere.

## Struktur

- `docs/01-OVERSIKT.md`
- `docs/02-HISTORIKK.md`
- `docs/03-KILDER-OG-STATUS.md`
- `docs/04-REFERANSER.md`
- `docs/kilder/`
- `docs/prosess/`
- `docs/noark5/`
- `docs/ny-standard/`
- `docs/workflow-manager/`
- `docs/beslutninger/`

## Åpent repo og interne kilder

Internt eller upublisert materiale skal **ikke** kopieres inn i dette åpne repoet. Det kan registreres at en nyere kilde finnes og påvirker statusvurderingen når dette kan gjøres forsvarlig, men intern informasjon skal ikke publiseres uten avklaring.

## Arbeidsregel for ny standard

Vi automatiserer ikke gamle skjemaer og rutiner rad for rad.

Først identifiserer vi informasjonsmodellen, kontrollene, evidensen og beslutningene under dagens praksis. Deretter avgjør vi hva som skal videreføres, forenkles, automatiseres eller erstattes.

Samtidig gjelder et konservativt prinsipp: **En eksisterende kontroll fjernes ikke før vi kan forklare hva som erstatter den, eller hvorfor den ikke lenger er nødvendig.**
