class Fenomens:
    zink = "Fenomenler"
    def __init__(self,ad,laf):
        self.ad = ad
        self.laf = laf
    
    @classmethod
    def adSoyle(cls):
        print(cls.ad)

    def lafSoyle(self): 
        print(self.laf)


