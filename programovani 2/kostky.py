from collections import deque
import copy
vstup = input()
start = [list(map(int, vstup[0:3])), list(map(int, vstup[3:6]))]
cil = [[1, 2, 3], [4, 5, 0]]

def nula(stav):
    for i in range(2):
        for j in range(3):
            if stav[i][j] == 0:
                return (i, j)

def sousede(stav):
    vysledky = []
    i0, j0 = nula(stav)

    for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        ni, nj = i0 + di, j0 + dj
        if 0 <= ni < 2 and 0 <= nj < 3:
            novy = copy.deepcopy(stav)
            novy[i0][j0], novy[ni][nj] = novy[ni][nj], novy[i0][j0]
            vysledky.append(novy)
    return vysledky

def string(stav):
    return ''.join(str(stav[i][j]) for i in range(2) for j in range(3))

def prohazovani(start):
    navstiveno = set()
    q = deque()
    q.append((start, 0))
    navstiveno.add(string(start))

    while q:
        stav, kroky = q.popleft()
        if string(stav) == string(cil):
            return kroky
        for posunuti in sousede(stav):
            s = string(posunuti)
            if s not in navstiveno:
                navstiveno.add(s)
                q.append((posunuti, kroky + 1))
    return "NELZE"

print(prohazovani(start))



