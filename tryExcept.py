#utilizziamo per evitare di bloccare il programma
try:
    print(x)
except NameError:
    print("c'è stato un errore")
except:
    print("c'è stato un errore non conosciuto")
finally:
    print("a prescindere da tutto")


y= -1

if y<0:
    raise Exception("numero minore di zero")
