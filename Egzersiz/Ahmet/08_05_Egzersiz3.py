"""Taş Kağıt Makas Oyununu kullanıcıyla birlikte oynayan bir
        python programı yazınız. Bu egzersiz sırasında birden fazla
        fonksiyon ve random modülünü kullanabilirsiniz.
    """
import random as rd
liste = ["taş", "kağıt", "makas"]
secim = rd.choice(liste)
print(secim)
anahtar = 0
adım = 0
sen = 0
bilgisayar = 0

def karsılastir():
        if kullanıcı == "taş" and secim == "taş":
                print("eşitlik")
                sen+=1
                bilgisayar+=1
                print(sen, bilgsayar)
        if kullanıcı == "taş" and secim == "kağıt":
                print("kaybettin")
                sen+=1
                bilgisayar+=1
                print(sen, bilgsayar)
        if kullanıcı == "taş" and secim == "makas":
                print("sen kazandın")
        if kullanıcı == "kağıt" and secim == "taş":
                print("sen kazandın")
        if kullanıcı == "kağıt" and secim == "kağıt":
                print("eşitlik")
        if kullanıcı == "kağıt" and secim == "makas":
                print("kaybettin")
        if kullanıcı == "makas" and secim == "taş":
                print("kaybettin")
        if kullanıcı == "makas" and secim == "kağıt":
                print("kazandın")
        if kullanıcı == "makas" and secim == "makas":
                print("eşitlik")
while anahtar == 0:
        kullanıcı = input("tahminini söyle :")
        karsılastir()

      
       