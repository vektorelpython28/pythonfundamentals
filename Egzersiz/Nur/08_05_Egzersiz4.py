""" Girilen bir sayıyı sözlü olarak ekrana yazdıran python
    programını yazınız. Örn:
    3,249,245 sayısını 
    üç milyon iki yüz kırk dokuz bin iki yüz kırk beş olarak ifade etmelidir.
    """
""" Girilen bir sayıyı sözlü olarak ekrana yazdıran python
    programını yazınız. Örn:
    3,249,245 sayısını 
    üç milyon iki yüz kırk dokuz bin iki yüz kırk beş olarak ifade etmelidir.
    """

# sayi = input("Sayıyı Giriniz:")
sayi = "3,249,245"
sayi = sayi.replace(",","").replace(".","")
print(sayi) # 3249245
# zfill
3-len(sayi)%3 + len(sayi) # 7 => 9,5 => 6, 11 => 12
# print("23".zfill(5))
ekleme = 0 if len(sayi)%3 == 0 else 3- len(sayi)%3
sayi = sayi.zfill(ekleme + len(sayi))
print(sayi) # 003249245
print(*range(len(sayi)//3))
for i in range(len(sayi)//3): # 0 1 2
    #  i = 0 [0:3], i = 1 [3:6] , i = 2 [6:9]
    print(sayi[i*3:i*3+3]) #003 249 245
birler = {"0":"","1":"Bir","2":"İki","3":"Üç"}
onlar = {"0":"","1":"On","2":"Yirmi"}
basamak = {0:"",1:"Bin",2:"Milyon",3:"Milyar"}
