import numpy 
import random
arreglo = []
for i in range (100):
    numero = random.randint(0,10)
    arreglo.append(numero)
print (arreglo)

for i in range (100):
    numero = random.randint(0,10)
    arreglo.append(numero)
    if  numero %2==0:
        arreglo.append(numero)
print(arreglo)