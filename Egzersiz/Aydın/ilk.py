tekAdet=0
ciftAdet=0
tekToplam=0
ciftToplam=0
 
n=int(input("Kaç Adet Sayı Girilecek : "))
for i in range(n):
    sayi=int(input("Sayı : "))
    if(sayi%2==0):
        tekAdet+=1
        tekToplam+=sayi
    else:
        ciftAdet+=1
        ciftToplam+=sayi
if(tekAdet!=0):#Eğer hiç tek sayı girilmemişse 0'a bölme hatası verecektir.
    print("Tek Sayıların Ortalaması : ",tekToplam/tekAdet)
if(ciftAdet!=0):#Eğer hiç çift sayı girilmemişse 0'a bölme hatası verecektir.
    print("Çift Sayıların Ortalaması : ",ciftToplam/ciftAdet)
