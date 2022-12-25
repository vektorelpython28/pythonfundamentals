
##################### 1.YOL ###################
anahtar = 1
menu = "#"*10 + """
1-Yeni Kayıt
5-Çıkış #
İşlem Numarasını Giriniz:
"""
yol  = "Dokumanlar/08_DosyaIslemleri/rehber.csv"
dosya = open(yol,"a+")
while anahtar==1:
    islem = input(menu)
    if islem == "1":
        adi = input("Adını Giriniz:")
        soyadi = input("Soyadı Giriniz:")
        telefon = input("Telefon Numarası Giriniz:")
        metin = ";".join([adi,soyadi,telefon]) + "\n"
        dosya.write(metin)
        dosya.flush()
    if islem == "5":
        anahtar = 0
else:
    dosya.close()
    print("Sistem Kapandı")

##################### 1.YOL ###################

##################### 2.YOL ###################
anahtar = 1
menu = "#"*10 + """
1-Yeni Kayıt
5-Çıkış 
İşlem Numarasını Giriniz:
"""
yol  = "Dokumanlar/08_DosyaIslemleri/rehber.csv"
# dosya = open(yol,"a+")
while anahtar==1:
    islem = input(menu)
    if islem == "1":
        adi = input("Adını Giriniz:")
        soyadi = input("Soyadı Giriniz:")
        telefon = input("Telefon Numarası Giriniz:")
        ####################################
        print(adi,soyadi,telefon,sep=";",file=open(yol,"a+"))
        ####################################
    if islem == "5":
        anahtar = 0
else:
    print("Sistem Kapandı")
##################### 2.YOL ###################