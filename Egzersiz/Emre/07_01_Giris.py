from datetime import datetime
def zaman():  
    now = datetime.now()
    print(now.year,"/",now.month,"/",now.day,"  :  ",now.hour+3,":",now.minute)

zaman()