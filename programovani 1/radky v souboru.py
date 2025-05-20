#kopie souboru aby obsahovala prvnich 10 radku nebo tolik kolik jich ma pod 1O
p = 0
with open("c.txt","r") as f, open("d.txt","w")as g:
    for line in f:
        g.write(line)
        p += 1
        if p == 10: break

    
    
