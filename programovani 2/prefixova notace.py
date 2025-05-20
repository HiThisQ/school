vstup = input().strip().split()

def vyhodnot(vyraz):
    if not vyraz:
        return "CHYBA"

    prvek = vyraz.pop(0)

    if prvek in "+-*/":
        a = vyhodnot(vyraz)
        if a == "CHYBA":
            return "CHYBA"
        b = vyhodnot(vyraz)
        if b == "CHYBA":
            return "CHYBA"

        if prvek == "+":
            return a + b
        elif prvek == "-":
            return a - b
        elif prvek == "*":
            return a * b
        elif prvek == "/":
            if b == 0:
                return "CHYBA"
            return a // b
    else:
        try:
            return int(prvek)
        except:
            return "CHYBA"

vysledek = vyhodnot(vstup)
print(vysledek)

#ja jsem celou dobu nahraval spatny soubor, omloivam se :Dd