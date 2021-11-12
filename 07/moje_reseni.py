import random

def vytvor_seznam_zvirat():
    seznam_zvirat = ["pes", "kočka", "králík", "had"]
    return seznam_zvirat

def filtruj_kratka_jmena(retezce):
    kratka_jmena = []
    for i in retezce:
        if len(i) < 5:
            kratka_jmena.append(i)
    return kratka_jmena

def filtruj_k(retezce):
    zac_na_k = []
    for i in retezce:
        if i[0] == 'k':
            zac_na_k.append(i)
    return zac_na_k

def obsahuje(retezce, slovo):
    if slovo in retezce:
        return True
    else:
        return False

def bez_prvniho(retezce):
    bp = retezce[1:]
    return bp

def vytvor_balicek():
    balicek = []
    cisla = list(range(2, 10)) + list('JQKA')
    barvy = list('♥' '♦' '♠' '♣')
    for i in cisla:
        for j in barvy:
            balicek.append((i, j))
    random.shuffle(balicek)
    return balicek

def serad_od_druheho(retezce):
    klic_hodnota = []
    hodnota = []
    for i in retezce:
        klic_hodnota.append((i[1:], i))
    klic_hodnota.sort()
    for i in klic_hodnota:
        hodnota.append(i[1])
    return hodnota