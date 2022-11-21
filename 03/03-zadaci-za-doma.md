---
description: Distribuirani sustavi - 03
author: Srđan Daniel Simić
license: CC BY-SA
---

![](fipu.png){height=23%}

# Distribuirani sustavi - Vježbe 03 - Zadaci za doma

1. Kreirajte jednu asinkronu (**afun1**) i jednu sinkronu (**fun2**) funkciju, te funkciju main.
Unutar funkcije main, kreiraju se tri datoteke u radnom direktoriju te se nazivi spremaju u listu.

   ["datoteka1", "datoteka2", "datoteka3"]  

   Nakon toga poziva se **afun1** koja uzima parametar lista naziva datoteka.
   Čeka 0.2 sekunde i vraća listu dictionary-a, gdje svaki dictonary sadrži naziv datoteke te njenu veličinu u byte-ovima.

    [{"naziv":"datoteka1", "velicina":1212},{"naziv":"datoteka2", "velicina":8912},{"naziv":"datoteka3", "velicina":2212}]

   Odmah nakon **afun1**, unutar main-a poziva se **fun2** koja prima listu naziva datoteka.
   Unutar nje, u svaku datoteku upisuje brojeve od 1 do 10 000.
   Na kraju main-a čeka se rezultat iz **afun1** koji se ispisuje u konzolu.

    (Hint: os package)


2. Kreirajte dvije asinkrone funkcije (**afunc1, afunc2**) i funkciju main.
Unutar funkcije main pozivaju se obje funkcije jedna za drugom.
**Afunc1** kreira 10 Normalnih distribucija s 1M sample-ova i nakon svake čeka 0.9 sekundi.
**Afunc2** prati iskorištenost CPU-a u vremenskom razmaku od 10 sekundi. 
Na kraju funkcije main, čeka se rezultat **afunc2** te se u konzolu ispisuje iskorištenost CPU-a. 

    (Hint: numpy, psutils package)

> Iskorištenost CPU u 10 sekundi iznosi : 3.8

