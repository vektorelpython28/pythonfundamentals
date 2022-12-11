yol = "Dokumanlar/08_DosyaIslemleri/ornek.csv"
"""
read
readline
readlines
"""
dosya = open(yol,"r+")
################ read

# print("1",dosya.read(25))
# print("2",dosya.read())

################ readline
# print("1",dosya.readline(2))
# print("2",dosya.readline(4))
# print("3",dosya.readline(5))
# print("4",dosya.readline(10))

################# readlines
print("1",dosya.readlines())