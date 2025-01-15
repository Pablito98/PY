class Persona:
    def __init__(self, nome, cognome, eta, competenze, aspirazioni, statoLavorativo):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        self.__competenze = competenze
        self.__aspirazioni = aspirazioni
        self.__statoLavorativo = statoLavorativo

    #get e set da completare
    def get_nome(self):
        return self.__nome
    
    def get_statoLavorativo(self):
        return self.__statoLavorativo

    def set_statoLavorativo(self, nuovo_stato):
        if nuovo_stato=="Junior Developer":  #ho volutamente limitare il set!
            self.__statoLavorativo = nuovo_stato
        else:
            raise ValueError("Stato lavorativo non valido!")

    def cercaLavoro(self):
        while self.get_statoLavorativo() == "disoccupato":
            x = input("Hai trovato lavoro? (si/no): ").strip().lower()
            if x == "no":
                print("Non arrenderti!")
            elif x == "si":
                self.set_statoLavorativo("Junior Developer")
                print(f"Congratulazioni, {self.get_nome()}! Ecco il tuo stato lavorativo aggiornato:")
                print(self.get_statoLavorativo())
            else:
                print("Risposta non valida. Scrivi 'si' o 'no'.")

paoloM = Persona(
    nome="Paolo Mariano",
    cognome="Fidanza",
    eta=26,
    statoLavorativo="disoccupato",
    competenze={
        "C#": "medio",
        "Java": "medio",
        "Python": "in corso"
    },
    aspirazioni=[
        "Trovare lavoro",
        "Conoscere più tecnologie possibili",
        "Dimostrare il mio valore"
    ]
)

paoloM.cercaLavoro()


