cislo1 = int(input())
n = [int(input()) for _ in range(cislo1)]
cislo2 = int(input())
m = [int(input()) for _ in range(cislo2)]

def trideni(n,m):
    while len(m) != 0: 
        for index in range(n):
            y = m(1)
            if y > [index]:
                n.insert(index - 1,y)
            m.pop(1)
    return

"print (trideni(n,m))"




