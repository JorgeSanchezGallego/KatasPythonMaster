#33- Crea una función lambda que sume elementos correspondientes de dos listas dadas.
numeros1 = [1,23,4,5,6,7,8,20]
numeros2 = [3,4,5,6,77,8,9,0,]
suma = list(map(lambda x,y : x+y, numeros1,numeros2))
print(suma)