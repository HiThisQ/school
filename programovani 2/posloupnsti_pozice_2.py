N, M = map(int, input().split())
poslN = list(map(int, input().split()))
poslM = list(map(int, input().split()))

def spojeni(n, m):
    vysledek, pozice_N, pozice_M = [], [], []
    i, j, index = 0, 0, 1

    while i < len(n) or j < len(m):
        if j == len(m) or (i < len(n) and n[i] < m[j]):
            pozice_N.append(index)
            vysledek.append(n[i])
            i += 1
        else:
            pozice_M.append(index)
            vysledek.append(m[j])
            j += 1
        index += 1

    return pozice_N, pozice_M

vysledekN, vysledekM = spojeni(poslN, poslM)
print(*vysledekN)
print(*vysledekM)
