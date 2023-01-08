"""Egzersiz<br>
* Cokgen adında bir sınıf oluşturunuz. 
* Bu sınıfta kenar sayısı ve Adı adından iki örnek özellik ve bir aci adında  gizli örnek özellik tanımlayınız
* AciSoyle adında bir getter fonksiyonu tanımlayınız. 
* Gizli değişken üretilen nesnenin adı Üçgen ise açı bilgisini verebilsin diğer seçeneklerde isim hatası değerini dönsün
* getter fonksiyonunu property e dönüştürünüz
* Bu sınıfı kullanarak Üçgen ve Kare adında iki farklı nesne oluşturunuz."""

class Cokgen: # sınıf oluşması
    def __init__(self, kenarsayisi, adi): # özellik ve gizli özellik oluşumu
        self.kenarsayisi = kenarsayisi
        self.adi = adi
        self.__aci= 180*(kenarsayisi-2) # gizli özellik
    @property
    def aciSoyle(self): # getter fonksiyonu
        if self.adi == "ucgen":
            return self.__aci
        else:
            return "isim hatası"
    @alver.setter
    def aciSoyle(self, param):
        if isinstance(param,int) and param in range(1,11) and self.adi == "ucgen":
            self.__adi = param

        
ucgen = Cokgen(3,"ucgen")
kare = Cokgen(5,"dikdortgen")
print(kare.aciSoyle)