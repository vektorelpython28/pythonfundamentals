""" 
proje içerisinde bulunan dibaetes.csv dosyasını
r+ modunda okuyarak ilk beş satırını ekrana yazdıran 
python fonksiyonunu yazınız.
08_03_Egzersiz1.py dosyası içerisine kodu yazabilirsiniz.
"""

def readFile(path):
    file = open(path,"r+")
    for i in range(5):
        print(file.readline(),end="")
readFile("diabetes.csv")

"""
dosyada ilk satırda yer alan 72 ve 35 değerlerini 
bir değişkene aktarıp ekrana yazdırın oluşturduğunuz fonksiyon üzerinde
değişiklik yaparak devam edebilirsiniz
"""


def readFile(path):
    file = open(path,"r+")
    line = file.readline()
    print(line.split(","))
    a,b = line.split(",")[2],line.split(",")[3]
    print(a,b)
    
readFile("diabetes.csv")
metin = "Ali;Veli;123" 
print(metin.split(";")) #['Ali', 'Veli', '123']