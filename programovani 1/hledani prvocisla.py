a = int (input())

b = 2
while b*b <= a:
    if a % b == 0:
        print ("slozene cislo")
        break
    b += 1
else:
    print ("prvocislo")
