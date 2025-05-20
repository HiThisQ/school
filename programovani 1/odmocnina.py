# chceme vypocitat odmocninu dame a0 je n/2 pak napiseme ai+1 = 1/2(ai + n/ai)
# takhle se nam bude do nekonecna priblizovat k odmocnice, zvolime epsyl, ktere
# urci jak blizko prestat (1e - 6 = 10 na -6)
n = int (input())
eps = 1e-6

a=n/2
b=n
while abs(b-a) > eps:
    b = a
    a = (a + n / a) / 2

print (a)

