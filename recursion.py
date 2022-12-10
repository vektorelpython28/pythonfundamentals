mandef reco(metin):
    if len(metin) == 1:
        print(metin)
    else:
        print(metin)
        reco(metin[1:])
reco("Vektorel")


def faktoriyel(n):
    if n == 1:
        return 1
    else:
        return n*faktoriyel(n-1)

print(faktoriyel(5))