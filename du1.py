import math

zobrazeni = input('V jakém zobrazení chcete mapu tvořit? ')
meritko = float(input('Jaké byste si přáli měřítko? '))

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
        epsilon = r*math.log(math.cos(uhel/2)/math.sin(uhel/2))
    else:
        zobrazeni = input('Zobrazení nebylo zadáno správně.\n'
                          'Pro spravný průběh je potřeba vybrat z možnosti M, L, B, A.\n'
                          'Zkuste zadat zobrazení znovu: ')
        print(i)
        i -= 20
        print(i)
        continue


    rovnobezky += ("{:.1f}  ".format(epsilon))

print(rovnobezky)