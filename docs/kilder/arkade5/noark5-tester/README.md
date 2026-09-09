# Arkade 5 – Noark 5-tester

## Formål

Denne dokumentasjonsserien skal beskrive **hva Arkade 5 sine Noark 5-tester faktisk gjør**, basert på den åpne kildekoden.

Dette er ment som faglig dokumentasjon for arkivmiljøet og som et etterprøvbart grunnlag for sammenligning med historiske Noark 5-tester, KDRS Query/XPath, U1/U2 og nye implementasjoner.

## Kilder

- Aktuell testliste: https://docs.arkade.nasjonalarkivet.no/no/latest/Systemdokumentasjon.html#noark-5
- Arkade 5: https://github.com/nasjonalarkivet/arkade5
- Testimplementasjoner: https://github.com/nasjonalarkivet/arkade5/tree/master/src/Arkivverket.Arkade.Core/Testing/Noark5
- Test factory: https://github.com/nasjonalarkivet/arkade5/blob/master/src/Arkivverket.Arkade.Core/Base/Noark5/Noark5TestFactory.cs
- Arkade 5 dokumentasjon: https://github.com/nasjonalarkivet/arkade5-dokumentasjon

## Dokumentasjonsmodell per test

For hver `N5.xx` skal vi så langt kildekoden gir grunnlag for det dokumentere:

1. test-ID og Arkade-navn
2. faglig hensikt
3. hvilke filer eller Noark 5-elementer testen leser
4. hvilken Arkade-klasse som implementerer testen
5. sentral testlogikk forklart i vanlig språk
6. hva testen teller, kontrollerer eller sammenligner
7. hvilke resultater, feil eller avvik den kan rapportere
8. forutsetninger og avhengigheter
9. kobling til historisk Noark 5-testopplegg
10. kobling til KDRS Query/XPath
11. kobling til U1/U2 der relevant
12. direkte lenke til implementasjonen i Arkade 5

## Status

Selve detaljkartleggingen test for test starter i neste dokumentasjonsrunde. Denne filen etablerer struktur, kildegrunnlag og dokumentasjonskrav.

Vi skal ikke gjette hvordan en test virker ut fra testnavnet alene. Beskrivelsen skal bygge på den faktiske implementasjonen og andre eksplisitte kilder.
