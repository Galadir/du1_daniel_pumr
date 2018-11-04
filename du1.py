#import modulu math, který poslouží při počítání převedených souřadnic
import math


#výběr zobrazení uživatelem
print('Pro výběr zobrazení vypište níže jednu z následujících možností:\n'
      'L - Lambertovo zobrazení\n'
      'A - Marinovo zobrazení\n'
      'B - Braunovo zobrazení\n'
      'M - Mercatorovo zobrazení\n')
zobrazeni = input('Zobrazení: ')

#podmínka, která řeší špatně zadané zobrazení
if zobrazeni not in ['M','A','L','B']:
    print('Zobrazení bylo zadáno chybně a program byl ukončen.')
    exit(0)

#try a except vytváří vyjímku pro případ, že bude špatně zadané měřítko a výpočet kvůli tomu v průběhu selže
try:
    #zadání měřítka uživatelem
    print('\nDále můžete zadat měřítko, ve kterém bude zobrazení vytvořeno.\n'
          'Měřítko zadejte jako číslo x, které bude odpovídat měřítku 1:x\n ')
    meritko = float(input('Měřítko: '))

    #podmínka, která v případě, že meritko bylo zadáno menší než 0, ukončuje program
    if meritko <=0:
        print('Měřítko bylo zadáno chybně a program byl ukončen. Měřítko musí být vždy větší než nula.')
        exit(0)

    #zadání poloměru Země uživatelem
    print('\nNakonec můžete zvolit poloměr referenční koule, se kterou bude počítáno.\n'
          'Hodnotu zadávejte v kilometrech. Pokud poloměr neznáte, zadejte "0"\n')
    polomer = float(input('Poloměr: '))

    # podmínka, která v případě, že poloměr byl zadán menší než 0, ukončuje program
    if polomer <0:
        print('Poloměr země byl zadán chybně a program byl ukončen. Poloměr musí být vždy větší než nula.')
        exit(0)

    #přepočet poloměru do daného měřítka
    if polomer == 0:
        r=637111000/meritko
    else:
        r=polomer*100000/meritko


    def vypocet_rovnobezky(zs):
        """
        Funkce počítá vzdálenost určité přepočtené rovnoběžky od rovníku na základě zadané zeměpisné šířky
        Zbylé proměnné bere z programu podle toho, jak byly dříve definovány.
        :param zs: zeměpisná šířka ve stupních
        :return: vzdálenost přepočtené rovnoběžky od rovníku
        """
        #přepočet úhlu na radiany
        uhel = zs/180*math.pi
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
            # podmínka řešící hodnoty na pólech a záporné hodnoty, které logaritmus nezpracuje
            # na póly je natvrdo vypsaná vzdálenost 101 cm, která se bude dále zobrazovat jako pomlčka
            if abs(i) == 90:
                e = 101
            elif i < 0:
                uhelM = (90 / 180 * math.pi) - abs(uhel)
                e = -(r * math.log(math.cos(uhelM / 2) / math.sin(uhelM / 2)))
            else:
                uhelM = (90/180*math.pi)-abs(uhel)
                e = r*math.log(math.cos(uhelM/2)/math.sin(uhelM/2))
        return e

    #výpočet hodnot pro rovnoběžky
    rovnobezky = 'Rovnoběžky: '
    for i in range(-90,91,10):
        epsilon = vypocet_rovnobezky(i)
        #připsání hodnoty do seznamu, místo hodnoat na 100 cm spojovník
        if epsilon <=100 and epsilon >=-100:
            rovnobezky += ("{:.1f} ".format(epsilon))
        else:
            rovnobezky += '- '

    def vypocet_poledniku(zd):
        """
        Funkce počítá vzdálenost určitého přepočteného poledníku na základě zadané zeměpisné délky
        Zbylé proměnné bere z programu podle toho, jak byly dříve definovány.
        Pro všechna zobrazení je výpočet stekjný
        :param zd: zeměpisná délka ve stupních
        :return: vzdálenost přepočteného poledníku od greenwiche
        """
        uhel = zd / 180 * math.pi
        p = r * uhel
        return p

    #výpočet konkrétních hodnot pro poledníky
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
    print('Měřítko nebo poloměr Země byly zadán chybně a program byl ukončen. Pravděpodobně se nejednalo o číslo.')
    exit(0)


