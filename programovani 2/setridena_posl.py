N, k = map(int, input().split())
data = list(map(int, input().split()))
dotazy = list(map(int, input().split()))

def bin_vyhl(data, i, N):
    l, p = 0, N - 1
    index = -1
    while l <= p:
        s = (l + p)//2
        if data[s] < i:
            l = s + 1
        elif data[s] > i:
            p = s -1
        else:
            index = s
            p = s -1
    return index + 1 if index != -1 else 0
vysledky = [(bin_vyhl(data, dotazy[i], N)) for i in range(k)]
print(" ".join(map(str, vysledky)))