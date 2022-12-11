liste = ["Tuna","Aydın",
    "Özlem","Bora","Emre","Muhammed","Naz","Ahmet","Muruvet","Taha","Iclal","Nur","Akın","Busra"]
import os 
dosyaismi = "07_01_Giris"
folderName = "Egzersiz"
for item in liste:
    if not os.path.exists(os.path.join(folderName,item)):
        os.mkdir(os.path.join(folderName,item))
    open(fr"/workspace/pythonfundamentals/Egzersiz/{item}/{dosyaismi}.py","a+")
