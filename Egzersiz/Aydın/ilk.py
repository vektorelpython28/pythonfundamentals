#finally
try:
    a = int(input("1. Sayıyı Giriniz:"))
    b = int(input("2. Sayıyı Giriniz:"))
except ValueError:
    print("Değer Hatası")
except ZeroDivisionError:
    print("Sıfıra Bölme Hatası")
finally:
    print("Yakarsa Dünyayı Garipler Yakar")
print("Program Çalışmaya Devam Ediyor")
