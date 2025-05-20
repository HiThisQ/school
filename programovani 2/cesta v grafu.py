graf = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

start = "A"
cil = "D"
memo = {}

def pocet_cest(v):
    if v == cil:
        return 1
    if v in memo:
        return memo[v]
    pocet = 0
    for soused in graf[v]:
        pocet += pocet_cest(soused)
        memo[v] = pocet
    return pocet

print(f"Počet cest z {start} do {cil} je:", pocet_cest(start))