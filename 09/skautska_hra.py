import random

def ziskej_odpovedi():
    odpovedi = {}
    otazky = ['Kdo?', 'S kým?', 'Co dělali?', 'Kde?', 'Kdy?','Proč?']
    for i in range(len(otazky)):
        odpoved = None
        odpovedi[otazky[i]] = []
        while odpoved != '':
            odpoved = input(otazky[i])
            if odpoved != '':
                odpovedi[otazky[i]].append(odpoved)
    return odpovedi

def vyber_odpovedi(odpovedi):
    vybrane_odpovedi = {}
    for klic, hodnoty in odpovedi.items():
        vybrane_odpovedi[klic] = random.choice(hodnoty)
    return vybrane_odpovedi

def vypis_vysledek(vybrane_odpovedi):
    odpoved = ''
    for hodnota in vybrane_odpovedi.values():
        odpoved = odpoved + hodnota + ' '
    print (odpoved)


vsechny_odpovedi = ziskej_odpovedi()
vybrane_odpovedi = vyber_odpovedi(vsechny_odpovedi)
vypis_vysledek(vybrane_odpovedi)