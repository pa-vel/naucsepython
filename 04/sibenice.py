from random import randrange

def zamen(pp_pismeno, pp_slovo, pp_stav):
    pp_pozice = -1
    # iteruj tolikrát, kolik je výskytů písmen pp_pismeno ve slově pp_slovo
    for i in range(pp_slovo.count(pp_pismeno)):
        pp_pozice = pp_slovo.index(pp_pismeno, pp_pozice + 1)
        pp_stav = pp_stav[:pp_pozice] + pp_pismeno + pp_stav[pp_pozice+1:]
    return pp_stav

seznam_slov = []
with open('08/slova.txt', encoding = 'utf-8') as soubor:
    for rslovo in soubor:
        seznam_slov.append(rslovo)

while True:
    nahoda = randrange(len(seznam_slov))
    slovo = seznam_slov[nahoda]
    slovo = slovo.rstrip()
    stav = '_' * len(slovo)
    neuspesne_pokusy = 0

    while True:
        pismeno = input('Zvol jedno písmeno:')
        if len(pismeno) == 1:
            if pismeno in slovo:
                stav = zamen(pismeno, slovo, stav)
            else:
                if pismeno.isalpha():
                    neuspesne_pokusy += 1
        else:
            print('Prosím zadej jen JEDNO písmeno!')
        print(stav)
        if '_' not in stav:
            print('Gratuluji, vyhrál jsi!')
            break
        print('Počet neúspěšných pokusů je:', neuspesne_pokusy)
        if neuspesne_pokusy >= 9:
            print('Bohužel jsi prohrál.')
            break
    if input('Chceš si zahrát znovu? Napiš ano nebo pro skončení napiš cokoli jiného.') != 'ano':
        break
