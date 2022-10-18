---
description: Raspodijeljeni sustavi - 02
author: Srđan Daniel Simić
license: CC BY-SA
---

![](fipu.png){height=23%}

# Raspodijeljeni sustavi - Blic 01

1. Funkcija prima listu stringova predmeta.
Provjeri je li lista i jesu li svi stringovi, ako ne error.
Kreira dictionary gdje je *key* index, a *value* obrnuti string. 
(Mora biti One-liner u return-u)

> Ispis : ["Stol", "Stolica", "Krevet", "Fotelja"] -> {0: 'lotS', 1: 'acilotS', 2: 'teverK', 3: 'ajletoF'}

2. Funkcija prima dva jednostavna dictionary-a s ključevima valuta i cijene, gdje je lista vrijednost za *key*.
Provjeri je su li oba parametra dictionary, ako ne error.
Provjeri jesu li vrijednosti u oba dictionary-a liste, ako ne error.
Provjeri postoje li ključevi "valute" i "cijena", ako ne error.
Kreira novu listu tupla u kojoj se nalaze samo elementi koji se ponavljaju u oba na istim indexima te imaju istu vrijednost.
(Mora biti One-liner u return-u)

> Ispis : {"valute":["GBP","USD","CZK","Error"], "cijena":[8.5,7.7,0.3,10.3]}, {"valute":["EUR","USD","CZK","Error"], "cijena":[7.5,7.7,0.3,5.5]}
-> [(7.7, 'USD'), (0.3, 'CZK')]

3. Funkcija uzima listu dictionary-a proizvoda.
Provjeri je li lista i jesu li svi dictionary, ako ne error.
Proizvod ima naziv,kategoriju i ocjenu.
Vraća dictionary s kategorijom za *key* i sumom ocjena.
(Jedan ili dva One-Linera)

> Ispis : [{"naziv":"Burek","kategorija":"pite", "ocjena":1},{"naziv":"Ramsteak","kategorija":"steak", "ocjena":9},{"naziv":"Ribeye","kategorija":"steak", "ocjena":4},{"naziv":"Sirnica","kategorija":"pite", "ocjena":5}]
-> {'pite': 6, 'steak': 13}

