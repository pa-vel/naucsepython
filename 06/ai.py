from random import randrange

def tah_pocitace_old(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače

    'pole' je herní pole, na které se hraje.
    'symbol' může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    while True:
        if '-' not in pole:
            raise ValueError
        tah_p = randrange(20)
        try:
            if pole[tah_p] == '-':
                return pole[:tah_p] + symbol + pole[tah_p + 1:]
        except:
            raise ValueError

def tah_pocitace(pole, symbol):
    if '-' not in pole:
        raise ValueError
    pocet_vyskytu = pole.count(symbol)
    pi = -1
    for i in range(pocet_vyskytu):
        pi = pole.index(symbol, pi + 1)
        if pi not in (0, 19):
            if pole[pi - 1] == '-':
                return pole[:pi-1] + symbol + pole[pi:]
            elif pole[pi + 1] == '-':
                return pole[:pi + 1] + symbol + pole[pi + 2:]

    while True:
        tah_p = randrange(20)
        try:
            if pole[tah_p] == '-':
                return pole[:tah_p] + symbol + pole[tah_p + 1:]
        except:
            raise ValueError
