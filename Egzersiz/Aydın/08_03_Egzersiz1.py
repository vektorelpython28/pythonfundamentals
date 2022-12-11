def readFile(path):
    file = open(path,"r+")
    for i in range(5):
        print(file.readline(),end="")
readFile("diabetes.csv")    
    