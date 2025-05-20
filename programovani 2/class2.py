import random
import string
class Animal:
    ID = 0
    uid = ""

    def __init__(self, id, uid) -> None: #sipka none je pouze kontrola
        self.id = id
        self.uid = uid
    def voice(self):
        pass
animal01 = Animal(1, "Máša")
animal02 = Animal(2, "Radan")

class cat(Animal):
    def __init__(self, id, uid):
        super().__init__(id, uid)
    def voice(self):
         print(f"Kocka id: {self.id}, uid: {self.uid}, mňau")

class dog(Animal):
    def __init__(self, id, uid):
        super().__init__(id, uid)
    def voice(self):
        print(f"Pes id: {self.id}, uid: {self.uid}, haf")
c1 = cat(1, "Jozef")
c2 = cat(8, "Marlenka")
d1 = dog(4, "Albert")
d2 = dog(6, "Jonas")
d3 = dog(19, "Kika")
zvirata = [c1,c2,d1,d2,d3]
for zvire in zvirata:
    zvire.voice()

def generate_uid(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

cats = [cat(random.randint(1, 20), generate_uid()) for _ in range(100)]
for cat in cats:
    cat.voice()