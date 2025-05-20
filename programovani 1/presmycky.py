
n = int(input())
r = []
for _ in range(n):
    slovo = input()
    r.append(slovo)

r_slovniky = []
for slovo in r:
    slovnik = {}
    for pismeno in slovo:
        if pismeno in slovnik:
            slovnik[pismeno] += 1
        else:
            slovnik[pismeno] = 1
    r_slovniky.append(slovnik)

m = int(input())
s = []
for _ in range(m):
    slovo = input()
    s.append(slovo)

s_slovniky = []
for slovo in s:
    slovniky = {}
    for pismeno in slovo:
        if pismeno in slovniky:
            slovniky[pismeno] += 1
        else:
            slovniky[pismeno] = 1
    s_slovniky.append(slovniky)


for prvek in s_slovniky:
    vysledek = []
    for prvky in r_slovniky:
        if prvek == prvky:
            vysledek.append((r[r_slovniky
    print(vysledek)
    





