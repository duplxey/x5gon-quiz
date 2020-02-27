# x5gon-quiz
Moj projekt za Inovacijski IT-šprint Pošte Slovenije, ki je potekal 23. in 24. januarja 2020.  
Spletna stran dogodka: <https://postartup.si/sprint-poste-slovenije-2020/>

## Problem
- x5gon ne pridobiva dovolj relevantnih vsebin
- Branje še ne pomeni učenje

## Uporabljena tehnologija
- Python 3.7.5
- Django 3.0.2
- MySQL 5.7.6
- X5GON API (<https://platform.x5gon.org/products/feed/>)
- Quillionz (<https://www.quillionz.com/>)

## Ciljna skupina
- Študenti
- Dijaki
- Vsi uporabniki x5gon platforme

## Rešitev
- Iskanje vsebin (x5gon)
- Ocenjevanje vsebin
- Sestavljanje kvizov
- Ocenjevanje in primerjanje rezultatov drugih uporabnikov (točkovni sistem, lestvica)

## Postopek rešitve
1. Uporabnik preko wrapper-ja poišče x5gon vsebine, ki bi se jih rad naučil.
1. Uporabnik se nato vsebine nauči/predela.
1. Po predelani vsebini se uporabniku zastavi vprašalnik (kviz), da preverimo njegovo dejansko znanje in razumevanje.
1. Kviz se ovrednoti, uporabnik pa vidi kako se je odrezal glede na ostale uporabnike.

## Izboljšave/neimplementirane rešitve
- Kreiranje kvizov z ML in NLP.
- Localisation, translation.

## Demo (projekt v akciji)
PPTX: https://drive.google.com/file/d/1lnynzDnLxGxKhSXl8JgUd_G--IXHsI_O/view  
Demo (slike): <https://github.com/duplxey/x5quiz/wiki/Demo-(preview)>
