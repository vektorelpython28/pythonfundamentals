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
        clear()



def game():
    lives = 3
    hP = 0
    cP = 0
    while lives > 0:
        countdown(3)
        attack = int(input("0- Taş,1- Kağıt,2- Makas:"))
        comp = randint(0, 2)
        gameList = [[0,1,2],[1,2,0],[2,0,1]]
        for item in gameList[attack]
                if item[1] == comp:


        

