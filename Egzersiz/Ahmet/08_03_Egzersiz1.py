yol = "/workspace/pythonfundamentals/diabetes.csv"
dosya = open(yol, "r+")
def dosya_oku():
    print("1",dosya.readline())
    print("2",dosya.readline())
    print("3",dosya.readline())
    print("4",dosya.readline())
    print("5",dosya.readline())