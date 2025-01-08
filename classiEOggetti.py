class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
    
      print("ciao sono " + self.nome)
        

persona1=Persona("luca","rossi")
persona2=Persona("marco","verdi")

print(persona1.cognome)
persona1.saluta()
#modificare
persona2.nome = "maria"
#eliminare
del persona2.cognome
del persona1
persona2.saluta()