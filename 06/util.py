def tah(pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici

    `pole` je herní pole, na které se hraje.
    `pozice` je číslo políčka. Čísluje se od nuly.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka.
    """
    if pozice < 0 or pozice > 19:
        raise ValueError('Zadávej jen čísla od 0 do 19!')
    if pole[pozice] != '-':
        raise ValueError('Tato pozice je obsazená!')
    if symbol not in ('x', 'o'):
        raise ValueError('')
    return pole[:pozice]+symbol+pole[pozice+1:]
