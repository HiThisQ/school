with open("a1.txt","r") as f, open("a2.txt","r")as g, open("b.txt","w") as h:
    s = list(map(int, f.read().split()))
    t = list(map(int, g.read().split()))
    while s != [] and t != []:
        if t[0] > s[0]:
            h.write(str(s[0])+" ")
            s.pop(0)
        else:
            h.write(str(t[0])+" ")
            t.pop(0)
    if s == []:
        for i in t:
            h.write(str(i)+" ")
    if t == []:
        for i in s:
            h.write(str(i)+" ")
    
