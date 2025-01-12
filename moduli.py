#importare con alias
import mioModulo as em
import platform
import math
#importare solo una parte del modulo
from mioModulo import parteDelModulo

#con funzione
em.saluta("luca")
#con variabile
x=em.persona1["nome"]
em.saluta(x)

print(em.__prova)


#platform è un modulo di py
y = platform.system()
print(y)

#math è un modulo di py
print(math.floor(2.90))
#con la funzione dir(math) vedo tutti i metodi del modulo
print(parteDelModulo)