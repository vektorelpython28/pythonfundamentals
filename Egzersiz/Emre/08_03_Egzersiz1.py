def okuma():
    dosya = open("diabetes.csv","r+")
    for i in range(5):
        print(dosya.readline())



def okuma():
    dosyaYolu = "/workspace/pythonfundamentals/diabetes.csv"
    dosya = open(dosyaYolu,"r+")
    print(dosya.readline())
    print(dosya.readline())
    print(dosya.readline())
    print(dosya.readline())
    print(dosya.readline())

def okuma():
    dosyaYolu = "/workspace/pythonfundamentals/diabetes.csv"
    dosya = open(dosyaYolu,"r+")
    for i in range(5):
        print(dosya.readline())

def dosyaOkuma():
    dosya = open("diabetes.csv","r+")
    for i in range(5):
        print(dosya.readline())