n = int(input())

def osevy(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    a, b = 1, 2
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(osevy(n))

def osevy2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return osevy2(n - 1) + osevy2(n - 2)

print(osevy2(n))

def mrkev(n):
    if n <= 1:
        return 1
    else:
        return petrzel(n-1)

def petrzel(n):
    if n <= 1:
        return 1
    else:
        return petrzel(n-1) + mrkev(n-1)

def petr_mrkev(n):
    return petrzel(n) + mrkev(n)



