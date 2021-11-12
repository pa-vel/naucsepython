from random import randrange

cislo = randrange(3)
if cislo == 0:
    tah_pocitace = 'kamen'
elif cislo == 1:
    tah_pocitace = 'nuzky'
else:
    tah_pocitace = 'papir'

tah_hrace = input('Zadej kamen, nuzky nebo papir: ')
while tah_hrace != 'konec':
    if tah_hrace == 'kamen':
        if tah_pocitace == 'kamen':
            print('remíza')
        elif tah_pocitace == 'nuzky':
            print('vyhrál jsi')
        else:
            print('prohrál jsi')
    elif tah_hrace == 'nuzky':
        if tah_pocitace == 'kamen':
            print('prohrál jsi')
        elif tah_pocitace == 'nuzky':
            print('remíza')
        else:
            print('vyhrál jsi')
    elif tah_hrace == 'papir':
        if tah_pocitace == 'kamen':
            print('vyhrál jsi')
        elif tah_pocitace == 'nuzky':
            print('prohrál jsi')
        else:
            print('remíza')
    else:
        print('Zkus to zadat znovu. Znám jen "kamen", "nuzky", "papir" a "konec"')
    print('Tah počítače byl:', tah_pocitace)
    cislo = randrange(3)
    if cislo == 0:
        tah_pocitace = 'kamen'
    elif cislo == 1:
        tah_pocitace = 'nuzky'
    else:
        tah_pocitace = 'papir'
    tah_hrace = input('Zadej kamen, nuzky nebo papir: ')

