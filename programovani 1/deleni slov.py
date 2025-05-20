text = input()
w = int(input())

def zarovnany_text (text, w):
    slova = text.split()
    vysledne_radky = []
    akradek = []
    delka_akradku = 0
    
    for ak_slovo in slova:
        if len(ak_slovo) + len(akradek) + delka_akradku <= w:
            akradek.append(ak_slovo)
            delka_akradku += len(ak_slovo)
        else:
            vysledne_radky.append(" ".join(akradek))
            akradek = []
            delka_akradku = 0
                                  
            if len(ak_slovo) > w:
                vysledne_radky.append(ak_slovo)
            else:
                
                akradek = [ak_slovo]
                delka_akradku = len(ak_slovo)
    if akradek:
        vysledne_radky.append(" ".join(akradek))
    
    return "\n".join(vysledne_radky)

vysledny_text = zarovnany_text (text, w)
print(vysledny_text)


        
        
            
            
            
