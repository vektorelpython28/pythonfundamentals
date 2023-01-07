#Egzersiz:<br>
#yukarıdaki araba sınıfı örneğinden faydalanarak internet fenomenleri tanımlayabileceğimiz bir sınıf örneği oluşturunuz.Çalışmalarınızı 10_01_Temel_Kavramlar.py dosyasında gerçekleştirebiliriz. 
# * örnek özellik olarak sloganı ve adını saklayınız
# * sınıf özelliği olarak internet fenomeni yazını
#* örnek metod çalıştırıldığında ilgili fenomenin ismi:slogan şeklinde bir çıktı üretsin

class Fenomen:
    tip = "İnternet Fenomenleri"
    def __init__(self,isim,slogan):
        self.isim = isim
        self.slogan = slogan
    
    @classmethod
    def tipSoyle(cls):
        print(cls.tip)

    def isimSoyle(self):
        print(self.isim,": ",self.slogan)
        
fenomen1 = Fenomen("Cemalcan","sütlaç")
fenomen2 = Fenomen("Ceyda Kasabalı","soğuk espiri")
fenomen1.isimSoyle()
fenomen2.isimSoyle()