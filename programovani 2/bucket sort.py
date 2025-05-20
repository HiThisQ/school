from contextlib import suppress
def bucket_sort():
    cisla = []
    with suppress(EOFError):
        while True:
            radek = input()
            if radek == "":
                break
            cisla.append(int(radek))

    if not cisla:
        return

    max_hodnota = max(cisla)
    max_cifer = len(str(max_hodnota))

    for cifra in range(7):
        oddelovace = [[] for _ in range(10)]
        for cislo in cisla:
            hodnota_cifer = (cislo // (10 ** cifra)) % 10
            oddelovace[hodnota_cifer].append(cislo)

        cisla = [num for oddelovac in oddelovace for num in oddelovac]
        print(" ".join(map(str, cisla)))
bucket_sort()

