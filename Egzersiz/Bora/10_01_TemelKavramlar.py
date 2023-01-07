class Fenomen:
    tip = "İnternet Fenomenleri"
    def __init__(self,isim,sloagan):
        self.marka = isim
        self.model = slogan
    
    @classmethod
    def isimSoyle(cls): # sınıf metodu
        print(cls.tip)

    def sloganSoyle(self): # örnek metodu
        print(self.marka)

fenomen1 = ("Beyin Bedava Abi","Atıyorum kafaya beyin bedava")
fenomen2 = ("Sivas Sporlu Dayı","Zabaha gadar burdayız")

fenomen1.isimSoyle()
fenomen2.solganSoyle()