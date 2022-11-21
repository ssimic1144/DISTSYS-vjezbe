---
description: Distribuirani sustavi - 04
author: Srđan Daniel Simić
license: CC BY-SA
---

![](fipu.png){height=23%}

# Distribuirani sustavi - Vježbe 04 - Zadaci na satu

1. Kreiraj dva jednostavna web servisa.
Prvi se sastoji od jedne rute. (`"/getFact"`)
Šalje 20 zahtjeva na `https://catfact.ninja/fact`, rezultate
pojedinacno prosljeđuje drugom servisu kao JSON.
Vraća odgovore drugog servisa.
Drugi servis se također sastoji od jedne rute. (`"/saveFact"`)
Ako nema greške, sprema činjenicu u *temporary storage* ako je duljina 
činjenice veća od 100.
Vraća kao odgovor činjenicu  ili grešku.

2. Testirajte s Apache Benchmark response time i throughput

