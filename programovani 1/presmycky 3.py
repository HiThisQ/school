n = int(input())
hesla = [input().strip() for _ in range(n)]
    
m = int(input())
dotazy = [input().strip() for _ in range(m)]

hesla_slovnik = {}
for heslo in hesla:
    klic = ''.join(sorted(heslo))
    if klic not in hesla_slovnik:
        hesla_slovnik[klic] = []
    hesla_slovnik[klic].append(heslo)

for dotaz in dotazy:
    klic = ''.join(sorted(dotaz))
    if klic in hesla_slovnik:
        presmycky = sorted(hesla_slovnik[klic])
        print(' '.join(presmycky))
    else:
        print()


