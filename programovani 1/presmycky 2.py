def seznamy_slovniku(slova):
    seznam_slovniku = []
    for slovo in slova:
        slovnik = {}
        for pismeno in slovo:
            if pismeno in slovnik:
                slovnik[pismeno] += 1
            else:
                slovnik[pismeno] = 1
        seznam_slovniku.append(slovnik)
    return seznam_slovniku

n = int(input())
r = [input() for _ in range(n)]
r_slovniky = seznamy_slovniku(r)

m = int(input())
s = [input() for _ in range(m)]
s_slovniky = seznamy_slovniku(s)

for prvek in s_slovniky:
        vysledek = []
        for i in range(len(r_slovniky)):
            if prvek == r_slovniky[i]:
                vysledek.append(r[i])
        for x in sorted(vysledek):
            print(x, end = " ")
                
        print()



