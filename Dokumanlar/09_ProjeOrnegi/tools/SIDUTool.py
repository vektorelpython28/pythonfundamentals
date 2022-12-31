def Ekle(metin,dosya):
    try:
        dt.dosyaYazma(dosya,metin) # bilgiler dosyaya yazıldı
        dt.dosyaKaydet(dosya) # dosya kaydedildi
        return True
    except:
        return False

def Guncelle(kayitNum,dosya,metin):
    try:
        kayitListe = dt.dosyaOkuList(dosya)
        kayitListe[int(kayitNum)-1] = metin
        dt.dosyaListeKaydet(dosya, kayitListe)
        return True
    except:
        return False

def Silme(kayitNum,dosya):
    try:
        kayitListe = dt.dosyaOkuList(dosya)
        del kayitListe[int(kayitNum)-1]
        dt.dosyaListeKaydet(dosya, kayitListe)
        return True
    except:
        return False

def Arama(dosya):
    sct.clear()
    results = []
    search = input("Anahtar Kelime ya da sayıyı giriniz (Tüm Kayıtlar İçin *): ")
    kayitListe = dt.dosyaOkuList(dosya)
    if search == "*":
        for num,item in enumerate(kayitListe):
            print(num,"-",*item.split(";"),end="")
    else:
        for num,item in enumerate(kayitListe):
            for rec in item.split(";"):
                if str(rec).count(search) > 0:
                    results.append((num,item))
        for num,result in results:
            print(num,"-",*result.split(";"),end="")


def AlanGuncelle(alanId,kayitNum,dosya,guncelBilgi):
    try:
        kayitListe = dt.dosyaOkuList(dosya)
        satir = kayitListe[int(kayitNum)-1].split(";")
        satir[alanId] = stokBilgisi
        kayitListe[int(kayitNum)-1] = ";".join(satir) 
        dt.dosyaListeKaydet(dosya, kayitListe)
        return True
    except:
        return False

