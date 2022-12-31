"""Taş Kağıt Makas Oyununu kullanıcıyla birlikte oynayan bir
        python programı yazınız. Bu egzersiz sırasında birden fazla
        fonksiyon ve random modülünü kullanabilirsiniz.
    """
import random
liste = ["taş","kağıt","makas"]
def giris():
        tekrar = 1
        while tekrar == 1:
                x = input()
                y = random.choice(liste)
                print(y)
                if x == y:
                        continue
                elif (x == "taş" and y == "kağıt") or (x == "kağt" and y == "makas") or (x == "makas" and y == "taş"):
                        print("Kaybettiniz")
                else:
                        print("Kazandınız")
                tekrar = int(input("Tekrar oynamak istermisiniz? (1/0)"))            
giris()