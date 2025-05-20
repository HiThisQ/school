N = int(input())
permutace = list(map(int, input().strip().split()))

def dalsi_permutace(N, permutace):
    x = -1
    for i in range(N - 1):
        if permutace[i] < permutace[i + 1]:
            x = i
    if x == -1:
        return "NEEXISTUJE"
    y = -1
    for i in range( x + 1, N):
        if permutace[x] < permutace [i]:
            y = i

    permutace[x], permutace[y] = permutace[y], permutace[x]

    prvni = x + 1
    posledni = N - 1
    
    while prvni < posledni:
        permutace[prvni], permutace[posledni] = permutace[posledni], permutace[prvni]
        prvni += 1
        posledni -= 1
        
    return " ".join(map(str, permutace))

print(dalsi_permutace(N, permutace))
