#list, ordinata e modificabile e permette duplicati

x= ["milano","roma","napoli"]
y=["ciao",34,False]
z=list(("milano","roma","napoli"))

x.append("brescia")
x.insert(2,"monte")
x.extend(y)
x.remove("milano")
x.pop() #rimuove ultimo elem se non diamo index
del x[0]
# x.clear pulisce la lista
print(x)
# [espressione for item in lista if condizione == true]
[print(elemento) for elemento in x if x != None]

x.sort #ordina la lista in ordine alfabetico

#come copiare una list
copia=x.copy()
copia2= list(x)

#tuple, ordinata e non modificabile



#set, non ordinata e non modificabile



#dictionary, ordinata e modificabile e non permette duplicati