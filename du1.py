import math

zobrazeni = input('V jakém zobrazení chcete mapu tvořit? ')

if zobrazeni not in ['M','A','L','B']:
    print('Zobrazení nebylo zadáno správně a program byl ukončen')
else:
    try:
        meritko = float(input('Jaké byste si přáli měřítko? '))

        if meritko <0:
            print('Měřítko bylo zadáno chybně a program byl ukončen. Měřítko musí být vždy větší než nula.')
        else:
            r=637111000/meritko
            rovnobezky = 'Rovnoběžky: '
            for i in range(-90,91,10):
                uhel=i/180*math.pi
                if zobrazeni == 'A':
                    epsilon = r*uhel
                elif zobrazeni == 'L':
                    epsilon = r*math.sin(uhel)
                elif zobrazeni == 'B':
                    epsilon =2*r*math.tan(uhel/2)
                elif zobrazeni == 'M':
                    if abs(i) == 90:
                        epsilon = 101
                    elif i < 0:
                        uhelM = (90 / 180 * math.pi) - abs(uhel)
                        epsilon = -(r * math.log(math.cos(uhelM / 2) / math.sin(uhelM / 2)))
                    else:
                        uhelM = (90/180*math.pi)-abs(uhel)
                        epsilon = r*math.log(math.cos(uhelM/2)/math.sin(uhelM/2))
                if epsilon <=100 and epsilon >=-100:
                    rovnobezky += ("{:.1f} ".format(epsilon))
                else:
                    rovnobezky += '- '

            poledniky = 'Poledniky: '
            for i in range(-180, 181, 10):
                uhel = i / 180 * math.pi
                ro = r * uhel
                if ro <=100 and ro >=-100:
                    poledniky += ("{:.1f} ".format(ro))
                else:
                    poledniky += '- '

            print(poledniky)
            print(rovnobezky)
    except ValueError:
        print('Měřítko bylo zadáno chybně a program byl ukončen. Pravděpodobně se nejednalo o číslo')