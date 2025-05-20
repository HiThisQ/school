seznam_hodnot = []

while True:
    cislo = int(input())
    if cislo == -1:
        break
    i = 0
    while i < len(seznam_hodnot) and seznam_hodnot[i] < cislo:
        i += 1
    seznam_hodnot.insert(i, cislo)

k = int(input())
mini = sum(seznam_hodnot[:k])
maxi = sum(seznam_hodnot[-k:])

print(mini, maxi)




