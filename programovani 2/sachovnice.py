n = int(input())
sachovnice = [list(input()) for _ in range(n)]

obsazene_sloupce = [False] * n

def veze(radek):
    pocet = 0
    if radek == n:
        return 1
    for sloupec in range(n):
        if sachovnice[radek][sloupec] == '.' and not obsazene_sloupce[sloupec]:
            obsazene_sloupce[sloupec] = True
            pocet += veze(radek + 1)
            obsazene_sloupce[sloupec] = False
    return pocet

vysledek = veze(0)
print(vysledek)



                

