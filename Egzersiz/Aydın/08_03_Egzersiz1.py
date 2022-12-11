def readFile(path):
    file = open(path,"r+")
    for i in range(5):
        print(file.readline(),end="")
readFile("diabetes.csv") #hocam valla bilmiom  list galiba 
list[6,148,72,35,0,33.6,0.627,50,1]
    