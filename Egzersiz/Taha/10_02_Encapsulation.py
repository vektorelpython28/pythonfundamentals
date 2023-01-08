class cokgen:
    def __init__(self,kenarsayisi):
        self.kenarsayisi = kenarsayisi
        self.adi = adi
        self.__aci = (kenarsayisi-2)*100

    @property
    def AciSoyle(self):
        if self.adi == "Üçgen":
            return self.__aci
        else:
            return "isim hatasi"

Üçgen = çokgen(3, 'Üçgen')
kare = çokgen(4, 'kare')
print(üçgen.kenar_sayisi)
print(kare.adi)
print(triangle.aciSoyle)
print(square.aciSoyle)