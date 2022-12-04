---
description: Raspodijeljeni sustavi - 06
author: Srđan Daniel Simić
license: CC BY-SA
---

![](fipu.png){height=23%}

# Raspodijeljeni sustavi - Blic 02

Kreiraj 4 web servisa.
Prvi servis sastoji se od jedne rute (`/getJokes`).
Unutar te rute šalje se 6 puta po 2 zahtjeva na 
sljedeća dva URL-a : 
```
https://official-joke-api.appspot.com/random_joke

https://randomuser.me/api/
```
Nakon toga, proslijeđuje podatke o korisnicima drugom servisu,
a podatke o šalama trećem servisu.

Drugi servis sastoji se od jedne rute (`/filterUser`).
Unutar njega za svakog korisnika se uzme ime i prezime, grad i
email te se tako proslijeđuje 4. servisu.
JSON koji se šalje 4. servisu treba izgledati :
```json
{
        data:{
                user:{
                        name:"John Doe",
                        city:"New York City",
                        username:"johndoe123"
                    }
            }
    }
```

Treći servis sastoji se od jedne rute (`filterJoke`).
Unutar njega za svaku šalu uzme se setup i punchline te se
proslijeđuje 4. servisu.
JSON koji se šalje 4. serivisu treba izgledati :
```json
{
        data:{
                joke:{
                        setup:"What do you give a sick lemon?"
                        punchline:"Lemonaid."
                    }
            }
    }
```

Četvrti servis sastoji se od jedne rute (`/storeData`).
Unutar tog servisa nalaze se 2 "temporary storage-a" (liste),
jedna za korisnika jedna za šalu.
Svaki put kad servis zaprimi zahtjev provjerava radi li se o 
korisniku ili šali.
Prvo sprema podatake o korisniku/šali u "temporary storage".
Ukoliko se radi o korisniku, provjeri postoji li u "temporary 
storage-u" spremljena već šala.
Ako postoji sprema korisnika i šalu u bazu podataka (SQLite) te 
ih briše iz "temporary storage-a", provjeri broj 
upisanih redaka u tablici i vraća JSON odgovor.
JSON izgleda :
```json
{
        status:"OK",
        data:{
                numberOfRowsInTable:1
            }
    }
```
Ako ne vraća negativan odgovor.
JSON izgleda : 
```json
{
        status:"Failed",
        message:"Joke not present"
    }
```
Isto vrijedi ukoliko se radi o šali, samo u tom slučaju negativan
odgovor sadrži odgovarajuću poruku.

Tablica se sastoji od sljedećih atributa:

|id|name|city|username|setup|punchline|
|:--|:----|:----|:-----|:-----:|:---------|
|1|John Doe|New York City|johndoe123|What do you give a sick lemon?|Lemonaid.|


