#Kayıt
dogru_sifre = " "
hak = 0
print("Giriş Yap Veya Kayıt Ol")
print(""" Giriş Yapmak için "G", Kayıt Olmak İçin "K" """)
cevap = input("")
if cevap == "G" or cevap == "g":
    girilen_sifre = input("Şifrenizi Girin:  ")   
    if girilen_sifre == dogru_sifre:
        print("Başarıyla Giriş Yapıldı.")
    elif girilen_sifre != dogru_sifre:
        while hak < 2:    
            print("Şifreniz Yanlış, Şifrenizi Doğru olduğundan emin olun.")
            girilen_sifre = input("Lütfen Tekrar Deneyiniz:  ")
            hak += 1
if cevap == "K" or cevap == "k":
    belirlenen_sifre = input("Bir Şifre Belirleyin : ")
    dogru_sifre = belirlenen_sifre
    print("Kaydınız Başarılı")
    