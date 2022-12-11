# dosya işlemleri fonksiyonu open
# open("/workspace/pytonfundamentals/Dokumanlar/08_DosyaIslemleri/ornek.csv")
relyol = "Dokumanlar/08_DosyaIslemleri/ornek.csv"
# dosya = open(relyol)
# print(type(dosya))
# print(dosya.read())
"""
r read Ön tanımlı Mod okuma modu
w write yazma modu dosya var olsa bile sıfırdan oluşturulur
a append modu dosyanın en sonunda imleç olacak şekilde açar, var olan dosyada silme işlemi YAPMAZ
x create dosya var ise hata verir yok ise oluşturur
r+
w+
a+
x+
Binary dosyalar için
rb+
wb+
ab+
xb+
"""
dosya = open(relyol,"a+")