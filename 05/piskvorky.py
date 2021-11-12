from ai import tah_pocitace
from util import tah

def vyhodnot(pole):
    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:
        return '!'
    else:
        return '-'

def tah_hrace(pole, symbol):
    """Zeptá se hráče na tah a vrátí nové herní pole

    'pole' je herní pole, na které se hraje.
    'symbol' může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    while True:
        pozice = input('Na které pole chceš hrát? Zadej 0 až 19. ')
        try:
            c_pozice = int(pozice)
            if c_pozice < 0 or c_pozice > 19:
                raise ValueError('Zadávej čísla od 0 do 19.')
            if pole[c_pozice] != '-':
                raise ValueError('Toto pole je obsazené.')
            return tah(pole, c_pozice, symbol)
        except ValueError:
            print('Zadávej jen čísla od 0 do 19 na neobsazená pole. ')

def piskvorky1d():
    pole = '-' * 20
    while True:
        pole = tah_hrace(pole, 'x')
        print('Stav po tahu hráče:', pole)
        if vyhodnot(pole) == 'x':
            print('Gratulujeme, vyhrál jsi!')
            break
        if vyhodnot(pole) == '!':
            print('Remíza!')
            break
        pole = tah_pocitace(pole, 'o')
        print('Stav po tahu počítače:', pole)
        if vyhodnot(pole) == 'o':
            print('Bohužel, vyhrál počítač!')
            break
        if vyhodnot(pole) == '!':
            print('Remíza!')
            break