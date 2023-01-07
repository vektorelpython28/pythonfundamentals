class Fenomen:
    tip = "internet Fenomeni"
    def __init__(self,isim,slogan):
        self.isim = isim
        self.slogan = slogan

    @classmethod
    def tipSoyle(cls):
        print(cls.tip)
    def markaSöyle(self):
        print(self.isim)
    
    Fenomen = Fenomen("Hadise" , "Acun ILICALI" , "Danla BİLİÇ")
    Slogan = 