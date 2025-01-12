#è un gestore di pacchetti(funzionalità extra)

#pip install camelcase nel terminale per installare

import camelcase
c= camelcase.CamelCase()

frase="ciao sono paolo"

print(c.hump(frase))

#per rimuovere pacchetti  pip unistall nomePacchetto

#per vedere pacc installati pip list