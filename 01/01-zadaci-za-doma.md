---
description: Distribuirani sustavi - 01
author: Srđan Daniel Simić
license: CC BY-SA
---

![](fipu.png){height=23%}

# Distribuirani sustavi - Vježbe 01 - Zadaci za doma

1. Funkcija uzima listu string-ova.
Provjeri dal su sve stringovi, ako ne error.
Vraća novu listu, gdje su string-ovi duži od 4 znaka.
(Funkcija od dvije linije)

> Ispis: ["Pas", "Macka", "Stol"] -> ["Macka"]

2. Funkcija uzima listu i dictionary.
Provjeri jesu li lista i dictionary, ako ne error.
Provjeri imaju li isti broj elemenata.
Provjeri jesu li svi elementi liste tipa integer.
Vraća novi dictionary, gdje je *value* element iz liste na tom indexu ako se nalazi unutar [5,10]
ako ne upisuje -1.

> Ispis : [8,7,1], {1:2,2:1,3:2} -> {1: 8, 2: 7, 3: -1}

3. Funkcija uzima listu dictionary-a o artiklima.
Provjerava je li parametar lista, ak ne error.
Provjerava jesu li svi elementi dictionary, ako ne error.
Provjerava imaju li svi dictionary odgovarajuća 3 ključeva, ako ne error. ("cijena","naziv","kolicina")
(Moze i u dvije linije)
Vraća novi nested dictionary s ključem "ukupno" i dictionary sa ključem "artikli" i listom svih 
odabranih artikala te "cijena" s ukupnom cijenom računa.
(Ne treba biti One-liner)

> Ispis: [{"cijena":8,"naziv":"Kruh","kolicina":1}, {"cijena":13,"naziv":"Sok","kolicina":2}, {"cijena":7,"naziv":"Upaljac","kolicina":1}]
-> {'ukupno': {'artikli': ['Kruh', 'Sok', 'Upaljac'], 'cijena': 57}}

4. Funkcija prima dvije liste, provjerava dal su istih duljina, ako nisu raise-a Error.
Vraća novu listu uspoređujući elemente na istim indeksima.
Ako su vrijednosti iste, vraća taj element, ako nisu vraća -1 na toj poziciji.
(Funkcija mora imati dvije linije)

> Ispis: [1,2,3,4,5],[2,2,4,4,5] -> [-1, 2, -1, 4, 5]

5. Funkcija prima listu tuple-a o studentima (id, ime, prezime).
Vraća novu sortiranu po id-u (manji-\>veci) listu dictionary-a o studentima kojima ime i prezime počinje istim slovom.
(One-liner u return-u)

> Ispis : [(121,"Ivan","Ivic"),(431,"Pero","Horvat"),(31,"Marija","Maric")] -> [{'id': 31, 'ime': 'Marija', 'prezime': 'Maric'}, {'id': 121, 'ime': 'Ivan', 'prezime': 'Ivic'}]

6. Funkciji se predaju dva parametra.
Provjera se jesu li parametri istog tipa, ako ne error.
Provjeri se jesu li parametri liste ili dictionary, ako ne error.
Vraća se spojena lista ili dictionary.

> Ispis : [1,2,1,2],[3,2] -> [1,2,1,2,3,2]

> Ispis : {1:2,3:2},{5:2,4:1} -> {1: 2, 3: 2, 5: 2, 4: 1}

