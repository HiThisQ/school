hodnoty = []
while True:
    cislo = float(input())
    if cislo == -1:
        break
    hodnoty.append(cislo)

def delici_bod(hodnoty):
    n = len(hodnoty)
    if n == 0:
        return -1
    maxi = [float('-inf')] * n
    for i in range(1, n):
        maxi[i] = max(maxi[i-1], hodnoty[i-1])

    mini = [float('inf')] * n
    for i in range(n-2, -1, -1):
        mini[i] = min(mini[i+1], hodnoty[i+1])

    for i in range(n):
        if maxi[i] < hodnoty[i] < mini[i]:
            return i
    return -1

vysledek = delici_bod(hodnoty)
print(vysledek)

