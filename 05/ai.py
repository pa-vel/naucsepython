from random import randrange

def tah_pocitace(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače

    'pole' je herní pole, na které se hraje.
    'symbol' může být 'x' nebo 'o', podle toho jestli počítač hraje za křížky
    nebo za kolečka.
    """
    while True:
        pozice = randrange(20)
        if pole[pozice] == '-':
            return pole[:pozice] + symbol + pole[pozice + 1:]