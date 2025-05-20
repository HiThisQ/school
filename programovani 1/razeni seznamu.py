def spojeni(cislo, n, dcislo, m):   
    for y in m:
        for index in range(len(n)):
            if y <= n[index]:
                n.insert(index,y)
                break
        else:
            n.append(y)

    return n


cislo = int(input())
n = [int(input()) for _ in range(cislo)]  

dcislo = int(input())
m = [int(input()) for _ in range(dcislo)]

serazena = spojeni(cislo, n, dcislo, m)

for vysledek in serazena:
    print(vysledek)
