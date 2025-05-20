#ze vsech znaku 1 udelejte znaky 2 do noveho souboru
with open("b.txt","r") as f, open("a.txt","w")as g:
    s = f.read()
    s = s.replace("1", "2")
    g.write(s)
