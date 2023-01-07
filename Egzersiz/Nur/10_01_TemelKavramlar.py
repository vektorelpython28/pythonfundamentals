class Fenomen():
    def __init__(self, isim, slogan):
        self.isim = isim
        self.slogan = slogan
    
    def goster(self):
        print("""
        İntenet Fenomenleri ve Sloganları
        İsim: {}
        Slogan: {}
        """.format(self.isim, self.slogan)
        )
goster1 = Fenomen("İnternet Mahir", "I kiss you all")
goster1.goster()
    