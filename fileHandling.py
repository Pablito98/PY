#lavorare con i file
# r -Read: apre il file per leggere, errore se non esiste
# a -Append: apre il file per appendere, crea il file se non esiste
# w -Write: apre il file per scrivere, crea se non esiste
# x - Create: crea il file, errore se esiste

#leggere un file intero o una parte
f = open("testo.txt","r")
print(f.read())#all interno delle parentesi posso decidere il numero di caratteri che voglio leggere
f.close()
#f.readline() legge la prima riga e aggiungiendo altri continua a leggere da ultima riga letta

#scrivere in un file (appendere)
#f = open("testo.txt","a")
#f.write("blablabla   ")
#f.close

#sovrascrivere tutto il file
#f = open("testo.txt","w")
#f.write("blablabla   ")
#f.close

#creare un file
#f = open("testo.txt","x")
#f.write("blablabla   ")
#f.close

#eliminare file
import os
#os.remove("testo.txt")

#vedere se esiste il file
#os.path.exists("testo.txt")

#eliminare cartella
#os.rmdir("nome cartella")