def dosyaOkuma(path):
    dosya = open(path,"r+")
    for i in range(5):
        print(dosya.readline())