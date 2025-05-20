import heapq
from collections import deque
def parkovaci_garaz():
    n, m = map(int, input().split())
    ceny = [int(input()) for _ in range(n)]
    vaha_aut = [int(input()) for _ in range(m)]
    volna_mista = list(range(n))
    heapq.heapify(volna_mista)
    fronta = deque()
    kde_parkuje = {}
    celkova_cena = 0
    udalosti = [int(input()) for _ in range(2 * m)]

    for udalost in udalosti:
        if udalost > 0:
            auto_id = udalost - 1

            if volna_mista:
                misto = heapq.heappop(volna_mista)
                kde_parkuje[auto_id] = misto
                celkova_cena += ceny[misto] * vaha_aut[auto_id]
            else:
                fronta.append(auto_id)

        else:
            auto_id = -udalost - 1
            misto = kde_parkuje.pop(auto_id)
            heapq.heappush(volna_mista, misto)

            if fronta:
                cekajici_auto_id = fronta.popleft()
                nove_misto = heapq.heappop(volna_mista)
                kde_parkuje[cekajici_auto_id] = nove_misto
                celkova_cena += ceny[nove_misto] * vaha_aut[cekajici_auto_id]

    print(celkova_cena)

parkovaci_garaz()
