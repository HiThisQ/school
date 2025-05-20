from collections import deque

pocet_prekazky = int(input())
prekazky = set()
for _ in range(pocet_prekazky):
    x,y = map(int, input().split())
    prekazky.add((x,y))

start = tuple(map(int, input().split()))
cil = tuple(map(int, input().split()))

def cesta_krale(start,cil):
    q = deque()
    navstiveno = set()
    q.append((start, [start]))
    navstiveno.add(start)

    while q:
        (i,j), cesta = q.popleft()
        if (i,j) == cil:
            return cesta
        for di, dj in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            ni, nj = i + di, j + dj
            if 1 <= ni <= 8 and 1 <= nj <= 8 and (ni,nj) not in navstiveno and (ni,nj) not in prekazky:
                navstiveno.add((ni, nj))
                q.append(((ni, nj), cesta + [(ni, nj)]))
    return -1

vysledek = cesta_krale(start, cil)
if vysledek == -1:
    print(-1)
else:
    for x,y in vysledek:
        print(*(x,y))
