class Cokgen():
    def __init__(self,kenar_sayisi, adi):
        self.kenar_sayisi = kenar_sayisi
        self.adi = adi
        self.__aci = 180*(kenar_sayisi-2)

    @property
    def AciSoyle(self): #getter
        if self.adi == "Üçgen":
            return self.__aci
        else:
            return "İsim Hatası"

obj1 = Cokgen(3,"Üçgen")
obj2 = Cokgen(4, "Kare")

print(obj1.AciSoyle)
print(obj2.AciSoyle)    
    