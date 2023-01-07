class Fenomen:
    tip = "internet Fenomeni"
    def __init__(self,isim,slogan):
        self.isim = isim
        self.slogan = slogan

    @classmethod
    def tipSoyle(cls):
        print(cls.tip)

    def isimsloganSoyle(self):
        print(self.isim,":",self.slogan)

fenomen1 = Fenomen("Danla BİLİÇ "," Evlen artık danla" )
fenomen2 = Fenomen("Gülgün DİKİŞ" ,"Dedeye sahip çıkalım hihihhi!" )
fenomen3 = Fenomen("Yurdagülün Annesi", "Ne anladın YURDAGÜL?") 
fenomen4 = Fenomen("Serap PAKÖZ","Bedenim sağ sağ çok")

liste = [fenomen1,fenomen2,fenomen3]
for item in liste:
    item.isimsloganSoyle()