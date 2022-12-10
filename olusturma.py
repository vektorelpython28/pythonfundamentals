liste = [
    "Özlem","Bora","Emre","Muhammed","Naz","Ahmet","Muruvet","Taha","Iclal","Nur"
]
import os 
dosyaismi = "ilk"
folderName = "Egzersiz"
for item in liste:
    if not os.path.exists(os.path.join(folderName,item)):
        os.mkdir(os.path.join(folderName,item))
    open(f"Egzersiz\{item}\{dosyaismi}.py","a+")
