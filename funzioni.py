def faiLaPasta(tipoPasta):
    if tipoPasta=="":
     print("sto cucinando" )
    else:
       print("sto cucinando "+ tipoPasta)
Pasta=""
faiLaPasta(Pasta)
# quando ci sono piu argomenti non conosciuti
def cucina(*opzioni):
   print("sto cucinando")
   print("metti "+ opzioni[0])
   if opzioni[1]:
      print("ho aggiunto il formaggio")

cucina("spaghetti", True)

#parametri di default
#non assegnando parametri passera rigatoni, in questo caso assegno penne rigate e quindi rigatoni non passa
def cucina1(tipoPasta="rigatoni"):
   print("sto cucinando " + tipoPasta)

cucina1("penne rigate")

#return di valori

def calcolaSomma(num1 ,num2):
   somma = num1+num2
   return somma
x = calcolaSomma(2, 20)
print(x)
print(calcolaSomma(3,4))