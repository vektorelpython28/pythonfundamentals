#Kayıt
dogru_sifre = " "
print("Giriş Yap Veya Kayıt Ol")
print(""" Giriş Yapmak için "G", Kayıt Olmak İçin "K" """)
cevap = input("")
if cevap == "G":
    While dogru_sifre != girilen_sifre:
        girilen_sifre = input("Şifrenizi Girin:  ")
        if girilen_sifre == dogru_sifre:
            print("Başarıyla Giriş Yapıldı.")
        elif girilen_sifre != dogru_sifre:
            print("Şifreniz Yanlış")
if cevap == "K":
    print("Bir Şifre Belirleyin")
    belirlenen_sifre = input(": ")
    dogru_sifre = belirlenen_sifre
    print("Kaydınız Başarılı")