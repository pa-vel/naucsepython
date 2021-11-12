def muz_zena(prijmeni):
    if prijmeni[-1] == 'á':
        pohlavi = 'zena'
    else:
        pohlavi = 'muz'
    return pohlavi

print(muz_zena('Nováková'))
print(muz_zena('Svoboda'))
print(muz_zena('Issová'))