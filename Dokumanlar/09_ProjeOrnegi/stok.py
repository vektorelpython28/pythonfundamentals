from db import dosyaislem as dt
from tools import screentools as sct
dt.alanlar = ["Ürün Adı","Ürün Adet","Ürün Fiyat"]
dt.yol = dt.yol.format("stok.csv")

def stokmenu():
    dosya = None
    menu = """
    Stok Programı
    1- Ürün Ekle
    2- Ürün Güncelle
    3- Ürün Sil
    4- Ürün Ara
    5- Ürün Stok Güncelle
    6- Ürün Fiyat Güncelle
    7- Ana Menü
    İşlem Seçiniz:
    """
    anahtar = 1

    while anahtar == 1:
        sct.clear()
        islem = input(menu)
        if islem and islem.isdigit():
            islem  = int(islem)
            if islem in range(1,7):
                if not dosya:
                    dosya = dt.dosyaAc(dt.yol)
                if islem == 1: # ürün ekleme
                    # dosya açılıyor
                    # dt.verilistele(dosya) # verilerili listeleme deneme
                    metin = dt.verigiris(dt.alanlar) # bilgi girişleri alındır
                    dt.dosyaYazma(dosya,metin) # bilgiler dosyaya yazıldı
                    dt.dosyaKaydet(dosya) # dosya kaydedildi
                if islem == 2: # ürün güncelleme
                    kayitListe = dt.dosyaOkuList(dosya)
                    dt.verilistele(dosya)
                    kayitNum = input("Düzenlemek istediğiniz kaydın numarasını giriniz:") 
                    metin = dt.verigiris(dt.alanlar) 
                    kayitListe[int(kayitNum)-1] = metin
                    dt.dosyaListeKaydet(dosya, kayitListe)

            if islem == 7:
                anahtar = 0
    else:
        ## TODO dosya işlemleri eklenebilir
        sct.clear()
        return True