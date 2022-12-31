"""Taş Kağıt Makas Oyununu kullanıcıyla birlikte oynayan bir
        python programı yazınız. Bu egzersiz sırasında birden fazla
        fonksiyon ve random modülünü kullanabilirsiniz.
    """
from random import randint 
while True:
    secenek = ["taş", "kağıt", "makas"]
    pc = secenek[randint(0,2)]
    kullanici = input("Hangisini seçeceğini belirleyiniz = taş, kağıt, makas?")

    if pc == kullanici:
        print("Berabere")

    elif kullanici == "taş":
        if pc == "kağıt":
            print("Kaybettiniz.", kullanici, pc, "sarar" )
        else:
            print("Kazandınız.", kullanici, pc, "kırar")

    elif kullanici == "kağıt":
        if pc == "makas":
            print("Kaybettiniz.", kullanici, pc, "keser")

        else:
            print("Kazandınız.", kullanici, pc, "sarar")
    
    elif kullanici == "makas":
        if pc == "taş":
            print("Kaybettiniz.", kullanici, pc, "kırar")

        else:
            print("Kazandınız.", kullanici, pc, "keser")
        
        
