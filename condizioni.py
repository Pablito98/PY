#if
if 5<10:
    print("si è minore")

if 9<3:
    print("si è minore")
else:
    print("no è maggiore")

#operaroti di comparazione
x=9
y=10

print(x==9) #uguale
print(x!=10) #diverso

if x<y and y<20:
    print("condizione verificata")

if x<y or x>y:
    print("condizione verificata")

if not(x<y):
    print("condizione verificata")
