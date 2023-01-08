class Cokgen:
    def __init__(self,kenar,adi):
        self.adi = adi
        self.kenar = kenar
        self.__aci = (kenar-2)*180

    @property
    def AciSoyle(self):
        if self.adi == "Üçgen":
            return self.__aci
        else:
            return "isim hatası"

c1 = Cokgen(3, "Üçgen")
c2 = Cokgen(5, "Beşgen")
c3 = Cokgen(6, "Altıgen")

print(c1.AciSoyle)