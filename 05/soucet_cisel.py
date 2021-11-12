def zadani_cisla(hlaska):
    while True:
        try:
            return int(input(hlaska))
        except ValueError:
            print('To nebylo číslo. Zkus to znovu.')

def vysledek(pc,dc, o):
        try:
            if o == "+":
                return pc + dc
            elif o == "-":
                return pc - dc
            elif o == "*":
                return pc * dc
            elif o == "/":
                return pc/dc
        except ZeroDivisionError:
            print('Nulou nelze dělit.')


prvni_cislo = zadani_cisla('Zadej první číslo: ')
druhe_cislo = zadani_cisla('Zadej druhé číslo: ')
while True:
    operace = input('Zadej typ operace "+", "-", "*" nebo "/" ')
    if operace not in ("+", "-", "*", "/"):
        print('Nerozumím zadané operaci:', operace, '. Zkus to znovu.')
    else:
        break
if vysledek(prvni_cislo, druhe_cislo, operace) != None:
    print(prvni_cislo, operace, druhe_cislo, "=", vysledek(prvni_cislo, druhe_cislo, operace))