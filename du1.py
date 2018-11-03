import math

#Výběr zobrazení uživatelem
zobrazeni = input('V jakém zobrazení chcete mapu tvořit? ')

#podmínka, která řeší špatně zadané zobrazení
if zobrazeni not in ['M','A','L','B']:
    print('Zobrazení nebylo zadáno správně a program byl ukončen')
else:
    #try a except vytváří vyjímku pro případ, že bude špatně zadané měřítko a výpočet kvůli tomu v průběhu selže
    try:
        meritko = float(input('Jaké byste si přáli měřítko? '))

        polomer = float(input('S jakým poloměrem země by mělo být počítáno? Zadávejte v kilometrech.\n'
                              '(V případě, že hodnotu neznáte, zadejte "0"): '))

        #podmínka, která řeší měřítko s hodnotou menší než nula
        if meritko <=0:
            print('Měřítko bylo zadáno chybně a program byl ukončen. Měřítko musí být vždy větší než nula.')
        elif polomer <0:
            print('Poloměr země byl zadán chybně a program byl ukončen. Poloměr musí být vždy větší než nula.')

        #výpočet hodnot pro rovnoběžky pomocí for cyklu, který sám bere hodnoty od -90 do 90 stupňu z š
        else:
            if polomer == 0:
                r=637111000/meritko
            else:
                r=polomer*100000/meritko

            rovnobezky = 'Rovnoběžky: '
            for i in range(-90,91,10):
                #přepočet úhlu na radiany
                uhel=i/180*math.pi
                #výpočet pro Marinovo zobrazeni
                if zobrazeni == 'A':
                    epsilon = r*uhel
                #výpočet pro Lambertovo zobrazeni
                elif zobrazeni == 'L':
                    epsilon = r*math.sin(uhel)
                # výpočet pro Braunovo zobrazeni
                elif zobrazeni == 'B':
                    epsilon =2*r*math.tan(uhel/2)
                # výpočet pro Mercatorovo zobrazeni
                elif zobrazeni == 'M':
                    #podmínka řešící hodnoty na poléch, kde se zobrazení táhne do nekonečna
                    # a vypisující minus před hodnoty jižní šířky
                    if abs(i) == 90:
                        epsilon = 101
                    elif i < 0:
                        uhelM = (90 / 180 * math.pi) - abs(uhel)
                        epsilon = -(r * math.log(math.cos(uhelM / 2) / math.sin(uhelM / 2)))
                    else:
                        uhelM = (90/180*math.pi)-abs(uhel)
                        epsilon = r*math.log(math.cos(uhelM/2)/math.sin(uhelM/2))
                #podmínka vypisující místo hodnot nad 100 cm spojovník
                if epsilon <=100 and epsilon >=-100:
                    rovnobezky += ("{:.1f} ".format(epsilon))
                else:
                    rovnobezky += '- '

            #výpočet hodnot pro poledníky - stejné pro všechna zobrazení
            poledniky = 'Poledniky: '
            for i in range(-180, 181, 10):
                uhel = i / 180 * math.pi
                ro = r * uhel
                if ro <=100 and ro >=-100:
                    poledniky += ("{:.1f} ".format(ro))
                else:
                    poledniky += '- '

            #tvorba výstupu
            print(poledniky)
            print(rovnobezky)
    except ValueError:
        print('Měřítko nebo poloměr Země byl zadán chybně a program byl ukončen. Pravděpodobně se nejednalo o číslo')