 #transponovana matice, prvek bij = aji

m = [[1,2,3,4],[5,6,7,8],[1,2,3],[9,8,7,6]]
def transpozice(matice):
    r = len(matice)
    s = len(matice[0])
    b = [[0]*r for _ in range (s)]
    for i in range (s):
        for j in range (r):
            b[i][j] = matice[j][i]
    return (b)

vysledek = transpozice(m)
print(vysledek)
    


    
