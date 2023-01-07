class Fenomen:
    tip = "internet fenomeni" 
    def __init__(self, adi, slogan):
        self.adi = adi
        self.slogan = slogan
    @classmethod(f)
    def kimligi(self):
        print(self.adi, self.slogan)

fenomen1 = Fenomen("İnternet Mahir", "I kiss You")
fenomen2 = Fenomen("Artiz Amca", "Ne tıkırtı var ne sıkırtı var")

fenomen1.kimligi()
print(fenomen1.tip)