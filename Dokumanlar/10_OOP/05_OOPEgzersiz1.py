import random as rnd
class Hero:
    def __init__(self,adi,guc,saglik,superGuc=False):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik
        self.superGuc = superGuc
    
    def vur(self):
        return self.guc

    def darbe(self,vur):
        self.saglik -= vur

    def bilgiVer(self):
        print(self.adi,"=>",self.saglik)

class MarvelHero(Hero):
    def __init__(self,adi,guc,saglik):
        super().__init__(adi, guc, saglik)


    def darbe(self,vur):
        liste = [self.darbe1,self.darbe2,self.darbe3]
        rnd.choice(liste)(vur)
    
    def darbe1(self,vur):
        self.saglik -= vur//2

    def darbe2(self,vur):
        self.saglik -= vur
    
    def darbe3(self,vur):
        self.saglik -= vur//3

class DCHero(Hero):
    def __init__(self,adi,guc,saglik):
        super().__init__(adi, guc, saglik)

    def vur(self):
        liste = [self.vur1,self.vur2,self.vur3]
        return rnd.choice(liste)()

    def vur1(self):
        return self.guc//2
    
    def vur2(self):
        return self.guc
    
    def vur3(self):
        return self.guc//3


class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool", 100, 1500)
        self.superGuc = True
    
    def darbe(self,vur):
        super().darbe(vur)
        if self.superGuc:
            self.saglik += 50

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk", 150, 2000)

class SuperMan(DCHero):
    def __init__(self):
        super().__init__("SuperMan", 150, 2000)

class Batman(DCHero):
    def __init__(self):
        super().__init__("Batman", 120, 1000)

dcList = [Batman,SuperMan]
marvelList = [DeadPool,Hulk]

import time
P1 = rnd.choice(dcList)()
P2 = rnd.choice(marvelList)()
while P1.saglik > 0 and P2.saglik > 0:
    P1.darbe(P2.vur())
    P2.darbe(P1.vur())
    P1.bilgiVer()
    P2.bilgiVer()
    time.sleep(0.7)
else:
    if P1.saglik>P2.saglik:
        print(P1.adi,"Kazandı")
    elif P1.saglik<P2.saglik:
        print(P2.adi,"Kazandı")
    else:
        print("Berabere")


"""
Turkish Hero Classını oluşturalım
Turkish Hero Classında hem darbe ile ilgili farklılıklar hem de vur fonk. ile 
ilgili farklılıklar olsun
3 karakter Turkish Hero için
1 er karakter ise DC ve Marvel için ekleyelim. 
"""