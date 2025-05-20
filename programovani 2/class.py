class Animal():
    vek = 0
    uid = ""
    def __init__(self, uid, vek) -> None:
        self.uid = uid
        self.vek = vek
    def voice(self):
        pass
#tvorime instance objektu animal
animal01 = Animal("rumprecht", 3)
animal02 = Animal("Adolf", 6)
print(animal01.uid)

#dedicnost
class Cat(Animal):
    def __init__(self, uid, vek):
        super().__init__(uid, vek)
    def voice(self):
        print(f"kocka uid: {self.uid}, mňau")
#super je odkaz na predka
c1 = Cat("007", 5)
c1.voice()

