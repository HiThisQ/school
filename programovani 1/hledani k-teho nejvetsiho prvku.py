s = []

while True:
    c = int(input())
    if c == -1:
        break
    s.append(c)

k = int(input())

while k > 0:
    x = s[0]
    for i in range (1, len(s)):
        if s [i] > x:
            x = s [i]
    s.remove(x)
    k -= 1

print (x)




    
    
    

    
    
    
