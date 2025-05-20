n = int(input())
sachovnice = [list(input()) for _ in range (n)]

obsazene_sloupce = [False] * n
obsazena_rdiagonala = [False] * (2 * n -1)
obsazena_ldiagonala = [False] * (2  * n -1)

def kralovny(radek):
    pocet = 0
    if radek == n:
        return 1
    for sloupec in range(n):
        if sachovnice[radek][sloupec] == "." and not obsazene_sloupce[sloupec] and not obsazena_ldiagonala[sloupec - radek + n -1] and not obsazena_rdiagonala[sloupec + radek]:
            obsazene_sloupce[sloupec] = True
            obsazena_rdiagonala[sloupec + radek] = True
            obsazena_ldiagonala[sloupec - radek + n -1] = True
            pocet += kralovny(radek + 1)
            obsazene_sloupce[sloupec] = False
            obsazena_rdiagonala[sloupec + radek] = False
            obsazena_ldiagonala[sloupec - radek + n - 1] = False
    return(pocet)
vysledek = kralovny(0)
print(vysledek)

