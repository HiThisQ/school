n = int(input())
permutace = list(map(int, input().split()))

i = n - 2
while i >= 0 and permutace[i] >= permutace[i + 1]:
    i -= 1

if i == -1:
    print("NEEXISTUJE")
else:
    j = n - 1
    while permutace[j] <= permutace[i]:
        j -= 1
    permutace[i], permutace[j] = permutace[j], permutace[i]
    permutace[i+1:] = reversed(permutace[i+1:])
    print(*permutace)
