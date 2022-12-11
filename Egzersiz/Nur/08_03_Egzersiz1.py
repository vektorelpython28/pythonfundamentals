
def readFile(path):
    file = open(path,"r+")
    line = file.readline()
    a,b = line.split(",")[2],line.split(",")[3]
    print(a,b)
    
readFile("diabetes.csv")