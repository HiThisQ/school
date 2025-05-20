N, M = map(int, input().split())
poslN = list(map(int, input().split()))
poslM = list(map(int, input().split()))

pozice_N, pozice_M = [], []
i, j, index = 0, 0, 1
while i < N or j < M:
    if j == M or (i < N and poslN[i]<poslM[j]):
        pozice_N.append(index)
        i += 1
    else:
        pozice_M.append(index)
        j += 1
    index += 1
print(*pozice_N)
print(*pozice_M)


