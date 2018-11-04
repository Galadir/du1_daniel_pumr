# Program na výpočet zobrazení
Tento program byl vytvořen v rámci domácího úkolu pro předmět 
Úvod do programování na Přírodovědecké fakulte Univerzity Karlovy.
Do zadání úkolu je možné nahlédnout zde: 
https://github.com/xtompok/uvod-do-prg/blob/master/du1/zadani.md

## Stručný popis programu
Program počítá polohu poledníků a rovnoběžek ve čtyřech válcových 
kartografických zobrazeních. Konkrétně program umí výpočty pro 
Marinovo, Lambertova, Braunovo a Mercatorovo zobrazení. 
Na základě uživatelem nadefinovaného měřítka a poloměru Země 
umí program vypsat polohu přepočítaných poledníků a rovnoběžek, 
vypsat souřadnice konkrétního zadaního bodu a dané zobrazení nakreslit.

## Funkce programu
Na začátek do programu uživatel zadá, pro které ze čtyř zobrazení, 
chce provádět výpočty. Dále se program uživatele zeptá na měřítko 
a na požadovaný poloměr referenční koule.Pokud uživatel zadá poloměr 
roven nule, je automaticky počítáno s hodnotou 6071,11.
### Výpis umístění rovnoběžek a poledníků
Nejprve program automaticky uživateli vypíše seznam vzdáleností na svislé ose, 
kde by měly být va daném měřítku a zobrazení vykresleny rovnoběžky 
a stejně tak pro poledníky vypíše všechny vzdálenosti na vodorovné ose.
### Výpočet souřadnic bodů 
Dále se program uživatele dotáže na konkrétní bod a po zadání souřadnic bodu 
ve stupních zeměpisné šířky či délky program vrátí souřadnice tohot bodu 
v zobrazení a měřítku zadaném na počátku.
Body je možné zadávat, dokud tuto funkci uživatel neukončí zadáním souřadnic 0,0
### Grafické znázornění zobrazení
Po skončení textové části programu se objeví okno, ve kterém je vybrané zobrazení
vykresleno.

## Fungování programu
Hlavním stavebním kamenem programu jsou funkce, které přepočítávájí souřadnice
rovnoběžek a poledníků pro všechna zobrazení na základě aktuálně zadaných hodnot. 
Tyto funkce jsou v různý formách a v rámci různých cyklů použity ve všech třech 
částech programu. 
Vstupy, které funkce využívá jsou vždy ošetřeny tak, aby se hodnoty,
které uživatel zadá, nacházely ve smyslupném intervalu a také v odpovídajícím
datovém typu. Pokud tomu tak není, program uživatele o problému informuje a ukončí se. 
Jediná vyjímka je u zadávání souřadnic bodů pro přepočet, kde program vyzve
uživatele k nápravě.
Pro grafické znázornění je využit modul Turtle, který umožňuje kresbu ve speciálním okne.
V rámci grafického znázonění figurují další dvě funkce, které určují pohyb želvy.
Tyto funkce pak figurují v cyklech, které zajišťují potřebný počet opakování.

