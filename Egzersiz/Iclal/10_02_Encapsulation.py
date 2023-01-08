class Cokgen:
    def __init__(self,kenarSayisi,adi):
        self.kenarSayisi = kenarSayisi
        self.adi = adi
        self.__aci = (kenarSayisi-2)*180
    
    @property
    def AciSoyle(self):
        if self.adi == "üçgen":
            return self.__aci
        else:
            return "İsim hatası!!!"

obj1 = Cokgen(3, "üçgen")
obj2 = Cokgen(4, "kare")

print(obj1.AciSoyle)
print(obj2.AciSoyle)
