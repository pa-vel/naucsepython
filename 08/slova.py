slova = []
with open('08/index.dic', encoding = 'utf-8') as soubor:
    for c_radku, radek in enumerate(soubor):
        if c_radku > 0:
            radek = radek.rstrip()
            if '/' in radek:
                l_radek = radek.split('/')
                slova.append(l_radek[0])
            else:
                slova.append(radek)
with open('08/slova.txt', encoding = 'utf-8', mode = 'w') as soubor:
    slova.reverse()
    while slova:
        slovo = slova.pop()
        print(slovo, file=soubor)
