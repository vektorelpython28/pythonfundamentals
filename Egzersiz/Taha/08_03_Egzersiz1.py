""" 
proje içerisinde bulunan dibaetes.csv dosyasını
r+ modunda okuyarak ilk beş satırını ekrana yazdıran 
python fonksiyonunu yazınız.
08_03_Egzersiz1.py dosyası içerisine kodu yazabilirsiniz.
"""


def okuma():
    dosyaYolu = "/workspace/pythonfundamentals/Dokumanlar/diabetes.csv"
    dosya = open(dosyaYolu,"r+")
    print(dosya.readlines(5))