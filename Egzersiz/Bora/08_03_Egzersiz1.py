#def dosyaOkuma():
#    dosya = open("diabetes.csv","r+")
#    for i in range(5):
#        print(dosya.readline())

def nums():
    file = open("diabetes.csv","r+")
    line = file.readline()
    a,b = line.split(",")[2],line.split(",")[3]
    print(a,b)