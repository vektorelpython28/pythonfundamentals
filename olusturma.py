liste = ["Tuna","Aydın","Ceren",
    "Özlem","Bora","Emre","Muhammed","Naz","Ahmet","Muruvet","Taha","Iclal","Nur","Akın","Busra","Ediz"]
import os 
dosyaismi = "10_01_TemelKavramlar"
folderName = "Egzersiz"
for item in liste:
    if not os.path.exists(os.path.join(folderName,item)):
        os.mkdir(os.path.join(folderName,item))
    dosya = open(fr"/workspace/pythonfundamentals/Egzersiz/{item}/{dosyaismi}.py","a+")
    metin = """\"\"\" Girilen bir sayıyı sözlü olarak ekrana yazdıran python
    programını yazınız. Örn:
    3,249,245 sayısını 
    üç milyon iki yüz kırk dokuz bin iki yüz kırk beş olarak ifade etmelidir.
    \"\"\"
"""
    dosya.write(metin)
    dosya.close()