print('\nPro výpočet přepočtených souřadnic bodů v daném zobrazení, zadávejte nyní ve stupních původní souřadnice.\n'
      'Pokud si přejete program ukončit, zadejte souřadnice "0,0"\n')

#try a except vytváří vyjímku pro případ, že budou souřadnice zadané zcela špatně
try:
    #úvodní výpočet souřadnic včetně cyklu nabízejícího opravu při špatných číslech
    x1 = float(input('Jaká je ZEMĚPISNÁ DÉLKA bodu? '))
    while not (x1>=-180 and x1<=180):
        print('Zeměpisná délka byla zadána chybně, zkuste to znovu.')
        x1 = float(input('Jaká je ZEMĚPISNÁ DÉLKA bodu? '))

    y1 = float(input('Jaká je ZEMĚPISNÁ ŠÍŘKA bodu? '))
    while not (y1>=-90 and y1<=90):
        print('Zeměpisná šířka byla zadána chybně, zkuste to znovu.')
        y1 = float(input('Jaká je ZEMĚPISNÁ ŠÍŘKA bodu? '))

    #cyklus umožňující zadávat souřadnice, dokut nebudou zadány hodnoty 0,0
    while not(x1==0 and y1==0):
        X = vypocet_poledniku(x1)
        Y = vypocet_rovnobezky(y1)
        souradnice = ("\nX = {:.1f}, Y = {:.1f}".format(X, Y))
        print(souradnice)
        x1 = float(input('\nJaká je ZEMĚPISNÁ DÉLKA bodu? '))
        while not (x1 >= -180 and x1 <= 180):
            print('Zeměpisná délka byla zadána chybně, zkuste to znovu.')
            x1 = float(input('Jaká je ZEMĚPISNÁ DÉLKA bodu? '))

        y1 = float(input('Jaká je ZEMĚPISNÁ ŠÍŘKA bodu? '))
        while not (y1 >= -90 and y1 <= 90):
            print('Zeměpisná šířka byla zadána chybně, zkuste to znovu.')
            y1 = float(input('Jaká je ZEMĚPISNÁ ŠÍŘKA bodu? '))
except ValueError:
    print('Zeměpisná šířka či délka byla zadána zcela chybně a program byl ukončen. Pravděpodobně se nejednalo o číslo.')
    exit(0)

#import knihovny turtle pro grafické vykreslení zobrazení
from turtle import forward, left, right, shape, penup, pendown, speed, setpos

def zelva_Y():
    """
    Fukce vykreslující rovnoběžky pomocí modulu turtle
    :return: 
    """
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
    """
    Fukce vykreslující poledníky pomocí modulu turtle
    :return: 
    """
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

#nastavení pohybu v modulu turtle: tvar želva, střední rychlost, začátek více vlevo
shape('turtle')
speed(6)
penup()
setpos(-300,0)
pendown()

#vykreslení pro bezproblémová zobrazení
if zobrazeni in ['A','L','B']:
    #definování délky a šířky vykresleného zobrazení
    maxZD = 20*vypocet_poledniku(180)
    maxZS = 20*vypocet_rovnobezky(90)

    #vykreslení rovnoběžek
    penup()
    left(90)
    for i in range(0, 91, 10):
        posunY = 10*(vypocet_rovnobezky(abs(i)))
        zelva_Y()

    #vykreslení poledníků
    forward(posunY)
    left(180)
    for i in range(18):
        posunX = 10*(vypocet_poledniku(10))
        zelva_X()
    pendown()
    forward(maxZS)

#vykreslení pro Mercatorovo zobrazení, kde jsou vynechány póly, jinak je postup stejný
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