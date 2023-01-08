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

cokgen1 = Cokgen(3,"üçgen")
cokgen2 = Cokgen(4,"kare") 

print(cokgen1.AciSoyle)
print(cokgen2.AciSoyle)