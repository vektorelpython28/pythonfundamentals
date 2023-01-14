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

class TurkishHero(Hero):
    def __init__(self,adi,guc,saglik):
        super().__init__(adi, guc, saglik)

    def heal(self,vur):
        liste = [self.heal1,self.heal2,self.heal3]
        rnd.choice(liste)(vur)
    
    def heal1(self,vur):
        self.saglik += vur//2
    
    def heal2(self,vur):
        self.saglik += vur//4
    
    def heal3(self,vur):
        self.saglik += vur//3


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

class Thor(MarvelHero):
    def __init__(self):
        super().__init__("Thor", 200, 1200)

class SuperMan(DCHero):
    def __init__(self):
        super().__init__("SuperMan", 150, 2000)

class Batman(DCHero):
    def __init__(self):
        super().__init__("Batman", 120, 1000)

class Flash(DCHero):
    def __init__(self):
        super().__init__("Flash", 100, 1200)

class Tarkan(TurkishHero):
    def __init__(self):
        super().__init__("Tarkan", 125, 1250)

class Atilla(TurkishHero):
    def __init__(self):
        super().__init__("Atilla", 120, 1500)

class Dedekorkut(TurkishHero):
    def __init__(self):
        super().__init__("Dedekorkut", 100, 1150)

thlist = [Tarkan,Atilla,Dedekorkut]
dcList = [Batman,SuperMan,Flash]
marvelList = [DeadPool,Hulk,Thor]

import time
P1 = rnd.choice(thlist)()
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