a = [[1,2],[2,3]]
b = [[1,6],[7,9]]
n = len(a)
c = [[0]*n for _ in range(n)]


for i in range (n):
    for j in range (n):
        c[i][j] = sum(a[i][k]*b[k][j] for k in range (n))

print (c)
