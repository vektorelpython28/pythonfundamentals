import os
print(os.sep)
print(os.path.exists("/workspace/pythonfundamentals/Dokumanlar/03_Karar Yapıları.ipynb"))
from datetime import datetime
simdi = datetime.now()
print(simdi.year,simdi.month,simdi.day,simdi.hour+3,simdi.minute)
print(os.getcwd())
print(os.path.join("Ali","Veli")) # Ali/Veli
yol = os.path.join(os.getcwd(),str(simdi.year),str(simdi.month),str(simdi.day),str(simdi.hour))
print(yol) # /workspace/pythonfundamentals/2022
os.makedirs(yol)
