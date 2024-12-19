x = "ciao"
y= 'paolo'

#con triplo " posso fare stringhe multiriga

z="""
aa
ss"""

#trattare stringhe come array

for carattere in x :
    print(carattere)

#prendere parte di stringa
prova="barattolo"

print(prova[:3])

#modificare stringa con upper() lower() strip() split() e replace()

print(prova.upper())
print(prova.replace("o","a"))

#format() per concatenare stringhe e numeri
prova1 = "ciao sono nato il {}"
print(prova1.format(5))
x = 13
print(prova1.format(x))
prova2 = "sono nato il {}, peso {} e altezza {}"
print(prova2.format(x,3,4))

#escape dei caratteri

prova3= "ciao sono paolo e sono \"simpatico\""