from random import randrange

aktualni_hod = 0
pocet_pokusu = 0
vitezny_pocet_pokusu = 0
vitezny_hrac = 0
i = 0
for i in range(4):
    while aktualni_hod < 6:
        aktualni_hod = randrange(1, 7)
        pocet_pokusu = pocet_pokusu + 1
        print('Hráč', i + 1, 'hodil', aktualni_hod, 'pokusem č.', pocet_pokusu)
    if pocet_pokusu > vitezny_pocet_pokusu:
        vitezny_hrac = i + 1
        vitezny_pocet_pokusu = pocet_pokusu
    aktualni_hod = 0
    pocet_pokusu = 0
print('Vyhrál hráč číslo', vitezny_hrac, 's celkovým počtem pokusů:', vitezny_pocet_pokusu )