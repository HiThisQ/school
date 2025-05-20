N, K = map(int, input().strip().split())

def K_permutace(N, K):
    cisla = list(range(1, N + 1))
    permutace = []
    
    faktorial = 1
    i = 1
    while i < N:
        faktorial *= i
        i += 1
    
    while N > 0:
        index = (K - 1) // faktorial
        permutace.append(cisla.pop(index))
        
        K = (K - 1) % faktorial + 1
        N -= 1
        
        if N > 0:
            faktorial //= N

    return permutace


vysledek = K_permutace(N, K)
print(" ".join(map(str, vysledek)))
