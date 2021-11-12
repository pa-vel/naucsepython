def secti(a, b):
    return a + b
def odecti(a, b):
    return a - b
def vynasob(a, b):
    return a * b
def podel(a, b):
    return a / b

slovnik_operaci = {
    '+': secti,
    '-': odecti,
    '*': vynasob,
    '/': podel,
}
pcislo = input('První číslo: ')
dcislo = input('Druhé číslo: ')
operace = input('Operace: ')
print(f'{pcislo} {operace} {dcislo} = {slovnik_operaci[operace](int(pcislo),int(dcislo))}')
