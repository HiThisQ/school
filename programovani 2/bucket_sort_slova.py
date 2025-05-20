from contextlib import suppress
def serad_slova(slova, pozice=0):
    if len(slova) <= 1:
        return slova
    oddelovace = {}
    kratsi_slova = []

    for slovo in slova:
        if pozice < len(slovo):
            znak = slovo[pozice]
            if znak not in oddelovace:
                oddelovace[znak] = []
            oddelovace[znak].append(slovo)
        else:
            kratsi_slova.append(slovo)

    serazeny_seznam = kratsi_slova
    klice = list(oddelovace.keys())
    for i in range(len(klice)):
        for j in range(i + 1, len(klice)):
            if ord(klice[i]) > ord(klice[j]):
                klice[i], klice[j] = klice[j], klice[i]
    for znak in klice:
        serazeny_seznam.extend(serad_slova(oddelovace[znak], pozice + 1))

    return serazeny_seznam

def bucket_sort_slova():
    seznam_slova = []
    with suppress(EOFError):
        while True:
            radek = input().strip()
            if radek == "-end-":
                break
            seznam_slova.append(radek)

    serazeny_vysledek = serad_slova(seznam_slova)
    for slovo in serazeny_vysledek:
        print(slovo)
    print("-end-")


bucket_sort_slova()
