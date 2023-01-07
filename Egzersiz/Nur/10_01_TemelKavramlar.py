class Fenomen:
    tip = "internet Fenomeni"
    def __init__(self,isim,slogan):
        self.isim = isim
        self.slogan = slogan

    @classmethod
    def tipSoyle(cls):
        print(cls.tip)

    def isimSoyle(self):
        print(self.isim)
    def sloganSoyle(self):
        print(self.slogan)

Fnmn1 = Fenomen("İnternet Mahir", "I kiss you all")
Fnmn2 = Fenomen("İsimsiz Vatandaş", "Erkan anektarlar koltuğun altında kalık beni ara")
Fnmn3 = Fenomen("Webcamci Çocuk", "Al kırdın kırdın...")
Fnmn4 = Fenomen("Katip Köksal", "Artiz mi? Artiz ne arar la bazarda")

Fnmn1.isimSoyle()
Fnmn1.sloganSoyle()

Fnmn2.isimSoyle()
Fnmn2.sloganSoyle()

Fnmn3.isimSoyle()
Fnmn3.sloganSoyle()

Fnmn4.isimSoyle()
Fnmn4.sloganSoyle()