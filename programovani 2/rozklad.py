n = int(input())
a = [n + 1] * (n + 1)

def rozklad(z, p):
    if z == 0:
        print("+".join(map(str, a[1:p])))
    else:
        for i in range(1, min(z, a[p-1])+1):
            a[p] = i
            rozklad(z-i, p+1)

rozklad(n, 1)
