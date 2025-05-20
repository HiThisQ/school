#dostaneme soubor s cisli na kazdem radku 1 nebo vice a mame najit nejvetsi v tom
f = open("a.txt","r")
v = -1
for line in f:
    v = max(v,max(int, line.split()))
    
f.close()
print(v)
    
