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

#tuple, ordinata e non modificabile permettono duplicati

listaTuple = ("milano", True, 3,56,"ciao")

(r,t,*u)= listaTuple

#tuple con un solo valore

singolo = ("roma", )


#set, non ordinata e non modificabile non permette duplicati

listaSet= {"milano", "roma", "napoli"}
listaSet2={"venezia", "udine", "napoli"}

#updete e union escludono i duplicati

listaSet.intersection_update(listaSet2) # restituisce solo elementi duplicati
listaSet.symmetric_difference_update(listaSet2)#restituisce tutto tranne i duplicati 

#dictionary, ordinata e modificabile e non permette duplicati

persona = {
    "nome":"luca",
    "cognome": "rossi",
    "eta":25,
    "indirizzo": {
        "citta": "milano",
        "cap": "00000",
        "civico": 34
    }
}

print(persona["indirizzo"]["civico"])



