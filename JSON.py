#leggere json in py
import json

x = '{"nome":"luca", "cognome":"rossi"}'

y = json.loads(x)

print(y)
print(y["nome"])

#da py a json

z = {
    "nome":"marco",
    "cognome":"verdi",
    "eta":25,
    "isOnline":False,
    "interessi":["calcio","ping pong"]
}
#per convertire in json
p = json.dumps(z)

print(p) 

#per formattare

print(json.dumps(z,indent=3))

#come ordinare le chiavi
print(json.dumps(z,indent=3,sort_keys=True))