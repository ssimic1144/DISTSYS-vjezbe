---
description: Distribuirani sustavi - 04
author: Srđan Daniel Simić
license: CC BY-SA
---

![](fipu.png){height=23%}

# Distribuirani sustavi - Vježbe 04 - Zadaci za doma

1. Kreiraj tri web servisa.
Prvi se sastoji od jedne rute. (`/getActivity`)
Unutar 30 sekundi šalje pet puta po 8 zahtjeva na 
`https://www.boredapi.com
/api/activity`.
Rezultate prosljeđuje pojedinačno prosljeđuje drugom servisu.
Drugi servis se sastoji od jedne rute. (`/parseActivities`)
Unutar drugog servisa aktivnosti se filtriraju ovisno o `type`,
te se zatim prosljeđuju trećem servisu.
Charity i Recreational se šalju na posebnu rutu trećeg servisa 
(`/charityAndRecreational`), ostale se šalju na običnu rutu 
(`/otherActivities`).
Treći servis sprema svaku aktivnost i tip u *temporary storage*.
Ukoliko se radi o ruti `/otherActivities`, za svaku aktivnost 
šalje zahtjev na `https://randomuser.me/api/` od kojeg uzme 
ime, prezime i datum rođenja te pridoda ih kao nove ključeve
aktivnosti.
Ukoliko se radi o ruti `/charityAndRecreational`, ponovo šalje
zahtjev za svaku aktivnost na `https://randomuser.me/api/` 
ovoga puta uzimajući kordinate iz JSON-a koje se pridodaju kao 
novi ključevi aktivnosti.
Kad treći servis završi sa radom šalje odgovor `{"status":"success"}`,
ako i samo ako ne dođe do određene greške tijekom izvođenja.
U toj situaciju servis vraća JSON odgovor da zahtjev nije uspješno 
izvršen zajedno s greškom koja se dogodila.
Drugi servis prosljeđuje odgovor trećeg servisa.
Prvi servis vraća odgovor drugog servisa.
