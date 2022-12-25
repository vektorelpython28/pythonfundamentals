yol  = "Dokumanlar/08_DosyaIslemleri/yazilan1.csv"
dosya = open(yol,"a+")
#################################
# write
# writelines
#################################
dosya.write("Ali;Veli;1231111111\n")
liste = ["Ali;Veli;1231111111\n",
"Ali;Veli;1232222222\n",
"Ali;Veli;9999999999\n"]
dosya.writelines(liste)
#################################
dosya.write("Birazdan Geçici Kayıt Yapacağım\n")
dosya.write("Ali;Veli;1231111111\n")