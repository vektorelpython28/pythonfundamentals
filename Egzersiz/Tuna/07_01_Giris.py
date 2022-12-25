
print("kilolu musun laaaaaaaaaaaaaaa ")
boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
 
endeks  = kilo/(boy*boy)
if endeks <112:
    print("\n zargana :{}".format(endeks))
elif endeks < 18 and  12: 
    print("\n zayıf :{}".format(endeks))
elif endeks > 18 and endeks <=25:
    print("\n kilolu :{}".format(endeks))
elif endeks > 25 and endeks <=30:
    print("\n obez :{}".format(endeks))
elif endeks > 30:
    print("\n ciddi obez :{}".format(endeks))