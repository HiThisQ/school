#matice v pythonu, seznam nahrazuje pole, 2 rozmerne pole se zapise
#jako seznam seznamu

m = []

r = int(input())
for _ in range(r):
    m.append(list(map(int, input().split())))

print (m)
