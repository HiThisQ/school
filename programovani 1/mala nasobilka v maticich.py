

def nasobilka():
    return[[i*j for j in range(1,11)]for i in range(1,11)]

vysledek = nasobilka()
for i in range(10):
    print(*vysledek[i])



#kdyz napisu hvezdicku vypisou se jednotlive prvky struktury

#jinak jde zapsat
for i in range(10):
    for j in range (10):
        print(vysledek[i][j], end=" ")
    print()

for i in range (10):
    for j in range (10):
        print(f"{vysledek[i][j]:4}", end="")
    print()
#f pred tim znamena formatovani a vypisovani na 3 ciferne pozice
