def KolikPismen(jake, text):
    pismena=0
    for i in text:
        if i==jake:
            pismena= pismena+1
    return(pismena)

f = open("data.txt", "r")
soucet=0
for a in f:
    cs = KolikPismen("a", a)
    soucet = soucet + cs


print(soucet)

