---
description: Distribuirani sustavi - 03
author: Srđan Daniel Simić
license: CC BY-SA
---

![](fipu.png){height=23%}

# Distribuirani sustavi - Vježbe 03 - Zadaci na satu


1. Kreirajte dvije asinkrone funkcije te funkciju main.
Prva funkcija vraća listu dictionary-a u kojem se nalaze artikli. 

    [{"artikl":"Kava"},{"artikl":"Voda"}]

    Druga funkcija prima listu dictionary-a artikala, te svakom artiklu dodaje random cijenu u range-u od 1 do 10.
    Prvo provjeri radi li se o listi, te jesu li svi njeni elementi dictionary.
    Funkcija main poziva obije funkcije, te njenim zavrsetkom zavrsava i program.

2. Kreirajte tri asinkrone funkcije te funkciju main.
Prva funkcija uzima listu korisnika i provjeri radi li se o listi.
Ovisno o veličini liste, svakom korisniku dodijeli id po redu.
Potom vraća listu dictonary-a korisnika. 

    [{"korisnik":"Ivan","id":0},{"korisnik":"Pero","id":1}]

    Druga funkcija ispisuje brojeve od 1 do 10. Ceka 0.01 sekundu poslje svakog broja.
    Treća funkcija uzima listu dictonary-a korisnika i provjeri radi li se o listi i jesu li svi elemnti dictionary.
    Također provjerava postoje li ključevi korisnik i id.
    Čeka 0.05 sekundi.
    Kreira i nakraju vraća listu tuple-a korisnika gdje dodatno svakom korisniku izraćuna duljinu imena.

    [("Ivan",0,4), ("Pero",1,4)]

    Funkcija main prvo kreira listu imena korisnika i poziva redom funkcije, te zavrsetkom treće funkcije zavrsava i program.


