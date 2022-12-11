print("kilolu musun laaa ")
boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
 
endeks  = kilo/(boy*boy)
 
if endeks <=18:
    print("\n zayıf :{}".format(endeks))
elif endeks > 18 and endeks <=25 :
    print("\n kilolu :{}".format(endeks))
elif endeks > 25 and endeks <=30:
    print("\n obez :{}".format(endeks))
elif endeks > 30:
    print("\n ciddi obez :{}".format(endeks))
elif endeks > 100:
    print("\n ölyüorumm bu geceeeee kim gleioo yardimaaa:{}".format(endeks))