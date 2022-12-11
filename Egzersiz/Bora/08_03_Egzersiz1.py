def dosyaOkuma():
    dosya = open("diabetes.csv","r+")
    for i in range(5):
        print(dosya.readline())