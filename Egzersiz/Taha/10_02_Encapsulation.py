class cokgen:
    def __init__(self,kenarsayisi,adi):
        self.kenarSayisi = kenarSayisi
        self.adi = adi
        self.__aci = (kenarSayisi-2)*180

    @property
    def AciSoyle(self):
        if self.adi == "Üçgen":
            return self.__aci
        else:
            return "isim hatasi"

cokgen1 = Cokgen(3,"Üçgen")
cokgen2 = Cokgen(4,"kare") 

print(cokgen1.AciSoyle)
print(cokgen2.AciSoyle)