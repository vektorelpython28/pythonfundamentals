class Fenomen:
    tip = "İnternet Fenomenleri"
    def __init__(self,isim,slogan):
        self.isim = isim
        self.slogan = slogan
    
    @classmethod
    def tipSoyle(cls):
        print(cls.tip)

    def fenomenSoyle(self):
        print(self.isim,": ",self.slogan)



fenomen1 = Fenomen("Beyin Bedava Abi","Atıyorum kafaya beyin bedava")
fenomen2 = Fenomen("Sivas Sporlu Dayı","Zabaha gadar burdayız")
fenomen3 = Fenomen("İnternet Mahir","I kiss you")
fenomen4 = Fenomen("Yurdagülün annesi","Ne anladın Yurdagül")

liste = [fenomen1, fenomen2, fenomen3, fenomen4]
for item in liste:
    item.fenomenSoyle()