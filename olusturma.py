liste = ["Tuna","Aydın","Ceren",
    "Özlem","Bora","Emre","Muhammed","Naz","Ahmet","Muruvet","Taha","Iclal","Nur","Akın","Busra","Ediz"]
import os 
dosyaismi = "10_03_Inheritance"
folderName = "Egzersiz"
for item in liste:
    if not os.path.exists(os.path.join(folderName,item)):
        os.mkdir(os.path.join(folderName,item))
    dosya = open(fr"/workspace/pythonfundamentals/Egzersiz/{item}/{dosyaismi}.py","w+")
