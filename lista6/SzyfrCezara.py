def encrypted(tekst,klucz):
    alphabet = "abcdefghijkmnolpqrstuvwxyzabcdefghijkmnolpqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKMNOLPQRSTUVWXYZABCDEFGHIJKMNOLPQRSTUVWXYZ"
    lista =[]
    for i in range(0,len(tekst)):
        lista.append(tekst[i])
        try:
            a= alphabet.index(lista[i])
            lista[i] = alphabet[a+klucz]
        except:
                try:
                    a = ALPHABET.index(lista[i])
                    lista[i] = ALPHABET[a + klucz]
                except:
                    pass
    tekst = "".join(lista)
    return tekst
def decrypted(tekst,klucz):
    klucz = klucz*(-1)
    alphabet = "abcdefghijkmnolpqrstuvwxyzabcdefghijkmnolpqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKMNOLPQRSTUVWXYZABCDEFGHIJKMNOLPQRSTUVWXYZ"
    lista =[]
    for i in range(0,len(tekst)):
        lista.append(tekst[i])
        try:
            a= alphabet.index(lista[i])
            lista[i] = alphabet[a+klucz]
        except:
                try:
                    a = ALPHABET.index(lista[i])
                    lista[i] = ALPHABET[a + klucz]
                except:
                    pass
    tekst = "".join(lista)
    return tekst


