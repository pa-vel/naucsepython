from random import randrange
"""for i in range(5):
    for j in range(5):
        print('X', end=' ')
    print()

for i in range(5):
    for j in range(5):
        print(i*j, end=' ')
    print()"""

x = 15
y = 15

def nakresli_mapu(seznam_souradnic, jidlo_souradnic):
    for i in range(x):
        for j in range(y):
            if (i,j) in seznam_souradnic:
                print('X', end=' ')
            elif (i,j) in jidlo_souradnic:
                print('?', end=' ')
            else:
                print('.', end=' ')
        print()

def pohyb(seznam, smer, jidlo):
    i, j = seznam[-1]
    if smer == 's':
        i = i + 1
    elif smer == 'd':
        j = j + 1
    elif smer == 'w':
        i = i - 1
    elif smer == 'a':
        j = j - 1
    if i in range(x) and j in range(y):
        if (i,j) not in seznam:
            seznam.append((i,j))
            if (i,j) in jidlo:
                jidlo.remove((i,j))
                while True:
                    k = randrange(x)
                    l = randrange(y)
                    if (k,l) not in seznam + jidlo:
                        jidlo.append((k,l))
                        break
            else:
                del seznam[0]
        else:
            raise ValueError('Game over')
    else:
        raise ValueError('Game over')

seznam = [(0, 0), (0, 1), (0, 2), (0, 3)]
jidlo = [(2, 3), (4, 5), (6, 7)]
nakresli_mapu(seznam, jidlo)
while True:
    ss = input('Kam chceš hrát? w, s, d nebo a? Pro ukončení stiskni q ')
    if ss == 'q':
        break
    if ss not in ('w', 's', 'd', 'a'):
        print('Nerozumím, zkus to znovu: ')
    else:
        pohyb(seznam, ss, jidlo)
        nakresli_mapu(seznam, jidlo)