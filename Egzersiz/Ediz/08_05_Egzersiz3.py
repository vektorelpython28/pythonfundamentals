from random import randint
from os import system, name
import time
liste = ["Taş","Kağıt","Makas"]
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def countdown(step):
    for i in range(step):
        time.sleep(1)
        print(i)



def game():
    lives = 3
    hP = 0
    cP = 0
    while lives > 0:
        countdown(3)
        attack = int(input("0- Taş,1- Kağıt,2- Makas:"))
        if attack in range(3):
            comp = randint(0, 2)
            gameList = [[0,1,2],[1,2,0],[2,0,1]]
            item =  gameList[attack]
            if item[1] == comp:
                cP+=1
                lives -= 1
            if item[2] == comp:
                hP += 1
                lives -= 1
            
            print("Bilgisayarın Hamlesi:",liste[comp],"Sizin Hamleniz:",liste[attack])
            print("İnsan:",hP,"Bilgisayar:",cP)
            time.sleep(2)
            clear()
        else:
            print("Seçiminiz Tahta")
    else:
        if hP<cP:
            print("Kaybettiniz")
        elif hP>cP:
            print("Kazandınız")
        else:
            print("Beraber")   

game()
        

