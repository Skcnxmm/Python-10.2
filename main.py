def KolikPismen(jake, text):
    pismena=0
    for i in text:
        if i==jake:
            pismena= pismena+1
    return(pismena)
def kolikvsbouboru(jake):
    f = open("data.txt", "r")
    soucet=0
    for a in f:
        cs = KolikPismen("a", a)
        soucet = soucet + cs
    f.close()
    return(soucet)
s=kolikvsbouboru("i")
print(s)

