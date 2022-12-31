from db import dosyaislem as dt
from tools import screentools as sct,SIDUTool as sidu
dt.alanlar = ["UrunId","Adet","Tutar"]
dt.yol = dt.yol.format("kasa.csv")

def stokmenu():
    dosya = None
    menu = """
    Satış Programı
    1- Ürün Satış
    2- Ürün Listele
    3- Ürün İade
    4- Gelir
    5- Gider
    6- Ana Menü
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
                    dt.verilistele(dosya)
                    kayitNum = input("Düzenlemek istediğiniz kaydın numarasını giriniz:") 
                    metin = dt.verigiris(dt.alanlar)
                    sidu.Guncelle(kayitNum, dosya, metin)
                if islem == 3:
                    kayitListe = dt.dosyaOkuList(dosya)
                    dt.verilistele(dosya)
                    kayitNum = input("Silmek istediğiniz kaydın numarasını giriniz:")
                    sidu.Silme(kayitNum, dosya)
                    devam = input("Devam Etmek İçin Bir Tuşa Basınız...")
                if islem == 4:
                    sidu.Arama(dosya)
                if islem == 5:
                    kayitListe = dt.dosyaOkuList(dosya)
                    dt.verilistele(dosya)
                    kayitNum = input("Düzenlemek istediğiniz kaydın numarasını giriniz:") 
                    stokBilgisi = input("Stok Bilgisini Giriniz:")
                    sidu.AlanGuncelle(1, kayitNum, dosya, stokBilgisi)
                if islem == 6:
                    kayitListe = dt.dosyaOkuList(dosya)
                    dt.verilistele(dosya)
                    kayitNum = input("Düzenlemek istediğiniz kaydın numarasını giriniz:") 
                    fiyatBilgisi = input("Fiyat Bilgisini Giriniz:")
                    sidu.AlanGuncelle(2, kayitNum, dosya, fiyatBilgisi)
            if islem == 7:
                anahtar = 0
    else:
        ## TODO dosya işlemleri eklenebilir
        sct.clear()
        return True