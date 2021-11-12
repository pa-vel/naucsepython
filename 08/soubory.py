"""soubor = open('08/basnicka.txt', encoding='utf-8')
obsah = soubor.read()
soubor.close()"""

with open('08/basnicka.txt', encoding = 'utf-8') as soubor:
    for radek in soubor:
        radek = radek.rstrip()
        print(radek.upper())