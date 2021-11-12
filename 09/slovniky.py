def mocniny(n):
    m = {}
    for i in range(n):
        m[i+1] = (i+1) ** 2
    return m

def vypis_slovnik(slovnik):
    for klic, hodnota in slovnik.items():
        print(f'Klíč {klic}, hodnota {hodnota}')

def otoc_slovnik(slovnik):
    oslovnik = {}
    for klic, hodnota in slovnik.items():
        oslovnik[hodnota] = klic
    return oslovnik

def pocet_znaku(retezec):
    sl = {}
    for i in range(len(retezec)):
        sl[retezec[i]] = retezec.count(retezec[i])
    return sl

slovnik = {
'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ',
'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u',
'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n',
'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z', 'A': '∀', 'B': 'B',
'C': 'Ɔ', 'D': 'D', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': 'פ', 'H': 'H', 'I': 'I',
'J': 'ſ', 'K': 'ʞ', 'L': '˥', 'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ',
'Q': 'Q', 'R': 'R', 'S': 'S', 'T': '┴', 'U': '∩', 'V': 'Λ', 'W': 'M',
'X': 'X', 'Y': '⅄', 'Z': 'Z', '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ',
'4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8', '9': '6', ',': "'",
'.': '˙', '?': '¿', '!': '¡', '"': '„', "'": ',', '`': ',', '(': ')',
')': '(', '[': ']', ']': '[', '{': '}', '}': '{', '<': '>', '>': '<',
'&': '⅋', '_': '‾'
}

with open('08/basnicka.txt', encoding='utf-8') as basnicka:
    for radek in basnicka:
        radek_po_zpatku = list(radek.strip())
        radek_po_zpatku.reverse()
        for i in radek_po_zpatku:
            print(slovnik.get(i, i), end = '')
        print()