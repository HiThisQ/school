class Zvire:
    def __init__(self, nazev):
        self.nazev = nazev
        self.dalsi = None
        pass

    def prichazi_za_mne(self, zvire):
        self.dalsi = zvire
        pass

    def kousni_dalsiho(self):
        if self.dalsi != None:
            return f'{self.nazev}: {self.dalsi.nazev} ma ode me kousanec'
        else:
            return f'{self.nazev}: nikdo za mnou neni'
        pass

prvni = None
predchozi = None
# TODO nacist vstup
while True:
    radek = input()
    if radek == "konec":
        break
    zvire = Zvire(radek)
    if prvni is None:
        prvni = zvire
    else:
        predchozi.prichazi_za_mne(zvire)
    predchozi = zvire

vypis = prvni
while vypis is not None:
     print(vypis.nazev)
     vypis = vypis.dalsi

prvni = prvni.dalsi

ptakopysk = Zvire("ptakopysk")
ptakopysk.dalsi = prvni
prvni = ptakopysk

mravenec = Zvire("mravenec")
mravenec.dalsi = prvni
prvni = mravenec

while prvni != None:
    print(prvni.kousni_dalsiho())
    prvni = prvni.dalsi

