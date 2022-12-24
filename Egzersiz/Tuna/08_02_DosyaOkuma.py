def sifreUret(uzunluk=10):
    if uzunluk >= 10:
        sonuc = ""
        liste = [ascii_uppercase,ascii_lowercase,digits,punctuation]
        while len(sonuc) < uzunluk:
            sonuc = ""
            while not sifreKontrol(sonuc):     
                sonuc += rnd.choice(rnd.choice(liste))
        else:
            return sonuc

    else:
        return "10 ya da daha büyük sayı giriniz"
sifreUret(3)