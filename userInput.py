persona={
    "nome": input("inserisci il tuo nome: "),
    "eta": input("inserisci età: ")
}

operazioni = ("aggiungere dati","modificare dati","eliminare dati","leggere")

def start():
    print(operazioni)
    operazione = input("cosa vuoi fare?: ")
    if operazione==operazioni[3]:
        print(persona)
    elif operazione==operazioni[0]:
        chiave=input("quale campo vuoi aggiungere?: ")
        valore=input("inserisci il valore del campo aggiunto: ")
        persona.__setitem__(chiave,valore)
    else:
        pass

start()
print(persona)