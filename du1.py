import math

#Výběr zobrazení uživatelem
zobrazeni = input('V jakém zobrazení chcete mapu tvořit? ')

#podmínka, která řeší špatně zadané zobrazení
if zobrazeni not in ['M','A','L','B']:
    print('Zobrazení nebylo zadáno správně a program byl ukončen')
    exit(0)


#try a except vytváří vyjímku pro případ, že bude špatně zadané měřítko a výpočet kvůli tomu v průběhu selže
try:
    meritko = float(input('Jaké byste si přáli měřítko? '))

    #podmínka, která řeší měřítko s hodnotou menší než nula
    if meritko <=0:
        print('Měřítko bylo zadáno chybně a program byl ukončen. Měřítko musí být vždy větší než nula.')
        exit(0)

    polomer = float(input('S jakým poloměrem země by mělo být počítáno? Zadávejte v kilometrech.\n'
                          '(V případě, že hodnotu neznáte, zadejte "0"): '))

    if polomer <0:
        print('Poloměr země byl zadán chybně a program byl ukončen. Poloměr musí být vždy větší než nula.')
        exit(0)

    #výpočet hodnot pro rovnoběžky pomocí for cyklu, který sám bere hodnoty od -90 do 90 stupňu z š
    if polomer == 0:
        r=637111000/meritko
    else:
        r=polomer*100000/meritko

    def vypocet_rovnobezky(zs):
        #přepočet úhlu na radiany
        uhel=zs/180*math.pi
        #výpočet pro Marinovo zobrazeni
        if zobrazeni == 'A':
            e = r*uhel
        #výpočet pro Lambertovo zobrazeni
        elif zobrazeni == 'L':
            e = r*math.sin(uhel)
        # výpočet pro Braunovo zobrazeni
        elif zobrazeni == 'B':
            e =2*r*math.tan(uhel/2)
        # výpočet pro Mercatorovo zobrazeni
        elif zobrazeni == 'M':
            #podmínka řešící hodnoty na poléch, kde se zobrazení táhne do nekonečna
            # a vypisující minus před hodnoty jižní šířky
            if abs(i) == 90:
                e = 101
            elif i < 0:
                uhelM = (90 / 180 * math.pi) - abs(uhel)
                e = -(r * math.log(math.cos(uhelM / 2) / math.sin(uhelM / 2)))
            else:
                uhelM = (90/180*math.pi)-abs(uhel)
                e = r*math.log(math.cos(uhelM/2)/math.sin(uhelM/2))
        return e

    rovnobezky = 'Rovnoběžky: '
    for i in range(-90,91,10):
        epsilon = vypocet_rovnobezky(i)
        #podmínka vypisující místo hodnot nad 100 cm spojovník
        if epsilon <=100 and epsilon >=-100:
            rovnobezky += ("{:.1f} ".format(epsilon))
        else:
            rovnobezky += '- '

    #výpočet hodnot pro poledníky - stejné pro všechna zobrazení
    def vypocet_poledniku(zd):
        uhel = zd / 180 * math.pi
        p = r * uhel
        return p


    poledniky = 'Poledniky: '
    for i in range(-180, 181, 10):
        ro = vypocet_poledniku(i)
        if ro <=100 and ro >=-100:
            poledniky += ("{:.1f} ".format(ro))
        else:
            poledniky += '- '

    #tvorba výstupu
    print(poledniky)
    print(rovnobezky)
except ValueError:
    print('Měřítko nebo poloměr Země byl zadán chybně a program byl ukončen. Pravděpodobně se nejednalo o číslo')
    exit(0)


print('\nPro výpočet přepočtených souřadnic bodů v daném zobrazení, zadávejte nyní ve stupních původní souřadnice.\n'
      'Pokud si přejete program ukončit, zadejte souřadnice 0,0')

try:
    x1 = float(input('Jaká je ZEMĚPISNÁ DÉLKA bodu? '))
    while not (x1>=-180 and x1<=180):
        print('Zeměpisná délka byla zadána chybně, zkuste to znovu.')
        x1 = float(input('Jaká je ZEMĚPISNÁ DÉLKA bodu? '))

    y1 = float(input('Jaká je ZEMĚPISNÁ ŠÍŘKA bodu? '))
    while not (y1>=-90 and y1<=90):
        print('Zeměpisná šířka byla zadána chybně, zkuste to znovu.')
        y1 = float(input('Jaká je ZEMĚPISNÁ ŠÍŘKA bodu? '))

    while not(x1==0 and y1==0):
        X = vypocet_poledniku(x1)
        Y = vypocet_rovnobezky(y1)
        souradnice = ("X = {:.1f}, Y = {:.1f}".format(X, Y))
        print(souradnice)
        x1 = float(input('Jaká je ZEMĚPISNÁ DÉLKA bodu? '))
        while not (x1 >= -180 and x1 <= 180):
            print('Zeměpisná délka byla zadána chybně, zkuste to znovu.')
            x1 = float(input('Jaká je ZEMĚPISNÁ DÉLKA bodu? '))

        y1 = float(input('Jaká je ZEMĚPISNÁ ŠÍŘKA bodu? '))
        while not (y1 >= -90 and y1 <= 90):
            print('Zeměpisná šířka byla zadána chybně, zkuste to znovu.')
            y1 = float(input('Jaká je ZEMĚPISNÁ ŠÍŘKA bodu? '))
except ValueError:
    print('Zeměpisná šířka či délka byla zadána zcela chybně a program byl ukončen. Pravděpodobně se nejednalo o číslo')
    exit(0)

from turtle import forward, left, right, shape, penup, pendown, speed

def zelva_Y():
    forward(posunY)
    right(90)
    pendown()
    forward(maxZD)
    penup()
    right(90)
    forward(2 * posunY)
    right(90)
    pendown()
    forward(maxZD)
    penup()
    right(90)
    forward(posunY)

def zelva_X():
    pendown()
    forward(maxZS)
    penup()
    left(90)
    forward(posunX)
    left(90)
    pendown()
    forward(maxZS)
    penup()
    right(90)
    forward(posunX)
    right(90)

shape('turtle')
speed(6)

if zobrazeni in ['A','L','B']:
    maxZD = 20*vypocet_poledniku(180)
    maxZS = 20*vypocet_rovnobezky(90)

    penup()
    left(90)
    for i in range(0, 91, 10):
        posunY = 10*(vypocet_rovnobezky(abs(i)))
        zelva_Y()

    forward(posunY)
    left(180)
    for i in range(18):
        posunX = 10*(vypocet_poledniku(10))
        zelva_X()
    pendown()
    forward(maxZS)

elif zobrazeni in ['M']:
    print('Je kreslen obraz pro Mercatorovo zobrazení. Nejsou zobrazeny póly – poslední rovnoběžkou je 80° z. š.')
    maxZD = 20 * vypocet_poledniku(180)
    maxZS = 20 * vypocet_rovnobezky(80)

    penup()
    left(90)
    for i in range(0, 81, 10):
        posunY = 10 * (vypocet_rovnobezky(abs(i)))
        zelva_Y()

    forward(posunY)
    left(180)
    for i in range(18):
        posunX = 10 * (vypocet_poledniku(10))
        zelva_X()
    pendown()
    forward(maxZS)