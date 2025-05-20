with open("a.txt","r") as f, open("b.txt","w")as g:
    s = f.read()
    s = " ".join(s.split())
    s = s.split(".")
    vety = []
    for veta in s:
        veta = veta.strip()
        if veta:
            vety.append(veta + ".")
    g.write("\n".join(vety))
        
    
