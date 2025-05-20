x = int(input())
y = int (input())


while x != y:
    if x > y:
        x = x - y
    else:
        y = y - x
        
print (x)
