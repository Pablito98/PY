class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
    
      print("ciao sono " + self.nome)
    def respira(self):
       print("sto respirando")

class Studente(Persona):
   def __init__(self, nome, cognome, classe):
      super().__init__(nome, cognome)
      self.classe=classe

   def saluta(self):
       print("ciao sono "+self.nome+" e sono uno studente")

   def daiIlCinque(self):
      print("batti il cinque!")


persona1 = Persona("nicola","verdi")
studente1 = Studente("luigi","rossi","3b")

studente1.saluta()
studente1.daiIlCinque()
#nota che studente1 eredita respira direttamente da persona
studente1.respira()
print(studente1.classe)
