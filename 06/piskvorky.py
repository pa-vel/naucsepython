from util import tah
from ai import tah_pocitace

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

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    while True:
        pozice = input('Zadej číslo pozice kam chceš hrát. Povolená čísla: 0 - 19: ')
        try:
            pozice_c = int(pozice)
            return tah(pole, pozice_c, symbol)
        except:
            print('Zadávej jen čísla od 0 do 19')

def piskvorky1d():
    pole = '-' * 20
    while True:
        pole = tah_hrace(pole, 'x')
        print('Stav hry:', pole)
        if vyhodnot(pole) == 'x':
            print('Gratuluji vyhrál jsi!')
            break
        elif vyhodnot(pole) == '!':
            print('Remíza!')
            break
        pole = tah_pocitace(pole, 'o')
        print('Stav hry:', pole)
        if vyhodnot(pole) == 'o':
            print('Vyhrál počítač!')
            break
        elif vyhodnot(pole) == '!':
            print('Remíza!')
            break
