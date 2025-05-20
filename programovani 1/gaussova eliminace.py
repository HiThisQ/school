m = []
def matice (m):
    n = int(input())
    
    for _ in range(n):
        radek = list(map(int, input().split()))
        m.append(radek)

    for i in range(n):      
            if m[i][i] == 0:
                for j in range(i+1, n):
                    if m[j][i] != 0:
                        m[i], m[j] = m[j], m[i]
                        break
            for j in range(i+1, n):
                if m[j][i] != 0:  
                    nasobek = m[j][i] / m[i][i]
                    for k in range(i, n+1):  
                        m[j][k] -= nasobek * m[i][k]
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = m[i][n] / m[i][i]  
        for j in range(i-1, -1, -1):
            m[j][n] -= m[j][i] * x[i]
    return(x)

vysledek = matice(m)
for prvek in vysledek:
    print(prvek)
    





