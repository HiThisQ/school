def encode(n):
    if n == 0:
        return '.'

    k = n + 1
    a = 0
    while k % 2 == 0:
        k //= 2
        a += 1
    b = (k - 1) // 2

    return f'({encode(a)}{encode(b)})'

# Čtení čísel po řádcích
cisla = [int(radek) for radek in input().splitlines()]

for c in cisla:
    print(encode(c))
