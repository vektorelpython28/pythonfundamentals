class Kisi:
    tip = "Fenomen"
    def __init__(self,isim,slogan):
        self.isim = isim
        self.slogan = slogan

    @classmethod
    def tipSoyle(cls): 
        print(cls.isim)
    
    def isimSoyle(self):
        print(self.isim)

    def sloganSoyle(self):
        print(self.slogan)
    
Kisi1 = Kisi("Internet mahir", "I kiss you")
Kisi2 = Kisi("Yurdagül", "Ne anladın yurdagül")
Kisi3 = Kisi("kcdurmaz", "bana var dendi")

Kisi1.isimSoyle()
Kisi1.sloganSoyle()
Kisi2.isimSoyle()
Kisi2.sloganSoyle()
Kisi3.isimSoyle()
Kisi3.sloganSoyle()