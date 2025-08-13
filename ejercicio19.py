#Crea una función lambda que filtre los números impares de una lista dada.
numeros = [1,2,3,4,5,6,7,8,9,10,11]
impares = list(filter(lambda x: x % 2 !=0, numeros))
print(impares)
# filter() recorre la lista y mantiene solo los números que cumplan la condición
# lambda x: x % 2 != 0 → True para números impares