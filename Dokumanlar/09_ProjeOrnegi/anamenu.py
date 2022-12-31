import stok
import satis
import sistem
from tools import screentools as sct

def anamenu():
    menu = """
    1- Satış Programı
    2- Stok Programı
    3- # Ayarlar
    4- Çıkış
    """
    anahtar = 1
    while anahtar == 1:
        print(sct.zamandamga())
        islem = input(menu)
        sct.clear()
        if islem == "2":
            if not stok.stokmenu():
                pass 
                # TODO hata ekranına yönlendirme
        if islem == "4":
            anahtar = 0
    else:
        print("Programdan Çıkıldı")


if __name__ == "__main__":
    anamenu()