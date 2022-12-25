from os import system, name
from time import sleep
from datetime import datetime

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def zamandamga(format=0):
    simdi = datetime.now()
    if not format:
        liste = list(map(str,[simdi.hour+3,simdi.minute,simdi.day,simdi.month,simdi.year]))
        return  "_".join(liste)
    elif format == 1:
        liste = list(map(str,[simdi.day,simdi.month,simdi.year]))
        return str(simdi.hour + 3) + ":" + str(simdi.minute) + "." + "_".join(liste)
    



if __name__ == "__main__":
    clear()