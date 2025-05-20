n = int(input())
memo = {}
def cesta_krale(x,y):
    if x < 0 or y < 0:
        return 0
    if x == 0 and y == 0:
        return 1
    if (x,y) in memo:
        return memo[(x,y)]
    memo[(x,y)] = cesta_krale(x-1,y) + cesta_krale(x, y-1) + cesta_krale(x-1,y-1)
    return memo[(x,y)]

print(cesta_krale(n,n))

