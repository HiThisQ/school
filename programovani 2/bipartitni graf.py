from collections import deque

N = int(input())
M = int(input())
hrany = [tuple(map(int, input().split())) for _ in range(M)]


def je_bipartitni(N, hrany):
    graf = [[] for _ in range(N + 1)]
    for u, v in hrany:
        graf[u].append(v)
        graf[v].append(u)

    barva = [-1] * (N + 1)

    for start in range(1, N + 1):
        if barva[start] == -1:
            queue = deque([start])
            barva[start] = 0

            while queue:
                u = queue.popleft()
                for v in graf[u]:
                    if barva[v] == -1:
                        barva[v] = 1 - barva[u]
                        queue.append(v)
                    elif barva[v] == barva[u]:
                        return None

    skupina0 = sorted([i for i in range(1, N + 1) if barva[i] == 0])
    skupina1 = sorted([i for i in range(1, N + 1) if barva[i] == 1])
    return skupina0, skupina1

vysledek = je_bipartitni(N, hrany)
if vysledek is None:
    print("Nelze")
else:
    a, b = vysledek
    print(' '.join(map(str, a)))
    print(' '.join(map(str, b)))
