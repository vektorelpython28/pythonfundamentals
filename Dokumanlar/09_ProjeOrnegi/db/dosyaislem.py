import os
# db/stok.csv
## DEBUG TRUE
yol = os.path.join("Dokumanlar","09_ProjeOrnegi","db","{}")
## DEBUG FALSE
# yol = os.path.join("db","{}")
alanlar = []
from tools import screentools as sct
# # db/ayarlar.csv
# # db\ayarlar.csv
# print(yol.format("ayarlar.csv"))
def dosyaAc(yolu=yol):
    return open(yol,"a+",encoding="UTF-8")


def dosyaYazma(dosya,bilgiler):
    dosya.write(bilgiler)

def dosyaKaydet(dosya,param=1):
    if param:
        dosya.flush()
    else:
        dosya.close()

def verigiris(alanlar,ayrac=";"):
    liste = []
    for item in alanlar:
        liste.append(input(f"{item} Giriniz:"))
    else:
        liste.append(sct.zamandamga())
    return ayrac.join(liste)  + "\n"


def verilistele(dosya):
    dosya.seek(0)
    liste = dosyaOkuList(dosya)
    liste = list(enumerate(liste))
    for item in liste:
        print(item[0] + 1,"-",*item[1].split(";"),end="")


def dosyaListeKaydet(dosya,kayitList):
    if kayitList:
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(kayitList)
        dosya.flush()
        return True
    else:
        return False

def dosyaOkuList(dosya):
    dosya.seek(0)
    return dosya.readlines()