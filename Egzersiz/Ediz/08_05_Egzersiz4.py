""" Girilen bir sayıyı sözlü olarak ekrana yazdıran python
    programını yazınız. Örn:
    3,249,245 sayısını 
    üç milyon iki yüz kırk dokuz bin iki yüz kırk beş olarak ifade etmelidir.
    """

# sayi = input("Sayıyı Giriniz:")
sayi = "3,249,245"
sayi = sayi.replace(",","").replace(".","")
# print(sayi) # 3249245
# zfill
3-len(sayi)%3 + len(sayi) # 7 => 9,5 => 6, 11 => 12
# print("23".zfill(5))
ekleme = 0 if len(sayi)%3 == 0 else 3- len(sayi)%3
sayi = sayi.zfill(ekleme + len(sayi))
# print(sayi) # 003249245
# print(*range(len(sayi)//3))
liste = []
for i in range(len(sayi)//3): # 0 1 2
    #  i = 0 [0:3], i = 1 [3:6] , i = 2 [6:9]
    # print(sayi[i*3:i*3+3]) #003 249 245
    liste.append(sayi[i*3:i*3+3])
birler = birler = {"0":"", "1":"Bİr", "2":"İki", "3":"Üç", "4":"Dört", "5":"Beş", "6":"Altı", "7":"Yedi", "8":"Sekiz", "9":"Dokuz"}
onlar = {"0":"","1":"On","2":"Yirmi","3":"Otuz","4":"Kırk","5":"Elli","6":"Altmış","7":"Yetmiş","8":"Seksen","9":"Doksan"}
basamak = {0:"",1:"Bin",2:"Milyon",3:"Milyar"}
sonuc = ""
for item in liste:
    sonuc = ""
    if item[0] != "0":
        if item[0] == "1":
            sonuc += " Yüz "
        else:
            sonuc += birler[item[0]] + " Yüz "
    sonuc += onlar[item[1]]
    sonuc += birler[item[2]]
    print(sonuc)