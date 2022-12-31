liste = ["Tuna","Aydın","Ceren",
    "Özlem","Bora","Emre","Muhammed","Naz","Ahmet","Muruvet","Taha","Iclal","Nur","Akın","Busra"]
import os 
dosyaismi = "08_05_Egzersiz3"
folderName = "Egzersiz"
for item in liste:
    if not os.path.exists(os.path.join(folderName,item)):
        os.mkdir(os.path.join(folderName,item))
    dosya = open(fr"/workspace/pythonfundamentals/Egzersiz/{item}/{dosyaismi}.py","w+")
    metin = """\"\"\"Taş Kağıt Makas Oyununu kullanıcıyla birlikte oynayan bir
        python programı yazınız. Bu egzersiz sırasında birden fazla
        fonksiyon ve random modülünü kullanabilirsiniz.
    \"\"\"
"""
    dosya.write(metin)
    dosya.close()
