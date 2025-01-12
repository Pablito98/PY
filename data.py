import datetime
#data corrente
x=datetime.datetime.now()

y=datetime.datetime(2025,1,12)

#formattare la data
print(x.strftime("%d/%m/%Y"))

#altre formattazioni consultare documentazione