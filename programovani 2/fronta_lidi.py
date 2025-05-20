class Clovek:
    def __init__(self, vek, dalsi=None):
        self.vek = vek
        self.dalsi = dalsi


class Fronta:
    def __init__(self):
        self.prvni = None
        while True:
            try:
                radek = input()
                if radek == "-1":
                    break
                vek = int(radek)
                if vek >= 0:
                    self.push(vek)
            except ValueError:
                pass

    def push(self, vek):
        novy_clovek = Clovek(vek)
        if self.prvni is None:
            self.prvni = novy_clovek
        else:
            aktualni = self.prvni
            while aktualni.dalsi:
                aktualni = aktualni.dalsi
            aktualni.dalsi = novy_clovek

    def vypis(self):
        if self.prvni is None:
            print("PRAZDNY")
        else:
            aktualni = self.prvni
            while aktualni:
                print(aktualni.vek, end=" ")
                aktualni = aktualni.dalsi
            print()

    def vyhodNejstarsi(self):
        if self.prvni is None:
            return
        max_vek = self.prvni.vek
        aktualni = self.prvni
        while aktualni:
            if aktualni.vek > max_vek:
                max_vek = aktualni.vek
            aktualni = aktualni.dalsi
        while self.prvni and self.prvni.vek == max_vek:
            self.prvni = self.prvni.dalsi
        aktualni = self.prvni
        while aktualni and aktualni.dalsi:
            if aktualni.dalsi.vek == max_vek:
                aktualni.dalsi = aktualni.dalsi.dalsi
            else:
                aktualni = aktualni.dalsi

    def nejstarsiDozadu(self):
        if self.prvni is None:
            return
        max_vek = self.prvni.vek
        aktualni = self.prvni
        while aktualni:
            if aktualni.vek > max_vek:
                max_vek = aktualni.vek
            aktualni = aktualni.dalsi
        front = None
        konec = None
        aktualni = self.prvni
        while aktualni:
            dalsi = aktualni.dalsi
            if aktualni.vek != max_vek:
                if front is None:
                    front = konec = aktualni
                else:
                    konec.dalsi = aktualni
                    konec = aktualni
            aktualni = dalsi
        aktualni = self.prvni
        while aktualni:
            if aktualni.vek == max_vek:
                if front is None:
                    front = konec = Clovek(max_vek)
                else:
                    konec.dalsi = Clovek(max_vek)
                    konec = konec.dalsi
            aktualni = aktualni.dalsi
        self.prvni = front

    def zdvojVsechny(self):
        aktualni = self.prvni
        while aktualni:
            novy_clovek = Clovek(aktualni.vek, aktualni.dalsi)
            aktualni.dalsi = novy_clovek
            aktualni = novy_clovek.dalsi

    def zdvojNejmladsi(self):
        if self.prvni is None:
            return
        min_vek = self.prvni.vek
        aktualni = self.prvni
        while aktualni:
            if aktualni.vek < min_vek:
                min_vek = aktualni.vek
            aktualni = aktualni.dalsi
        aktualni = self.prvni
        while aktualni:
            if aktualni.vek == min_vek:
                novy_clovek = Clovek(aktualni.vek, aktualni.dalsi)
                aktualni.dalsi = novy_clovek
                aktualni = novy_clovek.dalsi
            else:
                aktualni = aktualni.dalsi

    def vyhodTriPosledni(self):
        if self.prvni is None:
            return
        aktualni = self.prvni
        pocet = 0
        while aktualni:
            pocet += 1
            aktualni = aktualni.dalsi
        if pocet <= 3:
            self.prvni = None
            return
        aktualni = self.prvni
        for _ in range(pocet - 4):
            aktualni = aktualni.dalsi
        aktualni.dalsi = None

    def licheSude(self):
        if self.prvni is None:
            return
        liche = None
        sude = None
        liche_end = None
        sude_end = None
        aktualni = self.prvni
        while aktualni:
            if aktualni.vek % 2 == 1:
                if liche is None:
                    liche = liche_end = Clovek(aktualni.vek)
                else:
                    liche_end.dalsi = Clovek(aktualni.vek)
                    liche_end = liche_end.dalsi
            else:
                if sude is None:
                    sude = sude_end = Clovek(aktualni.vek)
                else:
                    sude_end.dalsi = Clovek(aktualni.vek)
                    sude_end = sude_end.dalsi
            aktualni = aktualni.dalsi
        if liche:
            self.prvni = liche
            liche_end.dalsi = sude
        else:
            self.prvni = sude

    def zrus(self):
        self.prvni = None


fronta = Fronta()
fronta.vypis()
fronta.vyhodNejstarsi()
fronta.vypis()
fronta.nejstarsiDozadu()
fronta.vypis()
fronta.vyhodTriPosledni()
fronta.vypis()
fronta.licheSude()
fronta.vypis()
fronta.zdvojNejmladsi()
fronta.vypis()
fronta.zdvojVsechny()
fronta.vypis()
fronta.zrus()
fronta.vypis()
fronta.vyhodNejstarsi()
fronta.vypis()
