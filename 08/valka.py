import random

def vytvor_balicek():
    """Vrátí nový zamíchaný balíček karet."""
    karty = []
    for barva in 'Sr', 'Pi', 'Ka', 'Kr':
        for hodnota in range(1, 14):
            karta = hodnota, barva
            karty.append(karta)
    random.shuffle(karty)
    return karty

def popis_kartu(karta):
    """Popíše danou kartu; vrací řetězec jako "7♣", "A♠" nebo "Q♥"."""
    hodnota, barva = karta
    if hodnota == 11:
        popis_hodnoty = 'J'
    elif hodnota == 12:
        popis_hodnoty = 'Q'
    elif hodnota == 13:
        popis_hodnoty = 'K'
    elif hodnota == 1:
        popis_hodnoty = 'A'
    elif hodnota == 10:
        # Aby byly všechny hodnoty jednopísmenné,
        # a líp se to pak vypisovalo,
        # desítku označíme římským číslem.
        popis_hodnoty = 'X'
    else:
        popis_hodnoty = str(hodnota)

    if barva == 'Sr':
        popis_barvy = '♥'
    elif barva == 'Pi':
        popis_barvy = '♠'
    elif barva == 'Ka':
        popis_barvy = '♦'
    else:
        popis_barvy = '♣'

    return popis_hodnoty + popis_barvy

def vypis_balicek():
    karty = vytvor_balicek()
    while karty:
        print(popis_kartu(karty.pop()))

def porovnej_karty(karta_a, karta_b):
    """Porovná hodnoty dvou karet.

    Vrací:
    * 'A', je-li lepší karta_a,
    * 'B', je-li lepší karta_b,
    * None, mají-li stejnou hodnotu.
    """
    hodnota_a, barva_a = karta_a
    hodnota_b, barva_b = karta_b
    if hodnota_a > hodnota_b:
        return 'A'
    elif hodnota_a < hodnota_b:
        return 'B'
    else:
        return None

def rozdej_balicky():
    """Rozdá trojici balíčků: dva pro hráče a jeden pro "stůl"

    Připraví zamíchaný balíček všech karet.
    Balíček pro hráče A bude jeho první polovina; balíček pro hráče B druhá
    """
    balicek = vytvor_balicek()

    # "polovina" musí být celé číslo, protože pak jí číslujeme seznam.
    # Proto celočíselné dělení. Zbytek po dělení ignorujeme.
    polovina = len(balicek) // 2

    balicek_a = balicek[:polovina]
    balicek_b = balicek[polovina:]

    return balicek_a, balicek_b, []

def vypis_rozdane_balicky():
    b_a, b_b, b_c = rozdej_balicky()
    print('Hráč A\t Hráč B')
    for a, b in zip(b_a, b_b):
        print(popis_kartu(a),'\t', popis_kartu(b))

def vyloz_karty(balicky):
    """Vyloží karty obou hráčů na stůl.

    "balicky" je trojice: balíček hráče A, balíček hráče B, karty na stole.

    Každý z hráčů vyloží poslední kartu svého balíčku na stůl.
    Nemá-li hráč co vyložit, nastane výjimka `SystemExit`.
    (To zjednodušuje zbytek hry.)

    Funkce vypisuje co dělá pomocí "print".
    (To taky zjednodušuje zbytek hry.)
    """
    balicek_a, balicek_b, na_stole = balicky
    try:
        karta_a = balicek_a.pop()
    except:
        raise SystemExit('Hráč B vyhrál')
    try:
        karta_b = balicek_b.pop()
    except:
        raise SystemExit('Hráč A vyhrál')
    print('Hráč A hraje kartu:', popis_kartu(karta_a))
    print('Hráč B hraje kartu:', popis_kartu(karta_b))
    na_stole.append(karta_a)
    na_stole.append(karta_b)

def valka():
    balicek_a, balicek_b, na_stole = rozdej_balicky()
    while True:
        vyloz_karty([balicek_a, balicek_b, na_stole])
        vysledek = porovnej_karty(na_stole[0], na_stole[1])
        while vysledek == None:
            print('Válka!')
            for i in range(3):
                vyloz_karty([balicek_a, balicek_b, na_stole])
            vysledek = porovnej_karty(na_stole[-2], na_stole[-1])
        if vysledek == 'A':
            print('Hráč A bere '+ str(len(na_stole)) + ' karty.')
            balicek_a.reverse()
            for i in range(len(na_stole)):
                balicek_a.append(na_stole[i])
            balicek_a.reverse()
        else:
            print('Hráč B bere '+ str(len(na_stole)) + ' karty.')
            balicek_b.reverse()
            for i in range(len(na_stole)):
                balicek_b.append(na_stole[i])
            balicek_b.reverse()
        na_stole.clear()
        print('Hráč A má '+ str(len(balicek_a)) + ' karet.')
        print('Hráč B má '+ str(len(balicek_b)) + ' karet.')
        print()
valka()