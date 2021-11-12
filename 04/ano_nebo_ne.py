def ano_nebo_ne(otazka):
    """Vrátí True nebo False podle odpovědi uživatele"""
    while True:
        odpoved = input(otazka)
        odpoved = odpoved.strip()
        odpoved = odpoved.lower()
        if odpoved == 'ano' or odpoved == 'a':
            return True
        elif odpoved == 'ne' or odpoved == 'n':
            return False

        print('Nerozumím! Odpověz "ano" nebo "ne".')

# Příklad použití
if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')