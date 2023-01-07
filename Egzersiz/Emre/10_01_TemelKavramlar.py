class Fenomens:
    zink = "Fenomenler"
    def __init__(self,ad,laf):
        self.ad = ad
        self.laf = laf
    
    @classmethod   
    def tipSoyle(cls):
        print(cls.zink)

    def lafSoyle(self): 
        print(self.laf)

    def adSoyle(self): 
        print(self.ad)

sarhosT = Fenomens("Sarhoş Talica", "Baba ben senin için le le le ley")
İboT = Fenomens("İbrahim Tatlıses", "Eşarbını yan bağlama")
Kuzey = Fenomens("Kuzey Tekinoğlu", "Kurabiye var simit var neye bakıyon")
TaylirAbim = Fenomens("Tyler Durden", "Bizler tarihin ortanca çocuklarıyız")

Kuzey.lafSoyle()
TaylirAbim.tipSoyle()
sarhosT.adSoyle()


