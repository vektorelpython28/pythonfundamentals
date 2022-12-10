try:
    a = int(input("1. Sayıyı Giriniz:"))
    b = int(input("2. Sayıyı Giriniz:"))
except ValueError:
    print("Değer Hatası")
else:
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Sıfıra Bölme Hatası")
print("Program Çalışmaya Devam Ediyor")

# raise
try:
    a = int(input("1. Sayıyı Giriniz:"))
    if a == 0:
        raise ZeroDivisionError("Sebebi Neydi Ki?")

    b = int(input("2. Sayıyı Giriniz:"))
    print(a/b)

except ValueError:
    print("Değer Hatası")

except ZeroDivisionError as hata:
    print("Sıfıra Bölme Hatası => ", hata)

finally:
        print("Yakalarsa Dünyayı Garipler Yakar")

print("Program Çalışmaya Devam Ediyor")

