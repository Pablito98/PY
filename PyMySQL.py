# pip install mysql-connector-python

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DOITA11",
    database="pysql" #mi connetto direttamente al db
)

cursor = db.cursor() #lo usiamo come cursore per muoverci nel db

#Creare db
#cursor.execute("CREATE DATABASE pysql")

#Controllare se db esiste
#cursor.execute("SHOW DATABASES")
#for x in cursor:
#    print(x)


#Creare tabella
#cursor.execute("CREATE TABLE clienti (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))")

#Controllare se tabella esiste esiste
#cursor.execute("SHOW TABLES")
#for x in cursor:
#    print(x)
