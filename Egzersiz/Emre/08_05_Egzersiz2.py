"""
Taş Kağıt Makas Oyununu kullanıcıyla birlikte oynayan bir
python programı yazınız. Bu egzersiz sırasında birden fazla
fonksiyon ve random modülünü kullanabilirsiniz.
"""
import random as rnd
move = ["Taş", "Kağıt", "Makas"]
tur = 0
print("TAŞ KAĞIT MAKAS")
baslat = input(""" Oyuna Başlamak İçin "E" , Çıkış İçin "Q" """)
if baslat == "E":
        while tur < 3:
                print("TUR-" + str(int(tur) + 1))
                oyun = input(""" 
                Taş 
                Kağıt
                Makas
                
                """)

                pc = rnd.choice(move)
                print("\n" + pc)
                
                tur += 1
                if oyun == pc:
                        print("Berabere")
                elif oyun == "Taş":
                        if pc == "Kağıt":
                                print("Kaybettiniz")
                        elif pc == "Makas":
                                print("Kazandınız")
                elif oyun == "Kağıt":
                        if pc == "Taş":
                                print("Kazandınız")
                        elif pc == "Makas":
                                print("Kaybettiniz")
                elif oyun == "Makas":
                        if pc == "Taş":
                                print("Kaybettiniz")
                        elif pc == "Kağıt":
                                print("Kazandınız")
elif baslat == "Q":
        print("Oyundan Çıkıldı..")
exit()