a = int(input())


while a>0 :
    if a % 10 == 7:
        print ("je tam 7")
        break
    a//=10
else:
    print ("není tam 7")
    
