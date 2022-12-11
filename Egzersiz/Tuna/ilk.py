tektane=0
cifttane=0
tekToplam=0
ciftToplam=0
 
n=int(input("Kaç tane Sayı Girilecek : "))
for i in range(n):
    sayi=int(input("Sayı : "))
    if(sayi%2==0):
        tektane+=1
        tekToplam+=sayi
    else:
        cifttane+=1
        ciftToplam+=sayi
if(tektane!=0):
    print("Tek Sayıların Ortalaması : ",tekToplam/tektane)
if(ciftAdet!=0):
    print("Çift Sayıların Ortalaması : ",ciftToplam/ciftAdet)
 