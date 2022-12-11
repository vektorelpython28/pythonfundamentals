
def dosya_okuma():
#readline:satır okur
    yol = "/workspace/pythonfundamentals/diabetes.csv"
    dosya = open(yol, "r+")
    print("1",dosya.readline())
    print("2",dosya.readline())
    print("3",dosya.readline())
    print("4",dosya.readline())
    print("5",dosya.readline()) 