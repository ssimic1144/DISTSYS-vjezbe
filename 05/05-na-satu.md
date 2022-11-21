---
description: Distribuirani sustavi - 05
author: Srđan Daniel Simić
license: CC BY-SA
---

![](fipu.png){height=23%}

# Distribuirani sustavi - Vježbe 05 - Zadaci na satu

1. Kreiraj dva web servisa.
Prvi se sastoji od jedne rute. (`/getActivity`)
Unutar 30 sekundi šalje pet puta po 8 zahtjeva na 
`https://www.boredapi.com
/api/activity`.
Rezultate prosljeđuje pojedinačno prosljeđuje drugom servisu.
Drugi servis se sastoji od jedne rute. (`/saveActivities`)
Unutar drugog servisa aktivnosti se filtriraju ovisno o `type`,
te se spremaju Charity i Recreational.
Koristi SQLite bazu.
Prvi servis vraća odgovor drugog servisa.
