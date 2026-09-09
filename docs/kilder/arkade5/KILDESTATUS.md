# Kildestatus for Arkade 5 Noark 5-testdokumentasjon

## Dokumentert kildegrunnlag

Repository: `nasjonalarkivet/arkade5`  
Standardgren: `master`  
Kode-snapshot brukt i første kartlegging: `40a32ee0ae84ddf44d1f3c35f1860567ca262733`

Denne commit-SHA-en kommer fra GitHub sin indekserte kildekodevisning som ble brukt ved kartleggingen. Direkte GitHub API-lesing av enkelte `nasjonalarkivet`-ressurser var blokkert av organisasjonens IP allow list i arbeidsmiljøet, derfor skal SHA-en behandles som det eksplisitte kode-snapshotet vi faktisk har analysert – ikke som en påstand om at det er nyeste commit på `master`.

Senere oppdateringer skal:

1. etablere ny konkret commit-SHA
2. sammenligne denne med dokumentert snapshot
3. finne hvilke Noark 5-testfiler som er endret
4. oppdatere bare berørt dokumentasjon
5. registrere nytt snapshot her

## Sentrale kodeplasseringer

- Testimplementasjoner:  
  `src/Arkivverket.Arkade.Core/Testing/Noark5/`
- Kobling test-ID → testklasse:  
  `src/Arkivverket.Arkade.Core/Base/Noark5/Noark5TestFactory.cs`
- Enhetstester:  
  `src/Arkivverket.Arkade.Core.Tests/Testing/Noark5/`

## Offentlige innganger

- https://github.com/nasjonalarkivet/arkade5
- https://github.com/nasjonalarkivet/arkade5/tree/master/src/Arkivverket.Arkade.Core/Testing/Noark5
- https://github.com/nasjonalarkivet/arkade5/blob/master/src/Arkivverket.Arkade.Core/Base/Noark5/Noark5TestFactory.cs
- https://docs.arkade.nasjonalarkivet.no/no/latest/Systemdokumentasjon.html#noark-5

## Oppdateringsprinsipp

Dokumentasjonen skal være etterprøvbar mot en bestemt kildekodeversjon. Flytende lenker til `master` brukes som navigasjon, mens dokumentert faglig innhold skal knyttes til en konkret commit.
